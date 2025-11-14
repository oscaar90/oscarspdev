from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, JSON
from datetime import datetime

from ..database import Base


class WebhookEvent(Base):
    __tablename__ = "webhook_events"

    id = Column(Integer, primary_key=True, index=True)
    evento_tipo = Column(String(100), nullable=False, index=True)
    # Tipos: proyecto_creado, estado_cambiado, proyecto_completado, proyecto_archivado

    proyecto_id = Column(Integer, nullable=True)  # ID del proyecto relacionado
    payload = Column(JSON, nullable=True)  # Datos del evento
    url_destino = Column(String(500), nullable=True)  # URL del webhook (si aplica)

    enviado = Column(Boolean, default=False, nullable=False)
    respuesta_codigo = Column(Integer, nullable=True)  # HTTP status code de la respuesta
    respuesta_contenido = Column(Text, nullable=True)

    fecha_creacion = Column(DateTime, default=datetime.utcnow, nullable=False)
    fecha_envio = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"<WebhookEvent(id={self.id}, tipo='{self.evento_tipo}', enviado={self.enviado})>"
