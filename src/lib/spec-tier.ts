/**
 * spec-tier.ts — P3 spec source tiering (数据来源分层).
 *
 * Five-tier vocabulary for how a specification value was sourced:
 *   official_spec      官方规格（厂家官网 / 工信部公告 / 监管文件）
 *   manufacturer_claim 厂商宣称（未独立验证的营销口径）
 *   independent_test   独立测试（第三方实测 / 机构评测）
 *   estimate           估算（本站推算，如 landed-cost 模板层固定值）
 *   unverified         未验证（有值但无法溯源）
 *
 * Initial mapping is a *deterministic derivation* from the existing
 * `data_tier` integer already recorded in vehicle frontmatter — no value is
 * invented. Tiers `estimate` and `unverified` are defined but NOT auto-assigned
 * here (no clean signal exists in current data); they remain available for
 * explicit per-field assignment in later batches.
 */

export const SPEC_SOURCE_TIERS = [
  'official_spec',
  'manufacturer_claim',
  'independent_test',
  'estimate',
  'unverified',
] as const;

export type SpecSourceTier = (typeof SPEC_SOURCE_TIERS)[number];

const TIER_BY_DATA_TIER: Record<number, SpecSourceTier> = {
  1: 'official_spec',
  2: 'manufacturer_claim',
  3: 'independent_test',
};

/**
 * Derive a spec source tier from a legacy integer data_tier.
 * Returns null when there is no basis (missing / unmapped data_tier) so the
 * original state is preserved rather than a tier being fabricated.
 */
export function tierFromDataTier(
  dataTier: number | null | undefined,
): SpecSourceTier | null {
  if (dataTier == null) return null;
  return TIER_BY_DATA_TIER[dataTier] ?? null;
}
