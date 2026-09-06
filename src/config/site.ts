/**
 * Site Configuration — CNEVhub
 *
 * @description
 * CNEVhub: Chinese EV export intelligence platform.
 * Company: Chengguang Energy (Jinzhou Chengguang Power Source Co., Ltd.)
 * Author: Wei Wang, EV & Battery Industry Analyst
 * Primary contact: Aaron.W (aaron@dinweys.com, WhatsApp/WeChat +86 13313137465)
 */

import type { SocialLinks, LegalConfig } from '../lib/types';

/** Site name displayed in header, footer, and meta tags */
export const name = import.meta.env.SITE_NAME || 'EV Hub';

/** Site description for SEO and meta tags */
export const description =
  import.meta.env.SITE_DESCRIPTION ||
  'The real landed cost of importing Chinese EVs — transparent breakdown of duties, VAT, freight, and certification.';

/** Production URL of your site (used for sitemap, RSS, canonical URLs) */
export const url = import.meta.env.SITE_URL || 'https://electricvehiclehub.net';

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
  name: 'Chengguang Energy',
  legalName: 'Jinzhou Chengguang Power Source Co., Ltd.',
  description:
    'Chengguang Energy (Jinzhou Chengguang Power Source Co., Ltd.) is an IATF 16949-certified automotive battery manufacturer founded in 2002, providing independent landed-cost intelligence and cross-border research for Chinese EV importers.',
  url: 'https://electricvehiclehub.net',
  logo: '/logo.svg',
  email: 'aaron@dinweys.com',
  phone: '+86 13313137465',
  whatsapp: '+86 13313137465',
  contactPerson: 'Aaron.W',
  author: 'Wei Wang',
  authorRole: 'EV & Battery Industry Analyst',
  authorBio:
    'Wei Wang has spent many years in automotive battery production, and in recent years has focused on commercial research into electric vehicles — import economics, tariffs, and cross-border compliance.',
};

/** Legal configuration for privacy policy and terms pages */
export const legal: LegalConfig = {
  privacyEmail: 'privacy@electricvehiclehub.net',
  legalEmail: 'legal@electricvehiclehub.net',
  lastUpdated: 'September 5, 2026',
};
