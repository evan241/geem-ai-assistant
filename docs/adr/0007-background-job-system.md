# ADR-0007: Background Job System

- Estado: Accepted
- Fecha: 2026-07-25
- Responsables: AI Engineering Lead

## Contexto

GEEM AI Assistant ejecutará procesos asíncronos y potencialmente largos como:

- assistant executions;
- document ingestion;
- embedding generation;
- approval continuations;
- tool execution continuations;
- memory processing;
- evaluation jobs;
- maintenance tasks.

Estos procesos requieren más que ejecución en memoria.

Un job deberá poder tener:

- identidad;
- tenant;
- estado;
- intentos;
- timestamps;
- timeout;
- error;
- idempotencia;
- observabilidad;
- recuperación después de reinicios.

La pérdida de Redis, el reinicio de un worker o el despliegue de una nueva
versión no deberán provocar la pérdida silenciosa de trabajo empresarial
persistente.

La arquitectura necesita una estrategia inicial que priorice durabilidad,
simplicidad operativa y consistencia antes que throughput extremo.

## Decisión

PostgreSQL será la foundation inicial para coordinación durable de background
jobs y eventos internos asíncronos.

La transactional outbox se utilizará para publicar de forma durable eventos
producidos por transacciones de negocio.

Los jobs operativos podrán utilizar tablas persistentes específicas cuando su
modelo de ejecución requiera estado, lease, retries o scheduling independiente
del outbox.

La arquitectura utilizará transactional outbox para registrar trabajo
asíncrono relacionado con cambios de estado persistentes.

Cuando un caso de uso necesite producir trabajo asíncrono como consecuencia de
una transacción de negocio, el cambio de estado y su evento de outbox deberán
persistirse dentro de la misma transacción PostgreSQL.

Los workers reclamarán trabajo mediante operaciones transaccionales que eviten
procesamiento concurrente del mismo registro.

Cuando corresponda se utilizarán mecanismos PostgreSQL como:

`FOR UPDATE SKIP LOCKED`

Los jobs persistentes deberán registrar como mínimo, cuando aplique:

- job/event ID;
- tenant ID;
- job type;
- payload o referencia al payload;
- status;
- attempt count;
- created timestamp;
- available timestamp;
- started timestamp;
- completed timestamp;
- error information;
- idempotency information.

El procesamiento deberá asumir semántica de entrega:

`at-least-once`

Por lo tanto, los handlers deberán ser idempotentes o utilizar mecanismos
explícitos que hagan segura la repetición.

Los retries utilizarán políticas explícitas con:

- máximo de intentos;
- backoff;
- clasificación de errores retryable/non-retryable;
- timeout;
- estado terminal.

Los jobs que agoten su política de retry permanecerán persistidos como fallidos
para permitir diagnóstico y recuperación controlada.

Redis podrá utilizarse para capacidades efímeras como:

- cache;
- rate limiting;
- coordinación temporal;
- señales no durables.

Redis no será la fuente de verdad del estado de un job empresarial.

Los workers serán entry points de infraestructura.

La lógica de negocio continuará residiendo en Domain y Application. Un worker
resolverá el handler o caso de uso correspondiente y no implementará reglas de
negocio independientes.

La implementación deberá permanecer detrás de contratos que permitan incorporar
un broker dedicado en el futuro sin reescribir los casos de uso.

## Alternativas consideradas

### Redis-backed queue

Considerada debido a que Redis ya forma parte de la infraestructura.

No se adopta como foundation durable porque el proyecto requiere que el estado
empresarial persistente permanezca en PostgreSQL y que Redis pueda tratarse
como infraestructura reemplazable y no como fuente de verdad.

Redis podrá incorporarse posteriormente como mecanismo de distribución o
aceleración sin convertirse necesariamente en la fuente canónica del estado.

### Celery u otro task framework con broker dedicado

No se adopta inicialmente.

Proporcionaría funcionalidades maduras de scheduling, retries y distribución,
pero introduce:

- mayor complejidad operativa;
- configuración adicional;
- semántica propia de persistencia;
- infraestructura adicional;
- otra superficie de observabilidad.

Podrá reconsiderarse cuando throughput, scheduling o distribución justifiquen
el costo.

### Background tasks en memoria dentro de la API

Rechazadas para trabajo empresarial durable.

El trabajo podría perderse ante:

- reinicios;
- crashes;
- deployments;
- escalamiento horizontal.

Solo podrán utilizarse para operaciones efímeras donde la pérdida sea
explícitamente aceptable.

## Consecuencias

### Positivas

- trabajo durable en la fuente persistente principal;
- coordinación transaccional mediante outbox;
- menor infraestructura inicial;
- recuperación después de reinicios;
- auditoría sencilla;
- aislamiento tenant-aware;
- retries e idempotencia explícitos;
- desarrollo local sencillo.

### Negativas

- PostgreSQL recibe carga adicional de coordinación;
- polling deberá diseñarse cuidadosamente;
- throughput máximo será inferior al de brokers especializados;
- scheduling avanzado requerirá implementación o tooling adicional;
- será necesario controlar crecimiento y retención de tablas de jobs/outbox.

## Riesgos

- handlers no idempotentes;
- mantener locks durante llamadas externas largas;
- polling excesivo sobre PostgreSQL;
- jobs atascados en estado running después de un crash;
- retries infinitos;
- procesamiento cross-tenant incorrecto;
- crecimiento ilimitado de tablas de outbox/jobs;
- ejecutar lógica de negocio directamente dentro del worker;
- asumir semántica exactly-once donde realmente existe at-least-once.

## Validación

La decisión se considerará correctamente aplicada cuando:

- el trabajo durable sobreviva al reinicio de workers;
- los cambios de negocio y eventos relacionados utilicen transactional outbox
  cuando requieran atomicidad;
- dos workers no puedan reclamar simultáneamente el mismo job;
- los handlers sean idempotentes;
- exista recuperación de jobs abandonados;
- retries, backoff y estados terminales sean explícitos;
- cada job tenant-scoped preserve `tenant_id`;
- métricas permitan observar queue depth, processing time, retries y failures;
- Redis no sea necesario para reconstruir el estado durable de un job;
- los workers deleguen comportamiento a Application;
- la estrategia pueda evolucionar hacia un broker dedicado sin cambiar los
  casos de uso.
- los jobs reclamados utilicen lease o mecanismo equivalente que permita
  recuperar trabajo después de la caída de un worker;

## Referencias

- Documento 11 — Project 1 Architecture Definition
- Documento 14 — Project 1 Data Architecture
- Documento 15 — Project 1 Application Architecture
- Documento 16 — Project 1 Infrastructure Architecture
- Issue #7 — Establish initial ADR set