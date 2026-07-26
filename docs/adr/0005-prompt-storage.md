# ADR-0005: Prompt Storage

- Estado: Accepted
- Fecha: 2026-07-25
- Responsables: AI Engineering Lead

## Contexto

GEEM AI Assistant utilizará prompts versionados para capacidades de
inteligencia artificial.

Los prompts forman parte del comportamiento del sistema y deberán poder:

- revisarse;
- versionarse;
- compararse;
- probarse;
- asociarse con evaluaciones;
- auditarse;
- desplegarse junto con cambios compatibles de código y contratos.

Durante la primera versión no se requiere que usuarios administrativos
modifiquen prompts dinámicamente desde la aplicación.

Introducir almacenamiento dinámico desde el inicio añadiría complejidad de
persistencia, autorización, historial, promoción entre ambientes y rollback sin
una necesidad operativa demostrada.

## Decisión

Git será la fuente de verdad inicial para los prompts de GEEM AI Assistant.

Los prompts se almacenarán como archivos versionados dentro del repositorio,
bajo una estructura perteneciente a AI Runtime.

Una ubicación conceptual será:

`src/geem_ai/ai_runtime/prompts/`

Cada prompt deberá tener una identidad estable mediante `prompt_key` y una
versión explícita.

La definición de un prompt deberá poder asociarse, cuando aplique, con:

- capability;
- template;
- variables schema;
- output schema;
- modelos soportados;
- estado;
- evaluación;
- metadata de versión.

Los estados conceptuales podrán incluir:

- draft;
- candidate;
- active;
- deprecated;
- retired.

La aplicación accederá a los prompts mediante un port `PromptRegistry`.

Los casos de uso no deberán leer archivos directamente ni conocer la ubicación
física de los prompts.

La implementación inicial de `PromptRegistry` podrá cargar definiciones desde
archivos versionados en Git durante el startup.

El contenido del prompt utilizado en una ejecución deberá poder identificarse
posteriormente mediante una referencia de versión estable.

Una base de datos podrá incorporarse en el futuro cuando exista una necesidad
demostrada de:

- administración dinámica;
- edición desde UI;
- activación sin deployment;
- workflows de aprobación;
- experimentación operativa;
- configuración específica por tenant.

La incorporación de almacenamiento dinámico requerirá una nueva decisión
arquitectónica o la revisión de este ADR.

## Alternativas consideradas

### Almacenar prompts en PostgreSQL desde el inicio

No se adopta inicialmente.

Permitirá administración dinámica, pero introduce prematuramente:

- CRUD administrativo;
- autorización;
- migración y seed de prompts;
- historial;
- promoción entre ambientes;
- rollback;
- sincronización con evaluación;
- riesgo de cambios no revisados mediante PR.

### Definir prompts directamente dentro del código Python

Rechazado.

Aunque seguirían versionados por Git, quedarían mezclados con lógica de
aplicación y serían más difíciles de revisar, comparar y evaluar como
artefactos independientes.

### Administrar prompts directamente en el proveedor AI

Rechazado como fuente de verdad principal.

Generaría dependencia del proveedor y dificultaría:

- portabilidad;
- revisión por Git;
- reproducibilidad;
- testing;
- trazabilidad de la versión ejecutada.

## Consecuencias

### Positivas

- historial y revisión mediante Git;
- cambios de prompt sujetos a Pull Request;
- rollback sencillo;
- comportamiento reproducible;
- fácil asociación entre código, prompt y evaluación;
- independencia del proveedor;
- menor complejidad operativa inicial.

### Negativas

- cambiar un prompt activo requiere inicialmente un cambio versionado y
  deployment;
- no existe edición dinámica desde UI;
- configuración específica por tenant será limitada mientras Git sea la única
  fuente de verdad;
- será necesario un loader y validación de definiciones.

## Riesgos

- modificar prompts sin actualizar sus evaluaciones;
- reutilizar una misma versión después de cambiar contenido;
- cargar un prompt inválido durante startup;
- perder trazabilidad entre una ejecución y la versión exacta del prompt;
- introducir secretos o información sensible en archivos versionados;
- permitir que Application dependa directamente del filesystem.

## Validación

La decisión se considerará correctamente aplicada cuando:

- los prompts iniciales estén versionados en Git;
- exista una estructura dedicada para prompts;
- cada prompt tenga `prompt_key` y versión;
- Application acceda mediante `PromptRegistry`;
- la implementación de filesystem permanezca en Infrastructure;
- una ejecución pueda registrar la referencia exacta del prompt utilizado;
- los cambios relevantes de prompt estén sujetos a revisión y evaluación;
- no existan secretos dentro de los prompts versionados.

## Referencias

- Documento 11 — Project 1 Architecture Definition
- Documento 13 — Project 1 API & Contract Standards
- Documento 15 — Project 1 Application Architecture
- Issue #7 — Establish initial ADR set