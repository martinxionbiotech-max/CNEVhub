/**
 * Site Configuration — CNEVhub
 *
 * @description
 * CNEVhub: Chinese EV export intelligence platform.
 * Company: Guangzhou Banghe Testing Technology Co., Ltd. (MCM)
 * Author: Wei Wang, Marketing Specialist
 */

import type { SocialLinks, LegalConfig } from '../lib/types';

/** Site name displayed in header, footer, and meta tags */
export const name = import.meta.env.SITE_NAME || 'CNEVhub';

/** Site description for SEO and meta tags */
export const description =
  import.meta.env.SITE_DESCRIPTION ||
  'The real landed cost of importing Chinese EVs — transparent breakdown of duties, VAT, freight, and certification.';

/** Production URL of your site (used for sitemap, RSS, canonical URLs) */
export const url = import.meta.env.SITE_URL || 'https://cnevhub.net';

/** Author name for meta tags and copyright */
export const author = import.meta.env.SITE_AUTHOR || 'Wei Wang';

/** Path to logo file (relative to /public) */
export const logo = '/logo.svg';

/** Path to Open Graph image (relative to /public) */
export const ogImage = '/images/og-image.png';

/** Social media links */
export const social: SocialLinks = {
  twitter: 'https://x.com/cnevhub',
  github: 'https://github.com/martinxionbiotech-max/CNEVhub',
  discord: '',
};

/** Company (EEAT Organization) */
export const company = {
  name: 'Guangzhou Banghe Testing Technology Co., Ltd. (MCM)',
  legalName: 'Guangzhou Banghe Testing Technology Co., Ltd.',
  description:
    'Guangzhou Banghe Testing Technology Co., Ltd. (MCM) provides automotive export compliance, testing, and landed-cost intelligence for Chinese EV importers worldwide.',
  url: 'https://cnevhub.net',
  logo: '/logo.svg',
  email: 'info@cnevhub.net',
  author: 'Wei Wang',
  authorRole: 'Marketing Specialist',
};

/** Legal configuration for privacy policy and terms pages */
export const legal: LegalConfig = {
  privacyEmail: 'privacy@cnevhub.net',
  legalEmail: 'legal@cnevhub.net',
  lastUpdated: 'September 5, 2026',
};
