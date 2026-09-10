# Criterios de clasificación de recursos académicos

Todo recurso que se incorpore al catálogo debe poder clasificarse con los siguientes criterios.
Cada uno define los valores admitidos.

## 1. Tipo de recurso

Define la naturaleza del material.

| Valor | Descripción |
|---|---|
| `libro` | Obra monográfica, impresa o digital. |
| `sitio_web` | Portal, blog o documentación en línea. |
| `video` | Clase, conferencia o tutorial audiovisual. |
| `articulo` | Artículo académico, de divulgación o técnico. |
| `software` | Herramienta, biblioteca o plataforma de software. |

## 2. Tema

Área de conocimiento del recurso. Valores sugeridos: `programacion`, `bases_de_datos`,
`redes`, `seguridad`, `inteligencia_artificial`, `matematicas`, `gestion_de_proyectos`.
El tema se registra en minúsculas y sin acentos para facilitar los filtros.

## 3. Nivel académico

Grado de profundidad o etapa de estudio para la que está pensado el recurso.

| Valor | Descripción |
|---|---|
| `introductorio` | No requiere conocimientos previos del tema. |
| `intermedio` | Requiere bases del tema. |
| `avanzado` | Requiere dominio previo y estudio especializado. |

## 4. Autor o fuente

Persona, institución o plataforma responsable del recurso. Debe registrarse el nombre
completo (o el nombre oficial de la institución) y, cuando exista, la URL de origen.

---

# Criterios adicionales

## 5. Idioma

Idioma principal del recurso, indicado con el código ISO 639-1 en minúsculas:
`es` (español), `en` (inglés), `pt` (portugués), `fr` (francés). Este criterio permite filtrar
el catálogo según el idioma de consulta del estudiante.

## 6. Licencia de uso

Condiciones bajo las cuales puede utilizarse el recurso:

| Valor | Descripción |
|---|---|
| `abierta` | Dominio público o licencia libre (CC, GPL, MIT). |
| `institucional` | Acceso mediante suscripción de la universidad. |
| `restringida` | Requiere compra, registro o autorización del autor. |

Este criterio es indispensable para saber si un recurso puede compartirse dentro del catálogo
sin infringir derechos de autor.
