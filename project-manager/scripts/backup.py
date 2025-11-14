#!/usr/bin/env python3
"""
Script de backup automático de base de datos
Crea copias de seguridad en la carpeta backups/
"""

import os
import shutil
from datetime import datetime
from pathlib import Path

# Rutas
PROJECT_ROOT = Path(__file__).parent.parent
BACKEND_DIR = PROJECT_ROOT / "backend"
BACKUPS_DIR = PROJECT_ROOT / "backups"
DB_FILE = BACKEND_DIR / "project_manager.db"


def crear_backup():
    """Crear backup de la base de datos"""
    try:
        # Verificar que existe la base de datos
        if not DB_FILE.exists():
            print(f"⚠️  Base de datos no encontrada en: {DB_FILE}")
            return False

        # Crear directorio de backups si no existe
        BACKUPS_DIR.mkdir(exist_ok=True)

        # Nombre del archivo de backup con timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"project_manager_backup_{timestamp}.db"
        backup_path = BACKUPS_DIR / backup_filename

        # Copiar base de datos
        shutil.copy2(DB_FILE, backup_path)

        # Obtener tamaño del backup
        size_mb = backup_path.stat().st_size / (1024 * 1024)

        print(f"✅ Backup creado exitosamente")
        print(f"Archivo: {backup_filename}")
        print(f"Tamaño: {size_mb:.2f} MB")
        print(f"Ruta: {backup_path}")

        # Limpiar backups antiguos (mantener solo los últimos 30)
        limpiar_backups_antiguos()

        return True

    except Exception as e:
        print(f"❌ Error al crear backup: {e}")
        return False


def limpiar_backups_antiguos(mantener=30):
    """Eliminar backups antiguos, manteniendo solo los más recientes"""
    try:
        # Obtener lista de backups ordenados por fecha de modificación
        backups = sorted(
            BACKUPS_DIR.glob("project_manager_backup_*.db"),
            key=lambda x: x.stat().st_mtime,
            reverse=True
        )

        # Eliminar backups que excedan el límite
        if len(backups) > mantener:
            eliminados = 0
            for backup in backups[mantener:]:
                backup.unlink()
                eliminados += 1

            print(f"🗑️  Backups antiguos eliminados: {eliminados}")

    except Exception as e:
        print(f"⚠️  Error al limpiar backups antiguos: {e}")


def listar_backups():
    """Listar todos los backups disponibles"""
    try:
        backups = sorted(
            BACKUPS_DIR.glob("project_manager_backup_*.db"),
            key=lambda x: x.stat().st_mtime,
            reverse=True
        )

        if not backups:
            print("📭 No hay backups disponibles")
            return

        print(f"\n📦 Backups disponibles ({len(backups)}):\n")
        print("=" * 80)

        for backup in backups:
            size_mb = backup.stat().st_size / (1024 * 1024)
            mtime = datetime.fromtimestamp(backup.stat().st_mtime)

            print(f"Archivo: {backup.name}")
            print(f"Fecha: {mtime.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Tamaño: {size_mb:.2f} MB")
            print("-" * 80)

    except Exception as e:
        print(f"❌ Error al listar backups: {e}")


def restaurar_backup(backup_filename):
    """Restaurar una base de datos desde un backup"""
    try:
        backup_path = BACKUPS_DIR / backup_filename

        if not backup_path.exists():
            print(f"❌ Backup no encontrado: {backup_filename}")
            return False

        # Confirmar restauración
        print(f"⚠️  ADVERTENCIA: Esta operación sobrescribirá la base de datos actual")
        print(f"Backup a restaurar: {backup_filename}")
        respuesta = input("¿Continuar? (sí/no): ")

        if respuesta.lower() not in ['sí', 'si', 's', 'yes', 'y']:
            print("❌ Restauración cancelada")
            return False

        # Crear backup de seguridad de la BD actual
        if DB_FILE.exists():
            safety_backup = BACKUPS_DIR / f"pre_restore_{datetime.now().strftime('%Y%m%d_%H%M%S')}.db"
            shutil.copy2(DB_FILE, safety_backup)
            print(f"💾 Backup de seguridad creado: {safety_backup.name}")

        # Restaurar backup
        shutil.copy2(backup_path, DB_FILE)

        print(f"✅ Base de datos restaurada exitosamente")
        return True

    except Exception as e:
        print(f"❌ Error al restaurar backup: {e}")
        return False


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Sistema de backup de base de datos")
    parser.add_argument(
        'accion',
        choices=['crear', 'listar', 'restaurar'],
        help='Acción a realizar'
    )
    parser.add_argument(
        '-f', '--file',
        help='Nombre del archivo de backup (para restaurar)'
    )

    args = parser.parse_args()

    if args.accion == 'crear':
        crear_backup()
    elif args.accion == 'listar':
        listar_backups()
    elif args.accion == 'restaurar':
        if not args.file:
            print("❌ Debes especificar el archivo de backup con -f")
        else:
            restaurar_backup(args.file)
