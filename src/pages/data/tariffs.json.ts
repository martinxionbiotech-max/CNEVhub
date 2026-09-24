import tariffs from '../../data/tariffs.json';

/**
 * /data/tariffs.json — machine-readable public export (§16).
 * Tariff / VAT / CVD reference data, re-exported from the single source of
 * truth (src/data/tariffs.json). All fields here are public reference data.
 */
export function GET() {
  return new Response(
    JSON.stringify(
      {
        name: 'Chinese EV Export Database — Tariff Reference',
        description:
          'Standard import duty, countervailing duty (EU BEV, producer-specific), VAT/GST rates and fixed-cost benchmarks used by the EV Hub landed-cost model.',
        license: 'CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)',
        updated: tariffs.updated,
        source: tariffs.source,
        cvd_scope: tariffs.cvd_scope,
        markets: tariffs.markets,
        brand_cvd: tariffs.brand_cvd,
        fixed_costs: tariffs.fixed_costs,
        cvd_meta: tariffs.cvd_meta,
      },
      null,
      2,
    ),
    {
      headers: { 'Content-Type': 'application/json; charset=utf-8' },
    },
  );
}
