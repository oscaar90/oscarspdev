import { useEffect, useState } from 'react';
import { useRoute, useLocation } from 'wouter';
import { loadPost, formatDate, type Post } from '@/lib/content';
import { Loader2, Calendar, ArrowLeft } from 'lucide-react';
import { Button } from '@/components/ui/button';
import ReactMarkdown from 'react-markdown';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { oneDark } from 'react-syntax-highlighter/dist/esm/styles/prism';

interface PostDetailProps {
  category: string;
}

export default function PostDetail({ category }: PostDetailProps) {
  const [, params] = useRoute('/:category/:slug');
  const [, setLocation] = useLocation();
  const [post, setPost] = useState<Post | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (params?.slug) {
      loadPost(category, params.slug).then((data) => {
        setPost(data);
        setLoading(false);
      });
    }
  }, [params?.slug, category]);

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <Loader2 className="w-8 h-8 animate-spin text-primary neon-glow" />
      </div>
    );
  }

  if (!post) {
    return (
      <div className="container mx-auto px-4 py-8">
        <div className="neon-border rounded-lg p-12 text-center">
          <p className="text-muted-foreground">Post no encontrado</p>
        </div>
      </div>
    );
  }

  return (
    <div className="container mx-auto px-4 py-12">
      <Button
        variant="ghost"
        className="mb-8 hover:text-primary transition-colors"
        onClick={() => setLocation(`/${category === 'noticias' ? '' : category}`)}
      >
        <ArrowLeft className="w-4 h-4 mr-2" />
        Volver
      </Button>

      <article className="max-w-4xl mx-auto">
        <div className="neon-border rounded-lg p-8 lg:p-12 bg-card">
          <header className="mb-10">
            <h1 className="text-4xl lg:text-5xl font-bold mb-6">
              {post.metadata.title}
            </h1>
            
            <div className="flex flex-wrap items-center gap-4 text-sm">
              <div className="flex items-center gap-2 text-muted-foreground">
                <Calendar className="w-4 h-4" />
                {formatDate(post.metadata.date)}
              </div>
              
              {post.metadata.category && (
                <span className="px-3 py-1 bg-primary/20 text-primary rounded-full text-xs font-medium border border-primary/40 neon-glow">
                  {post.metadata.category}
                </span>
              )}
              
              {post.metadata.difficulty && (
                <span className="px-3 py-1 bg-accent text-accent-foreground rounded-full text-xs font-medium border border-primary/30">
                  {post.metadata.difficulty}
                </span>
              )}
            </div>
          </header>

          <div className="prose prose-lg prose-invert max-w-none">
            <ReactMarkdown
              components={{
                code(props) {
                  const { children, className, ...rest } = props;
                  const match = /language-(\w+)/.exec(className || '');
                  return match ? (
                    <SyntaxHighlighter
                      style={oneDark}
                      language={match[1]}
                      PreTag="div"
                    >
                      {String(children).replace(/\n$/, '')}
                    </SyntaxHighlighter>
                  ) : (
                    <code className={className} {...rest}>
                      {children}
                    </code>
                  );
                },
              }}
            >
              {post.content}
            </ReactMarkdown>
          </div>

          {post.metadata.tech && post.metadata.tech.length > 0 && (
            <div className="mt-10 pt-8 border-t border-primary/30">
              <h3 className="text-lg font-semibold mb-4">
                <span className="neon-text">Tecnologías</span>
              </h3>
              <div className="flex flex-wrap gap-3">
                {post.metadata.tech.map((tech) => (
                  <span
                    key={tech}
                    className="px-4 py-2 bg-primary/10 text-primary rounded-lg text-sm font-medium border border-primary/30 hover:neon-glow transition-all"
                  >
                    {tech}
                  </span>
                ))}
              </div>
            </div>
          )}

          {post.metadata.github && (
            <div className="mt-6">
              <a
                href={post.metadata.github}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-2 text-primary hover:underline font-medium neon-text"
              >
                Ver en GitHub →
              </a>
            </div>
          )}
        </div>
      </article>
    </div>
  );
}
