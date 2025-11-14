from sqlalchemy.orm import Session
from typing import List, Optional
from ..models.etiqueta import Etiqueta
from ..schemas.etiqueta import EtiquetaCreate, EtiquetaUpdate


class EtiquetaService:
    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[Etiqueta]:
        """Obtener todas las etiquetas"""
        return db.query(Etiqueta).order_by(Etiqueta.nombre).offset(skip).limit(limit).all()

    @staticmethod
    def get_by_id(db: Session, etiqueta_id: int) -> Optional[Etiqueta]:
        """Obtener etiqueta por ID"""
        return db.query(Etiqueta).filter(Etiqueta.id == etiqueta_id).first()

    @staticmethod
    def get_by_nombre(db: Session, nombre: str) -> Optional[Etiqueta]:
        """Obtener etiqueta por nombre"""
        return db.query(Etiqueta).filter(Etiqueta.nombre == nombre).first()

    @staticmethod
    def create(db: Session, etiqueta: EtiquetaCreate) -> Etiqueta:
        """Crear nueva etiqueta"""
        db_etiqueta = Etiqueta(**etiqueta.model_dump())
        db.add(db_etiqueta)
        db.commit()
        db.refresh(db_etiqueta)
        return db_etiqueta

    @staticmethod
    def update(
        db: Session,
        etiqueta_id: int,
        etiqueta_update: EtiquetaUpdate
    ) -> Optional[Etiqueta]:
        """Actualizar etiqueta existente"""
        db_etiqueta = EtiquetaService.get_by_id(db, etiqueta_id)
        if not db_etiqueta:
            return None

        update_data = etiqueta_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_etiqueta, key, value)

        db.commit()
        db.refresh(db_etiqueta)
        return db_etiqueta

    @staticmethod
    def delete(db: Session, etiqueta_id: int) -> bool:
        """Eliminar etiqueta"""
        db_etiqueta = EtiquetaService.get_by_id(db, etiqueta_id)
        if not db_etiqueta:
            return False

        db.delete(db_etiqueta)
        db.commit()
        return True
