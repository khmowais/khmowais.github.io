export const SITE = {
  name: "Khawaja M. Owais",
  shortName: "owais",
  url: "https://owais.qzz.io",
  description:
    "AI Engineer, systems builder, writer and amateur radio operator. I write about AI systems, local-first software, tools and technology.",
  author: "Khawaja M. Owais",
  locale: "en",
} as const;

export const GOSHAWK = {
  name: "Goshawk Labs",
  url: "https://goshawklabs.qzz.io",
  // Where Goshawk currently lives on the personal site. Change this constant
  // and the site builds independently once Goshawk moves to its own domain.
  basePath: "/goshawk-labs",
  description:
    "Goshawk Labs builds software, websites and AI systems that are simple, fast and built to last.",
} as const;

export const SOCIALS = {
  github: "https://github.com/khmowais",
  linkedin: "https://www.linkedin.com/in/the-mohammad-owais",
  email: "owais.a.khawaja@gmail.com",
} as const;

export const BRAND = {
  accent: "#ff4a1f",
  accentAlt: "#00c896",
  inkDark: "#0a0a0a",
  paper: "#f5f5ef",
} as const;