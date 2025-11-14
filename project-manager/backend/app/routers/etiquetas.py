from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..schemas.etiqueta import EtiquetaCreate, EtiquetaUpdate, EtiquetaResponse
from ..services.etiqueta_service import EtiquetaService

router = APIRouter(prefix="/tags", tags=["tags"])


@router.get("/", response_model=List[EtiquetaResponse])
def get_etiquetas(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db)
):
    """Obtener lista de etiquetas"""
    return EtiquetaService.get_all(db, skip=skip, limit=limit)


@router.get("/{etiqueta_id}", response_model=EtiquetaResponse)
def get_etiqueta(etiqueta_id: int, db: Session = Depends(get_db)):
    """Obtener etiqueta por ID"""
    etiqueta = EtiquetaService.get_by_id(db, etiqueta_id)
    if not etiqueta:
        raise HTTPException(status_code=404, detail="Etiqueta no encontrada")
    return etiqueta


@router.post("/", response_model=EtiquetaResponse, status_code=201)
def create_etiqueta(etiqueta: EtiquetaCreate, db: Session = Depends(get_db)):
    """Crear nueva etiqueta"""
    # Verificar que no exista ya una etiqueta con ese nombre
    existing = EtiquetaService.get_by_nombre(db, etiqueta.nombre)
    if existing:
        raise HTTPException(
            status_code=400,
            detail="Ya existe una etiqueta con ese nombre"
        )
    return EtiquetaService.create(db, etiqueta)


@router.put("/{etiqueta_id}", response_model=EtiquetaResponse)
def update_etiqueta(
    etiqueta_id: int,
    etiqueta_update: EtiquetaUpdate,
    db: Session = Depends(get_db)
):
    """Actualizar etiqueta existente"""
    etiqueta = EtiquetaService.update(db, etiqueta_id, etiqueta_update)
    if not etiqueta:
        raise HTTPException(status_code=404, detail="Etiqueta no encontrada")
    return etiqueta


@router.delete("/{etiqueta_id}", status_code=204)
def delete_etiqueta(etiqueta_id: int, db: Session = Depends(get_db)):
    """Eliminar etiqueta"""
    success = EtiquetaService.delete(db, etiqueta_id)
    if not success:
        raise HTTPException(status_code=404, detail="Etiqueta no encontrada")
    return None
