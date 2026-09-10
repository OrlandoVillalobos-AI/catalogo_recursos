# Changelog

Todos los cambios relevantes de este proyecto se documentan en este archivo.
El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/).

## [0.1.0] - 2026-09-10

### Añadido

- Creación de la estructura inicial del proyecto `catalogo_recursos`.
- Carpetas `app/`, `data/`, `docs/`, `docs/evidencias/` y `tests/`.
- Archivos base: `README.md`, `requirements.txt`, `.gitignore` y `CHANGELOG.md`.
- Documentación inicial en `docs/alcance.md` y `docs/criterios.md`.
- Catálogo de ejemplo con dos registros en `data/recursos.json`.
- Punto de entrada `app/main.py` con salida identificadora del proyecto.

## [0.1.1] - 2026-09-10

### Añadido

- Documentación adicional: `docs/fuentes_recomendadas.md` con ocho plataformas de recursos
  académicos.
- Criterios 7 y 8 de clasificación (formato del archivo y vigencia del recurso) en
  `docs/criterios.md`.

### Cambiado

- Se amplía la documentación del proyecto sin modificar el código de la aplicación.

## [0.1.2] - 2026-09-10

### Añadido

- Sección *Tipos de recursos* en `README.md`, con los cinco tipos de recurso del catálogo y su
  correspondencia con los registros de ejemplo.

## [0.1.3] - 2026-09-10

### Añadido

- Carpeta `docs/evidencias/` con los diez archivos de evidencia del flujo de trabajo y su índice
  en `docs/evidencias/README.md`.
- Referencia al índice de evidencias en `docs/respuestas.md`.

## [0.2.0] - 2026-09-10

### Añadido

- Nuevo archivo `docs/fuentes_recomendadas.md` con ocho plataformas de recursos académicos, cada una
  con su URL, qué aporta y para qué sirve.
- Criterios 9 (costo de acceso) y 10 (subtítulos o traducción) en `docs/criterios.md`.

### Cambiado

- Se amplía la documentación del proyecto. No se modifica el código de la aplicación.
- **Atendida la observación de la revisión:** el valor `institucional` del criterio 9 se renombra a
  `cubierto_por_institucion` para no confundirse con el valor `institucional` del criterio 6
  (licencia de uso), que tiene un significado distinto.

## [0.2.1] - 2026-09-10

### Añadido

- Sección *Tipos de recursos* en `README.md`, con la descripción de los cinco tipos de recurso del
  catálogo, su nivel habitual y las fuentes típicas de cada uno. (Reto final de la práctica.)
