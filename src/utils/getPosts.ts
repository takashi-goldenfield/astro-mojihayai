import type { Author, Post } from "@/types";
import config from "@/config";
import { type CollectionEntry, getCollection, getEntry } from "astro:content";
import transformTags from "./transformTags";
import transformCategory from "./transformCategory";
import { url } from "./url";
import getFileCreateTime from "./getFileCreateTime";
import getFileUpdateTime from "./getFileUpdateTime";
import { CONTENT_DIR, BLOG_COLLECTION_NAME as collection } from "@/constants";
import { CONTRIBUTORS_COLLECTION_NAME } from "@/constants";

function getPostPath(id: string) {
  let path = url(CONTENT_DIR, collection, id);
  if (path.startsWith("/")) {
    path = path.slice(1);
  }
  return path;
}

function countTags(posts: CollectionEntry<"blog">[]) {
  const bucket = new Map<string, number>();
  posts.map((post) => {
    for (const tag of post.data.tags) {
      bucket.set(tag, (bucket.get(tag) ?? 0) + 1);
    }
  });
  return bucket;
}

function countCategories(posts: CollectionEntry<"blog">[]) {
  const bucket = new Map<string, number>();
  posts.map((post) => {
    const category = post.data.category.join("/");
    bucket.set(category, (bucket.get(category) ?? 0) + 1);
  });
  return bucket;
}

function postUrl(slug: string) {
  return url("posts", slug);
}

function postPermalink(slug: string) {
  const length = slug.length;
  const trim = slug.substring(11, length);
  return url(trim);
}

let cache: Post[] | null = null;

async function getPosts(): Promise<Post[]> {
  if (cache !== null) {
    return cache;
  }
  const posts = await getCollection(collection);
  const contributors = await getCollection(CONTRIBUTORS_COLLECTION_NAME);
  const tagsBucket = countTags(posts);
  const categoriesBucket = countCategories(posts);

  cache = await Promise.all(
    posts.map(async (post) => {
      const { Content, headings, remarkPluginFrontmatter } =
        await post.render();
      const _author = contributors.find(contributor => contributor.id.replace('.md', '') === post.data.author.id) ?? {
        name: config.author,
      };
      const date = post.data.date ?? getFileCreateTime(getPostPath(post.id));
      const updateDate =
        post.data.updateDate ?? getFileUpdateTime(getPostPath(post.id));
      return {
        slug: post.data.permalink ?? post.slug,
        title: post.data.title ?? "Untitled",
        url: postUrl(post.slug),
        permalink: postPermalink(post.slug),
        author: _author as Author,
        image: post.data.image,
        date: post.data.date ?? date,
        updateDate: post.data.updateDate ?? updateDate,
        draft: post.data.draft,
        category: {
          ...transformCategory(post.data.category),
          count: categoriesBucket.get(post.data.category.join("/")) ?? 1,
        },
        tags: transformTags(post.data.tags).map((tag) => ({
          ...tag,
          count: tagsBucket.get(tag.label) ?? 1,
        })),
        cardVariant: post.data.cardVariant,
        raw: remarkPluginFrontmatter.raw,
        excerpt: remarkPluginFrontmatter.excerpt,
        readingTime: remarkPluginFrontmatter.readingTime,
        wordCount: remarkPluginFrontmatter.wordCount,
        headings: headings,
        Content: Content,
      };
    })
  );
  return cache;
}

export default getPosts;
