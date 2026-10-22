# ElectricVehicleHub 重设计 — Phase 4b 新模块交付报告（/compare/ + /technology/）

> **对象**：生产站 `https://electricvehiclehub.net/`（仓库 `repos/CNEVhub`，`main`）
> **框架**：`phase2/54-evhub-redesign-prompt.md`（PHASE 4 页面模板 + PHASE 6 小步交付）
> **前置**：`docs/redesign-p2-architecture.md`（/compare/ 与 /technology/ 章节）、`docs/redesign-p4a-template-port.md`
> **时间**：2026-10-22（UTC）
> **纪律**：零虚构 · 对比数据单一数据源精确不混 trim · schema（BreadcrumbList/ItemList 适用处）· canonical/sitemap 自动纳入 · 每模块独立 commit 可回滚

---

## 〇、执行摘要

| 项 | 改造前 | 改造后 |
| :--- | :---: | :---: |
| /compare/ 对比工具 | 缺失（对标功能站有） | **1 个交互工具页** |
| /technology/ 技术参考 | 缺失（technical-master 137 实体**零渲染**） | **1 枢纽 + 137 实体页**（100% 渲染） |
| 新增 URL | — | **139**（compare 1 + technology 1 + 实体 137） |
| 技术实体渲染覆盖率 | 0/137 | **137/137（100%）** |
| 站点总页数 | 900 | **1039**（+139） |
| sitemap URL | 701 | **840**（+139） |

**关键结论**：P2 发现的 `technical-master.json`（137 实体）零渲染问题在本 Phase 闭环——137 个技术名词全部从数据文件渲染为独立可索引实体页，缺关联车型的实体以诚实空态 + 来源标注呈现，不虚构任何车辆关联。

---

## 一、/compare/ 模块（commit `p4b-compare`）

### 1.1 页面结构

- **URL**：`/compare/`（单交互工具页，`src/pages/compare/index.astro`）。
- **用户意图**：并排比较任意 2–3 款车型的同 trim 规格 + 价格 + 逐标准续航，辅助 B2B 采购决策。
- **选择器**：3 个车型下拉（按品牌 optgroup 分组，覆盖 517 款），URL query `?a=slug&b=slug&c=slug` 作为可分享/可收藏状态。
- **交互模型（静态托管适配）**：对比表由注入的目录 JSON（517 条）**客户端渲染**；下拉变更时 `history.replaceState` 同步 URL query、即时重渲染。服务端同时渲染默认对比（BYD Seal vs Xiaomi SU7）作为 no-JS / 可索引兜底。

### 1.2 对比表口径（数据纪律）

| 维度 | 实现 |
| :--- | :--- |
| 单一数据源 | `vehicles` content collection（517 车型），非 `vehicle-master.json`（陈旧分叉） |
| 同 trim 口径 | 每列 = 单车型的 listed trim（`trim` 字段，缺省「Standard (base)」），**不跨 trim 合并** |
| 续航标准 | **CLTC / WLTP / EPA 三行独立列示**，永不混为一个数字、不做标准换算 |
| 五段关键字段 | Overview（价格/落地成本）+ Range（分标准）+ Battery & Powertrain + Dimensions + Export profile（HS code/充电接口） |
| 价格 | ex-factory `price_usd` + 「Landed cost (Germany, est.)」标注 estimate |
| 缺值 | 统一「—」，不编造、不估算 |

### 1.3 Schema

- **WebApplication**（name/url/applicationCategory/offers $0/publisher）——工具页，无 rating/review/seller。
- **BreadcrumbList**（Home › Compare）。
- canonical 由 SEO 组件自动生成（`siteConfig.url` + pathname）。

---

## 二、/technology/ 模块（commit `p4b-technology`）

### 2.1 数据层

- 新增 `src/lib/technical.ts`：单一数据源 = `technical-master.json`（137 实体）。
- 暴露：`technicalEntities`、`getEntityById`、`getEntitiesByCategory`、`getEntitiesByVehicle(slug)`（反向映射）、`sourceUrl`（从 source 字符串提取 URL）、`TECH_CATEGORIES`（6 分类元数据 + 顺序）。

### 2.2 实体分布（6 分类，全部渲染）

| 分类 | label | 中文 | 实体数 |
| :--- | :--- | :--- | :---: |
| battery | Battery & Chemistry | 电池 | 39 |
| charging | Charging & Standards | 充电 | 36 |
| drivetrain | Drivetrain & Motors | 动力总成 | 23 |
| thermal | Thermal Management | 热管理 | 13 |
| range | Range & Efficiency | 续航 | 11 |
| body-safety | Body & Safety | 车身安全 | 15 |
| **合计** | | | **137** |

> 注：任务描述「电池/充电/动力总成三分类」为「三电」核心概括；数据实际含 6 分类。枢纽页以三电（battery/charging/drivetrain，98 实体）为主卡片，thermal/range/body-safety（39 实体）为参考卡片，**6 类 137 实体全部可达**，不因「三分类」丢弃其余 39 实体。

### 2.3 页面结构

- **枢纽 `/technology/`**：6 分类索引 + 137 实体链接（英文名 + 中文名）+ 分类计数。CollectionPage schema。
- **实体页 `/technology/[entity]/`**（137 条，`getStaticPaths` 从 technical-master 生成）：
  - 定义（definition，逐字来自数据）
  - 来源（source，含可点击 URL）
  - 关联车型（`related_vehicles` → `/vehicles/[slug]/` 卡片，含标题/品牌/价格/CLTC）
  - **诚实空态**：无关联车型时明确「当前目录（517 款）未标注此术语，定义与来源仅供引用，不隐含车辆关联」
  - DefinedTerm + BreadcrumbList schema（Home › Technology › [分类] › [实体]）

### 2.4 关联覆盖率（诚实口径）

- `related_vehicles` 字段仅 23/137 实体有值，覆盖 28 款车型。
- 实体页**只渲染数据里真实存在的关联**，不为无关联实体编造车型。

---

## 三、内链整合

| 整合点 | 改动 | 归属 commit |
| :--- | :--- | :--- |
| Header 主导航 | + Compare、+ Technology（并移出 How It Works/Docs 至 footer 已有项，保持主项 ≤7） | 分属两 commit |
| Footer product | + Compare、+ Technology | 分属两 commit |
| 首页 | +「Compare any two Chinese EVs」入口段；+「Understand the technology」入口段 | 分属两 commit |
| 车型详情页 | +「Compare this model」CTA（`/compare/?a=slug`）；+「Technology Reference」区块（互链 `/technology/[entity]/`） | 分属两 commit |
| 技术实体页 → 车型 | `related_vehicles` 反链到车型详情 | p4b-technology |
| 技术枢纽 → 实体 | 137 实体链接 | p4b-technology |
| Breadcrumb | Compare（Home›Compare）、Technology（Home›Technology›分类›实体） | 分属两 commit |

---

## 四、验证结果

| 项 | 命令/方法 | 结果 |
| :--- | :--- | :--- |
| 构建 | `npm run build` | ✅ **1039 页**，exit 0（186.7s；SITE_URL 未设回退 .net，非阻断） |
| compare 渲染 | `dist/compare/index.html` | ✅ 默认对比表（BYD Seal vs Xiaomi SU7）+ 注入 517 条 compare-data JSON |
| compare 数据 5 组抽检 | 脚本比对 5 组车型 price/CLTC/WLTP/battery + 交叉核对 frontmatter | ✅ 5/5 正确，零虚构 |
| compare 续航分离 | 抽 byd-seal/zeekr-001 等 | ✅ CLTC/WLTP/EPA 分行独立，无换算 |
| technology 实体渲染 | `dist/technology/` 目录 | ✅ 137 实体子目录 + 1 枢纽 index.html |
| technology 实体 10 抽检 | lfp/blade/nmc/nca/solid-state/800v/gbt-20234/cltc/wltp/heat-pump | ✅ 10/10 def/src/rel/schema 齐全 |
| 占位残留 | `npm run placeholder:scan` | ⚠️ md findings 90（均为 P4a 既有语义 N/A，非本批引入）、master findings **0** |
| sitemap 增项 | `dist/sitemap-0.xml` `<loc>` 计数 | ✅ 840 URL（701 → 840，+139 精确匹配） |
| 域名泄漏 | — | 无外链域名改动 |

> **占位扫描副作用说明**：`npm run placeholder:scan` 会向 `docs/data-quality-report.md` **追加**扫描章节（脚本 `appendFileSync`）。验证期间多次运行产生重复追加，已 `git checkout` 还原该文件——本批**未改动** data-quality-report.md。

---

## 五、commit 列表与回滚

| # | commit | 标记 | 内容 |
| :--: | :--- | :--- | :--- |
| 1 | `c4625d7` | p4b-compare | /compare/ 工具页 + Compare 内链（nav/首页/车型页） |
| 2 | `aaf3b3b` | p4b-technology | /technology/ 枢纽 + 137 实体页 + technical.ts + Technology 内链（nav/首页/车型页） |

**回滚（逆序单命令）**：

```bash
# 回滚 technology 模块（保留 compare）
git revert aaf3b3b

# 回滚 compare 模块（保留 technology）
git revert c4625d7

# 全量回滚两个模块
git revert aaf3b3b c4625d7
```

两 commit 相互独立、各自可单独回滚；回滚后 `npm run build` 回到对应状态（technology 回滚 → 站点回 900+1=901 页；compare 回滚 → 站点回 900+138=1038 页；全量 → 回 900 页）。

---

## 六、未做事项（红线，刻意不做）

1. **未补 `related_vehicles` 关联**：仅 23/137 实体有值，其余按诚实空态呈现；扩展关联属数据层工作（P3/P5），不在渲染层编造。
2. **未生成程序化配对页**：`/compare/` 仅单工具页，不做 `/compare/[a]-vs-[b]/`（517² 近重复爆炸，P2 决策）。
3. **未做 `/technology/battery/` 等分类子枢纽**：P2 记为「可选」，本批以单一枢纽 + 锚点分类索引覆盖全部实体。
4. **未改 `/data/*.json` 端点 / `vehicle-master.json`**：不在本批范围。
5. **未动 header 主 CTA**：保持「Browse Vehicles」；「Get a Quote → /quote/」属模块 9（后续 Phase）。
