# ElectricVehicleHub 重设计 — Phase 2 信息架构设计

> **文档类型**：纯设计交付（Information Architecture）— 零代码改动、零生产部署
> **对象**：生产站 `https://electricvehiclehub.net/`（仓库 `repos/CNEVhub`，`main` @ `058ccbb`）
> **参照重设计**：`https://electricvehiclehub-top.pages.dev/`（功能对标，不抄内容/设计）
> **对标功能站**：`https://chinaevpro.com/`（仅功能对标）
> **前置依赖**：`docs/redesign-p1-audit.md`（Phase 1 只读审计，两站同源分叉 + URL 建议表）
> **框架**：`phase2/54-evhub-redesign-prompt.md`（PHASE 2 信息架构 + PHASE 6 小步交付纪律）
> **时间**：2026-10-22（UTC）
> **纪律声明**：本文档所有「迁移/新建/归属」均为**设计建议**，不包含任何已执行的代码改动。数据可用性沿用 P1：GSC 未提供，排名/收录相关结论标 U，不归因。

---

## 〇、设计原则与红线（先于一切）

1. **保留有价值的 URL**：517 车型页 + 72 品牌页 + 77 博客 + 14 文档 + 法律页 7 均为核心资产，**默认 KEEP**。任何 URL 变更必须有「一对一 301 目标」，**无目标不迁**（PHASE 5 红线）。
2. **小步交付**：本 Phase 只交付架构图 + 映射表 + schema 表 + P3 预告清单。所有「新建模块」仅登记 URL 与模板归属，**不在本 Phase 落地**。
3. **数据已存在优先渲染，不新增数据采集**：九模块中 ①③④⑤ 所需数据（车型规格、technical-master 137 实体、market-master 30 市场、brand-master 72 品牌、regulatory-master 66 法规）**已在仓库**，缺的只是渲染层（P1 §七结论）。
4. **零虚构**：深度字段无来源标 N/A，禁止编造 WLTP/FOB/阻力系数等值；禁止给车型页补虚构 aggregateRating/review/seller（P1 §八红线 3、4）。
5. **对标不抄**：chinaevpro 仅作功能清单参照，URL 结构、文案、设计一律自行设计。

---

## 一、九模块信息架构总表（核心交付）

> 九模块 = 车型目录与档案 / 品牌目录与档案 / 对比 / 三电技术 / 国家进口情报 / 购买指南 / 原创研究 / landed-cost 计算器 / B2B 询盘流程。

| # | 模块 | 目标 URL 结构 | 页面类型 | 独立用户意图声明 | 模板归属 | 现状 → 建议（P1 对位） |
| :--: | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **车型目录与档案** | `/vehicles/` + `/vehicles/[slug]/` | 目录页 + 详情页 | 目录：「按价格/动力/车身/品牌检索 517 款可出口中国 EV」；详情：「某款车型的完整规格 + 30 市场落地成本 + 出口合规画像」 | VehicleDirectoryTemplate / VehicleDetailTemplate（由现有 `[slug].astro` 演进） | **KEEP + IMPROVE**（五段式深度档案 + 去模板化） |
| 2 | **品牌目录与档案** | `/brands/` + `/brands/[slug]/` | 目录页 + 档案页 | 目录：「72 品牌及其母公司/出口定位总览」；档案：「某品牌母公司关系 + CVD 税率 + 代表车型落地成本区间」 | BrandDirectoryTemplate / BrandDetailTemplate（现有） | **KEEP + IMPROVE**（正文 129 词→>500 词） |
| 3 | **对比** | `/compare/`（新增） | 交互工具页 | 「并排比较任意 2–3 款车型的规格 + 落地成本，辅助 B2B 采购决策」 | CompareToolTemplate（新建） | **缺失 → NEW**（对标 /compare） |
| 4 | **三电技术** | `/technology/` + `/technology/[entity]/`（新增） | 枢纽页 + 实体页 | 枢纽：「电池/充电/动力总成/热管理/续航/车身安全 6 类技术名词总览」；实体：「某个技术名词的定义 + 溯源 + 关联车型」 | TechnologyHubTemplate / TechnologyEntityTemplate（新建） | **缺失 → NEW**（technical-master 137 实体零渲染 → 全量渲染） |
| 5 | **国家进口情报** | `/markets/` + `/markets/[country]/`（新增 per-market） | 汇总页 + 落地页 | 汇总：「30 市场关税/VAT/CVD 一屏对比」；落地：「某国进口中国 EV 的完整税负 + 法规 + 认证 + 代表车型落地价」 | MarketCompareTemplate（现有）/ MarketLandingTemplate（新建） | `/markets/` **IMPROVE** + per-market **NEW**（30 市场） |
| 6 | **购买指南** | `/guides/`（新增枢纽）→ 帖子保留 `/blog/[slug]/` | 枢纽页 + 帖子 | 枢纽：「按任务入口导航所有『如何进口到 X 国/如何买』指南」；帖子：「某国进口的具体步骤/税负/合规」 | GuideHubTemplate（新建）+ BlogLayout（现有） | 博客 **KEEP** + 枢纽 **NEW**（内容分类分层） |
| 7 | **原创研究** | `/research/`（新增枢纽）→ 帖子保留 `/blog/[slug]/` | 枢纽页 + 帖子 | 枢纽：「深度评测/出口格局/关税分析/对比研究入口」；帖子：「某主题的深度原创分析」 | ResearchHubTemplate（新建）+ BlogLayout（现有） | 博客 **KEEP** + 枢纽 **NEW** |
| 8 | **landed-cost 计算器** | `/landed-cost-calculator/` + `/landed-cost-methodology/` | 工具页 + 方法论页 | 计算器：「输入车型 + 目的国 → 实时落地成本拆解」；方法论：「每项估算的公式/来源/假设」 | CalculatorTemplate（现有）+ DocsLayout/MarketingLayout | **KEEP**（差异化护城河） |
| 9 | **B2B 询盘流程** | `/quote/`（新增，单页 + `?model=` 参数） | 表单页 | 「针对具体车型 + 目的国提交询价，获取供应商报价引导」 | QuoteTemplate（新建） | 部分 → **NEW**（对标 /quote，补齐车型级询价） |

**关键架构决策（三条，均符合「无目标不迁」红线）**：

1. **博客不拆分 URL**：购买指南（模块 6）与原创研究（模块 7）**共用 `/blog/[slug]/` 的 77 篇帖子，URL 零迁移**。通过新增两个**可索引枢纽页** `/guides/` 与 `/research/` 做任务型/深度型分组入口，而非把 77 个 URL 拆到新路径（拆分会造成 77 条 301 + 长尾损失，违背小步纪律）。
2. **对比不生成程序化配对页**：`/compare/` 只做**一个**交互工具页；不做 `/compare/[a]-vs-[b]/` 程序化落地（517² 组合 = 近重复内容爆炸）。车型两两对比的内容需求由现有 17 篇博客对比文继续承载，工具页反向链接到相关对比文。
3. **询价只做单页**：`/quote/` 单页 + 车型详情页 CTA 传参 `?model=slug`，**不**为 517 款车型各建一张薄询价页（避免 517 张无实质内容的近重复表单页）。

---

## 二、九模块逐项详解

### 模块 1 — 车型目录与档案（KEEP + IMPROVE）

- **目标 URL**：`/vehicles/`（目录）、`/vehicles/[slug]/`（详情，517 条，slug 来自 content frontmatter `slug` 字段）。
- **页面类型**：目录页（CollectionPage）、详情页（Vehicle 详情）。
- **用户意图**：
  - 目录页 → 信息型 + 导航型：按品牌/车身/动力/价格/续航检索车型。
  - 详情页 → 信息型：单一车型的完整规格、30 市场落地成本、出口合规画像、溯源。
- **模板归属**：现有 `src/pages/vehicles/[slug].astro` 演进为 `VehicleDetailTemplate`；`index.astro` 演进为 `VehicleDirectoryTemplate`（补 facet 筛选）。
- **P1 对位**：`/vehicles/[slug]/` 517 条 → **IMPROVE**。核心改造 = 移植 REF 的五段式深度档案（Entity Snapshot / Powertrain & Architecture / Dimensions & Logistics / Market Compliance & Export Profile / Benchmarking Matrix，28 个新字段，见 P1 §1.2）+ Overview 去模板化（首句唯一率 99%）。
- **URL 映射**：**全部 KEEP 原 URL**，无迁移。

### 模块 2 — 品牌目录与档案（KEEP + IMPROVE）

- **目标 URL**：`/brands/`、`/brands/[slug]/`（72 条，slug = 品牌内容文件 id 去扩展名）。
- **页面类型**：目录页 + 档案页（Organization）。
- **用户意图**：品牌层级的出口定位、母公司关系、CVD 税率、代表车型落地成本区间。
- **模板归属**：现有 `src/pages/brands/[slug].astro`、`index.astro` 演进。
- **P1 对位**：72 条 → **IMPROVE**，正文 129 词 → 目标 >500 词，补：母公司关系（`parent_manufacturer` 已有）、brand-cvd 税率（`tariffs.brand_cvd` 已有）、代表车型 landed-cost 区间（`landed_cost_markets` 可聚合）。
- **增强（可选项，不单列模块）**：厂商目录 `/manufacturers/` 作为品牌模块的子视图——母公司（`parent_manufacturer`）聚合页，避免与 9 模块冲突。P1 §七「厂商目录 ⚠️ 部分」在此闭环。
- **URL 映射**：**全部 KEEP 原 URL**。

### 模块 3 — 对比（缺失 → NEW）

- **目标 URL**：`/compare/`（单个交互工具页，新增）。
- **页面类型**：工具页（WebApplication）。
- **用户意图**：并排比较任意 2–3 款车型的规格 + 落地成本，辅助 B2B 采购决策。
- **模板归属**：`CompareToolTemplate`（新建，客户端交互）。
- **数据来源**：车型规格（content collection）+ 落地成本（`landed_cost_markets`）——**数据已在仓库，缺渲染层**。
- **P1 对位**：对标 chinaevpro `/compare`（P1 §七「对比工具 ❌ 缺失」）。静态两两对比内容由现有 17 篇博客对比文承载，不新建程序化配对页。
- **URL 映射**：**NEW**，无迁移。

### 模块 4 — 三电技术（缺失 → NEW，数据 100% 已存在）

- **目标 URL**：`/technology/`（枢纽）、`/technology/battery/`、`/technology/charging/`、`/technology/drivetrain/`（分类枢纽，可选）、`/technology/[entity]/`（实体页）。
- **页面类型**：枢纽页（CollectionPage）、实体页（DefinedTerm）。
- **用户意图**：技术名词的定义、溯源、关联车型；枢纽按 6 类（battery 39 / charging 36 / drivetrain 23 / thermal 13 / range 11 / body-safety 15 = 137 实体）组织。
- **模板归属**：`TechnologyHubTemplate` + `TechnologyEntityTemplate`（新建）。
- **数据来源**：`technical-master.json`（137 实体，含 `id/name/name_zh/category/definition/source/related_vehicles`）——**数据存在但零页面渲染**（P1 §1.3）。
- **P1 对位**：对标 chinaevpro `/technology`（P1 §七「技术参考页 ❌ 缺失」）+ P1 §六「technical-master 数据零渲染」。
- **URL 映射**：**NEW**，无迁移。

### 模块 5 — 国家进口情报（IMPROVE + NEW per-market）

- **目标 URL**：`/markets/`（汇总，现有）、`/markets/[country]/`（30 市场落地页，新增）。
- **页面类型**：汇总页（CollectionPage）、落地页（市场指南）。
- **用户意图**：汇总 → 30 市场关税/VAT/CVD 一屏对比；落地页 → 单一目的国的完整进口税负 + 法规 + 认证 + 代表车型落地价。
- **模板归属**：现有 `src/pages/markets/index.astro` 保留；`MarketLandingTemplate`（新建）。
- **数据来源**：`market-master.json`（30 市场：`import_duty/vat_gst/countervailing_duty/registration_fee_usd/source_ids/effective_date/last_verified/market_code`）+ `regulatory-master.json`（66 法规，按 `jurisdiction` 关联）。
- **P1 对位**：`/markets/` → **IMPROVE**（当前仅单页汇总表）；per-market → **NEW**（P1 §5.6）。
- **URL 映射**：`/markets/` **KEEP**，`/markets/[country]/` **NEW**（30 条，market_id 作 slug）。

### 模块 6 — 购买指南（博客 KEEP + 枢纽 NEW）

- **目标 URL**：`/guides/`（新增枢纽，可索引）→ 帖子**保留** `/blog/[slug]/`（国家 import guide ~26 篇等）。
- **页面类型**：枢纽页（CollectionPage）+ 帖子（Article）。
- **用户意图**：枢纽 → 「如何进口到 X 国」任务入口；帖子 → 具体国家/流程指南。
- **模板归属**：`GuideHubTemplate`（新建）+ 现有 `BlogLayout`（帖子不变）。
- **P1 对位**：博客 77 篇 → **KEEP**（P1 §5.4，国家指南关税口径实质不同，非门页，不合并）。枢纽按 `content_type: guide` 分组（该分类字段 P3 补到 blog frontmatter）。
- **URL 映射**：帖子 **KEEP 原 URL 零迁移**；`/guides/` **NEW**。

### 模块 7 — 原创研究（博客 KEEP + 枢纽 NEW）

- **目标 URL**：`/research/`（新增枢纽，可索引）→ 帖子**保留** `/blog/[slug]/`（深度评测 17 篇对比 + 出口格局 + 关税分析）。
- **页面类型**：枢纽页（CollectionPage）+ 帖子（Article）。
- **用户意图**：枢纽 → 深度评测/出口格局/关税分析/对比研究入口；帖子 → 主题深度原创分析。
- **模板归属**：`ResearchHubTemplate`（新建）+ 现有 `BlogLayout`。
- **P1 对位**：博客 **KEEP**；枢纽按 `content_type: research` 分组。
- **URL 映射**：帖子 **KEEP**，`/research/` **NEW**。

### 模块 8 — landed-cost 计算器（KEEP，护城河）

- **目标 URL**：`/landed-cost-calculator/`（客户端工具）、`/landed-cost-methodology/`（方法论）。
- **页面类型**：工具页 + 方法论页。
- **用户意图**：计算器 → 输入车型 + 目的国 → 实时落地成本拆解；方法论 → 每项估算的公式/来源/假设（EEAT 支撑）。
- **模板归属**：现有 `src/pages/landed-cost-calculator.astro` + `landed-cost-methodology.astro`（KEEP）。
- **P1 对位**：**KEEP**（P1 §5.7「工具/方法论页 → IMPROVE」仅指域名/邮箱一致性，非结构变更）。
- **URL 映射**：**KEEP 原 URL**。

### 模块 9 — B2B 询盘流程（部分 → NEW）

- **目标 URL**：`/quote/`（单页，新增）+ 车型详情页 CTA `?model=slug` 传参。
- **页面类型**：表单页（WebPage + ContactPoint）。
- **用户意图**：针对具体车型 + 目的国提交询价，获取供应商报价引导（本站不卖车，仅情报 + 询价引导）。
- **模板归属**：`QuoteTemplate`（新建，含表单 + 邮件/WhatsApp 渠道）。当前纯静态站无后端，表单提交需在 P4 落地时接入 form 后端（Formspree / Cloudflare Pages Functions），本 Phase 仅登记 IA。
- **P1 对位**：对标 chinaevpro `/quote`（P1 §七「B2B 询价流程 ❌ 缺失」，当前仅 `/contact` 通用表单）。
- **URL 映射**：**NEW**，无迁移。`/contact/` 保留作通用联系入口。

---

## 三、首页信息架构（优先车型发现）

### 3.1 首页设计定位

首页**第一优先级 = 车型发现**（搜索/筛选入口 + 热门车型/品牌区块），第二优先级 = 落地成本差异化展示（护城河），第三优先级 = 三大新增能力入口（对比/技术/询价）。

### 3.2 对照 chinaevpro 功能清单逐项标注

> 功能对标，不抄设计。判定四档：已有 / 部分 / 缺失 / 不适用。

| # | 功能项 | chinaevpro | 生产站现状 | 判定 | P2/P4 建议 |
| :--: | :--- | :---: | :--- | :---: | :--- |
| 1 | 车型搜索框 | ✅ | ✅ `VehicleSearch`（按名称/品牌/车身类型过滤，客户端） | **已有** | 保留；P4 增强（搜索建议纳入价格/续航） |
| 2 | 车型多面筛选（facets：动力/车身/价格/续航/品牌） | ✅ | ❌ 无 facet，仅单一搜索框 | **缺失** | P4 新增 facet 面板（目录页 + 首页） |
| 3 | 热门车型区块 | ✅ | ✅ 首页 top-10 最便宜车型卡 | **已有** | 保留（当前排序=价格升序，可改「热门」口径） |
| 4 | 热门品牌区块/品牌墙 | ✅ | ✅ 72 品牌墙 | **已有** | 保留；P3 改单源（品牌数组当前硬编码在 `index.astro`） |
| 5 | 落地成本差异化示例 | ✅ | ✅ 首页 3 张示例卡（BYD Qin Plus/Seal/Xiaomi SU7 落地溢价） | **已有** | 保留（这是对标站没有的差异化资产） |
| 6 | 对比工具入口 | ✅（/compare） | ❌ 无 | **缺失** | P4 新增 `/compare/` 首页入口 |
| 7 | 技术/三电情报入口 | ✅（/technology） | ❌ 无 | **缺失** | P4 新增 `/technology/` 首页入口 |
| 8 | 市场情报入口 | ✅（/market-analysis） | ⚠️ 仅 footer 无首页入口 | **部分** | P4 首页补 `/markets/` 入口 |
| 9 | 购车指南入口 | ✅（/buying-guides） | ✅ 导航有 Guides（/blog） | **已有** | 保留；P4 升级为 `/guides/` 枢纽入口 |
| 10 | 新闻区块 | ✅（/news） | ❌ 无 | **缺失** | P4 可选（低优先，情报站非新闻站） |
| 11 | B2B 询价 CTA | ✅（/quote） | ⚠️ 仅 `/contact` 通用表单 | **部分** | P4 新增 `/quote/` 车型级询价 CTA |
| 12 | 用户账户/登录 | ✅（/auth） | ❌ 无 | **不适用** | 跳过（情报站不卖车，无需账户） |

**汇总**：**已有 5 / 部分 2 / 缺失 4 / 不适用 1**。首页需补齐的硬缺口 = ① 多面筛选、② 对比入口、③ 技术入口、④ 询价 CTA（新闻为可选低优先）。

### 3.3 首页区块顺序（设计建议）

1. Hero（标题 + 搜索框 + 「浏览数据库 / 计算落地成本」双 CTA）
2. 落地成本示例条（3 卡，护城河数据）
3. **热门车型区块**（top-10，含 facet 快捷入口）
4. **三大新能力入口带**（对比 / 三电技术 / 市场情报 —— 模块 3/4/5 的首页引导）
5. 三步落地成本拆解（How It Works）
6. 品牌墙（72 品牌）
7. 询价 CTA（新增 `/quote/`）

---

## 四、导航与内链层级

### 4.1 Header 主导航（设计目标态）

> 现状 7 项（Home/Vehicles/Brands/Landed Cost/How It Works/Guides/Docs）→ 目标态重组为九模块入口，主项 ≤7，其余进 footer 或分组。

| 主项 | 目标 URL | 对应模块 | 现状 |
| :--- | :--- | :---: | :--- |
| Vehicles | `/vehicles/` | 模块 1 | 已有 |
| Brands | `/brands/` | 模块 2 | 已有 |
| Compare | `/compare/` | 模块 3 | **新增** |
| Technology | `/technology/` | 模块 4 | **新增** |
| Markets | `/markets/` | 模块 5 | **新增**（footer 已有入口，升主项） |
| Guides | `/guides/` | 模块 6 | 改指（原 /blog） |
| Research | `/research/` | 模块 7 | **新增**（原 /blog 拆分入口） |

- **CTA**：主 CTA 由「Browse Vehicles」改为「Get a Quote → `/quote/`」（模块 9）；次 CTA 保留「Calculate Landed Cost → `/landed-cost-calculator/`」（模块 8）。
- **降级进 footer**：Landed Cost Calculator、Methodology、Docs、Blog（时间序索引）、FAQ、法律页、About/Contact。

### 4.2 Footer 结构（目标态）

沿用现有 `navigation.ts` 的 footer 五栏（product/solutions/resources/company/legal），做以下调整：

- **product 栏**：+ Compare、+ Technology、+ Markets（补模块 3/4/5）。
- **resources 栏**：+ Research（模块 7）；Blog 保留为「全部文章时间序」入口。
- **solutions 栏**：保留 3 篇代表性深度文（EU Import Guide / Export Landscape 2026 / BYD Seal Review）。
- **company 栏**：保留 About/Authors/Editorial Independence/Methodology/Contact。
- **legal 栏**：7 法律页不变。

### 4.3 Breadcrumb 层级（页面类型 → 面包屑）

| 页面类型 | 面包屑结构 |
| :--- | :--- |
| 车型详情 | Home › Vehicles › `[Brand]` › `[Model]`（现有已实现，见 `[slug].astro`） |
| 品牌档案 | Home › Brands › `[Brand]`（现有已实现） |
| 对比工具 | Home › Compare |
| 技术实体 | Home › Technology › `[Category]` › `[Entity]` |
| 市场落地页 | Home › Markets › `[Country]` |
| 购买指南枢纽 | Home › Guides |
| 研究枢纽 | Home › Research |
| 询价 | Home › Quote |
| 博客帖子 | Home › Blog › `[Post]` |

### 4.4 九模块互链路径图（信息架构层级）

```
                                    ┌───────────────────────┐
                                    │      首页 (/)          │
                                    │  优先车型发现 + 落地成本  │
                                    └──────────┬────────────┘
        ┌─────────────┬─────────────┬──────────┼──────────┬──────────────┬─────────────┐
        ▼             ▼             ▼          ▼          ▼              ▼             ▼
  ┌───────────┐ ┌───────────┐ ┌──────────┐ ┌────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
  │ /vehicles/│ │ /brands/  │ │ /compare/│ │/techno-│ │ /markets/│ │ /guides/ │ │ /quote/  │
  │ 车型目录   │ │ 品牌目录   │ │ 对比工具  │ │ logy/   │ │ 市场汇总  │ │ 购买指南  │ │ B2B询价  │
  └─────┬─────┘ └─────┬─────┘ └────┬─────┘ │ 技术枢纽 │ └────┬─────┘ └────┬─────┘ └────┬─────┘
        ▼             ▼            │        └────┬─────┘      ▼            ▼            │
  /vehicles/[slug]/ /brands/[slug]/│        /technology/[entity]/  /markets/[country]/ │
   (517 车型详情)    (72 品牌档案)   │         (137 技术实体)         (30 市场落地页)    │
        │             │            │                                    │            │
        │  互链：车型详情⇄品牌档案；技术实体→关联车型；市场落地页→代表车型；             │
        └─────────────┴────────────┴────────────────────────────────────┴────────────┘
                    ▲ 各模块详情页反向互链（实体图谱 entity-graph.json 扩展后）            ▲
                    │                                                                    │
              ┌─────┴──────┐          ┌─────────────────────────┐          ┌────────────┴─────┐
              │ /research/ │          │ /landed-cost-calculator/│          │  /blog/[slug]/   │
              │ 原创研究枢纽 │◄────────►│ + /landed-cost-methodology│        │  77 篇（共用）     │
              └────────────┘          └─────────────────────────┘          └──────────────────┘
```

**互链要点**：
- 车型详情页 ⇄ 品牌档案页（现有已实现「Related models from [Brand]」）。
- 技术实体页 → 关联车型（`related_vehicles` 字段已有）。
- 市场落地页 → 该市场代表车型（`landed_cost_markets` 按 market_key 聚合）。
- 对比工具页 ⇄ 博客对比文（工具页链接相关对比文）。
- 计算器 ⇄ 方法论页（现有 `markets/index.astro` 已链接计算器）。
- 内链密度目标：车型页现有 38 条唯一内链（P1 §4.5），新模块落地后每类详情页 ≥20 条唯一内链。

---

## 五、URL 迁移映射表（一对一 301 目标）

### 5.1 迁移总览（诚实结论）

> 依据 P1 §5.1 Action 分布：**KEEP 92 / IMPROVE 609 / MERGE 0 / REDIRECT 0 / NOINDEX 597 / REMOVE 0**。

| Action | 数量 | 一对一 301 目标 | 说明 |
| :--- | :---: | :--- | :--- |
| MERGE | 0（候选 2 组） | **无**（不迁） | 2 组 import guide 候选合并，P1 判「暂缓」——合并损失长尾，**保持原 URL** |
| REDIRECT | 0 | **无** | 无死链需 301（现有 redirects 均正确） |
| NOINDEX | 597 | **不适用 301**（用 `X-Robots-Tag: noindex`） | `.md` 变体 594 + `/data/*.json` 3，**非 301 迁移，是 robots 指令** |
| REMOVE | 0 | **无** | 无删除项 |

**核心结论：本 Phase 需执行的 301 迁移条数 = 0**。这是设计纪律的正面结果——九模块改造**全部在现有 URL 内完成（IMPROVE）或新增 URL（NEW）**，无一需要改 URL。

### 5.2 MERGE 候选组（有据保留，不迁）

| 候选组 | 现有 URL | 建议 | 理由（P1 §5.4） |
| :--- | :--- | :--- | :--- |
| 组 1 | `/blog/uae-import-guide/` + `/blog/saudi-arabia-import-guide/` | **保留两个，不合并** | 两国关税/VAT 口径实质不同（UAE 5% VAT vs KSA 15% VAT），非门页 |
| 组 2 | `/blog/turkey-import-guide/` + `/blog/indonesia-import-guide/` | **保留两个，不合并** | 区域不同（中东 vs 东南亚），税制差异大 |

> 若未来确需合并，301 目标 = 保留合并后主帖的 URL，被合并帖 301 → 主帖。**本 Phase 不触发**。

### 5.3 NOINDEX 清单（非 301，robots 指令）

| 模式 | 数量 | 处理 | 保留可访问性 |
| :--- | :---: | :--- | :--- |
| `/vehicles/[slug].md` | 517 | `X-Robots-Tag: noindex` | ✅ 保留（API/AI 消费） |
| `/blog/[slug].md` | 77 | `X-Robots-Tag: noindex` | ✅ 保留 |
| `/data/vehicles.json` + `/data/brands.json` + `/data/tariffs.json` | 3 | `X-Robots-Tag: noindex` | ✅ 保留（机器可读端点） |

> REF 独有 `/data/source-master.json`（生产 404）同样处理（P1 §5.8）。**注意**：NOINDEX 用 `X-Robots-Tag` 响应头，**不用** `robots.txt Disallow`（会破坏渲染/抓取，P1 §八红线 2）。

### 5.4 新增 URL 注册表（NEW，非迁移）

| 新 URL | 模块 | 数量 | 数据源 | Phase 归属 |
| :--- | :---: | :---: | :--- | :--- |
| `/compare/` | 3 | 1 | content collection + landed_cost | P4 |
| `/technology/` | 4 | 1 | technical-master.json | P4 |
| `/technology/battery/` `/charging/` `/drivetrain/` | 4 | 3（可选） | technical-master.json | P4 |
| `/technology/[entity]/` | 4 | 137 | technical-master.json | P4 |
| `/markets/[country]/` | 5 | 30 | market-master + regulatory-master | P4 |
| `/guides/` | 6 | 1 | blog（content_type: guide） | P4 |
| `/research/` | 7 | 1 | blog（content_type: research） | P4 |
| `/quote/` | 9 | 1 | 表单 + 参数 | P4 |
| `/manufacturers/`（可选子视图） | 2 | 1 | brand `parent_manufacturer` | P4（可选） |

---

## 六、Schema 组织架构（页面类型 → 结构化数据归属）

> 现状：首页 = WebSite/Organization/Dataset/Breadcrumb/ContactPoint；车型页 = 2 个 JSON-LD（Vehicle + Breadcrumb，**零 aggregateRating/review**，正确）；品牌页 = Organization + BreadcrumbList；博客 = Article + FAQPage（解析 FAQ 节）；目录页 = CollectionPage（P1 §4.5 实测）。

| 页面类型 | 一级 Schema | 二级 Schema | 归属模板/组件 |
| :--- | :--- | :--- | :--- |
| 首页 `/` | WebSite（含 SearchAction） | Organization · Dataset · BreadcrumbList · ContactPoint | `SEO.astro` + `index.astro`（Dataset） |
| 车型详情 `/vehicles/[slug]/` | **Vehicle**（含 `offers`，价格同源，无 seller/rating/review） | BreadcrumbList · Organization | `[slug].astro` |
| 车型目录 `/vehicles/` | CollectionPage | BreadcrumbList | `vehicles/index.astro` |
| 品牌档案 `/brands/[slug]/` | **Organization**（含 `parentOrganization`） | BreadcrumbList | `brands/[slug].astro` |
| 品牌目录 `/brands/` | CollectionPage | BreadcrumbList | `brands/index.astro` |
| 对比工具 `/compare/` | **WebApplication** | BreadcrumbList | `CompareToolTemplate`（新建） |
| 技术枢纽 `/technology/` | CollectionPage | BreadcrumbList | `TechnologyHubTemplate` |
| 技术实体 `/technology/[entity]/` | **DefinedTerm**（含 `source`/`sameAs`） | BreadcrumbList | `TechnologyEntityTemplate` |
| 市场汇总 `/markets/` | CollectionPage | BreadcrumbList | `markets/index.astro` |
| 市场落地 `/markets/[country]/` | **Article**（或 `Place`） | BreadcrumbList · Organization | `MarketLandingTemplate` |
| 指南枢纽 `/guides/` | CollectionPage | BreadcrumbList | `GuideHubTemplate` |
| 研究枢纽 `/research/` | CollectionPage | BreadcrumbList | `ResearchHubTemplate` |
| 博客帖子 `/blog/[slug]/` | **Article** | **FAQPage**（有 FAQ 节时，现有已实现）· BreadcrumbList | `BlogLayout` + `[...slug].astro` |
| 计算器 `/landed-cost-calculator/` | WebApplication | BreadcrumbList | `landed-cost-calculator.astro` |
| 方法论 `/landed-cost-methodology/` | Article | BreadcrumbList | DocsLayout/MarketingLayout |
| 询价 `/quote/` | WebPage | Organization · ContactPoint | `QuoteTemplate`（新建） |
| 法律页 7 | WebPage | BreadcrumbList · Organization | MarketingLayout |
| 文档 `/docs/[slug]/` | Article（或 TechArticle） | BreadcrumbList | DocsLayout |

**Schema 红线（P1 §八红线 3 落实）**：
- 车型页 **禁止** 添加 `aggregateRating` / `review` / `seller`（无真实数据，属 Structured Data Abuse）。
- Vehicle 保留 `offers`（价格与页面可见 `price_usd` 同源，不声明 seller）。
- 技术实体页用 `DefinedTerm`（已合法承载 `name/definition/url/sameAs`），**不用** 未验证的 `Product`/`Vehicle` 包装。

---

## 七、附录 — P3 预告性清单（数据质量单一数据源改造点）

> 本附录为 Phase 3「车辆数据质量」的**预告清单**，不包含任何本 Phase 的代码改动。全量落地在 P3。

### 7.1 单一数据源（Single Source of Truth）改造点清单

| # | 改造点 | 现状（P1 证据） | P3 目标 |
| :--: | :--- | :--- | :--- |
| 1 | `/data/vehicles.json` 端点字段 | 仅 **12 字段**，尺寸/扭矩/加速/极速/溯源等 14+ 字段 100% 缺失 | ≥ **20 字段**（对齐 content frontmatter 35 字段的核心子集） |
| 2 | `vehicle-master.json` vs content frontmatter | 已分叉（content 有完整规格，master 100% null） | 单一真源 = content frontmatter（权威），master 由 content **重新生成**，不再手维护 |
| 3 | 品牌数组硬编码 | 首页 `index.astro` 硬编码 58 品牌数组（llms.txt 又写 315/58 陈旧计数） | 品牌清单从 content/brand collection **派生**（`getActiveBrandSlugs()` 已有） |
| 4 | 站点计数 | llms.txt「315 models/58 brands」陈旧，实际 517/72 | 统一由 `site-stats.ts`（已单源）驱动，llms.txt 同步 |
| 5 | `data_reviewed` 全 false | 517×false（诚实但未闭环） | 推进人工复核，或明确「待审」口径 |

### 7.2 规格分层（官方规格/厂商宣称/独立测试/估算/未验证）

> 现状 `data_tier` 已有 3 档（333/163/21 分布，P1 证据）。P3 扩展为 **5 层 + 独立 `spec_source_type` 字段**：

| 层级 | 字段值 | 含义 | 现映射 |
| :--: | :--- | :--- | :--- |
| 1 | `official_specification` | 官方规格（厂家官网/工信部公告/监管文件） | data_tier=1 |
| 2 | `manufacturer_claim` | 厂商宣称（未独立验证的营销口径） | data_tier=2 |
| 3 | `independent_test` | 独立测试（第三方实测/机构评测） | data_tier=3 |
| 4 | `estimate` | 估算（本站推算，如 freight/certification 固定值） | 新增（现仅 landed-cost 模板层标注「EV Hub estimate」） |
| 5 | `unverified` | 未验证（有值但无法溯源） | 新增（对应 `data_reviewed: false` + 无 source_url） |

**规则**：每个规格字段记录 `{value, tier, source, source_url, timestamp}`，**无来源标 N/A，禁止编造**（P1 §八红线 4）。

### 7.3 CLTC / WLTP / EPA 区分字段设计

> 现状：`range_cltc_km` + `range_long_km` + `range_standard`（单一字符串「CLTC」）。P3 改为**逐标准独立字段**：

| 新字段 | 类型 | 现状 | 说明 |
| :--- | :--- | :--- | :--- |
| `range_cltc_km` | number\|null | 已有（缺失率 9.1%） | CLTC 续航，中国官方标准 |
| `range_wltp_km` | number\|null | **缺失**（REF 覆盖仅 2%，P1 §4.2C） | WLTP 续航，欧洲标准，**无来源必标 null** |
| `range_epa_km` | number\|null | **缺失** | EPA 续航，北美标准，**无来源必标 null** |
| `range_standard_primary` | enum(`CLTC`\|`WLTP`\|`EPA`) | 现 `range_standard`（单一 CLTC） | 指定页头展示的主标准 |
| 每标准溯源 | `{source, source_url, tier}` | 缺失 | 逐标准独立溯源，**禁止跨 trim 混用** |

**红线**：三个续航标准**永远独立列示**，不混为一个数字；不把 CLTC 值冒充 WLTP/EPA（CLTC 普遍比 WLTP 高 15–25%）；不同 trim 的规格**不合并**（当前 `trim` 字段缺失率 84%，P3 补齐）。

### 7.4 P3 交付物预告

1. `content.config.ts` 补 28 个深度字段（对齐 REF，P1 §1.2）+ 规格分层字段（`spec_source_type`/`range_wltp_km`/`range_epa_km`/`range_standard_primary`）。
2. `vehicle-master.json` 由 content frontmatter 重新生成（单源落地）。
3. `/data/vehicles.json` 端点扩到 ≥20 字段（含尺寸/扭矩/加速/极速/溯源/分层）。
4. 数据质量报告：字段缺失率矩阵 + 溯源覆盖 + 分层层级分布。

---

## 附：本 Phase 交付记录

- **九模块架构**：9 模块全部给出目标 URL / 页面类型 / 意图 / 模板 / P1 对位。
- **首页功能对照**：12 项 → 已有 5 / 部分 2 / 缺失 4 / 不适用 1。
- **URL 迁移映射**：**0 条 301 迁移**（MERGE 0 / REDIRECT 0 / REMOVE 0）；NOINDEX 597 条（非 301，用 X-Robots-Tag）；NEW 注册 9 类 URL。
- **Schema 归属表**：15 类页面类型 × 结构化数据归属。
- **P3 预告**：单源改造 5 点 + 规格分层 5 层 + CLTC/WLTP/EPA 字段设计。
- **零生产代码改动**：本 Phase 仅新增本文档，无 `src/` 改动，无部署。
