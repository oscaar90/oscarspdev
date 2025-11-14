from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Determinar qué base de datos usar basado en variable de entorno
DATABASE_TYPE = os.getenv("DATABASE_TYPE", "sqlite")

if DATABASE_TYPE == "postgresql":
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql://user:password@localhost/project_manager"
    )
else:
    # SQLite por defecto
    DATABASE_URL = "sqlite:///./project_manager.db"

# Crear engine con configuración específica para SQLite
if DATABASE_TYPE == "sqlite":
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False}
    )
else:
    engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """Dependency para obtener sesión de base de datos"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """Inicializar base de datos - crear todas las tablas"""
    Base.metadata.create_all(bind=engine)
