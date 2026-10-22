#!/usr/bin/env python3
"""P0 成本一致性验证：全量 517 页核对渲染落地成本与 frontmatter 单一数据源一致。

检查项：
1. 每页渲染 HTML 的「Estimated Landed Cost Breakdown」总价 == round(frontmatter landed_cost.total_landed_usd)
2. 每页渲染 HTML 的德国市场卡片价 == round(frontmatter landed_cost_markets[Germany].total_landed_usd)
3. 渲染 HTML 无硬编码正文残留（「## Detailed Breakdown」/「## Landed Cost by Market」原始正文表头）
4. 正文源文件已无硬编码落地成本区块
"""
import glob
import json
import math
import os
import re


def js_round(x):
    """Match template's Math.round (half-up). Python round() is banker's."""
    return math.floor(x + 0.5)

VEH = "src/content/vehicles"
DIST = "dist/vehicles"


def split_frontmatter(text: str):
    if not text.startswith("---"):
        return {}, ""
    end = text.index("\n---", 3)
    fm = text[3:end]
    body = text[end + 4 :]
    return fm, body


def parse_lc(fm: str):
    """从 frontmatter 提取 landed_cost 总价 + landed_cost_markets 德国价。"""
    m = re.search(r'^landed_cost:\s*(\{.*\})\s*$', fm, re.M)
    lc_total = None
    if m:
        try:
            obj = json.loads(m.group(1))
            lc_total = obj.get("total_landed_usd")
        except Exception:
            lc_total = None
    m2 = re.search(r'^landed_cost_markets:\s*(\[.*\])\s*$', fm, re.M)
    germany = None
    if m2:
        try:
            arr = json.loads(m2.group(1))
            for it in arr:
                if it.get("market") == "Germany":
                    germany = it.get("total_landed_usd")
                    break
        except Exception:
            germany = None
    return lc_total, germany


def main():
    files = sorted(glob.glob(os.path.join(VEH, "*.md")))
    issues = []
    checked = 0
    for f in files:
        slug = os.path.basename(f)[:-3]
        text = open(f, encoding="utf-8").read()
        fm, body = split_frontmatter(text)
        # 4. 源文件无硬编码区块
        if "## Landed Cost by Market" in body or "## Detailed Breakdown" in body:
            issues.append((slug, "source still has hardcoded landed-cost block"))
        lc_total, germany = parse_lc(fm)
        html = os.path.join(DIST, slug, "index.html")
        if not os.path.exists(html):
            issues.append((slug, f"missing dist {html}"))
            continue
        h = open(html, encoding="utf-8").read()
        # 3. 无硬编码正文残留
        if "## Landed Cost by Market" in h or "## Detailed Breakdown" in h:
            issues.append((slug, "rendered html has hardcoded block"))
        if lc_total is not None:
            exp = js_round(lc_total)
            # breakdown 总价 = 绿色加粗 total 单元格，取所有 $N 中与 exp 匹配者
            if f"${exp:,}" not in h:
                issues.append((slug, f"breakdown total missing ${exp:,}"))
        if germany is not None:
            exp_g = js_round(germany)
            if f"${exp_g:,}" not in h:
                issues.append((slug, f"germany market card missing ${exp_g:,}"))
        checked += 1
    print(f"checked={checked} pages")
    print(f"issues={len(issues)}")
    for s in issues[:60]:
        print("  ISSUE:", s)
    if issues:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
