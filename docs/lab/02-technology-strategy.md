# AI Engineering Lab

## Documento 02 — Technology Strategy

**Versión:** 1.0
**Estado:** Estrategia tecnológica inicial
**Responsable técnico:** Director de AI Engineering
**Lead Engineer:** Erick Eduardo Evangelista Velasco
Fecha de referencia: 19 de julio de 2026
## 1. Propósito

Este documento define la estrategia tecnológica oficial del AI Engineering Lab.
Su función es establecer:
- el stack base;
- las tecnologías aprobadas;
- las tecnologías experimentales;
- las tecnologías que no serán utilizadas inicialmente;
- los criterios para incorporar nuevas dependencias;
- la estrategia multi-modelo;
- las reglas de infraestructura;
- los estándares de interoperabilidad;
- el proceso para sustituir tecnologías.
La estrategia no busca acumular herramientas.
Busca construir productos:
- confiables;
- mantenibles;
- seguros;
- desplegables;
- evaluables;
- defendibles en entrevistas técnicas.
## 2. Principio central

Cada tecnología deberá justificar su presencia mediante una responsabilidad concreta dentro
del sistema.

Una tecnología no será incorporada solamente porque:
- aparece frecuentemente en vacantes;
- es popular;
- produce demostraciones atractivas;
- permite afirmar que fue utilizada;
- forma parte de un ecosistema conocido.
Toda incorporación deberá responder:
¿Qué problema resuelve?
¿Por qué la solución actual no es suficiente?
¿Qué costo de mantenimiento introduce?
¿Qué riesgo de dependencia genera?
¿Cómo será evaluada?
¿Cómo podrá sustituirse?
## 3. Clasificación tecnológica

Las tecnologías se clasificarán en cuatro categorías.
### 3.1. Core

Tecnologías oficiales sobre las que podrán construirse componentes de producción.
### 3.2. Supporting

Tecnologías auxiliares utilizadas para infraestructura, pruebas, desarrollo u operación.
### 3.3. Experimental

Tecnologías que se probarán en módulos aislados antes de aprobar su uso general.
### 3.4. Rejected or Deferred

Tecnologías descartadas inicialmente o pospuestas hasta que exista una necesidad demostrable.
1.
2.
3.
4.
5.
6.

## 4. Stack oficial consolidado

Área Tecnología oficial Clasificación
Lenguaje principal de IA Python Core
Backend de IA FastAPI Core
Validación y contratos Pydantic Core
ORM SQLAlchemy Core
Migraciones Alembic Core
Frontend React + TypeScript Core
Aplicación web Vite o Next.js según caso Core
Base de datos PostgreSQL Core
Búsqueda vectorial pgvector Core
Cache y estado efímero Redis Core
Modelos generativos OpenAI y Anthropic Core
Orquestación agéntica LangGraph Core para P2
Automatización n8n Core para P3
Integración de herramientas Tool calling Core
Protocolo interoperable MCP Core desde P1
Contenedores Docker Core
Desarrollo local Docker Compose Core
CI/CD GitHub Actions Core
Observabilidad OpenTelemetry Core
Testing backend Pytest Core
Testing frontend Vitest Core
Testing E2E Playwright Core
Documentación API OpenAPI Core
Autenticación OAuth 2.0 / OIDC / JWT Core
Almacenamiento documental Compatible con S3 Supporting
Framework general LLM LangChain Supporting

Área Tecnología oficial Clasificación
Framework multiagente CrewAI Experimental
Vector DB especializada Qdrant Experimental
Automatización durable Temporal Experimental
Kubernetes Diferido Deferred
## 5. Lenguaje principal: Python

Decisión
Python será el lenguaje principal para:
- orquestación de modelos;
- pipelines RAG;
- procesamiento documental;
- embeddings;
- evaluación;
- agentes;
- herramientas de IA;
- workers;
- análisis de datos;
- experimentación controlada.
Justificación
Python concentra el ecosistema más amplio para:
- inteligencia artificial;
- procesamiento de lenguaje;
- evaluación;
- agentes;
- búsqueda vectorial;
- integración de modelos;
- análisis de datos.
Además, permite mantener cercanía entre:
- prototipos;
- evaluaciones;
- APIs;
- procesos asíncronos;
- servicios productivos.

Restricción
Python no reemplazará automáticamente:
- Laravel;
- PHP;
- Node.js;
- servicios transaccionales existentes;
- aplicaciones donde ya exista una base estable.
La estrategia será integrar, no reescribir sin necesidad.
Nivel esperado
El laboratorio exigirá Python de producción:
- tipado;
- pruebas;
- linting;
- async;
- manejo de errores;
- profiling;
- packaging;
- observabilidad;
- seguridad.
No se aceptará código basado únicamente en notebooks.
## 6. Backend de IA: FastAPI

Decisión
FastAPI será el framework principal para servicios nuevos relacionados con inteligencia artificial.
Responsabilidades
- API de conversación;
- model gateway;
- retrieval service;
- memory service;
- tool registry;
- evaluation API;
- ingestion service;
- agent runtime;

- webhooks de IA;
- endpoints internos.
Justificación
FastAPI ofrece:
- integración natural con typing;
- validación mediante Pydantic;
- OpenAPI automático;
- soporte asíncrono;
- buen desempeño;
- estructura adecuada para APIs.
Regla
No toda lógica residirá en controladores.
La estructura deberá separar:
presentation
application
domain
infrastructure
ai
integration
## 7. Laravel y Node.js

Estado
Aprobados como tecnologías de integración y dominio empresarial.
Laravel
Se mantendrá como opción para:
- sistemas empresariales existentes;
- módulos transaccionales;
- administración;
- facturación;
- clientes;

- autenticación existente;
- servicios internos de GEEM;
- integración con Grest o GPOS.
Node.js
Se utilizará cuando resulte adecuado para:
- WebSockets;
- servicios locales;
- integraciones en tiempo real;
- aplicaciones JavaScript;
- comunicación con dispositivos;
- workers específicos;
- herramientas frontend compartidas.
Regla de arquitectura
Un servicio no será reescrito en Python solamente para declarar que forma parte de un producto de IA.
Los servicios AI podrán consumir APIs Laravel o Node.js mediante contratos explícitos.
## 8. Frontend: React y TypeScript

Decisión
React con TypeScript será el estándar de frontend.
Casos principales
- chat empresarial;
- panel de administración;
- visualización de fuentes;
- historial;
- aprobaciones humanas;
- herramientas ejecutadas;
- dashboard de evaluación;
- trazas;
- costos;
- configuración;
- gestión documental.

Vite vs Next.js
Vite
Se utilizará cuando:
- la aplicación sea principalmente privada;
- no se necesite renderizado del lado del servidor;
- el despliegue estático sea suficiente;
- se busque menor complejidad.
Next.js
Se utilizará cuando:
- exista contenido público;
- se requiera SSR;
- el portafolio necesite SEO;
- se requieran rutas híbridas;
- existan necesidades claras de server-side rendering.
Regla
No se elegirá Next.js por defecto.
Para paneles administrativos internos, React + Vite suele ser suficiente.
## 9. Base de datos: PostgreSQL

Decisión
PostgreSQL será la base de datos principal de los tres proyectos.
Responsabilidades
- usuarios;
- organizaciones;
- roles;
- permisos;
- conversaciones;
- documentos;
- metadata;
- memoria;
- herramientas;

- auditoría;
- configuraciones;
- evaluaciones;
- ejecuciones;
- costos;
- estados de workflows.
Justificación
PostgreSQL permite concentrar inicialmente:
- datos relacionales;
- full-text search;
- JSON;
- auditoría;
- metadata;
- búsqueda vectorial mediante pgvector.
Esto reduce la cantidad de componentes operativos durante las primeras versiones.
Estrategia multi-tenant
Se evaluarán tres modelos:
- tenant_id en tablas compartidas;
- esquemas separados;
- bases separadas.
Para el Proyecto 1 se iniciará con:
- tablas compartidas;
- tenant_id ;
- filtros obligatorios;
- políticas de acceso;
- pruebas de aislamiento.
Posteriormente se evaluará Row-Level Security.
## 10. Vector search: pgvector

Decisión
pgvector será la primera solución para búsqueda vectorial.
1.
2.
3.

pgvector permite almacenar vectores junto con los datos relacionales de PostgreSQL y soporta búsqueda
exacta y aproximada. También proporciona índices HNSW e IVFFlat. Su documentación señala que HNSW
ofrece generalmente un mejor equilibrio entre velocidad y recuperación, aunque requiere más memoria y
tiempo de construcción; IVFFlat construye más rápido y consume menos memoria, con un equilibrio menor
entre velocidad y recall.
Justificación
- menor complejidad operativa;
- datos y vectores en el mismo sistema;
- transacciones;
- filtros relacionales;
- backups unificados;
- menor infraestructura;
- integración sencilla con SQLAlchemy.
Estrategia inicial
Desarrollo y datasets pequeños
- búsqueda exacta;
- sin índice aproximado prematuro.
Crecimiento
- HNSW como primera opción;
- medición de recall;
- medición de latencia;
- comparación contra búsqueda exacta.
IVFFlat
Solo será utilizado cuando:
- el costo de construcción sea determinante;
- existan cargas masivas;
- su desempeño resulte mejor en pruebas reales.
Criterio de sustitución
pgvector será reevaluado si:
- la cantidad de vectores crece significativamente;
- los filtros afectan demasiado el recall;
- la latencia deja de cumplir los objetivos;
- se requiere clustering distribuido;
- se necesitan capacidades especializadas.

## 11. Vector database especializada: Qdrant

Clasificación
Experimental.
Razón
Qdrant será evaluado como alternativa especializada porque permite demostrar criterio sobre:
- filtros;
- índices;
- payloads;
- escalabilidad;
- separación entre datos transaccionales y retrieval.
Condición de adopción
No se incorporará a producción hasta comparar:
- latencia;
- recall;
- consumo de memoria;
- facilidad operativa;
- filtros;
- costo;
- recuperación;
- backups.
Resultado esperado
Crear un benchmark documentado:
ADR — pgvector vs Qdrant
La comparación será más valiosa profesionalmente que utilizar ambas sin justificación.

## 12. Redis

Decisión
Redis será utilizado para:
- cache;
- rate limiting;
- sesiones efímeras;
- locks;
- checkpoints temporales;
- colas ligeras;
- coordinación;
- datos con expiración.
Restricción
Redis no será fuente de verdad para información empresarial.
Los datos importantes deberán persistirse en PostgreSQL u otro almacenamiento durable.
## 13. Proveedores de modelos

Estrategia
El laboratorio trabajará inicialmente con:
- OpenAI;
- Anthropic.
No se pretende ocultar todas sus diferencias detrás de una abstracción universal.
Se implementará una interfaz común solo para capacidades compartidas.
Capacidades comunes
- generación de texto;
- streaming;
- structured outputs;
- tool calling;
- conteo de uso;
- manejo de errores;
- configuración;

trazabilidad.
Capacidades específicas
Cada proveedor podrá conservar adaptadores propios para:
- formatos particulares;
- caching;
- reasoning;
- tools;
- modelos;
- límites;
- opciones de seguridad;
- funcionalidades nativas.
Regla
No se utilizará un wrapper excesivamente genérico que impida aprovechar capacidades específicas.
## 14. OpenAI

Decisión
OpenAI será proveedor principal durante la fase Foundation y el Proyecto 1.
Uso previsto
- responses;
- structured outputs;
- tool calling;
- embeddings;
- streaming;
- evaluación comparativa;
- generación de respuestas;
- extracción estructurada.
Estrategia API
Se utilizarán las APIs actuales de OpenAI y no se iniciarán nuevos desarrollos sobre interfaces deprecadas.
La documentación actual agrupa en Responses API capacidades como creación y recuperación de
respuestas, entradas, conteo de tokens y uso de herramientas.

Regla
Todo uso deberá registrar:
- modelo;
- tokens;
- costo estimado;
- duración;
- solicitud;
- resultado;
- tool calls;
- errores;
- versión de prompt.
## 15. Anthropic

Decisión
Anthropic será el segundo proveedor oficial.
Objetivo
- evitar dependencia absoluta;
- comparar modelos;
- validar portabilidad;
- trabajar con MCP;
- evaluar diferentes comportamientos;
- construir fallbacks selectivos.
Política
No se utilizará Anthropic solamente como respaldo automático.
Se definirán casos donde sea útil por:
- calidad;
- contexto;
- razonamiento;
- costo;
- latencia;
- integración.

## 16. Model Gateway

Decisión
Se construirá un Model Gateway propio y ligero.
Responsabilidades
- seleccionar proveedor;
- seleccionar modelo;
- normalizar configuración;
- streaming;
- structured outputs;
- retries;
- timeouts;
- circuit breaking;
- trazas;
- costos;
- fallback controlado.
No deberá hacer
- ocultar diferencias importantes;
- transformar cualquier proveedor en una interfaz artificialmente idéntica;
- contener reglas de negocio;
- decidir permisos;
- almacenar prompts sin versión.
Contrato conceptual
ModelRequest
ModelResponse
StructuredResponse
ToolRequest
UsageMetadata
ProviderError
## 17. Structured Outputs

Decisión
Las salidas estructuradas serán obligatorias cuando una respuesta vaya a ser consumida por software.

Uso
- clasificación;
- extracción;
- reportes;
- decisiones;
- selección de herramientas;
- recomendaciones;
- planes;
- alertas;
- datos para interfaces.
Tecnología
- JSON Schema;
- Pydantic;
- validación estricta;
- reintentos limitados;
- manejo explícito de fallos.
Regla
No se analizarán respuestas empresariales críticas mediante expresiones regulares sobre texto libre.
## 18. Tool Calling

Decisión
Tool calling será el mecanismo oficial para conectar modelos con capacidades internas.
Cada herramienta deberá definir
- nombre;
- objetivo;
- argumentos;
- esquema;
- permisos;
- tenant;
- validaciones;
- timeout;
- idempotencia;
- efecto;
- nivel de riesgo;
- auditoría.

Clasificación de herramientas
Read-only
- consultar cliente;
- buscar documento;
- consultar ventas;
- consultar incidencia.
Controlled write
- crear tarea;
- preparar reporte;
- registrar borrador;
- actualizar estado no crítico.
High-impact
- enviar mensajes;
- modificar inventario;
- realizar compras;
- cancelar operaciones;
- aprobar gastos.
Las herramientas de alto impacto requerirán human-in-the-loop.
## 19. Model Context Protocol

Decisión
MCP será una tecnología oficial a partir del Proyecto 1.
MCP es un estándar abierto para conectar aplicaciones de IA con fuentes de datos, herramientas y
workflows externos. La especificación vigente lo define como un protocolo para integrar aplicaciones LLM
con sistemas externos, mientras que su documentación lo presenta como una interfaz estandarizada entre
aplicaciones AI y herramientas.
Uso previsto
Se construirá un servidor MCP para GEEM.
Podrá exponer:

Resources
- manuales;
- catálogos;
- procesos;
- documentación;
- información autorizada.
Tools
- consultar clientes;
- consultar servicios;
- consultar incidencias;
- generar reportes;
- crear seguimientos.
Regla de seguridad
MCP no elimina la necesidad de:
- autenticación;
- autorización;
- validación;
- auditoría;
- aislamiento;
- aprobación humana.
REST vs MCP
REST será utilizado para:
- aplicaciones empresariales convencionales;
- APIs públicas;
- operaciones transaccionales;
- integraciones explícitas.
MCP será utilizado para:
- ofrecer herramientas a clientes AI;
- exponer recursos;
- interoperabilidad con asistentes;
- integración estandarizada con agentes.

## 20. LangChain

Clasificación
Supporting.
Decisión
LangChain podrá utilizarse para:
- loaders;
- retrievers;
- integraciones;
- utilidades;
- componentes ya probados;
- compatibilidad con ecosistemas existentes.
Restricción
No se estructurará toda la aplicación alrededor de cadenas abstractas.
Razón
El dominio y las reglas críticas deben permanecer visibles, testeables y desacopladas.
## 21. LangGraph

Clasificación
Core para sistemas agénticos.
LangGraph se define oficialmente como un framework y runtime de orquestación de bajo nivel para
construir agentes persistentes, con estado y de larga duración. Su documentación recomienda comprender
primero modelos y herramientas antes de utilizarlo, lo cual coincide con la secuencia adoptada por el
laboratorio.
Uso
- workflows con estado;
- agentes;
- rutas condicionales;
- reanudación;

- checkpoints;
- ciclos controlados;
- human-in-the-loop;
- subgrafos;
- recuperación.
Regla
LangGraph no se utilizará para workflows completamente deterministas que puedan resolverse con código
convencional.
## 22. CrewAI

Clasificación
Experimental.
Objetivo
- conocer su paradigma;
- implementar un flujo acotado;
- comparar crews y flows;
- evaluar mantenibilidad;
- generar experiencia defendible.
Restricción
No será la base principal del Proyecto 2 sin que una evaluación demuestre ventajas claras frente a
LangGraph.
Entregable
ADR — LangGraph vs CrewAI
## 23. n8n

Clasificación
Core para Enterprise Automation Platform.

Uso
- webhooks;
- correo;
- WhatsApp;
- CRM;
- ERP;
- integraciones;
- scheduling;
- aprobaciones;
- coordinación de servicios;
- alertas;
- automatización.
Regla central
n8n coordinará procesos, pero no contendrá el núcleo de la lógica empresarial.
La lógica compleja deberá vivir en:
- servicios;
- APIs;
- módulos probados;
- funciones versionadas.
Motivo
Esto evita:
- workflows imposibles de probar;
- lógica duplicada;
- dependencia visual;
- mantenimiento difícil;
- cambios sin control de versiones.
## 24. Procesamiento asíncrono

Estrategia inicial
Se iniciará con una solución simple basada en:
- Redis;
- workers Python;
- tareas claramente definidas.

Casos de uso
- ingestión documental;
- embeddings;
- indexación;
- evaluaciones;
- reportes;
- llamadas prolongadas;
- envío de notificaciones.
Opciones
Celery
Aprobado como candidato por madurez y ecosistema.
Dramatiq
Aprobado como candidato por simplicidad.
Temporal
Experimental para workflows durables de larga duración.
Decisión
No se fijará Celery o Dramatiq hasta construir el primer proceso asíncrono real.
Se creará un ADR basado en:
- complejidad;
- retries;
- scheduling;
- observabilidad;
- recuperación;
- experiencia de desarrollo.
## 25. Observabilidad

Decisión
OpenTelemetry será el estándar transversal.

Señales
- traces;
- metrics;
- logs.
Datos de IA
- proveedor;
- modelo;
- prompt;
- versión;
- tokens;
- costo;
- latencia;
- tool calls;
- retrieval;
- errores;
- evaluaciones.
Herramientas especializadas
Se evaluarán:
- Langfuse;
- Phoenix;
- soluciones nativas de proveedor.
Estrategia
OpenTelemetry será la base neutral.
Una plataforma especializada podrá añadirse como visualización o análisis, pero no deberá convertirse en
el único lugar donde exista telemetría.
## 26. Evaluación

Decisión
La evaluación será un componente propio del sistema.
Tecnología inicial
- Pytest;

- datasets versionados;
- scripts de evaluación;
- métricas propias;
- evaluación humana;
- LLM-as-judge controlado.
Plataformas experimentales
Podrán evaluarse:
- promptfoo;
- DeepEval;
- Ragas;
- LangSmith;
- Phoenix evaluations.
Regla
Ninguna plataforma externa reemplazará:
- datasets propios;
- criterios de negocio;
- métricas verificables;
- revisión humana.
## 27. Seguridad

Stack
- OAuth 2.0;
- OpenID Connect;
- JWT;
- RBAC;
- auditoría;
- rate limiting;
- gestión de secretos;
- tenant isolation.
Seguridad de IA
- validación de outputs;
- delimitación de herramientas;
- prevención de prompt injection;
- detección de instrucciones maliciosas;

- separación entre contenido y órdenes;
- aprobación humana;
- least privilege;
- límites de ejecución.
Proveedores de identidad
Se evaluarán:
- Keycloak;
- Auth0;
- proveedor cloud;
- autenticación propia cuando sea suficiente.
Regla
No construiremos un sistema complejo de identidad propio sin necesidad.
## 28. Contenedores

Decisión
Docker será obligatorio en todos los proyectos.
Requisitos
- Dockerfile;
- imágenes multi-stage;
- usuario no root;
- health checks;
- variables de entorno;
- volúmenes;
- redes;
- límites;
- .dockerignore .
Docker Compose
Será el estándar para desarrollo local.
Servicios típicos:

frontend
api
worker
postgres
redis
object-storage
observability
## 29. Kubernetes

Clasificación
Deferred.
Razón
Kubernetes introduciría:
- mayor complejidad;
- operación adicional;
- costos;
- configuración;
- mantenimiento.
Criterio de adopción
Solo se utilizará si existe una necesidad real de:
- múltiples réplicas;
- autoescalado;
- despliegues complejos;
- alta disponibilidad;
- múltiples servicios;
- operación distribuida.
Utilizar Kubernetes únicamente para “ponerlo en el CV” sería una mala decisión.

## 30. CI/CD

Decisión
GitHub Actions será el estándar inicial.
Pipeline mínimo
lint
type-check
unit-tests
integration-tests
security-check
build
container-build
evaluation-smoke-test
Despliegue
Se establecerán ambientes:
- local;
- test;
- staging;
- production.
Regla
Los cambios de prompts y evaluaciones deberán pasar por CI cuando afecten comportamiento productivo.
## 31. Calidad de código

Python
- Ruff;
- Black cuando sea necesario;
- MyPy o Pyright;
- Pytest;
- pre-commit.

TypeScript
- ESLint;
- TypeScript strict;
- Prettier;
- Vitest;
- Playwright.
Seguridad
- dependencia automática;
- revisión de secretos;
- análisis de imágenes;
- actualización controlada.
## 32. Gestión de dependencias

Python
Se utilizará un gestor moderno y reproducible.
Candidatos:
- uv;
- Poetry.
Decisión inicial
Se evaluará uv durante Foundation.
Requisitos
- lockfile;
- versiones controladas;
- grupos de desarrollo;
- builds reproducibles;
- actualización programada.
JavaScript
- npm o pnpm;
- lockfile obligatorio;
- workspaces cuando exista monorepo.

## 33. Almacenamiento de documentos

Estrategia
Los archivos no deberán almacenarse directamente en la base de datos.
Se utilizará almacenamiento compatible con S3.
Desarrollo local
MinIO o almacenamiento local abstraído.
Producción
- proveedor S3 compatible;
- Amazon S3;
- Cloudflare R2;
- proveedor equivalente.
PostgreSQL almacenará
- metadata;
- permisos;
- versión;
- ubicación;
- checksum;
- estado de procesamiento.
## 34. Webhooks

Estándar
Todo webhook deberá implementar:
- validación de firma;
- timestamps;
- protección contra replay;
- idempotencia;
- retries;
- dead-letter handling;
- logs;
- correlación;

- respuesta rápida;
- procesamiento asíncrono.
Regla
Nunca se asumirá que un webhook llegará una sola vez.
## 35. API strategy

Estilo principal
REST con OpenAPI.
Posibles extensiones
- WebSockets para streaming;
- Server-Sent Events;
- webhooks;
- MCP;
- eventos internos.
GraphQL
Deferred.
Solo se considerará si existe un caso que lo justifique.
## 36. Estrategia de streaming

Uso
- respuestas de chat;
- ejecución de agentes;
- visualización de herramientas;
- estados;
- reportes prolongados.
Primera opción
Server-Sent Events cuando la comunicación sea principalmente servidor → cliente.

WebSockets
Se utilizarán cuando se necesite:
- comunicación bidireccional;
- eventos frecuentes;
- colaboración;
- dispositivos;
- control en tiempo real.
## 37. Arquitectura de servicios

Estrategia inicial
Modular monolith.
Razón
Permite:
- desarrollar más rápido;
- conservar transacciones;
- reducir operación;
- mantener límites de dominio;
- extraer servicios posteriormente.
Microservicios
Solo se extraerán cuando exista:
- escalado independiente;
- riesgo aislado;
- ciclo de despliegue diferente;
- carga especializada;
- frontera de dominio clara.

## 38. Tecnologías descartadas inicialmente

Fine-tuning como primera solución
No será utilizado antes de evaluar:
- prompting;
- RAG;
- tools;
- structured outputs.
Bases vectoriales múltiples
No se operarán varias bases en producción sin necesidad.
Agentes autónomos generales
No se construirán agentes con acceso amplio y objetivos abiertos.
Kubernetes
Pospuesto.
Microservicios prematuros
Descartados.
Modelos locales en producción inicial
Diferidos hasta disponer de:
- caso de privacidad;
- costo;
- latencia;
- infraestructura;
- evaluación.
Blockchain
Fuera de alcance.

## 39. Tecnologías futuras posibles

Podrán evaluarse posteriormente:
- modelos locales;
- vLLM;
- Ollama;
- Temporal;
- Qdrant;
- Kafka;
- Kubernetes;
- Terraform;
- cloud managed AI;
- multimodalidad;
- voice agents;
- computer vision;
- fine-tuning;
- synthetic data.
Estas tecnologías no forman parte del alcance inicial.
## 40. Proceso de incorporación tecnológica

Toda nueva tecnología seguirá:
Paso 1 — Problem Statement
Definir la limitación actual.
Paso 2 — Alternatives
Identificar mínimo dos opciones.
Paso 3 — Spike
Construir una prueba pequeña cuando sea necesario.
Paso 4 — Measurement
Medir:
- desempeño;
- costo;

- mantenibilidad;
- seguridad;
- complejidad.
Paso 5 — ADR
Registrar la decisión.
Paso 6 — Controlled Adoption
Incorporar primero en un módulo limitado.
Paso 7 — Review
Evaluar después de uso real.
## 41. Política de versiones

Regla general
No se fijarán versiones tecnológicas dentro de este documento porque cambian con rapidez.
Cada repositorio deberá registrar versiones exactas mediante:
- lockfiles;
- Docker images;
- .tool-versions ;
- documentación.
Actualización
Las dependencias se actualizarán:
- de forma controlada;
- con pruebas;
- con evaluación;
- sin actualizar producción automáticamente.

## 42. Estrategia de costos

Cada proveedor o servicio deberá registrar:
- costo por ejecución;
- costo por usuario;
- costo por documento;
- costo por workflow;
- costo mensual estimado.
Objetivos
- evitar sorpresas;
- comparar modelos;
- detectar prompts excesivos;
- medir eficiencia;
- justificar arquitectura.
Regla
No se optimizará únicamente por costo si eso destruye calidad.
Se buscará equilibrio entre:
- calidad;
- latencia;
- costo;
- seguridad.
## 43. Estrategia de portabilidad

Cada componente crítico deberá tener:
- interfaces;
- contratos;
- adaptadores;
- pruebas;
- configuración externa.
Componentes portables prioritarios
- model provider;
- embeddings provider;
- vector store;

- object storage;
- observability exporter;
- identity provider.
Restricción
No se crearán abstracciones preventivas para todo.
La portabilidad será aplicada donde exista riesgo real.
## 44. Stack por proyecto

Proyecto 1 — GEEM AI Assistant
Python
FastAPI
Pydantic
SQLAlchemy
PostgreSQL
pgvector
Redis
React
TypeScript
OpenAI
Anthropic
Tool Calling
MCP
Docker
OpenTelemetry
Pytest
Playwright
GitHub Actions
Proyecto 2 — Restaurant AI Operations
Python
FastAPI
PostgreSQL
Redis
LangGraph
OpenAI
Anthropic

React
Tool Calling
Human-in-the-loop
Evaluation
OpenTelemetry
Docker
CrewAI se utilizará únicamente en una implementación comparativa.
Proyecto 3 — Enterprise Automation Platform
n8n
FastAPI
PostgreSQL
Redis
React
WhatsApp API
Email APIs
CRM integrations
ERP integrations
OAuth
Webhooks
Docker
OpenTelemetry
## 45. Decisiones oficiales

Quedan aprobadas las siguientes decisiones:
Python será el lenguaje principal de AI Engineering.
FastAPI será el backend principal para servicios AI.
React y TypeScript serán el frontend estándar.
PostgreSQL será la base de datos principal.
pgvector será el vector store inicial.
Redis será utilizado para cache y estado efímero.
OpenAI y Anthropic serán los proveedores iniciales.
Se construirá un Model Gateway ligero.
Tool calling será el mecanismo principal de acciones.
MCP será incorporado durante el Proyecto 1.
LangGraph será el orquestador agéntico principal.
CrewAI será experimental.
n8n será el orquestador de automatización del Proyecto 3.
Docker y Docker Compose serán obligatorios.
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

GitHub Actions será el CI/CD inicial.
OpenTelemetry será la base de observabilidad.
La arquitectura inicial será modular monolith.
Kubernetes queda pospuesto.
Las bases vectoriales especializadas deberán demostrar su necesidad.
Toda incorporación tecnológica deberá documentarse mediante ADR.
## 46. Próximo documento

Documento 03 — Architecture Standards
Este documento definirá:
- arquitectura base;
- capas;
- límites;
- módulos;
- contratos;
- patrones;
- C4;
- secuencias;
- eventos;
- manejo de errores;
- multi-tenancy;
- seguridad;
- observabilidad;
- estructura de código.
## 47. Conclusión

La estrategia tecnológica del AI Engineering Lab queda basada en una combinación intencional de:
- Python para capacidades AI;
- tecnologías empresariales existentes para dominio y transacciones;
- PostgreSQL para reducir complejidad;
- tool calling para operaciones controladas;
- MCP para interoperabilidad;
- LangGraph para agentes con estado;
- n8n para automatización;
- Docker para reproducibilidad;
- OpenTelemetry para trazabilidad;
- evaluación como requisito de producción.
15.
16.
17.
18.
19.
20.

El stack no está diseñado para impresionar por cantidad.
Está diseñado para demostrar criterio de arquitectura, profundidad técnica y capacidad de construir
productos empresariales confiables impulsados por inteligencia artificial.
