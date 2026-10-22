# ElectricVehicleHub 重设计 — Phase 4a 车型页模板移植报告

> **对象**：生产站 `https://electricvehiclehub.net/`（仓库 `repos/CNEVhub`，`main`）
> **参照仓**：`repos/electricvehiclehub.top`（REF，从 CNEVhub fork，已完五段深度档案 + 去模板化）
> **框架**：`phase2/54-evhub-redesign-prompt.md`（PHASE 4 页面模板 + PHASE 6 小步交付）
> **时间**：2026-10-22（UTC）
> **纪律**：分批单提交可回滚 · 不盲目整文件覆盖 · 冲突字段以 git 判定哪个仓更新 · 绝不编造值

---

## 〇、执行摘要

| 项 | 改造前 | 改造后 |
| :--- | :---: | :---: |
| vehicles schema 字段 | 40 | **63**（+23 深度字段） |
| 车型页模板 | 84 词固定句式（无深度档） | **五段深度档案**（Entity Snapshot/Powertrain/Dimensions & Logistics/Market Compliance/Benchmarking + 40HQ 装箱 + 竞品矩阵） |
| 车型深度字段值 | 0 | **517/517**（6506 个深度字段值） |
| Overview 去模板化 | 0%（84 词固定句式） | **100%**（517 首句唯一，随 REF 移植） |
| sitemap | 701 URL | **701 URL（不变）** |

**分叉点判定**（冲突处理依据）：REF 仓库 init commit `3c09380` 的 tree == 生产 commit `b0b500b`（2026-10-06）的 tree，二者逐字节一致。自该分叉点起：
- **生产仓对 `src/content/vehicles/*.md` 零改动**（`git diff b0b500b..HEAD -- src/content/vehicles/` 为空）；
- 生产仓仅改动 schema（P3 的 4 字段）、端点、legal/docs 页——均与车型内容文件无交集。

故 517 车型文件移植为**纯增量**，无生产侧内容冲突；唯一需处理的是 REF 侧把 42 个文件的 `image_source` 内链域名从 `.net` 改成了自己的 `.top`（详见 §三）。

---

## 一、移植清单（6 commit，逆序可回滚）

| # | commit | 内容 | 净增 |
| :---: | :--- | :--- | :--- |
| 1 | `eac95d5` | `p4a-schema`：vehicles schema 加 23 深度字段（五段模板字段） | +23 字段 |
| 2 | `d6a2835` | `p4a-template`：`[slug].astro` 换五段模板（保留生产 JSON-LD/落地成本逻辑） | 五段落位 |
| 3 | `d5f6f09` | `p4a-content1`：130 车型深度字段值 + 去模板化叙事 | 130 |
| 4 | `624e128` | `p4a-content2`：130 车型 | 130 |
| 5 | `3073f45` | `p4a-content3`：130 车型 | 130 |
| 6 | `771e194` | `p4a-content4`：127 车型 | 127 |

### 1.1 schema 字段净增（23）

REF 深度块共 24 字段，其中 `range_wltp_km` 生产已在 P3 加入，故**净增 23**：

- ① Entity Snapshot：`trim` `fob_price_usd_min` `fob_price_usd_max`
- ② Powertrain & Architecture：`battery_type` `drive_type` `motor_type` `motor_model` `total_power_kw` `battery_thermal` `heat_pump` `suspension_front` `suspension_rear` `brakes` `drag_coefficient`
- ③ Dimensions & Logistics：`gross_weight_kg` `ground_clearance_mm` `trunk_l`
- ④ Market Compliance & Export Profile：`charging_interface` `charging_adapter` `infotainment_language` `network_bands` `certification_notes` `hs_code`

**保留生产 P3 独有字段**（REF 无、不回退）：`range_epa_km` `range_standard_primary` `spec_source_type`。全部 23 深度字段 `optional()`，不影响旧内容。

### 1.2 模板五段落位（`[slug].astro`）

换 REF 五段模板后，**针对性保留生产正确逻辑**（非整文件覆盖）：

- **JSON-LD offers**：保留生产的 `Vehicle ⊂ Product` 注释块（offers 与页面价格同源、不声明 seller、不加评分）——REF 简化版被替换回生产版。
- **落地成本数据层引用**（P3）：保留生产的 richer 文案——多国成本 `Confidence` 行（"official MSRP and EU duty rates; freight/certification/registration/customs are EV Hub estimates"）+ 明细表说明段（EU Reg 2024/2754 来源）。REF 删减的这两处已恢复。
- **costConfidence 推导注释**：保留生产版（§7 溯源约定 → Medium 推导）。

五段 = ① Entity Snapshot ② Powertrain & Architecture ③ Dimensions & Logistics（含 length-graded 40HQ 装箱估算）④ Market Compliance & Export Profile（HS code + GB/T→CCS2 适配 + 多国落地成本）⑤ Benchmarking Matrix（同细分最近价位竞品矩阵）。

---

## 二、内容移植进度（517 全量 ✅）

| 批次 | 文件数 | 深度字段值 |
| :--- | :---: | :---: |
| content1 | 130 | 130/130 |
| content2 | 130 | 130/130 |
| content3 | 130 | 130/130 |
| content4 | 127 | 127/127 |
| **合计** | **517** | **517/517（6506 个深度字段值）** |

- **深度字段值**：6506 个（`battery_type`/`drive_type`/`motor_type`/`brakes`/`heat_pump`/`certification_notes`/`hs_code`/`trim` 等，REF 已 backfill 至全量）。
- **去模板化叙事**：517 文件的 `description` + `Overview` 正文全部随 REF 移植（首句唯一、按 powertrain 差异化）；`data_source`/`data_updated` 同步 REF 的溯源深化（`data_updated: 2026-10-21`）。

---

## 三、冲突文件与处理（42 处，全部为域名内链）

逐文件 diff + git 判定结果：

| 冲突类型 | 文件数 | 字段 | 生产值 | REF 值 | 处理 |
| :--- | :---: | :--- | :--- | :--- | :--- |
| 域名内链 | 42 | `image_source` | `…electricvehiclehub.net/image-credits/` | `…electricvehiclehub.top/image-credits/` | **保留生产 `.net`** |

- 唯一冲突 = REF 侧把自己的域名 `.top` 写进了 42 个文件的 `image_source` 内链。移植时全局回退为生产 `.net`。
- **其余共享字段（price_usd/range/battery/landed_cost_markets/image 等）0 冲突**——因生产自分叉点起对车型 `.md` 零改动，REF 改动为纯增量（脚本比对 517 文件共享字段，0 值差异）。
- 移植后全仓 `grep electricvehiclehub.top` = **0 命中**，无域名泄漏。

---

## 四、验证结果

| 项 | 命令 | 结果 |
| :--- | :--- | :--- |
| 构建 | `npm run build` | ✅ **900 页**，exit 0（171.5s；SITE_URL 未设回退 .net，非阻断） |
| 数据校验 | `npm run validate:data` | ✅ 通过（仅 2 条 P3 既有 `md-drift`，非本批引入） |
| sitemap | `dist/sitemap-0.xml` `<loc>` 计数 | ✅ **701 URL 不变** |
| 占位扫描 | `npm run placeholder:scan` | ⚠️ 90 条（见下，均语义 N/A 非占位） |
| 抽 10 车型渲染 | 脚本 | ✅ **10/10 五段齐全 + 数据正确** |
| 域名泄漏 | `grep electricvehiclehub.top src/` | ✅ 0 命中 |

**抽 10 车型渲染**（排序索引 0/57/114/171/228/285/342/399/456/513）：`aeolus-e70` `bestune-e01` `changan-cs75-plus-idd` `deepal-l07-erev` `gac-motor-gs7` `hycan-v09` `leapmotor-a05` `neta-aya` `voyah-courage` `zeekr-8x` —— 8 项结构检查（五段 + 40HQ + Data Sources）10/10 齐全；price/CLTC range/battery 渲染与 frontmatter 一致（`voyah-courage` 的 battery 实为 `81.0`→渲染 `81 kWh`，脚本浮点格式化误报，人工核对正确）。

**占位扫描 90 条 = 语义 N/A，非占位残留**：全部为 REF 去模板化时对「不适用」字段的显式标注——`charging_interface` 19（HEV/ICE 无充电口）、`charging_adapter` 19、`heat_pump` 51（部分车型未配备）、`battery_thermal` 1。无 `TBD`/`占位`/`placeholder`/哨兵值/未来日期，0 真实占位残留。

---

## 五、回滚（逐 commit revert，逆序）

| 步骤 | commit | 回滚命令 |
| :---: | :--- | :--- |
| content4 | `771e194` | `git revert 771e194` |
| content3 | `3073f45` | `git revert 3073f45` |
| content2 | `624e128` | `git revert 624e128` |
| content1 | `d5f6f09` | `git revert d5f6f09` |
| template | `d6a2835` | `git revert d6a2835` |
| schema | `eac95d5` | `git revert eac95d5` |

全量回滚：`git revert 771e194 3073f45 624e128 d5f6f09 d6a2835 eac95d5`（逆序单命令）。每步回滚后即回到该步之前状态（content 回滚→去深度字段值；template 回滚→回 84 词模板；schema 回滚→去 23 深度字段）。content 四批互不重叠，可独立回滚单批而不影响其余。

---

## 六、未做事项（红线，刻意不做）

1. **未补 WLTP/EPA 值**：`range_wltp_km`/`range_epa_km` 仍 0 条（生产连 REF 那 2% 覆盖都无，禁编造换算）——待逐车型官方公告补录。
2. **未重构 `vehicle-master.json`**：仍为陈旧分叉文件（零消费方），留待 P3 后续「由 content 重新生成」。
3. **未改 `[slug].md.ts` / `/data/source-master.json.ts`**：不在本批范围（本批仅 schema/template/content 三件套）。
4. **占位扫描的 90 条 N/A**：为语义「不适用」，非占位，无需清除（如要收紧，可后续把 `heat_pump` 的 `N/A` 改为 `No`，属内容语义决策非本批范围）。
