from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from datetime import datetime

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/")
def health_check(db: Session = Depends(get_db)):
    """Verificar estado de la aplicación y conexión a base de datos"""
    try:
        # Intentar hacer query a la base de datos
        db.execute("SELECT 1")
        db_status = "healthy"
    except Exception as e:
        db_status = f"unhealthy: {str(e)}"

    return {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat(),
        "database": db_status,
        "service": "Project Manager API"
    }
