---
title: "CCS2 vs GB/T: The Charging Compatibility Cost of a Chinese EV"
description: "China's EVs charge on GB/T, Europe on CCS2. A China-market car won't plug into a European fast charger without an adapter or a port conversion — here's what that actually costs and what to check first."
author: "Wei Wang"
publishedDate: "2026-09-06"
draft: false
tags: [charging, ccs2, gbt, compliance, ev-import, adaptation]
---

## TL;DR

China and Europe use **different DC fast-charging standards**, and this is one of the most common and most expensive surprises in a Chinese EV import. China's market runs on **GB/T**, Europe on **CCS2**. A car built for the Chinese domestic market has a GB/T charging inlet that **will not plug into a European CCS2 fast charger** — and on the AC side, the connector and signaling differ too.

There are two real fixes: source the **export version** of the car (which ships with CCS2), or adapt a China-market car (an adapter for AC, and — for DC fast charging — a port conversion that can run into the thousands and may not be practical on every model). The cheapest fix is the one you make *before* you buy: **check the charging inlet standard on the exact vehicle.**

## Key statistics

- **China DC fast charging:** GB/T (a China-specific standard)
- **Europe DC fast charging:** CCS2 (Combined Charging System, Type 2)
- **Europe AC charging:** Type 2 (Mennekes)
- **The rule:** a GB/T car needs an adapter (AC) or a conversion (DC fast) to charge in Europe
- **The cheapest fix:** buy the export version, which ships with CCS2

## The two standards, side by side

| | China | Europe |
|---|---|---|
| AC charging | GB/T AC | Type 2 (Mennekes) |
| DC fast charging | GB/T DC | CCS2 |

The connector shapes and the communication protocols are different on both the AC and DC sides. This isn't a "voltage is different" problem — it's a "the plug physically doesn't fit and the car doesn't speak the charger's protocol" problem.

## What this means for a China-market import

If you import a China-market EV as-is:

- **AC charging** at home or a public AC point: needs a **GB/T-to-Type 2 adapter**. This is the manageable part — adapters exist and cost a few hundred dollars.
- **DC fast charging** on a CCS2 network: the hard part. A simple adapter is generally not viable for GB/T-to-CCS2 DC because of the protocol mismatch; you typically need a **charging-port conversion**, which is invasive, model-dependent, and can cost thousands — when it's possible at all.

The practical upshot: a China-market EV can usually be made to charge slowly (AC) without much trouble, but making it fast-charge on Europe's CCS2 network is the expensive, uncertain step.

## The fix: buy the export version

The cleanest solution is to buy the vehicle in its **export specification**. Most Chinese brands produce export variants with CCS2 for Europe, and the same model sold into the Chinese domestic market is simply the wrong build for Europe. This is a *spec* difference, not a retrofit you should assume you can fix later.

This is exactly why our catalog's [landed-cost methodology](/docs/landed-cost-methodology/) includes a certification line item — and why you should treat "which charging inlet does this exact car have?" as a deal-breaker question, not a footnote.

## What buyers should ask before importing

1. **"Which charging inlet does this exact vehicle have?"** — GB/T or CCS2? Get a photo of the port, not the spec sheet.
2. **"Is this the export version?"** — if it's a China-domestic build, assume you'll need adaptation.
3. **"What's the AC charging path, and is an adapter enough?"** — AC is usually solvable with a GB/T-to-Type 2 adapter.
4. **"Can it DC fast-charge on CCS2, and what does the conversion cost?"** — if the buyer needs road-trip charging, this is the make-or-break question.
5. **"Does the car's onboard charger support EU voltages?"** — confirm grid/charger compatibility beyond just the connector shape.

## Frequently asked questions

**Can I charge a Chinese EV in Europe with an adapter?**
For AC (slow) charging, generally yes — a GB/T-to-Type 2 adapter handles it. For DC fast charging on CCS2, an adapter is usually not enough; you need a port conversion.

**What's the difference between GB/T and CCS2?**
They're different connector and communication standards. GB/T is China's; CCS2 is Europe's. A GB/T port doesn't fit or talk to a CCS2 charger.

**Is a port conversion expensive?**
It can run into the thousands and isn't possible on every model, which is why the export (CCS2) version is the right buy for Europe.

**Does the UK use CCS2?**
Yes — the UK uses CCS2 for DC fast charging and Type 2 for AC, same as the EU.


## Related reading

- [WVTA vs Single-Vehicle Approval](/blog/wvta-vs-single-vehicle-approval/)
- [LHD vs RHD Markets](/blog/lhd-vs-rhd-markets/)
- [Why the Sticker Price Is Never the Landed Price](/blog/sticker-vs-landed-price/)

## Sources

- GB/T (China) and CCS2 / Type 2 (Europe) charging standards
- EV Hub landed-cost methodology — certification and adaptation line items
