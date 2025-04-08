import type { Config } from "./types";
import { getYear } from "date-fns";
import { url } from "@/utils/url";
import * as Author from "@/content/authors/default.json";

const config: Config = {
  title: "Moji Express",
  description:
    "Content that helps beginners and experienced enthusiasts alike understand the fundamentals of Bitcoin and blockchain technology.",
  author: Author.name,
  favicon: url("favicon.ico"),
  navbar: {
    logo: import("@/custom/NavLogo.astro"),
    menu: [
      {
        label: "Home",
        url: url("/"),
        icon: "tabler:home",
      },
      {
        label: "Tags",
        url: url("/tags"),
        icon: "tabler:tag",
      },
      {
        label: "Labels",
        url: url("/categories"),
        icon: "tabler:category",
      },
      {
        label: "Posts",
        url: url("/archive"),
        icon: "tabler:archive",
      },
      {
        label: "Authors",
        url: url("/authors"),
        icon: "tabler:users",
      },
      {
        label: "NFT",
        url: url("/nft"),
        icon: "tabler:heart-handshake",
      },
      {
        label: "About",
        url: url("/about"),
        icon: "tabler:info-circle",
      },
    ],
    hasSearchToggle: true,
    hasThemeToggle: true,
    hasWagmiToggle: true,
  },
  hero: {
    background: import("src/assets/hero-bg.webp"),
    description:
      "Welcome to the Moji Express, let’s see what I have been doing recently.",
    title: import("@/custom/MojiExpress.astro"),
  },
  sidebar: {
    widgets: [
      {
        name: "profile",
        author: Author.name,
        description: Author.description,
        avatar: import("public/assets/avatar.png"),
        background: import("src/assets/field.webp"),
        socialIcons: [
          {
            label: "github",
            color: "#7c8690",
            icon: "tabler:brand-github",
            url: "https://github.com/takashi-goldenfield",
          },
          {
            label: "bilibili",
            color: "#fc87b2",
            icon: "tabler:brand-bilibili",
            url: "https://space.bilibili.com/293591084",
          },
          {
            label: "netease music",
            color: "#ff4e6a",
            icon: "tabler:brand-netease-music",
            url: "https://music.163.com/user/390631653",
          },
          {
            label: "twitter",
            color: "#1d9bf0",
            icon: "tabler:brand-twitter",
            url: "https://twitter.com/vviderx",
          },
          {
            label: "mail",
            color: "#7562c7",
            icon: "tabler:mail",
            url: "mailto:meocona16@gmail.com",
          },
        ],
      },
      {
        name: "tag-cloud",
        sortBy: "count",
        order: "desc",
        limit: 30,
      },
      {
        name: "category-tree",
        sortBy: "count",
        order: "desc",
        expandDepth: 2,
      },
      {
        name: "component",
        component: import("@/components/Custom/Recommend.astro"),
      },
    ],
  },
  pagination: {
    itemLimit: 128,
    pageSize: 20,
    hasControls: true,
    hasEdges: false,
    siblings: 2,
    boundaries: 1,
  },
  article: {
    outdateTip: {
      outdateLimit: 180,
    },
    license: {
      licenseName: "CC BY-NC-SA 4.0",
      licenseUrl: "https://creativecommons.org/licenses/by-nc-sa/4.0/",
      infoText:
        "Please indicate the author and source when reprinting or quoting this article. It may not be used for commercial purposes.",
    },
  },
  comment: {
    provider: "giscus",
    options: {
      repo: "takashi-goldenfield/astro-mojihayai",
      repoId: "R_kgDOOHbPbQ",
      category: "General",
      categoryId: "DIC_kwDOOHbPbc4Cn6n2",
      mapping: "pathname",
      reactionsEnabled: "1",
      emitMetadata: "0",
      inputPosition: "top",
      lang: "en-US",
    },
  },
  footer: {
    links: [
      { label: "Changelog", url: url("changelog") },
      { label: "Reference", url: url("reference") },
      { label: "About", url: url("about") },
      { label: "Posts", url: url("archive") },
      { label: "Authors", url: url("authors") },
      { label: "Friends", url: url("friends") },
      { label: "Github", url: "https://github.com/takashi-goldenfield" },
    ],
    declarations: [
      `Copyright © ${getYear(new Date())} Moji Express All Rights Reserved.`,
    ],
    generator: true,
    rss: true,
    sitemap: true,
  },
  algolia: {
    appId: "1IIXBX6FGH",
    apiKey: "91aa4234096f4963e33d53262340b1ec",
    indexName: "wider",
  },
};

export default config;
