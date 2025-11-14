"""
Bot de Telegram integrado para gestionar proyectos
Requiere python-telegram-bot
"""

import os
import logging
from typing import Optional
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters
)
from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..schemas.proyecto import ProyectoCreate, EstadoProyecto, OrigenProyecto
from ..schemas.proyecto import ProyectoUpdate
from ..services.proyecto_service import ProyectoService

# Configurar logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


# Helpers para obtener sesión de DB
def get_db_session():
    """Obtener sesión de base de datos"""
    return SessionLocal()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Comando /start - Mensaje de bienvenida"""
    welcome_message = """
🎯 *Bot de Gestión de Proyectos*

Comandos disponibles:
/nuevo <texto> - Crear nuevo proyecto con estado 'idea'
/lista - Ver proyectos activos
/estado <ID> <nuevo_estado> - Actualizar estado de proyecto

Estados disponibles: idea, prototipo, en_progreso, bloqueado, pausado, completado, archivado

¡Comienza a gestionar tus proyectos!
"""
    await update.message.reply_text(welcome_message, parse_mode='Markdown')


async def nuevo_proyecto(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Comando /nuevo - Crear nuevo proyecto"""
    if not context.args:
        await update.message.reply_text(
            "❌ Por favor proporciona un título para el proyecto.\n"
            "Ejemplo: /nuevo Desarrollar aplicación de tareas"
        )
        return

    # Unir todos los argumentos como título del proyecto
    titulo = ' '.join(context.args)

    # Crear proyecto en la base de datos
    db = get_db_session()
    try:
        proyecto_data = ProyectoCreate(
            titulo=titulo,
            estado=EstadoProyecto.IDEA,
            origen=OrigenProyecto.WEBHOOK,
            prioridad=0
        )

        proyecto = ProyectoService.create(db, proyecto_data)

        await update.message.reply_text(
            f"✅ *Proyecto creado*\n\n"
            f"ID: {proyecto.id}\n"
            f"Título: {proyecto.titulo}\n"
            f"Estado: {proyecto.estado.value}\n"
            f"Fecha: {proyecto.fecha_creacion.strftime('%Y-%m-%d %H:%M')}",
            parse_mode='Markdown'
        )

    except Exception as e:
        logger.error(f"Error al crear proyecto: {e}")
        await update.message.reply_text(
            f"❌ Error al crear proyecto: {str(e)}"
        )
    finally:
        db.close()


async def listar_proyectos(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Comando /lista - Listar proyectos activos"""
    db = get_db_session()
    try:
        # Obtener proyectos que no estén archivados o completados
        proyectos = ProyectoService.get_all(db, limit=20)

        # Filtrar proyectos activos
        proyectos_activos = [
            p for p in proyectos
            if p.estado not in [EstadoProyecto.ARCHIVADO, EstadoProyecto.COMPLETADO]
        ]

        if not proyectos_activos:
            await update.message.reply_text("📭 No hay proyectos activos.")
            return

        # Formatear lista de proyectos
        mensaje = "📋 *Proyectos Activos*\n\n"
        for proyecto in proyectos_activos:
            emoji = {
                'idea': '💡',
                'prototipo': '🔬',
                'en_progreso': '🚀',
                'bloqueado': '🚫',
                'pausado': '⏸️',
            }.get(proyecto.estado.value, '📌')

            mensaje += (
                f"{emoji} *{proyecto.id}*: {proyecto.titulo}\n"
                f"   Estado: {proyecto.estado.value} | "
                f"Prioridad: {proyecto.prioridad}\n\n"
            )

        await update.message.reply_text(mensaje, parse_mode='Markdown')

    except Exception as e:
        logger.error(f"Error al listar proyectos: {e}")
        await update.message.reply_text(
            f"❌ Error al listar proyectos: {str(e)}"
        )
    finally:
        db.close()


async def cambiar_estado(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Comando /estado - Cambiar estado de un proyecto"""
    if len(context.args) < 2:
        await update.message.reply_text(
            "❌ Uso incorrecto.\n"
            "Ejemplo: /estado 1 en_progreso\n\n"
            "Estados: idea, prototipo, en_progreso, bloqueado, pausado, completado, archivado"
        )
        return

    try:
        proyecto_id = int(context.args[0])
        nuevo_estado = context.args[1]

        # Validar estado
        estados_validos = [e.value for e in EstadoProyecto]
        if nuevo_estado not in estados_validos:
            await update.message.reply_text(
                f"❌ Estado inválido. Estados disponibles:\n" +
                "\n".join(estados_validos)
            )
            return

        # Actualizar proyecto
        db = get_db_session()
        try:
            proyecto_update = ProyectoUpdate(
                estado=EstadoProyecto(nuevo_estado)
            )

            proyecto = ProyectoService.update(db, proyecto_id, proyecto_update)

            if not proyecto:
                await update.message.reply_text(
                    f"❌ No se encontró proyecto con ID {proyecto_id}"
                )
                return

            await update.message.reply_text(
                f"✅ *Estado actualizado*\n\n"
                f"Proyecto: {proyecto.titulo}\n"
                f"Nuevo estado: {proyecto.estado.value}",
                parse_mode='Markdown'
            )

        finally:
            db.close()

    except ValueError:
        await update.message.reply_text(
            "❌ ID de proyecto inválido. Debe ser un número."
        )
    except Exception as e:
        logger.error(f"Error al cambiar estado: {e}")
        await update.message.reply_text(
            f"❌ Error al cambiar estado: {str(e)}"
        )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Comando /help - Mostrar ayuda"""
    await start(update, context)


def setup_telegram_bot() -> Optional[Application]:
    """
    Configurar y retornar el bot de Telegram
    Retorna None si no está configurado el token
    """
    telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")

    if not telegram_token:
        logger.warning(
            "TELEGRAM_BOT_TOKEN no configurado. Bot de Telegram deshabilitado."
        )
        return None

    # Crear aplicación
    application = Application.builder().token(telegram_token).build()

    # Registrar comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("nuevo", nuevo_proyecto))
    application.add_handler(CommandHandler("lista", listar_proyectos))
    application.add_handler(CommandHandler("estado", cambiar_estado))

    logger.info("Bot de Telegram configurado correctamente")
    return application


async def start_telegram_bot(application: Application) -> None:
    """Iniciar el bot de Telegram"""
    if application:
        logger.info("Iniciando bot de Telegram...")
        await application.initialize()
        await application.start()
        await application.updater.start_polling()


async def stop_telegram_bot(application: Application) -> None:
    """Detener el bot de Telegram"""
    if application:
        logger.info("Deteniendo bot de Telegram...")
        await application.updater.stop()
        await application.stop()
        await application.shutdown()
