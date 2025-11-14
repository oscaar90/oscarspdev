from .proyectos import router as proyectos_router
from .notas import router as notas_router
from .adjuntos import router as adjuntos_router
from .etiquetas import router as etiquetas_router
from .webhooks import router as webhooks_router
from .health import router as health_router

__all__ = [
    "proyectos_router",
    "notas_router",
    "adjuntos_router",
    "etiquetas_router",
    "webhooks_router",
    "health_router",
]
