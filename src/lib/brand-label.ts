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

type VehicleLike = {
  title?: string;
  brand?: string;
  type?: string;
  powertrain?: string;
  image_credit?: string;
};

/** 标题已含品牌时不再重复品牌（避免 "Bestune Pony — Bestune Hatchback"） */
function descriptor(v: VehicleLike, map: Map<string, string>): string {
  const label = brandLabel(map, v.brand);
  const title = (v.title || '').trim();
  const titleHasBrand =
    !!label && title.toLowerCase().startsWith(label.toLowerCase());
  const spec = [v.type, v.powertrain ? `(${v.powertrain})` : '']
    .filter(Boolean)
    .join(' ')
    .trim();
  return [titleHasBrand ? '' : label, spec].filter(Boolean).join(' ');
}

/** 车型主图 alt：实拍为「车型 — 品牌 类型 (动力) 外观实拍」，自研插图单独说明 */
export function vehicleAlt(v: VehicleLike, map: Map<string, string>): string {
  const title = (v.title || '').trim();
  const desc = descriptor(v, map);
  if (/EV Hub original/i.test(v.image_credit || '')) {
    // 插图用扁平规格写法，避免出现 "(Sedan (BEV))" 这种嵌套括号
    const plain = [v.type, v.powertrain].filter(Boolean).join(' ');
    return `Technical illustration of the ${title}${plain ? ` (${plain})` : ''} — no freely licensed photograph of this vehicle is available`;
  }
  return `${title} — ${desc} exterior view`.replace(/\s+/g, ' ').trim();
}

/** 列表/缩略图 alt：更短，不重复品牌 */
export function vehicleThumbAlt(v: VehicleLike, map: Map<string, string>): string {
  return `${(v.title || '').trim()} — ${descriptor(v, map)}`.replace(/\s+/g, ' ').trim();
}
