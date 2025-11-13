import { useEffect, useState } from 'react';
import { loadPosts, type Post } from '@/lib/content';
import PostCard from '@/components/PostCard';
import { Loader2 } from 'lucide-react';

export default function Home() {
  const [posts, setPosts] = useState<Post[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadPosts('noticias').then((data) => {
      setPosts(data);
      setLoading(false);
    });
  }, []);

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <Loader2 className="w-8 h-8 animate-spin text-primary neon-glow" />
      </div>
    );
  }

  return (
    <div className="container mx-auto px-4 py-12">
      <div className="mb-12">
        <h1 className="text-5xl font-bold mb-4">
          <span className="text-foreground">Noticias</span>
        </h1>
        <p className="text-lg text-muted-foreground">
          Últimas actualizaciones y <span className="neon-text font-semibold">novedades</span>
        </p>
      </div>

      {posts.length === 0 ? (
        <div className="neon-border rounded-lg p-12 text-center">
          <p className="text-muted-foreground">
            No hay noticias publicadas aún.
          </p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {posts.map((post) => (
            <PostCard key={post.metadata.slug} post={post} category="noticias" />
          ))}
        </div>
      )}
    </div>
  );
}
