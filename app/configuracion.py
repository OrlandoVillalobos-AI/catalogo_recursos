"""Parámetros de configuración del proyecto.

Centraliza rutas y valores usados por la aplicación.
"""

from pathlib import Path

# Rutas base del proyecto
RAIZ_PROYECTO = Path(__file__).resolve().parent.parent
DIRECTORIO_DATOS = RAIZ_PROYECTO / "data"
DIRECTORIO_DOCS = RAIZ_PROYECTO / "docs"

# Archivo donde se almacena el catálogo
ARCHIVO_RECURSOS = DIRECTORIO_DATOS / "recursos.json"

# Codificación utilizada al leer y escribir archivos
CODIFICACION = "utf-8"

# Criterios admitidos para clasificar un recurso
TIPOS_VALIDOS = ("libro", "sitio_web", "video", "articulo", "software")
NIVELES_VALIDOS = ("introductorio", "intermedio", "avanzado")
