import { Link, useLocation } from 'wouter';
import { APP_TITLE } from '@/const';

export default function Header() {
  const [location] = useLocation();

  const navItems = [
    { path: '/', label: 'Noticias' },
    { path: '/writeups', label: 'Writeups' },
    { path: '/proyectos', label: 'Proyectos' },
    { path: '/contacto', label: 'Contacto' },
  ];

  return (
    <header className="fixed top-0 left-0 right-0 z-50 bg-background/95 backdrop-blur-md border-b border-primary/30">
      <nav className="container mx-auto px-4 h-16 flex items-center justify-between">
        <Link href="/" className="text-xl font-bold text-foreground hover:text-primary transition-colors">
          <span className="neon-text">{APP_TITLE}</span>
        </Link>
        
        <ul className="flex items-center gap-6">
          {navItems.map((item) => (
            <li key={item.path}>
              <Link
                href={item.path}
                className={`text-sm font-medium transition-all hover:text-primary ${
                  location === item.path
                    ? 'text-primary neon-text'
                    : 'text-muted-foreground'
                }`}
              >
                {item.label}
              </Link>
            </li>
          ))}
        </ul>
      </nav>
    </header>
  );
}
