from sqlalchemy.orm import Session
from typing import List, Optional
from ..models.proyecto import Proyecto, EstadoProyecto
from ..models.etiqueta import Etiqueta
from ..schemas.proyecto import ProyectoCreate, ProyectoUpdate


class ProyectoService:
    @staticmethod
    def get_all(
        db: Session,
        skip: int = 0,
        limit: int = 100,
        estado: Optional[EstadoProyecto] = None,
        prioridad_min: Optional[int] = None,
        search: Optional[str] = None
    ) -> List[Proyecto]:
        """Obtener todos los proyectos con filtros opcionales"""
        query = db.query(Proyecto)

        # Filtrar por estado si se proporciona
        if estado:
            query = query.filter(Proyecto.estado == estado)

        # Filtrar por prioridad mínima
        if prioridad_min is not None:
            query = query.filter(Proyecto.prioridad >= prioridad_min)

        # Búsqueda en título y descripción
        if search:
            search_term = f"%{search}%"
            query = query.filter(
                (Proyecto.titulo.ilike(search_term)) |
                (Proyecto.descripcion.ilike(search_term))
            )

        # Ordenar por prioridad desc, luego por fecha de actualización
        query = query.order_by(
            Proyecto.prioridad.desc(),
            Proyecto.fecha_actualizacion.desc()
        )

        return query.offset(skip).limit(limit).all()

    @staticmethod
    def get_by_id(db: Session, proyecto_id: int) -> Optional[Proyecto]:
        """Obtener proyecto por ID"""
        return db.query(Proyecto).filter(Proyecto.id == proyecto_id).first()

    @staticmethod
    def create(db: Session, proyecto: ProyectoCreate) -> Proyecto:
        """Crear nuevo proyecto"""
        db_proyecto = Proyecto(**proyecto.model_dump())
        db.add(db_proyecto)
        db.commit()
        db.refresh(db_proyecto)
        return db_proyecto

    @staticmethod
    def update(
        db: Session,
        proyecto_id: int,
        proyecto_update: ProyectoUpdate
    ) -> Optional[Proyecto]:
        """Actualizar proyecto existente"""
        db_proyecto = ProyectoService.get_by_id(db, proyecto_id)
        if not db_proyecto:
            return None

        # Actualizar solo los campos proporcionados
        update_data = proyecto_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_proyecto, key, value)

        db.commit()
        db.refresh(db_proyecto)
        return db_proyecto

    @staticmethod
    def delete(db: Session, proyecto_id: int) -> bool:
        """Eliminar proyecto"""
        db_proyecto = ProyectoService.get_by_id(db, proyecto_id)
        if not db_proyecto:
            return False

        db.delete(db_proyecto)
        db.commit()
        return True

    @staticmethod
    def add_etiqueta(
        db: Session,
        proyecto_id: int,
        etiqueta_id: int
    ) -> Optional[Proyecto]:
        """Agregar etiqueta a un proyecto"""
        db_proyecto = ProyectoService.get_by_id(db, proyecto_id)
        if not db_proyecto:
            return None

        etiqueta = db.query(Etiqueta).filter(Etiqueta.id == etiqueta_id).first()
        if not etiqueta:
            return None

        if etiqueta not in db_proyecto.etiquetas:
            db_proyecto.etiquetas.append(etiqueta)
            db.commit()
            db.refresh(db_proyecto)

        return db_proyecto

    @staticmethod
    def remove_etiqueta(
        db: Session,
        proyecto_id: int,
        etiqueta_id: int
    ) -> Optional[Proyecto]:
        """Remover etiqueta de un proyecto"""
        db_proyecto = ProyectoService.get_by_id(db, proyecto_id)
        if not db_proyecto:
            return None

        etiqueta = db.query(Etiqueta).filter(Etiqueta.id == etiqueta_id).first()
        if etiqueta and etiqueta in db_proyecto.etiquetas:
            db_proyecto.etiquetas.remove(etiqueta)
            db.commit()
            db.refresh(db_proyecto)

        return db_proyecto

    @staticmethod
    def get_by_estado(db: Session, estado: EstadoProyecto) -> List[Proyecto]:
        """Obtener proyectos por estado específico"""
        return db.query(Proyecto).filter(Proyecto.estado == estado).all()
