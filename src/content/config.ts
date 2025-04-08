import { z, defineCollection, reference } from "astro:content";

export const authors = defineCollection({
  type: "data",
  schema: ({ image }) =>
    z.object({
      name: z.string(),
      avatar: z.union([image(), z.string()]).optional(),
      description: z.string().optional(),
      background: z.union([image(), z.string()]).optional(),
      twitter: z.string().optional(),
      github: z.string().optional(),
      linkedin: z.string().optional(),
      website: z.string().optional(),
    }),
});

export const contributors = defineCollection({
  type: "content",
  schema: ({ image }) =>
    z.object({
      name: z.string(),
      avatar: z.union([image(), z.string()]).optional(),
      description: z.string().optional(),
      background: z.union([image(), z.string()]).optional(),
      twitter: z.string().optional(),
      github: z.string().optional(),
      linkedin: z.string().optional(),
      website: z.string().optional(),
      stackoverflow: z.string().optional(),
      devto: z.string().optional(),
      medium: z.string().optional(),
      youtube: z.string().optional(),
    }),
});

const blog = defineCollection({
  type: "content",
  schema: ({ image }) =>
    z
      .object({
        title: z.string(),
        image: z.union([image(), z.string()]).optional(),
        date: z.date().optional(),
        updateDate: z.date().optional(),
        draft: z.boolean().default(false),
        author: reference("authors").default("default"),
        excerpt: z.string().optional(),
        tags: z.string().array().default([]),
        category: z.string().array().default([]),
        permalink: z.string().optional(),
        cardVariant: z
          .enum(["blur", "material", "full", "plain"])
          .default("blur"),
      })
      .refine(
        (val) =>
          val.tags.every((item, index) => val.tags.indexOf(item) === index),
        (val) => ({
          message: `Tag "${val.tags.find((item, index) => val.tags.indexOf(item) !== index)}" is duplicated in post "${val.title}".`,
        })
      ),
});

export const friends = defineCollection({
  type: "data",
  schema: ({ image }) =>
    z.object({
      name: z.string(),
      link: z.string().url(),
      bgColor: z.string(),
      textColor: z.string(),
      avatar: z.union([image(), z.string()]),
      description: z.string(),
    }),
});

export const nft = defineCollection({
  type: "content",
  schema: ({ image }) =>
    z.object({
      name: z.string(),
      description: z.string(),
      image: z.union([image(), z.string()]),
      art: z.union([image(), z.string()]),
      external_url: z.string().url().optional(),
      artist: z.string().optional(),
      collection: z.string().optional(),
      conservation_status: z.string().optional(),
      attributes: z
        .array(
          z.object({
            trait_type: z.string(),
            value: z.string(),
          })
        )
        .optional(),
    }),
});

export const collections = {
  authors,
  blog,
  friends,
  contributors,
  nft,
};
