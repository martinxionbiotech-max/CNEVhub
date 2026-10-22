# ElectricVehicleHub 重设计 — Phase 5 SEO 与技术质量验证报告

> **对象**：生产站 `https://electricvehiclehub.net/`（仓库 `repos/CNEVhub`，`main`）
> **前置**：P4a 车型模板移植 + P4b /compare/ /technology/ 新模块
> **框架**：`phase2/54-evhub-redesign-prompt.md`（PHASE 5 技术 SEO 验证 + PHASE 6 小步交付纪律）
> **权威依据**：`docs/redesign-p1-audit.md`（URL 建议表）+ `docs/redesign-p2-architecture.md`（URL 迁移映射表）
> **时间**：2026-10-22（UTC）
> **数据可用性**：GSC 未提供，排名/收录相关结论标 U，不归因（沿用 P1 口径）

---

## 〇、执行摘要

P4a/P4b 改动后全站技术验证**七项全绿**，无 P0/P1 阻断项；迁移执行按 P2 映射表**诚实核对**——P2 权威表 **REDIRECT 0 / MERGE 0 / NOINDEX 597 / REMOVE 0**，本 Phase 实际执行的唯一迁移项 = **NOINDEX 597 条**（`.md` 变体 594 + `/data/*.json` 端点 3，用 `X-Robots-Tag: noindex`）。任务描述的「REDIRECT 1 项」经全站证据复核**不成立**（0 断链 / 0 死 URL / 0 改名），按「有据才做」纪律**未执行任何 301**。

| 检查项 | 结果 | 异常数 |
| :--- | :---: | :---: |
| ① canonical | 840/840 自引用正确 | **0** |
| ② sitemap 对账 | 840 loc 全部落地，dist 无 orphan | **0** |
| ③ robots/noindex 一致性 | noindex 页 0 条混入 sitemap | **0**（含 597 端点缺口 → 已修） |
| ④ title/desc 唯一性 | 840 标题 / 840 描述 | **0 重复** |
| ⑤ JSON-LD | 15 页抽检，零虚构 rating/review/seller | **0 虚构**（4 处 schema 冗余见 §五） |
| ⑥ SSR 渲染 | 车型 5/5 · 技术 5/5 · 对比 1/1 | **0** |
| ⑦ 内链 | 新模块入口已挂，109,589 条内链 | **0 断链** |

---

## 一、全站技术验证（七查）

### ① canonical 840/840 ✅

- `dist/sitemap-0.xml` 840 条 `<loc>`，全部同源 `https://electricvehiclehub.net`。
- 逐页抽 `<link rel="canonical">`：**840/840 自引用正确**，0 缺失、0 指向错误域名。
- 新模块 canonical 正确：`/compare/` → `…/compare/`；`/technology/` → `…/technology/`；`/technology/[entity]/`（抽 lfp-battery/blade-battery/800v-architecture）→ 各自自引用。

### ② sitemap 840 vs dist 实际页对账 ✅

- **840 条 sitemap loc 全部落地**（0 条 404）。
- dist 共 **1039 个 HTML 文件**；不在 sitemap 的 197 页 = `/blog/page/`（13）+ `/blog/tag/`（184），均为**已 noindex 页**，另有 `/404/`、`/500/` 排除。**0 orphan 可索引页**。
- `.md` 变体（594）+ `/data/*.json`（3）**均不在 sitemap**（正确，机器可读面不入索引）。

### ③ robots/noindex 一致性 ✅（含 597 端点缺口修复）

- **noindex 页 0 条混入 sitemap**（收录指令不矛盾）。
- 全站 meta robots noindex 共 199 页（分页 13 + 标签 184 + 404 + 500），全部正确排除出 sitemap。
- **迁移缺口（本 Phase 修复）**：`.md` 变体 594 + `/data/*.json` 3 = **597 条机器可读端点可索引但无 noindex**（P1 §5.8 / P2 §5.3 既定项）。已用 `X-Robots-Tag: noindex` 修复（`public/_headers` 边缘层 + 5 个端点 `.ts` 源码层双保险），见 §二。

### ④ title/desc 唯一性 ✅

- 840 页 `<title>`：**0 重复**。
- 840 页 `<meta name="description">`：**0 重复**。
- 新模块无模板化标题撞车（技术实体 137 页标题逐实体唯一）。

### ⑤ JSON-LD 校验 ✅（抽 15 页 · 零虚构）

抽 15 页（首页/车型目录/品牌目录/对比/技术枢纽/3 车型/1 品牌/2 技术实体/2 博客/市场/计算器）：

- **零虚构**：`aggregateRating` / `review` / `seller` / `ratingValue` / `reviewCount` **0 命中**（全 15 页 + 全站 grep）。
- **persona 核查**：唯一作者实体 = `Wei Wang`（"EV & Battery Industry Analyst"，`Chengguang Energy`），在 `/authors/`、`/editorial-independence/`、`/about/`、车型页署名**一致声明**，属**已声明的站内作者**，非虚构 reviewer/多重 persona。本站不声明可独立核验的真人身份（U）。
- 类型分布正确：车型页 `Vehicle`（含 `offers`，价格与页面同源、不声明 seller）· 博客页 `Article` · 首页 `WebSite/Organization/Dataset/BreadcrumbList/ContactPoint` · 对比 `WebApplication` · 技术实体 `DefinedTerm(+DefinedTermSet)` · 品牌/技术/目录 `CollectionPage`。

**4 处 schema 冗余（非虚构、非阻断，登记待后续清理）**：

| # | 页面 | 现象 | 来源 |
| :--: | :--- | :--- | :--- |
| S1 | 车型页 517 | 同时出 `Article`（含 author Person）+ `Vehicle`，主类型冗余 | **P4a 前既有**（`type="article"` 原始模板即存在） |
| S2 | `/vehicles/`、`/landed-cost-calculator/` | 基础 schema（WebSite+Org+Breadcrumb）渲染 **2 次** | 既有（页面同时 `<SEO>` + `<MarketingLayout>`） |
| S3 | `/brands/[slug]/` 72 | `Organization`+`BreadcrumbList` 各 **2 次** | 既有 |
| S4 | `/technology/[entity]/` 137 | `BreadcrumbList` **2 次**（页面自带 breadcrumbLd + Layout 再出） | **P4b 引入** |

> S4 为 P4b 新模块引入的轻微重复面包屑，建议后续单提交删除实体页内冗余 `breadcrumbLd`（Layout 已出面包屑）。

### ⑥ SSR 渲染（直出）✅（抽 10 页）

- **车型 5 页**（byd-seal/xiaomi-su7/wuling-binguo/zeekr-001/deepal-l07-erev）：五段式（Entity Snapshot/Powertrain/Dimensions & Logistics/Market Compliance/Benchmarking）+ 40HQ 装箱 + Data Sources **5/5 齐全**。
- **技术实体 5 页**（lfp-battery/blade-battery/800v-architecture/wltp/cltc）：定义 + 来源链接 + 关联车型/诚实空态 + schema **5/5 齐全**。
- **对比 1 页**：默认对比表（BYD Seal vs Xiaomi SU7）+ 注入 517 条 compare-data **渲染正确**。

### ⑦ 内链核查 ✅

- **新模块入口已挂**：首页含 `/compare/` + `/technology/` 入口；车型页含「Compare this model」CTA（`/compare/?a=slug`）+「Technology Reference」互链区块；Header/Footer 均含 Compare/Technology。
- **断链扫描全站 dist**：109,589 条内部 `href`/`src`，**0 断链**。

---

## 二、迁移执行清单（有据才做）

> 权威依据 = P2 迁移映射表 §5.1。每项独立 commit。

| Action | P2 表数量 | 本 Phase 实际执行 | 说明 |
| :--- | :---: | :---: | :--- |
| **REDIRECT** | 0 | **0（未执行）** | 任务描述「REDIRECT 1 项」经证据复核不成立：全站 0 断链、0 死 URL、0 改名、sitemap 0 缺失。P2 明确「无死链需 301」。按「一对一 301 有目标才迁」纪律，**无目标不迁**，故执行 0 条。 |
| **MERGE** | 0（候选 2 组） | **0（未执行）** | 2 组 import guide 候选（uae+saudi / turkey+indonesia）P2 §5.2 判「保留两个不合并」（关税/VAT 口径实质不同，非门页）。复核两站帖子均存在、内容实质，**维持不合并**。 |
| **NOINDEX** | 597 | **597（已执行）** | 594 `.md` + 3 `.json` → `X-Robots-Tag: noindex`（非 301、非 robots.txt Disallow，P1 §八红线 2）。 |
| **REMOVE** | 0 | **0（未执行）** | 无 URL 删除项。发现 1 个仓库残留文件，进待批准清单（§三）。 |

### NOINDEX 执行明细（commit `p5-seo-noindex`）

- `public/_headers`：`/vehicles/*.md`、`/blog/*.md` 各加 `X-Robots-Tag: noindex`；新增 `/data/*.json` → `X-Robots-Tag: noindex`（Cloudflare Pages 边缘层，生产生效）。
- 5 个端点 `.ts`（`vehicles/[slug].md.ts`、`blog/[...slug].md.ts`、`data/{vehicles,brands,tariffs}.json.ts`）：`Response` headers 各加 `X-Robots-Tag: noindex`（源码层，dev/preview + 非 CF 宿主防御）。

---

## 三、待批准清单（REMOVE，未执行）

> 破坏性操作需 review 纪律，以下仅登记，**本 Phase 未删除**，待人工批准。

| 项 | 位置 | 说明 | 建议 |
| :--: | :--- | :--- | :--- |
| R1 | `src/pages/brands/_t.txt`（内容 `hello123`） | 遗留测试文件，`_` 前缀在 Astro 不产路由、不影响线上 URL，但属仓库垃圾 | 人工确认后 `git rm`（单提交） |

---

## 四、回滚命令

### NOINDEX 回滚（撤销本 Phase 唯一迁移项）

```bash
# 回滚 X-Robots-Tag 改动（6 文件回到 P4b 状态）
git revert 4407165

# 或手工回退：
git checkout HEAD~1 -- public/_headers \
  "src/pages/vehicles/[slug].md.ts" "src/pages/blog/[...slug].md.ts" \
  src/pages/data/vehicles.json.ts src/pages/data/brands.json.ts \
  src/pages/data/tariffs.json.ts
```

### 若误删 R1 待批准项

```bash
git checkout HEAD~1 -- src/pages/brands/_t.txt
```

---

## 五、未做事项（红线，刻意不做）

1. **未执行任何 301**（REDIRECT/MERGE 均 0，无证据）。
2. **未删除 R1**（待批准）。
3. **未修 schema 冗余 S1–S4**：均为非虚构、非阻断的结构化数据重复/冗余，非本 Phase 迁移范围；S4（技术实体双面包屑）为 P4b 引入，建议后续单提交清理。
4. **未动 `robots.txt`**：维持 `Allow: /`（`/_astro/` 保持可抓取，P1 §八红线 2）；noindex 全部走 `X-Robots-Tag`。
5. **未补 `related_vehicles` 关联 / WLTP/EPA 值**：数据层工作，非验证/迁移范围。
6. **persona 真人身份**：`Wei Wang` 为站内声明作者，能否独立核验标 U（GSC/身份证明未提供）。

---

## 附：证据采样记录

- sitemap：840 loc（同源 .net）；dist 1039 HTML / 594 `.md` / 3 `.json`。
- canonical：840/840 自引用正确；新模块 `/compare/` `/technology/` `/technology/[entity]/` 均自引用。
- sitemap 排除面：197（分页 13 + 标签 184），0 orphan 可索引页。
- noindex：199 页（分页 13 + 标签 184 + 404 + 500），0 混入 sitemap；597 端点缺口已修。
- title/desc：840 标题 0 重复 / 840 描述 0 重复。
- JSON-LD：15 页抽检，`aggregateRating`/`review`/`seller` 0 命中；类型 Vehicle/Article/WebSite/BreadcrumbList/WebApplication/DefinedTerm/CollectionPage/Dataset 分布正确。
- 渲染：车型 5/5 五段+40HQ+Data Sources；技术 5/5 def/src/rel；对比 1/1。
- 内链：109,589 条，0 断链；首页/车型页含 /compare/ + /technology/ 入口。
- 迁移：NOINDEX 597 已执行（X-Robots-Tag，6 文件）；REDIRECT/MERGE/REMOVE 均 0 执行。
