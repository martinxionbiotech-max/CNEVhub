import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import icon from 'astro-icon';
import tailwindcss from '@tailwindcss/vite';
import { siteConfig } from './src/config';
import rehypeDropLeadingH1 from './src/plugins/rehype-drop-leading-h1.mjs';

// Site URL from environment variable with localhost fallback
const siteUrl = process.env.SITE_URL || 'https://electricvehiclehub.net';

// Custom integration to warn about missing environment variables after build
function envCheckIntegration() {
  return {
    name: 'env-check',
    hooks: {
      'astro:build:done': () => {
        if (!process.env.SITE_URL) {
          console.warn('='.repeat(60));
          console.warn('WARNING: SITE_URL environment variable not set');
          console.warn('Build completed with fallback URL: https://electricvehiclehub.net');
          console.warn('For production, create .env file and set SITE_URL');
          console.warn('='.repeat(60) + '\n');
        }
      },
    },
  };
}

export default defineConfig({
  site: siteUrl,
  integrations: [
    mdx(),
    icon(),
    envCheckIntegration(),
    sitemap({
      filter: (page) => {
        const { features } = siteConfig;

        // 分页页（/blog/page/N/）已设 noindex → 不进 sitemap（收录指令不能自相矛盾）
        if (page.includes('/blog/page/')) return false;

        // 标签聚合页（/blog/tag/x/）已设 noindex,follow → 不进 sitemap（§27 同原则）
        if (page.includes('/blog/tag/')) return false;

        // Filter out pages based on feature flags
        if (!features.blog && page.includes('/blog')) return false;
        if (!features.docs && page.includes('/docs')) return false;
        if (!features.changelog && page.includes('/changelog')) return false;
        if (!features.testimonials && page.includes('/testimonials')) return false;
        if (!features.roadmap && page.includes('/roadmap')) return false;

        return true;
      },
    }),
  ],
  // 去掉正文首个 H1（hero 已有 H1），修「一页两个 H1」
  markdown: {
    rehypePlugins: [rehypeDropLeadingH1],
  },
  vite: {
    plugins: [tailwindcss()],
  },
});
