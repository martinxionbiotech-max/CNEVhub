#!/usr/bin/env python3
"""EV Hub 车辆数据 QA 门禁（P0 数据完整性 + P1 结构化检查）。

只读检查，报告问题，不自动修复（例外：由人工任务书明确指定的单点修复另行执行）。
数据源：
- src/content/vehicles/*.md（frontmatter）
- src/data/tariffs.json（市场关税/VAT 参考、品牌 CVD 组）
- src/content/brands/*.md（品牌页文件存在性）

检查项：
  PRICE QA        price_usd > 0（区分负价/零价/缺失）
  MATH QA         landed_cost.total_landed_usd ≈ price_usd + sum(breakdown)，容差 ±1 USD
  CONSISTENCY QA  landed_cost 与 landed_cost_markets 主市场条目对齐（±0.01）
  TARIFF QA       EU 市场 BEV CVD 匹配品牌组（BYD 0.17 / Geely 0.188 / SAIC 0.353 / 其他 0.207）；
                  非 BEV（EREV/PHEV/HEV/ICE）与全部非 EU 市场 CVD = 0（反补贴税仅适用于 BEV 出口欧盟）
  VAT QA          landed_cost_markets 各市场 vat_rate 与 tariffs.json 参考一致
  DATE QA         data_updated 距今 ≤ 90 天
  DUPLICATE QA    slug 全站唯一（重复 slug / 文件名与 slug 不一致）
  RELATION QA     vehicle.brand ↔ src/content/brands/{brand}.md 双向存在（品牌无车型 / 车型无品牌页）
  ENUM QA         powertrain、type 受控词表校验
  RANGE QA        range_cltc_km 存在时应在 (0, 2000] 区间
  SOURCE QA       缺失 data_source 字段的车辆

用法：
  python3 scripts/qa_data.py                    # 完整报告（stdout）
  python3 scripts/qa_data.py --summary          # 仅摘要
  python3 scripts/qa_data.py --report PATH      # 完整报告同时写入 PATH（Markdown）
退出码：0 = 通过（或仅警告）；1 = 存在 FAIL 级问题。
"""
import glob
import json
import os
import re
import sys
from datetime import date, datetime, timedelta

VEHICLES = "src/content/vehicles"
BRANDS = "src/content/brands"
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

# 受控词表（与 scripts/quality-gate.mjs 保持一致）
ALLOWED_POWERTRAINS = {"BEV", "PHEV", "EREV", "HEV", "ICE", "FCEV", "Unknown"}
ALLOWED_TYPES = {
    "Sedan", "Hatchback", "SUV", "Crossover", "MPV", "Wagon", "Pickup", "Van",
    "Coupe", "Convertible", "Sports Car", "Other", "Unknown",
}

REPORT_ORDER = [
    "PRICE QA", "MATH QA", "CONSISTENCY QA", "TARIFF QA", "VAT QA", "DATE QA",
    "DUPLICATE QA", "RELATION QA", "ENUM QA", "RANGE QA", "SOURCE QA",
]


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


def format_report(stats, issues, today) -> str:
    lines = []
    total_issues = sum(len(v) for v in issues.values())
    fails = {k: v for k, v in issues.items() if v}
    lines.append("=" * 72)
    lines.append("EV HUB DATA QA REPORT")
    lines.append(f"  扫描文件: {stats['files']}  |  检查市场条目: {stats['markets_checked']}  |  日期: {today}")
    lines.append("=" * 72)
    for name in REPORT_ORDER:
        items = issues[name]
        status = "PASS" if not items else f"FAIL ({len(items)})"
        lines.append(f"\n[{name}] {status}")
        for it in items[:20]:
            lines.append(f"  - {it}")
        if len(items) > 20:
            lines.append(f"  ... 共 {len(items)} 条，仅显示前 20")
    lines.append("\n" + "=" * 72)
    if total_issues == 0:
        lines.append("结论: 全部检查通过 ✅")
    else:
        lines.append(f"结论: 发现 {total_issues} 个问题（按类分布: "
                     + ", ".join(f"{k}×{len(v)}" for k, v in fails.items()) + "）")
    lines.append("=" * 72)
    return "\n".join(lines)


def markdown_report(stats, issues, today) -> str:
    lines = []
    lines.append("# EV Hub 数据 QA 报告")
    lines.append("")
    lines.append(f"> 生成日期：{today} ｜ 工具：`python3 scripts/qa_data.py`")
    lines.append(f"> 扫描车辆文件：{stats['files']} ｜ 检查市场条目：{stats['markets_checked']}")
    lines.append("> 本工具只读检查、不自动修复；发现问题由人工任务书决策处理。")
    lines.append("")
    for name in REPORT_ORDER:
        items = issues[name]
        lines.append(f"## {name}")
        lines.append("")
        if not items:
            lines.append("✅ 通过")
        else:
            lines.append(f"❌ {len(items)} 个问题：")
            lines.append("")
            for it in items:
                lines.append(f"- {it}")
        lines.append("")
    total_issues = sum(len(v) for v in issues.values())
    lines.append("## 汇总")
    lines.append("")
    if total_issues == 0:
        lines.append("全部检查通过 ✅")
    else:
        for k, v in issues.items():
            if v:
                lines.append(f"- {k}：{len(v)} 个问题")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    summary_only = "--summary" in sys.argv
    report_path = None
    if "--report" in sys.argv:
        i = sys.argv.index("--report")
        if i + 1 < len(sys.argv):
            report_path = sys.argv[i + 1]
    today = date.today()

    tariffs = json.load(open(TARIFFS))
    markets_ref = tariffs.get("markets", {})

    issues = {k: [] for k in REPORT_ORDER}
    stats = {"files": 0, "markets_checked": 0}

    # 品牌页文件集合（RELATION QA 用）
    brand_files = {f[:-3] for f in os.listdir(BRANDS) if f.endswith(".md")}

    # 第一遍：收集 slug / brand 全量（DUPLICATE / RELATION QA 需要跨文件）
    file_meta = {}  # filename -> (slug, brand)
    for path in sorted(glob.glob(f"{VEHICLES}/*.md")):
        text = open(path, encoding="utf-8").read()
        fname = path.rsplit("/", 1)[-1][:-3]
        slug_raw = parse_frontmatter_field(text, "slug")
        slug = slug_raw.strip('"') if slug_raw else None
        brand_raw = parse_frontmatter_field(text, "brand")
        brand = brand_raw.strip('"') if brand_raw else None
        file_meta[fname] = (slug, brand)

    # DUPLICATE QA：slug 全站唯一 + 与文件名一致
    slug_to_files = {}
    for fname, (slug, _) in file_meta.items():
        if slug is None:
            issues["DUPLICATE QA"].append(f"{fname}: 缺少 slug 字段")
            continue
        slug_to_files.setdefault(slug, []).append(fname)
        if slug != fname:
            issues["DUPLICATE QA"].append(f"{fname}: 文件名与 slug 不一致 ({slug})")
    for slug, files in slug_to_files.items():
        if len(files) > 1:
            issues["DUPLICATE QA"].append(f"{slug}: 重复 slug，出现于 {', '.join(sorted(files))}")

    # RELATION QA：双向品牌 ↔ 品牌页
    vehicle_brands = {brand for _, (_, brand) in file_meta.items() if brand}
    for fname, (_, brand) in file_meta.items():
        if brand is None:
            issues["RELATION QA"].append(f"{fname}: 缺少 brand 字段")
        elif brand.lower() not in brand_files:
            issues["RELATION QA"].append(f"{fname}: brand={brand} 无品牌页文件 (src/content/brands/{brand}.md)")
    for bf in sorted(brand_files - {b.lower() for b in vehicle_brands}):
        issues["RELATION QA"].append(f"{bf}: 品牌页文件存在但无任何车型引用")

    for path in sorted(glob.glob(f"{VEHICLES}/*.md")):
        text = open(path, encoding="utf-8").read()
        fname = path.rsplit("/", 1)[-1][:-3]
        slug = fname
        stats["files"] += 1

        brand_raw = parse_frontmatter_field(text, "brand")
        brand = brand_raw.strip('"') if brand_raw else None
        powertrain = (parse_frontmatter_field(text, "powertrain") or "Unknown").strip('"')
        body_type = (parse_frontmatter_field(text, "type") or "Unknown").strip('"')
        price_raw = parse_frontmatter_field(text, "price_usd")
        range_raw = parse_frontmatter_field(text, "range_cltc_km")
        updated_raw = parse_frontmatter_field(text, "data_updated")
        if updated_raw:
            updated_raw = updated_raw.strip('"')
        data_source = parse_frontmatter_field(text, "data_source")

        lc = parse_json_field(text, "landed_cost")
        markets = parse_json_field(text, "landed_cost_markets")

        # ENUM QA
        if powertrain not in ALLOWED_POWERTRAINS:
            issues["ENUM QA"].append(f"{slug}: powertrain={powertrain!r} 不在受控词表 {sorted(ALLOWED_POWERTRAINS)}")
        if body_type not in ALLOWED_TYPES:
            issues["ENUM QA"].append(f"{slug}: type={body_type!r} 不在受控词表 {sorted(ALLOWED_TYPES)}")

        # PRICE QA（区分负价/零价/缺失）
        try:
            price = float(price_raw)
        except (TypeError, ValueError):
            issues["PRICE QA"].append(f"{slug}: price_usd 缺失或非数值 ({price_raw!r})")
            price = None
        else:
            if price < 0:
                issues["PRICE QA"].append(f"{slug}: price_usd={price} 为负价")
            elif price == 0:
                issues["PRICE QA"].append(f"{slug}: price_usd=0 为零价")

        # RANGE QA：range_cltc_km 存在时应在 (0, 2000]
        if range_raw is not None and range_raw.strip() not in ("null", ""):
            try:
                rng = float(range_raw)
            except ValueError:
                issues["RANGE QA"].append(f"{slug}: range_cltc_km 无法解析 ({range_raw!r})")
            else:
                if rng <= 0 or rng > 2000:
                    issues["RANGE QA"].append(f"{slug}: range_cltc_km={rng} 超出 (0, 2000]")

        # SOURCE QA
        if not data_source or not data_source.strip('"').strip():
            issues["SOURCE QA"].append(f"{slug}: data_source 缺失")

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

    if report_path:
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(markdown_report(stats, issues, today) + "\n")
        print(f"→ 报告已写入 {report_path}")

    if summary_only:
        print(f"files={stats['files']} markets={stats['markets_checked']} "
              + " | ".join(f"{k}={len(v)}" for k, v in issues.items())
              + f" | total_issues={total_issues}")
    else:
        print(format_report(stats, issues, today))

    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
