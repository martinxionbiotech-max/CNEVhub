#!/usr/bin/env node
/**
 * EV Hub build 后一致性 + sitemap 校验（§32 + §27）。
 * Run: node scripts/site-consistency.mjs   （需先 npm run build）
 *
 * 检查：
 *  1. 首页 / vehicles 索引 / about / 全部品牌页的计数与数据层一致
 *     （vehicle-master.json、brand-master.json、车型 md 派生计数）
 *  2. sitemap(-index) 全量 URL 有效性：URL 在 dist 有产物、无 404/500 混入
 *  3. sitemap 内无 noindex 页混入（/blog/page/、/blog/tag/、draft 博文）
 *  4. sitemap 分桶计数与数据层一致（vehicles / brands / 已发布博文）
 *
 * 退出码：0 = 全部通过；1 = 存在不一致。
 */
import { readFileSync, readdirSync, existsSync, statSync } from 'node:fs';
import { join } from 'node:path';

const ROOT = new URL('..', import.meta.url).pathname;
const DIST = join(ROOT, 'dist');
const SITE = 'https://electricvehiclehub.net';

const checks = [];
const failures = [];
const ok = (label) => checks.push(`✓ ${label}`);
const bad = (label) => {
  failures.push(label);
  checks.push(`✗ ${label}`);
};

// ── 数据层期望值 ──
const vehicleMaster = JSON.parse(readFileSync(join(ROOT, 'src/data/vehicle-master.json'), 'utf8'));
const brandMaster = JSON.parse(readFileSync(join(ROOT, 'src/data/brand-master.json'), 'utf8'));
const EXPECT_VEHICLES = vehicleMaster.vehicles.length;
const EXPECT_BRANDS = brandMaster.brands.length;
const EXPECT_MARKETS = Object.keys(JSON.parse(readFileSync(join(ROOT, 'src/data/tariffs.json'), 'utf8')).markets).length;

// 已发布博文数（draft 排除）
const blogFiles = readdirSync(join(ROOT, 'src/content/blog')).filter((f) => f.endsWith('.md'));
const publishedBlog = blogFiles.filter((f) => !readFileSync(join(ROOT, 'src/content/blog', f), 'utf8').includes('draft: true'));
const draftSlugs = blogFiles
  .filter((f) => readFileSync(join(ROOT, 'src/content/blog', f), 'utf8').includes('draft: true'))
  .map((f) => f.replace(/\.md$/, ''));

const readDist = (rel) => {
  const p = join(DIST, rel);
  return existsSync(p) ? readFileSync(p, 'utf8') : '';
};

// ── 1. 页面计数与数据层一致 ──
const home = readDist('index.html');
home.includes(`View all ${EXPECT_VEHICLES} vehicles`)
  ? ok(`首页计数 = ${EXPECT_VEHICLES} vehicles`)
  : bad(`首页计数 ≠ ${EXPECT_VEHICLES}（"View all N vehicles" 未命中）`);

const vehiclesIndex = readDist(join('vehicles', 'index.html'));
vehiclesIndex.includes(`${EXPECT_VEHICLES} vehicles`)
  ? ok(`/vehicles/ 计数 = ${EXPECT_VEHICLES}`)
  : bad(`/vehicles/ 计数 ≠ ${EXPECT_VEHICLES}`);

const about = readDist(join('about', 'index.html'));
const aboutOk =
  about.includes(`>${EXPECT_VEHICLES}<`) &&
  about.includes(`>${EXPECT_BRANDS}<`) &&
  about.includes(`>${EXPECT_MARKETS}<`) &&
  about.includes('Vehicles Cataloged') &&
  about.includes('Chinese Brands') &&
  about.includes('Export Markets Modeled');
aboutOk
  ? ok(`about 计数 = ${EXPECT_VEHICLES}/${EXPECT_BRANDS}/${EXPECT_MARKETS}`)
  : bad(`about 计数与 site-stats 不一致（期望 ${EXPECT_VEHICLES}/${EXPECT_BRANDS}/${EXPECT_MARKETS}）`);

// 品牌页：每页 "{n} models" 与车型 md 派生计数一致
const vehMdDir = join(ROOT, 'src/content/vehicles');
const brandModelCounts = {};
for (const f of readdirSync(vehMdDir)) {
  if (!f.endsWith('.md')) continue;
  const raw = readFileSync(join(vehMdDir, f), 'utf8');
  const m = raw.match(/^brand:\s*"?([^"\n]+)"?\s*$/m);
  if (!m) continue;
  const b = m[1].trim();
  brandModelCounts[b] = (brandModelCounts[b] ?? 0) + 1;
}
const brandSlugs = Object.keys(brandModelCounts);
let brandPagesOk = 0;
let brandPagesBad = [];
for (const slug of brandSlugs) {
  const html = readDist(join('brands', slug, 'index.html'));
  const want = brandModelCounts[slug];
  if (html.includes(`${want} models`)) brandPagesOk++;
  else brandPagesBad.push(`${slug} (期望 ${want} models)`);
}
brandPagesOk === brandSlugs.length
  ? ok(`品牌页 model 计数 ${brandPagesOk}/${brandSlugs.length} 一致`)
  : bad(`品牌页计数不一致 ${brandPagesBad.length} 个：${brandPagesBad.slice(0, 5).join(', ')}`);

// ── 2. sitemap 解析（sitemap-index → sitemap-0.xml）──
const sitemapIndex = readDist('sitemap-index.xml');
const subMaps = [...sitemapIndex.matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1]);
if (subMaps.length === 0) {
  bad('sitemap-index.xml 无子 sitemap 引用');
} else {
  ok(`sitemap-index 引用 ${subMaps.length} 个子 sitemap`);
  const locs = [];
  for (const sub of subMaps) {
    const name = sub.split('/').pop();
    const xml = readDist(name);
    for (const m of xml.matchAll(/<loc>([^<]+)<\/loc>/g)) locs.push(m[1]);
  }
  const siteLocs = locs.filter((l) => l.startsWith(SITE));
  ok(`sitemap 全量 URL：${siteLocs.length}`);
  const sitePaths = siteLocs.map((l) => new URL(l).pathname);

  // 分桶
  const bucket = { vehicles: 0, brands: 0, blogPosts: 0, blogTag: 0, blogPage: 0, other: 0 };
  for (const p of sitePaths) {
    if (p.startsWith('/vehicles/') && p !== '/vehicles/') bucket.vehicles++;
    else if (p.startsWith('/brands/') && p !== '/brands/') bucket.brands++;
    else if (p.startsWith('/blog/tag/')) bucket.blogTag++;
    else if (p.startsWith('/blog/page/')) bucket.blogPage++;
    else if (p.startsWith('/blog/') && p !== '/blog/') bucket.blogPosts++;
    else bucket.other++;
  }
  bucket.vehicles === EXPECT_VEHICLES
    ? ok(`sitemap vehicles = ${EXPECT_VEHICLES}`)
    : bad(`sitemap vehicles = ${bucket.vehicles} ≠ ${EXPECT_VEHICLES}`);
  bucket.brands === EXPECT_BRANDS
    ? ok(`sitemap brands = ${EXPECT_BRANDS}`)
    : bad(`sitemap brands = ${bucket.brands} ≠ ${EXPECT_BRANDS}`);
  bucket.blogPosts === publishedBlog.length
    ? ok(`sitemap 已发布博文 = ${bucket.blogPosts}（draft 未混入）`)
    : bad(`sitemap 博文 = ${bucket.blogPosts} ≠ 已发布 ${publishedBlog.length}`);

  // noindex 页混入检查
  const tagLocs = sitePaths.filter((p) => p.startsWith('/blog/tag/'));
  const pageLocs = sitePaths.filter((p) => p.startsWith('/blog/page/'));
  tagLocs.length === 0
    ? ok('sitemap 无 /blog/tag/ noindex 页混入')
    : bad(`sitemap 混入 ${tagLocs.length} 个 noindex tag 页`);
  pageLocs.length === 0
    ? ok('sitemap 无 /blog/page/ 分页混入')
    : bad(`sitemap 混入 ${pageLocs.length} 个分页 URL`);

  const draftInSitemap = sitePaths.filter((p) =>
    draftSlugs.some((s) => p === `/blog/${s}/`),
  );
  draftInSitemap.length === 0
    ? ok('sitemap 无 draft 博文')
    : bad(`sitemap 混入 draft：${draftInSitemap.join(', ')}`);

  // 404/500 混入 + URL 有效性（dist 产物存在）
  const forbidden = sitePaths.filter((p) => /\/404\/|\/500\//.test(p));
  forbidden.length === 0 ? ok('sitemap 无 404/500') : bad(`sitemap 混入 404/500：${forbidden.join(', ')}`);

  const fileForUrl = (pathname) => {
    if (pathname === '/') return join(DIST, 'index.html');
    return join(DIST, pathname.replace(/^\/+/, ''), 'index.html');
  };
  const missing = [];
  const noindexInSitemap = [];
  for (const p of sitePaths) {
    const f = fileForUrl(p);
    if (!existsSync(f)) {
      missing.push(p);
      continue;
    }
    const html = readFileSync(f, 'utf8');
    if (/<meta name="robots"[^>]*noindex/i.test(html.slice(0, 4000))) noindexInSitemap.push(p);
  }
  missing.length === 0
    ? ok(`sitemap 全部 URL 在 dist 有产物（${siteLocs.length}）`)
    : bad(`sitemap 有 ${missing.length} 个 URL 无产物：${missing.slice(0, 5).join(', ')}`);
  noindexInSitemap.length === 0
    ? ok('sitemap 中所有页面均无 noindex meta')
    : bad(`sitemap 中 ${noindexInSitemap.length} 个页面带 noindex：${noindexInSitemap.slice(0, 5).join(', ')}`);

  // 反向：dist 非错误页 HTML 是否都被 sitemap 覆盖（排除 noindex 页与 _astro）
  const known = new Set(sitePaths);
  const walk = (dir, out = []) => {
    for (const e of readdirSync(dir)) {
      const p = join(dir, e);
      if (statSync(p).isDirectory()) walk(p, out);
      else if (e === 'index.html') out.push(p);
    }
    return out;
  };
  const unindexed = [];
  for (const f of walk(DIST)) {
    let rel = f.replace(DIST, '').replace(/\/index\.html$/, '/');
    if (rel === '/') continue;
    if (rel.startsWith('/_') || rel.includes('/404/') || rel.includes('/500/') || rel === '/404/') continue;
    if (known.has(rel)) continue;
    // noindex 页允许不在 sitemap（分页/tag），其余为未收录
    const html = readFileSync(f, 'utf8');
    if (/<meta name="robots"[^>]*noindex/i.test(html.slice(0, 4000))) continue;
    unindexed.push(rel);
  }
  unindexed.length === 0
    ? ok('dist 全部可收录页面均被 sitemap 覆盖')
    : bad(`dist 有 ${unindexed.length} 个可收录页面未进 sitemap：${unindexed.slice(0, 10).join(', ')}`);
}

// ── 输出 ──
console.log('=== Site Consistency (§32) + Sitemap Validation (§27) ===');
console.log(`数据层期望：vehicles=${EXPECT_VEHICLES} brands=${EXPECT_BRANDS} markets=${EXPECT_MARKETS} 已发布博文=${publishedBlog.length}`);
for (const c of checks) console.log(' ', c);
console.log('');
if (failures.length === 0) {
  console.log('结论：全部一致 ✅');
  process.exit(0);
} else {
  console.log(`结论：${failures.length} 项不一致 ❌`);
  process.exit(1);
}
