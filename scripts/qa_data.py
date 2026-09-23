#!/usr/bin/env python3
"""EV Hub 车辆数据 QA 门禁（P0 数据完整性）。

只读检查，报告问题，不自动修复。数据源：
- src/content/vehicles/*.md（frontmatter）
- src/data/tariffs.json（市场关税/VAT 参考、品牌 CVD 组）

检查项：
  PRICE QA        price_usd > 0
  MATH QA         landed_cost.total_landed_usd ≈ price_usd + sum(breakdown)，容差 ±1 USD
  CONSISTENCY QA  landed_cost 与 landed_cost_markets 主市场条目对齐（±0.01）
  TARIFF QA       EU 市场 BEV CVD 匹配品牌组（BYD 0.17 / Geely 0.188 / SAIC 0.353 / 其他 0.207）；
                  非 BEV（EREV/PHEV/HEV/ICE）与全部非 EU 市场 CVD = 0（反补贴税仅适用于 BEV 出口欧盟）
  VAT QA          landed_cost_markets 各市场 vat_rate 与 tariffs.json 参考一致
  DATE QA         data_updated 距今 ≤ 90 天

用法：
  python3 scripts/qa_data.py            # 完整报告
  python3 scripts/qa_data.py --summary  # 仅摘要
退出码：0 = 通过（或仅警告）；1 = 存在 FAIL 级问题。
"""
import glob
import json
import re
import sys
from datetime import date, datetime, timedelta

VEHICLES = "src/content/vehicles"
TARIFFS = "src/data/tariffs.json"

# 品牌 → EU 反补贴税组（与 src/data/tariffs.json brand_cvd 保持一致）
BRAND_GROUPS = {
    "byd": 0.17, "denza": 0.17, "yangwang": 0.17, "fangchengbao": 0.17,
    "geely": 0.188, "geely-galaxy": 0.188, "zeekr": 0.188, "lynk-co": 0.188,
    "livan": 0.188, "geometry": 0.188,
    "mg": 0.353, "maxus": 0.353, "roewe": 0.353, "saic": 0.353,
    "wuling": 0.353, "baojun": 0.353, "im": 0.353,
}
DEFAULT_CVD = 0.207  # 其他合作方
CVD_TOLERANCE = 0.001
DATE_TOLERANCE_DAYS = 90


def cvd_for_brand(brand: str) -> float:
    return BRAND_GROUPS.get((brand or "").lower(), DEFAULT_CVD)


def parse_frontmatter_field(text: str, name: str):
    m = re.search(rf"^{name}:\s*([^\n]+)\s*$", text, re.M)
    return m.group(1) if m else None


def parse_json_field(text: str, name: str):
    m = re.search(rf"^{name}:\s*(\{{.*\}}|\[.*\])\s*$", text, re.M)
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except json.JSONDecodeError:
        return None


def main() -> int:
    summary_only = "--summary" in sys.argv
    today = date.today()

    tariffs = json.load(open(TARIFFS))
    markets_ref = tariffs.get("markets", {})

    issues = {"PRICE QA": [], "MATH QA": [], "CONSISTENCY QA": [],
              "TARIFF QA": [], "VAT QA": [], "DATE QA": []}
    stats = {"files": 0, "markets_checked": 0}

    for path in sorted(glob.glob(f"{VEHICLES}/*.md")):
        text = open(path, encoding="utf-8").read()
        slug = path.rsplit("/", 1)[-1][:-3]
        stats["files"] += 1

        brand = parse_frontmatter_field(text, "brand")
        if brand:
            brand = brand.strip('"')
        powertrain = (parse_frontmatter_field(text, "powertrain") or "Unknown").strip('"')
        price_raw = parse_frontmatter_field(text, "price_usd")
        updated_raw = parse_frontmatter_field(text, "data_updated")
        if updated_raw:
            updated_raw = updated_raw.strip('"')

        lc = parse_json_field(text, "landed_cost")
        markets = parse_json_field(text, "landed_cost_markets")

        # PRICE QA
        try:
            price = float(price_raw)
        except (TypeError, ValueError):
            issues["PRICE QA"].append(f"{slug}: price_usd 缺失或非数值 ({price_raw!r})")
            price = None
        else:
            if price <= 0:
                issues["PRICE QA"].append(f"{slug}: price_usd={price} ≤ 0")

        # DATE QA
        if not updated_raw:
            issues["DATE QA"].append(f"{slug}: data_updated 缺失")
        else:
            try:
                d = datetime.strptime(updated_raw, "%Y-%m-%d").date()
            except ValueError:
                issues["DATE QA"].append(f"{slug}: data_updated 无法解析 ({updated_raw!r})")
            else:
                age = (today - d).days
                if age > DATE_TOLERANCE_DAYS:
                    issues["DATE QA"].append(f"{slug}: data_updated={updated_raw} 距今 {age} 天 (> {DATE_TOLERANCE_DAYS})")
                if age < 0:
                    issues["DATE QA"].append(f"{slug}: data_updated={updated_raw} 在未来")

        # MATH / CONSISTENCY / TARIFF QA（依赖 landed_cost 与 markets）
        if not isinstance(lc, dict) or not isinstance(markets, list):
            if not isinstance(lc, dict):
                issues["MATH QA"].append(f"{slug}: landed_cost 缺失或非法")
            if not isinstance(markets, list):
                issues["CONSISTENCY QA"].append(f"{slug}: landed_cost_markets 缺失或非法")
            continue

        # MATH QA
        breakdown = lc.get("breakdown") or {}
        comps = ["duty_cif_usd", "countervailing_duty_usd", "vat_usd",
                 "freight_roro_usd", "customs_clearance_usd", "certification_usd",
                 "registration_usd", "inland_transport_usd"]
        comp_sum = sum(breakdown.get(c, 0) or 0 for c in comps)
        total = lc.get("total_landed_usd")
        if total is None or price is None:
            issues["MATH QA"].append(f"{slug}: landed_cost.total_landed_usd 或 price_usd 缺失，跳过")
        else:
            expected = price + comp_sum
            if abs(expected - total) > 1:
                issues["MATH QA"].append(
                    f"{slug}: landed={total:.2f} vs base+sum(breakdown)={expected:.2f} "
                    f"(差 {total - expected:+.2f}，容差 ±1)")

        # CONSISTENCY QA（主市场 = landed_cost.market）
        primary_market = lc.get("market")
        primary = next((m for m in markets
                        if isinstance(m, dict) and m.get("market") == primary_market), None)
        if primary is None:
            issues["CONSISTENCY QA"].append(
                f"{slug}: landed_cost_markets 缺少主市场条目 {primary_market!r}")
        elif total is not None:
            mv = primary.get("total_landed_usd")
            if mv is None or abs(mv - total) > 0.01:
                issues["CONSISTENCY QA"].append(
                    f"{slug}: {primary_market} landed_cost={total} vs markets={mv} 漂移 > ±0.01")

        # TARIFF / VAT QA（遍历全部市场）
        for m in markets:
            if not isinstance(m, dict):
                continue
            stats["markets_checked"] += 1
            market = m.get("market") or "?"
            region = m.get("region") or "?"
            key = m.get("market_key") or "?"
            cvd = m.get("countervailing_duty_rate")
            if cvd is None:
                issues["TARIFF QA"].append(f"{slug}: {market} countervailing_duty_rate 缺失")
                continue
            is_bev = (powertrain == "BEV")
            if region == "EU" and is_bev:
                expected_cvd = cvd_for_brand(brand)
                if abs(cvd - expected_cvd) > CVD_TOLERANCE:
                    issues["TARIFF QA"].append(
                        f"{slug}: {market} (EU/BEV) cvd={cvd} ≠ 品牌组 {brand} 期望 {expected_cvd}")
            else:
                # 非 EU 市场或非 BEV：CVD 应为 0
                if abs(cvd) > CVD_TOLERANCE:
                    issues["TARIFF QA"].append(
                        f"{slug}: {market} ({region}/{powertrain}) cvd={cvd} ≠ 0")

            # VAT QA
            vat = m.get("vat_rate")
            ref = markets_ref.get(key)
            if ref is None:
                issues["VAT QA"].append(f"{slug}: {market} market_key={key!r} 不在 tariffs.json")
            elif vat is None or abs(vat - ref["vat_rate"]) > 0.001:
                issues["VAT QA"].append(
                    f"{slug}: {market} vat={vat} ≠ 参考 {ref['vat_rate']} ({ref.get('label')})")

    # ---- 报告 ----
    total_issues = sum(len(v) for v in issues.values())
    fails = {k: v for k, v in issues.items() if v}

    if not summary_only:
        print("=" * 72)
        print("EV HUB DATA QA REPORT")
        print(f"  扫描文件: {stats['files']}  |  检查市场条目: {stats['markets_checked']}  |  日期: {today}")
        print("=" * 72)
        for name in ["PRICE QA", "MATH QA", "CONSISTENCY QA", "TARIFF QA", "VAT QA", "DATE QA"]:
            items = issues[name]
            status = "PASS" if not items else f"FAIL ({len(items)})"
            print(f"\n[{name}] {status}")
            for it in items[:20]:
                print(f"  - {it}")
            if len(items) > 20:
                print(f"  ... 共 {len(items)} 条，仅显示前 20")
        print("\n" + "=" * 72)
        if total_issues == 0:
            print("结论: 全部检查通过 ✅")
        else:
            print(f"结论: 发现 {total_issues} 个问题（按类分布: "
                  + ", ".join(f"{k}×{len(v)}" for k, v in fails.items()) + "）")
        print("=" * 72)
    else:
        print(f"files={stats['files']} markets={stats['markets_checked']} "
              + " | ".join(f"{k}={len(v)}" for k, v in issues.items())
              + f" | total_issues={total_issues}")

    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
