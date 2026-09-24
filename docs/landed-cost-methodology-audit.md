# Landed-Cost Methodology Audit（§9–§10）

> 审计日期：2026-09-24 ｜ 审计范围：`src/lib/` 计算代码、`scripts/recompute_from_tariffs.py`、`scripts/add_vehicles.py`、`src/pages/landed-cost-calculator.astro`、`src/content/docs/landed-cost-methodology.md`、`src/data/tariffs.json`、车型页 `landed_cost` / `landed_cost_markets` 数据
> 结论基调：本审计只记录现状与差异，**不自动修改任何公式**。需人工决策项见文末清单。

## 1. 公式实现与文档的对照

文档（`landed-cost-methodology.md` / 公开方法论页）声明的公式：

```
landed_price = base_price × (1 + std_duty) × (1 + countervailing_duty) × (1 + VAT)
               + RoRo freight + customs clearance + certification + registration + inland transport
```

实现（`recompute_from_tariffs.py` / `add_vehicles.py` / 计算器页）逐项为：

```
duty   = std_rate × base
cvd    = cvd_rate × (base + duty)        # 仅 EU 且 BEV
vat    = vat_rate × (base + duty + cvd)
total  = base + duty + cvd + vat + fixed（区域固定成本） + registration（按市场）
```

**一致点**：标准关税 → 反补贴税 → VAT 的复合顺序与文档一致；CVD 仅 EU + BEV 的适用范围与文档一致；VAT 基数含关税（duty-inclusive）与文档一致。

**差异点（见 §4 编号 D1）**：文档称关税“assessed on the CIF value (car price + insurance + freight)”，但实现中关税基数 = `base_price`，未加任何运费与保险。

## 2. 成本要素清单：included / excluded / official / estimated / calculated

| §9 结构 | 成本要素 | 数据出处 | 属性 | 是否纳入 landed_cost |
|---|---|---|---|---|
| base | 出厂价 `price_usd` | 厂商 MSRP（manufacturer/spec，tier 1–3） | **official** | ✅ |
| customs | 标准关税 | tariffs.json `standard_duty_rate`（TARIC/WTO tariff） | **official 税率 × calculated 金额** | ✅ |
| customs | 反补贴税 | tariffs.json `brand_cvd`（EU Reg 2024/2754） | **official 税率 × calculated 金额**；仅 EU + BEV | ✅ |
| taxes | VAT/GST | tariffs.json `vat_rate`（各国税法） | **official 税率 × calculated 金额** | ✅ |
| logistics | RoRo 海运 | `fixed_costs.freight_roro_usd = 2000` | **evhub_estimate** | ✅ |
| logistics | 内陆运输 | `fixed_costs.inland_transport_usd = 500` | **evhub_estimate** | ✅ |
| customs | 报关费 | `fixed_costs.customs_clearance_usd = 350` | **evhub_estimate** | ✅ |
| compliance | 认证/同质化 | `fixed_costs.certification_usd = 3250` | **evhub_estimate** | ✅ |
| registration | 注册费 | tariffs.json 每市场 `registration_fee_usd`（30–3500，跨市场差异极大） | **official-ish（中心表收录，未逐市场标注出处）** | ✅ |
| — | 保险（CIF 中的 I） | 无任何字段 | **excluded** | ❌（文档提及 CIF 但未实现） |
| — | 汇率（USD/CNY、EUR 波动） | 无字段 | **excluded** | ❌ |
| — | 融资/经销商加价/零售毛利 | 无字段 | **excluded** | ❌（B2B 口径，文档已声明） |
| — | 滞港费、堆存费、检验检疫 | 无字段 | **excluded** | ❌ |
| — | 本地特有税（新加坡 ARF/COE、土耳其特殊消费税等） | 无字段 | **excluded** | ❌ |
| — | 年检/年度道路税 | 无字段 | **excluded** | ❌ |

## 3. 按市场差异审计

30 个市场全部参与计算，关税/VAT/注册费逐市场取值（见 tariffs.json `markets`）。区域性差异点：

- **区域固定成本**（运费+报关+认证+内陆，不含注册费）在 `scripts/add_vehicles.py` 与计算器页以 `REGION_BASE_FIXED` 常量出现：EU 6100 / Non-EU Europe 5850 / Middle East 4150 / Oceania 5350 / Southeast Asia 4600 / North America 7000 / Latin America 6500 / Africa 6200。该常量**不在 tariffs.json `fixed_costs` 里**（中心表只有 2000/350/3250/500 一组 Germany 口径值）。
- **车型页 `landed_cost_markets` 的固定成本**由 `recompute_from_tariffs.py` 反解（`fixed = total_old − base − duty − cvd − vat`）保留——即各市场固定成本是从旧总额**倒推**的，非从中心表正向计算。用 hongqi-guoya 复核，反解值与 `REGION_BASE_FIXED + registration_fee` 完全一致，但方法上是“保留历史值”而非“从源表重算”。
- **注册费跨市场跨度大**（丹麦 3500、挪威 1400、以色列 700、瑞典 70、新西兰 23），已被计入总额。此项的每市场出处未在 tariffs.json 中标注来源（`source-master.json` 无对应条目）→ 见决策项 H3。
- 计算器页与车型页公式结构一致（区域固定 + 注册费分开加），数值经抽样核对一致；但二者**各自维护一份区域常量副本**（页面常量与 add_vehicles.py），有漂移风险。

## 4. 与任务书 §9 结构（base+logistics+customs+taxes+compliance+registration+local）的差异

| §9 结构 | 实现映射 | 差异/备注 |
|---|---|---|
| base | price_usd | ✅ 一致 |
| logistics | freight_roro + inland_transport | ✅ 有，但 inland（“local”）并进 logistics 常量，未单列 |
| customs | std duty + CVD + clearance | ✅ 有；D1：关税基数用 base 而非 CIF |
| taxes | VAT/GST | ✅ 有；D2：VAT 基数不含运费/保险（与 CIF 口径差异联动 D1） |
| compliance | certification 3250 | ✅ 有；全国市场统一 3250，未按市场/认证路线区分（文档称 1500–5000） |
| registration | registration_fee_usd | ✅ 有，逐市场 |
| local | inland transport 500 | ✅ 有但混入 logistics 常量；本地杂费（license plate、检验）未单列 |

**结构缺失**：§9 的 “local” 仅以内陆运输一个数字代表；无保险（I of CIF）、无本地特有税、无 FX 条款。

## 5. 发现清单（不自动修）

- **D1（公式/文档偏差）**：关税基数 = base，未含运费+保险。文档文字（CIF 口径）与实现（base 口径）不一致。若按 CIF 口径，所有市场 duty/VAT 都会上升，影响 517 台 × 30 市场全量数字。
- **D2（文档内部不一致）**：公开方法论页 CVD 表只列 BYD/Geely/SAIC/Other（18.8–35.3%），未列 Tesla 7.8%（数据源 `brand_cvd.tesla=0.078` 已存在）；内容文档写 “Other cooperating ~20.8%”，实现用 0.207（20.7%）。
- **D3（单一数据源缺口）**：区域固定成本（REGION_BASE_FIXED）不在 tariffs.json 中心表，散落在 add_vehicles.py 与计算器页两个副本。
- **D4（注册费溯源缺口）**：30 市场注册费出处未在 source-master.json 登记；丹麦 3500 等大值项影响 premium 数个百分点。
- **D5（反解 vs 正向计算）**：landed_cost_markets 的固定成本经反解保留；若某车旧数据有错，错误会被“保留”而非被中心表纠正。
- **D6（认证费全国统一）**：certification 统一 3250；文档承认 1500–5000 区间且欧盟整车型式 vs 单车认证路径差异大。欧洲以外（GCC/东南亚）实际认证成本结构不同。

## 6. 需人工决策项

| # | 决策 | 选项 | 建议 |
|---|---|---|---|
| H1 | D1 关税基数 | (a) 保持 base 口径并改文档；(b) 改为 CIF 口径重算全站 | 改文档（低风险），口径升级留后续批量决策 |
| H2 | D3 区域固定成本入中心表 | (a) 并入 tariffs.json `fixed_costs`（按区域）；(b) 保持现状 | 并入中心表，消除双副本 |
| H3 | D4 注册费逐市场出处 | 补 source-master 条目 | 补，逐市场一行 |
| H4 | D5 反解改为正向重算 | 用中心表正向重算 30 市场固定成本 | 与 H2 联动做 |
| H5 | D6 认证费分市场/分路线 | 按市场组设认证费 | 后续批次 |
| H6 | Tesla 7.8% 与 20.7/20.8 表述统一 | 更新公开方法论页 | 低成本，随时可做 |

**本审计未改动任何公式、常量或 517 个车型文件的 landed_cost 数值。**
