/**
 * Navigation Configuration — CNEVhub
 *
 * EV export information platform navigation (header + footer).
 * Removed SaaS-template residue (pricing/login/dashboard/etc.).
 */

import type { Navigation } from '../lib/types';

export const navigation: Navigation = {
  header: {
    main: [
      { label: 'Home', href: '/' },
      { label: 'Vehicles', href: '/vehicles' },
      { label: 'Brands', href: '/brands' },
      { label: 'Landed Cost', href: '/landed-cost-calculator' },
      { label: 'How It Works', href: '/landed-cost-methodology' },
      { label: 'Guides', href: '/blog', feature: 'blog' },
      { label: 'Docs', href: '/docs', feature: 'docs' },
    ],
    cta: [
      { label: 'Browse Vehicles', href: '/vehicles', variant: 'primary' },
    ],
  },

  footer: {
    product: [
      { label: 'Vehicles', href: '/vehicles' },
      { label: 'Brands', href: '/brands' },
      { label: 'Landed Cost Calculator', href: '/landed-cost-calculator' },
      { label: 'Methodology', href: '/landed-cost-methodology' },
      { label: 'Docs', href: '/docs' },
    ],
    solutions: [
      { label: 'EU Import Guide', href: '/blog/import-chinese-ev-eu-guide' },
      { label: 'Export Landscape 2026', href: '/blog/chinese-ev-export-landscape-2026' },
      { label: 'BYD Seal Review', href: '/blog/byd-seal-deep-review' },
    ],
    resources: [
      { label: 'Blog', href: '/blog', feature: 'blog' },
      { label: 'FAQ', href: '/faq' },
    ],
    company: [
      { label: 'About', href: '/about' },
      { label: 'Contact', href: '/contact' },
    ],
    legal: [
      { label: 'Privacy', href: '/privacy' },
      { label: 'Terms', href: '/terms' },
      { label: 'Cookies', href: '/cookies' },
      { label: 'Disclaimer', href: '/disclaimer' },
    ],
  },
};

