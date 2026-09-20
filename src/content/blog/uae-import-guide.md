---
title: "Importing a Chinese EV to the UAE: 5% GCC Duty, 5% VAT, and the Middle East's Re-Export Hub"
description: "The UAE charges a 5% GCC duty, 5% VAT and a $300 registration — a BYD Seal lands at $31,670.73 (+28.3%): $2,592 under Saudi Arabia, $12,743 under Germany, and only Qatar lands cheaper. The UAE stack, model by model."
image: "/logo.svg"
author: "Wei Wang"
publishedDate: "2026-09-17"
draft: false
tags: [uae, gulf, import-duty, vat, landed-cost, ev-import, market-guide, middle-east]
---

## TL;DR

The UAE sits at the centre of Gulf EV importing — the region's largest re-export hub, with an import stack that is three lines: **5% GCC duty, 5% VAT on the duty-paid value, and a $300 registration fee** — and no countervailing duty, because [that measure is EU-only](/blog/byd-countervailing-duty-landed-cost/). A [BYD Seal](/vehicles/byd-seal/) at $24,690 ex-factory lands at **$31,670.73 (+28.3%)**: $2,592 under Saudi Arabia, $12,743 under Germany, and $1,566 over Qatar, which charges no VAT at all.

## Key statistics

- **Import duty (UAE): 5%** — the GCC common external tariff on cars; no countervailing duty in the Gulf
- **VAT (UAE): 5%** — charged on the duty-paid value; [Qatar](/blog/qatar-import-guide/) charges 0%
- **Registration: $300** in EV Hub's model — ten times Qatar's $30, level with Saudi Arabia's $300
- **Worked example:** BYD Seal $24,690 → **$31,670.73 landed (+28.3%)**
- **UAE vs Saudi Arabia:** the UAE lands every model in this guide $525 to $3,990 cheaper
- **UAE vs Qatar:** Qatar lands cheaper on all eight models, by $532.50 to $2,265 — the spread is 5% VAT plus $270
- **Premium range inside the UAE:** +22.0% (Zeekr 001) to +99.3% (Wuling Hongguang MINI EV)
- **For contrast:** the same Seal lands at $44,413.48 in Germany (+79.9%)

Price basis, stated once and meant everywhere below: every base price is a **China ex-factory MSRP** — not a retail price, not a CIF quote. Every landed figure is EV Hub's model output, and every line is decomposed so you can rerun the arithmetic with your own numbers.

## The stack, as the model counts it

Three Gulf markets, one duty rate, three different bills:

| Layer | UAE | Qatar | Saudi Arabia |
|---|---|---|---|
| Standard import duty | 5% | 5% | 5% |
| Countervailing duty | none | none | none |
| VAT | **5%** | 0% | 15% |
| Registration (model input) | $300 | $30 | $300 |
| Fixed block — freight, clearance, certification, inland | $4,150 | $4,150 | $4,150 |

Read the table as a map: duty is identical across all three, so the entire spread between these lanes is consumption tax plus a registration line. The UAE sits in the middle — five points of VAT above Qatar, ten below Saudi Arabia, and a registration fee that matches Riyadh rather than Doha.

There is also no brand dimension to the UAE border. No countervailing duty, no producer-specific anti-subsidy measures — [BYD](/brands/byd/), [MG](/brands/mg/), [XPeng](/brands/xpeng/) and [Zeekr](/brands/zeekr/) cross the border on identical terms, which is not something any EU importer can say.

Rates from EV Hub's `market-master.json` and `tariffs.json` (verified 15 September 2026); cross-checked against the PwC country summaries in Sources. One modelling note before anyone budgets off this: the model applies duty to the ex-factory price as a simplified CIF. A customs assessor may value the car differently — and value is the single most common place an otherwise clean UAE deal moves. Treat every number here as a planning floor, not a quote.

## Worked example: a BYD Seal into the UAE

| Line | Amount |
|---|---|
| Base price (China ex-factory MSRP) | $24,690.00 |
| GCC import duty (5%) | $1,234.50 |
| VAT (5%) | $1,296.23 |
| RoRo freight | $2,000.00 |
| Customs clearance | $350.00 |
| Certification / GCC-spec compliance | $1,300.00 |
| Registration | $300.00 |
| Inland transport | $500.00 |
| **Total landed** | **$31,670.73** |

Formula: `24,690 × (1 + 0.05) × (1 + 0.05) + 4,450 = 31,670.73`. The $4,450 is the full fixed block — $2,000 freight, $350 clearance, $1,300 certification, $300 registration, $500 inland — the same inputs held constant between the three Gulf markets so the comparison isolates tax treatment.

The shape of the number: the border adds $6,980.73 to a $24,690 car. Of that, duty is $1,234.50, VAT is $1,296.23, and $4,450 — about two-thirds — is the fixed block. That structure is why the UAE's percentage premium runs from +22.0% on a $38,000 [Zeekr 001](/vehicles/zeekr-001/) to +99.3% on a $5,000 [Wuling Hongguang MINI EV](/vehicles/wuling-hongguang-mini-ev/): flat costs hurt cheap cars hardest.

## Model by model: UAE vs Qatar vs Saudi Arabia

Same eight models, same week's data, three destinations. All figures USD; bases are China ex-factory MSRPs:

| Model | Base (China) | UAE landed | Qatar landed | Saudi landed | Qatar cheaper than UAE by | UAE cheaper than Saudi by |
|---|---|---|---|---|---|---|
| Wuling Hongguang MINI EV | $5,000 | $9,962.50 | $9,430 | $10,487.50 | $532.50 | $525 |
| BYD Seagull | $8,940 | $14,306.35 | $13,567 | $15,245.05 | $739.35 | $938.70 |
| MG4 | $9,690 | $15,133.23 | $14,354.50 | $16,150.68 | $778.73 | $1,017.45 |
| BYD Dolphin | $14,020 | $19,907.05 | $18,901 | $21,379.15 | $1,006.05 | $1,472.10 |
| BYD Atto 3 | $16,260 | $22,376.65 | $21,253 | $24,083.95 | $1,123.65 | $1,707.30 |
| BYD Seal | $24,690 | $31,670.73 | $30,104.50 | $34,263.18 | $1,566.23 | $2,592.45 |
| XPeng G6 | $24,830 | $31,825.08 | $30,251.50 | $34,432.23 | $1,573.58 | $2,607.15 |
| Zeekr 001 | $38,000 | $46,345 | $44,080 | $50,335 | $2,265 | $3,990 |

Three patterns worth naming. First, the direction never flips inside the Gulf: Qatar lands cheapest on all eight, the UAE sits second on all eight, and Saudi Arabia pays most on all eight. Second, both gaps decompose exactly — Qatar's edge over the UAE is 5% of the duty-paid value plus $270 of registration, and the UAE's edge over Saudi Arabia is the ten-point VAT difference (5% against 15%) on the same duty-paid base; nothing about shipping or access explains either spread. Third, the edges scale with price: the microcar math is the ugliest in percentage terms, with the Wuling's +99.3% UAE premium the worst number in the table, while the biggest absolute saving — $3,990 on the Zeekr — lands at the top of the price range.

If you want the same dataset argued from the other direction, the [UAE vs Saudi Arabia deep dive](/blog/uae-saudi-arabia-import-comparison/) runs the full comparison, and the [Qatar guide](/blog/qatar-import-guide/) covers the zero-VAT lane in detail. Full 30-market landed-cost records for these models live on their vehicle pages: [BYD Seal](/vehicles/byd-seal/), [BYD Seagull](/vehicles/byd-seagull/), [BYD Dolphin](/vehicles/byd-dolphin/), [BYD Atto 3](/vehicles/byd-atto-3/), [MG4](/vehicles/mg-4/), [XPeng G6](/vehicles/xpeng-g6/), [Zeekr 001](/vehicles/zeekr-001/), [Wuling Hongguang MINI EV](/vehicles/wuling-hongguang-mini-ev/).

## Why the UAE matters beyond its own market

The UAE is the Middle East's largest re-export hub, and that is the reason to read it as a platform rather than a single destination. Jebel Ali and the surrounding free zones are built for exactly this: clear the car once, then move it onward — to East Africa, the CIS, South Asia, wherever the next buyer sits. For an importer, that optionality is the part no tariff table shows: a UAE clearance can feed more than one market's demand, and the emirates' left-hand-drive convention matches China-built cars, so nothing gets converted on arrival. The onward paperwork — free-zone storage, re-export documentation, whatever duty treatment applies on the second leg — is its own conversation with a broker. The first leg, at 5% duty, is about as clean as import math gets.

Two more structural details keep the model honest. The dirham is pegged to the dollar, so FX risk stays out of the landed-cost arithmetic — rare among the markets EV Hub tracks. And the UAE has already switched its VAT on at 5%, which means the number you model today is the number you can argue about today; there is no pending rate transition to hedge, unlike the [Qatar lane](/blog/qatar-import-guide/), where the GCC VAT framework sits agreed but unimplemented. One more nuance on drive configuration: matching China's LHD build is an advantage the UAE shares with Saudi Arabia, and the [LHD vs RHD breakdown](/blog/lhd-vs-rhd-markets/) shows why that quietly eliminates a whole cost category that right-hand-drive markets carry.

## Where the numbers could move

- **Importer margin is not in the figure.** Every number above is a landed cost, not a retail price. A UAE dealer's margin, warranty provisioning and floorplan sit on top.
- **Customs valuation is the live risk.** The model treats the ex-factory price as simplified CIF. If your assessor picks another basis — transaction value, reference pricing — the whole column shifts.
- **Registration is a model input at $300.** Confirm the actual fee schedule for your vehicle class with the emirate's traffic authority.
- **Certification is a model input at $1,300.** First-of-model homologation for small volumes can run above the Gulf-spec block held in the model.
- **Gulf-spec matters.** The car that lands is a China-market car until it is made Gulf-compliant — climate adaptation, charging interface, documentation. Budget the compliance work, not just the duty.
- **Service and parts.** Who supports the car in the UAE, and what does the warranty look like on a private import? After a clean customs file, this is usually where Gulf importers discover the real cost.

## What buyers should check before committing

1. **The customs treatment, in writing** — duty base, classification, and whether your structure (mainland purchase versus free-zone entity) changes the answer.
2. **The registration schedule for your exact vehicle class** with the emirate's traffic authority — the $300 here is a model input, not a fee schedule.
3. **Homologation and GCC-spec equipment** for the specific variant — not the brochure spec, the one on your invoice.
4. **The re-export route, if that is your plan** — free-zone rules, documentation and second-leg logistics priced before you commit, not after.
5. **Warranty and parts support** in the UAE — the after-sales file often decides whether a good landed number becomes a good deal.

Before wiring anything, run the Qatar lane against your own numbers. The five-point VAT gap is easy to audit: on the Seal it is $1,296 of VAT plus $270 of registration; on a $100k car, roughly $5,250 plus $270. One spreadsheet cell is all it takes to know which lane your margin actually lives in.

## The Author's Take

**Position.** In my view, the UAE is the Gulf lane to build a channel around: it lands every model in this guide between $525 and $3,990 under Saudi Arabia and between $532.50 and $2,265 over Qatar, while offering the region's deepest port, free-zone and re-export infrastructure — and infrastructure compounds in a way a five-point VAT edge does not.

**Reasoning.** First, the UAE's cost position relative to its neighbours is exactly two numbers — VAT and registration — and both are published, stable and auditable, so there is no hidden margin inside the spread; most import corridors cannot say the same. Second, the re-export plumbing changes what a UAE clearance is worth: the same entry can serve East Africa, the CIS or South Asia, and a left-hand-drive market that matches China's build means no conversion cost on the first leg. Third, the comparison with Qatar is a spread, not a strategy — Qatar's zero VAT is worth $532.50 to $2,265 per car in this dataset, and if a GCC-framework VAT ever reaches Doha, the two lanes converge to within registration. The UAE's structural position — ports, free zones, an LHD fleet — survives that convergence. A VAT arbitrage does not.

**Disclosure.** This is my analysis and opinion, not tax, customs or legal advice. Landed figures are EV Hub model estimates from records dated 15 September 2026; UAE, Qatar and Saudi tax rates come from the PwC country summaries below, checked on 17 September 2026. Confirm the treatment of your exact vehicle, buyer structure and re-export route with a UAE customs broker and the relevant traffic authority before committing capital.

## Sources

1. PwC — "United Arab Emirates — Corporate — Other taxes" (VAT 5%; customs duty generally 5% of CIF; GCC Customs Union context) — https://taxsummaries.pwc.com/united-arab-emirates/corporate/other-taxes — accessed 17 Sep 2026
2. PwC — "Qatar — Corporate — Other taxes" (no VAT or sales tax currently; customs duties on non-GCC origin normally 5%) — https://taxsummaries.pwc.com/qatar/corporate/other-taxes — accessed 17 Sep 2026
3. PwC — "Saudi Arabia — Corporate — Other taxes" (standard VAT rate 15% since 1 July 2020) — https://taxsummaries.pwc.com/saudi-arabia/corporate/other-taxes — accessed 17 Sep 2026
4. European Commission (EUR-Lex) — Commission Implementing Regulation (EU) 2024/2754 (countervailing duties on China-origin BEVs — the measure the Gulf does not apply) — https://eur-lex.europa.eu/eli/reg_impl/2024/2754/oj — accessed 17 Sep 2026
5. European Commission (Access2Markets) — "EU Commission imposes countervailing duties on imports of battery electric vehicles (BEVs) from China" — https://trade.ec.europa.eu/access-to-markets/en/news/eu-commission-imposes-countervailing-duties-imports-battery-electric-vehicles-bevs-china — accessed 17 Sep 2026
6. EV Hub — `market-master.json` and `tariffs.json` (UAE 5% duty / 5% VAT / $300 registration; Qatar 5% / 0% / $30; Saudi Arabia 5% / 15% / $300; fixed-cost inputs; verified 15 Sep 2026)
7. EV Hub — vehicle landed-cost records: UAE, Qatar and Saudi Arabia rows for the eight models in this guide (data updated 7 Sep 2026)

## Related reading

- [Qatar import guide — the Gulf's zero-VAT lane](/blog/qatar-import-guide/)
- [UAE vs Saudi Arabia: which Gulf market lands a Chinese EV cheaper](/blog/uae-saudi-arabia-import-comparison/)
- [Why the sticker price is never the landed price](/blog/sticker-vs-landed-price/)
- [Left-hand-drive vs right-hand-drive markets](/blog/lhd-vs-rhd-markets/)
- [Gulf import overview (docs)](/docs/uae-saudi-import/)
- [Landed cost methodology (docs)](/docs/landed-cost-methodology/)
- [BYD Seal landed-cost record](/vehicles/byd-seal/)
