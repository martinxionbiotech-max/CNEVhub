---
title: "Turkey vs Indonesia: Asia's Two Steepest Import Walls for Chinese EVs"
description: "Turkey's 40% duty + 20% VAT and Indonesia's 50% duty + 11% VAT land a BYD Seal within $80 of each other — $45,729 vs $45,809 — but they are opposite walls: Turkey's extra cost sits in a 25–75% ÖTV on top of the border bill, Indonesia's sits in a localisation deadline that expires in 2027. The crossover where Indonesia becomes the cheaper market sits at exactly a $30,000 base price."
image: "/logo.svg"
author: "Wei Wang"
publishedDate: "2026-09-22"
draft: false
tags: [turkey, indonesia, import, comparison, tariffs, landed-cost, asia]
---

## TL;DR

Turkey and Indonesia are the two steepest customs walls for a Chinese EV in Asia — and on the border numbers they land almost exactly level: a [BYD Seal](/vehicles/byd-seal/) clears at **$45,729 in Turkey** (40% duty + 20% VAT) and **$45,809 in Indonesia** (50% duty + 11% VAT). But the walls are built in opposite directions: Turkey's extra cost sits *inside* the market (a 25–75% ÖTV special consumption tax our model excludes), Indonesia's *inside the calendar* (a localisation programme whose duty relief expires at the end of 2027). And the ranking flips at exactly a **$30,000 base price**: below it Turkey lands cheaper, above it Indonesia does.

## Key statistics

- **Turkey:** 40% effective duty (10% MFN plus 30% additional, min **US$8,500 per EV**, whichever is higher — Decree no. 10486, from 22 Sep 2025) + **20% VAT**; no countervailing duty
- **Indonesia:** **50% duty + 11% VAT (PPN)** under the general CBU tariff after the 0% exemption expired on 31 December 2025; no countervailing duty
- **ÖTV (Turkey's special consumption tax, outside our model):** lowest band **25%**, higher bands **55–75%** since the July 2025 revision; the Seal's 170 kW and the [Xiaomi YU7](/vehicles/xiaomi-yu7/)'s 235 kW sit above the 160 kW line, the [BYD Atto 3](/vehicles/byd-atto-3/)'s 150 kW below it
- **PPnBM (Indonesia's luxury-goods tax, outside our model):** current BEV band **UNKNOWN**
- **Modeled landed totals:** Atto 3 → **$31,567 (TR) vs $31,773 (ID)**; Seal → **$45,729 (TR) vs $45,809 (ID)**; YU7 → **$64,226 (TR) vs $64,141 (ID)**
- **The crossover:** Indonesia becomes the cheaper market at exactly a **$30,000 base price** — the gap runs `$450 − 1.5% × base`
- **The Gulf contrast:** the same Seal lands at **$30,105 in Qatar (+21.9%)** — roughly **$15,600 below** both walls

## Two walls, opposite construction

These two markets are expensive for different reasons, and the difference dictates who can still import profitably into either one.

| Layer | Turkey | Indonesia |
|---|---|---|
| Import duty | **40% effective** — 10% MFN + 30% additional duty (min US$8,500/EV) | **50%** — general CBU tariff since the exemption expired |
| Countervailing duty | None | None |
| VAT on duty-paid value | **20%** (KDV) | **11%** (PPN) |
| Domestic consumption tax (outside our model) | **ÖTV 25–75%**, keyed to motor power and tax-base bracket | **PPnBM**, luxury tax — BEV band UNKNOWN |
| The layer that actually decides | ÖTV band placement | The 2026–2027 localisation window |

Turkey concentrates its cost in a domestic consumption tax: the border stack (40% duty, 20% VAT) is already the heaviest in the Middle East in our dataset; the ÖTV is the instrument doing the real work. Indonesia concentrates everything at the border — a flat 50% duty, a light 11% VAT — with an industrial-policy door for manufacturers who commit to local assembly. Neither market applies an EU-style countervailing duty; that is a European measure under [Regulation (EU) 2024/2754](/blog/byd-countervailing-duty-landed-cost/), not an Asian one.

## Same car, two markets

Three models across the price bands, run through both stacks on our [landed-cost formula](/docs/landed-cost-methodology/) — `base × (1 + duty) × (1 + VAT) + fixed import block` ($4,250 TR, $4,700 ID):

| Model | Base (China) | Turkey landed | Turkey premium | Indonesia landed | Indonesia premium | Gap |
|---|---|---|---|---|---|---|
| BYD Atto 3 | $16,260 | $31,567 | +94.1% | $31,773 | +95.4% | ID +$206 |
| BYD Seal | $24,690 | $45,729 | +85.2% | $45,809 | +85.5% | ID +$80 |
| Xiaomi YU7 | $35,700 | $64,226 | +79.9% | $64,141 | +79.7% | TR +$86 |

On a mid-size sedan the two walls are within $80 of each other — but watch the last column: Turkey wins at the budget end, Indonesia at the premium end. That is not noise, it is algebra.

The tax multipliers are `1.40 × 1.20 = 1.68` for Turkey and `1.50 × 1.11 = 1.665` for Indonesia — ten duty points against nine VAT points, but VAT compounds on the duty-paid total. The fixed block differs by $450. Solve it:

**Gap (Indonesia − Turkey) = $450 − 1.5% × base**

That gap hits zero at **$30,000 of base price**. Below that, the heavier VAT in Turkey outweighs the heavier duty in Indonesia; above it, the duty wins. The YU7 row shows the flip in real money: a $35,700 car lands **$86 cheaper in Indonesia**. Anyone quoting "Indonesia is the more expensive market" as a blanket rule has not run the math past the crossover.

At 22 September 2026 reference rates (USD/CNY 6.71, USD/TRY 48.82, USD/IDR 17,840 — see Sources), the Seal's $24,690 base is about ¥165,700 ex-factory, its Turkish border bill ₺2.23 million, its Indonesian bill Rp817 million.

## What the border number is missing in each market

**Turkey: the ÖTV.** The July 2025 revision raised the lowest EV band from 10% to **25%** and the higher bands to **55–75%**, keyed to motor power and tax-base bracket — the Seal's 170 kW and the YU7's 235 kW sit above the 160 kW line, the Atto 3's 150 kW below it. On the Seal's duty-paid base of $34,566, the 55–75% band adds roughly **$19,000 to $25,900 before VAT** — why [Turkey's stack is a 40% story only in the headline](/blog/turkey-import-guide/). At the cheap end, the **US$8,500 minimum additional duty** binds below roughly $28,300 of customs value; the 30% rate only takes over above it. The exact post-revision bracket thresholds (which price and power combinations land at 25%, 55%, or 75%) we could not pin to a primary schedule — **UNKNOWN** — so plan on the band range, not a single rate.

**Indonesia: the calendar.** The [50% duty is the price of standing outside the localisation programme](/blog/indonesia-import-guide/). Inside the 1 January 2026 – 31 December 2027 window, producers must build locally at a 1:1 ratio against their CBU import quotas, under TKDN domestic-content rules and a bank guarantee that is forfeit on a miss. Nine brands have committed (Geely, BYD, Citroën, VinFast, GWM, Volkswagen, Xpeng, Maxus, Aion); seven already operate facilities, reporting about Rp15.4 trillion (≈US$918 million) of investment and near 281,000 units a year of capacity. Indonesia's wall is climbable — you just climb it with a factory instead of a customs broker. The remaining border unknown is PPnBM, the luxury-goods tax: the expired incentive relieved CBU BEVs of it, and the current BEV band under the general regime is **UNKNOWN** — check any Indonesian quotation separately.

## The decision framework: which wall to climb

**If you are trading finished cars**, Turkey's wall is arithmetic you can predict (duty, VAT and ÖTV are all published numbers, even if bracket placement needs a broker); Indonesia's has a tax component you cannot price today (PPnBM). The Gulf corridor puts both in perspective: the same Seal lands at **$30,105 in Qatar (+21.9%)** and **$31,671 in the UAE (+28.3%)** — [roughly $15,600 of the Turkish bill exists purely because it is Turkey](/blog/uae-saudi-arabia-import-comparison/). Asia's two steepest walls are steep by choice, not by geography.

**If you are a brand**, the walls grade differently. Indonesia's entire incentive architecture is a carve-out for local producers — the duty is a toll on not having a factory. Turkey's stack has no equivalent door: the additional duty applies to motor cars regardless of origin (only EU/FTA-partner vehicles escape it), and the ÖTV applies to every sale, imported or domestic — which is why domestic champion TOGG gets separate support instead of a tariff carve-out.

For the sub-$30,000 volume segment, Turkey is cheaper by a few hundred dollars per car — and more punishing in absolute terms, since the ÖTV and the US$8,500 floor are why [cheap imported EVs effectively do not exist in Turkey](/blog/turkey-import-guide/). Above the crossover, Indonesia's lighter VAT wins at the border — but only with an answer for 2027.

## The Author's Take

### Position

In my view, "which wall is higher" is the wrong question. Turkey and Indonesia are not two versions of the same wall; they are two different policy sentences. Turkey's is fiscal — it taxes every EV heavily and exempts nothing. Indonesia's is industrial — it taxes finished cars and exempts factories.

### Reasoning

First, the arithmetic: the two markets land within $80 of each other on a mid-size sedan, so neither government was trying to out-tax the other — both converged on the same landing price by different routes, and both are deliberately writing off the cheap-CBU business model. Second, the $30,000 crossover is computable (`$450 − 1.5% × base`), which means "Indonesia is the most expensive ASEAN market" is true only below that line. Third, the exits differ in kind: Indonesia will settle for a factory (seven built, nine committed); Turkey offers no settlement, only band placement — which is why I treat the ÖTV bracket question, not the 40% duty, as the number an importer must nail down first.

### Disclosure

This is my analysis of published tariff schedules, tax reporting and EV Hub's landed-cost records — opinion, not legal or tax advice, and not a quotation. Modeled figures use EV Hub's tariff and vehicle records dated 15 September 2026 and exchange-rate references dated 22 September 2026. Items I could not verify from a primary source are flagged in the text — Indonesia's current PPnBM band for BEVs, the exact post-July-2025 ÖTV bracket thresholds, and Turkey's licensing path for a first-time private importer — each marked UNKNOWN rather than guessed. ÖTV brackets and localisation terms change by decree; confirm the current schedule with a licensed broker or counsel before committing capital.

## Sources

1. EY Global Tax News — "Turkiye removes additional tariffs on US, China and introduces new blanket tariffs for motor cars" (Decrees no. 10435/10436/10486; electric vehicles: 30% or US$8,500 per vehicle, whichever is greater; effective 22 September 2025) — https://globaltaxnews.ey.com/news/2025-1957-turkiye-removes-additional-tariffs-on-us-china-and-introduces-new-blanket-tariffs-for-motor-cars — published 29 September 2025; accessed 22 September 2026
2. Ember — "Türkiye ranks fourth in Europe in electric car sales" (ÖTV bands: lowest 25% and higher bands 55–75% after July 2025; previously 10% / 40–60%) — https://ember-energy.org/latest-insights/turkiye-ranks-fourth-in-europe-in-electric-car-sales/ — 2026 (2025 full-year data); accessed 22 September 2026
3. European Alternative Fuels Observatory — "Incentives and Legislation: Turkey" (pre-revision ÖTV table of 10% / 40% / 50% / 60%, as of 18 April 2025) — https://alternative-fuels-observatory.ec.europa.eu/transport-mode/road/turkey/incentives-legislations — published 18 April 2025; accessed 22 September 2026
4. Indonesia Business Post — "Indonesia to tighten fiscal policy on electric vehicles starting 2026" (no extension of CBU incentives beyond 2025; 1:1 localisation commitment; TKDN; nine brands committed, seven facilities, ~Rp15.4 trillion / US$918 million, ~281,000 units a year) — https://indonesiabusinesspost.com/5843/markets-and-finance/indonesia-to-tighten-fiscal-policy-on-electric-vehicles-starting-2026 — published 22 December 2025; accessed 22 September 2026
5. Kompas — "Indonesia to End EV Import Incentives, Eyes Billions in Tax Gains" (bank guarantee; forfeiture on missed targets) — https://go.kompas.com/read/2025/09/01/230700074/indonesia-to-end-ev-import-incentives-eyes-billions-in-tax-gains — 1 September 2025; cited via EV Hub's Indonesia guide (re-fetch attempted 22 September 2026, page did not render for extraction)
6. ExchangeRate-API (exchangerate-api.com) — USD reference rates, last update 22 September 2026: USD/CNY 6.7102 · USD/TRY 48.8242 · USD/IDR 17,840.44 — https://open.er-api.com/v6/latest/USD — accessed 22 September 2026
7. EV Hub — tariffs.json and market-master.json (Turkey duty 0.40 / VAT 0.20, Indonesia duty 0.50 / VAT 0.11, no countervailing duty in either; fixed import blocks $4,250 TR / $4,700 ID; last verified 15 September 2026)
8. EV Hub — vehicle landed-cost records (BYD Atto 3, BYD Seal, Xiaomi YU7), 15 September 2026

## Related reading

- [Turkey: 40% duty, 20% VAT, and the ÖTV bill most calculators skip](/blog/turkey-import-guide/)
- [Indonesia: 50% duty after the exemption expired](/blog/indonesia-import-guide/)
- [Thailand vs Malaysia vs Singapore vs Indonesia: which ASEAN market lands a Chinese EV cheapest?](/blog/asean-import-comparison/)
- [UAE vs Saudi Arabia: which Gulf market lands a Chinese EV cheaper?](/blog/uae-saudi-arabia-import-comparison/)
- [Qatar: the Gulf's zero-VAT import market](/blog/qatar-import-guide/)
- [Why the sticker price is never the landed price](/blog/sticker-vs-landed-price/)
- [How our landed-cost model works](/docs/landed-cost-methodology/)
- Vehicle pages: [BYD Seal](/vehicles/byd-seal/) · [BYD Atto 3](/vehicles/byd-atto-3/) · [Xiaomi YU7](/vehicles/xiaomi-yu7/)
