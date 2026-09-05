---
title: "Landed Cost Methodology"
description: "The exact formula, data sources, and assumptions behind every landed-cost number on CNEVhub — transparent, documented, and reproducible."
section: "Landed Cost"
order: 1
draft: false
---

# Landed Cost Methodology

Every number on CNEVhub is produced from a single, documented formula using public tariff schedules, national tax rates, and industry freight benchmarks. This page is that documentation, so you can verify — and reproduce — any figure on the site.

## Why we publish this

Most Chinese EV listings show only the factory or FOB price. A car advertised at $14,000 can land in Germany at over $28,000 once duties, VAT, freight, and certification are applied. That gap is the single biggest surprise for first-time importers — and the reason transparency matters.

## The formula

```
landed_price = base_price × (1 + standard_duty) × (1 + countervailing_duty) × (1 + VAT)
               + RoRo freight + customs clearance + certification + registration + inland transport
```

Duties compound in this order because that is how customs valuations cascade in practice:

1. **Standard duty** is assessed on the CIF value (car price + insurance + freight).
2. **Countervailing duty** is assessed on top of that (standard duty + CIF).
3. **VAT/GST** is charged last, on the duty-inclusive total.

You do not add the rates; you compound them. This is the single most expensive misunderstanding in EV importing.

## The fixed-cost benchmarks

The variable tax terms come from public schedules. The fixed costs come from industry benchmarks and are held as central estimates:

| Fixed cost | Typical (USD) | Basis |
|---|---|---|
| RoRo ocean freight | $2,000 | China → North Europe main ports |
| Customs clearance | $350 | per vehicle |
| Certification / homologation | $3,250 | ECWVTA or national single-vehicle |
| Registration | $400–$500 | varies by country |
| Inland transport | $500 | port → buyer |

## Producer-specific countervailing duties (EU)

The EU anti-subsidy duty on Chinese BEVs is producer-specific, not a flat rate:

| Producer | CVD |
|---|---|
| Tesla (Shanghai) | 7.8% |
| BYD | 17.0% |
| Geely (incl. Zeekr, Polestar) | 18.8% |
| SAIC (MG, Roewe, Maxus) | 35.3% |
| Other cooperating producers | ~20.8% |
| Non-cooperating producers | 35.3% |

Source: European Commission Implementing Regulation (EU) 2024/2754, effective 31 October 2024, five-year duration.

## Where the CVD applies — and where it doesn't

A critical distinction most calculators get wrong:

- **EU markets:** the countervailing duty applies in full, producer-specific.
- **UK, UAE, Saudi Arabia, Australia:** no countervailing duty applies.

This is why the United Kingdom and the Gulf land vehicles dramatically cheaper than the EU — the difference is structural, not incidental.

## A note on VAT recoverability

For B2B importers, VAT/GST is often recoverable (via VAT registration in the EU/UK, or GST registration in Australia). The duty and countervailing duty are permanent costs; VAT is frequently a cash-flow item rather than a final cost. Our landed-cost figures show the full VAT-inclusive number, so treat it as the "cash you need at the border," not necessarily the "final net cost" if you can reclaim.

## Assumptions & limits

These are **B2B import estimates**, not retail quotes. Actual landed cost varies with:

- Trim and battery specification
- Port of entry and shipping lane
- Import volume (freight and certification are volume-sensitive)
- Currency (USD/CNY, USD/EUR, USD/GBP movement)
- Homologation route (full type approval vs. single-vehicle)

Figures are refreshed when tariff schedules or tax rates change, and every estimate carries its data date.

## Related

- [Cost Breakdown Example](/docs/cost-breakdown-example/) — a fully worked example on a BYD Seal.
- [EU Import Guide](/docs/eu-import-guide/) — the tariff stack in context.
