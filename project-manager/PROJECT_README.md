# 📋 Project Manager - Gestión de Proyectos Personales

Sistema completo de gestión de proyectos personales con backend FastAPI, frontend Astro, integración con Telegram, webhooks para n8n, funciones de IA internas y sincronización automática.

## 🚀 Características

### Backend (FastAPI)
- ✅ API REST completa con endpoints CRUD
- ✅ Base de datos SQLite (compatible con PostgreSQL)
- ✅ Modelos: Proyecto, Nota, Adjunto, Etiqueta, WebhookEvent
- ✅ Sistema de estados: idea, prototipo, en_progreso, bloqueado, pausado, completado, archivado
- ✅ Webhooks automáticos para n8n (eventos de proyecto)
- ✅ Middleware CORS configurable
- ✅ Validación con Pydantic

### Frontend (Astro)
- ✅ Vista Kanban organizada por estados
- ✅ Vista de lista con filtros y búsqueda
- ✅ Formulario de creación de proyectos
- ✅ Página de detalle con edición
- ✅ Diseño minimalista y responsivo

### Integraciones
- ✅ Bot de Telegram integrado
- ✅ Sistema de webhooks para n8n
- ✅ CLI en Python para operaciones rápidas
- ✅ Backup automático diario
- ✅ Sincronización opcional con GitHub

### Funciones IA Internas
- ✅ Clustering de ideas por similitud
- ✅ Generación automática de resúmenes
- ✅ Extracción de palabras clave
- ✅ Generación de roadmap/checklist automático

---

## 📁 Estructura del Proyecto

```
project-manager/
├── backend/                    # API FastAPI
│   ├── app/
│   │   ├── models/            # Modelos SQLAlchemy
│   │   ├── schemas/           # Esquemas Pydantic
│   │   ├── routers/           # Endpoints de la API
│   │   ├── services/          # Lógica de negocio
│   │   ├── utils/             # Utilidades (IA, helpers)
│   │   ├── database.py        # Configuración de BD
│   │   └── main.py            # Aplicación principal
│   ├── requirements.txt       # Dependencias Python
│   └── .env.example          # Variables de entorno
│
├── frontend-pm/               # Frontend Astro
│   ├── src/
│   │   ├── layouts/          # Layouts de páginas
│   │   ├── pages/            # Páginas (index, kanban, lista, etc)
│   │   ├── components/       # Componentes reutilizables
│   │   └── lib/              # Cliente API
│   ├── package.json
│   └── astro.config.mjs
│
├── cli/                       # Scripts CLI
│   └── pm_cli.py             # Interfaz de línea de comandos
│
├── scripts/                   # Scripts de automatización
│   ├── backup.py             # Sistema de backups
│   ├── sync_github.py        # Sincronización con GitHub
│   └── setup_cron.sh         # Configuración de cron jobs
│
├── backups/                   # Backups de la base de datos
├── logs/                      # Logs de sistema
└── docs/                      # Documentación adicional
```

---

## 🔧 Instalación

### Requisitos
- Python 3.9+
- Node.js 18+
- Git

### 1. Backend FastAPI

```bash
# Navegar al directorio backend
cd project-manager/backend

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Editar .env según tus necesidades

# Inicializar base de datos y ejecutar
python -m app.main
```

El backend estará disponible en `http://localhost:8000`

Documentación interactiva: `http://localhost:8000/docs`

### 2. Frontend Astro

```bash
# Navegar al directorio frontend
cd project-manager/frontend-pm

# Instalar dependencias
npm install

# Ejecutar en modo desarrollo
npm run dev
```

El frontend estará disponible en `http://localhost:3000`

---

## 📚 Uso de la API

### Endpoints Principales

#### Proyectos
```bash
# Listar proyectos
GET /projects?estado=idea&prioridad_min=5&search=texto

# Obtener proyecto por ID
GET /projects/{id}

# Crear proyecto
POST /projects
{
  "titulo": "Mi Proyecto",
  "descripcion": "Descripción del proyecto",
  "estado": "idea",
  "prioridad": 5,
  "checklist": [
    {"texto": "Tarea 1", "completado": false}
  ]
}

# Actualizar proyecto
PUT /projects/{id}
{
  "estado": "en_progreso",
  "prioridad": 8
}

# Eliminar proyecto
DELETE /projects/{id}

# Agregar etiqueta a proyecto
POST /projects/{proyecto_id}/etiquetas/{etiqueta_id}
```

#### Notas
```bash
# Crear nota
POST /notes
{
  "proyecto_id": 1,
  "titulo": "Nota importante",
  "contenido": "Contenido de la nota"
}

# Listar notas de un proyecto
GET /notes?proyecto_id=1
```

#### Adjuntos
```bash
# Crear adjunto
POST /attachments
{
  "proyecto_id": 1,
  "nombre": "Documento.pdf",
  "ruta": "/ruta/al/archivo.pdf",
  "tipo": "document"
}
```

#### Etiquetas
```bash
# Crear etiqueta
POST /tags
{
  "nombre": "importante",
  "color": "#FF5733"
}

# Listar etiquetas
GET /tags
```

#### Webhooks
```bash
# Listar eventos webhook
GET /webhooks

# Reenviar webhook fallido
POST /webhooks/{id}/reenviar
```

#### Health Check
```bash
GET /health
```

---

## 🤖 Bot de Telegram

### Configuración

1. Crear bot con [@BotFather](https://t.me/botfather)
2. Obtener el token
3. Configurar en `.env`:
```env
TELEGRAM_BOT_TOKEN=tu_token_aqui
```

### Comandos Disponibles

```
/start              - Mensaje de bienvenida
/nuevo <texto>      - Crear proyecto con estado "idea"
/lista              - Ver proyectos activos
/estado <ID> <estado> - Actualizar estado de proyecto

Ejemplo:
/nuevo Desarrollar aplicación móvil
/estado 1 en_progreso
```

---

## 🔗 Integración con n8n

### Configuración de Webhooks

1. Crear workflow en n8n
2. Agregar nodo "Webhook"
3. Copiar la URL del webhook
4. Configurar en `.env`:
```env
N8N_WEBHOOK_URL=https://tu-n8n.com/webhook/...
```

### Eventos Disponibles

El sistema envía webhooks automáticamente para:

- **proyecto_creado**: Cuando se crea un proyecto
- **estado_cambiado**: Cuando cambia el estado de un proyecto
- **proyecto_completado**: Cuando un proyecto se marca como completado
- **proyecto_archivado**: Cuando un proyecto se archiva

### Payload de Ejemplo

```json
{
  "proyecto_id": 1,
  "titulo": "Mi Proyecto",
  "estado": "completado",
  "estado_anterior": "en_progreso"
}
```

---

## 💻 CLI - Interfaz de Línea de Comandos

### Agregar Proyecto
```bash
cd project-manager/cli
python pm_cli.py agregar "Nombre del proyecto" \
  -d "Descripción detallada" \
  -e idea \
  -p 5
```

### Listar Proyectos
```bash
# Todos los proyectos
python pm_cli.py listar

# Filtrar por estado
python pm_cli.py listar -e en_progreso

# Limitar resultados
python pm_cli.py listar -l 20
```

### Cambiar Estado
```bash
python pm_cli.py estado 1 completado
```

### Exportar a Markdown
```bash
# Exportar todos
python pm_cli.py exportar

# Exportar solo un estado
python pm_cli.py exportar -e completado

# Especificar archivo de salida
python pm_cli.py exportar -o mis_proyectos.md
```

---

## 💾 Sistema de Backup

### Backup Manual
```bash
cd project-manager/scripts
python backup.py crear
```

### Listar Backups
```bash
python backup.py listar
```

### Restaurar Backup
```bash
python backup.py restaurar -f project_manager_backup_20240101_120000.db
```

### Backup Automático (Cron)

```bash
# Configurar cron jobs
cd project-manager/scripts
chmod +x setup_cron.sh
./setup_cron.sh
```

Esto configura:
- Backup diario a las 2:00 AM
- Sincronización con GitHub cada 6 horas (opcional)

---

## 🔄 Sincronización con GitHub

### Configuración

1. Inicializar repositorio Git
```bash
cd project-manager
git init
git remote add origin https://github.com/usuario/repo.git
```

2. Configurar en `.env`:
```env
GITHUB_SYNC_ENABLED=true
```

### Sincronización Manual
```bash
cd scripts
python sync_github.py sync -m "Mensaje del commit"
```

### Verificar Estado
```bash
python sync_github.py status
```

### Sincronización Automática

El script `setup_cron.sh` puede configurar sincronización automática cada 6 horas.

---

## 🧠 Funciones de IA

Las funciones de IA están integradas en el backend y se pueden usar programáticamente:

```python
from app.utils.ia_helpers import (
    clustering_ideas,
    generar_resumen,
    extraer_palabras_clave,
    generar_roadmap
)

# Clustering de proyectos similares
proyectos = [{"titulo": "...", "descripcion": "..."}]
clusters = clustering_ideas(proyectos)

# Generar resumen
resumen = generar_resumen(texto_largo, max_palabras=50)

# Extraer palabras clave
keywords = extraer_palabras_clave(texto, top_n=5)

# Generar roadmap automático
roadmap = generar_roadmap("Desarrollar app móvil", "Aplicación para gestión de tareas")
```

---

## 🎨 Frontend - Vistas

### Vista Kanban (`/kanban`)
- Tablero organizado por estados
- Drag & drop entre columnas (próximamente)
- Vista rápida de todos los proyectos

### Vista Lista (`/lista`)
- Lista completa con filtros
- Búsqueda por texto
- Filtros por estado y prioridad
- Ordenamiento por prioridad

### Nuevo Proyecto (`/nuevo`)
- Formulario de creación
- Agregar checklist dinámico
- Selección de estado y prioridad

### Detalle de Proyecto (`/proyecto/{id}`)
- Información completa
- Editar estado
- Ver checklist
- Gestionar etiquetas

---

## 🔐 Variables de Entorno

### Backend `.env`
```env
# Base de datos
DATABASE_TYPE=sqlite
# DATABASE_URL=postgresql://user:password@localhost/project_manager

# CORS
CORS_ORIGINS=http://localhost:3000,http://127.0.0.1:3000

# n8n
N8N_WEBHOOK_URL=https://tu-n8n.com/webhook/...

# Telegram
TELEGRAM_BOT_TOKEN=123456:ABC-DEF...

# GitHub Sync
GITHUB_SYNC_ENABLED=false
```

### Frontend `.env` (opcional)
```env
PUBLIC_API_URL=http://localhost:8000
```

---

## 🚦 Estados de Proyecto

| Estado | Descripción | Badge |
|--------|-------------|-------|
| **idea** | Proyecto en fase de idea | 💡 |
| **prototipo** | Prototipo en desarrollo | 🔬 |
| **en_progreso** | Activamente en desarrollo | 🚀 |
| **bloqueado** | Bloqueado por algún impedimento | 🚫 |
| **pausado** | Temporalmente pausado | ⏸️ |
| **completado** | Proyecto completado | ✅ |
| **archivado** | Archivado para referencia | 📦 |

---

## 📊 Ejemplos de Requests

### Crear Proyecto con Checklist
```bash
curl -X POST http://localhost:8000/projects \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Desarrollar API REST",
    "descripcion": "API para gestión de usuarios",
    "estado": "idea",
    "prioridad": 7,
    "checklist": [
      {"texto": "Diseñar endpoints", "completado": false},
      {"texto": "Implementar autenticación", "completado": false},
      {"texto": "Escribir tests", "completado": false}
    ]
  }'
```

### Actualizar Estado
```bash
curl -X PUT http://localhost:8000/projects/1 \
  -H "Content-Type: application/json" \
  -d '{"estado": "en_progreso"}'
```

### Buscar Proyectos
```bash
curl "http://localhost:8000/projects?search=API&prioridad_min=5"
```

---

## 🛠️ Desarrollo

### Ejecutar Backend en Modo Desarrollo
```bash
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Ejecutar Frontend en Modo Desarrollo
```bash
cd frontend-pm
npm run dev
```

### Ejecutar Ambos (en terminales separadas)
```bash
# Terminal 1 - Backend
cd backend && python -m app.main

# Terminal 2 - Frontend
cd frontend-pm && npm run dev
```

---

## 📝 Notas Adicionales

### Migración a PostgreSQL

Para usar PostgreSQL en lugar de SQLite:

1. Instalar PostgreSQL
2. Crear base de datos:
```sql
CREATE DATABASE project_manager;
```

3. Actualizar `.env`:
```env
DATABASE_TYPE=postgresql
DATABASE_URL=postgresql://usuario:password@localhost/project_manager
```

### Despliegue en Producción

#### Backend
- Usar gunicorn o uvicorn con workers
- Configurar HTTPS
- Usar PostgreSQL
- Configurar backups automáticos

#### Frontend
```bash
npm run build
```
Servir carpeta `dist/` con nginx o servicio estático

---

## 🤝 Contribuciones

Este es un proyecto personal de gestión. Para mejoras:

1. Fork del repositorio
2. Crear rama de feature
3. Commit de cambios
4. Push a la rama
5. Crear Pull Request

---

## 📄 Licencia

MIT License - Libre para uso personal y comercial

---

## 🐛 Solución de Problemas

### Backend no inicia
- Verificar que el puerto 8000 no esté en uso
- Revisar que todas las dependencias estén instaladas
- Verificar variables de entorno en `.env`

### Frontend no conecta con Backend
- Verificar que el backend esté ejecutándose
- Revisar CORS en backend `.env`
- Verificar URL de API en frontend

### Bot de Telegram no responde
- Verificar token en `.env`
- Verificar que el backend esté ejecutándose
- Revisar logs de errores

### Backups no se crean
- Verificar permisos de escritura en carpeta `backups/`
- Verificar que existe la base de datos
- Revisar configuración de cron

---

## 📧 Soporte

Para preguntas o issues:
- Crear issue en GitHub
- Revisar documentación de la API en `/docs`

---

## ✅ Checklist de Instalación

- [ ] Python 3.9+ instalado
- [ ] Node.js 18+ instalado
- [ ] Clonar repositorio
- [ ] Instalar dependencias backend
- [ ] Configurar `.env` backend
- [ ] Ejecutar backend
- [ ] Instalar dependencias frontend
- [ ] Ejecutar frontend
- [ ] Verificar acceso a API `/health`
- [ ] Crear primer proyecto de prueba
- [ ] (Opcional) Configurar bot de Telegram
- [ ] (Opcional) Configurar webhooks n8n
- [ ] (Opcional) Configurar backups automáticos
- [ ] (Opcional) Configurar sincronización GitHub

---

**Proyecto creado con FastAPI, Astro, Telegram Bot API, SQLAlchemy y mucho ❤️**
