#!/bin/bash
#
# Script para configurar cron jobs para backup automático
# Ejecuta backup diario a las 2:00 AM
#

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

echo "🔧 Configurando cron jobs para Project Manager"
echo "Directorio del proyecto: $PROJECT_ROOT"
echo ""

# Crear comando de backup
BACKUP_CMD="0 2 * * * cd $PROJECT_ROOT && python3 $SCRIPT_DIR/backup.py crear >> $PROJECT_ROOT/logs/backup.log 2>&1"

# Crear comando de sincronización GitHub (opcional, cada 6 horas)
SYNC_CMD="0 */6 * * * cd $PROJECT_ROOT && python3 $SCRIPT_DIR/sync_github.py auto >> $PROJECT_ROOT/logs/sync.log 2>&1"

# Crear directorio de logs si no existe
mkdir -p "$PROJECT_ROOT/logs"

echo "📝 Cron jobs a configurar:"
echo ""
echo "1. Backup diario (2:00 AM):"
echo "   $BACKUP_CMD"
echo ""
echo "2. Sincronización GitHub (cada 6 horas - opcional):"
echo "   $SYNC_CMD"
echo ""

read -p "¿Deseas agregar el backup diario? (s/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[SsYy]$ ]]
then
    # Agregar cron job de backup
    (crontab -l 2>/dev/null | grep -v "backup.py crear"; echo "$BACKUP_CMD") | crontab -
    echo "✅ Cron job de backup agregado"
fi

read -p "¿Deseas agregar la sincronización automática con GitHub? (s/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[SsYy]$ ]]
then
    # Agregar cron job de sync
    (crontab -l 2>/dev/null | grep -v "sync_github.py auto"; echo "$SYNC_CMD") | crontab -
    echo "✅ Cron job de sincronización agregado"
    echo "⚠️  Recuerda configurar GITHUB_SYNC_ENABLED=true en .env"
fi

echo ""
echo "📋 Cron jobs actuales:"
crontab -l

echo ""
echo "✅ Configuración completada"
echo ""
echo "Para ver los logs:"
echo "  Backup: tail -f $PROJECT_ROOT/logs/backup.log"
echo "  Sync:   tail -f $PROJECT_ROOT/logs/sync.log"
