#!/usr/bin/env python3
"""
CLI para gestión de proyectos
Permite operaciones desde línea de comandos
"""

import sys
import os
from pathlib import Path

# Agregar el directorio backend al path
backend_path = Path(__file__).parent.parent / "backend"
sys.path.insert(0, str(backend_path))

import argparse
import json
from datetime import datetime

from app.database import SessionLocal, init_db
from app.models.proyecto import EstadoProyecto, OrigenProyecto
from app.schemas.proyecto import ProyectoCreate, ProyectoUpdate
from app.services.proyecto_service import ProyectoService


def agregar_proyecto(args):
    """Agregar nuevo proyecto"""
    db = SessionLocal()
    try:
        proyecto_data = ProyectoCreate(
            titulo=args.titulo,
            descripcion=args.descripcion if args.descripcion else None,
            estado=EstadoProyecto(args.estado) if args.estado else EstadoProyecto.IDEA,
            prioridad=args.prioridad if args.prioridad else 0,
            origen=OrigenProyecto.MANUAL
        )

        proyecto = ProyectoService.create(db, proyecto_data)

        print(f"✅ Proyecto creado exitosamente")
        print(f"ID: {proyecto.id}")
        print(f"Título: {proyecto.titulo}")
        print(f"Estado: {proyecto.estado.value}")
        print(f"Prioridad: {proyecto.prioridad}")

    except Exception as e:
        print(f"❌ Error al crear proyecto: {e}")
    finally:
        db.close()


def listar_proyectos(args):
    """Listar proyectos"""
    db = SessionLocal()
    try:
        estado = EstadoProyecto(args.estado) if args.estado else None

        proyectos = ProyectoService.get_all(
            db,
            estado=estado,
            limit=args.limit if args.limit else 100
        )

        if not proyectos:
            print("📭 No se encontraron proyectos")
            return

        print(f"\n📋 Proyectos encontrados: {len(proyectos)}\n")
        print("=" * 80)

        for proyecto in proyectos:
            print(f"\nID: {proyecto.id}")
            print(f"Título: {proyecto.titulo}")
            print(f"Estado: {proyecto.estado.value}")
            print(f"Prioridad: {proyecto.prioridad}")
            if proyecto.descripcion:
                print(f"Descripción: {proyecto.descripcion[:100]}...")
            print(f"Creado: {proyecto.fecha_creacion.strftime('%Y-%m-%d %H:%M')}")
            print("-" * 80)

    except Exception as e:
        print(f"❌ Error al listar proyectos: {e}")
    finally:
        db.close()


def cambiar_estado(args):
    """Cambiar estado de un proyecto"""
    db = SessionLocal()
    try:
        nuevo_estado = EstadoProyecto(args.nuevo_estado)

        proyecto_update = ProyectoUpdate(estado=nuevo_estado)
        proyecto = ProyectoService.update(db, args.proyecto_id, proyecto_update)

        if not proyecto:
            print(f"❌ No se encontró proyecto con ID {args.proyecto_id}")
            return

        print(f"✅ Estado actualizado exitosamente")
        print(f"Proyecto: {proyecto.titulo}")
        print(f"Nuevo estado: {proyecto.estado.value}")

    except ValueError as e:
        print(f"❌ Estado inválido. Estados disponibles:")
        for estado in EstadoProyecto:
            print(f"  - {estado.value}")
    except Exception as e:
        print(f"❌ Error al cambiar estado: {e}")
    finally:
        db.close()


def exportar_markdown(args):
    """Exportar proyectos a Markdown"""
    db = SessionLocal()
    try:
        estado = EstadoProyecto(args.estado) if args.estado else None

        proyectos = ProyectoService.get_all(db, estado=estado)

        if not proyectos:
            print("📭 No se encontraron proyectos para exportar")
            return

        # Generar contenido Markdown
        markdown = f"# Proyectos - {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"

        # Agrupar por estado
        proyectos_por_estado = {}
        for proyecto in proyectos:
            estado_key = proyecto.estado.value
            if estado_key not in proyectos_por_estado:
                proyectos_por_estado[estado_key] = []
            proyectos_por_estado[estado_key].append(proyecto)

        # Generar secciones por estado
        for estado_name, projs in sorted(proyectos_por_estado.items()):
            markdown += f"## {estado_name.upper()}\n\n"

            for proyecto in projs:
                markdown += f"### {proyecto.titulo}\n\n"
                markdown += f"- **ID**: {proyecto.id}\n"
                markdown += f"- **Prioridad**: {proyecto.prioridad}\n"
                markdown += f"- **Origen**: {proyecto.origen.value}\n"
                markdown += f"- **Creado**: {proyecto.fecha_creacion.strftime('%Y-%m-%d')}\n"

                if proyecto.descripcion:
                    markdown += f"\n{proyecto.descripcion}\n"

                if proyecto.checklist:
                    markdown += f"\n**Checklist**:\n"
                    for item in proyecto.checklist:
                        check = "✅" if item.get('completado') else "⬜"
                        markdown += f"- {check} {item.get('texto')}\n"

                markdown += "\n---\n\n"

        # Guardar archivo
        filename = args.output if args.output else f"proyectos_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(markdown)

        print(f"✅ Proyectos exportados a: {filename}")
        print(f"Total de proyectos: {len(proyectos)}")

    except Exception as e:
        print(f"❌ Error al exportar: {e}")
    finally:
        db.close()


def main():
    """Función principal del CLI"""
    parser = argparse.ArgumentParser(
        description="CLI para gestión de proyectos",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    subparsers = parser.add_subparsers(dest='comando', help='Comandos disponibles')

    # Comando: agregar
    parser_add = subparsers.add_parser('agregar', help='Agregar nuevo proyecto')
    parser_add.add_argument('titulo', help='Título del proyecto')
    parser_add.add_argument('-d', '--descripcion', help='Descripción del proyecto')
    parser_add.add_argument('-e', '--estado', help='Estado inicial', default='idea')
    parser_add.add_argument('-p', '--prioridad', type=int, help='Prioridad (0-10)', default=0)

    # Comando: listar
    parser_list = subparsers.add_parser('listar', help='Listar proyectos')
    parser_list.add_argument('-e', '--estado', help='Filtrar por estado')
    parser_list.add_argument('-l', '--limit', type=int, help='Límite de resultados', default=100)

    # Comando: estado
    parser_estado = subparsers.add_parser('estado', help='Cambiar estado de proyecto')
    parser_estado.add_argument('proyecto_id', type=int, help='ID del proyecto')
    parser_estado.add_argument('nuevo_estado', help='Nuevo estado')

    # Comando: exportar
    parser_export = subparsers.add_parser('exportar', help='Exportar a Markdown')
    parser_export.add_argument('-e', '--estado', help='Filtrar por estado')
    parser_export.add_argument('-o', '--output', help='Archivo de salida')

    args = parser.parse_args()

    # Inicializar base de datos
    init_db()

    # Ejecutar comando
    if args.comando == 'agregar':
        agregar_proyecto(args)
    elif args.comando == 'listar':
        listar_proyectos(args)
    elif args.comando == 'estado':
        cambiar_estado(args)
    elif args.comando == 'exportar':
        exportar_markdown(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
