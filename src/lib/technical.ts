/**
 * technical.ts — Technology reference data layer (single source of truth).
 *
 * Loads the 137-entity technical-master.json and exposes typed accessors for the
 * /technology/ hub and /technology/[entity]/ pages. Every entity is rendered
 * verbatim from this file; nothing is fabricated at the template layer.
 */
import technicalMaster from '@/data/technical-master.json';

export interface TechnicalEntity {
  id: string;
  name: string;
  name_zh: string;
  category: string;
  definition: string;
  source: string;
  related_vehicles?: string[];
}

export interface TechCategoryMeta {
  label: string;
  labelZh: string;
  description: string;
  order: number;
}

/** Category metadata + ordering for the hub index. */
export const TECH_CATEGORIES: Record<string, TechCategoryMeta> = {
  battery: {
    label: 'Battery & Chemistry',
    labelZh: '电池',
    description: 'Cell chemistries, pack structures, and battery systems.',
    order: 1,
  },
  charging: {
    label: 'Charging & Standards',
    labelZh: '充电',
    description: 'Connectors, charging standards, and infrastructure protocols.',
    order: 2,
  },
  drivetrain: {
    label: 'Drivetrain & Motors',
    labelZh: '动力总成',
    description: 'Motors, e-axles, and hybrid / range-extender architectures.',
    order: 3,
  },
  thermal: {
    label: 'Thermal Management',
    labelZh: '热管理',
    description: 'Battery and cabin thermal systems.',
    order: 4,
  },
  range: {
    label: 'Range & Efficiency',
    labelZh: '续航',
    description: 'Range standards and energy-efficiency concepts.',
    order: 5,
  },
  'body-safety': {
    label: 'Body & Safety',
    labelZh: '车身安全',
    description: 'Body structure, materials, and safety standards.',
    order: 6,
  },
};

const raw = technicalMaster as unknown as { entities: TechnicalEntity[] };
export const technicalEntities: TechnicalEntity[] = raw.entities ?? [];

/** All categories present in the data, in hub display order. */
export const orderedCategories = Object.entries(TECH_CATEGORIES)
  .filter(([key]) => technicalEntities.some((e) => e.category === key))
  .sort((a, b) => a[1].order - b[1].order)
  .map(([key]) => key);

export function getEntityById(id: string): TechnicalEntity | undefined {
  return technicalEntities.find((e) => e.id === id);
}

export function getEntitiesByCategory(category: string): TechnicalEntity[] {
  return technicalEntities.filter((e) => e.category === category);
}

/** Reverse lookup: all tech entities that reference a given vehicle slug. */
export function getEntitiesByVehicle(slug: string): TechnicalEntity[] {
  return technicalEntities.filter((e) => (e.related_vehicles ?? []).includes(slug));
}

/** Extract the first http(s) URL from a source string ("Label — https://…"). */
export function sourceUrl(source: string): string | undefined {
  const m = source?.match(/https?:\/\/[^\s)]+/);
  return m ? m[0].replace(/[.,;]+$/, '') : undefined;
}
