# EV Hub P0 Critical Fixes Report

> 日期：2026-09-17 ｜ 执行依据：P0 critical fix prompt（仅实施 P0，不涉及 P1/P2）
> 分支：fix/p0-data-integrity-2026-09-17（checkpoint 已建）

## Fixed（已修复）

| # | Issue | Cause | Location | Change | Validation |
|---|---|---|---|---|---|
| 1 | 首页/About/Brands 计数矛盾（58/315 vs 72/517） | 历史硬编码数字未随数据扩容更新 | `src/pages/index.astro` / `about.astro` / `brands/index.astro` | 品牌墙 58→72（补 14 个缺失品牌：Cowin/Dayun Yuanhang/Geometry/Hycan/JMC/Landian/Livan/Neta/Oshan/Sehol/Seres/Skywell/Venucia/Yudo）；标题 58→72；统计 315+→517、58→72 | build 788 页通过 |
| 2 | MG established=1029（无效年份） | 数据录入 typo | `src/data/brand-master.json` + `src/content/brands/mg.md` | 1029→1924（Wikipedia 查证：Morris Garages, Cecil Kimber, Oxford；站点正文自身亦写 "founded in Oxford, England, in 1924"） | validate:data 0 issues；72 品牌全量扫描仅此 1 个异常 |
| 3 | BYD Dolphin body_type=Sedan | 分类错误 | `vehicle-master.json` + `byd-dolphin.md` | Sedan→Hatchback（BYD 官方定位紧凑掀背，md description 自身写 "4,280 mm hatchback"） | 同源描述自证 |
| 4 | MG4 body_type=SUV | 分类错误 | `vehicle-master.json` + `mg-4.md` | SUV→Hatchback | 权威分类：MG4 为 C-segment 掀背 |
| 5 | Hongqi Guoya body_type=SUV | 分类错误 | `vehicle-master.json` + `hongqi-guoya.md` | SUV→Sedan（Wikipedia：full-size luxury car, 4-door sedan） | web 查证 |
| 6 | Wuling Jiachen body_type=SUV | 分类错误 | `vehicle-master.json` + `wuling-jiachen.md` | SUV→MPV（Wikipedia：minivan/5-door wagon） | web 查证 |
| 7 | ChangAn Nevo Lamore body_type=SUV（正文与 frontmatter 矛盾） | 分类错误 | `vehicle-master.json` + `changan-nevo-lamore.md` | SUV→Sedan | 权威分类 |
| 8 | 4 台 powertrain='Petrol'（非受控词表值） | 词表漂移 | `vehicle-master.json` + 4 个 md | Petrol→ICE ×3（lamore/x5-plus/jiachen）；Guoya→Unknown（V6/V8 + 160kW 电机结构不明确，不猜测） | validate:data powertrain 词表通过 |
| 9 | 车辆页 JSON-LD 虚构 offers（信息站不卖车） | schema 模板遗留 | `src/pages/vehicles/[slug].astro` | 移除 offers 块；信息型 Vehicle schema | build 通过 |
| 10 | JSON-LD fuelType 硬编码 'Electric'（PHEV/ICE 错误） | 模板硬编码 | 同上 | 按 powertrain 映射：BEV→Electric / PHEV→Plug-in hybrid / EREV→Extended-range electric / HEV→Hybrid / ICE→Gasoline / Unknown→省略 | build 通过 |
| 11 | 4 台非 BEV 车正文残留 "carries a X% countervailing duty"（与数据 CVD=0 矛盾） | 生成时未同步 | 4 个车辆 md | 改为 "applies the 10% standard tariff only — no countervailing duty applies to non-BEV/petrol powertrains" | 与 frontmatter landed_cost_markets 一致 |
| 12 | 关税数据无版本化结构（裸数字） | 结构缺失 | `src/data/tariffs.json` | 新增 `cvd_meta` 块：measure_type/powertrain_scope(BEV)/market_scope(EU)/legal_basis(EUR-Lex 2024/2754)/effective_from(2024-10-30)/status(active)/last_verified/source_url | 消费方零破坏（brand_cvd 数字映射保留） |
| 13 | 市场实体无 canonical code（任务 §14） | 字段缺失 | `src/data/market-master.json` | 30 市场全量加 `market_code`（ISO 3166-1 alpha-2） | validate:data 校验全部合法 |
| 14 | 3 个品牌缺 website/source_url | 数据缺失 | `brand-master.json` | jac/jac-refine→https://www.jac.com.cn/（HTTP 200 实测）；chery-new-energy→https://www.cheryinternational.com/（HTTP 200 实测） | 实测可访问 |
| 15 | mg.md model_count=2（实际 6 台） | 未同步 | `src/content/brands/mg.md` | 2→6 + Body types 更新 | 与 master vehicle_count 一致 |
| 16 | 无数据验证脚本 | 缺失 | `scripts/validate-data.mjs` + `package.json` | 新建可重复运行的 `npm run validate:data`（25 类检查） | 运行通过：0 issues |

## Not fixed（需人工决策）

| Issue | Reason |
|---|---|
| fast_charge='-' 占位（158 台） | 确定性占位符，渲染层已处理（显示 null）。数据层保留 '-' 作为「未知」语义，避免伪造数值。如需批量清空需人拍板 |
| data_reviewed 全部 false（517/517） | 诚实状态——未人工复核就保持 false。不应为通过校验而翻成 true |
| Hongqi Guoya powertrain=Unknown | V6/V8 汽油 + 160kW 电机的组合无法从公开源确定 HEV/PHEV 分类，按任务纪律标 Unknown 而非猜测 |
| entity-graph.json 中 chengguang-energy→wei-wang employs 关系带 NEEDS_REVIEW 标记 | 保留原样（既有诚实标记），不动 |

## Unknown（需权威源核实）

| 项 | 说明 |
|---|---|
| EU CVD 税率 2026-09 最新状态 | cvd_meta 记录基于 EUR-Lex 2024/2754 + 站点既有 brand_cvd（BYD 17%/Geely 18.8%/SAIC 35.3%/Tesla 7.8%/其他 20.7%），EUR-Lex 页面抓取被 JS 拦截未能全文复核——标记 last_verified=2026-09-15 沿用站点既有验证 |
| 部分品牌 established 年份未逐一人工核验 | 批量审计仅发现 MG 一个越界值；其余 71 个在 1800-2026 合法区间内，但未逐一手工对照官方史。validate:data 将持续监控 |

---

# P1+P2 数据/SEO 深度修复报告（2026-09-17 第二批）

> 执行依据：P1+P2 修复 prompt（用户已批准）｜ commit：见 git log ｜ 纪律：不改 URL/canonical/robots/sitemap 策略、不重写内容、不确定标 Unknown

## P1 完成（4/4）

| # | 项 | 变更 | 验证 |
|---|---|---|---|
| 1 | 价格语义规范化（§10） | vehicle-master 517 台全量加 `price_type: "China ex-factory price (MSRP)"`；content.config.ts schema 加 `price_type`（默认同值）；车辆页 specs 表新增 **Price basis** 行展示 | build 后 dist HTML 实测显示 "China ex-factory price (MSRP)"；validate 新增 price_type 检查通过。未虚构新价格 |
| 2 | 落地成本 confidence（§12） | 车辆页落地成本区渲染层新增 **Confidence: Medium**（官方 MSRP + 官方关税，运费/认证为固定估算 → 部分估算）+ **Last verified**（每车 data_updated，兜底 2026-09-15）。仅渲染层，md 数据零改动 | dist HTML 实测显示 Confidence/Last verified 行 |
| 3 | fast_charge 占位清理（§15） | 158 台 `fast_charge: "-"` → `null`（md frontmatter）；schema 改 `z.string().nullable().default(null)`；渲染层简化判断 | validate 新增回归检查（'-' 即 fail）通过；build 后全站无 '-' 占位显示（抽查原 158 台页面 0 处 Fast charge） |
| 4 | vehicle source 元数据继承（§8） | vehicle-master 517 台加 `source`/`source_url`，从 brand-master 品牌级来源继承（manufacturer specs；72 品牌 100% 覆盖），md data_source 字符串保留未动。**未逐车找官网规格页**（工作量大且易出错，按任务允许的继承策略） | validate 新增 source/source_url 检查通过 |

## P2 完成（4/4）

| # | 项 | 结果 |
|---|---|---|
| 5 | EU CVD 权威复核（§7） | **Unknown（抓取失败，按纪律保持现状）**。EUR-Lex 2024/2754 HTML/PDF 均被 AWS WAF challenge 拦截（curl 实测 `x-amzn-waf-action: challenge`），reader 代理 403，搜索 API 配额耗尽（Tavily 432）。cvd_meta 新增 `verification_status: "unknown"` + `verification_note`，**税率数字未动** |
| 6 | 索引安全质量门（§21） | 新增 `scripts/quality-gate.mjs`（npm run quality:gate）+ `docs/indexation-quality-gate.md`。五门槛：identity 517/517、brand 517/517、powertrain 516/517（Guoya Unknown）、specs 444/517（73 台缺失项，多为 ICE/PHEV 无 range/battery，如实保留 null）、source 517/517。**仅出报告，不自动 noindex**（无既有政策支持） |
| 7 | 全量 SEO 验证（§22-24, §28） | 新增 `scripts/seo-validation.mjs`（npm run seo:validate）。sitemap 786 URL 全部在 dist 存在（0 缺失）；65,328 条内链 0 断裂；抽样 10 车辆页+10 品牌页+5 blog+5 docs 关键数据全一致。结果追加 docs/seo-integrity-report.md |
| 8 | 全字段占位扫描（§15 扩展） | 新增 `scripts/placeholder-scan.mjs`（npm run placeholder:scan）。vehicle-master 全字段（含 variants）+ md frontmatter：9999 哨兵值/未来日期/负值/空串/placeholder 字样 → **0 异常**。结果追加 docs/data-quality-report.md |

## 最终验证

- `npm run validate:data`：✅ 0 issues
- `npm run build`：✅ 788 页通过（sitemap-index 正常生成）
- `npm run seo:validate`：✅ 0 issues
- `npm run quality:gate`：✅ 报告生成（73 条不完整记录清单）
- `npm run placeholder:scan`：✅ 0 异常

## 需人工决策项

1. **other cooperating CVD 税率**：站点值为 20.7%，公开报道常见的定稿值多为 20.8%（0.1pp 差异）。本次复核被 EUR-Lex 拦截无法权威确认，**数字未改**——建议人工复核后决定是否改 0.207→0.208（会影响 517 台落地成本计算）。
2. **specs 门 73 台缺失项**：多为 ICE/PHEV 车型无 range/battery 等 EV 专属字段（数据如实为 null）。如需索引完整性更高，需人工补数据。
3. **Guoya powertrain=Unknown**：延续 P0，需权威源判定 HEV/PHEV。
4. **CVD 2026-09 现行状态**：2024/2754 定稿税率沿用；若 2025-2026 有最低进口价谈判等新进展，需人工复核后更新 effective dates。
