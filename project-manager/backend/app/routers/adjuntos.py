from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..schemas.adjunto import AdjuntoCreate, AdjuntoUpdate, AdjuntoResponse
from ..services.adjunto_service import AdjuntoService

router = APIRouter(prefix="/attachments", tags=["attachments"])


@router.get("/", response_model=List[AdjuntoResponse])
def get_adjuntos(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    proyecto_id: int = Query(None, description="Filtrar por proyecto"),
    db: Session = Depends(get_db)
):
    """Obtener lista de adjuntos"""
    if proyecto_id:
        adjuntos = AdjuntoService.get_by_proyecto(db, proyecto_id)
    else:
        adjuntos = AdjuntoService.get_all(db, skip=skip, limit=limit)
    return adjuntos


@router.get("/{adjunto_id}", response_model=AdjuntoResponse)
def get_adjunto(adjunto_id: int, db: Session = Depends(get_db)):
    """Obtener adjunto por ID"""
    adjunto = AdjuntoService.get_by_id(db, adjunto_id)
    if not adjunto:
        raise HTTPException(status_code=404, detail="Adjunto no encontrado")
    return adjunto


@router.post("/", response_model=AdjuntoResponse, status_code=201)
def create_adjunto(adjunto: AdjuntoCreate, db: Session = Depends(get_db)):
    """Crear nuevo adjunto"""
    return AdjuntoService.create(db, adjunto)


@router.put("/{adjunto_id}", response_model=AdjuntoResponse)
def update_adjunto(
    adjunto_id: int,
    adjunto_update: AdjuntoUpdate,
    db: Session = Depends(get_db)
):
    """Actualizar adjunto existente"""
    adjunto = AdjuntoService.update(db, adjunto_id, adjunto_update)
    if not adjunto:
        raise HTTPException(status_code=404, detail="Adjunto no encontrado")
    return adjunto


@router.delete("/{adjunto_id}", status_code=204)
def delete_adjunto(adjunto_id: int, db: Session = Depends(get_db)):
    """Eliminar adjunto"""
    success = AdjuntoService.delete(db, adjunto_id)
    if not success:
        raise HTTPException(status_code=404, detail="Adjunto no encontrado")
    return None
