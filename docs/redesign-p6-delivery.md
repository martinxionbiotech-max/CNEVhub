# ElectricVehicleHub 重设计 — Phase 6 交付包（收口批）

> **对象**：生产站 `https://electricvehiclehub.net/`（仓库 `repos/CNEVhub`，`main`）
> **框架**：`phase2/54-evhub-redesign-prompt.md`（PHASE 6 交付纪律：小步可回滚 · 已验证 vs 建议分层 · 不破坏性操作）
> **前置报告**：`redesign-p1-audit.md` / `-p2-architecture.md` / `-p3-data-quality.md` / `-p4a-template-port.md` / `-p4b-new-modules.md` / `-p5-seo-validation.md`
> **时间**：2026-10-22（UTC）
> **数据可用性**：GSC 未提供，排名/收录结论标 U，不归因（沿用 P1/P5 口径）

---

## 〇、收口摘要

六阶段全部落地，**12 笔代码提交 + 6 笔文档提交**，工作树干净、`origin/main` 同步 **0/0**。最终站点 **1039 个 HTML 页 / sitemap 840 URL / 597 条机器可读端点 noindex**，全站技术验证七项全绿，无 P0/P1 阻断项。

**核心结论（已验证 vs 建议分层）**：
- **已验证落地**：车型页五段深度档案（517/517 去模板化）、`/data/vehicles.json` 端点 12→37 字段、规格分层 5 层、CLTC/WLTP/EPA 分字段、`/compare/` 交互工具、`/technology/` 137 实体页、597 条 `.md`/`.json` 端点 noindex。
- **建议分层（未落地，待人工决定）**：`/markets/[country]/`（30 页）、`/guides/`、`/research/`、`/quote/`、`/manufacturers/` 五模块为 P2 设计建议，本六阶段**刻意未交付**（见 §五 B 清单）。

---

## 一、六阶段执行摘要

| 阶段 | 交付物 | commit 范围（代码/文档） | 已验证结果 | 建议分层（未落地） |
| :--: | :--- | :--- | :--- | :--- |
| **P1 审计** | `docs/redesign-p1-audit.md` | 文档 `058ccbb`（0 代码） | 两站同源分叉、sitemap 均 701、`/data/vehicles.json` 仅 12 字段、Overview 模板化 mean 84 词、URL 建议表 KEEP 92 / IMPROVE 609 / NOINDEX 597 | 无（纯只读） |
| **P2 架构** | `docs/redesign-p2-architecture.md` | 文档 `5535834`（0 代码） | 九模块 IA 总表、URL 迁移映射表（REDIRECT 0 / MERGE 0 / NOINDEX 597 / REMOVE 0）、Schema 归属表 | `/markets/[country]/` `/guides/` `/research/` `/quote/` `/manufacturers/` 五模块仅登记、未落地 |
| **P3 数据质量** | 端点字段扩展 + 规格分层 + 续航分字段 | 代码 `bb92e8c` `7b8fc8a` `b60d412` + 文档 `b6a4200` | 端点 12→**37 字段**；`spec_source_type` 517/517 分层（333/163/21）；`range_wltp_km`/`range_epa_km` 分字段（WLTP/EPA 全 null，零换算）；build 900 页 | WLTP/EPA 逐车型官方补录（有来源才填） |
| **P4a 模板移植** | 车型页五段深度档案 | 代码 `eac95d5` `d6a2835` `d5f6f09` `624e128` `3073f45` `771e194` + 文档 `46cf700` | schema 40→**63 字段**；五段档案 + 40HQ 装箱 + 竞品矩阵；517/517 去模板化（6506 深度字段值）；42 处域名内链回退 `.net`（0 泄漏）；sitemap 701 不变 | 深度字段低覆盖（WLTP/FOB/阻力系数/离地间隙）待有来源补录 |
| **P4b 新模块** | `/compare/` + `/technology/` | 代码 `c4625d7` `aaf3b3b` + 文档 `e4d1814` | 新增 **139 URL**（compare 1 + 技术枢纽 1 + 实体 137）；技术实体 137/137 渲染（`related_vehicles` 仅 23 实体有值，其余诚实空态）；build 900→**1039**；sitemap 701→**840** | `/technology/battery/` 等分类子枢纽（P2 记「可选」）；`related_vehicles` 关联扩展（数据层） |
| **P5 SEO 验证** | 技术验证 + 迁移执行 + 待批准登记 | 代码 `4407165` + 文档 `0cdb5f8` | 七查全绿：canonical 840/840、sitemap 840 全落地、noindex 0 混入、title/desc 0 重复、JSON-LD 零虚构、SSR 10/10、内链 109,589 条 0 断链；**NOINDEX 597 已执行** | 4 处 schema 冗余 S1–S4 清理（非阻断）；R1 删除项待批准 |

> **计数口径说明**：任务描述「build 1037 页」与实际**不符**——实测 `dist` 为 **1039 个 HTML 文件**（P4b/P5 报告均记 1039，`find dist -name '*.html' | wc -l` 复测 1039）。本报告以 **1039** 为已验证终态。

---

## 二、URL 变更总表（全程）

### 2.1 新增 URL（139，已落地，无迁移）

| 新 URL 模式 | 数量 | commit | 数据源 |
| :--- | :---: | :--- | :--- |
| `/compare/` | 1 | `c4625d7` | vehicles content collection + `landed_cost_markets` |
| `/technology/`（枢纽） | 1 | `aaf3b3b` | `technical-master.json` |
| `/technology/[entity]/`（实体页） | 137 | `aaf3b3b` | `technical-master.json`（137 实体） |
| **合计** | **139** | — | — |

实体分布：battery 39 / charging 36 / drivetrain 23 / thermal 13 / range 11 / body-safety 15。

### 2.2 迁移执行项（一对一 301 目标映射）

> 权威依据 = P2 §5.1 迁移映射表。**全程 301 迁移 = 0 条**（无死链 / 0 改名 / 0 断链，按「无目标不迁」纪律未执行任何 301）。

| Action | P2 表数量 | 实际执行 | 一对一 301 目标 |
| :--- | :---: | :---: | :--- |
| **REDIRECT** | 0 | **0（未执行）** | 无（0 死链、0 死 URL、0 改名，证据见 P5 §二） |
| **MERGE** | 0（候选 2 组） | **0（未执行）** | 无（uae+saudi、turkey+indonesia 两组关税/VAT 口径实质不同，维持保留） |
| **NOINDEX** | 597 | **597（已执行）** | 不适用 301（用 `X-Robots-Tag: noindex`，非 301 迁移） |
| **REMOVE** | 0 | **0（未执行）** | 无（1 个仓库残留文件进待批准清单 §五 A） |

**NOINDEX 597 明细（commit `4407165`）**：
- `/vehicles/[slug].md` 517 + `/blog/[slug].md` 77 = **594 个 `.md` 变体** → `X-Robots-Tag: noindex`
- `/data/{vehicles,brands,tariffs}.json` = **3 个 JSON 端点** → `X-Robots-Tag: noindex`
- 实现位置：`public/_headers`（Cloudflare Pages 边缘层）+ 5 个端点 `.ts`（源码层 `Response` headers 双保险）

### 2.3 待批准 REMOVE 清单

| 项 | 位置 | 内容 | 建议 |
| :--: | :--- | :--- | :--- |
| R1 | `src/pages/brands/_t.txt` | `hello123`（9 字节） | 人工确认后 `git rm`（`_` 前缀在 Astro 不产路由，不影响线上 URL，属仓库垃圾） |

---

## 三、回滚手册（逐 commit revert）

> 原则：**逆序单命令回滚**，`git revert` 生成新 revert 提交保留历史；每阶段独立可回滚，回滚后 `npm run build` 即回到对应前状态。

### 3.1 分阶段回滚

| 阶段 | 回滚命令 | 回滚后站点状态 |
| :--- | :--- | :--- |
| **P5 回滚**（撤销 noindex） | `git revert 4407165` | 597 端点恢复可索引（回到 P4b 状态） |
| **P4b 回滚**（撤销新模块） | `git revert aaf3b3b c4625d7` | 站点回 **900 页**（technology→901，compare→1038，全量→900） |
| **P4a 回滚**（撤销模板移植） | `git revert 771e194 3073f45 624e128 d5f6f09 d6a2835 eac95d5` | 车型页回 84 词固定句式，schema 去 23 深度字段 |
| **P3 回滚**（撤销数据改造） | `git revert b60d412 7b8fc8a bb92e8c` | 端点回 **12 字段**，去 spec_source_type / WLTP/EPA 分字段 |

### 3.2 全量回滚（单命令）

```bash
git revert 4407165 aaf3b3b c4625d7 771e194 3073f45 624e128 d5f6f09 d6a2835 eac95d5 b60d412 7b8fc8a bb92e8c
```

### 3.3 特殊项恢复

```bash
# 若误删 R1 待批准项
git checkout HEAD~1 -- src/pages/brands/_t.txt

# 仅撤销 NOINDEX 的 6 文件（手工回退，非 revert）
git checkout HEAD~1 -- public/_headers \
  "src/pages/vehicles/[slug].md.ts" "src/pages/blog/[...slug].md.ts" \
  src/pages/data/vehicles.json.ts src/pages/data/brands.json.ts \
  src/pages/data/tariffs.json.ts
```

---

## 四、构建与测试结果汇总（终态）

| 验证项 | 终态 | 证据 |
| :--- | :---: | :--- |
| 构建 | ✅ **1039 页**，exit 0 | `find dist -name '*.html' \| wc -l` = 1039 |
| sitemap | ✅ **840 URL** | `grep -o '<loc>' dist/sitemap-0.xml \| wc -l` = 840 |
| `.md` 变体 | 594（517 车型 + 77 博客） | `find dist -name '*.md' \| wc -l` = 594 |
| JSON 端点 | 3（vehicles/brands/tariffs） | `find dist -path '*/data/*.json' \| wc -l` = 3 |
| 端点字段数 | **37**（P3 前 12） | `data/vehicles.json` 517 records |
| 规格分层覆盖 | 517/517（333/163/21） | `spec_source_type` 全标注 |
| 续航分字段 | CLTC 470 / WLTP 0 / EPA 0 | 零换算，未编造 |
| canonical | 840/840 自引用正确 | 0 缺失、0 错误域名 |
| sitemap 对账 | 840 loc 全落地，0 orphan 可索引页 | dist 1039 − 199 noindex（13 分页+184 标签+404+500） |
| title/desc | 840 标题 0 重复 / 840 描述 0 重复 | 全站去重 |
| JSON-LD | 15 页抽检零虚构 rating/review/seller | 4 处 schema 冗余（非阻断，§五 B） |
| SSR 渲染 | 车型 5/5 · 技术 5/5 · 对比 1/1 | 五段 + 40HQ + Data Sources 齐全 |
| 内链 | 109,589 条，0 断链 | 新模块入口已挂 |
| 域名泄漏 | `grep electricvehiclehub.top src/` = 0 | 无 `.top` 泄漏 |
| 数据校验 | 2 条**既有** md-drift（非本批引入） | `hongqi-guoya`（HEV vs Unknown）、`xpeng-p7-plus`（Sedan vs SUV）——P3 已记 |
| git 同步 | **0/0**（HEAD == origin/main） | `git fetch` 后 `rev-list --left-right --count` = 0 0 |

---

## 五、待人工批准清单

### A. 破坏性操作（REMOVE，本批未执行）

| 项 | 位置 | 说明 | 批准后操作 |
| :--: | :--- | :--- | :--- |
| R1 | `src/pages/brands/_t.txt`（`hello123`） | 遗留测试文件，不影响线上 URL | `git rm src/pages/brands/_t.txt && git commit` |

### B. 建议分层项（P2 设计，未交付，待人工决定优先级）

| # | 建议项 | 来源 | 现状 | 说明 |
| :--: | :--- | :--- | :--- | :--- |
| 1 | `/markets/[country]/`（30 页） | P2 §5.4 | 未交付 | `market-master.json` 30 市场数据已存在，缺渲染层 |
| 2 | `/guides/` 枢纽 | P2 模块 6 | 未交付 | 博客购买指南分组入口（帖子保留 `/blog/[slug]/` 零迁移） |
| 3 | `/research/` 枢纽 | P2 模块 7 | 未交付 | 原创研究分组入口 |
| 4 | `/quote/` B2B 询价 | P2 模块 9 | 未交付 | 需表单后端（Formspree / CF Pages Functions），当前纯静态站无后端 |
| 5 | `/manufacturers/`（可选子视图） | P2 §2 | 未交付 | 品牌 `parent_manufacturer` 聚合页 |
| 6 | **首页补 `/markets/` 入口** | P2 §3.2 项 8 | ⚠️ **orphan** | `/markets/` 页存在（sitemap 内）但全站 **0 条内链指向**（`grep -rl 'href="/markets' dist/` = 0），属导航缺口 |
| 7 | schema 冗余 S1–S4 清理 | P5 §五 | 未修 | S4（技术实体双面包屑）为 P4b 引入，建议单提交删实体页内冗余 `breadcrumbLd` |
| 8 | `vehicle-master.json` 重构 | P2 §7.1 / P3 | 未做 | 陈旧分叉文件（零消费方），应由 content frontmatter 重新生成 |
| 9 | WLTP/EPA 逐车型补录 | P3/P4a | 未做 | 内容层 0 条，禁编造，需官方公告来源 |

### C. 部署事项 — Cloudflare Pages 发布后验证清单

> 生产站当前部署于 CF Pages。发布后按以下清单逐项核验（`SITE_URL` 需设为 `https://electricvehiclehub.net`，否则构建回退默认值）。

**① URL 检查**
- [ ] 首页 `/`、`/vehicles/`、`/brands/`、`/compare/`、`/technology/`、`/markets/` 均 200
- [ ] 抽 5 车型页（byd-seal / xiaomi-su7 / zeekr-001 / deepal-l07-erev / wuling-binguo）200 且五段齐全
- [ ] 抽 5 技术实体页（lfp-battery / blade-battery / 800v-architecture / wltp / cltc）200

**② Schema 测试**
- [ ] Rich Results Test 验 `/vehicles/byd-seal/`（Vehicle，无 aggregateRating/review/seller）
- [ ] 验 `/technology/lfp-battery/`（DefinedTerm）、`/compare/`（WebApplication）
- [ ] Schema Markup Validator 验首页 WebSite/Organization/Dataset/BreadcrumbList/ContactPoint

**③ 重定向验证**
- [ ] `http://` → `https://` 301；`www` → 非 www 301；尾斜杠 308
- [ ] `/sitemap.xml` → `sitemap-index.xml` 301；`/blog/page/1/` → `/blog/` 301
- [ ] 确认 `robots.txt` 维持 `Allow: /`（`/_astro/` 可抓取）

**④ 301 / noindex 检查**
- [ ] 全程 0 条 301 迁移（本设计无 URL 改名，无死链需 301）
- [ ] `/vehicles/*.md`、`/blog/*.md`、`/data/*.json` 响应头含 `X-Robots-Tag: noindex`（CF Pages 边缘层 `public/_headers` 生效）
- [ ] `sitemap-index.xml` 840 URL 全同源 `.net`，0 指向错误域名

---

## 六、最终一致性复核（15 页跨模板抽验）

> 复核方法：直接解析 `dist` 渲染产物，逐页检查模板关键标记 + schema 类型 + 内链。**15/15 通过**（除首页 `/markets/` 导航缺口为 P2 已知项）。

| # | 页面 | 模板族 | 关键检查 | 结果 |
| :--: | :--- | :--- | :--- | :---: |
| 1 | `/vehicles/byd-seal/` | 车型详情 | 五段 + 40HQ + Data Sources | ✅ |
| 2 | `/vehicles/xiaomi-su7/` | 车型详情 | 五段 + 40HQ + Data Sources | ✅ |
| 3 | `/vehicles/zeekr-001/` | 车型详情 | 五段 + 40HQ + Data Sources | ✅ |
| 4 | `/vehicles/deepal-l07-erev/` | 车型详情 | 五段 + 40HQ + Data Sources | ✅ |
| 5 | `/vehicles/wuling-binguo/` | 车型详情 | 五段 + 40HQ + Data Sources | ✅ |
| 6 | `/brands/byd/` | 品牌档案 | Organization + BreadcrumbList | ✅ |
| 7 | `/brands/xiaomi/` | 品牌档案 | Organization + BreadcrumbList | ✅ |
| 8 | `/compare/` | 对比工具 | WebApplication + 默认对比 + compare-data JSON | ✅ |
| 9 | `/technology/` | 技术枢纽 | CollectionPage + 137 实体链接 | ✅ |
| 10 | `/technology/lfp-battery/` | 技术实体 | DefinedTerm + def + src | ✅ |
| 11 | `/technology/blade-battery/` | 技术实体 | DefinedTerm + def + src | ✅ |
| 12 | `/technology/800v-architecture/` | 技术实体 | DefinedTerm + def + src | ✅ |
| 13 | `/` | 首页 | `/vehicles/` `/brands/` `/compare/` `/technology/` `/landed-cost-calculator/` 入口 | ✅（`/markets/` 无入口，§五 B-6） |
| 14 | `/vehicles/` | 车型目录 | CollectionPage | ✅ |
| 15 | `/markets/` | 市场汇总 | CollectionPage（30 市场表） | ✅ |

**五段深度档案全链路**（车型详情 5/5）：
`Entity Snapshot / Powertrain & Architecture / Dimensions & Logistics / Market Compliance & Export Profile / Benchmarking Matrix` + 40HQ 装箱 + Data Sources **全部齐全**，价格/CLTC/battery 渲染与 frontmatter 一致。

**技术实体全链路**（技术实体 3/3 + 枢纽 1/1）：定义 + 来源链接 + 关联车型/诚实空态 + DefinedTerm schema 齐全；137 实体全部可达，`related_vehicles` 仅 23 实体有值（其余诚实空态，不虚构车辆关联）。

---

## 七、收尾记录（本批）

| 项 | 结果 |
| :--- | :--- |
| 交付文档 | `docs/redesign-p6-delivery.md`（本文件） |
| commit | `p6-delivery: 收口批交付包 — 六阶段摘要 + URL 变更总表 + 回滚手册 + 构建/测试终态 + 待批准清单 + 15 页一致性复核` |
| push | `origin/main` |
| 同步 | **0/0**（HEAD == origin/main，工作树干净） |

---

## 附：全程 commit 索引（12 代码 + 6 文档）

| # | commit | 标记 | 阶段 | 类型 |
| :--: | :--- | :--- | :--: | :--: |
| 1 | `058ccbb` | P1 audit | P1 | 文档 |
| 2 | `5535834` | P2 architecture | P2 | 文档 |
| 3 | `bb92e8c` | data-quality-A | P3 | 代码 |
| 4 | `7b8fc8a` | data-quality-B | P3 | 代码 |
| 5 | `b60d412` | data-quality-C | P3 | 代码 |
| 6 | `b6a4200` | P3 report | P3 | 文档 |
| 7 | `eac95d5` | p4a-schema | P4a | 代码 |
| 8 | `d6a2835` | p4a-template | P4a | 代码 |
| 9 | `d5f6f09` | p4a-content1 | P4a | 代码 |
| 10 | `624e128` | p4a-content2 | P4a | 代码 |
| 11 | `3073f45` | p4a-content3 | P4a | 代码 |
| 12 | `771e194` | p4a-content4 | P4a | 代码 |
| 13 | `46cf700` | P4a report | P4a | 文档 |
| 14 | `c4625d7` | p4b-compare | P4b | 代码 |
| 15 | `aaf3b3b` | p4b-technology | P4b | 代码 |
| 16 | `e4d1814` | P4b report | P4b | 文档 |
| 17 | `4407165` | p5-seo noindex | P5 | 代码 |
| 18 | `0cdb5f8` | P5 report | P5 | 文档 |
| 19 | （本批） | p6-delivery | P6 | 文档 |
