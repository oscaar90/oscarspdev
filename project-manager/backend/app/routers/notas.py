from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..schemas.nota import NotaCreate, NotaUpdate, NotaResponse
from ..services.nota_service import NotaService

router = APIRouter(prefix="/notes", tags=["notes"])


@router.get("/", response_model=List[NotaResponse])
def get_notas(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    proyecto_id: int = Query(None, description="Filtrar por proyecto"),
    db: Session = Depends(get_db)
):
    """Obtener lista de notas"""
    if proyecto_id:
        notas = NotaService.get_by_proyecto(db, proyecto_id)
    else:
        notas = NotaService.get_all(db, skip=skip, limit=limit)
    return notas


@router.get("/{nota_id}", response_model=NotaResponse)
def get_nota(nota_id: int, db: Session = Depends(get_db)):
    """Obtener nota por ID"""
    nota = NotaService.get_by_id(db, nota_id)
    if not nota:
        raise HTTPException(status_code=404, detail="Nota no encontrada")
    return nota


@router.post("/", response_model=NotaResponse, status_code=201)
def create_nota(nota: NotaCreate, db: Session = Depends(get_db)):
    """Crear nueva nota"""
    return NotaService.create(db, nota)


@router.put("/{nota_id}", response_model=NotaResponse)
def update_nota(
    nota_id: int,
    nota_update: NotaUpdate,
    db: Session = Depends(get_db)
):
    """Actualizar nota existente"""
    nota = NotaService.update(db, nota_id, nota_update)
    if not nota:
        raise HTTPException(status_code=404, detail="Nota no encontrada")
    return nota


@router.delete("/{nota_id}", status_code=204)
def delete_nota(nota_id: int, db: Session = Depends(get_db)):
    """Eliminar nota"""
    success = NotaService.delete(db, nota_id)
    if not success:
        raise HTTPException(status_code=404, detail="Nota no encontrada")
    return None
