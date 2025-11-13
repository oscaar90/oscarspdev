// Utilidades para cargar y procesar contenido Markdown

export interface PostMetadata {
  title: string;
  date: string;
  slug: string;
  excerpt?: string;
  category?: string;
  difficulty?: string;
  tech?: string[];
  status?: string;
  github?: string;
}

export interface Post {
  metadata: PostMetadata;
  content: string;
  rawContent: string;
}

// Función para parsear frontmatter y contenido
export function parseMarkdown(markdown: string): Post {
  const frontmatterRegex = /^---\n([\s\S]*?)\n---\n([\s\S]*)$/;
  const match = markdown.match(frontmatterRegex);

  if (!match) {
    return {
      metadata: {
        title: 'Sin título',
        date: new Date().toISOString(),
        slug: 'sin-slug',
      },
      content: markdown,
      rawContent: markdown,
    };
  }

  const frontmatter = match[1];
  const content = match[2];

  // Parsear frontmatter manualmente
  const metadata: any = {};
  frontmatter.split('\n').forEach((line) => {
    const colonIndex = line.indexOf(':');
    if (colonIndex > -1) {
      const key = line.substring(0, colonIndex).trim();
      let value: any = line.substring(colonIndex + 1).trim();
      
      // Remover comillas
      if (value.startsWith('"') && value.endsWith('"')) {
        value = value.slice(1, -1);
      }
      
      // Parsear arrays
      if (value.startsWith('[') && value.endsWith(']')) {
        value = value
          .slice(1, -1)
          .split(',')
          .map((v: string) => v.trim().replace(/"/g, ''));
      }
      
      metadata[key] = value;
    }
  });

  return {
    metadata: metadata as PostMetadata,
    content,
    rawContent: markdown,
  };
}

// Función para cargar un post individual
export async function loadPost(category: string, slug: string): Promise<Post | null> {
  try {
    const response = await fetch(`/content/${category}/${slug}.md`);
    if (!response.ok) return null;
    const markdown = await response.text();
    return parseMarkdown(markdown);
  } catch (error) {
    console.error(`Error loading post ${category}/${slug}:`, error);
    return null;
  }
}

// Función para cargar todos los posts de una categoría
export async function loadPosts(category: string): Promise<Post[]> {
  // En un sitio estático, necesitamos mantener un índice de posts
  // Este será generado por Decap CMS o manualmente
  try {
    const response = await fetch(`/content/${category}/index.json`);
    if (!response.ok) return [];
    
    const slugs: string[] = await response.json();
    const posts = await Promise.all(
      slugs.map((slug) => loadPost(category, slug))
    );
    
    return posts
      .filter((post): post is Post => post !== null)
      .sort((a, b) => new Date(b.metadata.date).getTime() - new Date(a.metadata.date).getTime());
  } catch (error) {
    console.error(`Error loading posts for category ${category}:`, error);
    return [];
  }
}

// Función para formatear fecha
export function formatDate(dateString: string): string {
  const date = new Date(dateString);
  return date.toLocaleDateString('es-ES', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  });
}
