import { compareDesc, getYear } from "date-fns";
import { Feed } from "feed";
import getPosts from "./getPosts";

interface RssFeedOptions {
  title: string;
  description?: string;
  site: string;
  author?: string;
  favicon?: string;
  format: "xml" | "json";
}

export default async function generateRssFeed(options: RssFeedOptions) {
  const { title, description, site, favicon, author, format } = options;
  const posts = (await getPosts())
    .filter((post) => !post.draft)
    .sort((a, b) => compareDesc(a.date, b.date));
  const feed = new Feed({
    title: title,
    description: description,
    id: new URL(site).href,
    link: new URL(site).href,
    language: "en-US",
    copyright: `Copyright © ${getYear(new Date())} ${author}`,
    image: favicon && new URL(favicon, site).href,
    favicon: favicon && new URL(favicon, site).href,
    updated: new Date(),
    author: {
      name: author,
    },
  });
  for (const post of posts) {
    let imageUrl: string | undefined;
    if (post.image) {
      if (typeof post.image === "string") {
        imageUrl = new URL(post.image, site).href;
      } else {
        const image = await post.image;
        imageUrl = new URL("default" in image ? image.default.src : image.src, site).href;
      }
    }
    feed.addItem({
      title: post.title,
      id: new URL(post.url, site).href,
      link: new URL(post.url, site).href,
      description: post.excerpt,
      date: post.date,
      content: post.raw,
      author: [{ name: post.author.name }],
      image: imageUrl,
    });
  }
  if (format === "xml") {
    return feed.rss2();
  }
  return feed.json1();
}
