# owais.qzz.io — personal site and Goshawk Labs

An Astro-based personal site that serves two sites from one codebase:

- the personal site (`/`) — portfolio, writing, and the link archive
- Goshawk Labs (`/goshawk-labs/`) — the AI-engineering studio site

Design system: "engineer's field notebook" — heavy grotesque display type,
IBM Plex Mono instruments, Instrument Serif annotations, vermilion on warm
paper for personal, instrument-and-obsidian dark for Goshawk Labs.

## Setup

```sh
npm install
npm run dev      # local development server
npm run build    # static build into dist/
npm run preview  # serve the built site locally
npx astro check  # typecheck (run before any commit)
```

Requires Node 20+. Linux-only commands are fine (the environment is Fedora).

## Repository layout

```
src/
  pages/                 # route pages (personal) and goshawk-labs/
    blog/                # personal field notes index
    blog/tag/[tag].astro # static tag pages, all audiences
    links.astro          # archive hub with client search/filter
    links/[category].astro # one editorial page per shelf (10 categories)
  content/posts/         # all blog posts (markdown, frontmatter schema in content.config.ts)
  data/links/            # the 499-item link archive, one JSON per category
  lib/
    links.ts             # aggregates the JSON catalog (CATEGORIES, ALL_LINKS, helpers)
    posts.ts             # post helpers: sort, audience, tags, related
  components/            # LinkCard, LinkFilterBar, PostCard, etc.
  styles/global.css      # design tokens and shared styles
scripts/links/           # generators + verifier for the link archive
```

## The link archive

499 hand-curated links across 10 shelves, stored as plain JSON under
`src/data/links/`. Every URL was link-checked before inclusion (0 dead at
last sweep). Contributing or re-checking:

```sh
python3 scripts/links/ai.py          # regenerate a category's JSON from its script
python3 scripts/links/verify.py      # full parallel curl sweep (write urls.txt)
```

See `src/data/links/README.md` for the exact schema and workflow.

## Writing posts

Posts live in `src/content/posts/*.md`. The frontmatter schema
(`src/content.config.ts`) expects at minimum `title`, `description`,
`pubDate`, `audience`. Audience semantics:

- `personal` — shown only on the personal blog
- `goshawk` — shown only on Goshawk Insights
- `both` — shown on the personal blog and Goshawk Insights

`audience: goshawk` posts stay canonical to Goshawk Insights and never
appear on the personal blog index (see `onPersonalSite` in `src/lib/posts.ts`).
Tags are shared globally; tag pages live at `/blog/tag/<slug>/` and list all
audiences. Keep tags few and consistent (reused tags build better tag pages).

Weight/quality rules: no placeholder text, descriptions written for humans,
`sources` point at real, verified URLs (the link shelf is a good source),
honest counts everywhere.