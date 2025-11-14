from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime


class AdjuntoBase(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=255)
    ruta: str = Field(..., min_length=1, max_length=500)
    tipo: Optional[str] = Field(None, max_length=50)


class AdjuntoCreate(AdjuntoBase):
    proyecto_id: int = Field(..., gt=0)


class AdjuntoUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=1, max_length=255)
    ruta: Optional[str] = Field(None, min_length=1, max_length=500)
    tipo: Optional[str] = Field(None, max_length=50)


class AdjuntoResponse(AdjuntoBase):
    id: int
    proyecto_id: int
    fecha_creacion: datetime

    model_config = ConfigDict(from_attributes=True)
