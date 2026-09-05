---
title: "Introduction"
description: "What CNEVhub is, how the landed-cost methodology works, and how to use the vehicle database to compare Chinese EV import prices across markets."
section: "Getting Started"
order: 1
draft: false
---

# Introduction to CNEVhub

CNEVhub is a data platform for anyone importing Chinese electric vehicles into Europe, the Middle East, and Oceania. We exist because the sticker price you see in China is almost never the price you actually pay.

## The core problem we solve

A Chinese EV advertised at $14,000 can land in Germany at over $28,000 once you stack import duty, countervailing duty, VAT, ocean freight, certification, and registration. That gap — the difference between *factory price* and *landed cost* — is the single biggest surprise for first-time importers.

Most listings show only the FOB or factory price. CNEVhub itemizes the full cost stack so you can see, before you commit, exactly what a vehicle will cost to get legal and drivable in your target market.

## What's on the platform

- **Vehicle database** — 315+ Chinese EVs with full specifications, priced transparently, each with a multi-market landed-cost breakdown.
- **Brand directory** — 58 brands, their parent manufacturers, founding details, and export-ready lineups.
- **Landed-cost calculator** — pick a vehicle and destination, get an itemized cost breakdown across 7 key export markets.
- **Methodology** — the exact formula, tariff schedules, and assumptions behind every number on the site.

## What "landed cost" means here

Landed cost is the total price to import a vehicle to a specific country, *before* dealer margin or retail markup. Our formula is:

```
landed_price = base_price × (1 + standard_duty) × (1 + countervailing_duty) × (1 + VAT)
               + RoRo freight + customs clearance + certification + registration + inland transport
```

Duties compound in this order because that's how customs valuations cascade in practice: standard duty on the CIF value, countervailing duty on top of that, then VAT last on the duty-inclusive total.

## A note on data quality

Every tariff rate, tax rate, and freight benchmark is sourced from public authorities (EU Official Journal, national tax authorities) and industry benchmarks. Rates are refreshed when they change, and each figure carries a data date. These are B2B import estimates, not retail quotes — actual costs vary with trim, port of entry, volume, currency, and homologation route.

## Who this is for

B2B fleet buyers, distributors, dealers, and experienced private importers evaluating the real economics of bringing Chinese EVs into export markets. If you're comparing vehicles, start with the [vehicle database](/vehicles/), then run the numbers in the [calculator](/landed-cost-calculator/).
