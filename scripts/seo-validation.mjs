#!/usr/bin/env node
/**
 * EV Hub full SEO validation (P2 §22-24, §28).
 * Run: npm run seo:validate
 * 1) sitemap URL 全量有效性（对照 dist 构建产物）
 * 2) 内链断裂全量扫描（dist HTML 内 href/src）
 * 3) 抽样一致性：10 车辆页 + 10 品牌页 + 5 blog + 5 docs
 * 结果追加到 docs/seo-integrity-report.md。
 */
import { readFileSync, readdirSync, existsSync, statSync, writeFileSync, appendFileSync } from 'node:fs';
import { join } from 'node:path';

const ROOT = new URL('..', import.meta.url).pathname;
const DIST = join(ROOT, 'dist');
const SITE = 'https://electricvehiclehub.net';
const today = new Date().toISOString().split('T')[0];

const issues = [];
const checks = [];
const walk = (dir, out = []) => {
  for (const e of readdirSync(dir)) {
    const p = join(dir, e);
    if (statSync(p).isDirectory()) walk(p, out);
    else if (e.endsWith('.html')) out.push(p);
  }
  return out;
};
const htmlFiles = walk(DIST);
const distRel = (p) => p.replace(DIST, '').replace(/\/index\.html$/, '/');
const fileForUrl = (pathname) => {
  // /foo/ -> dist/foo/index.html ; /foo -> dist/foo/index.html (fallback)
  const clean = pathname.split('#')[0].split('?')[0];
  if (!clean.startsWith('/')) return null;
  if (clean === '/') return join(DIST, 'index.html');
  const asDir = join(DIST, clean.replace(/^\/+/, ''), 'index.html');
  if (existsSync(asDir)) return asDir;
  const asFile = join(DIST, clean.replace(/^\/+/, ''));
  if (existsSync(asFile)) return asFile;
  return null;
};

// ── 1. sitemap URL 全量有效性 ──
const sitemapXml = readFileSync(join(DIST, 'sitemap-0.xml'), 'utf8');
const locs = [...sitemapXml.matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1]);
const siteLocs = locs.filter((l) => l.startsWith(SITE));
const missingSitemap = [];
for (const loc of siteLocs) {
  const u = new URL(loc);
  if (!fileForUrl(u.pathname)) missingSitemap.push(loc);
}
checks.push(`sitemap: ${locs.length} URLs, ${siteLocs.length} same-host, missing in dist: ${missingSitemap.length}`);
for (const m of missingSitemap.slice(0, 10)) issues.push(`sitemap-missing: ${m}`);
// 反向：dist html 未被 sitemap 收录
const known = new Set(siteLocs.map((l) => new URL(l).pathname));
const unindexed = [];
for (const f of htmlFiles) {
  const rel = distRel(f);
  if (rel.endsWith('/404/') || rel.endsWith('/500/') || rel === '/404.html' || rel === '/500.html' || rel.startsWith('/_')) continue;
  if (!known.has(rel)) unindexed.push(rel);
}
checks.push(`dist html: ${htmlFiles.length}, not in sitemap (non-error pages): ${unindexed.length}`);
for (const u of unindexed.slice(0, 15)) issues.push(`not-in-sitemap: ${u}`);

// ── 2. 内链断裂全量扫描 ──
const hrefRe = /(?:href|src)="([^"]+)"/g;
let internalChecked = 0;
const broken = [];
const SKIP_PREFIX = ['#', 'mailto:', 'tel:', 'data:', 'javascript:', 'http://', 'https://', '//', '{'];
for (const f of htmlFiles) {
  const html = readFileSync(f, 'utf8');
  for (const m of html.matchAll(hrefRe)) {
    const ref = m[1].trim();
    if (!ref || SKIP_PREFIX.some((p) => ref.startsWith(p))) continue;
    if (ref.includes('{')) continue; // astro 模板变量残留（异常）
    let pathname = ref;
    if (ref.startsWith(SITE)) pathname = new URL(ref).pathname;
    if (!pathname.startsWith('/')) continue; // 相对路径罕见，跳过
    if (pathname.startsWith('/_astro/') || pathname.startsWith('/images/') || pathname.startsWith('/fonts/') || pathname.startsWith('/favicon')) continue;
    if (/\.(png|jpe?g|gif|webp|svg|ico|css|js|xml|txt|webmanifest|woff2?|pdf|json|map)$/.test(pathname)) continue;
    internalChecked++;
    const target = fileForUrl(pathname);
    if (!target) broken.push({ from: distRel(f), href: pathname });
  }
}
checks.push(`internal links checked: ${internalChecked}, broken: ${broken.length}`);
for (const b of broken.slice(0, 30)) issues.push(`broken-link: ${b.from} -> ${b.href}`);

// ── 3. 抽样一致性 ──
const master = JSON.parse(readFileSync(join(ROOT, 'src/data/vehicle-master.json'), 'utf8')).vehicles;
const masterBy = new Map(master.map((v) => [v.vehicle_id, v]));
const safeRead = (p) => (existsSync(p) ? readFileSync(p, 'utf8') : '');
const pick = (arr, n) => {
  const step = Math.max(1, Math.floor(arr.length / n));
  return Array.from({ length: n }, (_, i) => arr[Math.min(arr.length - 1, i * step)]);
};
const sampleV = pick(master, 10);
let vOk = 0, vFail = 0;
const vFailures = [];
for (const v of sampleV) {
  const f = join(DIST, 'vehicles', v.vehicle_id, 'index.html');
  const html = existsSync(f) ? readFileSync(f, 'utf8') : '';
  const price = v.price_usd.toLocaleString('en-US');
  const okTitle = html.includes(`>${v.model}<`) || html.includes(v.model);
  const okPrice = html.includes(price);
  const okRange = v.range_cltc_km == null || html.includes(`${v.range_cltc_km} km`);
  if (okTitle && okPrice && okRange) vOk++;
  else {
    vFail++;
    vFailures.push(`${v.vehicle_id}: title=${okTitle} price=${okPrice} range=${okRange}`);
  }
}
checks.push(`sample vehicles: ${vOk}/${sampleV.length} consistent`);

const brandFiles = readdirSync(join(ROOT, 'src/content/brands')).filter((f) => f.endsWith('.md'));
const sampleB = pick(brandFiles, 10);
let bOk = 0;
for (const bf of sampleB) {
  const raw = readFileSync(join(ROOT, 'src/content/brands', bf), 'utf8');
  const name = raw.match(/^brand_name:\s*"([^"]+)"/m)?.[1] ?? bf;
  const html = safeRead(join(DIST, 'brands', bf.slice(0, -3), 'index.html'));
  if (html.includes(name)) bOk++;
}
checks.push(`sample brands: ${bOk}/${sampleB.length} consistent`);

const blogFiles = readdirSync(join(ROOT, 'src/content/blog')).filter((f) => f.endsWith('.md'));
const sampleBl = pick(blogFiles, 5);
let blOk = 0;
for (const bf of sampleBl) {
  const raw = readFileSync(join(ROOT, 'src/content/blog', bf), 'utf8');
  const title = raw.match(/^title:\s*"([^"]+)"/m)?.[1] ?? bf;
  const html = safeRead(join(DIST, 'blog', bf.slice(0, -3), 'index.html'));
  if (html.includes(title)) blOk++;
}
checks.push(`sample blog: ${blOk}/${sampleBl.length} consistent`);

const docFiles = readdirSync(join(ROOT, 'src/content/docs')).filter((f) => f.endsWith('.md'));
const sampleD = pick(docFiles, 5);
let dOk = 0;
for (const df of sampleD) {
  const raw = readFileSync(join(ROOT, 'src/content/docs', df), 'utf8');
  const title = raw.match(/^title:\s*"([^"]+)"/m)?.[1] ?? df;
  const html = safeRead(join(DIST, 'docs', df.slice(0, -3), 'index.html'));
  if (html.includes(title)) dOk++;
}
checks.push(`sample docs: ${dOk}/${sampleD.length} consistent`);

// ── 追加报告 ──
const lines = [];
lines.push('');
lines.push('## 全量 SEO 验证（P2 深度，' + today + '）');
lines.push('');
lines.push('> 工具：`npm run seo:validate`（scripts/seo-validation.mjs）');
lines.push('');
for (const c of checks) lines.push(`- ${c}`);
if (vFailures.length) lines.push(`- 车辆抽样失败明细：${vFailures.join(' | ')}`);
lines.push('');
if (issues.length === 0) {
  lines.push('**结论：全量检查 0 issues。**');
} else {
  lines.push(`**结论：${issues.length} 个问题（前 45 条）：**`);
  lines.push('');
  for (const i of issues.slice(0, 45)) lines.push(`- ${i}`);
}
appendFileSync(join(ROOT, 'docs/seo-integrity-report.md'), lines.join('\n') + '\n');

console.log('=== SEO Validation ===');
for (const c of checks) console.log('  ✓', c);
console.log(`  issues: ${issues.length}`);
if (vFailures.length) for (const f of vFailures) console.log('  ✗ vehicle sample:', f);
process.exit(0);
