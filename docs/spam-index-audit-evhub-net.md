# EV Hub (electricvehiclehub.net) — Spam & Index Quality 深度审计报告

> **审计对象**：https://electricvehiclehub.net/
> **审计模式**：READ_ONLY（严格只读 — 仅诊断推演 + 报告，零修复、零代码改动）
> **审计时间**：2026-10-19（UTC）
> **仓库**：`repos/CNEVhub`（线上站 = 本仓 Astro 构建产物）
> **站点画像**：Astro（Virex SaaS 主题二次开发）· 517 车型 / 72 品牌 / 86 博客（77 已发布 + 9 草稿）/ 14 文档 · 30 出口市场 landed-cost 测算 · **目录数据库 + 知识库混合型** · 稳定运营期
> **数据可用性**：GSC_DATA = **未提供**（所有依赖 GSC 的结论标「数据缺失 U」，禁止把无数据项写成风险）
> **框架依据**：`phase2/53-spamcheck-audit-framework.md`

---

## 〇、执行摘要（Executive Verdict）

**核心判定**：**未发现明确垃圾政策违规证据**。本站在 Google Spam Policy 维度合规度极高，属于「诚实的数据情报站」而非「规模化内容农场」。

**一句话总结**：EV Hub 是一个透明度与数据溯源做得异常扎实的 EV 进口情报站（明确声明「不卖车、不隶属任何主机厂」、逐页 landed-cost 拆解、data_tier/data_source/data_updated 三层溯源、完整法律页），当前 Google 体系下的最大阻碍**不是 Spam，而是内容差异化不足**——517 车型页的正文散文（Overview）由同构模板批量生成（平均仅 ~94 词、句式骨架完全相同），这是全站规模最大的内容集群，却也是唯一逼近「Scaled Content」信号的面。

**红线声明（贯穿全文）**：本报告所有「未发现异常」结论均附 URL / HTTP / HTML 证据；无证据处明确写「证据不足」。GSC 缺失项一律 U，不做归因推演。

---

## 一、维度风险评分表

| 评估维度 | 分值 (0-5/U) | 证据强度 | 核心发现与影响面 |
| :--- | :---: | :---: | :--- |
| 1. Spam Policies 违规 | **0** | 高 | 十项垃圾滥用核查零硬违规；无隐藏文本、无伪造 Schema、无 Cloaking、无寄生页、无垃圾注入 |
| 2. 内容独创性与有用性 | **2** | 中 | 数据价值高（landed_cost 独有测算），但 517 车型页 Overview 散文同构模板化（~94 词），品牌页偏薄（~507 词） |
| 3. 技术抓取与索引表现 | **1** | 高 | 静态 SSR 正文+内链全量输出；robots/sitemap/noindex 一致；仅 .md 变体与 /data JSON 端点可索引却未 noindex |
| 4. 架构与重复内容膨胀 | **2** | 高 | 184 标签页（已正确 noindex）、分页（已 noindex）；但 517 个 .md 变体 + 3 个 JSON 端点构成潜在重复内容面 |
| 5. 商业真实性与 EEAT | **1** | 高 | 主体披露、不卖车声明、作者资质、方法论、溯源体系齐备；仅 data_reviewed 全为 false、llms.txt 计数陈旧 |

---

## 二、十大垃圾滥用风险逐项核查（证据链第一）

### 1. Scaled Content Abuse（规模化内容滥用）— **低风险，非违规**

- **证据**：517 个车型页正文 Overview 段为**同构模板 + 变量槽位填充**。抽取 6 款（aion-lx / byd-seal / byd-atto-3 / xiaomi-su7 / tank-300 / wuling-binguo），句式骨架完全一致：
  > "The **[X]** is a **[尺寸] [车身] [动力形式]** from **[品牌]**，with **[功率] kW of motor power, a [X]-second 0–100 km/h time. It is positioned as a **[价值定位]** import, priced from $**[价格]** ex-factory. For importers, the cheapest entry point is **[最便宜市场]** at roughly +**[X]%** over base…"
- **量化**：517 篇 Overview 词数 min=30 / max=124 / mean=93.9 / median=96；数字掩码后仅个别重复骨架（top-3 各仅 2 款撞车），说明槽位填充变化度尚可，但句式模板单一。
- **关键豁免**：每页的**数据层是真正唯一的**——30 市场 landed-cost 表、逐项成本拆解（duty/countervailing/VAT/freight/certification）、规格表、data_source 引用。正文散文只是「包装层」，不是「内容主体」。
- **结论**：属于**低强度 scaled-content 信号**（模板化散文），但**不构成硬违规**——无证据表明是纯 AI 无价值拼接，数据主体有真实独家价值。

### 2. Site Reputation Abuse（站点声誉滥用 / Parasite SEO）— **未发现异常**

- **证据**：全站 URL 语义纯 EV 进口情报（/vehicles/ /brands/ /blog/ /docs/ /markets/），无任何脱节第三方子目录（无 /loan/ /gambling/ /coupon/ /casino/ 类寄生页）。sitemap 701 URL 全部属于本站主题。footer 外链仅 GitHub（本仓）+ X（官方账号）。
- **结论**：**未发现异常**。

### 3. Expired Domain Abuse（过期域名滥用）— **未发现异常（域名历史 = 证据不足 U）**

- **证据**：当前主题（中国 EV 出口 landed-cost 情报）与站名/品牌/内容完全一致，无「旧权重卖无关品类」的欺骗性断层迹象。
- **边界**：纯外部只读视角无法核验域名注册历史 / 是否曾过期转手（需 WHOIS/Archive.org 历史）。
- **结论**：**当前内容无断层，未发现异常**；域名历史本身 **U（证据不足，需人工提供）**。

### 4. Doorway Abuse（门页/桥页滥用）— **未发现异常**

- **证据**：博客存在国家/地区导向的 import guide 集群（austria / belgium / brazil / canada / australia / poland / germany 等）。抽查 4 篇词数：Austria 3195、Belgium 3765、Brazil 1486、Canada 1885 词，且每篇关税/VAT/配额口径**实质不同**（Austria 20% VAT+NoVA、Belgium 21% VAT+安特卫普港、Brazil 35% BEV 关税+级联税、Canada 6.1% MFN+4.9 万配额）。
- **关键豁免**：本站**无任何转化/销售漏斗**（不卖车），不存在「所有门页导向同一转化路径」的门页定义前提。
- **结论**：**未发现异常**（内容差异化、非桥接页）。

### 5. Scraped & Thin Content（采集与低附加值内容）— **未发现异常（有独家价值）**

- **证据（实测判定为有独家价值）**：
  - 每车型 30 市场 landed-cost 测算（`landed_cost_markets` 逐市场 total_landed_usd/premium_pct），并配逐项拆解表，明确区分「Source data（官方 MSRP/欧盟关税）」与「EV Hub calculation（运费/认证/注册 = 估算，页面标注 amber 徽章）」。
  - 方法论公开可复算（/landed-cost-methodology/、/methodology/），关税锚定 EU Reg 2024/2754。
  - 博客样例（byd-seal-deep-review）5681 词、71 处 "source" 引用。
  - data_source 字段非模板敷衍：314 条为统一口径，另 ~203 条为**中文具体出处**（如「风行雷霆410 RMB 99,800 (东风风行官网)」「零跑D99 RMB 249,800 (新浪汽车/CCTV, 2026-06-25)」），证明存在人工采集痕迹。
- **结论**：**未发现异常**——数据表格具有真实独家计算价值，非 RSS 聚合 / 机器翻译 / 空表。

### 6. Link Spam（链接作弊与操纵）— **未发现异常**

- **证据**：车型页出站外链仅 3 个——图片来源（`commons.wikimedia.org`，`rel="nofollow noopener"`）、GitHub 本仓（`rel="noopener noreferrer"`）、X 官方账号（同上）。**无 dofollow 锚文本赞助外链、无站群交叉强制链接**（单域名，未发现关联镜像站）。
- **结论**：**未发现异常**。

### 7. Cloaking & Sneaky Redirects（掩蔽/欺骗性重定向）— **未发现异常**

- **证据（Googlebot UA 对比实测）**：
  - 普通 UA 与 `Googlebot/2.1` UA 抓取 /vehicles/aion-lx/，**正文与 JSON-LD 字节级一致**（均 62168 字节）。
  - diff 唯一差异 = Cloudflare 的 `data-cfemail` / `/cdn-cgi/l/email-protection` 邮箱混淆密钥**每次请求轮换**（正文零差异）→ **假阳性，非 Cloaking**。
  - 重定向全链干净：`http→https` 301、`www→非 www` 301、`/vehicles/aion-lx→/vehicles/aion-lx/` 308、`/sitemap.xml→/sitemap-index.xml` 301。无欺骗性跳转。
- **结论**：**未发现异常**。

### 8. Structured Data Abuse（结构化数据作弊）— **未发现异常（复核已修口径）**

- **证据（aion-lx 页 5 个 JSON-LD block 全解析）**：
  - `Vehicle` 节点含 `offers`（price=40370，与页面可见 $40,370 同源；`description` 明确「China ex-factory price (MSRP) — indicative… before freight, duties and certification」）；**不声明 seller**。
  - **全页无 `aggregateRating` / `review` / `reviewCount` / `ratingValue`**（grep 命中数 = 0）→ **零虚构评分/评论**。
  - `Person` 作者 = "Wei Wang"（配真实 bio/jobTitle，非虚构 persona）；`Organization` = 完整 legalName + 地址（Jinzhou, Hebei, CN）+ 邮箱 + sameAs。
- **结论**：**未发现异常**（「Vehicle+offers 已修」口径复核通过，无 0 虚构 rating/review/persona）。

### 9. Hidden Text & Keyword Stuffing（隐藏文本/关键词堆砌）— **未发现异常**

- **证据**：车型页 + 首页 grep `display:none / visibility:hidden / opacity:0 / text-indent:-* / font-size:0` 命中数 = **0**。title/meta description/H1 品牌拼写一致、无数字宣称堆砌。
- **结论**：**未发现异常**。

### 10. Hacked Content & Spam Injections（被黑/垃圾参数注入）— **未发现异常**

- **证据**：
  - 垃圾参数探测：`?s=viagra` / `?poker` / `?casino` / `?page=999999` 均返回 **200 但内容 = 首页正文**（静态站忽略 query，无垃圾内容生成，title 仍为「EV Hub — The Real Landed Cost…」）。
  - `?q=купить+машину` / `?日本車` 返回 **400**（Cloudflare WAF 拦截，非垃圾内容）。
  - `/wp-admin` = **404**（非 WordPress，无 WP 攻击面）。
  - 无俄语博彩目录、无日文乱码（Japanese Keyword Hack）页面。
- **结论**：**未发现异常**。

---

## 三、页面价值与 EEAT 抽样（§3）

### 3.1 People-First 判定

| 模板 | 抽样 URL | 词数（可见正文） | People-First 判定 |
| :--- | :--- | :---: | :--- |
| 首页 | `/` | 524 | ✅ 价值主张清晰，主内容零广告 |
| 车型页 | `/vehicles/aion-lx/` | ~1034 | ✅ 数据优先，正文未被掩埋 |
| 品牌页 | `/brands/aion/` | ~507 | ⚠️ 偏薄（品牌简介 + 车型列表，附加值有限） |
| 博客文章 | `/blog/byd-seal-deep-review/` | 5681（71 引用） | ✅ 深度原创 |
| 国家指南 | `/blog/austria-import-guide/` | 3195 | ✅ 差异化实质内容 |

**关键正面信号**：全站 **0 广告、0 侵入式插页**，主内容（Main Content）未被掩埋——这是反「Search-Engine-First」的最有力证据。

### 3.2 数据源口径核验（data_tier / data_source / data_updated）

- **三层溯源体系已落地并运行**：
  - `data_tier`：333×tier1 / 163×tier2 / 21×tier3（共 517）。
  - `data_source`：314 条统一口径 + ~203 条中文具体出处（见 §2.5）。
  - `data_updated`：314×2026-09-07 / 202×2026-09-14 / 1×2026-09-24。
  - `data_reviewed`：**517 条全部 = false**（页面如实渲染「Pending review」）。
- **诚实性加分**：模板层将「Source data」与「EV Hub calculation」视觉二分，估算项明确 amber 标注 + Confidence 标签，不虚标「Reviewed」。

### 3.3 透明度与商业合规（本店不卖车：如实声明口径核验）

- **About 页**：明写 *"We do not sell vehicles and are not affiliated with any manufacturer. That independence is what lets us report prices and tariffs without a sales agenda."* ✅
- **Disclaimer 页**：*"Information Platform, Not an Advisor or Dealer… We do not sell vehicles… Landed-Cost Estimates Are Approximate"* ✅
- **法律页齐备**：Privacy(1006 词) / Terms / Cookie Policy / Disclaimer / Copyright & Takedown / Accessibility / Image Credits 全部 200 且内容实质。
- **主体披露**：公司全名（Jinzhou Chengguang Power Source Co., Ltd.）+ 地址（Jinzhou, Hebei, China）+ 邮箱（info@electricvehiclehub.net）+ IATF 16949 认证声明（在 About/Schema 一致）。

### 3.4 索引膨胀（Index Bloat）

- **标签页**：`/blog/tag/` 共 **184 个**，全部 `<meta name="robots" content="noindex,follow">`（实测 /blog/tag/import/ 确认）✅ 已正确排除索引。
- **分页**：`/blog/page/2/` noindex,follow ✅。
- **无 faceted/筛选参数页**：query string 全部返回首页正文，无 `?filter=`/`?price=` 类膨胀页。
- **隐患**：517 个 `/vehicles/[slug].md` 变体 + 3 个 `/data/*.json` 端点**可索引**（详见 §4）。

---

## 四、技术 SEO 全链路核验（§4）

### 4.1 软 404

- 无效车型 `/vehicles/wuling-mini-ev/` → **HTTP 404**，404 页含「Page Not Found」标题 + 导航，非软 404。✅
- sitemap 随机 12 URL 抽查全部 **200**。✅

### 4.2 robots / sitemap / noindex 冲突

- `robots.txt`：`Allow: /`（仅 `Disallow: /api/`），并正确保留 `/_astro/` 可抓取；显式 Allow GPTBot/ClaudeBot/Google-Extended 等 AI 爬虫（GEO/AIO 友好）。✅
- `sitemap-index.xml` → 1 个 `sitemap-0.xml`，**701 URL**（518 vehicles 含索引页 / 78 blog / 73 brands / 15 docs / 法律+工具页）。
- **一致性闭环**：sitemap 中 **0 个 `/blog/tag/`、0 个 `/blog/page/`、0 个 `.md`、0 个 noindex URL**——与 meta noindex 指令无自相矛盾。✅

### 4.3 Canonical / 斜杠 / 大小写闭环

| 变体 | 结果 |
| :--- | :--- |
| 无斜杠 `/vehicles/aion-lx` | 308 → `/vehicles/aion-lx/` ✅ |
| 大写 `/Vehicles/Aion-LX/` | 404（大小写敏感，可接受）|
| `http://` | 301 → https ✅ |
| `www.` | 301 → 非 www ✅ |
| 双斜杠 `/vehicles//aion-lx/` | **200（未规范化，低危）** ⚠️ |

- canonical 自引用带尾斜杠（`<link rel="canonical" href=".../vehicles/aion-lx/">`）✅。

### 4.4 SSR 渲染验证

- Astro 静态构建：初始 HTML 已含**正文 + 完整规格表 + landed-cost 表 + 内链 + JSON-LD**，无需执行客户端脚本即可抓取。Googlebot UA 与普通 UA 正文字节级一致（§2.7）。✅

### 4.5 移动视口

- 主题含响应式 Tailwind 栅格（`grid-cols-2 md:grid-cols-3` 等）+ viewport meta；无侵入式插页。✅（未做真机渲染，视觉细节标注「未实测」）

### 4.6 可索引但未 noindex 的重复/数据面（技术隐患）

- `/vehicles/[slug].md`（517 个，`text/markdown` 200）与 `/data/{vehicles,brands,tariffs}.json`（200 application/json）**均无 `X-Robots-Tag`、不在 sitemap、且无内部链接**。
- 影响：当前**发现/索引风险低**（无入口），但一旦被外部引用或被 Google 直接探测，将形成 517+ 页近重复内容面。属 P2 技术隐患，非 Spam。

---

## 五、GSC 归因纪律（§5）

- **GSC_DATA 未提供** → 以下结论**一律标「数据缺失 U」**，不作任何风险归因：
  - 「Discovered/Crawled - currently not indexed」分布：**U**
  - 抓取预算是否吃紧：**U**
  - Manual Action 状态：**U**
  - 曝光/排名断崖与 Core/Spam Update 时间轴比对：**U**
- **明令禁止的归因谬误已规避**：未用 `site:` 数字、未把「新站未收录」当处罚、未把模板散文当「已证实 Spam」。

---

## 六、Top 风险诊断清单（§8.三，按危害降序）

### 风险 1 — P2｜517 车型页正文散文模板化（全站最大内容集群差异化不足）
- **类型/等级**：P2 — Scaled Content 低强度信号 / Helpful Content 评级上限
- **涉及 URL**：`/vehicles/*`（517 页）
- **底层证据**：Overview 段同构骨架、mean 93.9 词（§2.1），句式 100% 复用「The [X] is a [size] [type] [powertrain] from [BRAND]…」
- **关联政策**：Google Scaled Content Abuse 政策（模板化量产低价值页）；Helpful Content 系统（原创性）
- **危害推演**：数据主体虽唯一，但 Google 对 517 页近同构散文可能降权该集群，压低全站内容质量评级；这是本站「最接近但不触线」的 Spam 面。

### 风险 2 — P2｜可索引但未 noindex 的 .md 变体 + JSON 数据端点
- **类型/等级**：P2 — 重复内容面 / 索引卫生
- **涉及 URL**：`/vehicles/[slug].md`（×517）、`/data/{vehicles,brands,tariffs}.json`（×3）
- **底层证据**：均 200、无 X-Robots-Tag、不在 sitemap、无内链（§4.6）
- **关联政策**：Consolidate Duplicate URLs（重复内容合并规范）
- **危害推演**：当前无入口故风险低；一旦被外部链接/探测发现，可能被判定为 517 页近重复、稀释权重。→ 建议对 .md / /data/ 端点加 `X-Robots-Tag: noindex`（**注意：这属于「建议」，本审计零修复**）。

### 风险 3 — P2｜184 标签页 + 品牌页偏薄（抓取预算）
- **类型/等级**：P2 — 抓取预算消耗 / 薄页
- **涉及 URL**：`/blog/tag/*`（184 个，已 noindex）、`/brands/*`（72 个，~507 词）
- **底层证据**：标签页 noindex 正确但 `follow` 仍可被抓取；品牌页词数偏薄
- **危害推演**：184 个可抓取标签页消耗抓取预算；品牌页附加值低

### 风险 4 — P3｜llms.txt 内部计数不一致
- **底层证据**：llms.txt 首段写「315 vehicle models across 58 Chinese EV brands」，下文写「517 Chinese EV models」；实测 517 车型 / 72 品牌
- **危害推演**：AI 引用口径混乱，非 Google 索引问题，但影响 AIO/GEO 一致性

### 风险 5 — P3｜双斜杠 URL 未规范化
- **底层证据**：`/vehicles//aion-lx/` 返回 200（应 301/404 归一）
- **危害推演**：极小概率被外部误链产生重复 URL

---

## 七、分级修复方案与实施路线（Action Plan — 仅建议，本审计不执行）

### P0（阻断级：安全/明确违规/人工处罚）
**无**。未发现任何需立即阻断的违规或安全项。

### P1（高收益：挽救抓取预算、解除核心技术阻碍）
**无硬性 P1**。当前无直接威胁抓取/索引的致命缺陷。

### P2（中长期：内容增值 + 实体信任 + 内链重构）

> **【去模板化车型页正文散文】**
> - **目标与原因**：解除 517 页同构散文的 scaled-content 信号，提升 Helpful Content 评级
> - **影响 URL 范围**：`/vehicles/*`（517 页）
> - **具体操作方法**：为每页 Overview 补充 1–2 句车型级独特见解（竞品定位、电池化学、出口强项/弱项、目标市场适配性），摆脱固定句式骨架
> - **风险控制与回滚**：逐批（20–25 款/窗口）改写，git 提交可逐批 revert；只动散文不动数据层
> - **效果验证指标**：改写后 Overview 词数 mean >150、句式骨架去重率提升；GSC 车型集群曝光（需数据）

> **【.md 变体 + /data/ 端点加 noindex】**
> - **目标与原因**：封堵 520 页潜在重复内容面
> - **影响 URL 范围**：`/vehicles/[slug].md`、`/data/*.json`
> - **具体操作方法**：在 `.md.ts` / `*.json.ts` 的 Response headers 加 `X-Robots-Tag: noindex`（数据仍供 API/AI 使用，不影响访问）
> - **风险控制与回滚**：纯 header 改动，单文件可回滚；先灰度 1 页验证
> - **效果验证指标**：`curl -D -` 确认 X-Robots-Tag 存在

> **【品牌页薄页增值】**
> - **目标与原因**：72 品牌页 ~507 词偏薄
> - **具体操作方法**：补充品牌出口定位、CVD 税率、代表车型 landed-cost 区间
> - **风险控制与回滚**：模板层增字段渲染，数据层可空置渲染 N/A
> - **效果验证指标**：品牌页词数 >800

### P3（边缘优化）

> **【llms.txt 计数修正】**：将「315/58」改为「517/72」一致口径
> **【双斜杠 URL 归一】**：中间件/规则将 `//` 归一为 `/` 或 404

---

## 八、未来 7 天优先执行事项（Top 5）

1. **给 .md 变体与 /data/ 端点加 `X-Robots-Tag: noindex`**（最低风险、独立可验证、封堵最大重复面）。
2. **修正 llms.txt 计数**（315→517、58→72，纯文本一致性）。
3. **起一窗「去模板化散文」试点批**（选 20 款高出口价值车型，改写 Overview，验证 build + 渲染 + commit）。
4. **申请开通 GSC**（当前无数据是归因盲区；手动拉取「页面索引」与「抓取统计」报表）。
5. **核验域名历史**（WHOIS / Archive.org），闭环 §2.3 的 Expired Domain 证据缺口。

---

## 九、红线警告（现在绝对不能做的三件事）

1. **禁止一键批量删除/301 517 个车型页或 184 个标签页**——标签页已正确 noindex，车型页是核心流量与转化价值资产，批量删除=灾难性流量损失。
2. **禁止在 `robots.txt` 里 `Disallow: /blog/tag/` 或 `Disallow: /_astro/` 替代 noindex**——noindex 才是正确指令；误 block `/_astro/` 会直接导致 Googlebot 无法渲染（GSC 报 "blocked resource"），本仓 robots.txt 已显式注释此点。
3. **禁止给车型页补虚构 `aggregateRating`/`review`/`offers.seller` 以「增强富结果」**——这是会把「0 违规」直接升级为「可触发 Manual Action 的 Structured Data Abuse」的最危险操作，现口径（价格同源 + 无评分无评论）必须保持。

---

## 十、需人工介入 / 提供更多数据的待办项（§8.八）

| # | 待办项 | 原因 | 阻塞的结论 |
| :--- | :--- | :--- | :--- |
| 1 | **GSC 数据**（页面索引报表 / 抓取统计 / Manual Action / 覆盖率） | 纯外部只读无法获知 | 抓取预算、收录率、是否被算法降权（当前全 U） |
| 2 | **域名历史**（WHOIS 注册时间 / 是否过期转手 / Archive.org 快照） | 需历史记录服务 | §2.3 Expired Domain 证据闭环 |
| 3 | **服务器访问日志**（Googlebot 抓取频率 / 429/5xx） | 无后端权限 | 抓取预算是否被标签页消耗的实际量级 |
| 4 | **真机移动端渲染截图** | 无浏览器渲染环境 | §4.5 移动视口视觉细节 |
| 5 | **出站链接主动核查**（GitHub/X 是否为公司官方账号的授权确认） | 外部只读无法坐实 | 虽无 dofollow 赞助链，但账号归属需人工确认 |

---

## 附：证据采样记录（原始数据快照）

- 内容规模：517 车型 / 72 品牌 / 86 博客（77 发布 + 9 草稿）/ 14 文档
- sitemap：`sitemap-index.xml` → `sitemap-0.xml`（53,201 字节，701 URL）
- 溯源分布：data_tier 333/163/21；data_reviewed 517×false；data_updated 314@09-07 / 202@09-14 / 1@09-24
- 词数采样：车型 article ~1034、Overview ~94、品牌 ~507、首页 524、博客 5681、国家指南 1486–3765、Privacy 1006
- Cloaking 实测：普通 UA vs Googlebot 字节级一致（唯一差异 = Cloudflare email 混淆密钥轮换）
- Schema：5 block（WebSite/Organization/BreadcrumbList/Article/Vehicle），无 aggregateRating/review/reviewCount/ratingValue
- 垃圾参数：?s/?poker/?casino/?page=999999 → 200 首页内容（无垃圾生成）；?q=西里尔/日文 → 400（WAF）；/wp-admin → 404
