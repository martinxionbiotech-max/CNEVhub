#!/usr/bin/env python3
"""Fix brand-level countervailing duty rates to match EU Reg 2024/2754.

Correct producer-group rates:
  BYD Group  (byd, denza, yangwang, fangchengbao)                    -> 17.0%
  Geely Group(geely, geely-galaxy, zeekr, lynk-co)                   -> 18.8%
  SAIC Group (mg, maxus, roewe, saic, wuling, baojun, im)            -> 35.3%
  Tesla (Shanghai)                                                   -> 7.8%
  Other cooperating producers (default)                              -> 20.7%

Applies to BEV vehicles only (PHEV/EREV already CVD=0). Recomputes
landed_cost + landed_cost_markets, preserving fixed import costs.
"""
import json
import re
import sys
from pathlib import Path

import yaml

VEHICLES = Path("src/content/vehicles")

GROUP_RATES = {
    "byd": 0.17, "denza": 0.17, "yangwang": 0.17, "fangchengbao": 0.17,
    "geely": 0.188, "geely-galaxy": 0.188, "zeekr": 0.188, "lynk-co": 0.188,
    "mg": 0.353, "maxus": 0.353, "roewe": 0.353, "saic": 0.353,
    "wuling": 0.353, "baojun": 0.353, "im": 0.353,
    "tesla": 0.078,
}
DEFAULT_RATE = 0.207  # other cooperating producers


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
    summary = {}
    preview = []
    for path in sorted(VEHICLES.glob("*.md")):
        raw = path.read_text()
        m = re.match(r"^---\n(.*?)\n---\n", raw, re.DOTALL)
        if not m:
            continue
        try:
            data = yaml.safe_load(m.group(1))
        except Exception as e:
            print(f"SKIP yaml {path.name}: {e}")
            continue
        pt = (data.get("powertrain") or "BEV").upper()
        if pt != "BEV":
            continue
        brand = (data.get("brand") or "").lower()
        target = GROUP_RATES.get(brand, DEFAULT_RATE)
        lc = data.get("landed_cost") or {}
        current = lc.get("countervailing_duty_rate")
        if current is None:
            continue
        if abs(current - target) < 0.0001:
            continue

        base = float(data.get("price_usd") or 0)
        new_lc = dict(lc)
        bd = lc.get("breakdown") or {}
        new_bd, total, premium = recompute_breakdown(
            base, lc.get("standard_duty_rate") or 0, lc.get("vat_rate") or 0, target, bd
        )
        new_lc["countervailing_duty_rate"] = target
        new_lc["total_landed_usd"] = total
        new_lc["premium_pct"] = premium
        new_lc["breakdown"] = new_bd

        new_markets = []
        for mk in data.get("landed_cost_markets") or []:
            nm = dict(mk)
            tot, prem = recompute_market(
                base, mk.get("standard_duty_rate") or 0, mk.get("vat_rate") or 0,
                mk.get("total_landed_usd") or 0, mk.get("countervailing_duty_rate") or 0, target,
            )
            nm["countervailing_duty_rate"] = target
            nm["total_landed_usd"] = tot
            nm["premium_pct"] = prem
            new_markets.append(nm)

        new_raw = re.sub(r'^landed_cost: .*$', f'landed_cost: {json.dumps(new_lc)}', raw, count=1, flags=re.M)
        new_raw = re.sub(r'^landed_cost_markets: .*$', f'landed_cost_markets: {json.dumps(new_markets)}', new_raw, count=1, flags=re.M)

        if new_raw != raw:
            changed += 1
            key = f"{current}->{target}"
            summary[key] = summary.get(key, 0) + 1
            if len(preview) < 5:
                preview.append((path.name, brand, current, target))
            if apply:
                path.write_text(new_raw)

    print(f"BEV CVD rate fixes: {changed} | mode={'APPLY' if apply else 'PREVIEW'}")
    for k, v in sorted(summary.items()):
        print(f"  rate {k}: {v} vehicles")
    for name, brand, cur, tgt in preview:
        print(f"    e.g. {name} ({brand}): {cur} -> {tgt}")


if __name__ == "__main__":
    process(apply="--apply" in sys.argv)
