#!/usr/bin/env python3
"""P0: Recompute every vehicle's landed-cost from the central tariff DB.

Reads src/data/tariffs.json (single source of truth for duty/CVD/VAT rates),
recomputes landed_cost + landed_cost_markets for all vehicles, preserving the
existing fixed import costs (derived from current data).
"""
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
VEHICLES = ROOT / "src/content/vehicles"
TARIFFS = json.loads((ROOT / "src/data/tariffs.json").read_text())

MARKET_KEY = {
    "germany": "Germany",
    "united_kingdom": "United Kingdom",
    "netherlands": "Netherlands",
    "france": "France",
    "united_arab_emirates": "United Arab Emirates",
    "saudi_arabia": "Saudi Arabia",
    "australia": "Australia",
}


def cvd_rate_for(brand, powertrain, region):
    # Countervailing duty applies to EU markets only, and to BEVs only.
    if region != "EU":
        return 0.0
    pt = (powertrain or "BEV").upper()
    if pt in ("PHEV", "EREV"):
        return 0.0
    return TARIFFS["brand_cvd"].get(brand, TARIFFS["brand_cvd"]["_default"])


def r2(x):
    return round(x + 1e-9, 2)


def r1(x):
    return round(x + 1e-9, 1)


def recompute_market(base, std_rate, vat_rate, total_old, cvd_old, cvd_new):
    duty = std_rate * base
    cvd_old_amt = cvd_old * (base + duty)
    vat_old = vat_rate * (base + duty + cvd_old_amt)
    fixed = total_old - base - duty - cvd_old_amt - vat_old
    cvd_new_amt = cvd_new * (base + duty)
    vat_new = vat_rate * (base + duty + cvd_new_amt)
    total_new = base + duty + cvd_new_amt + vat_new + fixed
    premium_new = (total_new - base) / base * 100 if base else 0.0
    return r2(total_new), r1(premium_new)


def recompute_breakdown(base, std_rate, vat_rate, cvd_new, bd):
    duty = r2(std_rate * base)
    cvd = r2(cvd_new * (base + duty))
    vat = r2(vat_rate * (base + duty + cvd))
    fixed = (bd.get("freight_roro_usd", 0) + bd.get("customs_clearance_usd", 0)
             + bd.get("certification_usd", 0) + bd.get("registration_usd", 0)
             + bd.get("inland_transport_usd", 0))
    total = r2(base + duty + cvd + vat + fixed)
    premium = r1((total - base) / base * 100) if base else 0.0
    return {
        "duty_cif_usd": duty,
        "countervailing_duty_usd": cvd,
        "vat_usd": vat,
        "freight_roro_usd": bd.get("freight_roro_usd", 0),
        "customs_clearance_usd": bd.get("customs_clearance_usd", 0),
        "certification_usd": bd.get("certification_usd", 0),
        "registration_usd": bd.get("registration_usd", 0),
        "inland_transport_usd": bd.get("inland_transport_usd", 0),
    }, total, premium


def process(apply: bool):
    changed = 0
    for path in sorted(VEHICLES.glob("*.md")):
        raw = path.read_text()
        m = re.match(r"^---\n(.*?)\n---\n", raw, re.DOTALL)
        if not m:
            continue
        try:
            data = yaml.safe_load(m.group(1))
        except Exception:
            continue
        base = float(data.get("price_usd") or 0)
        brand = (data.get("brand") or "").lower()
        pt = (data.get("powertrain") or "BEV").upper()
        cvd_new = cvd_rate_for(brand, pt, "EU")

        # landed_cost (Germany, with breakdown)
        lc = data.get("landed_cost") or {}
        new_lc = dict(lc)
        if lc:
            mk = TARIFFS["markets"].get("germany", {})
            new_bd, total, premium = recompute_breakdown(
                base, mk.get("standard_duty_rate", 0), mk.get("vat_rate", 0),
                cvd_new, lc.get("breakdown") or {},
            )
            new_lc["countervailing_duty_rate"] = cvd_new
            new_lc["total_landed_usd"] = total
            new_lc["premium_pct"] = premium
            new_lc["breakdown"] = new_bd

        # landed_cost_markets (7 markets)
        new_markets = []
        for mk in data.get("landed_cost_markets") or []:
            nm = dict(mk)
            key = next((k for k, v in MARKET_KEY.items() if v == mk.get("market")), None)
            if key and key in TARIFFS["markets"]:
                rates = TARIFFS["markets"][key]
                cvd_mkt = cvd_rate_for(brand, pt, rates.get("region"))
                tot, prem = recompute_market(
                    base, rates["standard_duty_rate"], rates["vat_rate"],
                    mk.get("total_landed_usd") or 0, mk.get("countervailing_duty_rate") or 0, cvd_mkt,
                )
                nm["countervailing_duty_rate"] = cvd_mkt
                nm["total_landed_usd"] = tot
                nm["premium_pct"] = prem
            new_markets.append(nm)

        new_raw = re.sub(r'^landed_cost: .*$', f'landed_cost: {json.dumps(new_lc)}', raw, count=1, flags=re.M)
        new_raw = re.sub(r'^landed_cost_markets: .*$', f'landed_cost_markets: {json.dumps(new_markets)}', new_raw, count=1, flags=re.M)

        if new_raw != raw:
            changed += 1
            if apply:
                path.write_text(new_raw)

    print(f"files recomputed: {changed} | mode={'APPLY' if apply else 'PREVIEW'}")
    print("(0 changes = all landed-cost data already matches the central tariff DB)")


if __name__ == "__main__":
    process(apply="--apply" in sys.argv)
