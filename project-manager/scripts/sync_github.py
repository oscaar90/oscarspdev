#!/usr/bin/env python3
"""
Script de sincronización con GitHub
Realiza commit y push automático de cambios
"""

import os
import subprocess
from datetime import datetime
from pathlib import Path

# Rutas
PROJECT_ROOT = Path(__file__).parent.parent


def ejecutar_comando(comando):
    """Ejecutar comando de shell y retornar resultado"""
    try:
        result = subprocess.run(
            comando,
            shell=True,
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True
        )
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)


def verificar_git():
    """Verificar que el directorio es un repositorio git"""
    success, stdout, stderr = ejecutar_comando("git status")
    return success


def obtener_cambios():
    """Obtener lista de archivos modificados"""
    success, stdout, stderr = ejecutar_comando("git status --porcelain")
    if not success:
        return []

    cambios = []
    for linea in stdout.strip().split('\n'):
        if linea:
            cambios.append(linea)

    return cambios


def sincronizar_github(mensaje_commit=None):
    """Realizar sincronización completa con GitHub"""
    try:
        # Verificar que es un repositorio git
        if not verificar_git():
            print("❌ Este directorio no es un repositorio git")
            return False

        # Verificar cambios
        cambios = obtener_cambios()
        if not cambios:
            print("✅ No hay cambios para sincronizar")
            return True

        print(f"\n📝 Cambios detectados: {len(cambios)}\n")
        for cambio in cambios[:10]:  # Mostrar primeros 10
            print(f"  {cambio}")

        if len(cambios) > 10:
            print(f"  ... y {len(cambios) - 10} más")

        # Mensaje de commit automático si no se proporciona
        if not mensaje_commit:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            mensaje_commit = f"Auto-sync: {timestamp}"

        # Git add
        print("\n📦 Agregando archivos...")
        success, stdout, stderr = ejecutar_comando("git add .")
        if not success:
            print(f"❌ Error al agregar archivos: {stderr}")
            return False

        # Git commit
        print(f"💾 Creando commit: {mensaje_commit}")
        success, stdout, stderr = ejecutar_comando(f'git commit -m "{mensaje_commit}"')
        if not success:
            if "nothing to commit" in stderr:
                print("✅ No hay cambios para commitear")
                return True
            print(f"❌ Error al crear commit: {stderr}")
            return False

        # Git push
        print("🚀 Enviando cambios a GitHub...")
        success, stdout, stderr = ejecutar_comando("git push")

        if not success:
            print(f"❌ Error al hacer push: {stderr}")
            print("\n💡 Intenta ejecutar manualmente:")
            print("   git push")
            return False

        print("\n✅ Sincronización completada exitosamente")
        print(stdout)
        return True

    except Exception as e:
        print(f"❌ Error durante sincronización: {e}")
        return False


def verificar_configuracion():
    """Verificar configuración de GitHub"""
    print("🔍 Verificando configuración...\n")

    # Verificar origen remoto
    success, stdout, stderr = ejecutar_comando("git remote -v")
    if success and stdout:
        print("📡 Remotos configurados:")
        print(stdout)
    else:
        print("⚠️  No se encontraron remotos configurados")

    # Verificar rama actual
    success, stdout, stderr = ejecutar_comando("git branch --show-current")
    if success:
        print(f"\n🌿 Rama actual: {stdout.strip()}")

    # Verificar estado
    success, stdout, stderr = ejecutar_comando("git status")
    if success:
        print(f"\n📊 Estado:")
        print(stdout)


def modo_auto():
    """Modo automático para cron jobs"""
    # Leer variables de entorno
    habilitar_sync = os.getenv("GITHUB_SYNC_ENABLED", "false").lower() == "true"

    if not habilitar_sync:
        print("ℹ️  Sincronización con GitHub deshabilitada")
        print("   Configura GITHUB_SYNC_ENABLED=true en .env para habilitar")
        return

    # Ejecutar sincronización
    mensaje = f"Auto-backup: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    sincronizar_github(mensaje)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Sincronización con GitHub")
    parser.add_argument(
        'accion',
        nargs='?',
        choices=['sync', 'status', 'auto'],
        default='sync',
        help='Acción a realizar'
    )
    parser.add_argument(
        '-m', '--mensaje',
        help='Mensaje de commit personalizado'
    )

    args = parser.parse_args()

    if args.accion == 'sync':
        sincronizar_github(args.mensaje)
    elif args.accion == 'status':
        verificar_configuracion()
    elif args.accion == 'auto':
        modo_auto()
