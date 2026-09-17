# EV Hub Entity Model Report

> 生成：2026-09-17 ｜ 反映本次 P0 修复后的实际数据模型

## 实体关系图

```
Manufacturer (parent_company)
    │ owns/operates
    ▼
Brand (brand_id)
    │ produces
    ▼
Vehicle (vehicle_id)
    │ classified by
    ├── BodyType (受控词表)
    ├── Powertrain (受控词表)
    └── Range (range_standard: CLTC 统一)
    │ priced for export into
    ▼
Market (market_id + market_code ISO)
    │ governed by
    ▼
Tariff (brand_cvd + cvd_meta 版本化)
    │ sourced from
    ▼
Source (source/source_url/last_verified)
```

## 实际实现位置

| 实体 | 存储 | 关键字段 | 主键 |
|---|---|---|---|
| Brand | `src/data/brand-master.json` (72) + `src/content/brands/*.md` | brand_name / parent_company / parent_location / established / website / source / source_url | brand_id |
| Vehicle | `src/data/vehicle-master.json` (517) + `src/content/vehicles/*.md` | brand / body_type / powertrain / price_usd / range_cltc_km / range_standard / battery_kwh / motor_power_kw | vehicle_id（slug，稳定不随名称变化）|
| Market | `src/data/market-master.json` (30) | market / region / import_duty / vat_gst / countervailing_duty / registration_fee_usd / source_ids | market_id + **market_code (ISO)** |
| Tariff | `src/data/tariffs.json` | brand_cvd（19 品牌率）+ **cvd_meta**（legal_basis/effective_from/powertrain_scope/status/last_verified）| brand slug → rate |
| Source | brand-master.source_url + tariffs.cvd_meta.source_url + market.source_ids + source-master.json | — | source id |
| Platform | `src/data/entity-graph.json` | Platform/Operator/Author/Contact/Database 实体 + relationships | entity id |

## 本次 P0 对实体模型的改动

1. **Market**：新增 `market_code`（ISO 3166-1 alpha-2），与 human-readable market 名并存——满足「Do not mix DE/DEU/Germany in the same field」
2. **Tariff**：新增 `cvd_meta` 版本化块（不再只有裸数字），brand_cvd 数值映射保留以零破坏消费方
3. **Brand**：新增 `source`/`source_url` 字段（72/72 覆盖）
4. **Vehicle**：body_type/powertrain 词表规范化（受控词表 13/7 值），vehicle_id 主键不变

## 词表（controlled vocabularies）

- **body_type**：Sedan / Hatchback / SUV / Crossover / MPV / Wagon / Pickup / Van / Coupe / Convertible / Sports Car / Other / Unknown
- **powertrain**：BEV / PHEV / EREV / HEV / ICE / FCEV / Unknown
- **range_standard**：CLTC / WLTP / NEDC / EPA / Manufacturer estimate / Real-world estimate / Unknown（当前全库 CLTC）
- **market_code**：ISO 3166-1 alpha-2

## 品牌与制造商分离（任务 §13）

brand-master 已用 `parent_company` + `parent_location` 表达 Manufacturer→Brand 关系（如 MG → SAIC (Shanghai)；Denza/Yangwang → BYD）。本次未改动该结构（已符合要求），entity-graph.json 保持既有实体关系。
