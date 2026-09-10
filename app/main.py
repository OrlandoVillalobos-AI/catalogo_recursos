"""Punto de entrada del Catálogo de recursos académicos.

En esta etapa el proyecto solo define su estructura. Este módulo imprime una
salida sencilla que identifica el proyecto.
"""

NOMBRE_PROYECTO = "Catálogo de recursos académicos"
VERSION = "0.1.0"
DESCRIPCION = "Estructura inicial de un catálogo de recursos académicos."


def main() -> None:
    """Imprime la identificación del proyecto."""
    print("=" * 50)
    print(f"  {NOMBRE_PROYECTO}")
    print(f"  Versión: {VERSION}")
    print("=" * 50)
    print(DESCRIPCION)
    print("Estructura inicial preparada. La aplicación aún no está implementada.")


if __name__ == "__main__":
    main()
