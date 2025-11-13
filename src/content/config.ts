import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    publishDate: z.coerce.date(),
    tags: z.array(z.string()).default([]),
    category: z.enum(['ctf', 'automation', 'ai', 'cybersecurity', 'tools']),
    type: z.enum(['project', 'post', 'created-ctf']).default('post'),
    difficulty: z.enum(['easy', 'medium', 'hard']).optional(),
    heroImage: z.string().optional(),
    draft: z.boolean().default(false),
    readingTime: z.string().optional(),
  }),
});

export const collections = { blog };