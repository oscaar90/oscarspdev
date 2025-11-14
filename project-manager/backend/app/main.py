"""
Aplicación principal de FastAPI para gestión de proyectos
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import os

from .database import init_db
from .routers import (
    proyectos_router,
    notas_router,
    adjuntos_router,
    etiquetas_router,
    webhooks_router,
    health_router
)
from .services.telegram_bot import setup_telegram_bot, start_telegram_bot, stop_telegram_bot


# Variable global para el bot de Telegram
telegram_app = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Eventos de inicio y cierre de la aplicación"""
    global telegram_app

    # Inicializar base de datos
    print("🗄️  Inicializando base de datos...")
    init_db()
    print("✅ Base de datos inicializada")

    # Configurar e iniciar bot de Telegram si está disponible
    telegram_app = setup_telegram_bot()
    if telegram_app:
        await start_telegram_bot(telegram_app)
        print("✅ Bot de Telegram iniciado")

    yield

    # Detener bot de Telegram al cerrar la aplicación
    if telegram_app:
        await stop_telegram_bot(telegram_app)
        print("🛑 Bot de Telegram detenido")


# Crear aplicación FastAPI
app = FastAPI(
    title="Project Manager API",
    description="API para gestión de proyectos personales con IA y webhooks",
    version="1.0.0",
    lifespan=lifespan
)

# Configurar CORS
origins = os.getenv("CORS_ORIGINS", "*").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins if origins != ["*"] else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar routers
app.include_router(health_router)
app.include_router(proyectos_router)
app.include_router(notas_router)
app.include_router(adjuntos_router)
app.include_router(etiquetas_router)
app.include_router(webhooks_router)


@app.get("/")
def root():
    """Endpoint raíz"""
    return {
        "message": "Project Manager API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
