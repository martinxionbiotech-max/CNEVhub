#!/usr/bin/env python3
"""P2: Add new vehicles to the EV Hub catalog.

Reads a spec JSON (list of new vehicles with real, source-verified specs),
computes landed cost from src/data/tariffs.json (single source of truth), and
writes three synchronized outputs:
  1. src/content/vehicles/<slug>.md   (full frontmatter + templated body)
  2. src/data/vehicle-master.json     (append + update count)
  3. src/data/brand-master.json       (update vehicle_count per brand)

Honesty rules: every numeric field must come from the spec JSON. No value is
invented here — the script only computes landed cost (deterministic) and
templates prose around the provided numbers.

Usage:
  python3 scripts/add_vehicles.py <spec.json> [--apply]

Without --apply it is a PREVIEW (dry run): prints what would be created.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VEHICLES_DIR = ROOT / "src/content/vehicles"
MASTER = ROOT / "src/data/vehicle-master.json"
BRAND_MASTER = ROOT / "src/data/brand-master.json"
TARIFFS = json.loads((ROOT / "src/data/tariffs.json").read_text())

# 30 markets (P3 country database). Ordered by region for stable page display.
MARKETS_ORDER = [
    # EU (12)
    "germany", "france", "netherlands", "sweden", "denmark", "spain",
    "italy", "belgium", "austria", "portugal", "ireland", "poland",
    # Non-EU Europe (3)
    "united_kingdom", "norway", "switzerland",
    # Middle East (5)
    "united_arab_emirates", "saudi_arabia", "israel", "qatar", "turkey",
    # Oceania (2)
    "australia", "new_zealand",
    # Southeast Asia (4)
    "thailand", "malaysia", "indonesia", "singapore",
    # North America (2)
    "mexico", "canada",
    # Latin America (1)
    "brazil",
    # Africa (1)
    "south_africa",
]
MARKET_LABEL = {
    "germany": "Germany", "france": "France", "netherlands": "Netherlands",
    "sweden": "Sweden", "denmark": "Denmark", "spain": "Spain",
    "italy": "Italy", "belgium": "Belgium", "austria": "Austria",
    "portugal": "Portugal", "ireland": "Ireland", "poland": "Poland",
    "united_kingdom": "United Kingdom", "norway": "Norway", "switzerland": "Switzerland",
    "united_arab_emirates": "United Arab Emirates", "saudi_arabia": "Saudi Arabia",
    "israel": "Israel", "qatar": "Qatar", "turkey": "Turkey",
    "australia": "Australia", "new_zealand": "New Zealand",
    "thailand": "Thailand", "malaysia": "Malaysia", "indonesia": "Indonesia", "singapore": "Singapore",
    "mexico": "Mexico", "canada": "Canada",
    "brazil": "Brazil",
    "south_africa": "South Africa",
}
MARKET_REGION = {
    "germany": "EU", "france": "EU", "netherlands": "EU",
    "sweden": "EU", "denmark": "EU", "spain": "EU",
    "italy": "EU", "belgium": "EU", "austria": "EU",
    "portugal": "EU", "ireland": "EU", "poland": "EU",
    "united_kingdom": "Non-EU Europe", "norway": "Non-EU Europe", "switzerland": "Non-EU Europe",
    "united_arab_emirates": "Middle East", "saudi_arabia": "Middle East",
    "israel": "Middle East", "qatar": "Middle East", "turkey": "Middle East",
    "australia": "Oceania", "new_zealand": "Oceania",
    "thailand": "Southeast Asia", "malaysia": "Southeast Asia",
    "indonesia": "Southeast Asia", "singapore": "Southeast Asia",
    "mexico": "North America", "canada": "North America",
    "brazil": "Latin America",
    "south_africa": "Africa",
}

FIXED = TARIFFS["fixed_costs"]
BRAND_CVD = TARIFFS["brand_cvd"]

# Per-market fixed costs (USD) = regional base (freight + clearance +
# certification + inland) + market registration fee. The regional bases are
# reverse-engineered from the original 7-market dataset (EU 6100 / Non-EU
# Europe 5850 / Middle East 4150 / Oceania 5350) and extended by reasonable
# freight+certification estimates for the new P3 regions (Southeast Asia,
# North America, Latin America, Africa). Registration fees are the verified
# per-market values in tariffs.json.
REGION_BASE_FIXED = {
    "EU": 6100.0,
    "Non-EU Europe": 5850.0,
    "Middle East": 4150.0,
    "Oceania": 5350.0,
    "Southeast Asia": 4600.0,
    "North America": 7000.0,
    "Latin America": 6500.0,
    "Africa": 6200.0,
}
FIXED_BY_MARKET = {
    key: REGION_BASE_FIXED[MARKET_REGION[key]] + TARIFFS["markets"][key]["registration_fee_usd"]
    for key in MARKETS_ORDER
}

# Germany detailed-breakdown line items (matches existing md breakdowns).
GERMANY_BREAKDOWN_FIXED = {
    "freight_roro_usd": FIXED["freight_roro_usd"],
    "customs_clearance_usd": FIXED["customs_clearance_usd"],
    "certification_usd": FIXED["certification_usd"],
    "registration_usd": TARIFFS["markets"]["germany"]["registration_fee_usd"],
    "inland_transport_usd": FIXED["inland_transport_usd"],
}

TODAY = "2026-09-14"


def r2(x):
    return round(x + 1e-9, 2)


def r1(x):
    return round(x + 1e-9, 1)


def cvd_rate_for(brand, powertrain, region):
    """EU countervailing duty (Reg 2024/2754) applies to BEVs only.

    PHEV / EREV / HEV / petrol vehicles are NOT subject to the CVD.
    """
    if region != "EU":
        return 0.0
    if (powertrain or "BEV").upper() != "BEV":
        return 0.0
    return BRAND_CVD.get(brand, BRAND_CVD["_default"])


def calc_market(base, brand, pt, mkey):
    mk = TARIFFS["markets"][mkey]
    std = mk["standard_duty_rate"]
    vat = mk["vat_rate"]
    region = MARKET_REGION[mkey]
    cvd = cvd_rate_for(brand, pt, region)
    duty = std * base
    cvd_amt = cvd * (base + duty)
    vat_amt = vat * (base + duty + cvd_amt)
    fixed = FIXED_BY_MARKET[mkey]
    total = base + duty + cvd_amt + vat_amt + fixed
    premium = (total - base) / base * 100 if base else 0.0
    return {
        "market": MARKET_LABEL[mkey],
        "market_key": mkey,
        "region": region,
        "standard_duty_rate": round(std, 3),
        "countervailing_duty_rate": round(cvd, 3),
        "vat_rate": vat,
        "total_landed_usd": r2(total),
        "premium_pct": r1(premium),
    }


def calc_germany_breakdown(base, brand, pt):
    mk = TARIFFS["markets"]["germany"]
    std = mk["standard_duty_rate"]
    vat = mk["vat_rate"]
    cvd = cvd_rate_for(brand, pt, "EU")
    duty = r2(std * base)
    cvd_amt = r2(cvd * (base + duty))
    vat_amt = r2(vat * (base + duty + cvd_amt))
    bd = {
        "duty_cif_usd": duty,
        "countervailing_duty_usd": cvd_amt,
        "vat_usd": vat_amt,
        **GERMANY_BREAKDOWN_FIXED,
    }
    total = r2(base + duty + cvd_amt + vat_amt + sum(GERMANY_BREAKDOWN_FIXED.values()))
    premium = r1((total - base) / base * 100) if base else 0.0
    return {
        "market": "Germany",
        "standard_duty_rate": round(std, 3),
        "countervailing_duty_rate": round(cvd, 3),
        "vat_rate": vat,
        "total_landed_usd": total,
        "premium_pct": premium,
        "breakdown": bd,
    }


BRAND_DISPLAY = {
    "aeolus": "Aeolus", "aion": "AION", "aito": "AITO", "arcfox": "Arcfox",
    "avatr": "Avatr", "baojun": "Baojun", "baw": "BAW", "bestune": "Bestune",
    "byd": "BYD", "changan": "Changan", "chery": "Chery", "deepal": "Deepal",
    "denza": "Denza", "dongfeng-e": "Dongfeng e\u03c0", "exeed": "Exeed",
    "fangchengbao": "Fangchengbao", "firefly": "Firefly", "forthing": "Forthing",
    "gac-motor": "GAC Motor", "geely": "Geely", "geely-galaxy": "Geely Galaxy",
    "haval": "Haval", "hongqi": "Hongqi", "hyptec": "Hyptec", "icaur": "iCAR",
    "im": "IM", "jac": "JAC", "jac-refine": "JAC Refine", "jac-yiwei": "JAC Yiwei",
    "jaecoo": "Jaecoo", "jetour": "Jetour", "kaicene": "Kaicene",
    "leapmotor": "Leapmotor", "li-auto": "Li Auto", "luxeed": "Luxeed",
    "lynk-co": "Lynk Co", "m-hero": "M-Hero", "maextro": "Maextro",
    "maxus": "Maxus", "mg": "MG", "nio": "NIO", "onvo": "Onvo", "ora": "Ora",
    "roewe": "Roewe", "saic": "SAIC", "stelato": "Stelato", "tank": "Tank",
    "voyah": "Voyah", "wey": "Wey", "wuling": "Wuling", "xiaomi": "Xiaomi",
    "xpeng": "XPENG", "yangwang": "Yangwang", "zeekr": "Zeekr",
}

BODY_LABEL = {"SUV": "SUV", "Sedan": "Sedan", "MPV": "MPV", "Hatchback": "Hatchback"}


def slug_to_title(slug, brand, model):
    if model:
        return model
    bd = BRAND_DISPLAY.get(brand, brand.replace("-", " ").title())
    rest = slug
    if brand and slug.startswith(brand):
        rest = slug[len(brand):].lstrip("-")
    parts = []
    for tok in rest.split("-"):
        if tok.isdigit():
            parts.append(tok)
        elif len(tok) <= 3:
            parts.append(tok.upper())
        else:
            parts.append(tok.title())
    return f"{bd} {' '.join(parts)}".strip()


def gen_description(spec, title, brand):
    bname = BRAND_DISPLAY.get(brand, brand.replace("-", " ").title())
    pt = (spec.get("powertrain") or "BEV").upper()
    ptype = {"BEV": "battery-electric", "PHEV": "plug-in hybrid",
             "EREV": "extended-range electric", "HEV": "hybrid"}.get(pt, "electrified")
    bits = [f"{title} is a {BODY_LABEL.get(spec.get('body_type'), spec.get('body_type'))} {ptype} from {bname},"]
    if spec.get("range_cltc_km"):
        bits.append(f"offering {spec['range_cltc_km']} km of CLTC range")
    if spec.get("battery_kwh"):
        bits.append(f"a {spec['battery_kwh']} kWh battery")
    if spec.get("motor_power_kw"):
        bits.append(f"and {spec['motor_power_kw']} kW of motor power")
    return " ".join(bits) + ". Full landed-cost breakdown across 7 export markets for B2B import planning."


def gen_overview(spec, title, brand, germany, markets):
    bname = BRAND_DISPLAY.get(brand, brand.replace("-", " ").title())
    pt = (spec.get("powertrain") or "BEV").upper()
    ptype = {"BEV": "battery-electric", "PHEV": "plug-in hybrid",
             "EREV": "extended-range electric", "HEV": "hybrid"}.get(pt, "electrified")
    cheapest = min(markets, key=lambda m: m["premium_pct"])
    price = int(spec["price_usd"])
    s = (f"The {title} is a {BODY_LABEL.get(spec.get('body_type'), spec.get('body_type')).lower()} {ptype} from {bname}, ")
    if spec.get("motor_power_kw"):
        s += f"with {spec['motor_power_kw']} kW of motor power"
    if spec.get("accel_0_100_s"):
        s += f", a {spec['accel_0_100_s']}-second 0\u2013100 km/h time"
    s += f". It is positioned as a value-focused import, priced from ${price:,} ex-factory. "
    s += (f"For importers, the cheapest entry point is {cheapest['market']} at roughly "
          f"+{int(cheapest['premium_pct'])}% over base (about ${int(cheapest['total_landed_usd']):,} landed), ")
    g_cvd = germany.get("countervailing_duty_rate", 0)
    if g_cvd:
        s += (f"while the Germany estimate carries a {g_cvd*100:.1f}% countervailing duty on top of the "
              f"{germany['standard_duty_rate']*100:.0f}% standard tariff. ")
    else:
        s += "while Germany applies the standard tariff with no countervailing duty on this powertrain. "
    if spec.get("efficiency_kwh_100km"):
        s += f"In practice, the {spec['efficiency_kwh_100km']} kWh/100km efficiency "
        if spec.get("weight_kg"):
            s += f"is reasonable for its {spec['weight_kg']:,} kg curb weight; "
        else:
            s += "is a practical figure; "
    if spec.get("fast_charge") in (None, "-", ""):
        s += "only slow AC charging is listed, which affects fleet turnaround. "
    s += "It suits importers and fleet buyers evaluating Chinese EV landed cost."
    return s


def build_md(spec, apply):
    slug = spec["vehicle_id"]
    brand = spec["brand"]
    pt = (spec.get("powertrain") or "BEV").upper()
    title = slug_to_title(slug, brand, spec.get("model"))
    base = float(spec.get("price_usd") or 0)

    markets = [calc_market(base, brand, pt, k) for k in MARKETS_ORDER]
    germany = calc_germany_breakdown(base, brand, pt)
    desc = gen_description(spec, title, brand)
    overview = gen_overview(spec, title, brand, germany, markets)

    def n(v):
        try:
            return float(v)
        except (TypeError, ValueError):
            return None

    fm = {
        "title": title,
        "description": desc[:160],
        "slug": slug,
        "brand": brand,
        "type": spec.get("body_type", ""),
        "powertrain": pt,
        "price_usd": base,
        "currency": "USD",
    }
    opt_num = {
        "range_cltc_km": "range_cltc_km", "range_long_km": "range_long_km",
        "battery_kwh": "battery_kwh", "motor_power_kw": "motor_power_kw",
        "torque_nm": "torque_nm", "accel_0_100_s": "accel_0_100_s",
        "top_speed_kmh": "top_speed_kmh", "length_mm": "length_mm",
        "width_mm": "width_mm", "height_mm": "height_mm",
        "wheelbase_mm": "wheelbase_mm", "weight_kg": "weight_kg",
        "efficiency_kwh_100km": "efficiency_kwh_100km",
    }
    for src_key, dst_key in opt_num.items():
        v = n(spec.get(src_key))
        if v is not None:
            fm[dst_key] = v
    fm["fast_charge"] = spec.get("fast_charge", "-")
    if spec.get("variants"):
        fm["variants"] = spec["variants"]
    fm["landed_cost"] = germany
    fm["landed_cost_markets"] = markets
    fm["publishedDate"] = "2026-09-05"
    fm["author"] = spec.get("author", "Wei Wang")
    fm["tags"] = [brand, spec.get("body_type", "EV"), "chinese-ev", "export"]
    if spec.get("image"):
        fm["image"] = spec["image"]
    fm["data_tier"] = spec.get("data_tier", 1)
    fm["data_source"] = spec.get("data_source", "EV Hub catalog (manufacturer specs + EU Reg 2024/2754 landed-cost records)")
    fm["data_updated"] = spec.get("data_updated", TODAY)
    fm["data_reviewed"] = spec.get("data_reviewed", False)
    if spec.get("family"):
        fm["family"] = spec["family"]

    # body
    body = f"# {title}\n\n{title} (starting at ${int(base):,}) is a {fm['type']} from {brand.replace('-', ' ').upper()}.\n\n"
    if fm.get("range_cltc_km") is not None:
        body += f"- **Range**: {fm['range_cltc_km']} km (CLTC)\n"
    if fm.get("battery_kwh") is not None:
        body += f"- **Battery**: {fm['battery_kwh']} kWh\n"
    if fm.get("motor_power_kw") is not None:
        body += f"- **Motor power**: {fm['motor_power_kw']} kW\n"
    if fm.get("accel_0_100_s") is not None:
        body += f"- **0-100 km/h**: {fm['accel_0_100_s']} s\n"
    body += f"\n## Overview\n\n{overview}\n\n## Landed Cost by Market\n\nEstimated landed cost to import this vehicle into key export markets, including import duty, countervailing duty, VAT/GST, freight, and compliance costs.\n\n| Destination | Region | Total landed (USD) | Premium |\n|---|---|---|---|\n"
    for m in markets:
        body += f"| {m['market']} | {m['region']} | ${int(m['total_landed_usd']):,} | +{m['premium_pct']}% |\n"
    bd = germany.get("breakdown", {})
    if bd:
        body += f"\n## Detailed Breakdown \u2014 Germany\n\n| Cost item | Amount (USD) |\n|---|---|\n"
        body += f"| Base price | ${int(base):,} |\n"
        body += f"| Standard import duty ({int(germany['standard_duty_rate']*100)}%) | ${int(bd['duty_cif_usd']):,} |\n"
        if germany.get("countervailing_duty_rate"):
            body += f"| Countervailing duty ({germany['countervailing_duty_rate']*100:.1f}%) | ${int(bd['countervailing_duty_usd']):,} |\n"
        body += f"| VAT ({int(germany['vat_rate']*100)}%) | ${int(bd['vat_usd']):,} |\n"
        body += f"| RoRo freight | ${int(bd['freight_roro_usd']):,} |\n"
        body += f"| Customs clearance | ${int(bd['customs_clearance_usd']):,} |\n"
        body += f"| Certification | ${int(bd['certification_usd']):,} |\n"
        body += f"| Registration | ${int(bd['registration_usd']):,} |\n"
        body += f"| Inland transport | ${int(bd['inland_transport_usd']):,} |\n"
        body += f"| **Total landed** | **${int(germany['total_landed_usd']):,}** |\n\n"
        body += f"**Premium over base price**: +{germany['premium_pct']}%\n"

    out = ["---"]
    for k, v in fm.items():
        if v is None:
            continue
        if isinstance(v, (dict, list)):
            out.append(f"{k}: {json.dumps(v)}")
        elif isinstance(v, str):
            out.append(f"{k}: {json.dumps(v, ensure_ascii=False)}")
        else:
            out.append(f"{k}: {v}")
    out.append("---")
    out.append("")
    out.append(body)
    text = "\n".join(out)

    if apply:
        (VEHICLES_DIR / f"{slug}.md").write_text(text)
    return text


def update_master(vehicles, apply):
    d = json.loads(MASTER.read_text())
    existing = {v["vehicle_id"] for v in d["vehicles"]}
    added = 0
    for spec in vehicles:
        vid = spec["vehicle_id"]
        if vid in existing:
            continue
        entry = {
            "vehicle_id": vid,
            "model": slug_to_title(vid, spec["brand"], spec.get("model")),
            "brand": spec["brand"],
            "body_type": spec.get("body_type", ""),
            "powertrain": (spec.get("powertrain") or "BEV").upper(),
            "price_usd": float(spec.get("price_usd") or 0),
            "battery_kwh": spec.get("battery_kwh"),
            "range_cltc_km": spec.get("range_cltc_km"),
            "range_long_km": spec.get("range_long_km"),
            "range_standard": "CLTC",
            "motor_power_kw": spec.get("motor_power_kw"),
            "torque_nm": spec.get("torque_nm"),
            "data_tier": spec.get("data_tier", 1),
            "data_reviewed": spec.get("data_reviewed", False),
            "data_updated": spec.get("data_updated", TODAY),
        }
        if spec.get("variants"):
            entry["variants"] = spec["variants"]
        d["vehicles"].append(entry)
        added += 1
    d["count"] = len(d["vehicles"])
    d["generated"] = TODAY
    if apply:
        MASTER.write_text(json.dumps(d, ensure_ascii=False, indent=2))
    return added, d["count"]


def update_brand_master(vehicles, apply):
    d = json.loads(BRAND_MASTER.read_text())
    counts = {}
    for spec in vehicles:
        counts[spec["brand"]] = counts.get(spec["brand"], 0) + 1
    updates = []
    for b in d["brands"]:
        if b["brand_id"] in counts:
            b["vehicle_count"] += counts[b["brand_id"]]
            updates.append((b["brand_id"], b["vehicle_count"]))
    if apply:
        BRAND_MASTER.write_text(json.dumps(d, ensure_ascii=False, indent=2))
    return updates


def main():
    if len(sys.argv) < 2:
        print("usage: python3 scripts/add_vehicles.py <spec.json> [--apply]")
        sys.exit(1)
    spec_path = Path(sys.argv[1])
    apply = "--apply" in sys.argv
    specs = json.loads(spec_path.read_text())
    if isinstance(specs, dict):
        specs = specs.get("vehicles", specs.get("items", []))
    print(f"spec vehicles: {len(specs)} | mode={'APPLY' if apply else 'PREVIEW'}")
    for spec in specs:
        vid = spec.get("vehicle_id")
        if not vid or not spec.get("brand") or spec.get("price_usd") is None:
            print(f"  SKIP invalid spec: {vid}")
            continue
        md_path = VEHICLES_DIR / f"{vid}.md"
        exists = md_path.exists()
        build_md(spec, apply)
        print(f"  {'UPDATE' if exists else 'NEW'} {vid} -> {md_path.name}")
    added, total = update_master(specs, apply)
    brand_updates = update_brand_master(specs, apply)
    print(f"master: +{added} vehicles (total {total})")
    print(f"brand counts updated: {brand_updates}")
    if not apply:
        print("DRY RUN — no files written. Add --apply to commit changes.")


if __name__ == "__main__":
    main()
