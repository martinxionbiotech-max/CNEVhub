#!/usr/bin/env python3
"""P0 成本一致性：移除 markdown 正文中硬编码的落地成本双渲染区块。

根因：517 款车型的 markdown 正文（frontmatter 之后）内嵌了「## Landed Cost by
Market」30 市场表 + 「## Detailed Breakdown — Germany」明细表两段硬编码文本，
与模板 `src/pages/vehicles/[slug].astro` 从 frontmatter（landed_cost +
landed_cost_markets）渲染的两块内容重复；且正文明细表在 fix_brand_cvd.py /
recompute_from_tariffs.py 更新 frontmatter 反补贴税率后未重新生成，导致同一页面
同一市场出现两套不一致数字（如 bestune-pony 正文 $12,043 vs frontmatter $12,130）。

修复：正文只保留 H1 + 简介 + ## Overview 散文，删除从「## Landed Cost by Market」
到文末的全部硬编码落地成本表格。frontmatter 成为单一数据源，模板成为单一渲染处。

幂等：重跑零 diff（正文已无该区块则跳过）。
"""
import glob
import os
import sys

ROOT = "src/content/vehicles"
FILES = sorted(glob.glob(os.path.join(ROOT, "*.md")))


def split_frontmatter(text: str):
    """返回 (frontmatter_raw, body)。frontmatter_raw 含首尾 --- 行。"""
    if not text.startswith("---"):
        return "", text
    end = text.index("\n---", 3)
    # 含开头的 --- 到结尾的 ---（含换行）
    fm_block = text[: end + 4]
    body = text[end + 4 :]
    return fm_block, body


MARKER = "## Landed Cost by Market"


def main() -> int:
    changed = 0
    skipped = 0
    for f in FILES:
        text = open(f, encoding="utf-8").read()
        fm, body = split_frontmatter(text)
        idx = body.find(MARKER)
        if idx == -1:
            skipped += 1
            continue
        # 保留区块前的 H1/简介/Overview，去掉硬编码落地成本表格
        new_body = body[:idx].rstrip() + "\n"
        new_text = fm + new_body
        if new_text != text:
            open(f, "w", encoding="utf-8").write(new_text)
            changed += 1
        else:
            skipped += 1
    print(f"changed={changed} skipped={skipped} total={len(FILES)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
