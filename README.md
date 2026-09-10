# Catálogo de recursos académicos

Proyecto de la práctica **Git y GitHub – Aplicación autónoma del flujo de trabajo**
(Desarrollo de Aplicaciones y Servicios Virtuales, Universidad Iberoamericana León).

## Descripción

Aplicación que representa la estructura inicial de un sistema para **registrar y consultar
recursos académicos**: libros, sitios web, videos, artículos y herramientas de software.

En esta etapa el proyecto únicamente define su estructura de archivos, su documentación y su
flujo de trabajo con Git. La lógica de la aplicación todavía no está implementada.

## Objetivo

Dejar preparada la base de un catálogo de recursos académicos, aplicando de forma autónoma el
flujo completo de trabajo con Git y GitHub: preparación, versionamiento, ramas, colaboración
mediante fork, Pull Requests, revisión y sincronización.

## Estructura general

```
catalogo_recursos/
│
├── app/
│   ├── main.py               # Punto de entrada (salida sencilla)
│   └── configuracion.py      # Parámetros de configuración
│
├── data/
│   └── recursos.json         # Registros de ejemplo del catálogo
│
├── docs/
│   ├── alcance.md            # Alcance de una versión futura
│   ├── criterios.md          # Criterios de clasificación
│   ├── fuentes_recomendadas.md
│   ├── respuestas.md         # Respuestas de la práctica
│   └── evidencias/           # Capturas del desarrollo del flujo
│
├── tests/
│   └── test_basico.py        # Pruebas básicas de estructura
│
├── .gitignore
├── README.md
├── requirements.txt
└── CHANGELOG.md
```

## Tecnologías utilizadas

| Tecnología | Uso en el proyecto |
|---|---|
| Python 3 | Lenguaje de la aplicación |
| `requests` | Consumo de fuentes externas de recursos |
| `rich` | Salida formateada en terminal |
| JSON | Almacenamiento inicial del catálogo |
| Git / GitHub | Control de versiones y colaboración |
| Visual Studio Code | Entorno de desarrollo |

## Instrucciones para preparar el entorno

1. Clonar el repositorio y entrar a la carpeta:

   ```bash
   git clone <URL-del-repositorio>
   cd catalogo_recursos
   ```

2. Crear el entorno virtual:

   ```bash
   python3 -m venv .venv
   ```

3. Activarlo:

   ```bash
   source .venv/bin/activate      # Linux / macOS
   .venv\Scripts\activate         # Windows
   ```

4. Instalar las dependencias declaradas:

   ```bash
   pip install -r requirements.txt
   ```

5. En Visual Studio Code, seleccionar el intérprete ubicado en `.venv/`
   (`Ctrl+Shift+P` → *Python: Select Interpreter*).

## Dependencias

Las dependencias del proyecto se declaran en `requirements.txt`:

```
requests==2.32.5
rich==14.2.0
```

> La carpeta `.venv/` no se almacena en el repositorio: se reconstruye en cada equipo a partir de
> `requirements.txt`.

## Tipos de recursos

El catálogo contempla cinco tipos de recurso académico. Esta sección describe qué se registra en cada
uno, para qué sirve y de qué fuente suele provenir:

### 1. `libro`

Obra monográfica completa, impresa o digital. Es el tipo adecuado para estudio estructurado y
consulta de referencia: se registra con autor, editorial, año y edición.

### 2. `sitio_web`

Portal, blog o documentación en línea. Incluye documentación oficial de lenguajes y herramientas. Su
valor está en la actualización constante, por lo que conviene registrar la fecha de consulta.

### 3. `video`

Clase, conferencia o tutorial audiovisual. Útil para explicaciones paso a paso y demostraciones
prácticas. Se registra la duración y el idioma para saber si requiere subtítulos.

### 4. `articulo`

Artículo académico, de divulgación o técnico. Es el tipo habitual de la literatura científica y se
registra con DOI o URL permanente cuando existe.

### 5. `software`

Herramienta, biblioteca o plataforma. Incluye repositorios de código y entornos de trabajo. Se
registra la versión y la licencia para saber si puede usarse libremente.

### Resumen

| Tipo | Contenido | Nivel habitual | Fuentes típicas |
|---|---|---|---|
| `libro` | Obra monográfica | introductorio a avanzado | editoriales, bibliotecas |
| `sitio_web` | Documentación en línea | intermedio | documentación oficial |
| `video` | Clase o tutorial | introductorio | plataformas de cursos |
| `articulo` | Texto académico | avanzado | arXiv, Google Scholar |
| `software` | Código o herramienta | introductorio a avanzado | GitHub |

Cada recurso se clasifica además por tema, nivel académico, autor o fuente, idioma, licencia de uso,
formato del archivo, vigencia, costo de acceso y disponibilidad de subtítulos.

## Próximas mejoras

Cambios previstos para las siguientes versiones del proyecto:

- Implementar el alta de recursos con validación de los campos obligatorios.
- Añadir búsqueda y filtrado del catálogo por tipo, tema y nivel.
- Incorporar exportación del catálogo a formato CSV.
- Enriquecer los registros consultando fuentes académicas externas.
- Agregar pruebas automáticas para la lectura y escritura de `data/recursos.json`.
- Sustituir el almacenamiento en JSON por una base de datos cuando el catálogo crezca.
