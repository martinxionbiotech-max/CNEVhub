#!/usr/bin/env python3
"""P3: Extend every vehicle's landed_cost_markets from 7 -> 30 markets.

Recomputes landed_cost_markets (frontmatter) and the body "Landed Cost by
Market" markdown table for all vehicles, using the regional fixed-cost model
in scripts/add_vehicles.py (REGION_BASE_FIXED + per-market registration fee).

The Germany landed_cost (with breakdown) is left unchanged — its duty/CVD/VAT
and fixed costs do not change under the 30-market expansion.

Usage:
  python3 scripts/extend_markets.py [--apply]
Without --apply it is a PREVIEW (dry run).
"""
import json
import re
import sys
from pathlib import Path

import yaml

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


def r2(x):
    return round(x + 1e-9, 2)


def r1(x):
    return round(x + 1e-9, 1)


def cvd_rate_for(brand, powertrain, region):
    if region != "EU":
        return 0.0
    if (powertrain or "BEV").upper() != "BEV":
        return 0.0
    return TARIFFS["brand_cvd"].get(brand, TARIFFS["brand_cvd"]["_default"])


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


def rebuild_body_table(body, markets, price):
    """Replace the '## Landed Cost by Market' table with 30 rows."""
    header = "| Destination | Region | Total landed (USD) | Premium |\n|---|---|---|---|"
    rows = []
    for m in markets:
        rows.append(f"| {m['market']} | {m['region']} | ${int(m['total_landed_usd']):,} | +{m['premium_pct']}% |")
    table = header + "\n" + "\n".join(rows)
    # 替换从表头到 "## Detailed Breakdown" 之前的所有行
    pattern = re.compile(
        r"\| Destination \| Region \| Total landed \(USD\) \| Premium \|.*?(?=\n## Detailed Breakdown)",
        re.DOTALL,
    )
    if pattern.search(body):
        return pattern.sub(table, body)
    return body


def process(apply):
    changed = 0
    for path in sorted(VEHICLES.glob("*.md")):
        raw = path.read_text()
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.DOTALL)
        if not m:
            continue
        try:
            data = yaml.safe_load(m.group(1))
        except Exception:
            continue
        base = float(data.get("price_usd") or 0)
        brand = (data.get("brand") or "").lower()
        pt = (data.get("powertrain") or "BEV").upper()

        markets = [calc_market(base, brand, pt, k) for k in MARKETS_ORDER]

        # frontmatter: replace landed_cost_markets line
        new_fm = re.sub(
            r'^landed_cost_markets: .*$',
            f'landed_cost_markets: {json.dumps(markets)}',
            m.group(1), count=1, flags=re.M,
        )

        # body: rebuild table
        new_body = rebuild_body_table(m.group(2), markets, base)

        new_raw = "---\n" + new_fm + "\n---" + new_body
        if new_raw != raw:
            changed += 1
            if apply:
                path.write_text(new_raw)

    print(f"files extended to 30 markets: {changed} | mode={'APPLY' if apply else 'PREVIEW'}")


if __name__ == "__main__":
    process(apply="--apply" in sys.argv)
