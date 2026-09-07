#!/usr/bin/env python3
"""P1: Add a 'family' field linking model variants (Brand -> Model -> Variant).

Derives family by stripping powertrain/trim suffixes (DM I / DMI / EV / GT /
Touring / BEV) from the model name, grouping e.g. 'Seal 06 DM I', 'Seal 06 EV',
'Seal 06 GT' under family 'Seal 06'.
"""
import re
import sys
from pathlib import Path

import yaml

VEHICLES = Path("src/content/vehicles")

# Brand display names (canonical casing), matching normalized titles
BRAND_DISPLAY = {
    "aeolus": "Aeolus", "aion": "AION", "aito": "AITO", "arcfox": "Arcfox",
    "avatr": "Avatr", "baojun": "Baojun", "baw": "BAW", "bestune": "Bestune",
    "byd": "BYD", "changan": "Changan", "changan-nevo": "Changan Nevo",
    "chery": "Chery", "chery-fulwin": "Chery Fulwin", "chery-new-energy": "Chery New Energy",
    "deepal": "Deepal", "denza": "Denza", "dongfeng-e": "Dongfeng eπ",
    "dongfeng-nammi": "Dongfeng Nammi", "exeed": "Exeed", "fangchengbao": "Fangchengbao",
    "firefly": "Firefly", "forthing": "Forthing", "gac-motor": "GAC Motor",
    "geely": "Geely", "geely-galaxy": "Geely Galaxy", "haval": "Haval",
    "hongqi": "Hongqi", "hyptec": "Hyptec", "icaur": "iCAR", "im": "IM",
    "jac": "JAC", "jac-refine": "JAC Refine", "jac-yiwei": "JAC Yiwei",
    "jaecoo": "Jaecoo", "jetour": "Jetour", "kaicene": "Kaicene",
    "leapmotor": "Leapmotor", "li-auto": "Li Auto", "luxeed": "Luxeed",
    "lynk-co": "Lynk Co", "m-hero": "M-Hero", "maextro": "Maextro",
    "maxus": "Maxus", "mg": "MG", "nio": "NIO", "onvo": "Onvo", "ora": "Ora",
    "roewe": "Roewe", "saic": "SAIC", "stelato": "Stelato", "tank": "Tank",
    "voyah": "Voyah", "wey": "Wey", "wuling": "Wuling", "xiaomi": "Xiaomi",
    "xpeng": "XPENG", "yangwang": "Yangwang", "zeekr": "Zeekr",
}

# Powertrain/trim suffixes to strip (longest first)
SUFFIXES = [
    r"\s+DMI Touring$", r"\s+DM I$", r"\s+DM-i$", r"\s+DMI$", r"\s+DM$",
    r"\s+EV$", r"\s+BEV$", r"\s+GT$", r"\s+Touring$",
]


def family_of(title, brand):
    bdisp = BRAND_DISPLAY.get(brand)
    name = title
    if bdisp and name.lower().startswith(bdisp.lower()):
        name = name[len(bdisp):].strip()
    for pat in SUFFIXES:
        name = re.sub(pat, "", name, flags=re.IGNORECASE)
    return name.strip() or title


def process(apply: bool):
    changed = 0
    fams = {}
    for path in sorted(VEHICLES.glob("*.md")):
        raw = path.read_text()
        m = re.match(r"^---\n(.*?)\n---\n", raw, re.DOTALL)
        if not m:
            continue
        try:
            data = yaml.safe_load(m.group(1))
        except Exception:
            continue
        fam = family_of(data.get("title") or "", (data.get("brand") or "").lower())
        fams.setdefault(fam, []).append(path.stem)
        if "family:" in m.group(1):
            continue
        new_fm = m.group(1) + f'\nfamily: "{fam}"'
        new_raw = raw.replace(m.group(1), new_fm, 1)
        if new_raw != raw:
            changed += 1
            if apply:
                path.write_text(new_raw)

    # report families with >1 member (variant groups)
    multi = {k: v for k, v in fams.items() if len(v) > 1}
    print(f"files to tag: {changed} | variant families (>1 member): {len(multi)} | mode={'APPLY' if apply else 'PREVIEW'}")
    for fam, members in sorted(multi.items())[:15]:
        print(f"  family '{fam}': {members}")


if __name__ == "__main__":
    process(apply="--apply" in sys.argv)
