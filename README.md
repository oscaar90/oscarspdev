# OscarAI - Sitio Personal

Sitio web personal minimalista con gestión de contenido mediante Markdown y Decap CMS.

## 🚀 Características

- **Diseño Minimalista**: Interfaz limpia y moderna con tonos azules suaves
- **Gestión de Contenido**: Decap CMS integrado para editar contenido desde VSCode o interfaz web
- **Markdown**: Todo el contenido se gestiona con archivos Markdown
- **Secciones**: Noticias, Writeups, Proyectos y Contacto
- **Responsive**: Diseño adaptable a todos los dispositivos
- **Header Fijo**: Navegación siempre visible al hacer scroll
- **Optimizado**: Build optimizado para producción

## 📁 Estructura del Proyecto

```
oscarai-tech/
├── client/
│   ├── public/
│   │   ├── content/          # Contenido en Markdown
│   │   │   ├── noticias/
│   │   │   ├── writeups/
│   │   │   └── proyectos/
│   │   └── admin/            # Decap CMS
│   │       ├── config.yml
│   │       └── index.html
│   └── src/
│       ├── components/       # Componentes React
│       ├── pages/           # Páginas
│       └── lib/             # Utilidades
├── scripts/
│   └── update-indexes.mjs   # Script para actualizar índices
├── netlify.toml             # Configuración de Netlify
└── package.json
```

## 🛠️ Desarrollo Local

### Requisitos

- Node.js 22+
- pnpm

### Instalación

```bash
# Instalar dependencias
pnpm install

# Iniciar servidor de desarrollo
pnpm dev
```

El sitio estará disponible en `http://localhost:3000`

## ✏️ Gestión de Contenido

### Opción 1: Editar archivos Markdown directamente

Los archivos de contenido están en `client/public/content/`:

- `noticias/` - Artículos de noticias
- `writeups/` - Writeups técnicos
- `proyectos/` - Proyectos

Cada archivo Markdown debe tener un frontmatter con metadatos:

```markdown
---
title: "Título del artículo"
date: "2024-01-15"
slug: "slug-del-articulo"
excerpt: "Descripción breve"
---

# Contenido

Tu contenido aquí...
```

**Importante**: Después de agregar o eliminar archivos, ejecuta:

```bash
pnpm update-indexes
```

### Opción 2: Usar Decap CMS

1. Accede a `/admin` en tu navegador
2. Configura Netlify Identity (solo en producción)
3. Edita contenido desde la interfaz visual

## 🏗️ Build para Producción

```bash
# Generar build de producción
npm run build
```

Este comando:
1. Actualiza automáticamente los índices de contenido
2. Genera los archivos optimizados en `client/dist/`

## 🚀 Despliegue en Netlify

### Configuración Inicial

1. **Conecta tu repositorio de GitHub** con Netlify
2. **Configuración de build**:
   - Build command: `npm run build`
   - Publish directory: `client/dist`
3. **Habilita Netlify Identity** (para Decap CMS):
   - Ve a Site settings → Identity
   - Habilita Identity
   - Configura Git Gateway

### Despliegue Automático

Cada push a la rama `main` desplegará automáticamente el sitio.

### Despliegue Manual

```bash
# Instalar Netlify CLI
npm install -g netlify-cli

# Deploy
netlify deploy --prod
```

## 📝 Agregar Nuevo Contenido

### Desde VSCode (Recomendado)

1. Crea un nuevo archivo `.md` en la carpeta correspondiente
2. Agrega el frontmatter con los metadatos
3. Escribe tu contenido en Markdown
4. Ejecuta `pnpm update-indexes`
5. Commit y push a GitHub

### Desde Decap CMS

1. Accede a `https://oscarai.tech/admin`
2. Inicia sesión con Netlify Identity
3. Crea nuevo contenido desde la interfaz
4. Publica

## 🎨 Personalización

### Colores

Los colores se definen en `client/src/index.css` usando variables CSS en formato OKLCH.

### Logo

Actualiza el logo en `client/src/const.ts`:

```typescript
export const APP_LOGO = "/ruta/a/tu/logo.png";
```

### Información de Contacto

Edita `client/src/pages/Contacto.tsx` con tus datos reales.

## 📦 Scripts Disponibles

- `pnpm dev` - Servidor de desarrollo
- `pnpm build` - Build de producción
- `pnpm preview` - Preview del build
- `pnpm update-indexes` - Actualizar índices de contenido
- `pnpm check` - Verificar tipos TypeScript
- `pnpm format` - Formatear código

## 🔧 Tecnologías

- **React 18** - Framework UI
- **TypeScript** - Tipado estático
- **Tailwind CSS 4** - Estilos
- **Wouter** - Enrutamiento
- **Decap CMS** - Gestión de contenido
- **Streamdown** - Renderizado de Markdown
- **Vite** - Build tool
- **Netlify** - Hosting y CI/CD

## 📄 Licencia

MIT
