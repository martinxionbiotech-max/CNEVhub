import { getCollection } from 'astro:content';

/**
 * 品牌显示名映射：车辆 frontmatter 的 brand 字段是小写 slug（byd / aion / zeekr），
 * 直接用于 alt 会出现 "byd SUV" 这种写法。品牌集合的 title 形如
 * "BYD: Chinese EV Brand Profile & Export Data"，取冒号前部分即为官方写法（BYD / AION / Zeekr）。
 */
let cache: Promise<Map<string, string>> | null = null;

export function brandLabelMap(): Promise<Map<string, string>> {
  if (!cache) {
    cache = getCollection('brands').then(
      (brands) => new Map(brands.map((b) => [b.id, (b.data.title || b.id).split(':')[0].trim()]))
    );
  }
  return cache;
}

/** 取品牌显示名，回退到原始 slug */
export function brandLabel(map: Map<string, string>, slug?: string): string {
  if (!slug) return '';
  return map.get(slug) || slug;
}
