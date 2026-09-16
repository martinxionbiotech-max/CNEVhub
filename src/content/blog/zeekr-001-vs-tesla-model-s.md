---
title: "Zeekr 001 vs Tesla Model S: Landed-Cost Reality Check in the EU"
description: "Zeekr 001 ($38,000 ex-factory, 710 km CLTC) against the Tesla Model S — full tariff-stack and landed-cost math, with Geely's 18.8% CVD and US-import duty nuance."
image: "/logo.svg"
author: "Wei Wang"
publishedDate: "2026-09-15"
draft: true
tags: ["zeekr", "001", "tesla", "model-s", "landed-cost", "eu-tariff", "countervailing-duty", "comparison", "ev-import", "germany"]
---

## TL;DR

The Zeekr 001 and the Tesla Model S are not direct competitors, and the reason is structural rather than just price. The Zeekr 001 lands in Germany at **$65,694** from a $38,000 ex-factory base (+72.9%), paying a 10% EU duty *plus* an 18.8% Geely-group countervailing duty. The Tesla Model S, built in Fremont and imported from the US, pays only the 10% EU duty with **no countervailing duty at all** — but it listed around €109,990 in Germany and has now been discontinued in Europe, so this comparison is more a lesson in tariff architecture than a buying decision.

## What "landed cost" means here

**Landed cost** is the total outlay to move a vehicle from the factory gate to the buyer's door: import duty, countervailing duty where applicable, VAT/GST, ocean freight, customs clearance, certification, registration, and inland transport. EV Hub computes every figure with the single compounding formula documented in the [landed-cost methodology](/docs/landed-cost-methodology/).

Three tariff terms do most of the work in this comparison:

- **Standard (MFN) duty** — the EU's baseline 10% tariff on imported passenger cars, applied to the CIF value.
- **Countervailing duty (CVD)** — an extra EU anti-subsidy duty that applies to Chinese-built BEVs only, under Implementing Regulation (EU) 2024/2754. It is producer-specific: Geely (including Zeekr) pays 18.8%, the "other cooperating" producers pay 20.7%, BYD pays 17.0%, SAIC/MG pays 35.3%, and Tesla's Shanghai-built cars pay 7.8%.
- **VAT** — Germany's 19% value-added tax, charged last on the duty-inclusive total.

The formula compounds rather than adds: `base × (1 + standard duty) × (1 + CVD) × (1 + VAT) + fixed costs`. Treating it as a simple sum of percentages is the most expensive mistake a first-time importer makes.

## The two tariff stacks are not the same

The single most important fact in this comparison: the countervailing duty is a *China-only* measure, and the Model S is not a Chinese car.

| Tariff line | Zeekr 001 (China, Geely) | Tesla Model S (US, Fremont) |
|---|---|---|
| Origin | China | United States |
| Standard EU duty | 10% | 10% |
| Countervailing duty | 18.8% (Geely group) | None — CVD targets Chinese BEVs only |
| German VAT | 19% | 19% |
| Combined pre-VAT | 28.8% | 10% |
| EU availability | Actively exported | Discontinued; no new inventory |

The 18.8% is Geely's sampled rate, not the 20.7% "other cooperating" default. Zeekr is a Geely Group entity, so its BEVs inherit Geely's rate by group attribution — the same way Lynk & Co and Geely Galaxy do. On the Zeekr 001 the CVD line is **$7,858**; at the 20.7% default it would have been roughly $8,651, a saving of about $790. The nuance matters, but the edge is modest, as detailed in [Zeekr's 18.8% countervailing duty explainer](/blog/zeekr-countervailing-duty/).

The Tesla Model S, by contrast, is assembled in Fremont, California. Giga Berlin builds only the Model Y, so European Model S and Model X units were always US imports — which means they faced the EU's 10% MFN duty and **nothing else** on the tariff side. No countervailing duty, because Regulation 2024/2754 covers BEVs exported from China, not cars built in the US.

## The spec gap

The two cars occupy different segments, which is visible in the numbers before any tariff is applied.

| Specification | Zeekr 001 | Model S Dual Motor AWD | Model S Plaid |
|---|---|---|---|
| Body style | Shooting-brake / liftback | Luxury liftback sedan | Luxury liftback sedan |
| Length | 4,977 mm | ~5.0 m (five-metre saloon) | ~5.0 m |
| Motor power | 680 kW | 670 PS (~493 kW) | 1,020 PS (~750 kW) |
| 0–100 km/h | 3.08 s | 3.2 s (0–62 mph) | 2.1 s (0–62 mph, rollout) |
| Top speed | 280 km/h | 250 km/h (155 mph) | 322 km/h (200 mph) |
| Battery (net) | 95 kWh | ~95 kWh NCA (unofficial) | ~95 kWh NCA (unofficial) |
| Range | 710 km CLTC | ~723 km WLTP (19″) | ~695 km WLTP (19″) |
| Base price | $38,000 (China) | €109,990 (Germany) | €119,990 (Germany) |

Two caveats sit under this table. First, CLTC and WLTP ranges are not directly comparable — CLTC tends to read higher than WLTP for the same hardware, so the Zeekr's 710 km is not an apples-to-apples win over the Model S's ~723 km WLTP. See [CLTC vs WLTP](/blog/cltc-vs-wltp-range/) for the detail. Second, the battery figure for the Model S is an unofficial net figure sourced from EV-Database, since Tesla does not publish an official pack size; the Zeekr figure comes from the [catalog](/vehicles/zeekr-001/).

The headline takeaway is the price, not the spec sheet: a $38,000 ex-factory Zeekr 001 against a €109,990 German Model S. Those two numbers are separated by a factor of roughly 2.3 even before any landed-cost adjustment.

## The landed-cost math, worked: Zeekr 001 → Germany

Here is the itemized landed cost for the Zeekr 001 into Germany, straight from the catalog's [landed-cost record](/vehicles/zeekr-001/):

| Cost item | Amount (USD) |
|---|---|
| Base price (CIF) | $38,000 |
| Standard import duty (10%) | $3,800 |
| Countervailing duty (18.8%) | $7,858 |
| VAT (19%) | $9,435 |
| RoRo freight | $2,000 |
| Customs clearance | $350 |
| Certification | $3,250 |
| Registration | $500 |
| Inland transport | $500 |
| **Total landed** | **$65,694 (+72.9%)** |

The full Zeekr 001 spread across 30 markets runs from **$44,080 in Qatar (+16%)** to **$73,170 in Mexico (+92.6%)**, with the EU cluster sitting near the top because of the countervailing duty. Germany is not the cheapest EU destination — Sweden and Denmark land higher because of their 25% VAT — but it is the reference point most importers ask about first.

## The same-base hypothetical: what the CVD actually costs

To isolate the tariff effect, hold the base price constant and ask what a US-built car would land for in Germany against the Chinese Zeekr. Using the methodology's fixed-cost benchmarks and Germany's 19% VAT, both at a $38,000 base:

| Line | Zeekr 001 (10% + 18.8% CVD) | Hypothetical US-built car (10%, no CVD) |
|---|---|---|
| Base price | $38,000 | $38,000 |
| Standard duty | $3,800 | $3,800 |
| Countervailing duty | $7,858 | $0 |
| VAT (19%) | $9,435 | $7,942 |
| Fixed costs | $6,600 | $6,600 |
| **Total landed** | **$65,694** | **$56,342** |

The gap is **$9,352**. Notice it is larger than the $7,858 CVD line item on its own — because German VAT is charged on the duty-inclusive total, so the 18.8% countervailing duty also attracts 19% VAT on top. The all-in cost of the CVD, once VAT compounds over it, is about $9,350 on this car.

That is the structural edge a US-built car enjoys in the EU tariff stack: skip the CVD entirely, and an identical $38,000 car lands about 14% cheaper. The point is not that the Model S is cheap — it is not — but that its *tariff burden* is genuinely lighter than the Zeekr's, purely because of country of origin.

## Why the real numbers still don't favor the Model S

The hypothetical above is instructive but detached from reality, for two reasons.

First, the Model S base price is far higher than $38,000. Its last listed German price was **€109,990 for the Dual Motor AWD** and **€119,990 for the Plaid**, after Tesla raised prices by roughly €17,000 on the base model in early 2025. At the September 2026 EUR/USD rate of about 1.15, that is roughly **$127,000 and $139,000** respectively — nearly double the Zeekr 001's $65,694 German landed cost, and those are retail prices that already include Tesla's margin and VAT. Skipping an 18.8% CVD cannot close a base-price gap of that size.

Second, the Model S is no longer available new in Europe. Tesla removed the Model S and Model X from the German configurator in 2025, leaving only whatever inventory remained — and there was effectively none left in Germany. By April 2026 Tesla confirmed Model S and Model X production had ended entirely, with only a few hundred units left in global inventory, almost all in the US. In practical terms, a European buyer cannot currently order a new Model S at any price.

So the comparison resolves to this: the Zeekr 001 is the car you can actually import today, and it is the one that *pays more* in relative tariff terms — 28.8% before VAT versus the Model S's 10% — precisely because the EU's countervailing-duty regime punishes Chinese-built EVs and leaves US-built cars untouched.

## The Author's Take

**Position:** In my view, comparing the Zeekr 001 to the Tesla Model S is mostly a demonstration of how the EU tariff stack treats country of origin, not a genuine purchase comparison — the Model S is gone from Europe, and even when it was there, its US origin let it skip the very countervailing duty that makes the Zeekr expensive.

**Reasoning:** First, the countervailing duty is China-only, so a Fremont-built Model S paid 10% duty and nothing else, while the Zeekr 001 pays 10% plus 18.8% Geely-group CVD plus VAT compounded on top — a structural gap worth roughly $9,350 on an identical base price. Second, that tariff advantage never mattered in practice because the Model S started near €110,000, about 2.3× the Zeekr's ex-factory price, so no duty saving could bring it into the Zeekr's cost band. Third, the Model S has been discontinued in Europe, which makes the whole exercise academic for anyone importing today — the Zeekr 001 is the only one of the two you can actually land.

**Disclosure:** This is my analysis of published EU tariff law, the EV Hub landed-cost records, and third-party pricing reports, not legal or tax advice. Countervailing-duty rates, Tesla pricing, and Model S availability can change; confirm current schedules and inventory with a customs broker or the seller before pricing anything.

## Related reading

- [Zeekr's 18.8% Countervailing Duty](/blog/zeekr-countervailing-duty/)
- [Geely's 18.8% Countervailing Duty](/blog/geely-188-countervailing-duty/)
- [Landed Cost Methodology](/docs/landed-cost-methodology/)
- [EU Import Guide](/docs/eu-import-guide/)
- [Why the Sticker Price Is Never the Landed Price](/blog/sticker-vs-landed-price/)
- [CLTC vs WLTP Range](/blog/cltc-vs-wltp-range/)
- [Zeekr 001 catalog page](/vehicles/zeekr-001/)

## Sources

1. EV Hub — Zeekr 001 catalog record: $38,000 base, 710 km CLTC, 95 kWh, 680 kW, 30-market landed-cost table (data updated 2026-09-07) — /vehicles/zeekr-001/
2. European Commission — Implementing Regulation (EU) 2024/2754, definitive countervailing duties on BEVs from China (BYD 17.0%, Geely 18.8%, SAIC 35.3%, other cooperating 20.8%, non-cooperating 35.3%) — https://eur-lex.europa.eu/eli/reg_impl/2024/2754/oj — 30 October 2024
3. EV Hub — Landed Cost Methodology (compounding formula and fixed-cost benchmarks) — /docs/landed-cost-methodology/
4. Motor1 — "Tesla Model S suddenly €17,000 more expensive in Germany" (Dual Motor AWD €109,990, Plaid €119,990, specs, ~95 kWh NCA battery per EV-Database) — https://www.motor1.com/features/750090/tesla-model-s-price-increase-germany — 2025 (accessed 2026-09-15)
5. InsideEVs — "The Tesla Model X And Model S Are Dead In Europe" (Europe left with inventory-only; no built-to-order units) — https://insideevs.com/news/767444/tesla-model-s-model-x-dead-europe — 2025 (accessed 2026-09-15)
6. Electrek — "Tesla confirms Model S and Model X production is over — only ~600 left" (production ended; ~295 new Model S units left, nearly all in the US) — https://electrek.co/2026/04/01/tesla-model-s-x-production-over-only-inventory-left — 1 April 2026
7. Kelley Blue Book — "2026 Tesla Model S Price" (US MSRP: AWD $86,630, Plaid $101,630) — https://www.kbb.com/tesla/model-s/ — accessed 2026-09-15
8. Trading Economics — EUR/USD exchange rate (1.1546 on 15 September 2026), used for EUR→USD conversions in this article — https://tradingeconomics.com/euro-area/currency — 15 September 2026
