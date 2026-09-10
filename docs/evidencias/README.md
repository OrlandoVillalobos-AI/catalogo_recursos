# Evidencias del desarrollo del flujo de trabajo

Esta carpeta reúne las evidencias del flujo completo de Git y GitHub seguido en la práctica
**Git y GitHub – Aplicación autónoma del flujo de trabajo**.

## Formato de las evidencias

Las capturas de pantalla solicitadas por la práctica se sustituyen por **transcripciones de
terminal**, que son evidencia verificable y auditable del flujo: no dependen de una captura manual,
se pueden reproducir ejecutando de nuevo los comandos y quedan versionadas junto al código.

Cada archivo registra los **comandos ejecutados** y su **salida real**, no una descripción de lo que
se pretendía hacer. Las evidencias que acreditan acciones realizadas en GitHub (Pull Requests,
revisiones, merges) se obtuvieron consultando la **API de GitHub** al momento de generar el archivo,
por lo que reflejan el estado real del repositorio remoto.

## Índice

| # | Archivo | Qué evidencia | Pasos de la práctica |
|---|---|---|---|
| 01 | `evidencia_01_estructura_proyecto.txt` | Estructura completa del proyecto | 1-4 (sección 4) |
| 02 | `evidencia_02_entorno_virtual.txt` | Entorno virtual `.venv` creado, activado y configurado | 5-9 (sección 5) |
| 03 | `evidencia_03_requirements.txt` | Dependencias instaladas y `requirements.txt` generado | 10-13 (sección 6) |
| 04 | `evidencia_04_historial_commits.txt` | Historial de commits del repositorio | 14-18 (sección 9) y sección 10 |
| 05 | `evidencia_05_repositorio_github.txt` | Repositorio publicado en GitHub; `.venv` ausente | 19-24 (sección 11) |
| 06 | `evidencia_06_fork.txt` | Copia de trabajo obtenida por `clone`; `.venv` debe reconstruirse | 25-34 (secciones 12-13) |
| 07 | `evidencia_07_rama_colaboracion.txt` | Rama `mejora-catalogo` y trabajo fuera de `main` | 35-46 (secciones 14-17) |
| 08 | `evidencia_08_pull_request.txt` | Pull Request #1: título, descripción, archivos y commits | sección 18 |
| 09 | `evidencia_09_request_changes.txt` | Solicitud de cambios y su atención sin crear otro PR | 47-53 (secciones 19-20) |
| 10 | `evidencia_10_merge.txt` | Aprobación, merge, sincronización local y reto final | 54-63 (secciones 21-23) |

## Correspondencia con los nombres sugeridos por la práctica

| Número | Nombre sugerido | Archivo entregado |
|---|---|---|
| 01 | `evidencia_01_estructura_proyecto.png` | `evidencia_01_estructura_proyecto.txt` |
| 02 | `evidencia_02_entorno_virtual.png` | `evidencia_02_entorno_virtual.txt` |
| 03 | `evidencia_03_requirements.png` | `evidencia_03_requirements.txt` |
| 04 | `evidencia_04_historial_commits.png` | `evidencia_04_historial_commits.txt` |
| 05 | `evidencia_05_repositorio_github.png` | `evidencia_05_repositorio_github.txt` |
| 06 | `evidencia_06_fork.png` | `evidencia_06_fork.txt` |
| 07 | `evidencia_07_rama_colaboracion.png` | `evidencia_07_rama_colaboracion.txt` |
| 08 | `evidencia_08_pull_request.png` | `evidencia_08_pull_request.txt` |
| 09 | `evidencia_09_request_changes.png` | `evidencia_09_request_changes.txt` |
| 10 | `evidencia_10_merge.png` | `evidencia_10_merge.txt` |

Se conservan los números y los nombres descriptivos para que la correspondencia con la práctica sea
directa.

## Cómo reproducir una evidencia

```bash
cd catalogo_recursos
source .venv/bin/activate
# leer la evidencia correspondiente y ejecutar los comandos que registra
```

## Enlaces verificables en GitHub

- Repositorio: https://github.com/OrlandoVillalobos-AI/catalogo_recursos
- Pull Request #1 (colaboración): https://github.com/OrlandoVillalobos-AI/catalogo_recursos/pull/1
- Pull Request #2 (reto final): https://github.com/OrlandoVillalobos-AI/catalogo_recursos/pull/2
- Rama de colaboración: https://github.com/OrlandoVillalobos-AI/catalogo_recursos/tree/mejora-catalogo
- Rama del reto final: https://github.com/OrlandoVillalobos-AI/catalogo_recursos/tree/actualiza-readme
- Historial de commits: https://github.com/OrlandoVillalobos-AI/catalogo_recursos/commits/main
