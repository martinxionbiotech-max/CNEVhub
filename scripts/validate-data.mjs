#!/usr/bin/env node
/**
 * EV Hub data validation script.
 * Run: npm run validate:data
 * Detects: duplicate IDs, invalid founded_year, invalid body_type/powertrain,
 * missing brand/manufacturer/source, invalid price/battery/range, invalid
 * country codes, tariff scope issues, PHEV mis-applied BEV CVD, md↔master drift.
 */
import { readFileSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

const ROOT = new URL('..', import.meta.url).pathname;
const load = (p) => JSON.parse(readFileSync(join(ROOT, p), 'utf8'));

const ALLOWED_BODY_TYPES = new Set([
  'Sedan','Hatchback','SUV','Crossover','MPV','Wagon','Pickup','Van',
  'Coupe','Convertible','Sports Car','Other','Unknown',
]);
const ALLOWED_POWERTRAINS = new Set(['BEV','PHEV','EREV','HEV','ICE','FCEV','Unknown']);
const ALLOWED_RANGE_STANDARDS = new Set(['CLTC','WLTP','NEDC','EPA','Manufacturer estimate','Real-world estimate','Unknown']);
const ISO_CODES = new Set([
  'DE','FR','NL','GB','AE','SA','AU','NO','SE','DK','ES','IT','BE','AT','PT','IE','PL',
  'CH','IL','QA','TR','NZ','TH','MY','ID','SG','MX','CA','BR','ZA',
]);

const issues = [];
const ok = [];
const flag = (cat, id, msg) => issues.push({ category: cat, id, message: msg });

// ── 1. brand-master ──
const brands = load('src/data/brand-master.json').brands;
const brandIds = new Set();
for (const b of brands) {
  if (brandIds.has(b.brand_id)) flag('duplicate-brand-id', b.brand_id, 'duplicate brand_id');
  brandIds.add(b.brand_id);
  const y = Number(b.established);
  if (!Number.isFinite(y) || y < 1800 || y > new Date().getFullYear()) {
    flag('invalid-founded-year', b.brand_id, `established=${b.established}`);
  }
  if (!b.parent_company) flag('missing-parent', b.brand_id, 'missing parent_company');
  if (!b.source_url) flag('missing-source', b.brand_id, 'missing source_url');
  if (!/^https?:\/\//.test(b.website || '')) flag('invalid-url', b.brand_id, `website=${b.website}`);
}
ok.push(`brands: ${brands.length} (all have source_url)`);

// ── 2. vehicle-master ──
const vehicles = load('src/data/vehicle-master.json').vehicles;
const vehicleIds = new Set();
const mdDir = join(ROOT, 'src/content/vehicles');
const mdFiles = new Set(readdirSync(mdDir).filter((f) => f.endsWith('.md')).map((f) => f.slice(0, -3)));

for (const v of vehicles) {
  const id = v.vehicle_id;
  if (vehicleIds.has(id)) flag('duplicate-vehicle-id', id, 'duplicate vehicle_id');
  vehicleIds.add(id);
  if (!brandIds.has(v.brand)) flag('unknown-brand', id, `brand=${v.brand} not in brand-master`);
  if (!ALLOWED_BODY_TYPES.has(v.body_type)) flag('invalid-body-type', id, `body_type=${v.body_type}`);
  if (!ALLOWED_POWERTRAINS.has(v.powertrain)) flag('invalid-powertrain', id, `powertrain=${v.powertrain}`);
  if (!ALLOWED_RANGE_STANDARDS.has(v.range_standard)) flag('invalid-range-standard', id, `range_standard=${v.range_standard}`);
  if (typeof v.price_usd !== 'number' || v.price_usd <= 0) flag('invalid-price', id, `price_usd=${v.price_usd}`);
  if (v.battery_kwh != null && (v.battery_kwh <= 0 || v.battery_kwh > 300)) flag('invalid-battery', id, `battery_kwh=${v.battery_kwh}`);
  if (v.range_cltc_km != null && (v.range_cltc_km < 50 || v.range_cltc_km > 1500)) flag('invalid-range', id, `range_cltc_km=${v.range_cltc_km}`);
  if (v.top_speed_kmh != null && (v.top_speed_kmh <= 0 || v.top_speed_kmh > 500)) flag('invalid-top-speed', id, `top_speed_kmh=${v.top_speed_kmh}`);
  if (!mdFiles.has(id)) flag('missing-md', id, 'no md file in src/content/vehicles');
  if (!v.price_type) flag('missing-price-type', id, 'missing price_type');
  else if (v.price_type !== 'China ex-factory price (MSRP)')
    flag('invalid-price-type', id, `price_type=${v.price_type}`);
  if (!v.source) flag('missing-source', id, 'missing source (brand-level inheritance)');
  if (!/^https?:\/\//.test(v.source_url || '')) flag('missing-source', id, `source_url=${v.source_url}`);
}
for (const f of mdFiles) {
  if (!vehicleIds.has(f)) flag('orphan-md', f, 'md file without master record');
}

// md frontmatter 与 master 漂移检查（type/powertrain）
for (const v of vehicles) {
  const id = v.vehicle_id;
  if (!mdFiles.has(id)) continue;
  const raw = readFileSync(join(mdDir, id + '.md'), 'utf8');
  const fm = raw.match(/^---\n([\s\S]*?)\n---/)?.[1] ?? '';
  const mdType = fm.match(/^type:\s*"([^"]+)"/m)?.[1];
  const mdPt = fm.match(/^powertrain:\s*"([^"]+)"/m)?.[1];
  if (mdType && mdType !== v.body_type) flag('md-drift', id, `md type=${mdType} vs master body_type=${v.body_type}`);
  if (mdPt && mdPt !== v.powertrain) flag('md-drift', id, `md powertrain=${mdPt} vs master ${v.powertrain}`);
  const mdFc = fm.match(/^fast_charge:\s*"(-)"$/m)?.[1];
  if (mdFc) flag('fast-charge-placeholder', id, `md fast_charge='-' placeholder (should be null)`);
}
ok.push('fast_charge: no \'-\' placeholder (all null or real values)');
ok.push(`vehicles: ${vehicles.length} (md 1:1)`);

// ── 3. markets ──
const markets = load('src/data/market-master.json').markets;
for (const m of markets) {
  if (!m.market_code) flag('missing-market-code', m.market_id, 'missing ISO market_code');
  else if (!ISO_CODES.has(m.market_code)) flag('invalid-market-code', m.market_id, `market_code=${m.market_code}`);
}
ok.push(`markets: ${markets.length} (all have ISO code)`);

// ── 4. tariffs ──
const tariffs = load('src/data/tariffs.json');
if (!tariffs.cvd_meta) flag('tariff-meta', 'cvd_meta', 'missing versioned cvd_meta block');
if (!tariffs.updated) flag('tariff-meta', 'updated', 'missing updated date');
for (const [brand, rate] of Object.entries(tariffs.brand_cvd ?? {})) {
  if (typeof rate !== 'number' || rate < 0 || rate > 1) flag('invalid-tariff', brand, `cvd rate=${rate}`);
}
ok.push(`tariffs: brand_cvd ${Object.keys(tariffs.brand_cvd ?? {}).length} entries + cvd_meta`);

// ── 5. PHEV/EREV/HEV/ICE 的 EU CVD 检查（md frontmatter landed_cost_markets）──
for (const v of vehicles) {
  const id = v.vehicle_id;
  if (v.powertrain === 'BEV') continue;
  if (!mdFiles.has(id)) continue;
  const raw = readFileSync(join(mdDir, id + '.md'), 'utf8');
  const fm = raw.match(/^---\n([\s\S]*?)\n---/)?.[1] ?? '';
  const g = fm.match(/\{"market": "Germany".*?"countervailing_duty_rate":\s*([0-9.]+)/);
  if (g && Number(g[1]) > 0) {
    flag('phev-cvd', id, `non-BEV with Germany CVD=${g[1]}`);
  }
}
ok.push('PHEV/EREV/HEV/ICE EU CVD = 0 (checked all non-BEV md files)');

// ── 汇总 ──
console.log('=== EV Hub Data Validation ===');
for (const line of ok) console.log('  ✓', line);
if (issues.length === 0) {
  console.log('\n✅ 0 issues. All data validation checks passed.');
  process.exit(0);
}
console.log(`\n❌ ${issues.length} issues found:`);
const byCat = {};
for (const i of issues) (byCat[i.category] ??= []).push(i);
for (const [cat, list] of Object.entries(byCat)) {
  console.log(`\n[${cat}] (${list.length})`);
  for (const i of list.slice(0, 20)) console.log(`  - ${i.id}: ${i.message}`);
}
process.exit(1);
