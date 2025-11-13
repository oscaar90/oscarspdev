import { Link } from 'wouter';
import { formatDate, type Post } from '@/lib/content';
import { Calendar } from 'lucide-react';

interface PostCardProps {
  post: Post;
  category: string;
}

export default function PostCard({ post, category }: PostCardProps) {
  const { metadata } = post;

  return (
    <Link href={`/${category}/${metadata.slug}`}>
      <div className="neon-border rounded-lg p-6 bg-card hover:neon-glow transition-all cursor-pointer h-full group">
        <h3 className="text-xl font-semibold mb-3 text-foreground group-hover:text-primary transition-colors">
          {metadata.title}
        </h3>
        
        <div className="flex items-center gap-2 text-sm text-muted-foreground mb-4">
          <Calendar className="w-4 h-4" />
          {formatDate(metadata.date)}
        </div>
        
        {metadata.excerpt && (
          <p className="text-muted-foreground leading-relaxed">
            {metadata.excerpt}
          </p>
        )}
        
        {metadata.category && (
          <div className="mt-4">
            <span className="inline-block px-3 py-1 bg-primary/20 text-primary rounded-full text-xs font-medium border border-primary/40">
              {metadata.category}
            </span>
          </div>
        )}
        
        {metadata.tech && metadata.tech.length > 0 && (
          <div className="mt-4 flex flex-wrap gap-2">
            {metadata.tech.slice(0, 3).map((tech) => (
              <span
                key={tech}
                className="inline-block px-2 py-1 bg-primary/10 text-primary rounded text-xs border border-primary/30"
              >
                {tech}
              </span>
            ))}
          </div>
        )}
      </div>
    </Link>
  );
}
