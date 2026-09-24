import { getCollection } from 'astro:content';

/**
 * /data/vehicles.json — machine-readable public export (§16).
 * Static JSON endpoint generated at build time from the vehicles content
 * collection. Only public fields are exposed — no internal notes.
 *
 * Consumers: researchers, LLMs, AI agents, spreadsheet imports.
 */
export async function GET() {
  const vehicles = await getCollection('vehicles');
  vehicles.sort((a, b) => a.data.slug.localeCompare(b.data.slug));

  const rows = vehicles.map((v) => {
    const d = v.data;
    return {
      slug: d.slug,
      title: d.title,
      brand: d.brand,
      type: d.type,
      powertrain: d.powertrain,
      price_usd: d.price_usd,
      currency: d.currency ?? 'USD',
      range_cltc_km: d.range_cltc_km ?? null,
      battery_kwh: d.battery_kwh ?? null,
      motor_power_kw: d.motor_power_kw ?? null,
      data_updated: d.data_updated ?? null,
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
