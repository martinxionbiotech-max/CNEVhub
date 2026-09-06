#!/usr/bin/env python3
"""Add a consistent 'Related reading' internal-linking section to each blog article.

Builds a hub-and-spoke structure: sticker-vs-landed-price is the hub; every
article links back to it and to its cluster siblings.
"""
import re
import sys
from pathlib import Path

BLOG = Path("src/content/blog")

TITLES = {
    "byd-countervailing-duty-landed-cost": "BYD's 17% Countervailing Duty",
    "saic-35-percent-countervailing-duty": "Why MG/SAIC Pays 35.3%",
    "geely-188-countervailing-duty": "Geely's 18.8% Countervailing Duty",
    "germany-netherlands-france-import-comparison": "Germany vs France vs Netherlands",
    "uae-saudi-arabia-import-comparison": "UAE vs Saudi Arabia",
    "australia-import-zero-duty": "Australia's Zero-Duty Market",
    "byd-volume-ev-landed-cost": "BYD's Volume EVs (Atto 3, Dolphin, Sealion)",
    "mg-budget-ev-tariff-paradox": "MG's Budget EVs and the Tariff Paradox",
    "wuling-leapmotor-microcar-import": "Wuling & Leapmotor Microcars",
    "xpeng-zeekr-premium-ev-landed-cost": "Xpeng G6 & Zeekr 001",
    "wvta-vs-single-vehicle-approval": "WVTA vs Single-Vehicle Approval",
    "ccs2-vs-gbt-charging": "CCS2 vs GB/T Charging",
    "lhd-vs-rhd-markets": "LHD vs RHD Markets",
    "cltc-vs-wltp-range": "CLTC vs WLTP Range",
    "sticker-vs-landed-price": "Why the Sticker Price Is Never the Landed Price",
    "fleet-buyer-margin-math": "Fleet Buyer's Margin Math",
}

HUB = "sticker-vs-landed-price"

RELATED = {
    "byd-countervailing-duty-landed-cost": ["saic-35-percent-countervailing-duty", "geely-188-countervailing-duty"],
    "saic-35-percent-countervailing-duty": ["byd-countervailing-duty-landed-cost", "geely-188-countervailing-duty"],
    "geely-188-countervailing-duty": ["byd-countervailing-duty-landed-cost", "saic-35-percent-countervailing-duty"],
    "germany-netherlands-france-import-comparison": ["uae-saudi-arabia-import-comparison", "australia-import-zero-duty"],
    "uae-saudi-arabia-import-comparison": ["germany-netherlands-france-import-comparison", "australia-import-zero-duty"],
    "australia-import-zero-duty": ["uae-saudi-arabia-import-comparison", "germany-netherlands-france-import-comparison"],
    "byd-volume-ev-landed-cost": ["mg-budget-ev-tariff-paradox", "wuling-leapmotor-microcar-import", "xpeng-zeekr-premium-ev-landed-cost"],
    "mg-budget-ev-tariff-paradox": ["byd-volume-ev-landed-cost", "wuling-leapmotor-microcar-import"],
    "wuling-leapmotor-microcar-import": ["mg-budget-ev-tariff-paradox", "byd-volume-ev-landed-cost"],
    "xpeng-zeekr-premium-ev-landed-cost": ["byd-volume-ev-landed-cost", "mg-budget-ev-tariff-paradox"],
    "wvta-vs-single-vehicle-approval": ["ccs2-vs-gbt-charging", "lhd-vs-rhd-markets"],
    "ccs2-vs-gbt-charging": ["wvta-vs-single-vehicle-approval", "lhd-vs-rhd-markets"],
    "lhd-vs-rhd-markets": ["wvta-vs-single-vehicle-approval", "ccs2-vs-gbt-charging"],
    "cltc-vs-wltp-range": ["fleet-buyer-margin-math"],
    "fleet-buyer-margin-math": ["cltc-vs-wltp-range"],
    # hub: links to everything (siblings)
    "sticker-vs-landed-price": ["cltc-vs-wltp-range", "fleet-buyer-margin-math", "byd-volume-ev-landed-cost", "mg-budget-ev-tariff-paradox", "xpeng-zeekr-premium-ev-landed-cost", "wuling-leapmotor-microcar-import"],
}


def build_section(slug: str) -> str:
    items = []
    # siblings first
    for s in RELATED.get(slug, []):
        items.append(f"- [{TITLES[s]}](/blog/{s}/)")
    # hub link (unless this IS the hub)
    if slug != HUB:
        items.append(f"- [{TITLES[HUB]}](/blog/{HUB}/)")
    return "\n## Related reading\n\n" + "\n".join(items) + "\n"


def process(apply: bool):
    changed = 0
    for path in sorted(BLOG.glob("*.md")):
        slug = path.stem
        if slug not in TITLES:
            continue
        raw = path.read_text()
        if "## Related reading" in raw:
            continue
        section = build_section(slug)
        # insert before "## Sources" (or append at end if no Sources section)
        if "## Sources" in raw:
            new_raw = raw.replace("## Sources", section + "\n## Sources", 1)
        else:
            new_raw = raw.rstrip() + "\n" + section
        if new_raw != raw:
            changed += 1
            if apply:
                path.write_text(new_raw)
    print(f"articles updated: {changed} | mode={'APPLY' if apply else 'PREVIEW'}")


if __name__ == "__main__":
    process(apply="--apply" in sys.argv)
