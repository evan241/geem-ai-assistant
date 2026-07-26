# AI Engineering Lab

## Documento 04 — Repository Standards

**Versión:** 1.0
**Estado:** Estándar oficial
**Responsable técnico:** Director de AI Engineering
**Lead Engineer:** Erick Eduardo Evangelista Velasco
## 1. Propósito

Este documento define los estándares oficiales para la creación, organización, mantenimiento y publicación
de los repositorios del AI Engineering Lab.
Su objetivo es garantizar que cada repositorio sea:
- comprensible;
- reproducible;
- mantenible;
- auditable;
- seguro;
- demostrable;
- profesional;
- defendible en entrevistas técnicas.
Los repositorios no serán utilizados únicamente como almacenamiento de código.
Cada repositorio deberá comunicar:
- qué problema resuelve;
- por qué fue construido;
- cómo está diseñado;
- cómo puede ejecutarse;
- qué decisiones técnicas se tomaron;
- cómo se evalúa;
- qué resultados produce;
- qué limitaciones mantiene.

## 2. Principio rector

Un repositorio profesional debe permitir que otra persona comprenda, ejecute, evalúe y
revise el proyecto sin depender de explicaciones privadas de su autor.
El código será solamente una parte del producto técnico.
También serán entregables:
- documentación;
- diagramas;
- decisiones;
- pruebas;
- automatización;
- evaluaciones;
- configuración;
- historial;
- releases;
- casos de estudio.
## 3. Repositorios oficiales

El laboratorio utilizará inicialmente los siguientes repositorios:
ai-engineering-playbook
geem-ai-assistant
restaurant-ai-operations
enterprise-automation-platform
ai-engineering-portfolio
## 4. Responsabilidad de cada repositorio

### 4.1. ai-engineering-playbook

Contendrá:
- estándares;
- Engineering Charter;
- Skills Matrix;
- Technology Strategy;

- Architecture Standards;
- Repository Standards;
- Definition of Done;
- Security Baseline;
- Evaluation Strategy;
- ADRs globales;
- plantillas;
- checklists;
- convenciones.
Este repositorio será la referencia de gobierno técnico del laboratorio.
No contendrá implementaciones completas de los productos.
### 4.2. geem-ai-assistant

Contendrá el producto:
- asistente empresarial;
- RAG;
- memoria;
- tools;
- MCP;
- knowledge management;
- evaluación;
- seguridad;
- observabilidad.
Será el primer proyecto principal y la base de componentes reutilizables.
### 4.3. restaurant-ai-operations

Contendrá:
- análisis de ventas;
- inventario;
- compras;
- inteligencia de menú;
- agentes;
- LangGraph;
- aprobaciones;
- reportes;
- evaluación multiagente.

### 4.4. enterprise-automation-platform

Contendrá:
- workflows;
- n8n;
- webhooks;
- integraciones;
- WhatsApp;
- correo;
- CRM;
- ERP;
- aprobaciones;
- auditoría;
- automatización con IA.
### 4.5. ai-engineering-portfolio

Contendrá la presentación pública del trabajo:
- casos de estudio;
- demos;
- diagramas;
- videos;
- fichas técnicas;
- narrativa profesional;
- enlaces;
- resultados;
- material para entrevistas.
No duplicará todo el código de los demás repositorios.
Referenciará sus releases y documentación pública.
## 5. Estrategia de repositorios separados

Decisión
Cada producto principal tendrá su propio repositorio.
Razones
- historial independiente;

- releases independientes;
- documentación enfocada;
- issues claros;
- demostración profesional;
- menor ruido;
- mejor presentación en GitHub.
Excepción
Dentro de cada producto podrá utilizarse un monorepo para agrupar:
- frontend;
- backend;
- workers;
- servidor MCP;
- paquetes compartidos;
- infraestructura.
## 6. Monorepo por producto

La estructura recomendada será:
project/
├── apps/
│ ├── api/
│ ├── web/
│ ├── worker/
│ └── mcp-server/
│
├── packages/
│ ├── domain/
│ ├── contracts/
│ ├── ai-core/
│ ├── observability/
│ └── shared/
│
├── tests/
├── docs/
├── infrastructure/
├── scripts/
├── docker/
├── .github/
├── .env.example
├── docker-compose.yml

├── Makefile
├── LICENSE
└── README.md
No todos los directorios deberán crearse desde el primer commit.
Se agregarán cuando exista una responsabilidad real.
## 7. Regla contra estructuras vacías

No se crearán decenas de carpetas vacías para simular una arquitectura avanzada.
Cada directorio deberá existir porque:
- contiene código;
- contiene documentación;
- existe una implementación próxima ya aprobada;
- forma parte de una estructura necesaria para tooling.
La arquitectura deberá crecer de manera controlada.
## 8. Convenciones de nombres de repositorios

Los nombres deberán:
- estar en minúsculas;
- usar kebab-case;
- ser claros;
- evitar abreviaturas innecesarias;
- evitar nombres temporales.
Correctos
geem-ai-assistant
restaurant-ai-operations
ai-engineering-playbook

Incorrectos
ProyectoIA
test-ai-v2
chatbot-final-final
geem_assistant_new
## 9. Visibilidad de repositorios

Cada repositorio podrá pasar por tres estados.
Private Development
Durante:
- definición inicial;
- manejo de información sensible;
- estabilización;
- limpieza de historial;
- pruebas internas.
Public Preview
Cuando:
- la arquitectura principal sea comprensible;
- no existan secretos;
- el README sea suficiente;
- exista instalación reproducible;
- se identifique claramente como versión preliminar.
Public Stable
Cuando:
- exista una release;
- la demo sea funcional;
- las pruebas pasen;
- la documentación esté actualizada;
- exista material de portafolio.

## 10. Reglas de publicación

Antes de hacer público un repositorio se deberá verificar:
- no contiene secretos;
- no contiene datos personales;
- no contiene información real de clientes;
- no contiene credenciales históricas;
- no contiene archivos innecesarios;
- tiene licencia;
- tiene README;
- tiene instrucciones;
- tiene capturas;
- tiene estado del proyecto;
- tiene limitaciones declaradas;
- tiene pruebas;
- tiene una release o versión identificable.
## 11. Licenciamiento

Cada repositorio público deberá incluir un archivo:
LICENSE
Estrategia inicial
Los proyectos demostrativos podrán utilizar una licencia permisiva cuando sea conveniente.
Candidatos:
- MIT;
- Apache License 2.0.
Restricción
El código que contenga propiedad intelectual exclusiva de Grupo GEEM no se publicará automáticamente.
Se podrán publicar:
- versiones sanitizadas;
- módulos genéricos;
- arquitectura;

- simuladores;
- datasets ficticios;
- interfaces;
- ejemplos.
La decisión final de licencia deberá documentarse por repositorio.
## 12. Propiedad intelectual y separación

Deberá distinguirse entre:
Código de portafolio
Diseñado para publicación y demostración.
Código empresarial privado
Contiene:
- reglas internas;
- datos reales;
- integraciones privadas;
- credenciales;
- procesos comerciales;
- propiedad intelectual reservada.
Componentes compartibles
Podrán extraerse siempre que:
- no expongan información sensible;
- no violen acuerdos;
- no revelen datos de clientes;
- tengan propósito educativo o profesional.
## 13. Rama principal

La rama principal será:
main

Representará siempre el estado:
- estable;
- integrado;
- revisado;
- potencialmente desplegable.
No deberá contener trabajo incompleto.
## 14. Uso de rama develop

La rama:
develop
será opcional.
Se utilizará cuando
- existan múltiples cambios paralelos;
- haya varios colaboradores;
- se necesite acumular una release;
- main deba permanecer estrictamente productiva.
No se utilizará cuando
- exista un solo desarrollador;
- las ramas sean pequeñas;
- haya despliegue continuo;
- los pull requests puedan integrarse directamente a main .
Estrategia inicial recomendada
Para Foundation y primeras versiones:
main
feature/*
fix/*
docs/*
Se evitará complejidad innecesaria.

## 15. Tipos de ramas

feature/*
fix/*
hotfix/*
refactor/*
docs/*
test/*
chore/*
spike/*
release/*
Ejemplos
feature/model-gateway-openai
feature/document-ingestion
fix/tenant-document-filter
refactor/tool-registry
docs/adr-pgvector-selection
test/rag-retrieval-evaluation
spike/qdrant-benchmark
release/0.1.0
## 16. Ramas cortas

Las ramas deberán:
- perseguir un objetivo específico;
- producir un cambio revisable;
- evitar mezclar responsabilidades;
- integrarse tan pronto como estén completas.
No deberán permanecer abiertas indefinidamente.
Una rama extensa indica que:
- la tarea es demasiado grande;
- falta dividir el trabajo;
- el diseño no está suficientemente claro.

## 17. Convención para nombres de ramas

Formato:
type/short-description
Reglas:
- minúsculas;
- kebab-case;
- sin acentos;
- sin espacios;
- descripción breve;
- sin nombres vagos.
Incorrectos
feature/cambios
fix/error
erick-pruebas
nueva-version
Correctos
feature/anthropic-provider
fix/tool-authorization-bypass
docs/security-threat-model
## 18. Convención de commits

Se utilizará Conventional Commits.
Tipos principales:
feat
fix
docs
refactor
test

perf
build
ci
chore
revert
Formato:
type(scope): imperative description
Ejemplos:
feat(gateway): add OpenAI response streaming
fix(retrieval): enforce tenant metadata filter
docs(adr): document modular monolith decision
test(tools): cover approval-required execution
refactor(memory): extract retention policy
ci(api): add Python type checking
## 19. Reglas de mensajes de commit

Los mensajes deberán:
- describir lo que cambia;
- utilizar una acción concreta;
- evitar textos genéricos;
- mencionar el módulo cuando sea útil;
- mantenerse comprensibles sin abrir el código.
Evitar
update
changes
fixes
working
final
more changes

Preferir
feat(knowledge): add document version tracking
fix(auth): reject expired organization membership
## 20. Atomic Commits

Cada commit deberá representar una unidad lógica.
Un commit no deberá mezclar:
- funcionalidad;
- refactor no relacionado;
- documentación diferente;
- configuración accidental;
- cambios de formato masivos.
Beneficios
- revisiones más claras;
- revert sencillo;
- historial útil;
- mejor debugging;
- mejor narrativa técnica.
## 21. Commits incompletos

Durante desarrollo local podrán existir commits intermedios.
Antes de integrar se podrá:
- reordenar;
- combinar;
- corregir mensajes;
- eliminar ruido.
El historial de main deberá permanecer comprensible.
No se realizará rebase sobre ramas compartidas sin coordinación.

## 22. Firma y autoría

Los commits deberán utilizar identidad profesional consistente.
La configuración deberá mantener:
- nombre real;
- correo asociado a GitHub;
- zona horaria correcta.
Cuando sea viable se utilizarán commits firmados.
Esto fortalece:
- autenticidad;
- trazabilidad;
- presentación profesional.
## 23. Pull Requests obligatorios

Todo cambio relevante deberá integrarse mediante Pull Request.
Incluso trabajando individualmente, los Pull Requests servirán para:
- revisión;
- disciplina;
- documentación;
- automatización;
- historial;
- práctica profesional.
Cambios menores exclusivamente documentales podrán usar un proceso simplificado, pero deberán
mantener CI cuando aplique.
## 24. Tamaño de Pull Requests

Un Pull Request deberá ser suficientemente pequeño para revisarse con claridad.
Ideal
- una funcionalidad;
- un bug;

- una decisión;
- un refactor acotado;
- una mejora de infraestructura.
Evitar
- múltiples módulos completos;
- cambios no relacionados;
- cientos de archivos sin explicación;
- funcionalidad y reformateo masivo juntos.
## 25. Título del Pull Request

Formato recomendado:
type(scope): concise result
Ejemplos:
feat(gateway): add Anthropic provider adapter
fix(retrieval): prevent cross-tenant search
docs(architecture): add RAG sequence diagram
## 26. Plantilla de Pull Request

Cada repositorio deberá incluir:
.github/pull_request_template.md
Contenido mínimo:
## Summary
Describe the purpose and result of this change.
## Problem
What problem does it solve?

## Solution
How was it implemented?
## Changes
- Change one
- Change two
## Testing
Explain how the change was validated.
## Security impact
Describe permissions, data, tools or integrations affected.
## AI behavior impact
Describe changes to models, prompts, retrieval, tools or evaluations.
## Evidence
Include logs, screenshots, metrics or evaluation results.
## Checklist
- [ ] Tests pass
- [ ] Documentation updated
- [ ] No secrets added
- [ ] Tenant isolation verified
- [ ] Observability included
- [ ] Evaluation updated when required
## 27. Revisión propia antes del PR

Antes de solicitar revisión, el autor deberá revisar el diff completo.
Deberá buscar:
- archivos accidentales;
- credenciales;
- código muerto;

- logs temporales;
- nombres incorrectos;
- comentarios obsoletos;
- pruebas faltantes;
- cambios de formato no intencionales;
- datos sensibles;
- prompts sin versión.
## 28. Requisitos de aprobación

Durante trabajo individual, una revisión formal podrá ser realizada mediante checklist y evidencia
automatizada.
Cuando existan colaboradores:
- al menos una aprobación para cambios ordinarios;
- aprobación del responsable técnico para arquitectura;
- revisión reforzada para seguridad;
- revisión reforzada para cambios de herramientas de alto impacto.
## 29. Branch Protection

La rama main deberá protegerse.
Políticas recomendadas:
- Pull Request obligatorio;
- CI obligatorio;
- ramas actualizadas;
- conversaciones resueltas;
- impedir force push;
- impedir eliminación;
- revisión de código cuando haya equipo;
- revisión de CODEOWNERS cuando aplique.
## 30. CODEOWNERS

Se utilizará:

.github/CODEOWNERS
cuando existan responsabilidades distribuidas.
Ejemplo:
/docs/architecture/ @architecture-owner
/src/modules/security/ @security-owner
/prompts/ @ai-owner
/infrastructure/ @platform-owner
En el inicio, Erick podrá ser propietario de todas las áreas, pero la estructura quedará preparada.
## 31. Issues

Todo trabajo mayor a un cambio trivial deberá relacionarse con un issue.
Los issues servirán para:
- definir problemas;
- registrar decisiones;
- establecer criterios;
- organizar milestones;
- documentar discusión;
- relacionar PRs.
## 32. Tipos de issues

Epic
Feature
Bug
Architecture
Security
Evaluation
Documentation
Technical Debt
Research Spike
Operations

## 33. Plantillas de issues

Cada repositorio deberá incluir plantillas en:
.github/ISSUE_TEMPLATE/
Plantillas iniciales:
feature.yml
bug.yml
architecture.yml
security.yml
evaluation.yml
research-spike.yml
## 34. Plantilla de Feature

Contenido mínimo:
## Problem
What user or business problem must be solved?
## User value
Who benefits and how?
## Scope
What is included?
## Out of scope
What is explicitly excluded?
## Acceptance criteria
- [ ] Criterion one
- [ ] Criterion two
## Architecture considerations

Modules, contracts, integrations and dependencies.
## Security considerations
Authentication, authorization, data and tool risks.
## Evaluation
How will quality be measured?
## Observability
What should be logged, traced or measured?
## 35. Plantilla de Bug

Debe incluir:
- descripción;
- comportamiento actual;
- comportamiento esperado;
- pasos para reproducir;
- ambiente;
- impacto;
- evidencia;
- logs sanitizados;
- hipótesis;
- regresión requerida.
## 36. Research Spikes

Las investigaciones técnicas deberán crearse como issues de tipo:
Research Spike
Ejemplos:
- comparar pgvector y Qdrant;
- evaluar SSE frente a WebSockets;
- comparar Celery y Dramatiq;

- probar modelos para clasificación;
- evaluar LangGraph frente a CrewAI.
Todo spike deberá tener
- pregunta;
- tiempo limitado;
- alternativas;
- experimento;
- métricas;
- resultado;
- recomendación;
- ADR cuando corresponda.
No se permitirá investigación indefinida sin decisión.
## 37. Epics

Los epics agruparán capacidades mayores.
Ejemplos para GEEM AI Assistant:
Foundation
Identity and Organizations
Knowledge Ingestion
Retrieval
Conversation
Tool Calling
Memory
MCP
Evaluation
Observability
Production Readiness
Portfolio Release
Cada epic deberá producir valor demostrable.
## 38. Milestones

Los milestones representarán entregas relevantes.
Ejemplo:

M0 — Repository Foundation
M1 — Model Gateway
M2 — Knowledge Ingestion
M3 — RAG Assistant
M4 — Tool Calling
M5 — Memory
M6 — MCP
M7 — Production Readiness
M8 — Public Portfolio Release
Un milestone no deberá ser solamente una fecha.
Deberá tener:
- objetivo;
- alcance;
- criterios de salida;
- issues relacionados;
- evidencia.
## 39. Labels

Se utilizará un conjunto consistente.
Tipo
type:feature
type:bug
type:architecture
type:security
type:evaluation
type:documentation
type:research
type:technical-debt
Prioridad
priority:critical
priority:high

priority:medium
priority:low
Estado
status:ready
status:blocked
status:in-progress
status:review
status:done
Área
area:api
area:web
area:ai
area:rag
area:tools
area:memory
area:mcp
area:security
area:platform
area:observability
## 40. Projects Board

Cada proyecto podrá utilizar un tablero con columnas:
Backlog
Ready
In Progress
Review
Blocked
Done
Límites de trabajo en progreso
Inicialmente:
- máximo una tarea principal de implementación;

- una tarea secundaria de documentación o investigación;
- no iniciar múltiples epics simultáneamente sin necesidad.
El objetivo es terminar antes de comenzar más trabajo.
## 41. Backlog

El backlog contendrá:
- nuevas ideas;
- mejoras;
- riesgos;
- deuda técnica;
- experimentos;
- oportunidades futuras.
Una idea registrada no implica compromiso inmediato.
Cada elemento deberá priorizarse según:
- valor;
- riesgo;
- dependencia;
- aprendizaje;
- impacto en portafolio;
- costo.
## 42. Definition of Ready para issues

Un issue estará listo cuando:
- el problema sea comprensible;
- exista objetivo;
- el alcance esté limitado;
- tenga criterios de aceptación;
- se conozcan dependencias;
- se hayan identificado riesgos;
- pueda estimarse su complejidad;
- exista evidencia esperada.
Los issues que no cumplan esto permanecerán en backlog.

## 43. Definition of Done para Pull Requests

Un PR estará terminado cuando:
- cumple criterios de aceptación;
- el código compila;
- el lint pasa;
- el type checking pasa;
- las pruebas pasan;
- se agregaron pruebas nuevas;
- la documentación está actualizada;
- no contiene secretos;
- la seguridad fue revisada;
- la observabilidad fue considerada;
- las evaluaciones fueron actualizadas cuando aplica;
- el CI está en verde;
- el cambio fue integrado.
## 44. Relación entre issues, ramas y PRs

Flujo:
Issue
│
▼
Branch
│
▼
Commits
│
▼
Pull Request
│
▼
CI and Review
│
▼
Merge
│
▼
Issue Closed
El PR deberá enlazar el issue mediante:

Closes #123
o
Relates to #123
## 45. Estrategia de merge

La estrategia inicial será:
Squash and Merge
Razón
- historial limpio;
- un cambio lógico por PR;
- mensaje claro;
- facilidad para revertir.
Excepciones
Se podrá utilizar Rebase and Merge cuando:
- los commits individuales sean valiosos;
- el historial esté bien construido;
- exista una razón técnica.
Se evitarán merge commits innecesarios.
## 46. Versionado semántico

Se utilizará Semantic Versioning:
MAJOR.MINOR.PATCH
Ejemplo:

1.4.2
MAJOR
Cambios incompatibles.
MINOR
Nuevas funcionalidades compatibles.
PATCH
Correcciones compatibles.
## 47. Versiones anteriores a 1.0

Durante desarrollo inicial:
0.1.0
0.2.0
0.3.0
La versión 1.0.0 deberá representar:
- funcionalidad principal estable;
- documentación;
- despliegue;
- seguridad;
- evaluación;
- observabilidad;
- demo;
- portafolio.
No se utilizará 1.0.0 únicamente porque el MVP funciona.

## 48. Releases

Cada release deberá incluir:
- versión;
- fecha;
- resumen;
- nuevas capacidades;
- correcciones;
- cambios incompatibles;
- instrucciones de migración;
- métricas relevantes;
- limitaciones;
- enlaces a documentación.
## 49. Changelog

Cada repositorio deberá mantener:
CHANGELOG.md
Formato recomendado:
# Changelog
## [Unreleased]
### Added
### Changed
### Fixed
### Security
## [0.2.0] - YYYY-MM-DD
Los cambios deberán registrarse durante el desarrollo, no reconstruirse al final.
## 50. Tags

Cada release deberá producir un tag:

v0.1.0
v0.2.0
v1.0.0
Los tags públicos deberán corresponder a estados reproducibles.
## 51. Release Candidates

Antes de releases importantes podrán utilizarse:
v1.0.0-rc.1
v1.0.0-rc.2
Esto permitirá validar:
- instalación;
- migraciones;
- despliegue;
- documentación;
- evaluación;
- demo.
## 52. Hotfixes

Los problemas críticos de producción podrán utilizar ramas:
hotfix/short-description
El hotfix deberá:
- incluir prueba de regresión;
- documentar causa;
- minimizar alcance;
- generar PATCH release;
- actualizar runbook cuando sea necesario.

## 53. README obligatorio

El archivo principal será:
README.md
Deberá ser útil para:
- reclutadores;
- ingenieros;
- arquitectos;
- evaluadores técnicos;
- usuarios interesados.
## 54. Estructura del README

# Project Name
One-sentence product definition.
## Problem
What business problem does it solve?
## Solution
How does the product solve it?
## Key capabilities
Main features.
## Architecture
High-level architecture and diagram.
## AI Engineering
Models, RAG, tools, agents, memory and evaluation.
## Security

Authentication, authorization and risk controls.
## Technology stack
Main technologies.
## Quick start
How to run it.
## Configuration
Required environment variables.
## Testing
How to execute tests.
## Evaluation
How AI quality is measured.
## Observability
How executions are traced.
## Demo
Screenshots, video or public deployment.
## Roadmap
Current and future milestones.
## Limitations
Known constraints.
## Documentation
Links to detailed documents.
## License

## 55. README para distintos públicos

Las primeras secciones deberán ser entendibles sin conocimientos profundos de IA.
El detalle técnico deberá aparecer posteriormente.
Orden recomendado:
- problema;
- valor;
- demo;
- capacidades;
- arquitectura;
- ingeniería;
- ejecución.
No se iniciará el README con una lista extensa de dependencias.
## 56. Badges

Se utilizarán badges únicamente cuando aporten información.
Ejemplos:
- build;
- tests;
- release;
- license;
- coverage;
- Python version.
No se llenará el README de insignias decorativas.
## 57. Capturas y demostraciones

Cada repositorio de producto deberá incluir:
- captura principal;
- interfaz relevante;
- diagrama;
- flujo;
- resultado de evaluación;
- 1.
2.
3.
4.
5.
6.
7.

video corto o GIF cuando sea útil.
Los recursos se almacenarán en:
docs/assets/
Deberán estar optimizados para repositorio.
## 58. Diagramas

Los diagramas deberán versionarse como código cuando sea posible.
Opciones:
- Mermaid;
- PlantUML;
- Structurizr DSL;
- archivos fuente de Excalidraw.
No se almacenará únicamente una imagen sin conservar su fuente editable.
## 59. Documentación del repositorio

Estructura:
docs/
├── product/
├── architecture/
├── adr/
├── api/
├── security/
├── evaluation/
├── operations/
├── interviews/
└── assets/
Cada documento deberá tener:
- título;
- objetivo;
- versión o fecha;

- estado;
- referencias relacionadas.
## 60. Architecture Decision Records

Ubicación:
docs/adr/
Formato:
ADR-0001-use-postgresql.md
ADR-0002-select-pgvector.md
Índice:
docs/adr/README.md
El índice deberá mostrar:
- número;
- título;
- estado;
- fecha;
- decisión sustituida.
## 61. Documentación de APIs

La especificación OpenAPI deberá:
- generarse automáticamente;
- mantenerse accesible;
- incluir autenticación;
- describir errores;
- incluir ejemplos;
- ocultar endpoints internos cuando corresponda.
Los contratos importantes podrán exportarse a:

docs/api/openapi.json
para releases.
## 62. Documentación de herramientas AI

Cada herramienta deberá documentar:
- objetivo;
- argumentos;
- respuesta;
- permisos;
- nivel de riesgo;
- aprobación;
- errores;
- idempotencia;
- auditoría.
Ubicación sugerida:
docs/ai/tools/
## 63. Documentación de prompts

Los prompts de producción deberán contar con:
- nombre;
- versión;
- objetivo;
- variables;
- outputs;
- pruebas;
- métricas;
- cambios.
No será necesario publicar prompts completos cuando exista riesgo de:
- seguridad;
- propiedad intelectual;
- abuso.

Podrá publicarse su arquitectura y propósito.
## 64. Datos de ejemplo

Los repositorios públicos podrán incluir:
examples/
fixtures/
sample-data/
Los datos deberán ser:
- ficticios;
- anonimizados;
- reproducibles;
- suficientes para ejecutar una demo.
Nunca se utilizarán exportaciones reales de clientes.
## 65. Datasets de evaluación

Ubicación:
tests/evaluation/datasets/
Deberán incluir:
- versión;
- origen;
- propósito;
- esquema;
- criterios;
- limitaciones.
Los datasets sensibles permanecerán privados.
Se podrá publicar una versión sanitizada.

## 66. Archivos ignorados

Cada repositorio deberá incluir .gitignore .
Deberá excluir:
- .env ;
- secretos;
- archivos temporales;
- entornos virtuales;
- dependencias;
- builds;
- caches;
- logs;
- archivos locales;
- datos privados;
- modelos pesados.
## 67. Environment Variables

El repositorio deberá incluir:
.env.example
Con:
- nombres;
- valores ficticios;
- comentarios mínimos;
- agrupación lógica.
Ejemplo:
APP_ENV=development
DATABASE_URL=postgresql://user:password@postgres:5432/app
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
REDIS_URL=redis://redis:6379/0
No se incluirán claves funcionales.

## 68. Gestión de secretos

Los secretos se almacenarán en:
- secret store del ambiente;
- GitHub Actions Secrets;
- plataforma de despliegue;
- gestor de secretos.
No deberán aparecer en:
- commits;
- issues;
- PRs;
- logs;
- screenshots;
- videos;
- archivos de configuración públicos.
## 69. Detección de secretos

El CI deberá incorporar una herramienta para detectar:
- API keys;
- tokens;
- contraseñas;
- certificados;
- credenciales cloud.
La detección deberá ejecutarse:
- antes del merge;
- sobre historial cuando se publique;
- localmente mediante pre-commit cuando sea posible.
## 70. Dependabot o sistema equivalente

Se activará automatización para detectar:
- vulnerabilidades;
- dependencias obsoletas;
- actualizaciones relevantes.

Las actualizaciones no se integrarán automáticamente sin pruebas.
## 71. Política de dependencias

Una dependencia deberá agregarse cuando:
- resuelva un problema real;
- tenga mantenimiento activo;
- su licencia sea compatible;
- su tamaño sea razonable;
- pueda probarse;
- no duplique funcionalidad ya disponible.
El PR deberá justificar dependencias importantes.
## 72. Lockfiles

Todo proyecto deberá mantener lockfiles.
Ejemplos:
uv.lock
poetry.lock
package-lock.json
pnpm-lock.yaml
No se eliminarán para resolver conflictos sin revisar consecuencias.
## 73. Automatización local

Cada repositorio deberá ofrecer comandos consistentes.
Ejemplo mediante Makefile :
make setup
make dev
make test
make lint
make typecheck

make evaluate
make build
make down
Esto reduce dependencia de conocimiento implícito.
## 74. Pre-commit Hooks

Se utilizarán hooks para:
- formato;
- lint;
- validación;
- secretos;
- archivos grandes;
- espacios;
- JSON/YAML;
- tipos cuando sea razonable.
Los hooks deberán ser rápidos.
Las pruebas completas permanecerán en CI.
## 75. GitHub Actions

Ubicación:
.github/workflows/
Workflows sugeridos:
ci.yml
security.yml
evaluation.yml
release.yml
container.yml
docs.yml

## 76. Pipeline de CI

El pipeline mínimo deberá ejecutar:
format-check
lint
type-check
unit-tests
integration-tests
security-scan
build
Cuando exista comportamiento AI:
evaluation-smoke-test
prompt-regression-check
tool-contract-tests
## 77. CI reproducible

El CI deberá:
- utilizar versiones fijas;
- instalar desde lockfiles;
- levantar servicios necesarios;
- evitar dependencias de estado local;
- guardar artifacts relevantes;
- mostrar errores comprensibles.
## 78. Artifacts de CI

Podrán conservarse:
- reportes de pruebas;
- cobertura;
- resultados de evaluación;
- OpenAPI;
- imágenes Docker;
- logs sanitizados;

reportes de seguridad.
Los artifacts no deberán contener secretos ni datos sensibles.
## 79. Code Coverage

La cobertura será una señal, no un objetivo absoluto.
Política
- módulos de dominio: cobertura alta;
- políticas de seguridad: cobertura alta;
- herramientas críticas: cobertura alta;
- infraestructura: cobertura razonable;
- UI visual: enfocarse en flujos.
No se escribirán pruebas sin valor únicamente para aumentar porcentaje.
## 80. Quality Gates

Un PR no podrá integrarse si:
- el build falla;
- el lint falla;
- los tipos fallan;
- las pruebas fallan;
- se detecta un secreto;
- existe vulnerabilidad crítica nueva;
- rompe evaluación mínima;
- afecta aislamiento de tenants;
- deja documentación crítica obsoleta.
## 81. GitHub Environments

Se configurarán ambientes:
development
staging
production

Los despliegues a producción deberán utilizar:
- protección;
- secretos separados;
- aprobación cuando corresponda;
- historial.
## 82. Estrategia de despliegue desde repositorio

Flujo recomendado:
Pull Request
│
▼
CI
│
▼
Merge to main
│
▼
Deploy to staging
│
▼
Validation
│
▼
Release tag
│
▼
Deploy to production
Durante primeras etapas, algunos pasos podrán ejecutarse manualmente, pero deberán documentarse.
## 83. Rollback

Cada release deberá poder revertirse.
Se deberá considerar:
- imagen anterior;
- tag anterior;

- migraciones;
- compatibilidad;
- configuración;
- prompts;
- modelos;
- índices;
- workflows.
Un cambio de prompt también puede requerir rollback.
## 84. Renovación de prompts y modelos

Los cambios de:
- modelo;
- proveedor;
- prompt;
- embeddings;
- retrieval;
- chunking;
- herramienta;
- deberán tratarse como cambios de comportamiento.
El PR deberá incluir:
- razón;
- evaluación anterior;
- evaluación nueva;
- costo;
- latencia;
- riesgos.
## 85. Seguridad de Pull Requests

Los PRs provenientes de forks no deberán acceder a secretos.
Los workflows deberán configurarse para evitar:
- ejecución arbitraria con secretos;
- exposición de tokens;
- publicación accidental;
- comandos no confiables.

## 86. Archivos grandes

No se almacenarán directamente en Git:
- modelos;
- dumps;
- videos grandes;
- datasets masivos;
- backups;
- archivos binarios generados.
Se utilizará:
- object storage;
- releases;
- Git LFS cuando esté justificado;
- enlaces documentados.
## 87. Git History Hygiene

Antes de publicar se verificará el historial para detectar:
- secretos eliminados pero aún presentes;
- datos reales;
- archivos pesados;
- mensajes inapropiados;
- código propietario;
- configuraciones privadas.
Eliminar un archivo en el último commit no lo elimina del historial.
## 88. Código generado por IA

El uso de herramientas de IA para apoyar programación está permitido.
Todo código generado deberá:
- revisarse;
- comprenderse;
- probarse;
- adaptarse;

- cumplir licencias;
- cumplir arquitectura;
- ser defendible.
No se integrará código que el responsable no pueda explicar.
## 89. Coautoría y atribución

Cuando una herramienta agregue coautoría automática, se decidirá conscientemente si conservarla.
La responsabilidad final del código permanecerá en el autor del PR.
No se atribuirá a una herramienta la responsabilidad de errores técnicos.
## 90. Comentarios de código

Los comentarios deberán explicar:
- por qué;
- restricción;
- decisión;
- riesgo;
- workaround.
No deberán repetir lo que el código ya expresa.
Los workarounds deberán enlazar:
- issue;
- ADR;
- documentación;
- fecha de revisión.
## 91. TODOs

Los TODOs deberán tener referencia.
Ejemplo:

TODO(#142): replace temporary in-memory checkpoint store
No se aceptarán TODOs indefinidos como:
TODO: improve this later
## 92. Deuda técnica

La deuda técnica deberá registrarse como issue.
Cada elemento deberá incluir:
- causa;
- impacto;
- riesgo;
- solución propuesta;
- prioridad;
- condición para resolverlo.
No toda deuda deberá resolverse inmediatamente.
Sí deberá ser visible.
## 93. Repository Health Files

Cada repositorio público deberá considerar:
CONTRIBUTING.md
CODE_OF_CONDUCT.md
SECURITY.md
SUPPORT.md
Requisitos iniciales
Como mínimo:

CONTRIBUTING.md
SECURITY.md
## 94. SECURITY.md

Deberá indicar:
- cómo reportar vulnerabilidades;
- qué información incluir;
- qué no publicar en issues;
- versiones soportadas;
- alcance de seguridad.
No se deberán discutir vulnerabilidades activas en issues públicos antes de resolverlas.
## 95. CONTRIBUTING.md

Deberá explicar:
- preparación del ambiente;
- ramas;
- commits;
- pruebas;
- Pull Requests;
- estilo;
- ADRs;
- seguridad;
- evaluaciones de IA.
## 96. Templates compartidas

El repositorio ai-engineering-playbook deberá ofrecer plantillas para:
- README;
- ADR;
- PR;
- issues;
- threat model;
- evaluación;
- runbook;

- postmortem;
- release notes.
Estas plantillas podrán copiarse a cada producto.
## 97. Postmortems

Los incidentes relevantes deberán documentarse.
Ubicación:
docs/operations/postmortems/
Formato:
- resumen;
- impacto;
- línea de tiempo;
- causa;
- factores contribuyentes;
- detección;
- resolución;
- acciones preventivas.
El objetivo será aprendizaje, no asignación de culpa.
## 98. Runbooks

Los flujos operativos importantes deberán contar con runbooks.
Ejemplos:
- proveedor de modelos caído;
- cola detenida;
- documentos sin indexar;
- embeddings corruptos;
- fuga de costos;
- tenant incorrecto;
- webhook duplicado;
- rollback de prompt.

## 99. Repository Scorecard

Antes de una release pública se evaluará:
Área Requisito
Problema Claramente explicado
Arquitectura Diagramada
Instalación Reproducible
Código Estructurado
Pruebas Automatizadas
Evaluación AI Documentada
Seguridad Revisada
Observabilidad Implementada
Demo Disponible
Release Versionada
Limitaciones Declaradas
Portafolio Caso de estudio preparado
## 100. Estándar de madurez del repositorio

Nivel 1 — Código local
- código funcional;
- sin estructura completa;
- instalación manual.
Nivel 2 — Colaborativo
- Git;
- issues;
- PRs;
- README;
- pruebas iniciales.

Nivel 3 — Reproducible
- Docker;
- CI;
- configuración;
- documentación.
Nivel 4 — Operable
- releases;
- seguridad;
- observabilidad;
- runbooks.
Nivel 5 — Portfolio Ready
- demo;
- caso de estudio;
- arquitectura;
- evaluación;
- video;
- narrativa defendible.
Los proyectos principales deberán alcanzar nivel 5.
## 101. Estrategia inicial de creación

El orden para crear cada repositorio será:
- crear repositorio privado;
- agregar README inicial;
- agregar licencia provisional;
- agregar .gitignore ;
- agregar .env.example ;
- configurar ramas;
- agregar plantillas;
- configurar CI mínimo;
- crear milestone inicial;
- crear issues Foundation;
- implementar primer vertical slice;
- preparar primera release interna.
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
12.

## 102. Primer commit

El primer commit no deberá contener una aplicación completa generada sin revisión.
Deberá establecer la base.
Ejemplo:
chore(repository): initialize project standards
Podrá incluir:
- README;
- LICENSE;
- .gitignore ;
- .editorconfig ;
- estructura mínima;
- plantillas;
- CI inicial.
## 103. Vertical Slice

La primera implementación deberá atravesar el sistema completo.
Ejemplo para GEEM AI Assistant:
User request
│
▼
FastAPI endpoint
│
▼
Application use case
│
▼
Model Gateway
│
▼
OpenAI provider
│
▼
Structured response

│
▼
React interface
Este vertical slice deberá ser pequeño, probado y observable.
Será preferible a construir muchas capas sin una funcionalidad ejecutable.
## 104. Repositorios de demostración secundaria

Los experimentos pequeños no deberán contaminar los repositorios principales.
Podrán ubicarse en:
experiments/
dentro del proyecto cuando estén relacionados.
O en repositorios separados cuando:
- tengan valor independiente;
- comparen tecnologías;
- sean publicables;
- no formen parte del producto.
No se creará un repositorio por cada prueba trivial.
## 105. Archive Policy

Un repositorio podrá archivarse cuando:
- el experimento terminó;
- fue sustituido;
- quedó obsoleto;
- ya no será mantenido.
Antes de archivarlo deberá indicar:
- motivo;
- alternativa vigente;
- última versión;

limitaciones.
## 106. Forks y dependencias externas

Cuando se modifique un proyecto externo:
- se documentará el origen;
- se respetará licencia;
- se mantendrán referencias;
- se evitará presentar trabajo ajeno como propio;
- se explicarán las contribuciones realizadas.
## 107. Evidencia para entrevistas

Cada repositorio deberá generar historias técnicas basadas en:
- issues;
- ADRs;
- Pull Requests;
- evaluaciones;
- incidentes;
- releases;
- decisiones.
La documentación no será solamente operativa.
También servirá para responder:
- ¿por qué elegiste esta arquitectura?;
- ¿qué salió mal?;
- ¿cómo mediste calidad?;
- ¿cómo aseguraste los tools?;
- ¿cómo preveniste acceso entre tenants?;
- ¿cómo controlaste costos?;
- ¿cómo hiciste rollback?;
¿qué cambiarías al escalar?

## 108. Actividad visible y calidad

No se intentará simular experiencia mediante:
- commits artificiales;
- actividad diaria vacía;
- repositorios incompletos;
- proyectos copiados;
- múltiples demos superficiales.
El perfil deberá reflejar trabajo real.
La calidad de los repositorios será más importante que la cantidad de contribuciones.
## 109. Idioma

Código
En inglés:
- variables;
- clases;
- funciones;
- commits;
- ramas;
- APIs;
- errores técnicos.
Documentación pública
Preferentemente en inglés para maximizar alcance internacional.
Podrán existir:
- versión principal en inglés;
- resúmenes en español;
- casos comerciales en español.
Documentación interna del laboratorio
Podrá mantenerse en español durante el desarrollo.
Antes de publicación se preparará la versión correspondiente.

## 110. Política de limpieza

Antes de cada release se eliminarán:
- código muerto;
- logs de prueba;
- archivos temporales;
- comentarios obsoletos;
- dependencias no utilizadas;
- feature flags vencidos;
- TODOs sin issue;
- configuraciones duplicadas.
## 111. Decisiones oficiales

Quedan aprobados los siguientes estándares:
Cada producto principal tendrá un repositorio independiente.
Cada producto podrá utilizar un monorepo interno.
main representará estado estable y desplegable.
develop será opcional y no se utilizará inicialmente sin necesidad.
Se utilizarán ramas cortas y específicas.
Los commits seguirán Conventional Commits.
Todo cambio relevante utilizará Pull Request.
Los PRs deberán incluir pruebas, seguridad y evidencia.
Los issues representarán trabajo real y criterios verificables.
Los milestones representarán entregas, no solamente fechas.
Se utilizará Semantic Versioning.
Cada release tendrá changelog y tag.
Todo repositorio público tendrá README profesional.
Los datos de clientes nunca se publicarán.
Los secretos serán detectados automáticamente.
CI será obligatorio antes de integrar cambios.
Los cambios de comportamiento AI deberán incluir evaluación.
Los repositorios principales deberán alcanzar madurez Portfolio Ready.
El código generado con asistencia AI deberá ser comprendido y defendible.
La calidad prevalecerá sobre la actividad artificial.
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
12.
13.
14.
15.
16.
17.
18.
19.
20.

## 112. Próximo documento

Documento 05 — Definition of Done
Definirá con precisión cuándo se considera terminado:
- un issue;
- un componente;
- un endpoint;
- una herramienta;
- un pipeline RAG;
- un agente;
- un workflow;
- un milestone;
- un proyecto;
- una release pública;
- un entregable de portafolio.
También establecerá:
- evidencias obligatorias;
- criterios de calidad;
- excepciones;
- gates;
- responsabilidades de aprobación.
## 113. Conclusión

Los repositorios del AI Engineering Lab deberán demostrar ingeniería profesional desde su estructura
hasta sus releases.
Cada uno deberá conservar:
- historial comprensible;
- decisiones visibles;
- cambios revisables;
- pruebas automáticas;
- seguridad;
- evaluación;
- documentación;
- operación reproducible;
- evidencia de producto.
El objetivo no será únicamente mostrar que Erick puede programar una solución con inteligencia artificial.

El objetivo será demostrar que puede dirigir técnicamente el ciclo completo de un producto de AI
Engineering:
- definición;
- arquitectura;
- implementación;
- revisión;
- evaluación;
- seguridad;
- despliegue;
- operación;
- mejora;
- comunicación profesional.
