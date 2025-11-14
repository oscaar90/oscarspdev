from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from datetime import datetime
from enum import Enum


class EstadoProyecto(str, Enum):
    IDEA = "idea"
    PROTOTIPO = "prototipo"
    EN_PROGRESO = "en_progreso"
    BLOQUEADO = "bloqueado"
    PAUSADO = "pausado"
    COMPLETADO = "completado"
    ARCHIVADO = "archivado"


class OrigenProyecto(str, Enum):
    MANUAL = "manual"
    IA = "IA"
    WEBHOOK = "webhook"


class ChecklistItem(BaseModel):
    texto: str
    completado: bool = False


class ProyectoBase(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=255)
    descripcion: Optional[str] = None
    estado: EstadoProyecto = EstadoProyecto.IDEA
    prioridad: int = Field(default=0, ge=0, le=10)
    checklist: Optional[List[ChecklistItem]] = None
    origen: OrigenProyecto = OrigenProyecto.MANUAL


class ProyectoCreate(ProyectoBase):
    pass


class ProyectoUpdate(BaseModel):
    titulo: Optional[str] = Field(None, min_length=1, max_length=255)
    descripcion: Optional[str] = None
    estado: Optional[EstadoProyecto] = None
    prioridad: Optional[int] = Field(None, ge=0, le=10)
    checklist: Optional[List[ChecklistItem]] = None


class ProyectoResponse(ProyectoBase):
    id: int
    fecha_creacion: datetime
    fecha_actualizacion: datetime

    # Incluir etiquetas en la respuesta
    etiquetas: List["EtiquetaResponse"] = []

    model_config = ConfigDict(from_attributes=True)


# Importar después para evitar import circular
from .etiqueta import EtiquetaResponse
ProyectoResponse.model_rebuild()
