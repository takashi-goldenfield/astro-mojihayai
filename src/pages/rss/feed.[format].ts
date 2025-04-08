import type { APIRoute, GetStaticPaths } from "astro";
import generateRssFeed from "@/utils/generateRSSFeed";
import config from "@/config";

export const GET: APIRoute = async ({ params, site }) => {
  if (!site) {
    return new Response();
  }
  const format = params.format as "xml" | "json";

  return new Response(
    await generateRssFeed({
      title: config.title,
      description: config.description,
      site: site.href,
      author: config.author,
      favicon: config.favicon,
      format: format,
    })
  );
};

export const getStaticPaths = (() => {
  return [{ params: { format: "xml" } }, { params: { format: "json" } }];
}) satisfies GetStaticPaths;
