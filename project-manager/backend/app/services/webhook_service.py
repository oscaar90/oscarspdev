from sqlalchemy.orm import Session
from typing import List, Optional, Dict, Any
from datetime import datetime
import requests
import os

from ..models.webhook_event import WebhookEvent
from ..schemas.webhook_event import WebhookEventCreate


class WebhookService:
    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[WebhookEvent]:
        """Obtener todos los eventos de webhook"""
        return db.query(WebhookEvent).order_by(
            WebhookEvent.fecha_creacion.desc()
        ).offset(skip).limit(limit).all()

    @staticmethod
    def get_by_id(db: Session, webhook_id: int) -> Optional[WebhookEvent]:
        """Obtener evento de webhook por ID"""
        return db.query(WebhookEvent).filter(WebhookEvent.id == webhook_id).first()

    @staticmethod
    def create(db: Session, webhook: WebhookEventCreate) -> WebhookEvent:
        """Crear nuevo evento de webhook"""
        db_webhook = WebhookEvent(**webhook.model_dump())
        db.add(db_webhook)
        db.commit()
        db.refresh(db_webhook)
        return db_webhook

    @staticmethod
    def enviar_webhook(db: Session, webhook_id: int) -> Optional[WebhookEvent]:
        """Enviar webhook a URL destino"""
        db_webhook = WebhookService.get_by_id(db, webhook_id)
        if not db_webhook or not db_webhook.url_destino:
            return None

        try:
            response = requests.post(
                db_webhook.url_destino,
                json=db_webhook.payload,
                timeout=10
            )

            db_webhook.enviado = True
            db_webhook.respuesta_codigo = response.status_code
            db_webhook.respuesta_contenido = response.text[:1000]  # Limitar tamaño
            db_webhook.fecha_envio = datetime.utcnow()

        except Exception as e:
            db_webhook.enviado = False
            db_webhook.respuesta_contenido = str(e)[:1000]

        db.commit()
        db.refresh(db_webhook)
        return db_webhook

    @staticmethod
    def crear_evento_proyecto(
        db: Session,
        evento_tipo: str,
        proyecto_id: int,
        payload: Dict[str, Any]
    ) -> Optional[WebhookEvent]:
        """
        Crear y enviar evento de webhook para proyecto
        Tipos: proyecto_creado, estado_cambiado, proyecto_completado, proyecto_archivado
        """
        # Obtener URL de webhook de variable de entorno
        webhook_url = os.getenv("N8N_WEBHOOK_URL")

        if not webhook_url:
            # Si no hay URL configurada, solo crear el evento sin enviar
            webhook_data = WebhookEventCreate(
                evento_tipo=evento_tipo,
                proyecto_id=proyecto_id,
                payload=payload,
                url_destino=None
            )
            return WebhookService.create(db, webhook_data)

        # Crear evento con URL
        webhook_data = WebhookEventCreate(
            evento_tipo=evento_tipo,
            proyecto_id=proyecto_id,
            payload=payload,
            url_destino=webhook_url
        )
        db_webhook = WebhookService.create(db, webhook_data)

        # Intentar enviar webhook
        WebhookService.enviar_webhook(db, db_webhook.id)

        return db_webhook

    @staticmethod
    def reenviar_webhook(db: Session, webhook_id: int) -> Optional[WebhookEvent]:
        """Reenviar un webhook que falló"""
        return WebhookService.enviar_webhook(db, webhook_id)
