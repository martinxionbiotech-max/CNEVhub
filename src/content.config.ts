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

const changelog = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/changelog' }),
  schema: z.object({
    version: z.string(),
    date: z.coerce.date(),
    title: z.string(),
    type: z.enum(['major', 'minor', 'patch']),
    draft: z.boolean().default(false),
  }),
});

const testimonials = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/testimonials' }),
  schema: z.object({
    quote: z.string(),
    author: z.string(),
    role: z.string(),
    company: z.string(),
    avatar: z.string().optional(),
    featured: z.boolean().default(false),
    order: z.number().default(0),
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
    currency: z.string().default('USD'),
    range_cltc_km: z.number().nullable().optional(),
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
    fast_charge: z.string().default('-'),
    landed_cost: z.any().optional(),
    image: z.string().optional(),
    publishedDate: z.coerce.date(),
    author: z.string(),
    tags: z.array(z.string()).default([]),
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

export const collections = { blog, docs, changelog, testimonials, vehicles, brands };
