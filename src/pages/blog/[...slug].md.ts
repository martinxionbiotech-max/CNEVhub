import type { APIRoute } from 'astro';
import { getCollection, type CollectionEntry } from 'astro:content';
import { siteConfig } from '@/config';

/**
 * /blog/[...slug].md — clean Markdown variant of each blog post.
 *
 * Generated at build time from the `blog` content collection body — the same
 * source Markdown the HTML page renders. Output is the post's title, front
 * matter metadata, full body (including its Sources section), and a canonical
 * link back to the HTML page. No navigation, footer, or JavaScript.
 */

type BlogPost = CollectionEntry<'blog'>;

const yaml = (v: unknown): string => JSON.stringify(v ?? '');

export async function getStaticPaths() {
  const posts = await getCollection('blog', ({ data }: { data: BlogPost['data'] }) => !data.draft);
  return posts.map((post) => ({ params: { slug: post.id } }));
}

export const GET: APIRoute = async ({ params }) => {
  const posts = await getCollection('blog', ({ data }: { data: BlogPost['data'] }) => !data.draft);
  const slug = Array.isArray(params.slug) ? params.slug.join('/') : params.slug;
  const post = posts.find((p) => p.id === slug);
  if (!post) {
    return new Response('Not found', { status: 404 });
  }
  const { data } = post;
  const canonical = `${siteConfig.url}/blog/${post.id}/`;

  const out: string[] = [];
  out.push('---');
  out.push(`title: ${yaml(data.title)}`);
  out.push(`description: ${yaml(data.description)}`);
  out.push(`author: ${yaml(data.author)}`);
  out.push(`published: ${yaml(data.publishedDate.toISOString().slice(0, 10))}`);
  if (data.tags && data.tags.length > 0) {
    out.push(`tags: [${data.tags.map((t) => yaml(t)).join(', ')}]`);
  }
  out.push(`canonical: ${yaml(canonical)}`);
  out.push('---');
  out.push('');
  out.push(`# ${data.title}`);
  out.push('');
  out.push(post.body || '');
  out.push('');

  return new Response(out.join('\n'), {
    headers: { 'Content-Type': 'text/markdown; charset=utf-8' },
  });
};
