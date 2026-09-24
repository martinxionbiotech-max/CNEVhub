---
title: "Data Provenance & Traceability"
description: "EV Hub field-level data provenance conventions — source types, confidence levels, and verification dates for every vehicle record."
section: "Data Quality"
order: 10
draft: false
---

# Data Provenance & Traceability

Every vehicle record on EV Hub carries provenance metadata so readers can tell **where a number came from and how much to trust it**. This page is the convention document for that system (task book §7).

## Machine-readable convention

The canonical field convention lives in [`src/data/source-master.json`](/data/source-master.json) under the `_conventions` block (schema version 1, adopted 2026-09-24). It defines:

### Source type enum

Every source that feeds a vehicle field is classified as exactly one of:

| `source_type` | Meaning | Example |
|---|---|---|
| `manufacturer` | Official manufacturer datasheet / website | Hongqi official spec sheet |
| `government` | Government-issued data (tax, customs, statistics) | National VAT legislation |
| `regulation` | Regulatory text | EU Reg 2024/2754 (CVD) |
| `customs` | Customs tariff schedules | EU TARIC, WTO Tariff Facility |
| `industry` | Industry media / industry benchmarks | CnEVPost, RoRo freight benchmarks |
| `primary` | Primary source (generic alias for official channels) | — |
| `secondary` | Secondary / aggregated catalog data | Autohome / 懂车帝 |
| `evhub_calculation` | Computed by EV Hub from a documented formula | `landed_cost`, VAT compounding |
| `evhub_estimate` | EV Hub benchmark estimate | RoRo freight, certification fees |

### Confidence levels

| `confidence` | Meaning |
|---|---|
| `high` | Official primary source, cross-verified |
| `medium` | Official + estimate mix, or single official source not yet reviewed |
| `low` | Tier-3/4 media source, or awaiting verification |

### Verification dates

`verified_date` (YYYY-MM-DD) records the last authoritative verification, either per field or per record. Vehicle-level `data_updated` serves this role today.

## Vehicle frontmatter fields (current state)

The vehicle markdown frontmatter already carries record-level provenance:

- `data_source` — text description of where the record's data comes from
- `data_updated` — last update/verification date (enforced ≤ 90 days by `scripts/qa_data.py` DATE QA)
- `data_reviewed` — human review flag
- `data_tier` — tier 1–4 (1 = official primary, 4 = tertiary cross-check)
- `confidence` — optional record-level confidence (`high` / `medium` / `low`); when absent the template derives a display value from the source mix (landed-cost estimates render as `Medium`)

The template on every vehicle page renders `data_source`, `data_updated`, `data_reviewed` and the confidence level in the **Data Sources & Verification** block.

### Per-field provenance (future)

`field_sources` — an optional object mapping each frontmatter field to `{source_id, source_type, confidence, verified_date}` — is specified in the convention but **not yet rolled out**. Batch-migrating 517 vehicle files is a separate decision; until then record-level metadata remains authoritative.

## Migration status

- 8 source records in `source-master.json` keep their legacy `source_type` values; the convention block maps them to the new enum (`customs tariff` → `customs`, `spec` → `manufacturer`, `catalog` → `secondary`, `tax` → `government`, `industry media` → `industry`, `tertiary` → `secondary`).
- No vehicle file was batch-modified as part of this step.
- New or hand-fixed records (e.g. Hongqi Guoya powertrain, verified 2026-09-24) record the verification date in `data_source` / `data_updated`.

## Related

- [QA gate](/docs/) — `scripts/qa_data.py` (SOURCE QA flags missing `data_source`)
- [Indexation quality gate](/docs/) — `scripts/quality-gate.mjs` (five gates incl. source)
- [Landed Cost Methodology](/docs/landed-cost-methodology/)
