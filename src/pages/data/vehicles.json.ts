import { getCollection } from 'astro:content';
import { tierFromDataTier } from '@/lib/spec-tier';

/**
 * /data/vehicles.json — machine-readable public export (§16).
 * Static JSON endpoint generated at build time from the vehicles content
 * collection. Only public fields are exposed — no internal notes.
 *
 * Consumers: researchers, LLMs, AI agents, spreadsheet imports.
 *
 * P3 (data quality): the record shape now mirrors the full content
 * frontmatter spec + provenance subset (12 → 33 fields). Every added field
 * is a *transparent pass-through* of data already present in the content
 * collection — no value is fabricated or computed. Absent fields are `null`.
 */
export async function GET() {
  const vehicles = await getCollection('vehicles');
  vehicles.sort((a, b) => a.data.slug.localeCompare(b.data.slug));

  const rows = vehicles.map((v) => {
    const d = v.data;
    return {
      // Identity
      slug: d.slug,
      title: d.title,
      description: d.description,
      brand: d.brand,
      type: d.type,
      powertrain: d.powertrain,
      family: d.family ?? null,

      // Pricing
      price_usd: d.price_usd,
      price_type: d.price_type ?? null,
      currency: d.currency ?? 'USD',

      // Range & battery (CLTC / WLTP / EPA kept as separate fields)
      range_cltc_km: d.range_cltc_km ?? null,
      range_long_km: d.range_long_km ?? null,
      range_wltp_km: d.range_wltp_km ?? null,
      range_epa_km: d.range_epa_km ?? null,
      range_standard_primary: d.range_standard_primary ?? (d.range_cltc_km != null ? 'CLTC' : null),
      battery_kwh: d.battery_kwh ?? null,

      // Performance & dimensions
      motor_power_kw: d.motor_power_kw ?? null,
      torque_nm: d.torque_nm ?? null,
      accel_0_100_s: d.accel_0_100_s ?? null,
      top_speed_kmh: d.top_speed_kmh ?? null,
      length_mm: d.length_mm ?? null,
      width_mm: d.width_mm ?? null,
      height_mm: d.height_mm ?? null,
      wheelbase_mm: d.wheelbase_mm ?? null,
      weight_kg: d.weight_kg ?? null,
      efficiency_kwh_100km: d.efficiency_kwh_100km ?? null,
      fast_charge: d.fast_charge ?? null,

      // Provenance (single source of truth)
      data_tier: d.data_tier ?? null,
      spec_source_type: tierFromDataTier(d.data_tier) ?? d.spec_source_type ?? null,
      data_source: d.data_source ?? null,
      data_updated: d.data_updated ?? null,
      data_reviewed: d.data_reviewed ?? null,
      confidence: d.confidence ?? null,

      // Media
      image: d.image ?? null,
      image_credit: d.image_credit ?? null,
      image_source: d.image_source ?? null,

      // Landed cost (per export market)
      landed_cost_markets: (d.landed_cost_markets ?? []).map((m) => ({
        market: m.market,
        market_key: m.market_key,
        region: m.region,
        total_landed_usd: m.total_landed_usd,
        premium_pct: m.premium_pct,
      })),
    };
  });

  return new Response(
    JSON.stringify(
      {
        name: 'Chinese EV Export Database — Vehicles',
        description:
          'Normalized Chinese EV vehicle records with China ex-factory price and estimated landed cost per export market (indicative B2B estimates, not retail quotes).',
        license: 'CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)',
        generated_at: new Date().toISOString(),
        records: rows.length,
        vehicles: rows,
      },
      null,
      2,
    ),
    {
      headers: { 'Content-Type': 'application/json; charset=utf-8' },
    },
  );
}
