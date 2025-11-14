from sqlalchemy.orm import Session
from typing import List, Optional
from ..models.adjunto import Adjunto
from ..schemas.adjunto import AdjuntoCreate, AdjuntoUpdate


class AdjuntoService:
    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[Adjunto]:
        """Obtener todos los adjuntos"""
        return db.query(Adjunto).offset(skip).limit(limit).all()

    @staticmethod
    def get_by_id(db: Session, adjunto_id: int) -> Optional[Adjunto]:
        """Obtener adjunto por ID"""
        return db.query(Adjunto).filter(Adjunto.id == adjunto_id).first()

    @staticmethod
    def get_by_proyecto(db: Session, proyecto_id: int) -> List[Adjunto]:
        """Obtener todos los adjuntos de un proyecto"""
        return db.query(Adjunto).filter(Adjunto.proyecto_id == proyecto_id).all()

    @staticmethod
    def create(db: Session, adjunto: AdjuntoCreate) -> Adjunto:
        """Crear nuevo adjunto"""
        db_adjunto = Adjunto(**adjunto.model_dump())
        db.add(db_adjunto)
        db.commit()
        db.refresh(db_adjunto)
        return db_adjunto

    @staticmethod
    def update(
        db: Session,
        adjunto_id: int,
        adjunto_update: AdjuntoUpdate
    ) -> Optional[Adjunto]:
        """Actualizar adjunto existente"""
        db_adjunto = AdjuntoService.get_by_id(db, adjunto_id)
        if not db_adjunto:
            return None

        update_data = adjunto_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_adjunto, key, value)

        db.commit()
        db.refresh(db_adjunto)
        return db_adjunto

    @staticmethod
    def delete(db: Session, adjunto_id: int) -> bool:
        """Eliminar adjunto"""
        db_adjunto = AdjuntoService.get_by_id(db, adjunto_id)
        if not db_adjunto:
            return False

        db.delete(db_adjunto)
        db.commit()
        return True
