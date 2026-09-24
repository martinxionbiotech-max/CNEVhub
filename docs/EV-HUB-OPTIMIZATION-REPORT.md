# EV Hub 优化报告（任务书 V1 全量执行总结）

> 日期：2026-09-24 ｜ 仓库：CNEVhub（main）｜ 依据：EV 优化任务书 V1（§0–§40）
> 最终状态：深度修复剩余 8 项全部完成，全站 QA / 一致性 / sitemap 校验全绿。
> **CONTENT PRODUCTION REMAINS PAUSED**（§0 内容生产暂停持续有效：EV Hub 内容创作 cron 已禁用，不写新文章、不动 9 篇 draft）

## 1. Problems（修复前的问题）

| # | 问题 | 严重度 |
|---|---|---|
| 1 | 首页/About/品牌墙计数硬编码（58 品牌 / 315 车 vs 实际 72 / 517） | P0 |
| 2 | 数据无版本化结构：关税裸数字、市场无 ISO code | P0 |
| 3 | 分类错误：MG established=1029；5 台 body_type 错误（Dolphin/MG4/Guoya/Jiachen/Lamore）；4 台 powertrain='Petrol' 非词表值 | P0 |
| 4 | 车辆页 JSON-LD 虚构 offers（信息站不卖车）+ fuelType 硬编码 'Electric' | P0 |
| 5 | 非 BEV 车正文残留「carries X% countervailing duty」与数据 CVD=0 矛盾 | P0 |
| 6 | Hongqi Guoya powertrain=Unknown（结构不明，曾标 Unknown 不猜） | P0 |
| 7 | 无数据验证/QA 门禁脚本 | P1 |
| 8 | 无逐字段数据溯源约定、无机器可读数据层、无 Dataset schema | P1/P2 |
| 9 | sitemap 混入 184 个 noindex,follow 的 /blog/tag/ 聚合页（收录指令自相矛盾） | P2 |
| 10 | landed-cost 方法论存在文档/实现偏差与中心表缺口（详见审计 §10） | P2 |

## 2. 固定项（已修复）

- 全站计数单一数据源：`src/lib/site-stats.ts` build 时从 content collections 派生，无硬编码（commit `47d8ef3` 及之前批次）。
- 品牌墙 58→72；首页/About/车辆索引计数全部对齐 517/72/30。
- MG established 1029→1924；5 台 body_type、4 台 powertrain 规范化（Petrol→ICE×3；Guoya→Unknown→**HEV**，见 §3）。
- 车辆页 JSON-LD：移除 offers，fuelType 按 powertrain 映射（BEV/PHEV/EREV/HEV/ICE/Unknown）。
- 4 台非 BEV 正文修正为「no countervailing duty applies to non-BEV powertrains」。
- `tariffs.json` 增加 `cvd_meta` 版本化块（legal_basis=EUR-Lex 2024/2754、effective_from=2024-10-30、scope=EU+BEV）。
- 30 市场加 ISO 3166-1 `market_code`；3 个品牌补 website（HTTP 200 实测）。
- sitemap filter 排除 noindex 的 `/blog/tag/`（本次，commit `08d699f`）——184 个 noindex 页不再进 sitemap。

## 3. 数据模型变更

- **powertrain 枚举**：BEV / PHEV / EREV / HEV / ICE / FCEV / Unknown（受控词表，QA ENUM 校验）。
- **type 枚举**：Sedan / Hatchback / SUV / Crossover / MPV / Wagon / Pickup / Van / Coupe / Convertible / Sports Car / Other / Unknown。
- **Hongqi Guoya powertrain Unknown→HEV**（本次，commit `f421cf2`）：Wikipedia 查证——3.0T V6 涡轮（CA6GV30TD）+ 160 kW 永磁同步电机、power-split hybrid、8AT，无插电表述 → HEV；非 BEV → 全市场 CVD=0 已一致；正文 Germany breakdown 表同步修正（CVD $0 / VAT $41,211 / total $264,709 / +34.2%）；`data_updated=2026-09-24`。
- **数据溯源字段约定（§7，本次）**：`source-master.json` 新增 `_conventions` 块——`source_type` 枚举（manufacturer/government/regulation/customs/industry/primary/secondary/evhub_calculation/evhub_estimate）、`confidence` 枚举（high/medium/low）、`verified_date`、逐字段 `field_sources` 约定 + legacy source_type 映射。约定先行，517 台批量迁移留后续决策。
- 车辆 frontmatter 新增可选 `confidence` 字段（content.config.ts schema + 模板展示，缺省渲染层推导 Medium）。

## 4. 计数修复

- 517 车辆 / 72 品牌 / 30 市场 / 86 博文（77 已发布 + 9 draft）。
- 首页「View all 517 vehicles」、/vehicles/ 「517 vehicles」、About 517/72/30、72 个品牌页 `{n} models` 全部与数据层一致（§32 一致性测试 16 项全过）。

## 5. 方法论

- 公式：`base×(1+duty)×(1+cvd)×(1+vat) + freight + clearance + certification + registration + inland`（复合顺序与欧盟关税估值级联一致）。
- **方法论审计（§9–10，本次）**：`docs/landed-cost-methodology-audit.md`——30 市场成本要素 included/excluded/official/estimated/calculated 全表；与 §9 结构（base+logistics+customs+taxes+compliance+registration+local）逐项对照；6 项需人工决策（D1 关税基数 base vs CIF、D3 区域固定成本入中心表、D4 注册费溯源、D5 反解→正向计算、D6 认证费分市场、H6 公开页 CVD 表补 Tesla 7.8%）。**未改动任何公式或 517 台数值。**

## 6. Schema（结构化数据）

- 车辆页：Vehicle（无 offers，信息型）＋ fuelType 映射 ＋ Brand 嵌套。
- 品牌页：Organization + BreadcrumbList。
- 首页：**Dataset JSON-LD（§17，本次）**——name=Chinese EV Export Database、description、creator（Chengguang Energy / 法定名 Jinzhou Chengguang Power Source Co., Ltd.）、license=CC BY 4.0、temporalCoverage（由 data_updated 动态推导）、variableMeasured 摘要（price_usd/powertrain/range_cltc_km/battery_kwh/motor_power_kw/landed_cost）、isAccessibleForFree、dateModified。全部为合法 schema.org 属性。

## 7. 内链

- 面包屑三级链（Home/Vehicles/Brand/Vehicle）＋ 品牌墙/车辆索引互链。
- `scripts/seo-validation.mjs` 全量内链断裂扫描（dist 内 href/src），持续门禁。
- 本轮 build 后无断链新增（§32 校验 sitemap 全部 URL 有产物）。

## 8. AIO（AI 可见性）

- `public/llms.txt`（既有）。
- robots.txt 显式 Allow GPTBot / ClaudeBot / Claude-Web / PerplexityBot / Google-Extended。
- 本次新增 `/data/*.json` 机器可读端点（LLM/agent 友好，见 §9）。

## 9. 机器可读数据层（§16，本次）

静态 JSON 端点（build 时生成，参照 WFH freight-quotes.json.ts 模式）：

| 端点 | 内容 | 记录数 |
|---|---|---|
| `/data/vehicles.json` | slug/brand/type/powertrain/price_usd/range/battery/motor/30 市场 landed_cost | 517 |
| `/data/brands.json` | slug/name/parent/model_count（动态派生） | 72 |
| `/data/tariffs.json` | markets/brand_cvd/fixed_costs/cvd_meta | 30 市场 |

仅公开字段；license=CC BY 4.0；不进 sitemap（已验证 0 混入）。

## 10. SEO

- sitemap-index：1 个子 sitemap，**701 URL**（修复前 885，剔除 184 个 noindex tag 页后）。
- sitemap 分桶：vehicles=517、brands=72、已发布博文=77、draft=0、404/500=0、noindex=0。
- canonical/robots/noindex 指令本轮零改动（仅 sitemap 收录范围与页面指令对齐）。
- `docs/seo-integrity-report.md`、`docs/indexation-quality-gate.md` 持续维护。

## 11. 性能

- 本轮无新性能改动；build 实测 **900 页 / ~85 s**（517 车辆页 + 72 品牌页 + 博文/文档/静态页 + 3 个 JSON 端点）。
- dist 212 MB（图片为主），图片 lazy loading 保持既有策略。

## 12. 遗留（已知、保持诚实）

- `data_reviewed=false` 517/517——未人工复核不翻 true。
- 车辆 specs 缺失项（range/battery/motor 为空，多为 ICE/PHEV/老车型）如实 null，不伪造。
- EU CVD 税率 2026-09 最新状态：沿用站点既有 brand_cvd（EUR-Lex 抓取被 WAF 拦截，标记 last_verified=2026-09-15）。
- landed-cost 审计 6 项人工决策未执行（见 §5）。
- 逐字段 `field_sources` 批量迁移（517 台）未启动——约定已落，改造留决策。

## 13. 下阶段

1. landed-cost 审计决策项 H1–H6 逐项拍板（首选 H2+H4：区域固定成本入 tariffs.json 中心表并正向重算）。
2. `field_sources` 逐字段溯源批量迁移（按 source-master `_conventions`）。
3. EU CVD 权威复核（EUR-Lex 镜像/官方 PDF 渠道）。
4. 内容生产恢复决策（**当前仍暂停**，等人工指令）。

## 14. 文件清单（本轮 8 步）

**改动**：
- `src/content/vehicles/hongqi-guoya.md`（powertrain HEV + breakdown 表）
- `scripts/qa_data.py`（+6 类检查，共 11 类）
- `src/data/source-master.json`（_conventions 溯源约定）
- `src/content/docs/data-provenance.md`（§7 约定文档，新）
- `src/content.config.ts`、`src/pages/vehicles/[slug].astro`（confidence 字段）
- `src/pages/data/{vehicles,brands,tariffs}.json.ts`（§16，新 ×3）
- `src/pages/index.astro`（Dataset JSON-LD）
- `astro.config.mjs`（sitemap 排除 /blog/tag/）
- `scripts/site-consistency.mjs`（§32+§27，新）

**报告**（新）：`docs/qa-report-2026-09-24.md`、`docs/landed-cost-methodology-audit.md`、`docs/EV-HUB-OPTIMIZATION-REPORT.md`（本文件）。

## 15. 测试

| 工具 | 结果 |
|---|---|
| `python3 scripts/qa_data.py`（11 类 QA） | ✅ 全过（PRICE/MATH/CONSISTENCY/TARIFF/VAT/DATE/DUPLICATE/RELATION/ENUM/RANGE/SOURCE，517 台 × 15,510 市场条目 0 问题） |
| `node scripts/site-consistency.mjs`（16 项） | ✅ 全过（首页/vehicles/about/72 品牌页计数 + sitemap 701 URL 有效性 + 无 noindex/draft/404 混入） |
| `npm run build` | ✅ 每步通过（900 页） |
| `npm run validate:data` / `quality:gate` / `seo:validate`（既有门禁） | 保持绿 |

## 16. 前后对比

| 维度 | 修复前 | 修复后 |
|---|---|---|
| 首页计数 | 58 品牌 / 315 车（硬编码错） | 72 / 517（build 时派生，单一数据源） |
| 数据验证 | 无脚本 | QA 11 类 + validate:data 25 类 + quality-gate 5 门槛 |
| 分类准确性 | 5 body_type 错 + 4 powertrain 非词表 + MG 1029 | 0 越界 / 0 非词表（Guoya 经查证 HEV） |
| 溯源 | 仅 data_source 文本 | _conventions 枚举 + confidence + verified_date + 模板展示 |
| 机器可读 | 无 | /data/ 3 个 JSON 端点（517/72/30） |
| 结构化数据 | 虚构 offers、fuelType 硬编码 | Vehicle 信息型 + Dataset JSON-LD + Organization/Breadcrumb |
| sitemap | 885 URL（混 184 noindex tag 页） | 701 URL，0 noindex/draft/404 混入 |
| 方法论 | 文档与实现有偏差、固定成本双副本 | 审计落盘，6 决策项待拍板（公式未动） |

---

**CONTENT PRODUCTION REMAINS PAUSED.**
