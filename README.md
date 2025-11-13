# 🚀 OscarAI Tech - JAMStack Blog

Un sitio web moderno construido con tecnologías JAMStack, diseño minimalista oscuro y efectos tech/cyberpunk.

## ✨ Stack Tecnológico

### Core
- **React 18** - Framework UI
- **Vite 7** - Build tool ultra rápido
- **TypeScript** - Tipado estático
- **TailwindCSS 4** - Estilos utility-first con Oklch
- **Wouter** - Routing ligero para SPA

### CMS & Contenido
- **Decap CMS v3** (anteriormente Netlify CMS) - Git-based CMS
- **Markdown** - Formato de contenido
- **Content Collections** - Sistema de índices JSON
- **Git Gateway** - Backend para Decap CMS

### Despliegue & CI/CD
- **Netlify** - Hosting y CDN
- **GitHub Actions** - CI/CD automático
- **Express** - Servidor Node.js para producción

### UI/UX
- **Radix UI** - Componentes accesibles
- **Framer Motion** - Animaciones
- **Lucide React** - Iconos
- **React Markdown** - Renderizado de markdown

## 🎨 Características del Diseño

### Tema Oscuro Tech/Cyberpunk
- Paleta de colores **Oklch** (espacio de color moderno)
- Fondo azul oscuro profundo: `oklch(0.14 0.015 240)`
- Acentos azul brillante: `oklch(0.7 0.15 230)`

### Efectos Visuales
- **Neón pulsante** - Bordes con animación de pulso
- **Glow effects** - Brillos suaves en hover
- **Text flicker** - Parpadeo estilo terminal retro
- **Tech grid** - Fondo de rejilla sutil
- **Scanlines** - Efecto CRT vintage
- **Terminal text** - Tipografía monoespaciada
- **Smooth transitions** - Transiciones fluidas

### Clases CSS Disponibles
```css
.neon-border      /* Bordes neón con pulso */
.neon-glow        /* Brillo neón animado */
.neon-text        /* Texto con efecto neón y flicker */
.tech-grid        /* Fondo de rejilla tech */
.scanlines        /* Efecto de líneas de escaneo */
.terminal-text    /* Texto estilo terminal */
.tech-link        /* Enlaces con animación de línea */
```

## 📁 Estructura del Proyecto

```
oscarspdev/
├── .github/
│   └── workflows/
│       └── ci.yml              # CI/CD con GitHub Actions
├── client/                     # Frontend
│   ├── public/
│   │   ├── admin/              # Decap CMS
│   │   │   ├── config.yml      # Configuración del CMS
│   │   │   └── index.html      # Panel de administración
│   │   ├── content/            # Contenido Markdown
│   │   │   ├── noticias/
│   │   │   ├── writeups/
│   │   │   └── proyectos/
│   │   └── images/             # Imágenes y uploads
│   ├── src/
│   │   ├── components/         # Componentes React
│   │   ├── contexts/           # Context providers (Theme)
│   │   ├── hooks/              # Custom hooks
│   │   ├── lib/                # Utilidades (content.ts)
│   │   ├── pages/              # Páginas de la app
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   └── index.css           # Estilos globales
│   └── index.html
├── server/
│   └── index.ts                # Servidor Express para producción
├── scripts/
│   └── update-indexes.mjs      # Genera índices JSON de contenido
├── netlify.toml                # Configuración de Netlify
├── vite.config.ts              # Configuración de Vite
└── package.json
```

## 🚀 Inicio Rápido

### Prerrequisitos
- Node.js 22+
- pnpm 10+

### Instalación

```bash
# Instalar dependencias
pnpm install

# Desarrollo local
pnpm dev

# Build para producción
pnpm build

# Preview del build
pnpm preview
```

## 📝 Uso del CMS

### Acceso al Panel de Administración
1. En desarrollo: `http://localhost:3000/admin`
2. En producción: `https://tu-dominio.com/admin`

### Desarrollo Local
El CMS está configurado con `local_backend: true` para desarrollo local:

```bash
# Terminal 1: Servidor de desarrollo
pnpm dev

# Terminal 2: Backend local del CMS
npx decap-server
```

### Colecciones Disponibles

#### 📰 Noticias
- Título
- Fecha
- Slug
- Extracto (opcional)
- Contenido (Markdown)

#### 📝 Writeups
- Título
- Fecha
- Slug
- Categoría (opcional)
- Dificultad: Easy/Medium/Hard (opcional)
- Extracto (opcional)
- Contenido (Markdown)

#### 🚀 Proyectos
- Título
- Fecha
- Slug
- Tecnologías (lista)
- Estado: En desarrollo/Completado/En pausa
- GitHub (URL)
- Extracto (opcional)
- Contenido (Markdown)

## 🎯 Content Collections

El sistema de contenido usa un enfoque híbrido:

1. **Archivos Markdown** en `/client/public/content/`
2. **Índices JSON** generados automáticamente
3. **Parser de frontmatter** manual para metadatos

### Ejemplo de Frontmatter

```markdown
---
title: "Mi Primer Post"
date: "2024-01-15"
slug: "mi-primer-post"
category: "Tutorial"
tech: ["React", "TypeScript", "Vite"]
excerpt: "Una breve descripción del post"
---

# Contenido

Tu contenido markdown aquí...
```

### Actualizar Índices Manualmente

```bash
pnpm update-indexes
```

Los índices se actualizan automáticamente en cada build.

## 🌐 Despliegue en Netlify

### Configuración Automática

El proyecto incluye `netlify.toml` con configuración optimizada:

- **Build command**: `npm run build`
- **Publish directory**: `dist/public`
- **Node version**: 22
- **Redirects**: Configurados para SPA
- **Headers**: Seguridad y cache optimizados

### Variables de Entorno

Si usas Netlify Identity para el CMS, no necesitas configurar variables adicionales. El `git-gateway` se configura automáticamente.

### Deploy Manual

```bash
# Instalar Netlify CLI
npm i -g netlify-cli

# Login
netlify login

# Deploy
netlify deploy --prod
```

## 🔄 CI/CD con GitHub Actions

El proyecto incluye un workflow de CI/CD que:

1. ✅ Ejecuta en push a `main` y branches `claude/**`
2. ✅ Setup de Node.js 22 y pnpm 10
3. ✅ Cache de dependencias
4. ✅ TypeScript type checking
5. ✅ Build del proyecto
6. ✅ Validación del output
7. ✅ Upload de artifacts

Netlify se conecta automáticamente a tu repositorio para deploys continuos.

## 🎨 Personalización del Diseño

### Colores Oklch

Los colores están definidos en `/client/src/index.css`:

```css
.dark {
  --background: oklch(0.14 0.015 240);     /* Fondo oscuro */
  --foreground: oklch(0.95 0.005 240);     /* Texto claro */
  --primary: oklch(0.7 0.15 230);          /* Azul brillante */
  --muted: oklch(0.2 0.02 240);            /* Gris oscuro */
  --border: oklch(0.7 0.15 230);           /* Borde azul */
}
```

### Cambiar Colores Primarios

Para cambiar el esquema de color, modifica los valores Oklch en las variables CSS. Usa [Oklch Color Picker](https://oklch.com/) para explorar colores.

### Tipografía

El proyecto usa **Inter** como fuente principal. Para cambiar:

```css
body {
  font-family: 'Tu-Fuente', system-ui, sans-serif;
}
```

## 📊 Scripts Disponibles

```bash
pnpm dev              # Servidor de desarrollo (puerto 3000)
pnpm build            # Build de producción + índices
pnpm start            # Ejecutar en producción
pnpm preview          # Preview del build local
pnpm check            # TypeScript type checking
pnpm format           # Formatear código con Prettier
pnpm update-indexes   # Actualizar índices de contenido
```

## 🔒 Seguridad

Headers de seguridad configurados en Netlify:

- `X-Frame-Options: DENY`
- `X-XSS-Protection: 1; mode=block`
- `X-Content-Type-Options: nosniff`
- `Referrer-Policy: strict-origin-when-cross-origin`

## 📦 Optimizaciones

### Build
- Code splitting automático con Vite
- Tree shaking
- Minificación
- Optimización de assets

### Cache
- Assets estáticos: `max-age=31536000, immutable`
- Imágenes: Cache de 1 año
- HTML: No cacheado para SPA routing

### Performance
- Lazy loading de componentes
- Optimización de imágenes
- Preload de recursos críticos

## 🤝 Contribuir

1. Fork el repositorio
2. Crea una branch: `git checkout -b feature/mi-feature`
3. Commit: `git commit -am 'Add: nueva funcionalidad'`
4. Push: `git push origin feature/mi-feature`
5. Crea un Pull Request

## 📄 Licencia

MIT License - Ver archivo LICENSE para más detalles.

## 🙏 Agradecimientos

- [Decap CMS](https://decapcms.org/) - Git-based CMS
- [TailwindCSS](https://tailwindcss.com/) - Framework CSS
- [Radix UI](https://www.radix-ui.com/) - Componentes primitivos
- [Netlify](https://www.netlify.com/) - Hosting y deployment
- [Vite](https://vitejs.dev/) - Build tool

---

Hecho con ❤️ usando tecnologías JAMStack modernas
