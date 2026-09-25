import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const posts = defineCollection({
  loader: glob({ pattern: "**/*.{md,mdx}", base: "./src/content/posts" }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    tags: z.array(z.string()).default([]),
    author: z.string().default("Khawaja M. Owais"),
    // "personal" -> shows only on the personal site's blog,
    // "goshawk" -> shows only on Goshawk Insights,
    // "both"     -> shows on the personal blog and (with a canonical link)
    //              a condensed entry on Goshawk Insights.
    audience: z.enum(["personal", "goshawk", "both"]).default("personal"),
    readingMinutes: z.number().int().positive().optional(),
    sources: z.array(z.string().url()).default([]),
    draft: z.boolean().default(false),
  }),
});

export const collections = { posts };