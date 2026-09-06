/**
 * Calculate reading time based on word count
 *
 * @description
 * Estimates the reading time for a given text based on an average reading
 * speed of 200 words per minute. Returns the ceiling value to ensure
 * at least 1 minute is shown for any non-empty text.
 *
 * @param text - The text content to analyze
 * @returns Reading time in minutes (minimum 1 for non-empty text)
 *
 * @example
 * ```typescript
 * const minutes = calculateReadingTime(blogPost.body);
 * console.log(`${minutes} min read`);
 * ```
 */
export function calculateReadingTime(text: string): number {
  const wordCount = text.trim().split(/\s+/).length;
  return Math.ceil(wordCount / 200);
}

/**
 * Format a date for display
 *
 * @description
 * Formats a Date object into a human-readable string using the Intl.DateTimeFormat API.
 * Defaults to a medium-length date format (e.g., "Jan 15, 2025") if no options are provided.
 *
 * @param date - The date to format
 * @param options - Optional Intl.DateTimeFormatOptions for customizing the output
 * @returns Formatted date string
 *
 * @example
 * ```typescript
 * // Default format: "Jan 15, 2025"
 * formatDate(new Date('2025-01-15'));
 *
 * // Custom format: "January 15, 2025"
 * formatDate(new Date('2025-01-15'), { dateStyle: 'long' });
 *
 * // Full format with weekday: "Wednesday, January 15, 2025"
 * formatDate(new Date('2025-01-15'), { dateStyle: 'full' });
 * ```
 */
export function formatDate(
  date: Date,
  options: Intl.DateTimeFormatOptions = {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
  }
): string {
  return new Intl.DateTimeFormat('en-US', options).format(date);
}

/**
 * Normalize a tag into a URL-safe lowercase kebab-case slug.
 * Collapses case and whitespace variants so "BYD", "byd" and "BYD Seal"
 * never generate duplicate tag pages.
 */
export function slugifyTag(tag: string): string {
  return tag
    .trim()
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
}

const TAG_ACRONYMS = new Set([
  'byd', 'ev', 'eu', 'b2b', 'wltp', 'suv', 'mpv', 'bev', 'phev', 'erev',
  'hev', 'usd', 'uk', 'uae', 'ne', 'mg', 'nv', 'gt',
]);

/**
 * Prettify a kebab-case tag slug for display ("byd-seal" -> "BYD Seal").
 */
export function formatTag(tag: string): string {
  return tag
    .split('-')
    .map((w) =>
      TAG_ACRONYMS.has(w.toLowerCase())
        ? w.toUpperCase()
        : w.charAt(0).toUpperCase() + w.slice(1)
    )
    .join(' ');
}
