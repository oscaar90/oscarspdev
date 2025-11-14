from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship

from ..database import Base

# Tabla intermedia para relación muchos-a-muchos entre Proyecto y Etiqueta
proyecto_etiqueta = Table(
    'proyecto_etiqueta',
    Base.metadata,
    Column('proyecto_id', Integer, ForeignKey('proyectos.id'), primary_key=True),
    Column('etiqueta_id', Integer, ForeignKey('etiquetas.id'), primary_key=True)
)


class Etiqueta(Base):
    __tablename__ = "etiquetas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), unique=True, nullable=False, index=True)
    color = Column(String(7), nullable=True)  # Color hex, ej: #FF5733

    # Relación con Proyecto
    proyectos = relationship("Proyecto", secondary=proyecto_etiqueta, back_populates="etiquetas")

    def __repr__(self):
        return f"<Etiqueta(id={self.id}, nombre='{self.nombre}')>"
