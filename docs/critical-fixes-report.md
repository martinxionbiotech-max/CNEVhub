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
