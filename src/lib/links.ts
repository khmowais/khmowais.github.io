import ai from "../data/links/ai.json";
import localAi from "../data/links/local-ai.json";
import lowlevel from "../data/links/lowlevel.json";
import radio from "../data/links/radio.json";
import wildlife from "../data/links/wildlife.json";
import history from "../data/links/history.json";
import ownership from "../data/links/ownership.json";
import systems from "../data/links/systems.json";
import software from "../data/links/software.json";
import misc from "../data/links/misc.json";

export type LinkType =
  | "paper"
  | "article"
  | "docs"
  | "repo"
  | "project"
  | "tool"
  | "book"
  | "archive"
  | "org"
  | "dataset"
  | "video"
  | "forum"
  | "guide"
  | "course"
  | "news";

export interface LinkItem {
  id: string;
  categoryId: string;
  title: string;
  url: string;
  description: string;
  tags: string[];
  type: LinkType;
  subcategory?: string;
  year?: number;
  source?: string;
}

export interface LinkCategory {
  id: string;
  name: string;
  blurb: string;
  items: LinkItem[];
}

export const TYPE_LABELS: Record<LinkType, string> = {
  paper: "Paper",
  article: "Article",
  docs: "Docs",
  repo: "Repo",
  project: "Project",
  tool: "Tool",
  book: "Book",
  archive: "Archive",
  org: "Org",
  dataset: "Dataset",
  video: "Video",
  forum: "Forum",
  guide: "Guide",
  course: "Course",
  news: "News",
};

interface RawLinkItem {
  title: string;
  url: string;
  description: string;
  tags: string[];
  type: string;
  subcategory?: string;
  year?: number;
  source?: string;
}

interface RawCategory {
  id: string;
  items: RawLinkItem[];
}

const CATEGORY_META: Record<string, { name: string; blurb: string }> = {
  ai: {
    name: "AI & AI Engineering",
    blurb:
      "Foundational papers, agents, RAG, context engineering, evals and the open tools the field is actually built on.",
  },
  "local-ai": {
    name: "Local AI & Self-Hosting",
    blurb:
      "Ollama, llama.cpp, GGUF and the homelab stack that runs open weights on your own hardware.",
  },
  lowlevel: {
    name: "Low-Level & Homebrew Computing",
    blurb:
      "From silicon to syscalls — assembly, emulation, OS internals, retro machines and the boards people still solder.",
  },
  radio: {
    name: "Radio, SDR & Digital Comms",
    blurb:
      "Amateur radio, HF, digital modes, packet, LoRa mesh, SDR and the comms that survive the internet going dark.",
  },
  wildlife: {
    name: "Wildlife, Raptors & Falconry",
    blurb:
      "The goshawk shelf, falconry, ornithology and the wild places of Pakistan, AJK and the Himalayas.",
  },
  history: {
    name: "Kashmir & North-West History",
    blurb:
      "Primary sources, gazetteers and archives for the history of Kashmir and the lands adjoining the Indus.",
  },
  ownership: {
    name: "Digital Ownership & Preservation",
    blurb:
      "DRM, right to repair, abandonware, preservation and local-first software — owning your digital life.",
  },
  systems: {
    name: "Systems & Infrastructure",
    blurb:
      "Distributed systems, internet infrastructure and the boring machinery that keeps the pedal down.",
  },
  software: {
    name: "Programming & Software",
    blurb:
      "Languages, tools, books and craft for people who write code for a living.",
  },
  misc: {
    name: "Machines, Science & Rabbit Holes",
    blurb:
      "Robotics, science, heavy machinery, resilience and the internet's better rabbit holes.",
  },
};

const RAW: RawCategory[] = [
  { id: "ai", items: ai },
  { id: "local-ai", items: localAi },
  { id: "lowlevel", items: lowlevel },
  { id: "radio", items: radio },
  { id: "wildlife", items: wildlife },
  { id: "history", items: history },
  { id: "ownership", items: ownership },
  { id: "systems", items: systems },
  { id: "software", items: software },
  { id: "misc", items: misc },
];

export const CATEGORY_ORDER = Object.keys(CATEGORY_META);

function buildCategory(raw: RawCategory): LinkCategory {
  return {
    id: raw.id,
    name: CATEGORY_META[raw.id].name,
    blurb: CATEGORY_META[raw.id].blurb,
    items: raw.items.map((it, i) => ({
      ...it,
      id: `${raw.id}:${i}`,
      categoryId: raw.id,
      type: it.type as LinkType,
    })),
  };
}

export const CATEGORIES: LinkCategory[] = RAW.map(buildCategory);

export const ALL_LINKS: LinkItem[] = CATEGORIES.flatMap((c) => c.items);

export function categoryById(id: string): LinkCategory | undefined {
  return CATEGORIES.find((c) => c.id === id);
}

export function allTags(): string[] {
  const set = new Set<string>();
  for (const it of ALL_LINKS) for (const t of it.tags) set.add(t);
  return [...set].sort();
}

export function allSubcategories(categoryId: string): string[] {
  const set = new Set<string>();
  const cat = categoryById(categoryId);
  for (const it of cat?.items ?? []) if (it.subcategory) set.add(it.subcategory);
  return [...set].sort();
}

export function filterLinks(opts: {
  category?: string;
  type?: LinkType | "";
  subcategory?: string;
  query?: string;
}): LinkItem[] {
  const q = (opts.query ?? "").trim().toLowerCase();
  return ALL_LINKS.filter((it) => {
    if (opts.category && it.categoryId !== opts.category) return false;
    if (opts.type && it.type !== opts.type) return false;
    if (opts.subcategory && it.subcategory !== opts.subcategory) return false;
    if (!q) return true;
    return (
      it.title.toLowerCase().includes(q) ||
      it.description.toLowerCase().includes(q) ||
      it.tags.some((t) => t.includes(q))
    );
  });
}