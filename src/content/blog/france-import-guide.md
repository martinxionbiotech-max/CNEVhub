---
title: "Importing a Chinese EV to France: 10% EU Duty, Brand CVD, and 20% VAT — and a Malus Layer Outside the Math"
description: "Importing a Chinese EV to France stacks the EU's 10% standard duty, a brand-specific countervailing duty (BYD 17%, Geely 18.8%, SAIC/MG 35.3%, most other exporters 20.7%), and 20% VAT — plus a registration line our model holds flat at $400. A BYD Seal lands at about $44,631 (+80.8%) in our 30-market records: $218 above Germany and $318 below the Netherlands. France is also a Stellantis home market that both competes with these imports and distributes Chinese-built cars."
image: "/logo.svg"
author: "Wei Wang"
publishedDate: "2026-09-17"
draft: false
tags: [france, ev-import, landed-cost, eu-tariffs, countervailing-duty, vat, stellantis, chinese-ev, market-analysis]
---

## TL;DR

Importing a Chinese EV to France means the full EU stack — **10% standard duty, a brand-specific countervailing duty (BYD 17%, Geely 18.8%, SAIC/MG 35.3%, most other exporters 20.7%), then 20% VAT on the duty-paid value** — which lands a BYD Seal at about **$44,631 (+80.8%)** in EV Hub's records: $218 above Germany and $318 below the Netherlands. But France's two local wrinkles matter more than that VAT point: a registration/malus layer our model deliberately does not price, and a home-market incumbent (Stellantis) that competes with these imports while distributing a Chinese-developed brand through its own European network.

## Key statistics

- **Import duty:** 10% MFN — the EU's common external tariff on battery-electric passenger cars (CN 8703 80 10), identical at every EU border, including the French ones
- **Countervailing duty (CVD):** brand-specific and BEV-only — BYD group 17% · Geely group (incl. Zeekr, Lynk & Co) 18.8% · SAIC group (MG, Wuling, Maxus, Roewe) 35.3% · Tesla Shanghai 7.8% · other cooperating exporters 20.7% · non-cooperating 35.3%; PHEVs and EREVs sit outside the measure in our records
- **VAT:** 20% — the second-lowest rate among the EU's four largest car markets (Germany 19%, France 20%, Spain 21%, Italy 22%), charged on the duty- and CVD-paid value and recoverable for VAT-registered businesses
- **Registration:** a flat ~$400 in our model — with a warning: France's national registration regime also includes the malus on CO₂ and its weight component, which our landed model does not price per vehicle (treated as UNKNOWN below)
- **Worked example:** BYD Seal $24,690 ex-factory → **$44,631 landed (+80.8%)**
- **France vs neighbours on the same car:** Germany $44,413 · France $44,631 · Netherlands $44,949 — the France-versus-Germany gap is $218, entirely one VAT point minus a $100-cheaper registration line
- **Fixed import block:** $6,500 for France (freight $2,000 · clearance $350 · certification $3,250 · registration $400 · inland $500)

## The terms that decide this market

- **Landed cost** — what the car costs by the time it is cleared and registered: the China price, plus duty, plus CVD, plus VAT, plus freight, clearance, certification, registration and inland transport. It is not a showroom price, and it is not a quote.
- **CIF** — cost, insurance and freight; the customs-value concept the duty stack is assessed on. Our model starts from the ex-factory price and adds freight as a separate line.
- **MFN duty** — the EU's common external tariff for cars, 10%, identical in Paris, Hamburg, Rotterdam or Athens because the EU is a single customs territory.
- **CVD (countervailing duty)** — the anti-subsidy tariff Brussels imposed on China-built BEVs, set by producer rather than by destination. A BYD pays 17% at every EU border; an MG pays 35.3%. The measure passed in late 2024 and runs five years.
- **VAT** — France's standard rate is 20%, charged on the duty- and CVD-paid value at import/registration. For VAT-registered businesses it is usually a cash-flow item rather than a final cost; for private buyers it is terminal.
- **Malus** — France's registration-time vehicle tax, tied to CO₂ output with a weight-based component. It sits outside our landed-cost model, which holds a flat $400 registration line. Per-vehicle exposure for an import is outside our dataset — treat it as UNKNOWN and verify before committing (more below).
- **Réception à titre isolé** — France's national single-vehicle approval route for cars without EU whole-vehicle type approval. It is the realistic path for a private or low-volume import, and it is paperwork-heavy relative to some neighbours.
- **WVTA** — Whole Vehicle Type Approval, the EU-wide homologation route; cars not built to it need national or individual approval instead, which is where a private import's compliance budget can blow up.

## What a Chinese EV actually pays at the French border

| Layer | Rate for a China-origin BEV | Levied on | In EV Hub's landed model |
|---|---|---|---|
| Import duty | **10%** (EU MFN) | customs value | Yes |
| Countervailing duty | **17% / 18.8% / 35.3% / 20.7%** by brand | duty-paid value | Yes |
| VAT | **20%** | duty- and CVD-paid value | Yes |
| Registration | ~$400 in our records | — | Yes (flat) |
| Malus / weight component | varies by vehicle | registration-time | **No — UNKNOWN** |
| Freight, clearance, certification, inland | ~$6,100 fixed | — | Yes |

That is the whole story of why France is not a cheap landing and not an expensive one. The two customs layers — 10% plus a 17%–35.3% brand rate — are set in Brussels and collected identically whether the car clears at Le Havre, Hamburg or Rotterdam. The French variables are the 20% VAT and the national registration regime: a flat fee we can model, and a malus layer we cannot. Most markets we track stack one or two double-digit layers; France stacks three, like every EU market, and then hands the last move to its registration desk.

## Landed cost by model (France)

Figures from EV Hub's vehicle records: ex-factory China price, plus 10% duty, plus the brand CVD, plus 20% VAT, plus the fixed import block (freight, clearance, certification, registration, inland — $6,500 for France). Premium is the total uplift over the China price.

| Model | Powertrain | Brand CVD | Base (China) | France landed | Premium |
|---|---|---|---|---|---|
| Wuling Hongguang MINI EV | BEV | 35.3% | $5,000 | $15,430 | +208.6% |
| Leapmotor T03 | BEV | 20.7% | $8,440 | $19,947 | +136.3% |
| BYD Seagull | BEV | 17% | $8,940 | $20,307 | +127.1% |
| BYD Atto 2 | BEV | 17% | $10,540 | $22,778 | +116.1% |
| MG 4 | BEV | 35.3% | $9,690 | $23,806 | +145.7% |
| BYD Seal 06 DM-i | PHEV | 0% | $14,000 | $24,980 | +78.4% |
| BYD Dolphin | BEV | 17% | $14,020 | $28,152 | +100.8% |
| BYD Atto 3 | BEV | 17% | $16,260 | $31,612 | +94.4% |
| Leapmotor C10 | BEV | 20.7% | $17,300 | $34,063 | +96.9% |
| MG S5 EV | BEV | 35.3% | $16,460 | $35,897 | +118.1% |
| Zeekr X | BEV | 18.8% | $21,940 | $40,905 | +86.4% |
| BYD Han | BEV | 17% | $23,700 | $43,102 | +81.9% |
| BYD Seal | BEV | 17% | $24,690 | $44,631 | +80.8% |
| Xpeng G6 | BEV | 20.7% | $24,830 | $46,060 | +85.5% |
| Xiaomi SU7 | BEV | 20.7% | $30,320 | $54,807 | +80.8% |
| Zeekr 001 | BEV | 18.8% | $38,000 | $66,090 | +73.9% |

Three patterns are worth naming, because they explain most of the table.

First, the percentage premium falls as the price rises — the fixed import block of $6,500 hits a $5,000 microcar proportionally far harder (+208.6%) than a $38,000 Zeekr (+73.9%). The cheapest Chinese cars are rarely the cheapest *imports*; the arithmetic is the same in every market in our dataset.

Second, the brand tax is visible in the middle of the table. The MG S5 EV and the Leapmotor C10 are within $840 of each other on base price, but the S5's SAIC rate (35.3%) versus the C10's 20.7% leaves the MG $1,834 more expensive at the French border. SAIC's rate is the single biggest variable in this market for any given size of car — we covered why in our [SAIC 35.3% CVD explainer](/blog/saic-35-percent-countervailing-duty/) and the [NIO/Xpeng/Leapmotor rate-tier piece](/blog/nio-xpeng-leapmotor-countervailing-duty/).

Third, the PHEV row sits near the bottom of the premium column. The BYD Seal 06 DM-i carries no CVD — plug-in hybrids were excluded from the anti-subsidy measure — so its landing premium (+78.4%) is the lowest in the table despite a mid-table price. Keep that row in mind: whether it survives depends on a scope decision in Brussels, not on French policy.

## Worked example: a BYD Seal in France

| Line | Amount |
|---|---|
| Base price (ex-factory China) | $24,690 |
| Import duty (10%) | $2,469 |
| Countervailing duty (17%, on duty-paid value) | $4,617 |
| VAT (20%, on duty- and CVD-paid value) | $6,355 |
| Freight, clearance, certification, registration, inland | $6,500 |
| **Total landed** | **$44,631** |

Formula: `base × (1 + duty) × (1 + CVD) × (1 + VAT) + fixed costs`. Every input is from EV Hub's tariff and vehicle records dated 15 September 2026. The compounding is the part most price comparisons miss: the CVD is charged on the duty-paid value, and VAT is charged on both. Ten percent plus seventeen plus twenty is not forty-seven — the layers compound to a 54.4% uplift on the base price before the fixed block, which is why the Seal lands at +80.8% all-in. For how the model is built, see [How our landed-cost model works](/docs/landed-cost-methodology/).

Hold the car constant and change only the rate, and the brand-tier premium becomes visible: the same Seal under SAIC's 35.3% would land at about $50,595 — roughly $5,964 more, purely from the producer-level rate. Flip the exercise onto the [MG 4](/vehicles/mg-4/): its SAIC rate lands the car at $23,806, while the same base with BYD's 17% would land at $21,465 — a $2,341 difference on a car that costs less than $10,000 ex-factory. For a French importer choosing between brands, the CVD column is worth more diligence than the VAT column ever will be.

## France vs Germany vs the Netherlands: the same car, three VAT rates

Inside the EU, the duty and the CVD are identical for any given car — the only variables are VAT and each country's registration line. France charges 20% VAT with a $400 registration line; Germany charges 19% with $500; the Netherlands charges 21% with $400. Here is what that does to nine models:

| Model | Base (China) | France | Germany | Netherlands | France vs Germany | France vs Netherlands |
|---|---|---|---|---|---|---|
| Wuling Hongguang MINI EV | $5,000 | $15,430 | $15,455 | $15,504 | −$26 | −$74 |
| Leapmotor T03 | $8,440 | $19,947 | $19,935 | $20,059 | +$12 | −$112 |
| BYD Seagull | $8,940 | $20,307 | $20,292 | $20,422 | +$15 | −$115 |
| MG 4 | $9,690 | $23,806 | $23,762 | $23,950 | +$44 | −$144 |
| BYD Dolphin | $14,020 | $28,152 | $28,072 | $28,333 | +$80 | −$180 |
| BYD Atto 3 | $16,260 | $31,612 | $31,503 | $31,821 | +$109 | −$209 |
| BYD Seal | $24,690 | $44,631 | $44,413 | $44,949 | +$218 | −$318 |
| Xpeng G6 | $24,830 | $46,060 | $45,830 | $46,390 | +$230 | −$330 |
| Zeekr 001 | $38,000 | $66,090 | $65,694 | $66,587 | +$397 | −$497 |

Three readings of the table.

First, France sits between Germany and the Netherlands on every row, and on one row — the cheapest — it beats both. The France-versus-Germany delta is one VAT point on the duty-and-CVD-paid value minus the $100-cheaper registration line; for cheap cars the registration line wins and France comes out $26 ahead on the Wuling. France-versus-Netherlands is cleaner: one VAT point, same $400 registration, so France is cheaper by roughly 1% of the pre-VAT total on every row.

Second, the absolute gaps stay small — $12 to $497, or well under 1% of landed cost — against brand-driven spreads of thousands. On the same Seal, moving from BYD's rate to SAIC's adds about $5,964; no amount of VAT-point shopping inside the EU recovers that. If you are choosing between brands rather than between markets, the rate table (and the [BYD](/brands/byd/) and [SAIC](/brands/saic/) brand-level math) is where the money is.

Third, don't try to arbitrage the spread: the car is registered where it will live, and the registration country determines the VAT owed. Entry-point shopping across Le Havre, Rotterdam and Hamburg is a fiction that produces duplicate paperwork. Our [Germany vs Netherlands vs France comparison](/blog/germany-netherlands-france-import-comparison/) walks through the full argument; for France itself, widen the frame to the big four and the same Seal lands at $44,659 in Spain and $45,117 in Italy — France is the second-cheapest of the group after Germany, by $28 and $486 respectively. Outside the customs union the picture changes character entirely: the same car lands at $38,841 in the UK and $33,807 in Switzerland, because neither applies the EU countervailing duty — our [UK](/blog/uk-import-guide/) and [Switzerland](/blog/switzerland-import-guide/) guides run those numbers.

## The Stellantis factor: a home market, again

France is one of Stellantis's European home markets — Peugeot, Citroën and DS are French brands, and the group's French plants sit at the centre of the country's automotive politics the way Fiat's do in Italy. We walked through the Italy half of this story in detail in our [Italy guide](/blog/italy-import-guide/): an incumbent under pressure, courting Chinese partnerships rather than only fighting imports, with a Leapmotor stake and a distribution joint venture that puts Chinese-developed cars on European forecourts.

France shows the same contradiction from a different angle. The competitive set a French buyer weighs against a landed Seal or MG 4 includes domestically built French-brand EVs — the segment where the incumbent sets the price the import has to beat. And through the Leapmotor channel, part of the Chinese-built alternative reaches that buyer through the incumbent's own network. So an import's French margin case has to survive against the incumbent at both ends: domestic product on one side, Chinese-partnered product on the other.

We keep this section deliberately free of numbers. Our dataset tracks tariffs, taxes and landed costs; it does not include Stellantis's French production volumes, sales or market share — those are UNKNOWN in our records and we do not estimate them. For sourced detail on the group's China entanglements, the [Italy guide](/blog/italy-import-guide/) is where our records on that story live.

## What buyers should check before committing

1. **Match the CVD to the brand — and the powertrain.** Rates run from 7.8% to 35.3% and apply to BEVs; PHEVs and EREVs currently sit outside them in our records. A brand's rate, not the car's size, often decides the deal: see our [BYD](/blog/byd-countervailing-duty-landed-cost/), [Geely](/blog/geely-188-countervailing-duty/) and [startup-tier](/blog/nio-xpeng-leapmotor-countervailing-duty/) explainers.
2. **Budget the fixed block honestly.** Certification is the big variable at ~$3,250 in our model, and France's route for a non-type-approved car is the réception à titre isolé — our [WVTA vs single-vehicle approval](/blog/wvta-vs-single-vehicle-approval/) piece maps the trade-offs and the adaptation risks.
3. **Model VAT as real money.** 20% at import on the duty- and CVD-paid value; businesses should get tax advice on recovery through a French VAT registration, while private buyers should treat it as terminal.
4. **Treat the malus as an open item.** Our flat $400 registration line does not include France's malus/weight component; per-vehicle exposure is outside our dataset. Any net price promised without this line is provisional — confirm with a French broker or the registration authority.
5. **Register where you will drive.** The registration country determines VAT; cross-border arbitrage does not work in practice (see the [three-market comparison](/blog/germany-netherlands-france-import-comparison/)).
6. **Watch two things.** The scope of the CVD regime — the plug-in rows in our table are cheap because of an exemption, not a French policy — and localisation, since Europe-built Chinese-brand cars stop being imports and stop paying this table at all (context in our [export landscape piece](/blog/chinese-ev-export-landscape-2026/)).

## The Author's Take

**Position.** In my view, France is the most "normal" landing in the EU and the one most likely to mislead a spreadsheet: the customs bill is Brussels', the VAT is a point above Germany's, and the same BYD Seal lands within $218. What actually decides French outcomes sits in two places our model handles imperfectly — a registration-time malus layer we deliberately do not price, and a market whose incumbent competes with these imports on one side and distributes a Chinese-developed brand on the other. The arithmetic is nearly German; the market is not.

**Reasoning.** First, the cost structure rewards the right diligence order: France-versus-Germany and France-versus-Netherlands gaps are entirely VAT points and a $100 registration differential — $218 and $318 on the Seal — while a single brand-tier switch moves thousands: the same MG 4 differs by $2,341 between SAIC's rate and BYD's, and the same Seal differs by $5,964. Second, the malus layer is genuinely the biggest unpriced line for a French registration; our flat $400 is a simplification, the per-vehicle treatment is outside our records, and I would treat any net-price promise built without it as provisional. Third, the structural risks run through scope and localisation rather than rates: the plug-in row looks cheap because of an exemption we expect to be contested, and every Europe-built Chinese-brand car that comes online is one less unit paying this table at all. Add the incumbent's dual game, and France is a market where resale and margin assumptions deserve as much attention as the duty column.

**Disclosure.** These are my interpretations of published rules and our own records — not legal, tax or customs advice, and not a quote. Landed figures come from EV Hub's model (central-estimate fixed block; excludes incentives, dealer margin and the malus layer). The CVD rates are carried in our records as last verified 15 September 2026; a later automated re-check was blocked at the source and a manual re-verification is pending, so treat the rates as recorded rather than freshly re-confirmed. Confirm duties, origin treatment and registration with a French customs broker and the registration authority before committing capital.

## Related reading

- [Italy: 10% duty, brand CVDs, and 22% VAT in Stellantis's home market](/blog/italy-import-guide/)
- [Spain: 10% duty, brand CVD, and 21% VAT in Europe's volume-price hub](/blog/spain-import-guide/)
- [Germany vs Netherlands vs France: the VAT-only spread inside the EU](/blog/germany-netherlands-france-import-comparison/)
- [How to import a Chinese EV to the EU: the complete 2026 walkthrough](/blog/import-chinese-ev-eu-guide/)
- [Why SAIC pays the 35.3% countervailing duty](/blog/saic-35-percent-countervailing-duty/)
- [BYD's 17% countervailing duty: the full landed-cost math](/blog/byd-countervailing-duty-landed-cost/)
- [Geely's 18.8% CVD: what it means for Zeekr and Lynk & Co](/blog/geely-188-countervailing-duty/)
- [The startup tier: NIO, Xpeng and Leapmotor CVD rates](/blog/nio-xpeng-leapmotor-countervailing-duty/)
- [Xiaomi and Hongqi: the next wave's tariff math](/blog/xiaomi-hongqi-countervailing-duty/)
- [Sticker vs landed price: why they diverge](/blog/sticker-vs-landed-price/)
- [CLTC vs WLTP: reading Chinese range claims in Europe](/blog/cltc-vs-wltp-range/)
- Vehicle pages: [Wuling Hongguang MINI EV](/vehicles/wuling-hongguang-mini-ev/) · [Leapmotor T03](/vehicles/leapmotor-t03/) · [MG 4](/vehicles/mg-4/) · [BYD Dolphin](/vehicles/byd-dolphin/) · [BYD Seal](/vehicles/byd-seal/) · [Xpeng G6](/vehicles/xpeng-g6/) · [Xiaomi SU7](/vehicles/xiaomi-su7/) · [Zeekr 001](/vehicles/zeekr-001/)
- Brand pages: [BYD](/brands/byd/) · [MG](/brands/mg/) · [Leapmotor](/brands/leapmotor/) · [Xpeng](/brands/xpeng/) · [Zeekr](/brands/zeekr/) · [Xiaomi](/brands/xiaomi/) · [Wuling](/brands/wuling/)

## Sources

1. European Commission — Commission Implementing Regulation (EU) 2024/2754, definitive countervailing duties on battery-electric vehicles from China (brand-level rates; five-year term; effective 30 October 2024) — https://eur-lex.europa.eu/eli/reg_impl/2024/2754/oj — rates carried in our records as last verified 15 September 2026; a later automated re-check was blocked at source, values unchanged, manual re-verification pending
2. European Commission — TARIC / Common Customs Tariff, CN 8703 80 10: 10% MFN duty on battery-electric passenger cars — https://ec.europa.eu/taxation_customs/dds2/taric/taric_consultation.jsp — record dated 15 September 2026
3. EV Hub — `tariffs.json` and `market-master.json` (France: standard duty 10%, VAT 20%, registration ~$400, brand CVD table, fixed-cost inputs; France is an EU market with countervailing duty in force) — internal dataset, last verified 15 September 2026
4. EV Hub — vehicle landed-cost records: 30 markets × 517 models with itemised duty/CVD/VAT/fixed block (France, Germany, Netherlands, Italy, Spain, UK and Switzerland rows used above) — internal dataset, records updated 7–14 September 2026
5. National tax authorities — French standard VAT rate of 20% (and comparative EU rates) as carried in our market records — accessed via EV Hub dataset, 15 September 2026
