import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
import { siteConfig } from '@/config';

/**
 * /vehicles/[slug].md — clean Markdown variant of each vehicle page.
 *
 * Generated at build time from the SAME data layer the HTML page renders
 * (the `vehicles` content collection frontmatter), with no navigation,
 * footer, or JavaScript. Every value is sourced verbatim from the record;
 * nothing is fabricated.
 */

/** YAML-safe scalar (JSON strings are valid YAML scalars). */
const yaml = (v: unknown): string => JSON.stringify(v ?? '');

/** Escape a value for use inside a Markdown table cell. */
const cell = (v: unknown): string =>
  String(v ?? '').replace(/\r?\n/g, ' ').replace(/\|/g, '\\|').trim();

/** Format a decimal rate (0.17) as a percentage string. */
const pct = (r: unknown): string =>
  typeof r === 'number' ? `${(r * 100).toLocaleString('en-US')}%` : '—';

/** Format a number as a rounded USD string. */
const usd = (n: unknown): string =>
  typeof n === 'number' ? `$${Math.round(n).toLocaleString('en-US')}` : '—';

export async function getStaticPaths() {
  const vehicles = await getCollection('vehicles');
  return vehicles.map((v) => ({ params: { slug: v.data.slug } }));
}

export const GET: APIRoute = async ({ params }) => {
  const vehicles = await getCollection('vehicles');
  const vehicle = vehicles.find((v) => v.data.slug === params.slug);
  if (!vehicle) {
    return new Response('Not found', { status: 404 });
  }
  const data = vehicle.data;
  const canonical = `${siteConfig.url}/vehicles/${data.slug}/`;

  // Key specifications — mirrors src/pages/vehicles/[slug].astro (same labels
  // and same null handling), so the .md output is consistent with the HTML page.
  const specs: { label: string; value: string | null }[] = [
    { label: 'Brand', value: data.brand.toUpperCase() },
    { label: 'Body type', value: data.type },
    { label: 'Powertrain', value: data.powertrain },
    { label: 'Price (ex-factory China)', value: `$${data.price_usd.toLocaleString('en-US')} ${data.currency || 'USD'}` },
    { label: 'Price basis', value: data.price_type || 'China ex-factory price (MSRP)' },
    { label: 'Range (CLTC)', value: data.range_cltc_km ? `${data.range_cltc_km} km` : null },
    { label: 'Battery', value: data.battery_kwh ? `${data.battery_kwh} kWh` : null },
    { label: 'Motor power', value: data.motor_power_kw ? `${data.motor_power_kw} kW` : null },
    { label: 'Torque', value: data.torque_nm ? `${data.torque_nm} Nm` : null },
    { label: '0-100 km/h', value: data.accel_0_100_s ? `${data.accel_0_100_s} s` : null },
    { label: 'Top speed', value: data.top_speed_kmh ? `${data.top_speed_kmh} km/h` : null },
    { label: 'Length', value: data.length_mm ? `${data.length_mm} mm` : null },
    { label: 'Width', value: data.width_mm ? `${data.width_mm} mm` : null },
    { label: 'Height', value: data.height_mm ? `${data.height_mm} mm` : null },
    { label: 'Wheelbase', value: data.wheelbase_mm ? `${data.wheelbase_mm} mm` : null },
    { label: 'Curb weight', value: data.weight_kg ? `${data.weight_kg} kg` : null },
    { label: 'Efficiency', value: data.efficiency_kwh_100km ? `${data.efficiency_kwh_100km} kWh/100km` : null },
    { label: 'Fast charge', value: data.fast_charge || null },
  ].filter((s) => s.value);

  // Per-market landed cost (stored values only: rates, total, premium).
  const markets = (data.landed_cost_markets || []).filter(
    (m) => m && typeof m.total_landed_usd === 'number',
  );

  // Itemized breakdown for the primary market (stored values only).
  const lc = data.landed_cost || {};
  const breakdown = lc.breakdown || {};

  const out: string[] = [];

  out.push('---');
  out.push(`title: ${yaml(data.title)}`);
  out.push(`description: ${yaml(data.description)}`);
  out.push(`brand: ${yaml(data.brand.toUpperCase())}`);
  out.push(`type: ${yaml(data.type)}`);
  out.push(`powertrain: ${yaml(data.powertrain)}`);
  out.push(`canonical: ${yaml(canonical)}`);
  if (data.data_updated) out.push(`updated: ${yaml(data.data_updated)}`);
  out.push('---');
  out.push('');

  out.push(`# ${data.title}`);
  out.push('');
  out.push(data.description || '');
  out.push('');

  out.push('## Specifications');
  out.push('');
  out.push('| Spec | Value |');
  out.push('| --- | --- |');
  for (const s of specs) out.push(`| ${cell(s.label)} | ${cell(s.value)} |`);
  out.push('');

  if (markets.length > 0) {
    out.push('## Landed Cost by Market');
    out.push('');
    out.push('| Market | Region | Standard duty | Countervailing duty | VAT | Landed total (USD) | Premium |');
    out.push('| --- | --- | --- | --- | --- | --- | --- |');
    for (const m of markets) {
      out.push(
        `| ${cell(m.market)} | ${cell(m.region)} | ${cell(pct(m.standard_duty_rate))} | ${cell(pct(m.countervailing_duty_rate))} | ${cell(pct(m.vat_rate))} | ${cell(usd(m.total_landed_usd))} | ${cell(m.premium_pct != null ? `+${m.premium_pct}%` : '—')} |`,
      );
    }
    out.push('');
  }

  if (typeof lc.total_landed_usd === 'number' || Object.keys(breakdown).length > 0) {
    const marketName = lc.market || 'Germany';
    out.push(`## Landed Cost Breakdown — ${marketName}`);
    out.push('');
    out.push('| Cost item | Amount (USD) |');
    out.push('| --- | --- |');
    if (typeof data.price_usd === 'number') {
      out.push(`| Base price | ${cell(usd(data.price_usd))} |`);
    }
    const items: [string, unknown][] = [
      ['Standard import duty', breakdown.duty_cif_usd],
      ['Countervailing duty', breakdown.countervailing_duty_usd],
      ['VAT', breakdown.vat_usd],
      ['RoRo freight', breakdown.freight_roro_usd],
      ['Customs clearance', breakdown.customs_clearance_usd],
      ['Certification', breakdown.certification_usd],
      ['Registration', breakdown.registration_usd],
      ['Inland transport', breakdown.inland_transport_usd],
    ];
    for (const [label, val] of items) {
      if (typeof val === 'number') out.push(`| ${cell(label)} | ${cell(usd(val))} |`);
    }
    if (typeof lc.total_landed_usd === 'number') {
      out.push(`| **Total landed** | **${cell(usd(lc.total_landed_usd))}** |`);
    }
    out.push('');
  }

  out.push('## Sources & Last Updated');
  out.push('');
  if (data.data_source) out.push(`- Data source: ${data.data_source}`);
  if (data.data_updated) out.push(`- Last updated: ${data.data_updated}`);
  out.push(`- Confidence: ${data.confidence || 'Medium'}`);
  out.push(`- Status: ${data.data_reviewed ? 'Reviewed' : 'Pending review'}`);
  out.push('');
  out.push(`View the full HTML page: ${canonical}`);
  out.push('');

  return new Response(out.join('\n'), {
    headers: { 'Content-Type': 'text/markdown; charset=utf-8' },
  });
};
