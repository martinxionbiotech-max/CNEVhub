#!/usr/bin/env python3
"""Landed-cost formula regression tests (Phase 5).

Replicates the exact landed-cost formula used by the calculator page,
scripts/add_vehicles.py and scripts/extend_markets.py, then:

  1. Asserts a set of hand-verified test cases (market x powertrain x vehicle),
     covering EU high-CVD, PHEV/EREV (no CVD), Middle East, Oceania, and a
     high non-EU duty market.
  2. Recomputes every vehicle's landed_cost (Germany) and landed_cost_markets
     (30 markets) from src/data/tariffs.json and compares against frontmatter,
     catching any drift between data and the single-source tariff DB.

Usage:
  python3 scripts/test_landed_cost_regression.py          # run all checks
  python3 scripts/test_landed_cost_regression.py --cases  # test cases only
  python3 scripts/test_landed_cost_regression.py --full   # full 517x30 recompute only
"""
import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VEHICLES = ROOT / "src/content/vehicles"
TARIFFS = json.loads((ROOT / "src/data/tariffs.json").read_text())

MARKETS_ORDER = [
    "germany", "france", "netherlands", "sweden", "denmark", "spain",
    "italy", "belgium", "austria", "portugal", "ireland", "poland",
    "united_kingdom", "norway", "switzerland",
    "united_arab_emirates", "saudi_arabia", "israel", "qatar", "turkey",
    "australia", "new_zealand",
    "thailand", "malaysia", "indonesia", "singapore",
    "mexico", "canada",
    "brazil",
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
REGION_BASE_FIXED = {
    "EU": 6100.0, "Non-EU Europe": 5850.0, "Middle East": 4150.0,
    "Oceania": 5350.0, "Southeast Asia": 4600.0, "North America": 7000.0,
    "Latin America": 6500.0, "Africa": 6200.0,
}

BRAND_CVD = TARIFFS["brand_cvd"]


def r2(x):
    return round(x + 1e-9, 2)


def r1(x):
    return round(x + 1e-9, 1)


def cvd_rate_for(brand, powertrain, region):
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
    fixed = REGION_BASE_FIXED[region] + mk["registration_fee_usd"]
    total = base + duty + cvd_amt + vat_amt + fixed
    premium = (total - base) / base * 100 if base else 0.0
    return r2(total), r1(premium)


def calc_germany_breakdown(base, brand, pt):
    mk = TARIFFS["markets"]["germany"]
    std = mk["standard_duty_rate"]
    vat = mk["vat_rate"]
    cvd = cvd_rate_for(brand, pt, "EU")
    duty = r2(std * base)
    cvd_amt = r2(cvd * (base + duty))
    vat_amt = r2(vat * (base + duty + cvd_amt))
    fixed = sum([
        TARIFFS["fixed_costs"]["freight_roro_usd"],
        TARIFFS["fixed_costs"]["customs_clearance_usd"],
        TARIFFS["fixed_costs"]["certification_usd"],
        mk["registration_fee_usd"],
        TARIFFS["fixed_costs"]["inland_transport_usd"],
    ])
    total = r2(base + duty + cvd_amt + vat_amt + fixed)
    premium = r1((total - base) / base * 100) if base else 0.0
    return total, premium


# (vehicle_slug, base, brand, powertrain, market_key, expected_total)
CASES = [
    ("byd-dolphin", 14020.0, "byd", "BEV", "germany", 28072.05),        # EU, BYD 17% CVD
    ("mg-4", 9690.0, "mg", "BEV", "germany", 23761.74),                  # EU, SAIC 35.3% CVD
    ("xiaomi-su7", 30320.0, "xiaomi", "BEV", "germany", 54504.48),       # EU, default 20.7% CVD
    ("byd-qin-plus-dm-i", 11080.0, "byd", "PHEV", "germany", 21103.72),  # EU, PHEV => no CVD
    ("aito-m9-erev", 65250.0, "aito", "EREV", "germany", 92012.25),      # EU, EREV => no CVD
    ("byd-dolphin", 14020.0, "byd", "BEV", "united_arab_emirates", 19907.05),  # ME, no CVD, 5% duty
    ("byd-dolphin", 14020.0, "byd", "BEV", "australia", 21272.00),       # Oceania, 0 duty
    ("byd-dolphin", 14020.0, "byd", "BEV", "turkey", 27803.60),          # ME, 40% duty (no SCT)
    ("mg-4", 9690.0, "mg", "BEV", "saudi_arabia", 16150.68),             # ME, SAIC no CVD, 5% duty
]


def run_cases():
    failures = 0
    for slug, base, brand, pt, mkey, expected in CASES:
        total, premium = calc_market(base, brand, pt, mkey)
        ok = abs(total - expected) < 0.005
        if not ok:
            failures += 1
        mark = "PASS" if ok else "FAIL"
        print(f"{mark}  {slug:<22} {brand:<8} {pt:<5} -> {MARKET_LABEL[mkey]:<20} "
              f"got {total:>10.2f}  expected {expected:>10.2f}  (+{premium}%)")
    return failures


def split_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not m:
        return {}, ""
    return m.group(1), m.group(2)


def parse_num_from_fm(fm, key_pattern):
    m = re.search(key_pattern, fm)
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except Exception:
        return None


def run_full():
    import yaml
    files = sorted(VEHICLES.glob("*.md"))
    checked = 0
    mismatches = []
    artifacts = []  # ±1-cent rounding-order artifacts (cosmetic, not formula errors)
    for path in files:
        raw = path.read_text()
        fm, _body = split_frontmatter(raw)
        if not fm:
            continue
        try:
            data = yaml.safe_load(fm)
        except Exception:
            continue
        base = float(data.get("price_usd") or 0)
        brand = (data.get("brand") or "").lower()
        pt = (data.get("powertrain") or "BEV").upper()

        # Germany landed_cost
        lc = data.get("landed_cost")
        if lc and "total_landed_usd" in lc:
            exp_total, _ = calc_germany_breakdown(base, brand, pt)
            diff = abs(float(lc["total_landed_usd"]) - exp_total)
            if diff >= 0.015:
                mismatches.append((path.stem, "germany", float(lc["total_landed_usd"]), exp_total, diff))
            elif diff > 0:
                artifacts.append((path.stem, "germany", diff))

        # 30-market landed_cost_markets
        for m in data.get("landed_cost_markets") or []:
            mkey = m.get("market_key")
            if not mkey or mkey not in TARIFFS["markets"]:
                continue
            exp_total, _ = calc_market(base, brand, pt, mkey)
            diff = abs(float(m.get("total_landed_usd", 0)) - exp_total)
            if diff >= 0.015:
                mismatches.append((path.stem, mkey, float(m.get("total_landed_usd", 0)), exp_total, diff))
            elif diff > 0:
                artifacts.append((path.stem, mkey, diff))
        checked += 1

    print(f"\nfull recompute: checked={checked} vehicles")
    print(f"real mismatches (>= $0.015): {len(mismatches)}")
    print(f"±1-cent rounding artifacts (cosmetic, < $0.015): {len(artifacts)}")
    for slug, mkey, got, exp, diff in mismatches[:40]:
        print(f"  MISMATCH  {slug:<24} {mkey:<20} frontmatter={got:<12.2f} recomputed={exp:<12.2f} Δ={diff:.2f}")
    return len(mismatches)


def main():
    args = set(sys.argv[1:])
    only_cases = "--cases" in args
    only_full = "--full" in args
    do_cases = only_cases or not only_full
    do_full = only_full or not only_cases

    failures = 0
    if do_cases:
        print("== Test cases ==")
        failures += run_cases()
    if do_full:
        failures += run_full()

    print(f"\n{'FAIL' if failures else 'PASS'} ({failures} failure(s))")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
