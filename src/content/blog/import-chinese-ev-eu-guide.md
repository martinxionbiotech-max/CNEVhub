---
title: "How to Import a Chinese EV to the EU: Complete 2026 Guide"
description: "A step-by-step guide to importing Chinese EVs into the EU, with the full tariff stack (10% duty + countervailing duty + VAT), a landed-cost formula, and a worked BYD Seal example."
author: "Wei Wang"
publishedDate: "2026-09-05"
draft: false
tags: [import, eu, tariff, countervailing-duty, wltp, ev, china, byd, landed-cost]
---

## TL;DR

Importing a Chinese EV into the EU isn't a single tax — it's a stacked calculation. You pay the standard 10% duty, then a countervailing duty (CVD) of 17% to 35.3% depending on the brand [Source: European Commission, October 2024], and then VAT on top of both. A BYD Seal Premium that costs $24,690 in China lands at roughly $44,413 in Germany — a 79.9% increase — before you've paid a cent of dealer margin. The good news: VAT is recoverable if you're VAT-registered, and a handful of brands (including Tesla's Shanghai plant) got sharply lower individual CVD rates.

## Key Statistics

- **Standard EU import duty on Chinese EVs:** 10% of CIF value [Source: EU Common Customs Tariff, TARIC classification 8703.80]
- **Countervailing duty (CVD) range:** 17.0% (BYD) to 35.3% (SAIC/MG) [Source: European Commission Implementing Regulation (EU) 2024/2754, October 2024]
- **Other "cooperating" producers:** ~20.8%; the rest treated as "non-cooperating" at ~35.3% [Source: European Commission, October 2024]
- **Tesla Shanghai's individual CVD rate:** significantly lower, set at 7.8% [Source: European Commission, October 2024]
- **CVD duration:** 5 years, effective 31 October 2024 [Source: European Commission]
- **EU VAT rates:** Germany 19%, France 20%, Netherlands 21%, Italy 22%, Spain 21%, Portugal 23% [Source: European Commission VAT rates database, 2025]
- **RoRo shipping from Shanghai to EU port:** roughly $1,500–$2,500 per vehicle [Source: industry freight quotes, 2025]
- **WLTP vs CLTC discrepancy:** CLTC range figures run 15–30% higher than real-world WLTP [Source: multiple independent EV range tests, 2023–2025]

---

# How to Import a Chinese EV to the EU: The Complete 2026 Guide

If you're a fleet buyer, a dealer, or a private importer eyeing the price gap between Chinese EV sticker prices and what the same cars fetch in Europe, you've probably already run the "saving" in your head. Car costs $25k in Shanghai. Equivalent German EV costs €45k. Easy money, right?

Not quite. The moment you add up duty, countervailing duty, VAT, freight, certification, and registration, that margin compresses hard — and in some cases disappears entirely.

I've spent the last several years on the ground at MCM (广州邦禾检测技术有限公司), helping importers and distributors figure out what a Chinese EV actually costs by the time it's legal to drive on a European road. This guide walks through the full 10-step process, unpacks the three-layer tariff stack, and ends with a worked cost example on a BYD Seal so you can see exactly where the money goes.

Let's get the definition locked in first, because the whole exercise turns on it.

**Definition:** A *countervailing duty (CVD)* is an additional import tax the EU applies on top of the standard customs duty, designed to offset subsidies a foreign government gives its exporters. For Chinese EVs, the EU applies a brand-specific CVD of between 7.8% and 35.3% on top of the 10% standard duty [Source: European Commission Implementing Regulation (EU) 2024/2754].

So what does that mean in practice? You don't add 10 + 35.3 + 19. You *compound* them. That's the single most expensive misunderstanding in this business, and I'll show you the math in full later.

---

## The 10-Step Import Process

Before we touch numbers, you need the sequence. Almost every failed import I've seen collapsed because someone did step 7 before step 3. Here's the order that keeps you out of trouble.

| # | Step | What actually happens | Typical lead time |
|---|------|----------------------|-------------------|
| 1 | Select the vehicle | Confirm exact trim, battery spec, VIN availability | 1–2 weeks |
| 2 | Supplier due diligence | Verify export license, COC documentation, payment terms | 1–3 weeks |
| 3 | Place the order | Signed proforma invoice, deposit (usually 10–30%) | 1 week |
| 4 | Payment | Balance before shipment; consider escrow or LC | 1–2 weeks |
| 5 | Ocean freight | RoRo or container from Chinese port to EU port | 4–8 weeks |
| 6 | Customs clearance | Broker files entry, duty + CVD assessed | 3–7 days |
| 7 | Pay duties & VAT | Duty + CVD at import; VAT due or deferred | At clearance |
| 8 | Certification & homologation | EU WVTA or German §21 single-vehicle approval | 2–6 weeks |
| 9 | Registration | Local authority plates & road tax | 1–2 weeks |
| 10 | Delivery | Inland transport to buyer or pickup | 2–7 days |

Note the two long poles: ocean freight (4–8 weeks) and certification (2–6 weeks). Budget 3–4 months end to end on your first import. It gets faster once you've got a supplier and a homologation route dialed in.

### Step 1: Selecting the Vehicle

The vehicle has to exist in a configuration that can be homologated for Europe. Not every Chinese-market trim has a matching EU type approval. The safest picks are models already sold in the EU — BYD Seal, Atto 3, Dolphin, MG4, and a few XPeng and NIO models — because they carry existing EU type approval you can lean on [Source: European type-approval database, and manufacturer announcements]. Browse the full catalog of importable models in our [vehicles directory](/vehicles/) if you're still sizing up the field.

If you're importing a model with no EU presence, you're into single-vehicle approval territory, which is slower and pricier. More on that in the certification section.

### Step 2: Supplier Due Diligence

This is where I've seen importers lose six figures. You're wiring tens of thousands of dollars to a company you've never visited.

Check at least these three things before any payment:

1. **Export license** — legitimate Chinese auto exporters hold a valid business license with vehicle export rights. Ask for it and verify it against the Chinese company registry (国家企业信用信息公示系统).
2. **COC (Certificate of Conformity)** — if the model has EU type approval, the manufacturer issues a CoC. Without it, you're relying on single-vehicle approval. This is often the difference between a 2-week and a 6-week certification.
3. **Payment terms** — never pay 100% upfront to a first-time supplier. Standard practice is a 10–30% deposit with the balance due against a bill of lading. A supplier demanding full payment before shipment is a red flag.

A quick sanity check I always run: ask for a recent bill of lading with a destination port in the EU. A real exporter can produce one in under a day. If they can't, be careful.

### Step 3: Placing the Order

You'll get a proforma invoice (PI) that lists the vehicle, the specification, the unit price in USD or EUR, and the Incoterm. Pay attention to the Incoterm — it determines who owns the freight risk:

- **FOB (Free on Board)** — supplier handles export clearance and gets the car to the Chinese port. You take over from there. This is the most common for first-time importers.
- **CIF (Cost, Insurance, Freight)** — supplier pays freight and insurance to the EU port, and you pay a single landed figure. Convenient, but you forfeit control over the freight forwarder.

Most of my clients start with FOB so they control the forwarder and the certification paperwork from day one.

### Step 4: Payment

Importers with volume use Letter of Credit (LC). First-timers often use T/T wire transfer with staged payments. Whatever you choose, document everything — the PI, the wire confirmation, the loading photos, the bill of lading.

One thing to flag: Chinese suppliers increasingly prefer settlement in USD, and some export via Hong Kong or via a trading company. Confirm the exact legal entity you're paying before you send anything.

I'll hold the remaining steps (freight through delivery) for the sections below, where the money actually moves.

### Step 5: Ocean Freight

Chinese EVs almost always ship RoRo (roll-on/roll-off) — the car drives onto a purpose-built vessel and off at the destination port. RoRo is cheaper and simpler than containerizing a vehicle.

Current pricing runs roughly $1,500–$2,500 per vehicle from Shanghai or Ningbo to a major northern European port like Rotterdam, Hamburg, or Antwerp [Source: 2025 ocean freight spot and contract quotes from major forwarders]. That figure has been volatile post-Red Sea disruptions, so treat it as a planning number, not a quote.

Transit time: 4–8 weeks depending on routing and port congestion.

If you're importing a single high-value vehicle, container shipping (in a 40ft or 45ft flat/open-top) is occasionally cheaper on a per-car basis for one-offs, but RoRo wins for anything over a couple of units.

### Step 6: Customs Clearance

A licensed customs broker files the entry against the EU TARIC code for the vehicle. Electric passenger cars fall under CN code **8703.80.10** [Source: EU Combined Nomenclature / TARIC]. The broker declares the CIF value (vehicle cost + freight + insurance) and that becomes the customs value — the base the duties are calculated on.

Clearance itself costs around $350 in broker and port handling fees [Source: typical EU broker fee schedules, 2025].

This is also where you pay — or defer — the duty and VAT. I'll get into the exact amounts right now.

### Step 7: The Three-Layer Tariff Stack

Here's the part that separates a profitable import from a loss. You pay three layers, and they *compound*, they don't add.

**Layer 1 — Standard import duty: 10%.** Applied to the CIF value (car + freight + insurance) [Source: EU Common Customs Tariff, CN 8703.80]. Every car, no exceptions, no brand-specific relief.

**Layer 2 — Countervailing duty (CVD): 17%–35.3%, brand-specific.** The EU concluded its anti-subsidy investigation in October 2024 and imposed a five-year CVD, effective 31 October 2024 [Source: European Commission Implementing Regulation (EU) 2024/2754]. Here's the breakdown by producer:

| Manufacturer / Group | CVD rate | Notes |
|----------------------|----------|-------|
| BYD | 17.0% | Lowest among the "sampled" Chinese producers |
| Geely (incl. Zeekr, Polestar) | 18.8% | |
| SAIC (MG, Maxus) | 35.3% | Highest; deemed non-cooperating |
| Other cooperating companies | ~20.8% | Weighted average for those that cooperated but weren't sampled |
| Non-cooperating companies | ~35.3% | Residual duty |
| Tesla (Shanghai Gigafactory) | 7.8% | Individual rate, far below the Chinese producers |

Source: European Commission Implementing Regulation (EU) 2024/2754, October 2024.

Two things jump out. First, Tesla Shanghai got 7.8% — the EU treated it separately on grounds it received fewer subsidies, so a Shanghai-built Tesla lands much lighter than a BYD or an MG. Second, MG (SAIC) is the most heavily penalized at 35.3%, which is why MG's aggressive European pricing had to be reworked once the duty bit.

**Layer 3 — VAT.** Applied on the *customs value plus duty plus CVD* — in other words, VAT is charged on a number that already includes both duties [Source: EU VAT Directive 2006/112/EC and national transposition]. That's the compounding I keep harping on.

European VAT rates differ by member state:

| Country | Standard VAT rate |
|---------|-------------------|
| Germany | 19% |
| France | 20% |
| Netherlands | 21% |
| Italy | 22% |
| Spain | 21% |
| Portugal | 23% |
| UK (post-Brexit, separate regime) | 20% |

Source: European Commission VAT rates in the EU, 2025.

**Why compounding matters.** If you naively add 10 + 17 + 19 = 46%, you'll under-budget. The real multiplier is (1.10) × (1.17) × (1.19) = 1.532 — that's a 53.2% uplift on the CIF value, not 46%. On a $25,000 car, the difference between naive and compounded is over $1,800 — and on an MG with a 35.3% CVD, the compounding gap is even wider.

This is exactly why we built a dedicated calculator. Before you commit to a purchase, run the numbers through our [landed cost calculator](/landed-cost-calculator/) rather than eyeballing it. And if you want the full derivation of the formula and why every factor multiplies, read our [landed cost methodology](/landed-cost-methodology/).

### Step 8: Certification & Homologation

A car can't get EU plates unless it's type-approved. You have two routes, and they're very different in cost and speed.

**Route A — EU Whole Vehicle Type Approval (WVTA).** Governed by Regulation (EU) 2018/858. If the model already holds a valid EU WVTA (which it will, if the manufacturer officially sells it in Europe), you can import against that approval. You need the manufacturer's Certificate of Conformity (CoC), which is issued per-VIN [Source: Regulation (EU) 2018/858].

The catch: some Chinese manufacturers won't issue a CoC to a grey importer, because they'd rather you buy through their European distribution. That single document is often the make-or-break of a whole import. If you can't get the CoC, you're pushed to Route B.

**Route B — Single Vehicle Approval (Germany: §21 StVZO).** This is Germany's national individual-approval path for vehicles without EU type approval. A technical inspection body (TÜV, DEKRA, or similar) physically inspects the car, verifies it meets applicable safety and emissions requirements, and issues a single-vehicle certification [Source: German Road Traffic Licensing Regulation, §21 StVZO].

It's slower and more expensive. Certification costs run roughly $1,500–$5,000 per vehicle depending on whether you need light modifications (European headlamps, speedometer in km/h, rear fog lamp), retesting, and the inspection body's fees [Source: TÜV/DEKRA single-vehicle approval fee ranges, 2025]. You'll also need a Certificate of Conformity to individual requirements, plus often a certificate proving the vehicle meets EU noise and EMC rules.

The classic first-time failure: importing a Chinese-market car with a GB/T charging inlet and a Chinese-only speedometer, then discovering neither is legal for EU road use without modification. Budget for the modifications *before* you buy, not after.

### Charging Standard: GB/T vs CCS2 / Type 2

China uses **GB/T** charging connectors (AC and DC). Europe uses **Type 2** for AC and **CCS2** for DC fast charging. These are physically incompatible [Source: CHAdeMO/IEC 62196 and GB/T 20234 standards].

What that means for you:

- A China-spec EV won't plug into a European AC charger or a CCS2 fast charger without a conversion. GB/T-to-Type2 adapters exist for AC, but GB/T-to-CCS2 DC fast-charging adapters are larger, expensive, and not universally reliable.
- The right fix is a factory-conversion to CCS2/Type 2 — and that's only realistic if the model has an EU version. BYD, MG, and the others that sell in Europe already build CCS2 versions with EU charging electronics.
- If you import a China-only trim and rely on adapters, you're accepting a compromised charging experience that no fleet customer will tolerate.

For anyone buying at volume, the rule is simple: import the EU-spec version, not the China-market version. The charging inlet alone decides how sellable the car is.

### Range: WLTP vs CLTC vs NEDC

This is the number-one buyer-confusion issue, and it feeds directly into how you market an imported car.

- **WLTP** (Worldwide Harmonised Light Vehicles Test Procedure) is the EU's real-world-oriented test cycle [Source: EU WLTP regulation and type-approval framework].
- **CLTC** (China Light-duty Test Cycle) is China's equivalent. It rewards frequent low-speed, stop-start driving, which inflates range figures relative to real-world and WLTP numbers.
- **NEDC** is the old, now-withdrawn European cycle — even more optimistic than WLTP.

In practice, CLTC range figures run roughly **15–30% higher** than what the same car scores on WLTP [Source: multiple independent EV range comparisons, 2023–2025]. A Chinese-market listing that boasts "700km CLTC" will show perhaps 550–600 km on WLTP — and the real-world number at highway speeds is lower still.

If you're advertising imported stock in the EU, you *must* quote WLTP, not CLTC. Misleading range claims land distributors in consumer-protection trouble, and the EU has no tolerance for a spec sheet that says 700 km when the dashboard reads 520.

Our [BYD Seal deep review](/blog/byd-seal-deep-review/) digs into this exact gap on a real model — the claimed CLTC number versus the WLTP-certified figure versus what owners actually see.

### Step 9: Registration

Once homologated, you register the vehicle with the local authority in your target member state. Registration fees run roughly $400–$500 in most EU countries, plus road tax where applicable [Source: national vehicle registration fee schedules, 2025]. Electric vehicles get favorable treatment in several markets — some countries waive road tax for EVs, and a few (like Norway, historically) go further, but the EU core markets generally levy registration costs regardless of powertrain.

One legal note: you'll need proof of insurance *before* registration in most member states, and the vehicle must be physically in the country for the inspection in the single-vehicle-approval route.

### Step 10: Delivery

The final leg — inland transport from the port or inspection facility to the buyer. For a single vehicle within Germany or the Benelux, budget around $500; longer hauls to southern or eastern Europe cost more [Source: European automotive logistics quotes, 2025].

### Full Fee Breakdown (Planning Numbers)

| Cost item | Typical range (per vehicle) |
|-----------|------------------------------|
| Ocean freight (RoRo, Shanghai → EU) | $1,500–$2,500 |
| Customs clearance & port handling | ~$350 |
| Certification / homologation | $1,500–$5,000 |
| Registration | $400–$500 |
| Inland transport | ~$500 |

Source: consolidated 2025 freight, broker, and inspection-body quotes. These are planning ranges, not firm bids — confirm with your forwarder and broker before you commit.

---

## The Landed-Cost Formula (and a Worked Example)

Now the part you came for. The full formula:

**Landed cost = Vehicle price × (1 + duty) × (1 + CVD) × (1 + VAT) + freight + clearance + certification + registration + inland transport**

Note the three taxes *multiply* the vehicle price, and the fixed fees *add* on top. Here's exactly what that looks like on a real car.

### Worked Example: BYD Seal Premium → Germany

Take a BYD Seal Premium with a China market price of **$24,690** [Source: BYD official China pricing, 2025]. Import to Germany (VAT 19%, BYD CVD 17.0%).

| Line item | Amount (USD) | Calculation |
|-----------|--------------|-------------|
| Base vehicle price | $24,690 | — |
| Standard duty (10%) | $2,469 | 24,690 × 0.10 |
| Countervailing duty (17.0%) | $4,617 | (24,690 + 2,469) × 0.17 |
| VAT (19%) | $6,037 | (24,690 + 2,469 + 4,617) × 0.19 |
| Ocean freight | $2,000 | RoRo, Shanghai → Hamburg |
| Customs clearance | $350 | broker + port handling |
| Certification | $3,250 | mid-range WVTA/single-vehicle |
| Registration | $500 | Germany |
| Inland transport | $500 | port → buyer |
| **Total landed cost** | **$44,413** | — |

Source: calculation based on the formula above and European Commission Implementing Regulation (EU) 2024/2754 duty rates; fee figures are 2025 planning estimates.

That's **$44,413 from a $24,690 car — a 79.9% increase.** The taxes alone (duty + CVD + VAT) turn a $24,690 car into a $37,813 taxable base. The fixed fees add another $6,600.

And remember, this is *before* any dealer margin, before any homologation modifications like a speedometer or charge-port swap, and before marketing.

Compare that to a Shanghai-built Tesla carrying a 7.8% CVD instead of 17%: the same $24,690 base would save roughly $2,200 in CVD cascade (because the lower CVD also shrinks the VAT base). Brand choice alone moves the landed price by thousands.

Two tax notes that decide whether this works for you:

1. **VAT is recoverable.** If you're a VAT-registered importer, you reclaim the $6,037 in the example as input VAT. That drops your *net* landed cost to ~$38,376 [Source: EU VAT Directive 2006/112/EC input-VAT deduction rules].
2. **CVD is not recoverable.** The $4,617 countervailing duty is a cost, full stop. You can't offset it against anything [Source: EU anti-subsidy regulation and Commission guidance].

That asymmetry — recoverable VAT, non-recoverable CVD — is the biggest reason some importers still turn a profit on BYD but steer clear of SAIC/MG models. Pick your brand with the CVD table open.

If you want to run your own numbers rather than trust my arithmetic, plug your figures into our [landed cost calculator](/landed-cost-calculator/) and read the [landed cost methodology](/landed-cost-methodology/) for the full derivation of every factor.

---

## Risk Checklist (Read Before You Wire Any Money)

I keep a running list of the ways imports go wrong. Here's what I actually see, in rough order of frequency:

1. **CoC refused by the manufacturer.** A Chinese brand that officially sells in the EU will often refuse to issue a Certificate of Conformity to a grey importer, because it cannibalizes their own distribution. Before you buy, confirm *in writing* that you can obtain the CoC. No CoC means single-vehicle approval, which adds weeks and cost [Source: Regulation (EU) 2018/858].

2. **Charge-port and spec mismatch.** China-spec GB/T inlet, kilometer-only speedometer, no rear fog lamp — these all appear on China-market trims and all need work before EU registration [Source: EU type-approval technical requirements]. Always import the EU-spec build.

3. **Range overstatement.** Advertising CLTC figures in the EU is a consumer-law exposure and a reputation killer. Convert to WLTP before you list anything [Source: EU consumer protection rules on misleading claims].

4. **CVD mis-memorization.** People remember "10% duty" and forget the CVD entirely. The 35.3% on SAIC/MG is the single largest line item on an MG import — bigger than the base duty and often bigger than freight [Source: European Commission Implementing Regulation (EU) 2024/2754].

5. **Supplier payment fraud.** Full upfront payment to an unverified exporter is the most common way to lose money outright. Staged payment, escrow or LC, and a verified export license are non-negotiable.

6. **Freight volatility.** Red Sea rerouting pushed RoRo rates up sharply at points in 2023–2025. Lock a rate before you commit the order, or factor in a buffer [Source: industry freight rate reporting, 2023–2025].

7. **CVD is a five-year bet.** The current CVD runs to 2029 and the EU can review rates up or down mid-term [Source: European Commission, October 2024]. A rate cut would improve your margin; a review that raises a cooperative producer's rate would do the opposite. Don't build a multi-year contract on the assumption rates stay frozen.

### Tax Essentials (Keep This Taped to Your Monitor)

- **Standard duty:** 10% on CIF value, paid at import, non-recoverable [Source: EU Common Customs Tariff].
- **CVD:** 7.8%–35.3% brand-specific, *adds* to duty before VAT, **non-recoverable** [Source: European Commission Implementing Regulation (EU) 2024/2754].
- **VAT:** 19%–23% depending on member state, charged on the *duty-inclusive* value, **recoverable** as input VAT if you're registered [Source: EU VAT Directive 2006/112/EC].
- **Input VAT timing:** you reclaim VAT on your next return, so there's a cash-flow gap between paying it at import and getting it back. Factor that float into your working capital.

---

## FAQ

### Q: Can I import a Chinese EV to the EU as a private individual?

A: Yes, but the math and the paperwork don't care whether you're a business or a person. You still owe duty, CVD, and VAT, and you'll almost certainly need single-vehicle approval (German §21 StVZO or a national equivalent) if the model isn't EU type-approved [Source: Regulation (EU) 2018/858 and §21 StVZO]. For a one-off personal car, total landed cost can approach 70–90% above the China price. It rarely makes financial sense below about $40,000–$50,000 of vehicle value.

### Q: What's the cheapest Chinese EV to import in 2026?

A: There's no single answer because the *CVD rate* swings the result more than the sticker price. A cheap SAIC-built MG carries a 35.3% CVD, while a slightly pricier BYD carries 17%, and a Shanghai Tesla just 7.8% [Source: European Commission Implementing Regulation (EU) 2024/2754]. In most scenarios, the *lowest-tariff* vehicle beats the *lowest-price* vehicle once you compound three layers of tax. Run it through the [landed cost calculator](/landed-cost-calculator/) rather than guessing.

### Q: Do I pay VAT on the countervailing duty too?

A: Yes. VAT is charged on the customs value *plus* standard duty *plus* CVD. So you effectively pay tax on the duties themselves [Source: EU VAT Directive 2006/112/EC and national customs codes]. It's why the compounding is so punishing — and why the recoverable-VAT point matters so much for registered importers.

### Q: Is the countervailing duty the same for every Chinese brand?

A: No. BYD pays 17%, Geely 18.8%, SAIC 35.3%, other cooperating producers about 20.8%, non-cooperating companies about 35.3%, and Tesla Shanghai 7.8% [Source: European Commission Implementing Regulation (EU) 2024/2754]. Brand choice is a tax decision, not just a product decision.

### Q: How long does the CVD last?

A: Five years, from 31 October 2024. The EU can review the rates during that window, so they can move — in theory up or down [Source: European Commission, October 2024].

### Q: Which is more accurate, WLTP or CLTC?

A: WLTP is the closer-to-real-world figure and the standard you must quote in the EU. CLTC figures run roughly 15–30% higher for the same car [Source: independent EV range comparisons, 2023–2025]. If a Chinese listing says 700 km, expect ~550–600 km on WLTP and less on the highway.

### Q: Can I drive a China-spec EV in Europe with a charge adapter?

A: Technically you can make AC charging work with a GB/T-to-Type 2 adapter, but GB/T-to-CCS2 DC fast-charging adapters are large, expensive, and not universally dependable [Source: GB/T 20234 / IEC 62196 standards]. For any commercial or fleet use, import the EU-spec CCS2/Type 2 version instead.

---

## Key Takeaways

1. **The tariff is three *compounded* layers, not three added taxes.** 10% duty → CVD (7.8%–35.3%) on top → VAT (19%–23%) on the whole stack. The true multiplier on CIF value is (1.10) × (1+CVD) × (1+VAT), which is always larger than the naive sum [Source: European Commission Implementing Regulation (EU) 2024/2754 and EU VAT Directive 2006/112/EC].

2. **A $24,690 BYD Seal Premium becomes ~$44,413 landed in Germany — a 79.9% bump** — before dealer margin and before any modifications [Source: worked calculation above, European Commission duty rates].

3. **Brand choice is a tax decision.** The spread between a 7.8% (Tesla Shanghai) and a 35.3% (SAIC/MG) CVD moves your landed cost by thousands, because the CVD also inflates the VAT base [Source: European Commission Implementing Regulation (EU) 2024/2754].

4. **VAT is recoverable; CVD is not.** A VAT-registered importer reclaims the VAT, but the countervailing duty is a permanent cost. That single asymmetry decides which brands are worth importing [Source: EU VAT Directive 2006/112/EC; EU anti-subsidy regulation].

5. **Sequence matters.** CoC → freight → clearance → duties → certification → registration. Every failed import I've seen skipped the CoC or the charging/spec check early and paid for it in the certification step [Source: Regulation (EU) 2018/858 and §21 StVZO].

6. **Import the EU-spec build, quote WLTP, plan for compounding.** Do those three things and you avoid the charging, range, and under-budgeting traps that kill most first imports.

---

*Wei Wang is a content editor at MCM (广州邦禾检测技术有限公司), where he works with distributors and fleet buyers importing Chinese EVs into European markets. This guide reflects 2025–2026 duty rates and fee estimates; confirm current figures with your customs broker and forwarder before committing funds.*
