# Configuración para Desarrollo Local

Este documento explica cómo configurar el proyecto después de descargarlo desde Manus.

## Requisitos Previos

- **Node.js 22+**
- **pnpm** (recomendado) o npm

## Instalación

### 1. Instalar Dependencias

**Con pnpm (recomendado):**
```bash
pnpm install
```

**Con npm:**
```bash
npm install --legacy-peer-deps
```

> **Nota**: Si usas npm, necesitas el flag `--legacy-peer-deps` debido a conflictos de versiones de peer dependencies en Decap CMS.

### 2. Configurar Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```env
# Información de la aplicación
VITE_APP_TITLE="OscarAI - Sitio Personal"
VITE_APP_LOGO="/logo.png"

# Analytics (opcional - puedes dejar vacío para desarrollo local)
VITE_ANALYTICS_ENDPOINT=""
VITE_ANALYTICS_WEBSITE_ID=""

# ID de la aplicación
VITE_APP_ID="oscarai-tech"
```

### 3. Iniciar Servidor de Desarrollo

**Con pnpm:**
```bash
pnpm dev
```

**Con npm:**
```bash
npm run dev
```

El sitio estará disponible en `http://localhost:3000`

## Solución de Problemas

### Error: "vite: orden no encontrada"

Asegúrate de haber instalado las dependencias primero:
```bash
pnpm install
# o
npm install --legacy-peer-deps
```

### Warnings sobre variables de entorno no definidas

Crea el archivo `.env` como se indica en el paso 2.

### Error ERESOLVE con npm

Usa el flag `--legacy-peer-deps`:
```bash
npm install --legacy-peer-deps
```

O mejor aún, usa **pnpm** que maneja mejor las dependencias:
```bash
npm install -g pnpm
pnpm install
```

## Gestión de Contenido

### Agregar Nuevo Contenido

1. Crea un archivo `.md` en la carpeta correspondiente:
   - `client/public/content/noticias/`
   - `client/public/content/writeups/`
   - `client/public/content/proyectos/`

2. Actualiza los índices:
```bash
pnpm update-indexes
# o
npm run update-indexes
```

### Usar Decap CMS Localmente

Para usar Decap CMS en desarrollo local, necesitas configurar el backend local:

1. Accede a `http://localhost:3000/admin`
2. El CMS funcionará en modo local (configurado en `config.yml`)

## Build para Producción

```bash
pnpm build
# o
npm run build
```

Los archivos generados estarán en `client/dist/`

## Despliegue en Netlify

1. Sube el proyecto a GitHub
2. Conecta tu repositorio en Netlify
3. Netlify detectará automáticamente la configuración de `netlify.toml`
4. Las variables de entorno se configurarán automáticamente en Netlify

Para más información, consulta el archivo `README.md` principal.
