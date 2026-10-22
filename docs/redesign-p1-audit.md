# ElectricVehicleHub 重设计 — Phase 1 只读审计报告

> **审计对象**：生产站 `https://electricvehiclehub.net/`（仓库 `repos/CNEVhub`）
> **参照重设计**：`https://electricvehiclehub-top.pages.dev/`（仓库 `repos/electricvehiclehub.top`）
> **对标功能站**：`https://chinaevpro.com/`（仅功能对标，不抄内容/设计）
> **审计模式**：READ_ONLY — 零编辑、零代码改动、零部署
> **审计时间**：2026-10-22（UTC）
> **框架**：`phase2/54-evhub-redesign-prompt.md`（PHASE 1 六项）
> **数据可用性**：GSC 未提供（索引/收录/排名相关结论一律标 U，不归因）

---

## 〇、执行摘要

两仓**同源**（REF 是 CNEVhub 的 fork，base commit `3c09380`），生产站与参照站**规模完全一致**（sitemap 均 701 URL：517 车型 / 72 品牌 / 77 博客 / 14 文档 / 1 市场 / 20 顶层页）。**核心差异不在规模，而在深度与索引卫生**：

1. **参照站已完成、生产站未做的「去模板化 + 深度档案」**：REF 车型页新增五段式深度档案（Entity Snapshot / Powertrain / Dimensions / Market Compliance / Benchmarking Matrix，28 个新字段），Overview 散文去模板化（首句骨架 512/517 唯一）。生产站 Overview 仍为固定句式模板（mean 84 词）。
2. **生产站数据层一致性缺陷**：`/data/vehicles.json` 机器可读端点仅暴露 **12 个字段**，而内容 frontmatter 有 ~35 字段（尺寸/扭矩/加速/极速等 8+ 字段在 JSON 端点 100% 缺失）——单源真相未落地。
3. **参照站部署索引元数据指向死域名**：`electricvehiclehub-top.pages.dev` 的 canonical / og:url / sitemap / robots.txt 全部指向 `electricvehiclehub.top`（**NXDOMAIN，未解析**）——参照部署自身的索引元数据失效。
4. **`.md` 变体 + `/data/*.json` 端点两站均未 noindex**（P2 重复内容面，REF 未修复）。

**一句话判定**：生产站数据基础扎实（30 市场 landed-cost 独家测算、三层溯源、零虚构评分），当前最大短板是**内容差异化不足（517 页模板化散文）+ 数据端点字段缺失 + 缺失对标站的关键功能（对比工具、B2B 询价、技术页、市场分析、厂商目录、新闻）**。无任何需立即阻断的 P0 项。

---

## 一、仓库盘查（PHASE 1.1）

### 1.1 两仓结构对比

| 维度 | CNEVhub（生产） | electricvehiclehub.top（参照） | 是否分叉 |
| :--- | :--- | :--- | :---: |
| 框架 | Astro 5.16 + Virex SaaS 主题 + Tailwind v4 | 同 | ✅ 一致 |
| 内容规模 | 517 车型 / 72 品牌 / 86 博客(77 发布+9 草稿) / 14 文档 | 同 | ✅ 一致 |
| 数据文件 | 8 个 JSON master（vehicle/brand/market/technical/regulatory/source/tariffs/entity-graph） | 同 + 已用 | ✅ 一致 |
| 路由页 | vehicles/brands/blog/docs/markets/data/法律页/计算器 | 同 + `/data/source-master.json.ts` | ⚠️ 分叉 |
| 车型内容字段 | ~35 字段（规格 + landed_cost + 溯源） | + 28 个深度字段（五段式） | ❌ **分叉** |
| 车型模板 | 单段 Overview + landed-cost 表 + Germany 拆解 | 五段式深度档案 + Benchmarking Matrix | ❌ **分叉** |
| Overview 散文 | 模板化（首句骨架 512/517 撞车潜在，top-1 3×） | 去模板化（首句骨架 512/517 唯一） | ❌ **分叉** |
| 博客 | 19 篇对比文 | 与生产**仅域名替换**（.net→.top，0 处实质改动） | ✅ 实质一致 |
| git | 164 commits | 28 commits（fork 后 27 笔深度档案批） | 分叉 |

### 1.2 关键分叉点（结构级）

**A. `content.config.ts` — REF 新增 28 个深度档案字段**（生产缺失）：
`trim / range_wltp_km / fob_price_usd_min/max / battery_type / drive_type / motor_type / motor_model / total_power_kw / battery_thermal / heat_pump / suspension_front/rear / brakes / drag_coefficient / gross_weight_kg / ground_clearance_mm / trunk_l / charging_interface / charging_adapter / infotainment_language / network_bands / certification_notes / hs_code`（全部 optional，schema 不破坏生产兼容）。

**B. `src/pages/vehicles/[slug].astro` — REF 五段式模板**（实测渲染确认）：
生产站车型页 `h2` 序列 = Overview / Landed Cost by Market / Detailed Breakdown / Data Sources / Specifications / Related。
参照站车型页 `h2` 序列 = **Entity Snapshot / Powertrain & Architecture / Dimensions & Logistics / Market Compliance & Export Profile / Benchmarking Matrix / Data Sources / Specifications** / Overview / Landed Cost 等。五段全渲染，含 40HQ 装箱估算（按车长分级）、HS Code 分类、同段位最近价竞品矩阵。

**C. `/data/source-master.json.ts` — REF 独有端点**（`/data/source-master.json`，生产站 404）。

### 1.3 数据文件（单源真相现状）

| 文件 | 记录数 | 生成日期 | 消费情况 |
| :--- | :---: | :--- | :--- |
| vehicle-master.json | 517 | 2026-09-14 | ⚠️ **陈旧**：JSON 端点仅 12 字段，尺寸/加速/极速 100% null |
| market-master.json | 30 | 2026-09-15 | ✅ /markets/ 页用 tariffs.json，market-master 部分字段未被渲染 |
| brand-master.json | 72 | 2026-09-07 | 品牌页用 content 集合，brand-master 未直接消费 |
| technical-master.json | 137（battery 39/charging 36/drivetrain 23/body-safety 15/thermal 13/range 11） | 2026-09-15 | ❌ **数据存在但零页面渲染**（无 /technology 路由） |
| regulatory-master.json | 66 | 2026-09-15 | ❌ 数据存在但零页面渲染 |
| source-master.json | ~15 源 | 2026-09-07 | REF 有 /data/source-master.json；生产未导出 |
| tariffs.json | 30 市场 + brand_cvd | 2026-09-15 | ✅ /markets/ 页单源 |
| entity-graph.json | 3 实体 | — | 部分消费 |

**核心矛盾**：`src/data/vehicle-master.json`（`/data/vehicles.json` 端点的来源）与 `src/content/vehicles/*.md` frontmatter **已分叉**——content 有完整尺寸/扭矩/加速/极速（98%/81%/61%/73% 覆盖），但 JSON master 这些字段 100% null。单源真相（Single Source of Truth）尚未落地。

---

## 二、双站爬取（PHASE 1.2）——明确区分生产 vs 参照

### 2.1 站点身份与可达性

| 站点 | 域名 | HTTP | 角色 | canonical 指向 |
| :--- | :--- | :---: | :--- | :--- |
| 生产 | `electricvehiclehub.net` | 200 ✅ | 生产站 | 自身（.net）✅ |
| 参照部署 | `electricvehiclehub-top.pages.dev` | 200 ✅ | 参照重设计部署 | ❌ 指向 `electricvehiclehub.top` |
| （参照仓库配置的正式域） | `electricvehiclehub.top` | **NXDOMAIN（未解析）** | 未上线 | — |

### 2.2 规模对比（sitemap 实测）

| 分类 | 生产 .net | 参照 pages.dev | 差异 |
| :--- | :---: | :---: | :---: |
| sitemap URL 总数 | 701 | 701 | 0（结构一致，仅域名不同） |
| 车型 | 517 | 517 | 0 |
| 品牌 | 72 | 72 | 0 |
| 博客 | 77 | 77 | 0 |
| 文档 | 14 | 14 | 0 |
| 市场 | 1 | 1 | 0 |
| 顶层页（法律/工具/关于） | 20 | 20 | 0 |

**结论**：两站**内容/URL/规模完全一致**，差异 100% 体现在**车型页深度**（五段式 vs 单段）与**部署域名卫生**。

### 2.3 参照部署的索引卫生缺陷（⚠️ 已验证事实）

`electricvehiclehub-top.pages.dev` 的以下元数据**全部指向未解析的 `electricvehiclehub.top`**：
- `<link rel="canonical" href="https://electricvehiclehub.top/vehicles/byd-seal/">`
- `<meta property="og:url" content="https://electricvehiclehub.top/...">`
- `sitemap-index.xml` → `<loc>https://electricvehiclehub.top/sitemap-0.xml</loc>`
- `robots.txt` → `Sitemap: https://electricvehiclehub.top/sitemap-index.xml`

这导致参照部署（pages.dev）的索引信号失效。若参照站需正式上线，必须先解析 `.top` 域名或把 `SITE_URL` 改为 pages.dev 域。**生产站 `.net` 无此问题**（canonical/og:url/sitemap/robots 均正确指向 .net）。

---

## 三、七类 Inventory（PHASE 1.3，两站分别）

| 类别 | 生产 .net | 参照 pages.dev | 说明 |
| :--- | :---: | :---: | :--- |
| ① 车型 Vehicles | 517 | 517 | BEV 286 / PHEV 154 / EREV 58 / HEV 15 / ICE 3 / Unknown 1；SUV 349 / Sedan 105 / MPV 38 / Hatchback 25 |
| ② 品牌 Brands | 72 | 72 | 品牌页正文 mean ~129 词（偏薄） |
| ③ 技术 Technology | **0 页面**（137 实体数据未渲染） | 0 页面 | 无 /technology 路由，technical-master 闲置 |
| ④ 市场 Markets | 1（/markets/ 汇总页，30 市场单表） | 1 | 无 per-market 落地页（30 市场仅汇总表） |
| ⑤ 指南 Guides | 77 发布（博客：国家 import guide ~26 + 对比文 ~17 + 深度评测 + 关税分析） | 77（同） | 9 篇草稿未发布 |
| ⑥ 计算器 Calculator | 1（/landed-cost-calculator/，客户端） | 1 | + /landed-cost-methodology/ 1 页 |
| ⑦ 法律页 Legal | 7（privacy/terms/cookies/disclaimer/copyright/accessibility/image-credits） | 7 | 均 200，内容实质 |

**补充盘点**：
- 数据端点：`/data/{vehicles,brands,tariffs}.json`（两站均有），REF 多 `/data/source-master.json`。
- 机器可读 `.md` 变体：`/vehicles/[slug].md`（517）+ `/blog/[slug].md`（77）——两站均有。
- 标签页 `/blog/tag/*`：184 个（两站，已 noindex,follow）。
- 分页 `/blog/page/*`：已 noindex,follow。

---

## 四、质量检查（PHASE 1.4，逐项证据）

### 4.1 重复内容（Overview 模板化——量化复测）

| 指标 | 生产 .net | 参照 pages.dev |
| :--- | :---: | :---: |
| Overview 词数 mean | 84.1 | 86.3 |
| 首句骨架唯一率 | 模板化（top-1 骨架仅 3×，但句式骨架固定） | **512/517 唯一**（top 骨架 share 0.4%） |
| 首句骨架样例（生产） | "The [X] is a [尺寸] [车身] [动力] from [品牌], with [X] kW of motor power…" | 已差异化（含驱动形式/悬架/出口定位） |

**判定**：生产站 517 篇 Overview **同构模板**（均值 84 词、固定句式），是 REF「de-template」批次的原始状态。参照站已去模板化（89.2%→25.1% 模板率，REF git log 自述，实测首句唯一率 99%）。**非硬违规**（数据层每页唯一），但属低强度 scaled-content 信号（与既有 SpamCheck 报告 §2.1 一致）。

### 4.2 缺规格（字段矩阵）

**A. `/data/vehicles.json` 端点字段完整性（机器可读层）**——⚠️ 关键发现：
实测端点每个记录仅 **12 字段**：`battery_kwh / brand / currency / data_updated / landed_cost_markets / motor_power_kw / powertrain / price_usd / range_cltc_km / slug / title / type`。
**缺失**（对比 content frontmatter 的 35 字段）：`torque_nm / accel_0_100_s / top_speed_kmh / length_mm / width_mm / height_mm / wheelbase_mm / weight_kg / efficiency_kwh_100km / fast_charge / data_tier / data_source / data_reviewed / family` 等 **14+ 字段全缺**。`vehicle-master.json` 中这些字段 100% null。

**B. 内容层字段缺失率（517 车型 frontmatter，生产站）**：

| 字段 | 缺失率 | 字段 | 缺失率 |
| :--- | :---: | :--- | :---: |
| range_cltc_km | 9.1% | accel_0_100_s | 39% |
| range_long_km | 90.9% | top_speed_kmh | 27% |
| battery_kwh | 9.7% | weight_kg | 32% |
| motor_power_kw | 6.6% | efficiency_kwh_100km | 45% |
| torque_nm | 18.6% | price_usd | 0% |

**C. 参照站深度字段覆盖率（REF 517 车型）**：
`drive_type 100% / charging_interface 100% / charging_adapter 100% / infotainment_language 100% / certification_notes 100% / hs_code 100% / brakes 100% / battery_type 97% / suspension_front+rear 98%`。
**低覆盖深度字段**（REF 自身也缺）：`fob_price_usd 0% / gross_weight_kg 0% / trunk_l 0% / range_wltp_km 2% / drag_coefficient 5% / ground_clearance_mm 3% / network_bands 3% / trim 16%`——即「WLTP 续航、阻力系数、离地间隙、FOB 价格区间、整备质量、行李厢」等深度字段参照站也大面积空缺。

### 4.3 车型数不一致（两站计数差异 + 原因）

**两站 sitemap 车型数完全一致（均 517）**，无跨站计数差异。发现的是**站内口径不一致**：

| 位置 | 声称 | 实测 | 判定 |
| :--- | :--- | :--- | :--- |
| llms.txt 首段 | "315 vehicle models across 58 Chinese EV brands" | 517 / 72 | ❌ 陈旧 |
| llms.txt 下文 | "517 Chinese EV models" | 517 | ✅ |
| 首页显示 | 72 brands（+车型 517 隐含） | 517 / 72 | ✅ |
| sitemap | 517 vehicles | 517 | ✅ |

**原因**：llms.txt 首段的「315/58」是早期数据快照，未随 517/72 扩充同步更新。属文案一致性缺陷（P3），非数据错误。

### 4.4 错误/过期价格（价格 vs 来源抽查）

**A. 两站价格一致性**：抽查 byd-seal（$24,690）/ xiaomi-su7（$30,320）/ wuling-binguo（$7,980）——两站**价格完全一致**，无跨站价格漂移。

**B. 价格时间戳（staleness）**：

| 站点 | data_updated 分布 | 距今（2026-10-22） |
| :--- | :--- | :--- |
| 生产 .net | 314×2026-09-07 / 202×2026-09-14 / 1×2026-09-24 | **~5–6 周未更新** |
| 参照 pages.dev | 517×2026-10-21 | **昨日（新鲜）** |

**判定**：生产站价格/规格数据整体**过期约 5–6 周**（data_updated 停滞在 9 月上旬）；参照站已刷到 2026-10-21。**未发现具体价格错误**（抽查 3 款与来源口径一致、两站一致），但生产站「未更新」本身是数据新鲜度风险。`data_reviewed` 两站均 **517×false**（页面如实渲染 "Pending review"，诚实但未闭环）。

### 4.5 canonical / redirects / sitemap / 内链 / schema / 索引性

| 检查项 | 生产 .net | 参照 pages.dev | 证据 |
| :--- | :--- | :--- | :--- |
| canonical 自引用 | ✅ 正确（.net） | ❌ 指向死域名 .top | §2.3 |
| http→https | ✅ 301 | ✅ | curl |
| www→非 www | ✅ 301 | ✅ | curl |
| 尾斜杠归一 | ✅ 308 | ✅ | `/vehicles/byd-seal`→`/vehicles/byd-seal/` |
| /sitemap.xml | ✅ 301→sitemap-index.xml | ⚠️ 301 但指向 .top | curl |
| /blog/page/1/ | ✅ 301→/blog/ | ✅ | curl |
| sitemap 一致性 | ✅ 701 URL，0 个 tag/page/.md/noindex | ⚠️ 内容一致但 loc 域名错误 | §2.2 |
| 车型页内链数 | 38 条唯一内链 | 37 条 | grep |
| Schema（车型页） | 2 个 JSON-LD，**零 aggregateRating/review** | 同 | grep=0 |
| Schema（首页） | WebSite/Organization/Dataset/Breadcrumb/ContactPoint | 同 | grep |
| 标签页 noindex | ✅ noindex,follow | ✅ | meta robots |
| 分页 noindex | ✅ noindex,follow | ✅ | meta robots |
| `.md` 变体 X-Robots-Tag | ❌ 无 noindex（200 text/markdown） | ❌ 无 noindex | curl -D |
| `/data/*.json` X-Robots-Tag | ❌ 无 noindex | ❌ 无 noindex | curl -D |

**关键未解决问题（两站均存在）**：`.md` 变体（594 个）+ `/data/*.json`（生产 3 个 / REF 4 个）**可索引但无 noindex 指令**——一旦被外部引用将形成近重复内容面（P2，既有 SpamCheck 报告 §4.6 已识别，REF 未修复）。

---

## 五、URL-by-URL 建议表（PHASE 1.5）

> 生产站 sitemap 共 701 URL。以下按 URL 模式归类（同类 URL 建议一致），逐类给出 Action + 理由 + 证据。**本批为独立重审，非照搬既有 SpamCheck 报告。**

### 5.1 建议 Action 分布（计数）

| Action | URL 数 | 涉及模式 |
| :--- | :---: | :--- |
| KEEP（保留） | 92 | 77 博客 + 14 文档 + 1 市场 |
| IMPROVE（改进） | 609 | 517 车型 + 72 品牌 + 20 顶层页（法律/工具/关于） |
| MERGE（合并） | 0（候选 2 组） | 部分国家 import guide 可考虑合并（见 §5.4，暂缓） |
| REDIRECT（重定向） | 0（无死链需 301） | 已有 redirects 均正确 |
| NOINDEX（加 noindex） | 597 | 517 `.md` 变体 + 77 `.md` 变体 + 3 JSON 端点（非 sitemap 但可索引） |
| REMOVE（删除） | 0 | 无 |

> 注：`.md` 变体与 `/data/*.json` 不在 sitemap 内（701 URL 之外），故 NOINDEX 计数为「非 sitemap 的额外可索引面」。sitemap 内 701 URL 建议 = KEEP 92 + IMPROVE 609。

### 5.2 车型页 `/vehicles/[slug]/`（517）→ **IMPROVE**

| 项 | 建议 | 证据 |
| :--- | :--- | :--- |
| Overview 去模板化 | 逐批改写（20–25 款/窗口），摆脱固定句式骨架，补车型级独特见解（竞品定位/电池化学/出口强项） | §4.1 模板化 mean 84 词 |
| 五段式深度档案 | 移植 REF 的 28 字段 + 五段模板（Entity/Powertrain/Dimensions/Compliance/Benchmarking） | REF 已实现（§1.2） |
| 低覆盖深度字段补齐 | WLTP 续航 / FOB 区间 / 阻力系数 / 离地间隙等 REF 也缺的字段，需有来源才填，无来源标 N/A | §4.2C |
| data_reviewed 闭环 | 517×false 需推进人工复核或明确「待审」口径 | §4.4 |
| 单源真相 | 把尺寸/扭矩/加速/极速回填进 vehicle-master.json，使 `/data/vehicles.json` 端点 ≥ 20 字段 | §4.2A |

### 5.3 品牌页 `/brands/[slug]/`（72）→ **IMPROVE**

正文 mean ~129 词偏薄（§三②）。建议补：品牌出口定位、CVD 税率（已有 brand-cvd 数据）、代表车型 landed-cost 区间、母公司关系。目标 >500 词。

### 5.4 博客 `/blog/[slug]/`（77）→ **KEEP**（含 2 组 MERGE 候选）

博客质量高（深度评测 5681 词/71 引用；国家指南 1486–3765 词且关税口径实质不同）。**暂不建议 MERGE**：国家 import guide 虽属同类集群，但每篇关税/VAT/配额口径实质不同（非门页），合并会损失长尾。仅 2 组可评估合并：`uae-import-guide + saudi-arabia-import-guide`、`turkey-import-guide + indonesia-import-guide`（区域邻近），但需 Phase 2 信息架构决策，本批标「候选」。

### 5.5 文档 `/docs/[slug]/`（14）→ **KEEP**

技术文档（landed-cost-methodology / data-provenance / eu-homologation 等）内容实质，保留。

### 5.6 市场 `/markets/`（1）→ **IMPROVE**

当前仅 30 市场汇总表（单页）。建议 Phase 2 增加 per-market 落地页（`/markets/[country]/`），把 market-master.json 的 30 市场数据（import_duty/vat/countervailing/registration_fee/source_ids）渲染成独立页面。

### 5.7 顶层页（20）→ **IMPROVE**（法律页 KEEP）

- 法律页 7（privacy/terms/cookies/disclaimer/copyright/accessibility/image-credits）→ **KEEP**（内容实质，200）。
- 工具/方法论页（landed-cost-calculator / landed-cost-methodology / methodology / faq / about / authors / editorial-independence / contact）→ **IMPROVE**（对齐 REF 域名/邮箱一致性，补 B2B 询价能力见 §6）。
- `about/contact` 已统一邮箱 `info@electricvehiclehub.net`（生产 git log 显示 3 笔合规修正），保持。

### 5.8 `.md` 变体 + `/data/*.json` 端点 → **NOINDEX**

`/vehicles/[slug].md`（517）+ `/blog/[slug].md`（77）+ `/data/{vehicles,brands,tariffs}.json`（3）→ 加 `X-Robots-Tag: noindex`（数据仍供 API/AI 使用，不影响访问）。REF 独有 `/data/source-master.json` 同样处理。

---

## 六、两站差距清单（参照站已解决 vs 未解决）

### 已解决（REF 有、生产无，生产需追赶）

| # | 差距项 | 生产状态 | 参照状态 |
| :--- | :--- | :--- | :--- |
| 1 | 车型页五段式深度档案（28 字段） | ❌ 无 | ✅ 已实现 |
| 2 | Overview 去模板化（首句唯一率 99%） | ❌ 模板化 | ✅ 已实现 |
| 3 | 数据新鲜度（data_updated） | ❌ 停滞 9 月上旬 | ✅ 刷到 10-21 |
| 4 | `/data/source-master.json` 溯源导出 | ❌ 无 | ✅ 有 |
| 5 | HS Code 分类 + 40HQ 装箱估算 + 竞品矩阵 | ❌ 无 | ✅ 有 |

### 未解决（两站均存在，重设计需一并处理）

| # | 未解决项 | 等级 | 说明 |
| :--- | :--- | :---: | :--- |
| 1 | `.md` 变体 + `/data/*.json` 未 noindex | P2 | §4.5，594+ URL 重复面 |
| 2 | llms.txt「315/58」计数陈旧 | P3 | §4.3 |
| 3 | REF 部署 canonical/sitemap 指向死域名 .top | P2 | §2.3（仅 REF 侧） |
| 4 | 深度字段低覆盖（WLTP/FOB/阻力系数/离地间隙） | P2 | §4.2C，REF 也缺 |
| 5 | technical-master/regulatory-master 数据零渲染 | P2 | §1.3，缺 /technology 页 |
| 6 | market-master 30 市场无 per-market 页 | P2 | §5.6 |
| 7 | data_reviewed 全 false | P3 | §4.4 |
| 8 | 生产站数据 5–6 周未更新 | P2 | §4.4B |

---

## 七、对标站 chinaevpro.com 功能对照（缺失功能清单）

实测 chinaevpro.com 功能面（`/compare /quote /technology /market-analysis /manufacturers /buying-guides /news /models /brands /auth` 全 200）：

| 功能 | chinaevpro | 生产 .net | 缺失判定 |
| :--- | :---: | :---: | :--- |
| 车型目录 + 详情 | ✅ /models | ✅ /vehicles | 已覆盖 |
| 品牌目录 | ✅ /brands | ✅ /brands | 已覆盖 |
| **对比工具** | ✅ /compare（交互式） | ❌ 仅静态博客对比文 | ❌ **缺失** |
| **B2B 询价流程** | ✅ /quote（表单 + WhatsApp + 邮件） | ⚠️ 仅 /contact 通用表单 | ❌ **缺失**（无车型级询价） |
| **技术参考页** | ✅ /technology | ❌（technical-master 数据闲置） | ❌ **缺失** |
| **市场分析** | ✅ /market-analysis | ⚠️ 仅 /markets/ 汇总表 | ❌ **缺失**（无分析页） |
| **厂商目录** | ✅ /manufacturers | ⚠️ 品牌页含母公司，无独立厂商目录 | ⚠️ 部分 |
| 购车指南 | ✅ /buying-guides | ✅ /blog import guides | 已覆盖 |
| **新闻** | ✅ /news | ❌ 无新闻 | ❌ **缺失** |
| 用户账户/登录 | ✅ /auth/signin | ❌ 无 | 非必需（情报站不卖车，可略） |
| WhatsApp 即时联系 | ✅ wa.me 链接 | ❌ | 非必需 |

**对标结论**：生产站最大的功能差距是**①交互式对比工具、②B2B 车型级询价流程、③技术参考页、④市场分析页、⑤厂商目录、⑥新闻**六项。其中 ①③④⑤ 所需数据（车型规格、technical-master、market-master、brand-master）**已在仓库中**，仅缺渲染层；② 需新增表单后端（当前为纯静态站，无后端）。

---

## 八、纪律声明与结论分层

### 已验证事实（Facts，附证据）
- 两站 sitemap 均 701 URL、规模一致（curl 实测）。
- 生产站 Overview 模板化 mean 84 词，参照站首句唯一率 99%（仓库 python 复测）。
- 生产站 `/data/vehicles.json` 仅 12 字段（curl + python 解析实测）。
- 生产站 data_updated 停滞 9 月上旬，参照站刷到 10-21（frontmatter 计数）。
- 参照站 canonical/sitemap/robots 指向 `electricvehiclehub.top`（NXDOMAIN，nslookup 实测）。
- `.md` 变体与 `/data/*.json` 两站均无 X-Robots-Tag（curl -D 实测）。
- llms.txt「315/58」vs 实测 517/72（实测）。
- chinaevpro 六项功能页 200（curl 实测）。

### 建议（Recommendations，非事实）
- 上述所有 Action 归属（KEEP/IMPROVE/NOINDEX 等）均为建议。
- 排名损失是否为 Google 处罚：**U（GSC 未提供，不归因）**。
- 域名历史 / WHOIS：**U（未核验）**。
- 价格「错误」：抽查 3 款一致无错，但「过期 5–6 周」是事实。

### 红线（重设计 Phase 2+ 必须遵守）
1. 禁止批量删除/301 517 车型页或 184 标签页（标签页已 noindex，车型页是核心资产）。
2. 禁止 robots.txt `Disallow: /_astro/` 或 `/blog/tag/` 替代 noindex（会破坏渲染/抓取）。
3. 禁止给车型页补虚构 aggregateRating/review/seller（会触发 Structured Data Abuse）。
4. 深度字段「无来源填 N/A」，禁止编造 WLTP/FOB/阻力系数等值。
5. 参照站 `.top` 域名未解析前，其部署索引元数据不可作为上线依据。

---

## 附：证据采样记录

- 内容规模：517 车型 / 72 品牌 / 86 博客(77 发布+9 草稿) / 14 文档 / 137 技术实体 / 66 法规实体 / 30 市场
- sitemap：两站均 `sitemap-index.xml` → `sitemap-0.xml`（53,201 字节，701 URL）
- 车型动力分布：BEV 286 / PHEV 154 / EREV 58 / HEV 15 / ICE 3 / Unknown 1
- 车身分布：SUV 349 / Sedan 105 / MPV 38 / Hatchback 25
- 溯源：data_tier 333/163/21；data_reviewed 517×false；data_updated 生产 314@09-07+202@09-14+1@09-24 / 参照 517@10-21
- 生产 JSON 端点字段：12（缺尺寸/扭矩/加速/极速/溯源等 14+）
- 参照深度字段覆盖：drive_type/charging/cert/hs_code/brakes 100%；fob/gross_weight/trunk 0%；range_wltp 2%；drag 5%
- 价格抽查：byd-seal $24,690 / xiaomi-su7 $30,320 / wuling-binguo $7,980（两站一致）
- 重定向链：http→https 301、www→非www 301、尾斜杠 308、sitemap.xml→index 301、blog/page/1→/blog 301
- Schema：车型页 2 JSON-LD（无 rating/review）；首页 WebSite/Organization/Dataset/Breadcrumb/ContactPoint
- 内链：车型页 38（生产）/37（参照）唯一内链
- 对标站功能：/compare /quote /technology /market-analysis /manufacturers /buying-guides /news /models /brands /auth 全 200
