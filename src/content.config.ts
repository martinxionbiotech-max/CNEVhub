import { defineCollection } from 'astro:content';
import { z } from 'astro/zod';
import { glob } from 'astro/loaders';

const blog = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    publishedDate: z.coerce.date(),
    author: z.string(),
    image: z.string().optional(),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
  }),
});

const docs = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/docs' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    order: z.number().default(0),
    section: z.string(),
    draft: z.boolean().default(false),
  }),
});

const vehicles = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/vehicles' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    slug: z.string(),
    brand: z.string(),
    type: z.string(),
    powertrain: z.string(),
    price_usd: z.number(),
    price_type: z.string().default('China ex-factory price (MSRP)'),
    currency: z.string().default('USD'),
    range_cltc_km: z.number().nullable().optional(),
    range_long_km: z.number().nullable().optional(),
    range_wltp_km: z.number().nullable().optional(),
    range_epa_km: z.number().nullable().optional(),
    range_standard_primary: z.enum(['CLTC', 'WLTP', 'EPA']).nullable().optional(),
    battery_kwh: z.number().nullable().optional(),
    motor_power_kw: z.number().nullable().optional(),
    torque_nm: z.number().nullable().optional(),
    accel_0_100_s: z.number().nullable().optional(),
    top_speed_kmh: z.number().nullable().optional(),
    length_mm: z.number().nullable().optional(),
    width_mm: z.number().nullable().optional(),
    height_mm: z.number().nullable().optional(),
    wheelbase_mm: z.number().nullable().optional(),
    weight_kg: z.number().nullable().optional(),
    efficiency_kwh_100km: z.number().nullable().optional(),
    fast_charge: z.string().nullable().default(null),
    landed_cost: z.any().optional(),
    landed_cost_markets: z.any().default([]),
    image: z.string().optional(),
    image_credit: z.string().optional(),
    image_source: z.string().optional(),
    publishedDate: z.coerce.date(),
    author: z.string(),
    tags: z.array(z.string()).default([]),
    data_tier: z.number().optional(),
    data_source: z.string().optional(),
    data_updated: z.string().optional(),
    data_reviewed: z.boolean().optional(),
    confidence: z.string().optional(),
    family: z.string().optional(),
    spec_source_type: z
      .enum(['official_spec', 'manufacturer_claim', 'independent_test', 'estimate', 'unverified'])
      .optional(),
    // ── EVHub Top deep-profile fields (five-section template; all optional) ──
    // ① Entity Snapshot
    trim: z.string().optional(),
    fob_price_usd_min: z.number().nullable().optional(),
    fob_price_usd_max: z.number().nullable().optional(),
    // ② Powertrain & Architecture
    battery_type: z.string().optional(),
    drive_type: z.string().optional(),
    motor_type: z.string().optional(),
    motor_model: z.string().optional(),
    total_power_kw: z.number().nullable().optional(),
    battery_thermal: z.string().optional(),
    heat_pump: z.string().optional(),
    suspension_front: z.string().optional(),
    suspension_rear: z.string().optional(),
    brakes: z.string().optional(),
    drag_coefficient: z.number().nullable().optional(),
    // ③ Dimensions & Logistics
    gross_weight_kg: z.number().nullable().optional(),
    ground_clearance_mm: z.number().nullable().optional(),
    trunk_l: z.number().nullable().optional(),
    // ④ Market Compliance & Export Profile
    charging_interface: z.string().optional(),
    charging_adapter: z.string().optional(),
    infotainment_language: z.string().optional(),
    network_bands: z.string().optional(),
    certification_notes: z.string().optional(),
    hs_code: z.string().optional(),
  }),
});

const brands = defineCollection({
  loader: glob({ pattern: "**/*.{md,mdx}", base: "./src/content/brands" }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    brand_name: z.string(),
    established: z.string(),
    parent_manufacturer: z.string(),
    parent_location: z.string(),
    parent_founded: z.string(),
    website: z.string(),
    model_count: z.number(),
    publishedDate: z.coerce.date(),
    tags: z.array(z.string()).default([]),
  }),
});

export const collections = { blog, docs, vehicles, brands };
