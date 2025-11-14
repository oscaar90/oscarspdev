from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Dict, Any
from datetime import datetime


class WebhookEventBase(BaseModel):
    evento_tipo: str = Field(..., min_length=1, max_length=100)
    proyecto_id: Optional[int] = None
    payload: Optional[Dict[str, Any]] = None
    url_destino: Optional[str] = Field(None, max_length=500)


class WebhookEventCreate(WebhookEventBase):
    pass


class WebhookEventResponse(WebhookEventBase):
    id: int
    enviado: bool
    respuesta_codigo: Optional[int] = None
    respuesta_contenido: Optional[str] = None
    fecha_creacion: datetime
    fecha_envio: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
