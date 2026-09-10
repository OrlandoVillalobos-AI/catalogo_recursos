"""Pruebas básicas de la estructura del proyecto.

Verifican que los archivos y carpetas principales existan y que el catálogo
de ejemplo sea un JSON válido.
"""

import json
import sys
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))


class TestEstructuraProyecto(unittest.TestCase):
    """Comprueba la existencia de los elementos de la estructura inicial."""

    def test_existen_directorios_principales(self):
        for nombre in ("app", "data", "docs", "docs/evidencias", "tests"):
            with self.subTest(directorio=nombre):
                self.assertTrue((RAIZ / nombre).is_dir(), f"Falta la carpeta {nombre}")

    def test_existen_archivos_principales(self):
        for nombre in (
            "README.md",
            "requirements.txt",
            "CHANGELOG.md",
            ".gitignore",
            "app/main.py",
            "app/configuracion.py",
            "data/recursos.json",
            "docs/alcance.md",
            "docs/criterios.md",
            "docs/respuestas.md",
        ):
            with self.subTest(archivo=nombre):
                self.assertTrue((RAIZ / nombre).is_file(), f"Falta el archivo {nombre}")

    def test_recursos_json_es_valido(self):
        contenido = (RAIZ / "data" / "recursos.json").read_text(encoding="utf-8")
        datos = json.loads(contenido)
        self.assertIn("recursos", datos)
        self.assertGreaterEqual(len(datos["recursos"]), 2)

    def test_cada_recurso_tiene_campos_obligatorios(self):
        datos = json.loads((RAIZ / "data" / "recursos.json").read_text(encoding="utf-8"))
        obligatorios = {"id", "titulo", "tipo", "tema", "nivel", "autor", "fuente"}
        for recurso in datos["recursos"]:
            with self.subTest(recurso=recurso.get("titulo")):
                self.assertTrue(obligatorios.issubset(recurso.keys()))

    def test_main_es_ejecutable(self):
        import importlib.util

        spec = importlib.util.spec_from_file_location("main", RAIZ / "app" / "main.py")
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)
        self.assertTrue(hasattr(modulo, "main"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
