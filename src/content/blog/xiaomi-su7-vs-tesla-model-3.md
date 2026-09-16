---
title: "Xiaomi SU7 vs Tesla Model 3: Landed-Cost Reality Check in the EU"
description: "Xiaomi SU7 ($30,320 ex-factory, 700 km CLTC) against the Tesla Model 3 — full tariff-stack and landed-cost math in Germany and the EU, with sourcing nuance."
image: "/logo.svg"
author: "Wei Wang"
publishedDate: "2026-09-15"
draft: false
tags: [xiaomi, su7, tesla, model-3, landed-cost, eu-tariff, comparison, ev-import, germany]
---

## TL;DR

The Xiaomi SU7 and the Tesla Model 3 look like a fair fight on paper — two rear-drive electric sedans within shouting distance on size and range. They are not a fair fight on a dock in Germany, because the tariff treats them as different companies even though **both cars are built in China**.

The SU7 ex-factory price is $30,320, but it lands in Germany at **$54,504 (+79.8%)** once Xiaomi's **20.7% countervailing duty**, the 10% standard duty, 19% VAT, and the fixed freight/certification stack are applied. The Tesla Model 3 — which Europe gets from **Gigafactory Shanghai**, not Berlin — carries Tesla's individually negotiated **7.8% countervailing duty**. That 12.9-point gap is worth roughly **$5,120 on a single car** at the SU7's price point, and it is the reason a Model 3 Standard retails in Germany at **€36,990** — below the SU7's *landed cost*, before the importer adds a single euro of margin.

## Definitions

**Landed cost** — the total cost to get a vehicle from the factory gate in China to a registered, road-legal state in the destination market: base price + import duty + countervailing duty + VAT/GST + ocean freight + customs clearance + certification + registration + inland transport. EV Hub's single formula for this is documented in the [landed-cost methodology](/docs/landed-cost-methodology/).

**Countervailing duty (CVD)** — the EU's anti-subsidy tariff on Chinese-built battery-electric vehicles, layered *on top of* the standard 10% import duty. It is producer-specific, not a flat rate: BYD 17.0%, Geely 18.8%, SAIC 35.3%, Tesla (Shanghai) 7.8%, and every other cooperating exporter — including Xiaomi — at **20.7%** under Implementing Regulation (EU) 2024/2754.

**China-built vs China-brand** — the distinction that decides this comparison. "China-built" is a manufacturing fact; "China-brand" is a marketing fact. The EU tariff cares about the first one. Tesla and Xiaomi are *both* China-built for the European Model 3 and SU7 respectively, but they pay very different duty rates.

## The two cars, side by side

| Attribute | Xiaomi SU7 | Tesla Model 3 Standard RWD |
|---|---|---|
| Body | Full-size sedan (4,997 mm) | Mid-size sedan (~4,720 mm) |
| Drivetrain | RWD, single motor | RWD, single motor |
| Battery | 73.6 kWh | ~64 kWh (60 kWh usable), LFP |
| Range (claimed) | 700 km CLTC | ~534 km WLTP |
| Power | 220 kW / 400 Nm | ~286 hp (~213 kW) |
| 0–100 km/h | 5.28 s | 6.2 s |
| China ex-factory / base | $30,320 | n/a (Tesla sells retail, not ex-factory) |
| EU countervailing duty | 20.7% | 7.8% |
| Germany landed (SU7) / retail (Model 3) | $54,504 | €36,990 |

Sources: EV Hub catalog for the SU7 ([/vehicles/xiaomi-su7](/vehicles/xiaomi-su7)); Tesla Model 3 Standard specs from EV-Database and go-electra (sourced from tesla.com, March 2026). Note the range figures are not the same test cycle — 700 km CLTC versus 534 km WLTP — and should not be compared one-to-one; see the [CLTC vs WLTP explainer](/blog/cltc-vs-wltp-range/).

## The sourcing nuance most comparisons miss

The single biggest error in Xiaomi-vs-Tesla buyer math is assuming the Model 3 is "locally built" in Europe because Tesla has a German factory. It is not. Gigafactory Berlin-Brandenburg builds the **Model Y**; the **Model 3 sold in Europe has been supplied from Gigafactory Shanghai**, and that remains the case into 2026 (Teslarati/Elonbuzz, December 2025; TESMAG market analysis).

This matters for one concrete reason: a Shanghai-built Model 3 entering the EU is a *Chinese-origin BEV* and is therefore inside the countervailing-duty net — but at Tesla's individual **7.8%** rate rather than the 20.7% "other cooperating" line that Xiaomi gets. Both companies cooperated with the Commission's investigation; Tesla's individual rate reflects a lower assessed subsidy exposure.

So the honest framing is not "Chinese car vs German car." It is "Chinese car at 20.7% CVD vs Chinese-built car at 7.8% CVD." That 12.9-point spread, applied to roughly the same customs value, is the real story — and it is almost never surfaced in consumer comparisons because they price the *retail* number, not the *landed* stack.

## Worked example: Xiaomi SU7 → Germany

Itemized using the same [landed-cost methodology](/docs/landed-cost-methodology/) as the rest of the catalog, with Xiaomi's 20.7% CVD:

| Cost item | Amount (USD) | How it's calculated |
|---|---|---|
| Base price (CIF) | $30,320 | Xiaomi SU7, China ex-factory |
| Standard import duty | $3,032 | 10% of CIF |
| Countervailing duty | $6,904 | 20.7% of (CIF + duty) |
| VAT | $7,649 | 19% of (CIF + duty + CVD) |
| RoRo freight | $2,000 | China → Northern Europe |
| Customs clearance | $350 | per vehicle |
| Certification | $3,250 | homologation |
| Registration | $500 | Germany |
| Inland transport | $500 | port → buyer |
| **Total landed** | **$54,504** | **+79.8% over base** |

The countervailing duty alone ($6,904) is more than double the standard duty ($3,032) and is 22.8% of the base price by itself. The fixed stack ($6,600) adds another ~22 points of premium on top.

## The counterfactual: same car, Tesla's duty rate

The cleanest way to isolate what the CVD spread actually costs is to run the identical math with the only change being the manufacturer's rate:

| Cost item | Xiaomi (20.7% CVD) | Hypothetical (7.8% CVD) |
|---|---|---|
| Base + 10% duty | $33,352 | $33,352 |
| Countervailing duty | $6,904 | $2,601 |
| VAT (19%) | $7,649 | $6,831 |
| Fixed stack | $6,600 | $6,600 |
| **Total landed** | **$54,504** | **$49,385** |

The 12.9-point CVD difference is worth **$5,119** on this car ($4,303 in duty, plus $817 of VAT charged on top of that duty). That is derived math from EV Hub's own tariff records, not an estimate: hold every other input constant and swap 20.7% for 7.8%, and the landing price drops by roughly nine points of premium (+79.8% → +62.9%).

Put another way: the SU7 does not lose this comparison on engineering or even on its China price. It loses a large slice of it *before the car is off the boat*, purely on the duty rate attached to the brand.

## The retail reality check

Here is where the gap becomes brutal for an importer. The Tesla Model 3 Standard RWD has been listed in Tesla's German configurator from **€36,990** since December 2025 (electrive, 5 December 2025). At a rough €1 ≈ $1.08, that is about **$40,000** — and it is a *finished retail price* with Tesla's own margin already inside it.

The Xiaomi SU7's **landed cost alone** is $54,504, before the importer adds dealer margin, warranty provisioning, floorplan interest, or any discounting. Even the Model 3's larger-battery Long Range RWD (~702 km WLTP, ~84 kWh) lists around €44,990–€45,000 in France and Germany — still below the SU7's landed cost, and closer to it on spec.

The conclusion is structural, not incidental: at today's duty rates, a Xiaomi SU7 imported through the standard channel cannot be priced to undercut a Tesla Model 3 in Germany. The importer's only viable positioning is *above* Tesla on spec (size, range, interior), not below it on price — and even that is a narrow window when the Model 3 Long Range already carries 702 km WLTP.

## What buyers should ask before importing an SU7 against a Model 3

1. **"Which duty rate does my competitor actually pay?"** — the Model 3 pays 7.8%, the SU7 pays 20.7%. That is the single largest line-item difference, and it is fixed by EU regulation, not negotiable.
2. **"Am I comparing landed cost to landed cost?"** — the SU7's $30,320 is ex-factory China; the Model 3's €36,990 is German retail. Mixing the two is the fastest route to a wrong decision.
3. **"What's the destination market?"** — the 20.7% CVD applies only in the EU. In the UK, the UAE, or Australia the countervailing duty drops to zero and the SU7's economics recover sharply (see the [Xiaomi/Hongqi CVD write-up](/blog/xiaomi-hongqi-countervailing-duty/) for the market-by-market spread).
4. **"Is my volume enough to amortize certification?"** — the $3,250 certification line and the $6,600 fixed stack hit a single-vehicle import proportionally hard; batch imports spread it.
5. **"Am I quoting the same range cycle?"** — 700 km is CLTC; Tesla's ~534 km is WLTP. Quoting CLTC against a WLTP number hands the Tesla buyer a free credibility win.

## The Author's Take

**Position:** In my view, the SU7 is the better car on paper and the worse import in the EU — not because of the product, but because a 20.7% countervailing duty against a 7.8% rival is a handicap no amount of engineering can recover on a German price tag.

**Reasoning:** First, both cars are Shanghai/China-built, so the comparison is decided almost entirely by the ~12.9-point CVD spread, which costs $5,119 on a $30,320 car before a single margin is added. Second, the Model 3's German retail price (€36,990) already sits below the SU7's landed cost ($54,504), which means a price-arbitrage import thesis is dead on arrival in the EU. Third, the SU7's realistic path is outside the EU — the UK, the Gulf, and Australia, where the countervailing duty disappears and its $30,320 base price plus strong CLTC spec can actually win on value.

**Disclosure:** This is my analysis of published EU tariff law, EV Hub's landed-cost records, and public Tesla pricing — not legal or tax advice, and not a claim that the SU7 is objectively "better" or "worse" as a car. Countervailing-duty rates and covered exporters are set by EU regulation and can change; Tesla's European sourcing and pricing also move. Verify the current duty schedule and your actual destination's landed cost with a customs broker before pricing anything.

## Related reading

- [Xiaomi and Hongqi's 20.7% Countervailing Duty](/blog/xiaomi-hongqi-countervailing-duty/)
- [Why the Sticker Price Is Never the Landed Price](/blog/sticker-vs-landed-price/)
- [BYD Seal Deep Review: Landed Cost vs Model 3](/blog/byd-seal-deep-review/)
- [CLTC vs WLTP: Why Chinese Range Claims Look Inflated](/blog/cltc-vs-wltp-range/)
- [The full landed-cost formula](/docs/landed-cost-methodology/)
- [The SU7 catalog record](/vehicles/xiaomi-su7)

## Sources

1. European Commission Implementing Regulation (EU) 2024/2754 — definitive countervailing duties on Chinese BEVs (Tesla 7.8%, "other cooperating" 20.7%) — https://eur-lex.europa.eu/eli/reg_impl/2024/2754/oj — 30 October 2024
2. EV Hub catalog — Xiaomi SU7 spec and Germany landed-cost record ($30,320 base, $54,504 landed, 20.7% CVD) — verified 2026-09-15
3. electrive — "Tesla Model 3 standard starts at €36,990" (German configurator) — https://www.electrive.com/2025/12/05/tesla-model-3-standard-starts-at-e36990 — 5 December 2025
4. go-electra — "Tesla Model 3 Standard: price, range, specs" (~64 kWh LFP, 534 km WLTP, 286 hp; sourced from tesla.com/fr) — https://www.go-electra.com/en/newsroom/tesla-model-3-standard-price-range-specs-and-reviews-2026 — March 2026
5. EV-Database — Tesla Model 3 RWD (Highland): 60 kWh usable / 64 kWh nominal LFP — https://ev-database.org/car/3403/Tesla-Model-3-RWD — accessed 2026-09-15
6. Teslarati / Elonbuzz — Gigafactory Shanghai four-millionth vehicle; Shanghai supplies Model 3 volume to Europe (Berlin = Model Y) — https://elonbuzz.com/tesla-announces-major-milestone-at-gigafactory-shanghai — December 2025
7. TESMAG — Tesla Model 3 EU volume tied to Shanghai; individual CVD rate ~7.8% — https://www.teslaacessories.com/blogs/news/how-new-tariffs-are-reshaping-tesla-market-strategy-in-europe — accessed 2026-09-15
