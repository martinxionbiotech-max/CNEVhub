import { getCollection } from 'astro:content';
import { getModelCountByBrand } from '@/lib/site-stats';

/**
 * /data/brands.json — machine-readable public export (§16).
 * Brand registry with dynamic per-brand model counts derived from the
 * vehicle records themselves (single source of truth).
 */
export async function GET() {
  const brands = await getCollection('brands');
  const modelCounts = await getModelCountByBrand();

  const rows = brands
    .map((b) => {
      const d = b.data;
      const slug = b.id.replace(/\.mdx?$/, '');
      return {
        slug,
        name: d.brand_name,
        parent: d.parent_manufacturer,
        parent_location: d.parent_location,
        established: d.established,
        website: d.website,
        model_count: modelCounts.get(slug) ?? d.model_count ?? 0,
      };
    })
    .sort((a, b) => a.slug.localeCompare(b.slug));

  return new Response(
    JSON.stringify(
      {
        name: 'Chinese EV Export Database — Brands',
        description:
          'Brand registry for the Chinese EV export database. model_count is derived at build time from vehicle records.',
        license: 'CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)',
        generated_at: new Date().toISOString(),
        records: rows.length,
        brands: rows,
      },
      null,
      2,
    ),
    {
      headers: { 'Content-Type': 'application/json; charset=utf-8' },
    },
  );
}
