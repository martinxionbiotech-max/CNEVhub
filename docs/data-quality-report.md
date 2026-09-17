# EV Hub Data Quality Report

> 生成：2026-09-17 ｜ 数据快照：vehicle-master.json / brand-master.json / market-master.json / tariffs.json
> 验证工具：`npm run validate:data`（scripts/validate-data.mjs）

## 总量

| 实体 | 数量 | 完整性 |
|---|---|---|
| Vehicles | 517 | md 1:1，0 差异 |
| Brands | 72 | 全部有 brand_name/parent_company/established/website/source_url |
| Markets | 30 | 全部有 ISO market_code + duty/vat/registration |
| Tariff rates (brand_cvd) | 19 | + cvd_meta 版本化块 |

## 重复实体

- 重复 vehicle_id：**0**
- 重复 model 名：**0**
- 品牌名规范化后重复：**0**

## 无效值（本次修复后）

- 无效 founded_year：**0**（原 MG=1029 已修）
- 无效 body_type：**0**（5 处分类错误已修：Dolphin/MG4/Guoya/Jiachen/Lamore）
- 无效 powertrain：**0**（4 处 Petrol 已规范化：3×ICE + 1×Unknown）
- 无效 price（0/负）：**0**
- 无效 battery/range/top-speed：**0**
- 无效 range_standard：**0**（517 台全 CLTC，统一）
- 无效 URL：**0**（3 个缺失 website 已补并实测 200）
- 无效 market_code：**0**（30/30 ISO 合法）

## 已知缺口（保留原样，未伪造）

| 项 | 状态 | 说明 |
|---|---|---|
| fast_charge='-' | 158 台 | 确定性占位符=未知；渲染层已隐藏。不伪造数值 |
| data_reviewed=false | 517/517 | 诚实状态，未人工复核 |
| Guoya powertrain=Unknown | 1 台 | V6/V8+电机的混合结构无法从公开源判定 HEV/PHEV |
| 品牌 established 年份 | 71/72 区间合法 | 仅 MG 越界已修；其余未逐一手工核验（持续监控）|

## 来源覆盖（source coverage）

- 品牌 source_url 覆盖：**72/72（100%）**——本次新增 source/source_url 字段
- 关税 legal_basis：**1/1**——cvd_meta 新增 EUR-Lex 2024/2754
- 市场 source_ids：30/30 已存在（eu-2024-2754 / national-tax）
- 车辆 md 有 data_source 字符串字段（泛化来源说明），无逐字段 source_url——**报告为剩余缺口**（任务 §8 允许先覆盖最高风险字段）

## 关税覆盖（tariff coverage）

- EU 市场 brand_cvd：19 个品牌/集团条目（BYD 17%、Geely 系 18.8%、SAIC 系 35.3%、Tesla 7.8%、其他配合 20.7%）
- powertrain_scope：BEV-only（PHEV/EREV/HEV/ICE 不适用）
- PHEV/EREV 误套 BEV CVD：**0**（全量扫描通过）
