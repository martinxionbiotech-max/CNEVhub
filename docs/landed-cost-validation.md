# Landed-Cost & Export Content — Phase 5 Validation Report

> 核验日期：2026-10-22 ｜ 范围：CNEVhub（electricvehiclehub.net）计算器 + 方法论文档 + 数据三方对账；chinaevmart（chinaevmart.com，仓 electricvehiclehub.top）交叉一致性说明。
> 结论基调：**公式与数据一致**；发现 3 处文档/代码措辞偏差（已修，均为文案层）、1 处文档行项错误（已修）、若干溯源/口径缺口（**待人工复核**，未当已确认事实呈现）。

---

## 1. 三方对账结论（公式 · 文档 · 数据）

### 1.1 计算实现定位

落地成本由**三处并行实现**，公式结构完全一致：

| 实现位置 | 角色 |
|---|---|
| `src/pages/landed-cost-calculator.astro`（前端 JS `calc()`） | 交互式计算器（10 精选车型 × 30 市场） |
| `scripts/add_vehicles.py` / `scripts/extend_markets.py` | 批量生成车型页 `landed_cost` + `landed_cost_markets`（30 市场） |
| `scripts/recompute_from_tariffs.py` | P0 一致性重算（保留旧 fixed 反解值） |

**核心公式（三处一致）**：

```
duty = standard_duty_rate × base
cvd  = cvd_rate × (base + duty)        # 仅 EU 且 BEV；PHEV/EREV/HEV/非EU 市场 = 0
vat  = vat_rate × (base + duty + cvd)
fixed = REGION_BASE_FIXED[region] + registration_fee_usd
total = base + duty + cvd + vat + fixed
```

方法论文档声明的公式块 `base × (1+std_duty) × (1+cvd) × (1+VAT) + 固定项` 与代码**代数恒等**（已用 BYD Dolphin / Seal / MG 4 / Qin Plus DM-i / Aito M9 EREV 逐项复核）。

### 1.2 成本构成核对（无遗漏 · 无重复）

| 成本要素 | 数据出处 | 属性 | 结论 |
|---|---|---|---|
| 出厂价 `price_usd` | 车型 frontmatter（厂商 MSRP） | official | ✅ 基数，未重复计入 |
| 标准关税 | `tariffs.json` `standard_duty_rate` | official 税率 × 计算 | ✅ 单次 |
| 反补贴税 (CVD) | `tariffs.json` `brand_cvd`（EU Reg 2024/2754） | official 税率 × 计算 | ✅ 单次，仅 EU+BEV |
| VAT/GST | `tariffs.json` `vat_rate` | official 税率 × 计算 | ✅ 单次 |
| RoRo 海运 | 区域固定成本内（中心 `fixed_costs.freight_roro_usd=2000`） | 估算 | ✅ 单次 |
| 报关费 | 区域固定成本内（`350`） | 估算 | ✅ 单次 |
| 认证/同质化 | 区域固定成本内（`3250`） | 估算 | ✅ 单次 |
| 内陆运输 | 区域固定成本内（`500`） | 估算 | ✅ 单次 |
| 注册费 | `tariffs.json` 每市场 `registration_fee_usd` | 收录值，未逐市场溯源 | ✅ 单次 |

**无重复计算**：duty/cvd/vat/fixed/registration 各计一次，复合顺序（duty→cvd→vat）正确。
**无遗漏（在声明口径内）**：8 项成本要素齐全。

### 1.3 数据一致性（517 车 × 30 市场）

- 全部 517 个车型含 `landed_cost`（Germany）+ `landed_cost_markets`（30 市场）。
- 回归脚本全量重算：**0 处真实偏差（≥$0.015）**。
- **78 处 ±$0.01 取整伪差**（cosmetic，不影响显示——站点以 `Math.round` 整元展示）：源于历史生成管线中 Germany breakdown 对 duty/cvd/vat 逐项 `r2` 后求和、而 markets 路径用全精度 + 反解 fixed 的取整顺序不一致。**非公式错误**，见 §4-6。

---

## 2. 修正清单（已执行）

### 2.1 CNEVhub（.net）— 文案/文档对齐

| # | 文件 | 修正 | 依据 |
|---|---|---|---|
| F1 | `src/pages/landed-cost-methodology.astro` | 「标准关税按 CIF 值计」→「按出厂基价计」，注明 CIF 为严格口径的保守简化 | 代码 `duty = std × base`，不含运费/保险 |
| F1 | `src/content/docs/landed-cost-methodology.md` | 同上，并新增「运费/保险不计入应税基数」说明 | 同上 |
| F2 | `src/pages/landed-cost-methodology.astro` | CVD 表补 Tesla 7.8% + other-cooperating 20.7%，标题「17%–35.3%」→「7.8%–35.3%」 | EU Reg 2024/2754 全档税率 |
| F2 | `src/content/docs/landed-cost-methodology.md` | 「~20.8%」→「20.7%」 | 数据源 `brand_cvd._default=0.207` |
| F3 | `src/content/docs/cost-breakdown-example.md` | UAE 固定成本 `~$6,250`→`$4,150`+注册`$300`；澳洲 `~$6,250`→`$5,350`+注册`$500` | 区域固定成本 Middle East 4150 / Oceania 5350 + 注册费 |
| F8 | 两处方法论文档 | 「Assumptions & limits」新增**排除项**（保险/汇率/本地特有税等） | 补齐口径披露 |

### 2.2 chinaevmart（chinaevmart.com）— 交叉一致性（仅改文案，未动 .net 数据）

| # | 文件 | 修正 |
|---|---|---|
| C1 | `src/pages/landed-cost-methodology.astro` | 顶部新增指针说明「本平台不运行计算器，交互计算器与逐市场数据在 electricvehiclehub.net」；改 intro「China EV Mart 估算」→「共享公式，计算器在姊妹站」 |
| C2 | `src/content/docs/landed-cost-methodology.md` | 同上指针说明 + 同 CVD/CIF 文案修正（保持与 .net 一致） |

> **交叉一致性说明**：chinaevmart 的车辆页「Export considerations」绿框（指向 `electricvehiclehub.net/vehicles/{slug}/`）、`markets/index.astro`（指向 `/landed-cost-calculator/`）、`methodology.astro`（明确「本平台无计算器，落地成本在姊妹站」）引用**均正确且一致**。唯一不符处是遗留的 `/landed-cost-methodology/` 页面把公式表述为 chinaevmart 自身产出，与 `methodology.astro` 定位矛盾——已按 C1/C2 修正措辞。

---

## 3. 测试用例表（回归脚本：`scripts/test_landed_cost_regression.py`）

9 个用例（≥5 要求，覆盖 EU 高关税 / PHEV / EREV / 中东 / 澳新 / 高非欧关税），全部 PASS：

| # | 车型 | 动力 | 品牌 | 市场 | 关键参数 | 预期 landed (USD) |
|---|---|---|---|---|---|---|
| 1 | BYD Dolphin | BEV | byd (17%) | Germany | 10%+17%+19% VAT | 28,072.05 |
| 2 | MG 4 | BEV | mg (35.3%) | Germany | 10%+35.3%+19% | 23,761.74 |
| 3 | Xiaomi SU7 | BEV | xiaomi (20.7%) | Germany | 10%+20.7%+19% | 54,504.48 |
| 4 | BYD Qin Plus DM-i | PHEV | byd | Germany | 10%+0% CVD+19% | 21,103.72 |
| 5 | Aito M9 EREV | EREV | aito | Germany | 10%+0% CVD+19% | 92,012.25 |
| 6 | BYD Dolphin | BEV | byd | UAE | 5%+0%+5% | 19,907.05 |
| 7 | BYD Dolphin | BEV | byd | Australia | 0%+0%+10% | 21,272.00 |
| 8 | BYD Dolphin | BEV | byd | Turkey | 40%+0%+20% | 27,803.60 |
| 9 | MG 4 | BEV | mg | Saudi Arabia | 5%+0%+15% | 16,150.68 |

**运行方式**：

```bash
python3 scripts/test_landed_cost_regression.py            # 用例 + 全量重算
python3 scripts/test_landed_cost_regression.py --cases    # 仅用例
python3 scripts/test_landed_cost_regression.py --full     # 仅 517×30 全量重算
```

脚本从 `src/data/tariffs.json` 正向复算，断言（a）9 个手核用例、（b）全量 517×30 对账（≥$0.015 判为真实偏差）。**未来改公式/税率后跑一次即可回归**。

---

## 4. 待人工复核清单（不可核验规则，未当已确认事实呈现）

| # | 项目 | 现状 | 复核动作 |
|---|---|---|---|
| H1 | EU CVD 税率（Reg 2024/2754）权威复核 | `tariffs.json` `verification_status: unknown`；上次 EUR-Lex 抓取被 AWS WAF 拦截失败 | 人工到 EUR-Lex 权威页确认 BYD 17.0 / Geely 18.8 / SAIC 35.3 / Tesla 7.8 / other-cooperating 20.7 / non-coop 35.3 |
| H2 | 非欧市场关税税率（Turkey 40%、Indonesia 50%、Singapore 20%、Brazil 35%、Mexico 50% 等） | 站点既有值，未逐市场权威溯源 | 逐市场核对 TARIC / 各国海关现行 MFN 税率 |
| H3 | 30 市场注册费（丹麦 3500、挪威 1400、以色列 700 等） | `source-master.json` 无逐市场条目 | 补逐市场出处 |
| H4 | 区域固定成本 `REGION_BASE_FIXED` | 三处副本（add_vehicles.py / extend_markets.py / 计算器页），不在 tariffs.json 中心表；旧值反解保留 | 并入中心表消除多副本（前审计 H2/H4） |
| H5 | 本地特有税（Turkey SCT、Singapore ARF/COE、Indonesia PPnBM、Brazil IPI/ICMS、Malaysia 消费税） | **未建模**（低估这些市场真实落地成本） | 决策是否分市场建模，或持续在口径中披露排除 |
| H6 | 认证费全国统一 $3,250 | 未按市场/认证路线区分（文档自述 1500–5000 区间） | 分市场组设认证费（前审计 H5） |
| H7 | 保险（CIF 的 "I"）、汇率/币种、融资/毛利 | 完全无字段，已披露排除 | 确认披露充分性；如需严格 CIF 口径则需新增保险字段 |
| H8 | D1 口径升级（base → CIF 作为应税基数） | 当前用出厂基价（保守低估 duty/VAT） | 决策是否按严格 CIF 重算全站（前审计 H1，建议保持 base + 披露） |

**不可核验的税率/规则已全部按「待人工复核」呈现**，未在任何页面作为「已确认事实」陈述；`tariffs.json` 的 `cvd_meta.verification_note` 已明确记载复核失败记录。

---

## 5. 收尾状态

- 回归测试：9/9 用例 PASS，全量 517×30 重算 0 真实偏差、78 处 ±$0.01 取整伪差（cosmetic）。
- 文档修正：CNEVhub 3 文件 + chinaevmart 2 文件。
- 报告路径：`docs/landed-cost-validation.md`（本文档）。
- 回滚：`git revert <commit>` 即可撤销本批（纯文案 + 新增测试脚本，无数据/公式改动）。
