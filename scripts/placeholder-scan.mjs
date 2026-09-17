#!/usr/bin/env node
/**
 * EV Hub 全字段占位扫描（P2 §15 扩展）。
 * Run: npm run placeholder:scan
 * 扫描 vehicle-master 全字段 + md frontmatter：
 * 9999/99999 哨兵值、未来日期、负值、空串、placeholder/TBD/N/A 等字样。
 * 结果追加到 docs/data-quality-report.md。
 */
import { readFileSync, readdirSync, appendFileSync } from 'node:fs';
import { join } from 'node:path';

const ROOT = new URL('..', import.meta.url).pathname;
const today = new Date().toISOString().split('T')[0];
const load = (p) => JSON.parse(readFileSync(join(ROOT, p), 'utf8'));
const vehicles = load('src/data/vehicle-master.json').vehicles;

const SENTINEL_NUMS = new Set([9999, 99999, 999999, -1]);
// 哨兵值仅适用于非价格字段（价格恰为 9999 是合理值，如入门车价）
const SENTINEL_FIELDS = new Set(['battery_kwh','range_cltc_km','range_long_km','motor_power_kw','torque_nm',
  'accel_0_100_s','top_speed_kmh','length_mm','width_mm','height_mm','wheelbase_mm','weight_kg',
  'efficiency_kwh_100km','data_tier','vehicle_count','established','model_count']);
const PLACEHOLDER_RE = /placeholder|tbd|todo|fixme|待定|占位|n\/a/i;
const findings = [];

const checkVal = (id, field, val) => {
  if (val === null || val === undefined) return;
  if (typeof val === 'number') {
    if (val < 0) findings.push({ id, field, value: String(val), why: 'negative number' });
    else if (SENTINEL_NUMS.has(val) && (SENTINEL_FIELDS.has(field) || field.endsWith('_km') || field.endsWith('_kw') || field.endsWith('_nm'))) findings.push({ id, field, value: String(val), why: 'sentinel number (9999-class)' });
  } else if (typeof val === 'string') {
    if (val.trim() === '') findings.push({ id, field, value: '(empty)', why: 'empty string' });
    else if (PLACEHOLDER_RE.test(val)) findings.push({ id, field, value: val, why: 'placeholder text' });
    else if (/^\d{4}-\d{2}-\d{2}/.test(val) && val > today) findings.push({ id, field, value: val, why: 'future date' });
  } else if (Array.isArray(val)) {
    val.forEach((item) => { if (item && typeof item === 'object') checkObj(id, field, item); });
  } else if (typeof val === 'object') {
    checkObj(id, field, val);
  }
};
const checkObj = (id, prefix, obj) => {
  for (const [k, v] of Object.entries(obj)) {
    checkVal(id, prefix ? `${prefix}.${k}` : k, v);
    if (v && typeof v === 'object' && !Array.isArray(v)) checkObj(id, `${prefix}.${k}`, v);
  }
};

// ── master 全字段 ──
for (const v of vehicles) checkObj(v.vehicle_id, '', v);
const masterFindings = findings.slice();
const masterCount = masterFindings.length;

// ── md frontmatter ──
const mdFindings = [];
const mdDir = join(ROOT, 'src/content/vehicles');
for (const f of readdirSync(mdDir)) {
  if (!f.endsWith('.md')) continue;
  const raw = readFileSync(join(mdDir, f), 'utf8');
  const fm = raw.match(/^---\n([\s\S]*?)\n---/)?.[1] ?? '';
  for (const line of fm.split('\n')) {
    const m = line.match(/^([a-z_0-9]+):\s*(.*)$/);
    if (!m) continue;
    const [, k, vstr] = m;
    const val = vstr.trim();
    if (val === '' || val === 'null') continue;
    if (val === '-1' || val === '9999' || val === '99999') {
      mdFindings.push({ id: f, field: k, value: val, why: 'sentinel number' });
      continue;
    }
    if (PLACEHOLDER_RE.test(val) && k !== 'data_source') {
      mdFindings.push({ id: f, field: k, value: val.slice(0, 60), why: 'placeholder text' });
      continue;
    }
    if (k === 'data_updated' && /^\d{4}-\d{2}-\d{2}/.test(val) && val > today) {
      mdFindings.push({ id: f, field: k, value: val, why: 'future date' });
    }
  }
}

// ── 汇总追加报告 ──
const lines = [];
lines.push('');
lines.push('## 全字段占位扫描（P2 §15 扩展，' + today + '）');
lines.push('');
lines.push('> 工具：`npm run placeholder:scan`（scripts/placeholder-scan.mjs）。扫描 9999/99999 哨兵值、未来日期、负值、空串、placeholder/TBD/N/A 字样。');
lines.push('');
lines.push(`- vehicle-master 全字段（含 variants）：**${masterCount}** 条异常`);
lines.push(`- md frontmatter 扫描：**${mdFindings.length}** 条异常`);
lines.push('');
if (masterCount === 0 && mdFindings.length === 0) {
  lines.push('✅ 无异常值。');
} else {
  lines.push('| 来源 | id | 字段 | 值 | 原因 |');
  lines.push('|---|---|---|---|---|');
  for (const x of [...masterFindings, ...mdFindings].slice(0, 100)) {
    lines.push(`| master/md | ${x.id} | ${x.field} | ${x.value} | ${x.why} |`);
  }
  if (masterFindings.length + mdFindings.length > 100) lines.push(`| … | … | … | 共 ${masterFindings.length + mdFindings.length} 条，其余略 | |`);
}
appendFileSync(join(ROOT, 'docs/data-quality-report.md'), lines.join('\n') + '\n');

console.log('=== Placeholder Scan ===');
console.log(`  master findings: ${masterCount}`);
console.log(`  md findings: ${mdFindings.length}`);
for (const x of [...masterFindings, ...mdFindings].slice(0, 20)) console.log(`  - ${x.id} | ${x.field} | ${x.value} | ${x.why}`);
