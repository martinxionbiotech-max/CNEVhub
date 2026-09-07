#!/usr/bin/env python3
"""P0: Normalize brand/model casing in vehicle titles (and descriptions).

Fixes inconsistent display names: Byd->BYD, Gac->GAC, Jac->JAC, Mg->MG,
Nio->NIO, Saic->SAIC, Xpeng->XPENG, plus obvious all-caps model tokens
(HAN->Han, QIN->Qin, AIR->Air, DMI->DM-i, etc.).
"""
import re
import sys
from pathlib import Path

import yaml

VEHICLES = Path("src/content/vehicles")

# token -> canonical casing (applied word-by-word)
TOKEN_FIX = {
    "Byd": "BYD", "Gac": "GAC", "Jac": "JAC", "Mg": "MG", "Nio": "NIO",
    "Saic": "SAIC", "Xpeng": "XPENG",
    "HAN": "Han", "QIN": "Qin", "AIR": "Air", "HUA": "Hua", "XIAN": "Xian",
    "ZI": "Zi", "DMI": "DM-i", "PLUS": "Plus", "PRO": "Pro", "MAX": "Max",
    "NEW": "New", "ENERGE": "Energy", "YEP": "Yep",
}


def normalize_tokens(text: str) -> str:
    # split on spaces, fix each token
    return " ".join(TOKEN_FIX.get(w, w) for w in text.split(" "))


def process(apply: bool):
    changed = 0
    preview = []
    for path in sorted(VEHICLES.glob("*.md")):
        raw = path.read_text()
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.DOTALL)
        if not m:
            continue
        try:
            data = yaml.safe_load(m.group(1))
        except Exception:
            continue
        title = data.get("title") or ""
        desc = data.get("description") or ""
        new_title = normalize_tokens(title)
        new_desc = normalize_tokens(desc)

        if new_title == title and new_desc == desc:
            continue
        changed += 1
        if len(preview) < 12:
            preview.append((path.stem, title, new_title))
        if apply:
            new_raw = raw
            if new_title != title:
                new_raw = new_raw.replace(f'title: "{title}"', f'title: "{new_title}"', 1)
            if new_desc != desc:
                new_raw = new_raw.replace(f'description: "{desc}"', f'description: "{new_desc}"', 1)
            path.write_text(new_raw)

    print(f"files changed: {changed} | mode={'APPLY' if apply else 'PREVIEW'}")
    for stem, old, new in preview:
        print(f"  {stem}: \"{old}\" -> \"{new}\"")


if __name__ == "__main__":
    process(apply="--apply" in sys.argv)
