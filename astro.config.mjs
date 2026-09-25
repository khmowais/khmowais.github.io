import { defineConfig } from "astro/config";
import mdx from "@astrojs/mdx";
import sitemap from "@astrojs/sitemap";

export default defineConfig({
  site: "https://owais.qzz.io",
  output: "static",
  trailingSlash: "ignore",

  integrations: [mdx(), sitemap()],

  markdown: {
    shikiConfig: {
      theme: "github-dark",
      wrap: true,
    },
  },

  vite: {
    server: {
      host: "0.0.0.0",
      port: 8080,
      allowedHosts: [".trycloudflare.com"]

    },
  },
});