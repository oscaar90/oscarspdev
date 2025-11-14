from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..schemas.webhook_event import WebhookEventCreate, WebhookEventResponse
from ..services.webhook_service import WebhookService

router = APIRouter(prefix="/webhooks", tags=["webhooks"])


@router.get("/", response_model=List[WebhookEventResponse])
def get_webhooks(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db)
):
    """Obtener lista de eventos webhook"""
    return WebhookService.get_all(db, skip=skip, limit=limit)


@router.get("/{webhook_id}", response_model=WebhookEventResponse)
def get_webhook(webhook_id: int, db: Session = Depends(get_db)):
    """Obtener evento webhook por ID"""
    webhook = WebhookService.get_by_id(db, webhook_id)
    if not webhook:
        raise HTTPException(status_code=404, detail="Webhook no encontrado")
    return webhook


@router.post("/", response_model=WebhookEventResponse, status_code=201)
def create_webhook(webhook: WebhookEventCreate, db: Session = Depends(get_db)):
    """Crear nuevo evento webhook"""
    db_webhook = WebhookService.create(db, webhook)

    # Si tiene URL destino, intentar enviar
    if webhook.url_destino:
        WebhookService.enviar_webhook(db, db_webhook.id)

    return db_webhook


@router.post("/{webhook_id}/reenviar", response_model=WebhookEventResponse)
def reenviar_webhook(webhook_id: int, db: Session = Depends(get_db)):
    """Reenviar un webhook que falló"""
    webhook = WebhookService.reenviar_webhook(db, webhook_id)
    if not webhook:
        raise HTTPException(status_code=404, detail="Webhook no encontrado")
    return webhook
