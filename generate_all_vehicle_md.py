#!/usr/bin/env python3
"""C 阶段：为全部 315 款车型生成 markdown（含多国落地成本自动计算）。

数据源：
- data/vehicles.json : 315 款车型基础数据（价格/续航/电池/尺寸等）
- data/enriched/*.json : 10 标杆车型的落地成本+描述（优先复用描述）
- data/landed-cost-params.json : 多国落地成本参数（含 markets 字段）

落地成本公式：
  landed = base * (1+std_duty) * (1+cvd) * (1+vat) + freight + clearance + cert + reg + inland
"""
import json, os, glob

VEHICLES = "data/vehicles.json"
ENRICHED = "data/enriched"
PARAMS = "data/landed-cost-params.json"
OUT = "output/vehicles-md"
os.makedirs(OUT, exist_ok=True)

vehicles = json.load(open(VEHICLES))
params = json.load(open(PARAMS))

# 车型 -> 本地图片映射
VEH_IMG = "data/vehicle_images.json"
veh_img_map = {}
if os.path.exists(VEH_IMG):
    veh_img_map = json.load(open(VEH_IMG))

# 品牌 -> 反补贴税率（cvd）
cvd_rates = params["countervailing_duty"]
DEFAULT_CVD = cvd_rates["default"]  # 18.8%

def get_cvd(brand):
    """根据品牌返回反补贴税率。byd=17%, geely/zeekr=18.8%, saic=35.3%, 其他 default。"""
    if not brand:
        return DEFAULT_CVD
    b = brand.lower()
    if b == "byd":
        return cvd_rates["byd"]
    if b in ("geely", "geely-galaxy", "zeekr", "lynk-co"):
        return cvd_rates["geely"]
    if b == "saic" or b in ("mg", "roewe", "maxus", "wuling", "bao jun"):
        return cvd_rates["saic"]
    return DEFAULT_CVD

# 已加载的 enriched 数据（10 标杆）
enriched_map = {}
for fn in glob.glob(f"{ENRICHED}/*.json"):
    d = json.load(open(fn))
    enriched_map[d["slug"]] = d

def slug_to_name(slug, brand):
    """从 slug 和 brand 推演显示名。"""
    if not slug:
        return brand or "EV"
    rest = slug
    if brand and slug.startswith(brand):
        rest = slug[len(brand):].lstrip("-")
    if not rest:
        rest = "series"
    name_parts = []
    for token in rest.split("-"):
        if token.isdigit():
            name_parts.append(token)
        elif token.lower() in ("e", "es", "et", "u", "v", "gt", "ev", "pro", "max", "plus", "mini", "standard", "long", "range", "performance", "ultra"):
            name_parts.append(token.upper())
        elif token.lower() == "atto":
            name_parts.append("Atto")
        elif len(token) <= 3:
            name_parts.append(token.upper())
        else:
            name_parts.append(token.title())
    display = " ".join(name_parts)
    brand_display = brand.replace("-", " ").title() if brand else ""
    return f"{brand_display} {display}".strip()

def calc_landed_market(base_price, brand, mkey, mdata):
    """用指定市场参数计算落地成本。"""
    std = mdata["standard_duty_rate"]
    cvd = get_cvd(brand) if mdata.get("countervailing_duty") else 0.0
    vat = mdata["vat_rate"]
    freight = mdata["freight_roro_usd"]
    cert = mdata["certification_usd"]
    reg = mdata["registration_fee_usd"]
    clearance = params["other_costs"]["customs_clearance_usd"]
    inland = params["other_costs"]["inland_transport_usd"]

    duty = base_price * std
    cvd_amt = base_price * (1 + std) * cvd
    vat_amt = base_price * (1 + std) * (1 + cvd) * vat
    total = base_price + duty + cvd_amt + vat_amt + freight + clearance + cert + reg + inland
    premium = (total - base_price) / base_price * 100

    return {
        "market": mdata["country"],
        "market_key": mkey,
        "region": mdata.get("region", ""),
        "standard_duty_rate": round(std, 3),
        "countervailing_duty_rate": round(cvd, 3),
        "vat_rate": vat,
        "total_landed_usd": round(total, 2),
        "premium_pct": round(premium, 1),
    }

def calc_landed_germany(base_price, brand):
    """计算德国为主市场（供 detailed breakdown）。"""
    mkts = params.get("markets", {})
    if "germany" in mkts:
        m = calc_landed_market(base_price, brand, "germany", mkts["germany"])
        # 附带 breakdown
        std = m["standard_duty_rate"]
        cvd = m["countervailing_duty_rate"]
        vat = m["vat_rate"]
        freight = mkts["germany"]["freight_roro_usd"]
        cert = mkts["germany"]["certification_usd"]
        reg = mkts["germany"]["registration_fee_usd"]
        clearance = params["other_costs"]["customs_clearance_usd"]
        inland = params["other_costs"]["inland_transport_usd"]
        m["breakdown"] = {
            "duty_cif_usd": round(base_price * std, 2),
            "countervailing_duty_usd": round(base_price * (1 + std) * cvd, 2),
            "vat_usd": round(base_price * (1 + std) * (1 + cvd) * vat, 2),
            "freight_roro_usd": freight,
            "customs_clearance_usd": clearance,
            "certification_usd": cert,
            "registration_usd": reg,
            "inland_transport_usd": inland,
        }
        return m
    return {}

def gen_description(slug, brand, base, vtype):
    """生成模板化描述。"""
    bname = brand.replace("-", " ").title()
    parts = [f"{slug_to_name(slug, brand)} is a {vtype.lower()} from {bname},"]
    if base.get("range_cltc"):
        parts.append(f"offering {base['range_cltc']} km of CLTC range")
    if base.get("battery_kwh"):
        parts.append(f"a {base['battery_kwh']} kWh battery")
    if base.get("motor_power"):
        parts.append(f"and {base['motor_power']} kW of motor power")
    desc = " ".join(parts) + "."
    desc += " Full landed-cost breakdown across key export markets included for B2B import planning."
    return desc

count = 0
skipped = []
for slug in sorted(vehicles.keys()):
    base = vehicles[slug]
    brand = base.get("brand") or None
    if brand is None and slug.startswith("jac-refine"):
        brand = "jac-refine"
    if not brand:
        skipped.append((slug, "no brand"))
        continue

    enriched = enriched_map.get(slug)
    if enriched:
        name = enriched.get("name") or slug_to_name(slug, brand)
        desc = enriched.get("description_en", "")
    else:
        name = slug_to_name(slug, brand)
        desc = gen_description(slug, brand, base, base.get("type", ""))

    vtype = base.get("type", "")
    price = float(base.get("price_usd", 0) or 0)

    def num(v):
        try:
            return float(v)
        except (TypeError, ValueError):
            return None

    # 多国落地成本
    multi_lc = []
    germany_lc = {}
    if price > 0:
        mkts = params.get("markets", {})
        for mkey in ["germany", "united_kingdom", "netherlands", "france", "united_arab_emirates", "saudi_arabia", "australia"]:
            if mkey in mkts:
                r = calc_landed_market(price, brand, mkey, mkts[mkey])
                multi_lc.append(r)
                if mkey == "germany":
                    germany_lc = calc_landed_germany(price, brand)

    fm = {
        "title": name,
        "description": (desc or "")[:160],
        "slug": slug,
        "brand": brand,
        "type": vtype or "",
        "powertrain": base.get("powertrain", "BEV"),
        "price_usd": price,
        "currency": "USD",
        "range_cltc_km": int(num(base.get("range_cltc"))) if num(base.get("range_cltc")) else None,
        "battery_kwh": num(base.get("battery_kwh")),
        "motor_power_kw": int(num(base.get("motor_power"))) if num(base.get("motor_power")) else None,
        "torque_nm": int(num(base.get("torque"))) if num(base.get("torque")) else None,
        "accel_0_100_s": num(base.get("accel")),
        "top_speed_kmh": int(num(base.get("top_speed"))) if num(base.get("top_speed")) else None,
        "length_mm": int(num(base.get("length"))) if num(base.get("length")) else None,
        "width_mm": int(num(base.get("width"))) if num(base.get("width")) else None,
        "height_mm": int(num(base.get("height"))) if num(base.get("height")) else None,
        "wheelbase_mm": int(num(base.get("wheelbase"))) if num(base.get("wheelbase")) else None,
        "weight_kg": int(num(base.get("weight"))) if num(base.get("weight")) else None,
        "efficiency_kwh_100km": num(base.get("efficiency")),
        "fast_charge": base.get("fast_charge", "-").replace("\\-", "-"),
        "landed_cost": germany_lc,
        "landed_cost_markets": multi_lc,
        "publishedDate": "2026-09-05",
        "author": "Wei Wang",
        "tags": [brand, vtype or "EV", "chinese-ev", "export"],
    }

    imgname = veh_img_map.get(slug)
    if imgname:
        fm["image"] = f"/images/vehicles/{imgname}"

    # 生成 markdown body
    body = f"# {name}\n\n{name} (starting at ${int(price):,}) is a {fm['type']} from {brand.replace('-', ' ').upper()}.\n\n"
    if fm['range_cltc_km'] is not None:
        body += f"- **Range**: {fm['range_cltc_km']} km (CLTC)\n"
    if fm['battery_kwh'] is not None:
        body += f"- **Battery**: {fm['battery_kwh']} kWh\n"
    if fm['motor_power_kw'] is not None:
        body += f"- **Motor power**: {fm['motor_power_kw']} kW\n"
    if fm['accel_0_100_s'] is not None:
        body += f"- **0-100 km/h**: {fm['accel_0_100_s']} s\n"

    body += f"\n## Overview\n\n{desc}\n\n## Landed Cost by Market\n\nEstimated landed cost to import this vehicle into key export markets, including import duty, countervailing duty, VAT/GST, freight, and compliance costs.\n\n| Destination | Region | Total landed (USD) | Premium |\n|---|---|---|---|\n"
    for m in multi_lc:
        body += f"| {m['market']} | {m.get('region','')} | ${int(m['total_landed_usd']):,} | +{m['premium_pct']}% |\n"

    # 详细 breakdown（德国）
    bd = germany_lc.get("breakdown", {})
    if bd:
        body += f"\n## Detailed Breakdown — Germany\n\n| Cost item | Amount (USD) |\n|---|---|\n"
        body += f"| Base price | ${int(price):,} |\n"
        body += f"| Standard import duty ({int(germany_lc.get('standard_duty_rate', 0.1)*100)}%) | ${int(bd.get('duty_cif_usd', 0)):,} |\n"
        body += f"| Countervailing duty ({int(germany_lc.get('countervailing_duty_rate', 0)*100)}%) | ${int(bd.get('countervailing_duty_usd', 0)):,} |\n"
        body += f"| VAT ({int(germany_lc.get('vat_rate', 0.19)*100)}%) | ${int(bd.get('vat_usd', 0)):,} |\n"
        body += f"| RoRo freight | ${int(bd.get('freight_roro_usd', 0)):,} |\n"
        body += f"| Customs clearance | ${int(bd.get('customs_clearance_usd', 0)):,} |\n"
        body += f"| Certification | ${int(bd.get('certification_usd', 0)):,} |\n"
        body += f"| Registration | ${int(bd.get('registration_usd', 0)):,} |\n"
        body += f"| Inland transport | ${int(bd.get('inland_transport_usd', 0)):,} |\n"
        body += f"| **Total landed** | **${int(germany_lc.get('total_landed_usd', 0)):,}** |\n\n"
        body += f"**Premium over base price**: +{germany_lc.get('premium_pct', 0)}%\n"

    outfile = os.path.join(OUT, f"{slug}.md")
    with open(outfile, "w") as f:
        f.write("---\n")
        for k, v in fm.items():
            if v is None:
                continue
            if isinstance(v, (dict, list)):
                f.write(f"{k}: {json.dumps(v)}\n")
            elif isinstance(v, str):
                f.write(f"{k}: {json.dumps(v, ensure_ascii=False)}\n")
            else:
                f.write(f"{k}: {v}\n")
        f.write("---\n\n")
        f.write(body)
    count += 1

print(f"Total generated: {count} markdown files -> {OUT}")
if skipped:
    print(f"Skipped {len(skipped)}: {skipped}")
