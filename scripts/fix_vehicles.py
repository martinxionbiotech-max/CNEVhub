#!/usr/bin/env python3
"""One-shot content+data fix for electricvehiclehub.net vehicle pages.

1. Fix micro-car body types (SUV -> Hatchback) + empty type (Stelato S9T -> Sedan)
2. Fix URL spelling: chery-tiggo-7-plus-new-energe -> -new-energy
3. Regenerate the templated "## Overview" paragraph with unique, data-driven commentary
"""
import hashlib
import re
import sys
from pathlib import Path

import yaml

VEHICLES = Path("src/content/vehicles")

# (filename, old_type, new_type)
TYPE_FIXES = {
    "baojun-kiwi-ev.md": ("SUV", "Hatchback"),
    "bestune-pony.md": ("SUV", "Hatchback"),
    "changan-nevo-lumin.md": ("SUV", "Hatchback"),
    "geely-galaxy-lc.md": ("SUV", "Hatchback"),
    "leapmotor-t03.md": ("SUV", "Hatchback"),
    "wuling-air-ev.md": ("SUV", "Hatchback"),
    "wuling-hongguang-mini-ev.md": ("SUV", "Hatchback"),
    "wuling-nano-ev.md": ("SUV", "Hatchback"),
    "stelato-s9t.md": ("", "Sedan"),
}


def h(s: str, n: int) -> int:
    return int(hashlib.md5(s.encode()).hexdigest(), 16) % n


def money(v) -> str:
    if v is None:
        return ""
    return f"${v:,.0f}"


def classify(data) -> str:
    t = (data.get("type") or "").strip().lower()
    length = data.get("length_mm") or 0
    if t == "mpv":
        return "MPV"
    if t == "hatchback":
        return "micro hatchback" if length and length < 3600 else "compact hatchback"
    if t == "sedan":
        if length and length >= 4900:
            return "full-size sedan"
        if length and length >= 4600:
            return "midsize sedan"
        return "compact sedan"
    if t == "suv":
        if length and length < 4400:
            return "subcompact SUV"
        if length and length < 4800:
            return "compact SUV"
        if length and length < 5100:
            return "midsize SUV"
        return "full-size SUV"
    return "vehicle"


def price_tier(p) -> str:
    if p < 12000:
        return "budget"
    if p < 25000:
        return "value"
    if p < 40000:
        return "mid-market"
    if p < 65000:
        return "premium"
    return "luxury"


def powertrain_label(p) -> str:
    p = (p or "BEV").upper()
    return {"BEV": "battery-electric", "EREV": "extended-range electric", "PHEV": "plug-in hybrid"}.get(p, p.lower())


def overview(data) -> str:
    title = data.get("title", "").strip()
    brand = (data.get("brand") or "the brand").strip().upper()
    seg = classify(data)
    pt_label = powertrain_label(data.get("powertrain"))
    price = data.get("price_usd")
    rng = data.get("range_cltc_km")
    power = data.get("motor_power_kw")
    accel = data.get("accel_0_100_s")
    eff = data.get("efficiency_kwh_100km")
    weight = data.get("weight_kg")
    markets = data.get("landed_cost_markets") or []

    seg_article = "an" if seg[0].lower() in "aeiou" else "a"

    # --- sentence 1: identity + spec highlight ---
    spec_bits = []
    if rng:
        spec_bits.append(f"{rng:,.0f} km of CLTC range")
    if power:
        spec_bits.append(f"{power:,.0f} kW of motor power")
    if accel and accel < 8:
        spec_bits.append(f"a {accel}-second 0\u2013100 km/h time")
    spec_phrase = ", ".join(spec_bits) if spec_bits else "a compact electric powertrain"
    s1 = f"The {title} is {seg_article} {seg} {pt_label} from {brand}, with {spec_phrase}."

    # --- sentence 2: positioning / price tier ---
    tier = price_tier(price) if price is not None else "mid-market"
    tier_map = {
        "budget": "It sits at the affordable end of the Chinese EV export range",
        "value": "It is positioned as a value-focused import",
        "mid-market": "It lands in the mid-market segment where spec-to-price ratio matters most",
        "premium": "It is positioned as a premium import",
        "luxury": "It is a luxury-tier flagship",
    }
    s2 = f"{tier_map[tier]}{', priced from ' + money(price) + ' ex-factory' if price is not None else ''}."

    # --- sentence 3: import economics (cheapest market + EU CVD) ---
    econ_parts = []
    if markets:
        valid = [m for m in markets if isinstance(m, dict) and m.get("premium_pct") is not None]
        if valid:
            cheapest = min(valid, key=lambda m: m["premium_pct"])
            econ_parts.append(
                f"the cheapest entry point is {cheapest['market']} at roughly +{cheapest['premium_pct']:.0f}% over base"
                + (f" (about {money(cheapest.get('total_landed_usd'))} landed)" if cheapest.get('total_landed_usd') else "")
            )
        eu = [m for m in valid if (m.get("region") == "EU" and (m.get("countervailing_duty_rate") or 0) > 0)]
        if eu:
            max_cvd = max(m["countervailing_duty_rate"] for m in eu)
            cvd_market = eu[0]["market"]
            econ_parts.append(
                f"the {cvd_market} estimate carries a {max_cvd*100:.1f}% countervailing duty on top of the 10% standard tariff"
            )
    if econ_parts:
        s3 = f"For importers, {', while '.join(econ_parts)}."
    else:
        s3 = "Import economics vary by destination, with duty, VAT and freight stacking on the base price."

    # --- sentence 4: practical / buyer note ---
    practical = []
    if rng and rng < 250:
        practical.append("its short range suits urban and last-mile use rather than long trips")
    if eff and weight:
        if eff > 20:
            practical.append(f"the {eff} kWh/100km efficiency is unremarkable for its {weight:,} kg curb weight")
        else:
            practical.append(f"the {eff} kWh/100km efficiency is strong for its {weight:,} kg curb weight")
    pt_key = (data.get("powertrain") or "BEV").upper()
    if pt_key == "BEV" and data.get("fast_charge") in (None, "", "-"):
        practical.append("only slow AC charging is listed, which affects fleet turnaround")
    buyer_map = {
        "micro hatchback": "private urban buyers and small delivery fleets",
        "compact hatchback": "city commuters and first-time importers",
        "subcompact SUV": "urban families who want a raised driving position",
        "compact SUV": "families and fleet buyers who need practicality",
        "midsize SUV": "family and executive buyers prioritizing space",
        "full-size SUV": "large families and executive fleets",
        "compact sedan": "budget-conscious commuters and ride-hailing fleets",
        "midsize sedan": "business fleets and long-distance commuters",
        "full-size sedan": "executive and chauffeur-driven fleets",
        "MPV": "shuttle operators and large families",
        "vehicle": "buyers who prioritize landed-cost value",
    }
    who = f"it suits {buyer_map.get(seg, 'buyers who prioritize landed-cost value')}"
    if practical:
        s4 = "In practice, " + "; ".join(practical) + ". " + who[0].upper() + who[1:] + "."
    else:
        s4 = "In practice, " + who + "."

    return " ".join([s1, s2, s3, s4])


def fix_type_strings(text: str, old: str, new: str) -> str:
    if not old:  # empty type fix (Stelato S9T)
        text = re.sub(r'type: ""', f'type: "{new}"', text)
        text = re.sub(r'\) is a  from', f') is a {new} from', text)  # intro line, capitalized
        text = text.replace('is a  from', f'is a {new.lower()} from')  # remaining = description, lowercase
        return text
    text = re.sub(rf'type: "{old}"', f'type: "{new}"', text)
    text = text.replace(f'is a {old.lower()} from', f'is a {new.lower()} from')  # description + old overview (lowercase)
    text = text.replace(f'"{old}"', f'"{new}"')  # tags
    text = text.replace(f'is a {old} from', f'is a {new} from')  # intro line (uppercase)
    return text


def process(apply: bool):
    files = sorted(VEHICLES.glob("*.md"))
    changed = 0
    type_fixed = 0
    previews = []
    for path in files:
        raw = path.read_text()
        data, body = None, ""
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.DOTALL)
        if not m:
            continue
        try:
            data = yaml.safe_load(m.group(1))
            body = m.group(2)
        except Exception as e:
            print(f"SKIP (yaml): {path.name}: {e}")
            continue

        new_raw = raw

        # 1) type fixes
        if path.name in TYPE_FIXES:
            old_t, new_t = TYPE_FIXES[path.name]
            new_raw = fix_type_strings(new_raw, old_t, new_t)
            data["type"] = new_t
            type_fixed += 1

        # 2) URL spelling
        if path.name == "chery-tiggo-7-plus-new-energe.md":
            new_raw = new_raw.replace("Chery Tiggo 7 PLUS NEW Energe", "Chery Tiggo 7 PLUS New Energy")
            new_raw = new_raw.replace("chery-tiggo-7-plus-new-energe", "chery-tiggo-7-plus-new-energy")
            data["title"] = data["title"].replace("NEW Energe", "New Energy")
            data["slug"] = "chery-tiggo-7-plus-new-energy"
            new_name = path.with_name("chery-tiggo-7-plus-new-energy.md")

        # 3) regenerate Overview
        ov = overview(data)
        marker_s = "## Overview\n\n"
        marker_e = "\n## Landed Cost by Market"
        try:
            i_s = body.index(marker_s) + len(marker_s)
            i_e = body.index(marker_e, i_s)
            new_body = body[:i_s] + ov + body[i_e:]
            new_raw = new_raw.replace(body, new_body, 1)
        except ValueError:
            print(f"WARN: overview markers missing in {path.name}")

        if new_raw != raw:
            changed += 1
            if len(previews) < 4:
                previews.append((path.name, ov))
            if apply:
                if path.name == "chery-tiggo-7-plus-new-energe.md":
                    path.write_text(new_raw)
                    path.rename(new_name)
                    print(f"RENAMED + fixed: {path.name} -> {new_name.name}")
                else:
                    path.write_text(new_raw)

    print(f"\nTotal files: {len(files)} | changed: {changed} | type-fixed: {type_fixed}")
    print(f"Mode: {'APPLY' if apply else 'PREVIEW'}\n")
    for name, ov in previews:
        print(f"--- {name} ---")
        print(ov)
        print()


if __name__ == "__main__":
    process(apply="--apply" in sys.argv)
