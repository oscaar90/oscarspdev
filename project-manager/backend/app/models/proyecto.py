from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from ..database import Base


class EstadoProyecto(str, enum.Enum):
    IDEA = "idea"
    PROTOTIPO = "prototipo"
    EN_PROGRESO = "en_progreso"
    BLOQUEADO = "bloqueado"
    PAUSADO = "pausado"
    COMPLETADO = "completado"
    ARCHIVADO = "archivado"


class OrigenProyecto(str, enum.Enum):
    MANUAL = "manual"
    IA = "IA"
    WEBHOOK = "webhook"


class Proyecto(Base):
    __tablename__ = "proyectos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), nullable=False, index=True)
    descripcion = Column(Text, nullable=True)
    estado = Column(
        Enum(EstadoProyecto),
        default=EstadoProyecto.IDEA,
        nullable=False,
        index=True
    )
    prioridad = Column(Integer, default=0, nullable=False, index=True)
    checklist = Column(JSON, nullable=True)  # Lista de items con {texto, completado}
    origen = Column(
        Enum(OrigenProyecto),
        default=OrigenProyecto.MANUAL,
        nullable=False
    )
    fecha_creacion = Column(DateTime, default=datetime.utcnow, nullable=False)
    fecha_actualizacion = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    # Relaciones
    notas = relationship("Nota", back_populates="proyecto", cascade="all, delete-orphan")
    adjuntos = relationship("Adjunto", back_populates="proyecto", cascade="all, delete-orphan")
    etiquetas = relationship("Etiqueta", secondary="proyecto_etiqueta", back_populates="proyectos")

    def __repr__(self):
        return f"<Proyecto(id={self.id}, titulo='{self.titulo}', estado='{self.estado}')>"
