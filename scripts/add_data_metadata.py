#!/usr/bin/env python3
"""P0: Add data quality metadata to every vehicle frontmatter.

- data_tier: 1 (complete) / 2 (missing one spec) / 3 (thin, missing 2+)
- data_source: provenance string
- data_updated: last data refresh date
- data_reviewed: human-review flag (default false)
"""
import re
import sys
from pathlib import Path

import yaml

VEHICLES = Path("src/content/vehicles")

ESSENTIAL = ("price_usd", "type", "landed_cost_markets")
SPEC = ("range_cltc_km", "battery_kwh", "motor_power_kw")

DATE = "2026-09-07"
SOURCE = "EV Hub catalog (manufacturer specs + EU Reg 2024/2754 landed-cost records)"


def tier_of(d) -> int:
    missing_essential = [k for k in ESSENTIAL if not d.get(k)]
    missing_spec = [k for k in SPEC if not d.get(k)]
    if missing_essential or len(missing_spec) >= 2:
        return 3
    if len(missing_spec) == 1:
        return 2
    return 1


def process(apply: bool):
    from collections import Counter
    dist = Counter()
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
        tier = tier_of(data)
        dist[tier] += 1

        # insert metadata fields before the closing --- of frontmatter
        fm = m.group(1)
        if "data_tier:" in fm:
            continue
        new_fields = (
            f"\ndata_tier: {tier}"
            f'\ndata_source: "{SOURCE}"'
            f'\ndata_updated: "{DATE}"'
            f"\ndata_reviewed: false"
        )
        new_fm = fm + new_fields
        new_raw = raw.replace(fm, new_fm, 1)
        if new_raw != raw:
            changed += 1
            if apply:
                path.write_text(new_raw)

    print(f"tier distribution: {dict(dist)}")
    print(f"files to tag: {changed} | mode={'APPLY' if apply else 'PREVIEW'}")


if __name__ == "__main__":
    process(apply="--apply" in sys.argv)
