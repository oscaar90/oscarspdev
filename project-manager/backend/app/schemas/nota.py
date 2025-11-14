from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime


class NotaBase(BaseModel):
    titulo: Optional[str] = Field(None, max_length=255)
    contenido: str = Field(..., min_length=1)


class NotaCreate(NotaBase):
    proyecto_id: int = Field(..., gt=0)


class NotaUpdate(BaseModel):
    titulo: Optional[str] = Field(None, max_length=255)
    contenido: Optional[str] = Field(None, min_length=1)


class NotaResponse(NotaBase):
    id: int
    proyecto_id: int
    fecha_creacion: datetime
    fecha_actualizacion: datetime

    model_config = ConfigDict(from_attributes=True)
