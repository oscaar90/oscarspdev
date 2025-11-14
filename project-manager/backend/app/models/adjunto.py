from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from ..database import Base


class Adjunto(Base):
    __tablename__ = "adjuntos"

    id = Column(Integer, primary_key=True, index=True)
    proyecto_id = Column(Integer, ForeignKey("proyectos.id"), nullable=False)
    nombre = Column(String(255), nullable=False)
    ruta = Column(String(500), nullable=False)  # Puede ser ruta local o URL
    tipo = Column(String(50), nullable=True)  # image, document, link, etc.
    fecha_creacion = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relación con Proyecto
    proyecto = relationship("Proyecto", back_populates="adjuntos")

    def __repr__(self):
        return f"<Adjunto(id={self.id}, nombre='{self.nombre}')>"
