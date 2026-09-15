---
title: "BYD Seal vs Tesla Model 3: Landed-Cost Reality Check in the EU"
description: "BYD Seal ($24,690 ex-factory) against the Tesla Model 3 — full tariff-stack and landed-cost math in Germany and the EU, with sourcing and import-duty nuance."
image: "/logo.svg"
author: "Wei Wang"
publishedDate: "2026-09-15"
draft: true
tags: [byd, seal, tesla, model-3, landed-cost, eu-tariff, comparison, ev-import, germany]
---

## TL;DR

A BYD Seal ex-factory at $24,690 does not beat a Tesla Model 3 in Germany — it loses on the one number that decides everything: **duty**. The Seal pays BYD's 17% countervailing duty on top of the EU's 10% import duty and 19% VAT, landing a full **$44,413 (≈ €38,500) before a single euro of importer margin**. A Shanghai-built Model 3 Standard retails in Germany at **€36,990 — already below the Seal's landed cost** — because Tesla's individually assessed countervailing duty is just **7.8%**, less than half BYD's rate. The car is not the product; the tariff attached to the manufacturer is a large part of the product.

## Definitions

- **FOB / ex-factory price** — what the car costs at the Chinese factory gate or port before shipping, duty, and tax. The BYD Seal's $24,690 is an FOB figure.
- **Landed cost** — the fully delivered cost once import duty, countervailing duty, VAT, freight, clearance, certification, registration, and inland transport are added. The Seal's is $44,413 in Germany.
- **On-the-road (OTR) retail price** — what a consumer pays at a dealer, duty-paid, VAT-inclusive, and already carrying the seller's margin. Tesla's €36,990 is an OTR figure.
- **Countervailing duty (CVD)** — the EU's anti-subsidy tariff on Chinese-built BEVs, set per producer under Regulation (EU) 2024/2754. BYD pays 17%; Tesla (Shanghai) pays 7.8%.
- **Most-favored-nation (MFN) duty** — the EU's standard 10% import duty applied to any non-EU car, on top of which the CVD is layered.

## The headline comparison

| Metric | BYD Seal (base) | Tesla Model 3 Standard RWD |
|---|---|---|
| China ex-factory / base | $24,690 (FOB) | n/a (sold as OTR in Germany) |
| Germany list price | not a retail price — import estimate | €36,990 (OTR, incl. 19% VAT) |
| Battery | 61.44 kWh LFP | ~60 kWh usable LFP (CATL) |
| Range | 450 km **CLTC** | ~450 km real-world (WLTP-based) |
| Power | 170 kW / 380 Nm | ~208 kW (≈279 hp) |
| 0–100 km/h | 6.5 s | ~6.2 s |
| Length / wheelbase | 4,800 mm / 2,920 mm | 4,720 mm / 2,875 mm |
| Curb weight | 1,950 kg | ~1,847 kg |
| EU countervailing duty | **17%** (BYD) | **7.8%** (Tesla, Shanghai) |
| EU standard duty | 10% MFN | 10% MFN |

Two spec numbers need immediate qualification. First, **450 km CLTC is not 450 km WLTP.** CLTC is the optimistic Chinese cycle; the same Seal is closer to ~350–380 km under WLTP-style real-world conditions. The Model 3's "450 km real range" is already the conservative figure. Quoting them side by side as equal is a beginner's error — see our [CLTC vs WLTP explainer](/blog/cltc-vs-wltp-range/). Second, the two price bases are **not the same unit**: the Seal's $24,690 is ex-factory, while the Model 3's €36,990 is a German retail price that already includes all duties, VAT, logistics, and Tesla's own margin. Comparing them directly is how most buyer-side comparisons go wrong.

## The tariff stack, side by side

The EU duties compound, not add. Standard duty is applied to the CIF value (price + freight + insurance), the countervailing duty is applied on top of that, and VAT is charged last on the duty-inclusive total. Read the full order of operations in our [landed-cost methodology](/docs/landed-cost-methodology/).

| Tariff layer | BYD Seal | Tesla Model 3 (Shanghai) |
|---|---|---|
| Standard MFN import duty | 10% | 10% |
| Countervailing duty | 17% | 7.8% |
| VAT (Germany) | 19% | 19% |

The difference is one number: **9.2 percentage points of CVD.** On an identically valued car it is worth real money. Take a hypothetical $24,690 CIF value — the exact Seal base:

| Line | BYD (17% CVD) | Tesla (7.8% CVD) |
|---|---|---|
| CIF value | $24,690 | $24,690 |
| Standard duty (10%) | $2,469 | $2,469 |
| CVD on (CIF + duty) | **$4,617** | **$2,118** |
| CVD gap | — | **$2,499 cheaper** |

So before VAT, freight, or margin, Tesla's rate saves **$2,499 of countervailing duty on an identically priced car**. That is the structural reason a Shanghai-built Model 3 can undercut a Seal in the EU despite the Seal carrying the lower China price tag. [Sources: European Commission Reg 2024/2754; Reuters tariff factbox]

## The Seal's landed cost, line by line (Germany)

Here is the full chain for the base Seal, from our [vehicle record](/vehicles/byd-seal/) and the documented [cost-breakdown example](/docs/cost-breakdown-example/):

| Cost item | Amount (USD) |
|---|---|
| Base price (China, FOB) | $24,690 |
| Standard import duty (10%) | $2,469 |
| Countervailing duty (BYD, 17%) | $4,617 |
| VAT (19%) | $6,037 |
| RoRo freight | $2,000 |
| Customs clearance | $350 |
| Certification / homologation | $3,250 |
| Registration | $500 |
| Inland transport | $500 |
| **Total landed** | **$44,413 (+79.9%)** |

At the September 15, 2026 EUR/USD rate of roughly 1.15, that $44,413 is **≈ €38,500** [Source: Trading Economics]. Read the number again: a third-party importer's *landed cost — before any dealer margin, warranty provisioning, or currency risk — is already higher than Tesla's German retail price of €36,990.* There is no margin left to compete on price; a Seal importer has to win on something other than sticker.

## Why the Model 3 lands the way it does: sourcing, not magic

The most common misconception I see is "Tesla builds in Berlin, so the Model 3 avoids the China tariffs." That is only half right, and the half that is wrong matters.

Berlin-Brandenburg (Giga Berlin, in Grünheide) produces the **Model Y** for most continental European left-hand-drive demand. It does **not** currently produce the Model 3. The Model 3 sold in Europe is imported from **Giga Shanghai**, and therefore *does* sit inside the EU's countervailing-duty regime — it just pays Tesla's individually assessed 7.8% rate rather than BYD's 17% [Sources: eletric-vehicles.com Giga Shanghai export reporting; Reuters].

There are credible but unconfirmed reports that Berlin could add Model 3 lines in the future, but as of this writing the Model 3's EU supply is Shanghai-based. The practical consequence: **Tesla does not dodge the tariff; it pays a lower tariff.** Both cars are China-built for EU purposes, but the manufacturer-specific CVD is wildly different — 7.8% for Tesla against 17% for BYD. That gap, not the factory location, is the whole ballgame.

## The FOB-versus-retail trap, spelled out

Most comparison tables I've seen put "$24,690 BYD Seal" next to "€36,990 Tesla Model 3" and conclude the Seal is the bargain. That is a category error on two axes:

1. **Currency and base.** The Seal number is USD FOB; the Tesla number is EUR OTR. You cannot subtract across those two.
2. **What's already in the price.** The Tesla figure already contains 10% duty, 7.8% CVD, 19% VAT, freight, and Tesla's margin. The Seal figure contains none of those.

The honest comparison is **Seal landed ($44,413 / ≈ €38,500) versus Tesla OTR (€36,990)** — and even then the Seal number is flattered, because it excludes the importer's margin while the Tesla number includes Tesla's. To make the Seal genuinely competitive, a buyer needs the landed cost to sit *meaningfully below* the Tesla retail, not merely at parity. It does not.

There is one legitimate nuance on the other side. For a **B2B importer who is VAT-registered**, the Seal's $6,037 of VAT is recoverable — it is a cash-flow item, not a final cost. Strip VAT from both and the picture shifts from "Seal slightly above" to "closer to parity," because the Seal's higher absolute value carries more recoverable VAT. The countervailing duty, by contrast, is never recoverable. Run both scenarios through the [landed-cost calculator](/landed-cost-calculator/) with your own VAT position before deciding.

## Who should care about this comparison

- **A dealer or distributor** weighing a China-sourced Seal against ordering from Tesla directly: you are not competing on invoice delta; you are competing on the 9.2-point CVD gap.
- **A fleet buyer** benchmarking total cost of ownership: the Model 3's Supercharger access and the Seal's interior tactility matter, but they are second-order to the fact that the Seal's landed cost exceeds the Model 3's retail in Germany.
- **Anyone reading a "$24,690 vs €36,990" headline**: that comparison is comparing an import estimate to a finished retail product, and it flatters the Seal by roughly the entire CVD gap.

## The Author's Take

**Position:** In the EU, the Tesla Model 3 is the structurally cheaper car to actually buy today — not because it is the better or worse product, but because Tesla's 7.8% countervailing duty is less than half BYD's 17%, and that 9.2-point gap wipes out the Seal's ex-factory price advantage before the Seal even reaches a showroom.

**Reasoning:** The Seal's $24,690 FOB becomes $44,413 landed in Germany, which is already above the Model 3's €36,990 retail. That means a third-party importer has no price headroom to compete on sticker, while Tesla sells a duty-paid, margin-inclusive car below the Seal's pre-margin landed cost. The difference is a single regulatory line item — the producer-specific CVD — and it is not an accident; it is the outcome of Tesla cooperating in the EU's anti-subsidy investigation and demonstrating lower subsidy exposure than BYD. The Seal remains a strong car on spec, but its value proposition in Europe today is not "cheaper than a Model 3." It is "comparable car, different cost structure, win on service and positioning rather than price."

**Disclosure:** This is my editorial judgment as the author, based on the documented tariff rates and the EV Hub landed-cost methodology — not a price quote, not a legal opinion, and not a claim that either car is "better." Verify current German list prices and your own VAT recovery position before acting; the EU has also begun approving tariff-exemption deals for individual models under minimum-price/quota terms, which can change these numbers on short notice.

## Key takeaways

1. **Duty, not sticker, decides the EU outcome.** BYD 17% CVD vs Tesla 7.8% CVD is a 9.2-point gap worth ~$2,499 of duty on a $24,690 car.
2. **The Seal lands at $44,413 in Germany (+79.9%)** — already above the Model 3's €36,990 German retail, before any importer margin.
3. **The Model 3 sold in Europe is Shanghai-built, not Berlin-built.** Giga Berlin makes the Model Y; the Model 3 still pays the China CVD regime, just at Tesla's lower individual rate.
4. **CLTC ≠ WLTP.** The Seal's 450 km CLTC is not comparable to the Model 3's ~450 km real-world figure.
5. **FOB ≠ OTR.** Comparing $24,690 ex-factory to €36,990 retail is a category error that flatters the Seal by roughly the entire CVD gap.

## Sources

1. European Commission (Access2Markets) — "EU Commission imposes countervailing duties on imports of battery electric vehicles (BEVs) from China" (Implementing Regulation (EU) 2024/2754) — https://trade.ec.europa.eu/access-to-markets/en/news/eu-commission-imposes-countervailing-duties-imports-battery-electric-vehicles-bevs-china — 30 October 2024
2. Reuters — "EU tariffs on imports of China-made EVs" (tariff factbox: BYD 17%, Tesla Shanghai 7.8%) — https://www.reuters.com/world/china/eu-tariffs-imports-china-made-evs-2026-02-11 — 11 February 2026
3. electrive.com — "Tesla Model 3 standard starts at €36,990" — https://www.electrive.com/2025/12/05/tesla-model-3-standard-starts-at-e36990 — 5 December 2025
4. EV Database — "Tesla Model 3 RWD (Highland)" specifications and Germany price (€37,970) — https://ev-database.org/car/3403/Tesla-Model-3-RWD — accessed September 2026
5. eletric-vehicles.com — "Tesla Giga Shanghai exports" (Model 3 for European markets imported from Shanghai; Tesla 7.8% rate) — https://eletric-vehicles.com/tesla/tesla-gigashanghai-exports-surpass-2025-total-in-just-seven-months — 2026
6. Trading Economics — EUR/USD exchange rate (1.1546 on 15 September 2026) — https://tradingeconomics.com/euro-area/currency — 15 September 2026
7. EV Hub — BYD Seal vehicle record and landed-cost breakdown (base $24,690 → $44,413 Germany) — internal data file, updated 7 September 2026

## Related reading

- [BYD Seal Deep Review: Real Landed Cost & Import Math](/blog/byd-seal-deep-review/)
- [Why the Sticker Price Is Never the Landed Price](/blog/sticker-vs-landed-price/)
- [CLTC vs WLTP: The Range You Won't Get](/blog/cltc-vs-wltp-range/)
- [EU Import Guide](/docs/eu-import-guide/)
- [Landed Cost Methodology](/docs/landed-cost-methodology/)
- [BYD Seal vehicle record](/vehicles/byd-seal/)
