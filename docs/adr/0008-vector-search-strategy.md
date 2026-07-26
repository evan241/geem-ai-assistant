# ADR-0008: Vector Search Strategy

- Estado: Accepted
- Fecha: 2026-07-25
- Responsables: AI Engineering Lead

## Contexto

GEEM AI Assistant utilizará retrieval sobre conocimiento interno.

El sistema necesitará combinar señales semánticas y lexicales para recuperar
chunks relevantes de documentos autorizados.

Los embeddings deberán permanecer vinculados explícitamente con:

- tenant;
- document version;
- chunk;
- embedding model;
- embedding dimension;
- timestamps;
- estado de indexación.

La primera versión del producto no requiere introducir un vector database
independiente.

La estrategia debe priorizar:

- simplicidad operativa;
- aislamiento multi-tenant;
- trazabilidad;
- compatibilidad con PostgreSQL;
- posibilidad de combinar búsqueda lexical y vectorial;
- evolución basada en benchmarks reales.

## Decisión

PostgreSQL con pgvector será el vector store inicial de GEEM AI Assistant.

Los embeddings se almacenarán junto con metadata suficiente para identificar:

- tenant;
- documento;
- versión;
- chunk;
- modelo de embedding;
- dimensión;
- versión o estado de indexación cuando aplique.

No se mezclarán embeddings generados por modelos o dimensiones incompatibles
dentro de una misma estrategia de búsqueda sin control explícito.

La búsqueda vectorial inicial utilizará la estrategia más simple que cumpla los
objetivos de latencia y calidad.

Se priorizará inicialmente exact vector search mientras el volumen permita
cumplir los budgets definidos.

Los índices aproximados como HNSW o IVFFlat se introducirán únicamente cuando
benchmarks representativos demuestren una necesidad.

La selección entre estrategias considerará:

- volumen de chunks;
- cardinalidad por tenant;
- latencia p95;
- recall;
- costo de indexación;
- consumo de memoria;
- frecuencia de actualización;
- complejidad operativa.

PostgreSQL Full-Text Search será la primera opción para recuperación lexical.

La estrategia de retrieval podrá combinar:

- vector search;
- full-text search;
- filtros estructurados;
- autorización;
- tenant isolation.

La combinación o ranking híbrido pertenecerá a la capa de Retrieval y no se
delegará al almacenamiento como una decisión implícita.

Todo retrieval tenant-scoped deberá aplicar aislamiento antes de considerar
resultados como candidatos válidos.

## Alternativas consideradas

### Vector database dedicado desde el inicio

No se adopta inicialmente.

Introduciría:

- infraestructura adicional;
- sincronización entre PostgreSQL y vector store;
- más credenciales y networking;
- observabilidad adicional;
- mayor superficie operativa;
- riesgo de inconsistencias entre metadata y embeddings.

Podrá reconsiderarse si volumen, latencia o características especializadas
superan claramente la capacidad razonable de PostgreSQL + pgvector.

### HNSW desde el primer día

No se adopta como requisito inicial.

HNSW puede ofrecer excelente desempeño en búsquedas aproximadas, pero introduce
costos de memoria, construcción y mantenimiento que deben justificarse mediante
benchmarks.

### IVFFlat desde el primer día

No se adopta como requisito inicial.

Su eficacia depende de tuning, volumen y distribución de datos.

### Búsqueda exclusivamente vectorial

Rechazada.

Las consultas empresariales pueden contener:

- códigos;
- nombres;
- términos exactos;
- identificadores;
- frases específicas.

La recuperación lexical continuará siendo una señal relevante.

## Consecuencias

### Positivas

- menor infraestructura inicial;
- embeddings y metadata permanecen cerca de la fuente relacional;
- aislamiento tenant-aware más sencillo;
- backups y migraciones centralizados;
- posibilidad de combinar FTS y pgvector;
- evolución guiada por evidencia;
- menor riesgo de optimización prematura.

### Negativas

- PostgreSQL asumirá carga adicional de retrieval;
- exact search dejará de ser suficiente a cierto volumen;
- índices vectoriales requerirán tuning;
- algunos casos futuros podrían necesitar un vector store especializado;
- benchmarks deberán mantenerse representativos.

## Riesgos

- mezclar embeddings incompatibles;
- crear índices aproximados sin medir recall;
- ignorar filtros tenant-aware durante búsqueda vectorial;
- introducir un vector store externo sin estrategia de sincronización;
- optimizar únicamente latencia sacrificando calidad de retrieval;
- usar solamente similitud vectorial para consultas donde lexical search sea
  superior;
- reindexar documentos sin preservar trazabilidad de modelo y versión.

## Validación

La decisión se considerará correctamente aplicada cuando:

- pgvector esté habilitado mediante migración;
- los embeddings incluyan tenant, document version, chunk, model y dimension;
- embeddings incompatibles estén separados o controlados explícitamente;
- exista una implementación inicial de exact vector search;
- PostgreSQL Full-Text Search esté disponible para retrieval lexical;
- cualquier adopción de HNSW o IVFFlat esté respaldada por benchmarks;
- las pruebas de retrieval validen aislamiento por tenant;
- métricas permitan observar latencia, volumen y calidad de recuperación;
- sea posible reindexar una versión de documento sin perder trazabilidad.

## Referencias

- Documento 11 — Project 1 Architecture Definition
- Documento 14 — Project 1 Data Architecture
- Documento 15 — Project 1 Application Architecture
- Issue #7 — Establish initial ADR set
- Issue #10 — Enable pgvector extension