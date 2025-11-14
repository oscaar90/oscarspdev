from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class EtiquetaBase(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100)
    color: Optional[str] = Field(None, pattern="^#[0-9A-Fa-f]{6}$")


class EtiquetaCreate(EtiquetaBase):
    pass


class EtiquetaUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=1, max_length=100)
    color: Optional[str] = Field(None, pattern="^#[0-9A-Fa-f]{6}$")


class EtiquetaResponse(EtiquetaBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
