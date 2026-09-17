# EV Hub SEO Integrity Report

> 生成：2026-09-17 ｜ 构建产物：dist/（788 页，build 通过）

## Indexable URLs

- 构建页面总数：**788**（含 vehicles 517 + brands 72 + markets 30 + blog + docs + 工具页）
- noindex 页面：**0**（未新增任何 noindex）
- 被排除页面：sitemap filter 沿用既有策略，本次未改动

## Sitemap

- `dist/sitemap-index.xml` + 分片生成正常（build 输出确认）
- sitemap URL 与 canonical 一致性：sample 抽查通过（下）

## Canonical 检查（sample）

| 页面 | canonical | 状态 |
|---|---|---|
| /vehicles/byd-seal/ | https://electricvehiclehub.net/vehicles/byd-seal/ | ✅ 自引用 |
| /brands/mg/ | https://electricvehiclehub.net/brands/mg/ | ✅ 自引用 |
| /about/ | 自引用 | ✅ |
| /landed-cost-calculator/ | 自引用 | ✅ |

- canonical 策略未做任何改动（任务要求：仅修复可证明的错误，未发现错误）

## Schema 修复（本次）

| 页面类型 | 修复 |
|---|---|
| 车辆页 | 移除虚构 `offers`（price/availability InStock）——信息站不卖车；`fuelType` 从硬编码 'Electric' 改为按 powertrain 映射；保留 Vehicle + Brand + @id 稳定结构 |
| 品牌页 | foundingDate 原样输出（MG 数据修复后自动变为 1924）|
| Blog/FAQ | 既有 FAQPage schema 未动 |

## 内链完整性

- Vehicle → Brand：`/brands/{brand}/` 链接存在 ✅
- Brand → Vehicle：`/vehicles/{slug}/` 链接存在 ✅
- Breadcrumb：Home / Vehicles / Brand / Vehicle ✅
- 品牌墙（首页）：58→72 后所有链接目标均有对应品牌页（72 个 brand md 全存在）

## 已知不动作项

- robots.txt：未改动（既有策略无错误）
- sitemap 结构：未改动
- URL 结构：未改动（0 URL 变化）
