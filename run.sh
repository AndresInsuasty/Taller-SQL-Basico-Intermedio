#!/bin/bash
# Script para ejecutar el generador de datos con uv

echo "🚀 Generador de Base de Datos - El Último Salto"
echo "=================================================="
echo ""
echo "Ejecutando con uv + Python 3.11..."
echo ""

uv run python generar_data.py

echo ""
echo "✓ Completo. Base de datos en: tienda.db"
echo "✓ Copia también disponible en: datos/tienda.db"
