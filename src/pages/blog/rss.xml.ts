import rss from "@astrojs/rss";
import { getCollection } from "astro:content";
import { published, sortByDate } from "../../lib/posts";
import { SITE } from "../../config";

const posts = sortByDate(published(await getCollection("posts")));

export const GET = async () =>
  rss({
    title: `${SITE.name} — Blog`,
    description: SITE.description,
    site: SITE.url,
    items: posts.map((p) => ({
      title: p.data.title,
      description: p.data.description,
      pubDate: p.data.pubDate,
      link: `/blog/${p.id}/`,
    })),
    customData: `<language>en-us</language>`,
  });