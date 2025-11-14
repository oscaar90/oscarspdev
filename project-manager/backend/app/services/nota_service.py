from sqlalchemy.orm import Session
from typing import List, Optional
from ..models.nota import Nota
from ..schemas.nota import NotaCreate, NotaUpdate


class NotaService:
    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[Nota]:
        """Obtener todas las notas"""
        return db.query(Nota).offset(skip).limit(limit).all()

    @staticmethod
    def get_by_id(db: Session, nota_id: int) -> Optional[Nota]:
        """Obtener nota por ID"""
        return db.query(Nota).filter(Nota.id == nota_id).first()

    @staticmethod
    def get_by_proyecto(db: Session, proyecto_id: int) -> List[Nota]:
        """Obtener todas las notas de un proyecto"""
        return db.query(Nota).filter(Nota.proyecto_id == proyecto_id).all()

    @staticmethod
    def create(db: Session, nota: NotaCreate) -> Nota:
        """Crear nueva nota"""
        db_nota = Nota(**nota.model_dump())
        db.add(db_nota)
        db.commit()
        db.refresh(db_nota)
        return db_nota

    @staticmethod
    def update(
        db: Session,
        nota_id: int,
        nota_update: NotaUpdate
    ) -> Optional[Nota]:
        """Actualizar nota existente"""
        db_nota = NotaService.get_by_id(db, nota_id)
        if not db_nota:
            return None

        update_data = nota_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_nota, key, value)

        db.commit()
        db.refresh(db_nota)
        return db_nota

    @staticmethod
    def delete(db: Session, nota_id: int) -> bool:
        """Eliminar nota"""
        db_nota = NotaService.get_by_id(db, nota_id)
        if not db_nota:
            return False

        db.delete(db_nota)
        db.commit()
        return True
