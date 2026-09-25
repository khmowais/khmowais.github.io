import type { CollectionEntry } from "astro:content";

export type Post = CollectionEntry<"posts">;

export function sortByDate(posts: Post[]): Post[] {
  return [...posts].sort(
    (a, b) => b.data.pubDate.getTime() - a.data.pubDate.getTime()
  );
}

export function published(posts: Post[]): Post[] {
  return posts.filter((p) => !p.data.draft);
}

export function byAudience(posts: Post[], audience: "personal" | "goshawk"): Post[] {
  return published(posts).filter(
    (p) => p.data.audience === "both" || p.data.audience === audience
  );
}

// Posts that belong on the personal site's blog index: goshawk-only notes
// stay canonical to Goshawk Insights rather than leaking into the personal feed.
export function onPersonalSite(posts: Post[]): Post[] {
  return published(posts).filter((p) => p.data.audience !== "goshawk");
}

export function formatDate(d: Date): string {
  return d.toLocaleDateString("en-GB", { year: "numeric", month: "short", day: "numeric" });
}

export function estimateReadingMinutes(bodyMarkdown: string): number {
  const words = bodyMarkdown
    .replace(/```[\s\S]*?```/g, " ")
    .replace(/[^\w\s]/g, " ")
    .trim()
    .split(/\s+/)
    .filter(Boolean).length;
  return Math.max(1, Math.round(words / 200));
}

export function tagSlug(tag: string): string {
  return tag
    .toLowerCase()
    .replace(/&/g, "and")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

export function allTags(posts: Post[]): string[] {
  const set = new Set<string>();
  for (const p of published(posts)) {
    for (const t of p.data.tags ?? []) set.add(t);
  }
  return [...set].sort((a, b) => a.localeCompare(b));
}

export function postsForTag(posts: Post[], tag: string): Post[] {
  return published(posts).filter((p) => (p.data.tags ?? []).includes(tag));
}

export function relatedPosts(posts: Post[], post: Post, count = 3): Post[] {
  const mine = new Set(post.data.tags ?? []);
  return published(posts)
    .filter((p) => p.id !== post.id)
    .filter((p) => (p.data.tags ?? []).some((t) => mine.has(t)))
    .sort((a, b) => {
      const score = (p: Post) =>
        (p.data.tags ?? []).filter((t) => mine.has(t)).length;
      return score(b) - score(a);
    })
    .slice(0, count);
}