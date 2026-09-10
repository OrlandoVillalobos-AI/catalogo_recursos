# Alcance del proyecto

## Alcance actual

En esta primera versión el proyecto **no implementa funcionalidad de negocio**. Su alcance se
limita a:

- Definir la estructura de carpetas y archivos del sistema.
- Documentar el objetivo, los criterios de clasificación y las fuentes de recursos.
- Preparar el entorno de desarrollo reproducible mediante `requirements.txt`.
- Establecer el flujo de trabajo en Git y GitHub.

## Alcance de una versión futura

Una versión posterior del sistema podría convertirse en un catálogo funcional de recursos
académicos. Como mínimo se contemplan las siguientes funcionalidades:

1. **Registrar recursos.** Alta de un recurso académico con sus datos: título, tipo, tema, nivel,
   autor o fuente, URL y fecha de consulta.

2. **Consultar y filtrar el catálogo.** Búsqueda de recursos por tipo (libro, sitio web, video,
   artículo, software), por tema y por nivel académico, mostrando los resultados en terminal.

3. **Validar y normalizar los registros.** Comprobación de que cada recurso cumple con los campos
   obligatorios definidos en `docs/criterios.md` antes de guardarlo, evitando duplicados por URL o
   por título.

4. **Importar y exportar el catálogo.** Lectura y escritura del catálogo en formato JSON, con
   posibilidad de exportar a CSV para su uso en hojas de cálculo.

5. **Enriquecer recursos desde fuentes externas.** Consulta automática de fuentes académicas
   (por ejemplo catálogos bibliográficos o repositorios abiertos) para completar metadatos como
   autor, año o editorial.

6. **Reportar estadísticas del catálogo.** Conteo de recursos por tipo, tema y nivel, para
   identificar vacíos de cobertura temática.

## Fuera de alcance por ahora

- Interfaz gráfica o aplicación web.
- Base de datos: el almacenamiento se mantiene en archivos JSON.
- Autenticación de usuarios y perfiles.
- Despliegue en servidor.

## Criterio de avance

Cada funcionalidad futura se desarrollará en una rama propia, se registrará con commits
descriptivos y se integrará a `main` mediante un Pull Request revisado. Sin revisión no hay
integración.
