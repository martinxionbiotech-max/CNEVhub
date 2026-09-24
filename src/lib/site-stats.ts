/**
 * site-stats.ts — Single Source of Truth for all site-wide counts (P0-1).
 *
 * Every public number (vehicle count, brand count, per-brand model count,
 * powertrain split) is derived at build time from the content collections.
 * Nothing is hardcoded in templates.
 */
import { getCollection } from 'astro:content';

export interface SiteStats {
  vehicles: number;
  brands: number;
  bevCount: number;
  phevCount: number;
  erevCount: number;
  otherPowertrainCount: number;
  markets: number;
  publishedArticles: number;
}

let cached: SiteStats | null = null;
let cachedModelCounts: Map<string, number> | null = null;

export async function getSiteStats(): Promise<SiteStats> {
  if (cached) return cached;
  const vehicles = await getCollection('vehicles');
  const brands = await getCollection('brands');
  const blog = await getCollection('blog');

  const powertrain = (p: string) => p.toUpperCase();
  let bevCount = 0;
  let phevCount = 0;
  let erevCount = 0;
  let otherPowertrainCount = 0;
  const marketSet = new Set<string>();
  for (const v of vehicles) {
    const p = powertrain(v.data.powertrain ?? '');
    if (p === 'BEV') bevCount++;
    else if (p === 'PHEV') phevCount++;
    else if (p === 'EREV' || p === 'REEV') erevCount++;
    else otherPowertrainCount++;
    for (const m of v.data.landed_cost_markets ?? []) {
      if (m?.market_key) marketSet.add(m.market_key);
    }
  }

  cached = {
    vehicles: vehicles.length,
    brands: brands.length,
    bevCount,
    phevCount,
    erevCount,
    otherPowertrainCount,
    markets: marketSet.size,
    publishedArticles: blog.filter((b) => !b.data.draft).length,
  };
  return cached;
}

/** Per-brand active model count, derived from the vehicle records themselves. */
export async function getModelCountByBrand(): Promise<Map<string, number>> {
  if (cachedModelCounts) return cachedModelCounts;
  const vehicles = await getCollection('vehicles');
  const map = new Map<string, number>();
  for (const v of vehicles) {
    const brand = v.data.brand;
    map.set(brand, (map.get(brand) ?? 0) + 1);
  }
  cachedModelCounts = map;
  return map;
}

/** All brands present in vehicle records (authoritative brand universe). */
export async function getActiveBrandSlugs(): Promise<string[]> {
  const map = await getModelCountByBrand();
  return Array.from(map.keys()).sort();
}
