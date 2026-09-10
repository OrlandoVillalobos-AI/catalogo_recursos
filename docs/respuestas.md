# Respuestas de la práctica

Práctica: **Git y GitHub – Aplicación autónoma del flujo de trabajo**
Desarrollo de Aplicaciones y Servicios Virtuales — Universidad Iberoamericana León.

Las capturas que evidencian cada paso se encuentran en `docs/evidencias/`. El índice completo con la
correspondencia entre cada archivo de evidencia y los pasos de la práctica está en
`docs/evidencias/README.md`.

---

## Preguntas de control

### ¿Qué ventaja tiene registrar las dependencias del proyecto en requirements.txt en lugar de compartir la carpeta .venv?

**Ventaja principal: portabilidad y reproducibilidad sin arrastrar archivos que no pertenecen al
código fuente.**

1. **Tamaño y peso.** `.venv/` contiene miles de archivos y cientos de megabytes de binarios
   compilados para un sistema operativo y una versión de Python concretos. `requirements.txt` es un
   archivo de texto de unos cuantos renglones con el que se obtiene el mismo resultado.

2. **Portabilidad entre sistemas.** Las rutas absolutas y los binarios de `.venv/` quedan ligados
   al equipo donde se creó: otro sistema operativo, otra arquitectura o incluso otra versión de
   Python puede no ser capaz de ejecutarlo. `requirements.txt` se resuelve en el equipo destino
   instalando la versión correcta de cada paquete para esa plataforma.

3. **Control de versiones sano.** Meter `.venv/` al repositorio generaría diffs enormes, ruido en
   cada commit e historial ilegible, además de conflictos imposibles de resolver a mano. Con
   `requirements.txt` cada cambio de dependencia es una línea de diferencia, revisable en un Pull
   Request.

4. **Seguridad.** Dentro de `.venv/` pueden quedar archivos con credenciales o rutas internas del
   equipo. Mantenerlo fuera del repositorio evita publicar información que no debe salir de la
   máquina.

5. **Instalación en un paso.** Cualquier integrante reproduce el entorno exacto con
   `pip install -r requirements.txt`, sin depender de que alguien le copie su carpeta.

Por eso la práctica exige que `.venv/` esté declarado en `.gitignore` y que las dependencias se
declaren en `requirements.txt`: **el entorno se reconstruye, no se comparte.**

---

### ¿Por qué el repositorio que tienes ahora en tu computadora no es el mismo concepto que el fork creado en GitHub?

Porque son **dos cosas distintas en dos capas distintas**: el fork es una copia del repositorio en
la nube, y el repositorio local es la copia de trabajo con la que se editan archivos.

1. **El fork vive en GitHub, no en la computadora.** Un fork es una copia completa del repositorio
   original (con sus commits e historial) creada **dentro de la cuenta de GitHub de la persona
   colaboradora**. Es un repositorio remoto: existe en los servidores de GitHub y no tiene archivos
   de trabajo ni ramas locales.

2. **El repositorio local es una copia de trabajo.** Al ejecutar `git clone` se descarga una copia
   del fork a la computadora. Esa copia tiene *working directory*, índice y un `.git/` local donde
   se hacen los commits. Sin commits locales no hay nada que enviar.

3. **El fork guarda la relación con el original; el clon guarda la relación con el fork.** En
   GitHub, el fork recuerda de qué repositorio proviene, y eso es lo que permite abrir un Pull
   Request desde una rama del fork hacia `main` del repositorio original. En la computadora, el
   remoto `origin` apunta al fork de la persona colaboradora, y opcionalmente `upstream` apunta al
   repositorio del propietario. Son relaciones diferentes.

4. **Puede existir fork sin clon y clon sin fork.** Se puede hacer fork en GitHub y nunca descargarlo;
   se puede clonar el repositorio original directamente sin haber hecho fork. Son operaciones
   independientes que la práctica encadena: primero el fork (capa GitHub), después el clone (capa
   local).

**Conclusión.** El fork es la copia remota que permite proponer cambios sin tocar el repositorio del
propietario; el repositorio local es el espacio de trabajo donde realmente se editan y registran los
archivos. Para que un cambio llegue al proyecto original hace falta recorrer las dos capas:
commit local → push al fork → Pull Request → merge a `main` del original.

---

## Preguntas individuales

### 79. ¿Cómo identificaste el comando necesario cuando la práctica no lo proporcionó?

Traduciendo la **acción** descrita al verbo del flujo de Git, en lugar de memorizar comandos. El
procedimiento fue:

1. Identificar la **capa** sobre la que actúa la instrucción: ¿archivos locales, repositorio local o
   GitHub? Por ejemplo, "relaciona el repositorio local con el remoto" opera sobre la configuración
   local de Git.
2. Convertir la acción a su operación equivalente: *crear el repositorio* → `git init`; *consultar el
   estado* → `git status`; *preparar archivos* → `git add`; *registrar el cambio* → `git commit`.
3. Apoyarme en `git --help` y en `git <comando> --help` cuando la redacción no era evidente, y en
   `git status`, que en cada salida sugiere el comando siguiente.
4. Verificar el resultado de cada paso con el comando de consulta correspondiente (`git status`,
   `git log`, `git branch`, `git remote -v`) antes de avanzar al paso siguiente.

La clave es que la práctica describe **resultados esperados**, y casi todos se comprueban con un
comando de solo lectura. Si el resultado coincide con lo descrito, el comando elegido era el
correcto.

### 80. ¿Qué diferencia existe entre preparar un archivo para un commit y crear el commit?

Son dos momentos distintos del proceso, con el área de preparación (índice) entre ellos.

- **Preparar el archivo (`git add`)** copia el estado actual del archivo al **área de preparación**
  (staging area o índice). A partir de ese momento Git considera que ese cambio formará parte del
  próximo commit. El archivo pasa de "modificado" a "preparado para commit".

- **Crear el commit (`git commit`)** toma exactamente lo que está en el área de preparación y lo
  **guarda de forma permanente en el historial** del repositorio, generando un identificador único
  (hash SHA-1) y asociándole un mensaje descriptivo y un autor.

La diferencia práctica es el **control de granularidad**: separar los dos pasos permite decidir qué
cambios entran juntos y cuáles en otro commit. Un archivo puede tener cambios preparados y otros sin
preparar al mismo tiempo. Además, `git add` es reversible (`git restore --staged archivo`) y no deja
rastro en el historial; `git commit` ya es parte del historial del proyecto y solo se deshace con
`git reset` o `git revert`.

En esta práctica se aprovechó esa separación: los cambios de la colaboración se prepararon solo con
`git add docs/fuentes_recomendadas.md docs/criterios.md CHANGELOG.md`, dejando fuera cualquier otro
archivo para que el commit contuviera únicamente la aportación.

### 81. ¿Cómo puedes comprobar en qué rama estás trabajando?

Con `git branch`, que lista las ramas locales y marca con un asterisco la rama activa:

```bash
git branch
# * mejora-catalogo
#   main
```

También con `git status`, en cuya primera línea aparece la rama actual:

```
En la rama mejora-catalogo
```

Y de forma más breve, `git branch --show-current`, que imprime únicamente el nombre de la rama
activa. Si además se quiere saber a qué rama remota está enlazada la local, `git branch -vv` muestra
esa relación.

### 82. ¿Cómo puedes determinar qué archivos fueron modificados antes de registrarlos?

Con **`git status`**, que clasifica los archivos en tres grupos:

- **Modificados sin preparar** (rojo): ya existían y cambiaron, pero todavía no están en el índice.
- **Archivos nuevos sin seguimiento** (*untracked*): Git no los conoce aún; hay que añadirlos con
  `git add` antes de que puedan formar parte de un commit.
- **Preparados para el commit** (verde): lo que entrará en el próximo `git commit`.

Para saber qué archivos concretos cambiaron de forma resumida, `git status --short` muestra una
columna de estado por archivo (`M` modificado, `A` añadido, `??` sin seguimiento). En la práctica
este paso permitió distinguir que `docs/fuentes_recomendadas.md` era **nuevo** mientras que
`docs/criterios.md` y `CHANGELOG.md` eran **modificaciones**.

### 83. ¿Cómo puedes observar exactamente qué cambió dentro de un archivo?

Con **`git diff`**, que muestra las diferencias línea por línea usando el formato unificado: las
líneas eliminadas con `-` y las agregadas con `+`, junto con su contexto.

- `git diff` → diferencias entre el último commit y el directorio de trabajo (lo que **no** está
  preparado).
- `git diff --staged` → diferencias entre el último commit y el área de preparación (lo que **sí**
  se va a commitear). Es la revisión obligada antes de registrar.
- `git diff <commit1> <commit2>` o `git diff main..mejora-catalogo` → diferencias entre dos puntos
  del historial.
- `git diff -- palabra` → limita la salida al texto que contenga ese término.

Para revisar el detalle de un archivo ya commiteado se usa `git show <hash>:ruta/del/archivo`, y en
GitHub la pestaña *Files changed* del Pull Request ofrece la misma comparación en el navegador.

### 84. ¿Por qué debe reconstruirse .venv después de obtener un repositorio?

Porque **`.venv/` no viaja en el repositorio**: está declarado en `.gitignore`, así que al clonar el
proyecto esa carpeta simplemente no existe. Los motivos por los que se excluye y se reconstruye son:

1. **El entorno virtual es específico de la máquina.** Contiene enlaces simbólicos a la ruta absoluta
   del Python del equipo donde se creó y binarios compilados para un sistema operativo concreto. Un
   `.venv/` creado en otra máquina sería inservible, o produciría errores difíciles de diagnosticar.
2. **Es un artefacto derivado, no código fuente.** Todo lo que contiene se puede regenerar a partir de
   `requirements.txt`; guardarlo sería almacenar información redundante.
3. **Tamaño y ruido.** Son cientos de archivos y megabytes en cada clonación, lo que haría inmanejable
   el historial de cambios de dependencias.

Por eso el flujo correcto al obtener un repositorio es: `python3 -m venv .venv` → activarlo →
`pip install -r requirements.txt`. Así se obtiene un entorno equivalente, adaptado al equipo, sin
transportar binarios entre personas.

### 85. ¿Qué relación existe entre requirements.txt y .gitignore?

Son las **dos caras de la misma decisión**: qué se comparte y qué no.

- **`.gitignore` excluye `.venv/`** del repositorio. Le dice a Git: *esta carpeta no se versiona,
  no la consideres parte del proyecto*.
- **`requirements.txt` se versiona y se comparte** en su lugar. Le dice a las demás personas: *estas
  son las dependencias exactas que necesitas para reconstruir el entorno*.

La relación es de **sustitución**: `requirements.txt` es el sustituto portable de `.venv/`. Si se
eliminara `.venv/` del `.gitignore` y se subiera al repositorio, `requirements.txt` perdería gran
parte de su sentido; si no existiera `requirements.txt`, excluir `.venv/` dejaría a quien clone el
proyecto sin forma de saber qué instalar.

En resumen: `.gitignore` define el **límite** de lo que se sube; `requirements.txt` garantiza que
excluir el entorno virtual no deje el proyecto inutilizable. Funcionan como un par y no tienen
sentido el uno sin el otro.

### 86. ¿Por qué la colaboración se realiza desde una rama y no directamente desde main?

Porque `main` es la **versión estable y publicable** del proyecto, y toda aportación debe pasar por
revisión antes de integrarse.

1. **Protege la estabilidad.** Si cada cambio se hiciera directo sobre `main`, cualquier error, archivo
   a medio escribir o experimento fallido quedaría en la rama principal, y quien clone el repositorio
   obtendría código roto.

2. **Permite revisar antes de integrar.** Una rama permite abrir un Pull Request: la persona
   propietaria puede ver las diferencias, pedir cambios y aprobar. Con commits directos en `main` no
   hay punto de revisión ni oportunidad de corregir antes de que el cambio sea definitivo.

3. **Aísla el trabajo en curso.** La rama `mejora-catalogo` contiene únicamente la aportación. Mientras
   no se integre, nadie más depende de ella; si el trabajo queda a medias, `main` sigue intacta.

4. **Habilita el rechazo limpio.** Si la aportación no se aprueba, basta con no integrarla (o cerrar el
   Pull Request) y borrar la rama. Si los commits estuvieran en `main`, habría que revertirlos
   generando commits de reversión en el historial principal.

5. **Facilita el trabajo paralelo.** Varias personas pueden trabajar simultáneamente en ramas distintas
   sin pisarse, y sus cambios se integran cuando estén listos.

En la práctica esto se comprobó explícitamente con el paso 43: verificar que el commit estaba en
`mejora-catalogo` y **no** en `main`. `main` solo recibió cambios en el momento del merge.

### 87. ¿Por qué una solicitud de cambios no requiere crear un Pull Request nuevo?

Porque un Pull Request **no es un cambio concreto, sino una comparación entre dos ramas** que
permanece abierta. Lo que se revisa es `mejora-catalogo` frente a `main`, no un commit específico.

Cuando se atiende la observación y se añaden commits nuevos a la misma rama, esa comparación se
recalcula automáticamente: el Pull Request existente incorpora los commits nuevos sin perder la
conversación ni el historial de revisión. Si se abriera un Pull Request nuevo, se duplicaría el
trabajo: aparecerían dos solicitudes para el mismo cambio, la revisión anterior quedaría huérfana y
la persona propietaria perdería el contexto de qué se observó y cómo se atendió.

Para que esto funcione basta con:

1. Regresar a la misma rama (`git checkout mejora-catalogo`, o `git switch mejora-catalogo`).
2. Hacer el cambio y registrarlo con un commit nuevo.
3. Enviar la actualización al **mismo** remoto y la misma rama (`git push origin mejora-catalogo`).

Al hacer push, GitHub detecta los commits nuevos en la rama de origen y el Pull Request se actualiza
solo. El beneficio real es que **se conserva la trazabilidad**: queda registrado que hubo una
observación, cuál fue y con qué commit se resolvió, que es exactamente lo que demuestra el flujo de
colaboración.

### 88. Después de realizar el merge en GitHub, ¿por qué todavía es necesario actualizar el repositorio local?

Porque **el merge ocurre en el repositorio remoto de GitHub y el repositorio local no se enteró**.

Git no sincroniza automáticamente: los cambios que se integran en GitHub existen en el servidor, y la
copia local conserva el estado anterior hasta que se le indique lo contrario. En concreto:

1. **El merge se ejecutó sobre `main` remoto.** Desde la computadora del propietario, `main` local
   sigue apuntando al último commit que se conocía antes del merge, sin la aportación integrada.

2. **`git fetch` solo descarga objetos; no modifica la rama de trabajo.** Con `git pull` (fetch +
   merge) se traen los commits remotos y se actualiza la rama local activa.

3. **Los archivos nuevos no existen localmente hasta ese momento.** `docs/fuentes_recomendadas.md`,
   creado por la persona colaboradora, no está en el disco del equipo del propietario hasta que se
   sincroniza. Sin este paso, el repositorio local y el de GitHub estarían desalineados.

4. **Trabajar desincronizado genera conflictos.** Si se siguiera trabajando sobre un `main` local
   atrasado, los commits nuevos partirían de una base vieja y provocarían conflictos y divergencias
   al intentar publicar.

El orden correcto al cerrar el ciclo es: `git checkout main` (asegurarse de estar en la rama principal)
→ `git pull` (o `git fetch` + `git merge`) → `git log --oneline` para confirmar que el commit del merge
aparece y `git status` para verificar que el árbol está limpio.

---

## Nota sobre la forma de trabajo

La práctica indica trabajar en parejas con intercambio de roles. En este caso el flujo se ejecutó con
el propietario como responsable de `main` y el colaborador representado mediante una rama de trabajo
sobre el mismo repositorio (`mejora-catalogo`), documentando igualmente el ciclo completo de
aportación, revisión, solicitud de cambios, atención, aprobación y merge. La evidencia del ciclo
queda en los Pull Requests y en `docs/evidencias/`.
