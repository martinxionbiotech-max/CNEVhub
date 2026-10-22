# ElectricVehicleHub 重设计 — Phase 3 数据质量改造报告

> **对象**：生产站 `https://electricvehiclehub.net/`（仓库 `repos/CNEVhub`，`main`）
> **框架**：`phase2/54-evhub-redesign-prompt.md`（PHASE 3 车辆数据质量 + PHASE 6 小步交付）
> **前置**：`docs/redesign-p1-audit.md`（§4.2 数据层 12/35 字段缺陷）+ `docs/redesign-p2-architecture.md`（附录七 P3 改造清单）
> **时间**：2026-10-22（UTC）
> **纪律**：绝不编造缺失值 · 不混拼不同 trim 规格 · CLTC/WLTP/EPA 分字段 · 来源 URL+时间戳记录（本批为**透明透出 + 确定性推导**，未新增任何数值）

---

## 〇、执行摘要

三步改造全部落地，单提交可回滚，生产数据值**零改动**（仅透出 + 分层标记）：

| 项 | 改造前 | 改造后 |
| :--- | :---: | :---: |
| `/data/vehicles.json` 端点字段 | **12** | **37** |
| 规格来源分层字段 | 无 | `spec_source_type`（5 层枚举，517/517 已标注） |
| 续航标准字段 | 仅 `range_cltc_km`（无 WLTP/EPA） | + `range_wltp_km` / `range_epa_km` / `range_standard_primary`（WLTP/EPA 全 N/A） |

**零虚构验证**：WLTP/EPA 在内容层 0 条数据，端点如实输出 `null`（未做任何换算填充）；`spec_source_type` 100% 由既有 `data_tier` 确定性推导，无一条编造。

---

## 一、改造清单（每步独立提交）

### 步骤 A — JSON 端点字段暴露（commit `data-quality-A`）

`src/pages/data/vehicles.json.ts`：端点从 **12 字段**扩展为 **33 字段**，全部为 content frontmatter 已有数据的**透明透出**（`d.field ?? null`），无任何数值计算/改写。

- 保留 12：`slug / title / brand / type / powertrain / price_usd / currency / range_cltc_km / battery_kwh / motor_power_kw / data_updated / landed_cost_markets`
- 补暴露 21：`description / price_type / range_long_km / torque_nm / accel_0_100_s / top_speed_kmh / length_mm / width_mm / height_mm / wheelbase_mm / weight_kg / efficiency_kwh_100km / fast_charge / data_tier / data_source / data_reviewed / confidence / family / image / image_credit / image_source`

### 步骤 B — 规格来源分层（commit `data-quality-B`）

1. `src/content.config.ts`：vehicles schema 增可选字段 `spec_source_type`（5 层枚举）。
2. 新增 `src/lib/spec-tier.ts`：分层词汇 + 确定性推导函数 `tierFromDataTier()`。
3. 端点透出 `spec_source_type`（`data_tier` 映射优先，显式 frontmatter 值次之，无据为 `null`）。

**映射规则（有来源依据才标注，无据保持原状）**：

| data_tier | spec_source_type | 语义 |
| :---: | :--- | :--- |
| 1 | `official_spec` | 官方规格（厂家官网/工信部公告/监管文件） |
| 2 | `manufacturer_claim` | 厂商宣称（未独立验证的营销口径） |
| 3 | `independent_test` | 独立测试/行业媒体/目录（第三方口径） |
| — | `estimate` | 估算（**定义但未自动赋**，当前数据无干净信号） |
| — | `unverified` | 未验证（**定义但未自动赋**，517 条均有 data_source） |

### 步骤 C — 续航标准区分（commit `data-quality-C`）

1. `src/content.config.ts`：增 `range_wltp_km`（number|null）、`range_epa_km`（number|null）、`range_standard_primary`（enum CLTC/WLTP/EPA|null）。
2. 端点透出三字段；`range_standard_primary` 在 `range_cltc_km != null` 时确定性标注 `'CLTC'`（字段名本身即标准依据，非编造）。

**核对结论**：内容层 `range_wltp_km` / `range_epa_km` **0 条**（P1 证据：REF 覆盖仅 2%），生产仓连 REF 那 2% 都无——故 WLTP/EPA **全量 N/A（null）**，未做 CLTC→WLTP/EPA 换算（红线：CLTC 普遍比 WLTP 高 15–25%，禁止冒充）。

---

## 二、分层标注覆盖（步骤 B 结果）

| spec_source_type | 数量 | 占比 | 来源依据 |
| :--- | :---: | :---: | :--- |
| `official_spec` | 333 | 64.4% | data_tier=1 |
| `manufacturer_claim` | 163 | 31.5% | data_tier=2 |
| `independent_test` | 21 | 4.1% | data_tier=3 |
| `estimate` | 0 | 0% | （无信号，未自动赋） |
| `unverified` | 0 | 0% | （517 条均有 data_source） |
| **已标注合计** | **517** | **100%** | — |

> 注：`estimate`/`unverified` 两档已定义但初始批量**有意留空**——`estimate` 仅适用 landed-cost 模板层固定值（非规格字段），`unverified` 需「有值但无 source_url」，当前 517 条均含 `data_source`，故无符合条件者。后续批次可逐字段显式赋。

---

## 三、续航字段填充实况（步骤 C 结果）

| 字段 | 填充 | 缺失 | 说明 |
| :--- | :---: | :---: | :--- |
| `range_cltc_km` | 470 | 47 | 已有字段（9.1% 缺失，P1 已知；HEV/部分 EREV 无纯电 CLTC） |
| `range_long_km` | 47 | 470 | 增程/混动综合续航（已透出） |
| `range_wltp_km` | **0** | 517 | 全 N/A（内容层无来源，未编造） |
| `range_epa_km` | **0** | 517 | 全 N/A（内容层无来源，未编造） |
| `range_standard_primary` | 470 | 47 | 有 CLTC 值者标注 `'CLTC'`，其余 null |

---

## 四、端点字段完整性（抽 10 车型）

确定性抽样（排序后索引 0/57/114/171/228/285/342/399/456/513）：

| 车型 | spec_source_type | CLTC | 缺失字段 |
| :--- | :--- | :---: | :--- |
| aeolus-e70 | official_spec | 347 | 无 |
| bestune-e01 | official_spec | — | range_cltc_km |
| changan-cs75-plus-hev | official_spec | — | range_cltc_km,battery_kwh,torque_nm,accel,top_speed,weight |
| deepal-l07 | manufacturer_claim | 530 | 无 |
| gac-motor-gs7 | manufacturer_claim | 150 | 无 |
| hycan-v09 | official_spec | 620 | accel,top_speed |
| leapmotor-a05 | official_spec | 405 | torque,accel,weight |
| neta-aya | official_spec | 318 | torque,accel,top_speed,weight |
| voyah-courage | official_spec | 650 | 无 |
| zeekr-8x | official_spec | 318 | torque,top_speed,weight |

**结论**：身份/溯源字段（slug/title/brand/type/powertrain/price/data_tier/spec_source_type/data_source/data_updated/data_reviewed）10/10 完整；缺失均为**真实缺失的规格值**（与 P1 缺失率一致：accel 39% / top_speed 27% / weight 32% / torque 18.6%），端点如实输出 `null`，未补造。

---

## 五、验证结果（步骤 D）

| 项 | 命令 | 结果 |
| :--- | :--- | :--- |
| 构建 | `npm run build` | ✅ **900 页**，exit 0（151s；SITE_URL 未设，回退 .net，非阻断） |
| 端点字段数 | 解析 `dist/data/vehicles.json` | ✅ 12 → **37**，517 records |
| 分层覆盖 | 同上 | ✅ 517/517（333/163/21） |
| 续航字段 | 同上 | ✅ CLTC 470 / WLTP 0 / EPA 0（无换算） |
| 数据校验 | `npm run validate:data` | ⚠️ 2 条**既有** `md-drift`（非本批引入，见下） |
| 抽 10 车型 | 脚本 | ✅ 见 §四 |

**validate:data 的 2 条 issue 为既有问题（非本批引入）**：
- `hongqi-guoya`：md powertrain=HEV vs master Unknown
- `xpeng-p7-plus`：md type=Sedan vs master SUV

成因 = P1 已识别的「`vehicle-master.json` 与 content frontmatter 已分叉」（master 陈旧，未随 content 更新）。本批只改端点/`content.config.ts`/新增 `spec-tier.ts`，**未触碰** master 与 .md，故这 2 条与 P3 无关，留待 P3 后续「master 由 content 重新生成」步骤闭环（P2 §7.1 改造点 2）。

---

## 六、回滚说明（每步单提交可回滚）

> 回滚顺序：按 C→B→A 逆序执行（`git revert` 会生成新 revert 提交，保留历史）。

| 步骤 | commit | 回滚命令 |
| :---: | :--- | :--- |
| A | `bb92e8c` | `git revert bb92e8c` |
| B | `7b8fc8a` | `git revert 7b8fc8a` |
| C | `b60d412` | `git revert b60d412` |

- 全量回滚三步：`git revert b60d412 7b8fc8a bb92e8c`（逆序单命令）。
- 每步回滚后端点即回到该步之前状态：C 回滚→去 WLTP/EPA 字段；B 回滚→去 spec_source_type；A 回滚→回到 12 字段。
- 若仅撤销 B/C 的 schema 增字段，`content.config.ts` 会一并还原，构建不受影响。

---

## 七、未做事项与后续（P3 余量 / P4 预告）

本批**只做数据透出与分层标记**，以下按红线**刻意未做**：

1. **未填 WLTP/EPA 值**：内容层无来源，全量 N/A（红线：禁止编造/换算）。后续需逐车型从官方 WLTP/EPA 公告补录，逐字段带 `source/source_url/timestamp`。
2. **未补缺失规格值**（accel/top_speed/weight/torque 等真实缺失）：保持 `null`，待有来源时填。
3. **未重构 `vehicle-master.json`**：它仍是陈旧分叉文件（零消费方），P3 后续应「由 content frontmatter 重新生成」落地单源真相（P2 §7.1）。
4. **`estimate`/`unverified` 两档未自动赋**：留待有干净信号时逐字段显式赋。
5. **`.md` 变体 + `/data/*.json` 的 noindex**：属 P2 §5.3（robots 指令），不在本批数据质量范围。

---

## 附：字段覆盖全量矩阵（517 车型，本批透出前实测）

| 字段 | 覆盖 | 字段 | 覆盖 |
| :--- | :---: | :--- | :---: |
| title/description/slug/brand/type/powertrain/price_usd/currency | 517 | torque_nm | 421 |
| family/image/image_credit/image_source | 517 | top_speed_kmh | 378 |
| data_tier/data_source/data_updated/data_reviewed | 517 | weight_kg | 353 |
| range_cltc_km | 470 | accel_0_100_s | 316 |
| length_mm | 505 | efficiency_kwh_100km | 284 |
| width_mm | 503 | range_long_km | 47 |
| height_mm | 504 | range_wltp_km | **0** |
| wheelbase_mm | 500 | range_epa_km | **0** |
| battery_kwh | 467 | confidence | 0（渲染层默认 Medium） |
| motor_power_kw | 483 | price_type | 0（schema 默认 MSRP） |
| fast_charge | 359 | | |
