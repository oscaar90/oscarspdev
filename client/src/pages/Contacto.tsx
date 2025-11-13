import { Mail, Github, Linkedin, Twitter } from 'lucide-react';

export default function Contacto() {
  return (
    <div className="container mx-auto px-4 py-12">
      <div className="mb-12">
        <h1 className="text-5xl font-bold mb-4">
          <span className="text-foreground">Con</span><span className="neon-text">tacto</span>
        </h1>
        <p className="text-lg text-muted-foreground">
          Conecta conmigo a través de <span className="neon-text font-semibold">estas plataformas</span>
        </p>
      </div>

      <div className="max-w-3xl mx-auto">
        <div className="neon-border rounded-lg p-8 bg-card">
          <h2 className="text-2xl font-bold mb-6 text-foreground">
            Información de <span className="neon-text">Contacto</span>
          </h2>
          
          <div className="space-y-6">
            <a
              href="mailto:contacto@oscarai.tech"
              className="flex items-center gap-4 p-4 rounded-lg hover:bg-accent transition-all group neon-border border-transparent hover:border-primary/40"
            >
              <div className="w-12 h-12 rounded-full bg-primary/20 flex items-center justify-center group-hover:neon-glow transition-all">
                <Mail className="w-6 h-6 text-primary" />
              </div>
              <div>
                <p className="font-semibold text-foreground group-hover:text-primary transition-colors">Email</p>
                <p className="text-sm text-muted-foreground">
                  contacto@oscarai.tech
                </p>
              </div>
            </a>

            <a
              href="https://github.com/oscarai"
              target="_blank"
              rel="noopener noreferrer"
              className="flex items-center gap-4 p-4 rounded-lg hover:bg-accent transition-all group neon-border border-transparent hover:border-primary/40"
            >
              <div className="w-12 h-12 rounded-full bg-primary/20 flex items-center justify-center group-hover:neon-glow transition-all">
                <Github className="w-6 h-6 text-primary" />
              </div>
              <div>
                <p className="font-semibold text-foreground group-hover:text-primary transition-colors">GitHub</p>
                <p className="text-sm text-muted-foreground">
                  github.com/oscarai
                </p>
              </div>
            </a>

            <a
              href="https://linkedin.com/in/oscarai"
              target="_blank"
              rel="noopener noreferrer"
              className="flex items-center gap-4 p-4 rounded-lg hover:bg-accent transition-all group neon-border border-transparent hover:border-primary/40"
            >
              <div className="w-12 h-12 rounded-full bg-primary/20 flex items-center justify-center group-hover:neon-glow transition-all">
                <Linkedin className="w-6 h-6 text-primary" />
              </div>
              <div>
                <p className="font-semibold text-foreground group-hover:text-primary transition-colors">LinkedIn</p>
                <p className="text-sm text-muted-foreground">
                  linkedin.com/in/oscarai
                </p>
              </div>
            </a>

            <a
              href="https://twitter.com/oscarai"
              target="_blank"
              rel="noopener noreferrer"
              className="flex items-center gap-4 p-4 rounded-lg hover:bg-accent transition-all group neon-border border-transparent hover:border-primary/40"
            >
              <div className="w-12 h-12 rounded-full bg-primary/20 flex items-center justify-center group-hover:neon-glow transition-all">
                <Twitter className="w-6 h-6 text-primary" />
              </div>
              <div>
                <p className="font-semibold text-foreground group-hover:text-primary transition-colors">Twitter</p>
                <p className="text-sm text-muted-foreground">
                  @oscarai
                </p>
              </div>
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}
