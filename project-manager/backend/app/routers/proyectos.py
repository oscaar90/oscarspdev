from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from ..database import get_db
from ..schemas.proyecto import ProyectoCreate, ProyectoUpdate, ProyectoResponse, EstadoProyecto
from ..services.proyecto_service import ProyectoService
from ..services.webhook_service import WebhookService

router = APIRouter(prefix="/projects", tags=["projects"])


@router.get("/", response_model=List[ProyectoResponse])
def get_proyectos(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    estado: Optional[EstadoProyecto] = None,
    prioridad_min: Optional[int] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Obtener lista de proyectos con filtros opcionales"""
    proyectos = ProyectoService.get_all(
        db,
        skip=skip,
        limit=limit,
        estado=estado,
        prioridad_min=prioridad_min,
        search=search
    )
    return proyectos


@router.get("/{proyecto_id}", response_model=ProyectoResponse)
def get_proyecto(proyecto_id: int, db: Session = Depends(get_db)):
    """Obtener proyecto por ID"""
    proyecto = ProyectoService.get_by_id(db, proyecto_id)
    if not proyecto:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return proyecto


@router.post("/", response_model=ProyectoResponse, status_code=201)
def create_proyecto(proyecto: ProyectoCreate, db: Session = Depends(get_db)):
    """Crear nuevo proyecto"""
    db_proyecto = ProyectoService.create(db, proyecto)

    # Crear evento webhook de proyecto creado
    WebhookService.crear_evento_proyecto(
        db,
        evento_tipo="proyecto_creado",
        proyecto_id=db_proyecto.id,
        payload={
            "proyecto_id": db_proyecto.id,
            "titulo": db_proyecto.titulo,
            "estado": db_proyecto.estado.value,
            "origen": db_proyecto.origen.value,
        }
    )

    return db_proyecto


@router.put("/{proyecto_id}", response_model=ProyectoResponse)
def update_proyecto(
    proyecto_id: int,
    proyecto_update: ProyectoUpdate,
    db: Session = Depends(get_db)
):
    """Actualizar proyecto existente"""
    # Obtener estado anterior para detectar cambios
    proyecto_anterior = ProyectoService.get_by_id(db, proyecto_id)
    if not proyecto_anterior:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")

    estado_anterior = proyecto_anterior.estado

    # Actualizar proyecto
    db_proyecto = ProyectoService.update(db, proyecto_id, proyecto_update)

    # Si el estado cambió, crear evento webhook
    if proyecto_update.estado and proyecto_update.estado != estado_anterior:
        WebhookService.crear_evento_proyecto(
            db,
            evento_tipo="estado_cambiado",
            proyecto_id=db_proyecto.id,
            payload={
                "proyecto_id": db_proyecto.id,
                "titulo": db_proyecto.titulo,
                "estado_anterior": estado_anterior.value,
                "estado_nuevo": db_proyecto.estado.value,
            }
        )

        # Eventos especiales para completado y archivado
        if db_proyecto.estado == EstadoProyecto.COMPLETADO:
            WebhookService.crear_evento_proyecto(
                db,
                evento_tipo="proyecto_completado",
                proyecto_id=db_proyecto.id,
                payload={
                    "proyecto_id": db_proyecto.id,
                    "titulo": db_proyecto.titulo,
                }
            )

        elif db_proyecto.estado == EstadoProyecto.ARCHIVADO:
            WebhookService.crear_evento_proyecto(
                db,
                evento_tipo="proyecto_archivado",
                proyecto_id=db_proyecto.id,
                payload={
                    "proyecto_id": db_proyecto.id,
                    "titulo": db_proyecto.titulo,
                }
            )

    return db_proyecto


@router.delete("/{proyecto_id}", status_code=204)
def delete_proyecto(proyecto_id: int, db: Session = Depends(get_db)):
    """Eliminar proyecto"""
    success = ProyectoService.delete(db, proyecto_id)
    if not success:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return None


@router.post("/{proyecto_id}/etiquetas/{etiqueta_id}", response_model=ProyectoResponse)
def add_etiqueta_to_proyecto(
    proyecto_id: int,
    etiqueta_id: int,
    db: Session = Depends(get_db)
):
    """Agregar etiqueta a proyecto"""
    proyecto = ProyectoService.add_etiqueta(db, proyecto_id, etiqueta_id)
    if not proyecto:
        raise HTTPException(
            status_code=404,
            detail="Proyecto o etiqueta no encontrado"
        )
    return proyecto


@router.delete("/{proyecto_id}/etiquetas/{etiqueta_id}", response_model=ProyectoResponse)
def remove_etiqueta_from_proyecto(
    proyecto_id: int,
    etiqueta_id: int,
    db: Session = Depends(get_db)
):
    """Remover etiqueta de proyecto"""
    proyecto = ProyectoService.remove_etiqueta(db, proyecto_id, etiqueta_id)
    if not proyecto:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return proyecto
