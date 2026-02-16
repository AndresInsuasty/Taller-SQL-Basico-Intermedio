# Guía de Instalación y Configuración con uv

## ¿Qué es uv?

**uv** es un gestor de proyectos Python ultrarrápido escrito en Rust. Reemplaza a `pip`, `poetry` y `venv` en un solo comando.

- ⚡ **Velocidad:** 10-100x más rápido que pip
- 📦 **Gestión de dependencias:** Similar a poetry
- 🐍 **Gestión de Python:** Descarga automáticamente versiones de Python
- 🔒 **Lock file:** `uv.lock` asegura reproducibilidad

## Instalación

### 1. Instalar uv (macOS/Linux/Windows)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Luego, verifica:
```bash
uv --version
```

Deberías ver algo como: `uv 0.x.x`

### 2. Clonar o Descargar el Taller

```bash
cd /ruta/al/taller
ls  # Deberías ver: generar_data.py, pyproject.toml, etc.
```

## Setup del Proyecto

### Opción A: Setup Automático (Recomendado)

```bash
# Sincroniza dependencias e instala Python 3.11 si es necesario
uv sync

# Verifica que está funcionando
uv run python --version
# Output: Python 3.11.14
```

### Opción B: Setup Manual

```bash
# Crea venv explícitamente
uv venv

# Activa el venv
source .venv/bin/activate

# Instala dependencias
uv pip install faker

# Desactiva
deactivate
```

## Usar el Proyecto

### Generar la Base de Datos

```bash
# Opción 1: Con uv run (recomendado)
uv run python generar_data.py

# Opción 2: Con script bash
bash run.sh

# Opción 3: Activar venv y ejecutar directo
source .venv/bin/activate
python generar_data.py
deactivate
```

### Ejecutar Consultas SQL Interactivas

```bash
# Con uv
uv run sqlite3 tienda.db

# O si tienes sqlite3 instalado globalmente
sqlite3 tienda.db
```

Ejemplo de consultas:
```sql
SELECT COUNT(*) as total_clientes FROM clientes;
SELECT COUNT(*) FROM ventas WHERE cupon_usado = 'ULTIMO_SUSPIRO';
SELECT nombre, precio FROM productos ORDER BY precio DESC LIMIT 5;
```

## Estructura de Archivos Clave

### `pyproject.toml`
Define la configuración del proyecto:
```toml
[project]
name = "taller-sql"
requires-python = ">=3.11"
dependencies = ["faker>=40.4.0"]
```

### `uv.lock`
Archivo generado automáticamente por uv que "congela" las versiones exactas:
- Garantiza que todos usen `faker 40.4.0` exactamente
- Asegura reproducibilidad entre máquinas

### `.venv/`
Directorio virtual de Python (creado automáticamente por uv)
- Contiene _todas_ las dependencias aisladas
- Seguro ignorar en Git (está en `.gitignore`)

## Troubleshooting

### Problema: "uv: command not found"

**Solución:**
```bash
# Verifica que está instalado
~/.local/bin/uv --version

# Agrega a tu PATH si es necesario
export PATH="$HOME/.local/bin:$PATH"

# O usa la ruta completa
~/.local/bin/uv run python generar_data.py
```

### Problema: "Python 3.11 not found"

**Solución:**
```bash
# uv descargará Python 3.11 automáticamente
uv sync --python 3.11

# O especifica explícitamente
uv --python 3.11 run python generar_data.py
```

### Problema: "Permission denied" en run.sh

**Solución:**
```bash
chmod +x run.sh
bash run.sh
```

### Problema: "tienda.db not found"

**Solución:**
```bash
# Regenera la base de datos
uv run python generar_data.py

# Verifica que se creó
ls -lh tienda.db
```

## Verificación de Instalación Exitosa

Corre este script de verificación:

```bash
#!/bin/bash
echo "Verificando instalación de uv..."

# 1. uv disponible
if ! command -v uv &> /dev/null; then
    echo "❌ uv no instalado"
    exit 1
fi
echo "✅ uv instalado"

# 2. Python 3.11 disponible via uv
if ! uv run python --version | grep -q "3.11"; then
    echo "❌ Python 3.11 no disponible"
    exit 1
fi
echo "✅ Python 3.11 disponible"

# 3. Dependencias
if ! uv run python -c "import faker" 2>/dev/null; then
    echo "❌ faker no instalado"
    exit 1
fi
echo "✅ faker instalado"

# 4. Base de datos
if [ ! -f "tienda.db" ]; then
    echo "⚠️  tienda.db no existe, generando..."
    uv run python generar_data.py
fi
echo "✅ tienda.db existe"

echo ""
echo "🎉 ¡Todas las verificaciones pasaron!"
```

Guárdalo como `verificar.sh` y ejecuta:
```bash
bash verificar.sh
```

## Próximos Pasos

1. **Genera la base de datos:**
   ```bash
   uv run python generar_data.py
   ```

2. **Lee el taller:** Abre [taller.md](taller.md)

3. **Resuelve los ejercicios:** Crea tus archivos `.sql` en `soluciones/`

4. **Version control:**
   ```bash
   git init
   git config user.name "Tu Nombre"
   git config user.email "tu@email.com"
   git add .
   git commit -m "Inicial: Taller SQL"
   ```

## Recursos Adicionales

- [uv Official Docs](https://docs.astral.sh/uv/)
- [uv GitHub](https://github.com/astral-sh/uv)
- [pyproject.toml Spec](https://packaging.python.org/en/latest/specifications/pyproject-toml/)

---

**¡Listo para comenzar! 🚀**
