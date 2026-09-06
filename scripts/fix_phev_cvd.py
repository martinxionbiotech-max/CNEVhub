#!/usr/bin/env python3
"""Fix landed-cost data: PHEV/EREV vehicles must not carry the BEV countervailing duty.

EU CVD (Reg 2024/2754) applies to BEVs only. PHEV and EREV pay only the 10%
standard duty. Recompute landed_cost + landed_cost_markets with CVD = 0,
preserving the fixed import costs (freight/clearance/cert/registration/inland).
"""
import json
import re
import sys
from pathlib import Path

import yaml

VEHICLES = Path("src/content/vehicles")


def round2(x):
    return round(x + 1e-9, 2)


def round1(x):
    return round(x + 1e-9, 1)


def recompute_market(base, std_rate, vat_rate, total_old, cvd_old_rate):
    """Recompute a single market entry with CVD removed, preserving fixed costs."""
    duty = std_rate * base
    cvd_old = cvd_old_rate * (base + duty)
    vat_old = vat_rate * (base + duty + cvd_old)
    fixed = total_old - base - duty - cvd_old - vat_old
    # new, CVD = 0
    vat_new = vat_rate * (base + duty)
    total_new = base + duty + vat_new + fixed
    premium_new = (total_new - base) / base * 100 if base else 0.0
    return round2(total_new), round1(premium_new), round2(fixed)


def recompute_breakdown(base, std_rate, vat_rate, bd):
    """Recompute the detailed Germany breakdown with CVD = 0, keep fixed costs."""
    duty = round2(std_rate * base)
    cvd = 0.0
    vat = round2(vat_rate * (base + duty + cvd))
    fixed = (bd.get("freight_roro_usd", 0) + bd.get("customs_clearance_usd", 0)
             + bd.get("certification_usd", 0) + bd.get("registration_usd", 0)
             + bd.get("inland_transport_usd", 0))
    total = round2(base + duty + cvd + vat + fixed)
    premium = round1((total - base) / base * 100) if base else 0.0
    return {
        "duty_cif_usd": duty,
        "countervailing_duty_usd": 0.0,
        "vat_usd": vat,
        "freight_roro_usd": bd.get("freight_roro_usd", 0),
        "customs_clearance_usd": bd.get("customs_clearance_usd", 0),
        "certification_usd": bd.get("certification_usd", 0),
        "registration_usd": bd.get("registration_usd", 0),
        "inland_transport_usd": bd.get("inland_transport_usd", 0),
    }, total, premium


def process(apply: bool):
    changed = 0
    preview = []
    for path in sorted(VEHICLES.glob("*.md")):
        raw = path.read_text()
        m = re.match(r"^---\n(.*?)\n---\n", raw, re.DOTALL)
        if not m:
            continue
        fm_text = m.group(1)
        try:
            data = yaml.safe_load(fm_text)
        except Exception as e:
            print(f"SKIP yaml {path.name}: {e}")
            continue
        pt = (data.get("powertrain") or "BEV").upper()
        if pt not in ("PHEV", "EREV"):
            continue
        base = float(data.get("price_usd") or 0)

        # 1) landed_cost (Germany, with breakdown)
        lc = data.get("landed_cost") or {}
        new_lc = dict(lc)
        bd = lc.get("breakdown") or {}
        new_bd, total, premium = recompute_breakdown(
            base, lc.get("standard_duty_rate") or 0, lc.get("vat_rate") or 0, bd
        )
        new_lc["countervailing_duty_rate"] = 0.0
        new_lc["total_landed_usd"] = total
        new_lc["premium_pct"] = premium
        new_lc["breakdown"] = new_bd

        # 2) landed_cost_markets (7 markets)
        new_markets = []
        for mk in data.get("landed_cost_markets") or []:
            nm = dict(mk)
            tot, prem, _fixed = recompute_market(
                base, mk.get("standard_duty_rate") or 0, mk.get("vat_rate") or 0,
                mk.get("total_landed_usd") or 0, mk.get("countervailing_duty_rate") or 0,
            )
            nm["countervailing_duty_rate"] = 0.0
            nm["total_landed_usd"] = tot
            nm["premium_pct"] = prem
            new_markets.append(nm)

        # 3) rewrite the two frontmatter lines
        new_raw = raw
        lc_json = json.dumps(new_lc, ensure_ascii=False)
        mk_json = json.dumps(new_markets, ensure_ascii=False)
        new_raw = re.sub(r'^landed_cost: .*$', f'landed_cost: {lc_json}', new_raw, count=1, flags=re.M)
        new_raw = re.sub(r'^landed_cost_markets: .*$', f'landed_cost_markets: {mk_json}', new_raw, count=1, flags=re.M)

        if new_raw != raw:
            changed += 1
            if len(preview) < 3:
                preview.append((path.name, pt, base, lc.get("total_landed_usd"), total,
                                lc.get("premium_pct"), premium))
            if apply:
                path.write_text(new_raw)

    print(f"PHEV/EREV fixed: {changed} | mode={'APPLY' if apply else 'PREVIEW'}")
    for name, pt, base, old_t, new_t, old_p, new_p in preview:
        print(f"  {name} ({pt}) base ${base:,.0f}: DE landed ${old_t:,.0f}->${new_t:,.0f} (+{old_p}% -> +{new_p}%)")


if __name__ == "__main__":
    process(apply="--apply" in sys.argv)
