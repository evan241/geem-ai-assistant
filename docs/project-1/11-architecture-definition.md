# AI Engineering Lab

## Documento 11 --- Project 1 Architecture Definition

GEEM AI Assistant **Versión:** 1.0 **Estado:** Arquitectura oficial del
Proyecto 1 **Responsable técnico:** Director de AI Engineering **Lead
Engineer:** Erick Eduardo Evangelista Velasco **Estilo arquitectónico:**
Modular Monolith Backend principal: FastAPI Frontend principal: React +
TypeScript **Base de datos principal:** PostgreSQL + pgvector

## 1. Propósito

Este documento define la arquitectura específica de GEEM AI Assistant.

Su objetivo es transformar la definición de producto en una estructura
técnica concreta que permita:

-   implementar módulos de manera ordenada;
-   evitar acoplamiento innecesario;
-   proteger los límites del dominio;
-   integrar proveedores externos;
-   soportar inteligencia artificial;
-   controlar herramientas;
-   mantener aislamiento multi-tenant;
-   evaluar calidad;
-   operar el sistema;
-   reutilizar componentes en proyectos posteriores.

Este documento será la referencia técnica principal durante el
desarrollo del Proyecto 1.

## 2. Objetivos arquitectónicos

La arquitectura deberá permitir:

## 1. construir vertical slices completos;

## 2. mantener lógica empresarial independiente de frameworks;

## 3. sustituir proveedores AI;

## 4. separar comportamiento determinista de comportamiento probabilístico;

## 5. controlar acceso a datos y herramientas;

## 6. soportar multi-tenancy;

## 7. ejecutar procesos asíncronos;

## 8. rastrear cada operación;

## 9. evaluar componentes AI;

## 10. evolucionar sin adoptar microservicios prematuramente.

## 3. Principio rector

La inteligencia artificial será una capacidad dentro del sistema, no el
centro de toda la arquitectura.

Los módulos de negocio no deberán depender directamente de:

-   OpenAI;
-   Anthropic;
-   LangGraph;
-   pgvector;
-   Redis;
-   SDKs externos;
-   prompts concretos.

Las dependencias externas deberán permanecer detrás de interfaces y
adaptadores.

## 4. Estilo arquitectónico

El sistema utilizará:

Modular Monolith Esto significa que:

-   habrá una sola aplicación principal desplegable;
-   los módulos tendrán límites explícitos;
-   cada módulo tendrá responsabilidades propias;
-   la comunicación interna estará controlada;
-   la base de datos podrá ser compartida físicamente;
-   la propiedad lógica de tablas será por módulo;
-   los módulos no accederán directamente a tablas ajenas.

## 5. Razones para utilizar Modular Monolith

Se elige este estilo porque:

-   el equipo inicial es pequeño;
-   el producto aún está validándose;
-   se necesita velocidad de aprendizaje;
-   existen múltiples capacidades relacionadas;
-   evita complejidad operativa prematura;
-   facilita transacciones;
-   facilita pruebas;
-   mantiene posibilidad de extracción futura.

## 6. Criterios para extraer un servicio

Un módulo solo podrá convertirse en servicio independiente si demuestra:

-   necesidad de escalado separado;
-   ciclo de despliegue independiente;
-   límites estables;
-   carga operativa diferente;
-   riesgo que requiere aislamiento;
-   necesidad de tecnología distinta;
-   beneficio superior al costo operativo.

No se extraerá un servicio por moda o estética arquitectónica.

## 7. Capas principales

La arquitectura utilizará las siguientes capas:

Presentation

``` text
│
▼
```

Application

``` text
│
▼
```

Domain

``` text
│
▼
```

Ports

``` text
│
▼
```

Infrastructure Adapters

Además existirán capacidades transversales:

-   AI;
-   security;
-   observability;
-   audit;
-   evaluation;
-   configuration.

## 8. Presentation Layer

Responsable de:

-   HTTP;
-   WebSocket o streaming;
-   MCP transport;
-   validación de request;
-   autenticación inicial;
-   serialización;
-   códigos de respuesta;
-   manejo de errores de presentación.

No deberá contener reglas de negocio.

## 9. Application Layer

Responsable de:

-   casos de uso;
-   coordinación;
-   autorización;
-   transacciones;
-   invocación de puertos;
-   publicación de eventos;
-   construcción de respuestas;
-   idempotencia;
-   ejecución de políticas.

## 10. Domain Layer

Responsable de:

-   entidades;
-   value objects;
-   invariantes;
-   reglas;
-   estados;
-   políticas de dominio;
-   eventos de dominio.

No deberá depender de:

-   FastAPI;
-   SQLAlchemy;
-   OpenAI;
-   Redis;
-   HTTP;
-   infraestructura.

## 11. Infrastructure Layer

Responsable de implementar puertos para:

-   PostgreSQL;
-   Redis;
-   object storage;
-   proveedores AI;
-   embeddings;
-   email;
-   APIs externas;
-   OpenTelemetry;
-   colas;
-   parsers.

## 12. AI Layer

La capa AI coordinará capacidades probabilísticas.

Incluirá:

-   Model Gateway;
-   Prompt Registry;
-   structured outputs;
-   retrieval;
-   context assembly;
-   tool selection;
-   agent orchestration;
-   evaluators.

Esta capa no podrá evadir:

-   autorización;
-   validación;
-   reglas de dominio;
-   auditoría;
-   aprobación.

## 13. Bounded Contexts

GEEM AI Assistant se dividirá inicialmente en los siguientes contextos:

Identity Organizations Conversations AI Runtime Knowledge Retrieval
Tools Approvals Memory Audit Evaluation Observability MCP Administration

## 14. Mapa de módulos

Identity

``` text
│
├── Organizations
│        │
│        ├── Conversations
│        ├── Knowledge
│        ├── Tools
│        ├── Memory
│        └── Administration
│
├── AI Runtime
│        ├── Retrieval
│        ├── Tools
│        └── Approvals
│
├── Audit
├── Evaluation
├── Observability
└── MCP
```

## 15. Identity Module

Responsable de:

-   autenticación;
-   usuarios;
-   sesiones;
-   tokens;
-   identidad actual;
-   credenciales;
-   MFA futura;
-   eventos de acceso.

Entidades iniciales:

-   User;
-   Session;
-   IdentityProvider;
-   AuthenticationEvent.

## 16. Organizations Module

Responsable de:

-   organizaciones;
-   tenants;
-   membresías;
-   roles;
-   permisos;
-   invitaciones;
-   contexto organizacional.

Entidades:

-   Organization;
-   Tenant;
-   Membership;
-   Role;
-   Permission;
-   Invitation.

## 17. Relación Organization y Tenant

En la primera versión:

-   una organización tendrá al menos un tenant;
-   el tenant será la frontera de aislamiento de datos;
-   una organización podrá soportar múltiples tenants en el futuro;
-   los casos de uso resolverán siempre un tenant activo.

No se asumirá que organization_id y tenant_id son permanentemente
equivalentes.

## 18. Conversations Module

Responsable de:

-   conversaciones;

-   mensajes;

-   ejecuciones;

-   historial;

-   títulos;

-   estados;

-   streaming;

-   feedback.

Entidades:

-   Conversation;
-   Message;
-   AssistantExecution;
-   UserFeedback.

## 19. AI Runtime Module

Responsable de ejecutar capacidades AI.

Subcomponentes:

-   Model Gateway;
-   Provider Router;
-   Prompt Registry;
-   Response Validator;
-   Cost Calculator;
-   Retry Policy;
-   Fallback Policy;
-   Streaming Coordinator.

## 20. Knowledge Module

Responsable de:

-   documentos;
-   versiones;
-   archivos;
-   permisos;
-   ingestión;
-   extracción;
-   normalización;
-   chunks;
-   embeddings;
-   estados de procesamiento.

Entidades:

-   Document;

-   DocumentVersion;

-   DocumentPermission;

-   IngestionJob;

-   Chunk;

-   EmbeddingRecord.

## 21. Retrieval Module

Responsable de:

-   consulta semántica;
-   búsqueda textual;
-   filtros;
-   búsqueda híbrida;
-   ranking;
-   reranking;
-   context assembly;
-   referencias;
-   evaluación de suficiencia.

No será propietario de documentos.

Consumirá conocimiento mediante contratos.

## 22. Tools Module

Responsable de:

-   registro;
-   definición;
-   esquema;
-   permisos;
-   riesgo;
-   disponibilidad;
-   ejecución;
-   resultados;
-   errores;
-   idempotencia.

Entidades:

-   ToolDefinition;

-   ToolVersion;

-   ToolExecution;

-   ToolPermission;

-   ToolResult.

## 23. Approvals Module

Responsable de:

-   solicitudes;
-   decisiones;
-   expiración;
-   vinculación;
-   aprobadores;
-   políticas;
-   estado;
-   reanudación.

Entidades:

-   ApprovalRequest;
-   ApprovalDecision;
-   ApprovalPolicy;
-   ApprovalExecutionBinding.

## 24. Memory Module

Responsable de:

-   memoria de usuario;
-   memoria de trabajo;
-   hechos confirmados;
-   expiración;
-   corrección;
-   eliminación;
-   recuperación.

Entidades:

-   Memory;
-   MemoryType;
-   MemorySource;
-   MemoryRevision.

## 25. Audit Module

Responsable de registrar acciones relevantes de forma independiente de
los logs operativos.

Entidades:

-   AuditEvent;
-   AuditActor;
-   AuditResource;
-   AuditChangeSet.

## 26. Evaluation Module

Responsable de:

-   datasets;
-   casos;
-   runs;
-   métricas;
-   resultados;
-   baselines;
-   comparaciones;
-   regresiones.

Entidades:

-   EvaluationDataset;
-   EvaluationCase;
-   EvaluationRun;
-   EvaluationResult;
-   EvaluationMetric;
-   BaselineVersion.

## 27. Observability Module

Será principalmente una capacidad transversal.

Responsable de:

-   correlation IDs;

-   execution IDs;

-   traces;

-   metrics;

-   structured logs;

-   deployment metadata;

-   telemetry enrichment.

No será propietario de la auditoría empresarial.

## 28. MCP Module

Responsable de exponer recursos y tools mediante Model Context Protocol.

Deberá reutilizar:

-   autenticación;
-   autorización;
-   tenant context;
-   casos de uso;
-   Tool Registry;
-   Audit.

No duplicará lógica funcional.

## 29. Administration Module

Responsable de:

-   panel administrativo;
-   usuarios;
-   roles;
-   documentos;
-   tools;
-   aprobaciones;
-   auditoría;
-   configuración;
-   estados operativos.

Funcionará como fachada sobre otros módulos.

## 30. Estructura del repositorio

geem-ai-assistant/

``` text
├── apps/
│   ├── api/
│   ├── web/
│   ├── worker/
│   └── mcp/
├── src/
│   └── geem_ai/
│         ├── identity/
│         ├── organizations/
│         ├── conversations/
│         ├── ai_runtime/
│         ├── knowledge/
│         ├── retrieval/
│         ├── tools/
│         ├── approvals/
│         ├── memory/
│         ├── audit/
│         ├── evaluation/
│         ├── observability/
│         ├── administration/
│         └── shared/
├── tests/
├── docs/
├── infrastructure/
├── scripts/
├── docker/
└── .github/
```

## 31. Estructura interna de un módulo

module/

``` text
├── domain/
│   ├── entities.py
│   ├── value_objects.py
│   ├── events.py
│   ├── policies.py
│   └── exceptions.py
├── application/

│    ├── commands/
│    ├── queries/
│    ├── handlers/
│    ├── dto.py
│    └── ports.py
├── infrastructure/
│    ├── persistence/
│    ├── adapters/
│    └── mappers/
└── presentation/
├── api/
└── schemas/
```

No será obligatorio crear todos los archivos desde el inicio.

Se crearán conforme exista contenido real.

## 32. Shared Kernel

El directorio shared podrá contener únicamente conceptos verdaderamente
comunes.

Ejemplos:

-   EntityId;
-   TenantId;
-   UserId;
-   Money;
-   Clock;
-   DomainEvent;
-   Pagination;
-   Result;
-   base exceptions.

No deberá convertirse en un contenedor genérico de utilidades.

## 33. Regla de dependencia entre módulos

Un módulo no podrá importar directamente infraestructura interna de
otro.

Podrá consumir:

-   contratos públicos;

-   DTOs;

-   application services;

-   eventos;

-   puertos definidos.

## 34. Public API de módulos

Cada módulo deberá exponer explícitamente su interfaz pública.

Ejemplo:

``` text
from geem_ai.knowledge.public import (
```

GetAuthorizedDocument, SearchAuthorizedDocuments, )

El resto deberá considerarse interno.

## 35. Comunicación síncrona

Se utilizará para:

-   consultas requeridas inmediatamente;
-   validaciones;
-   operaciones dentro de una transacción;
-   coordinación simple.

La comunicación deberá pasar por application services o puertos
públicos.

## 36. Comunicación asíncrona

Se utilizará para:

-   ingestión;

-   embeddings;

-   notificaciones;

-   evaluaciones;

-   auditoría secundaria;

-   procesamiento pesado;

-   reintentos;

-   acciones diferidas.

## 37. Domain Events

Los eventos de dominio representarán hechos internos relevantes.

Ejemplos:

DocumentUploaded DocumentProcessingRequested ConversationCreated
ApprovalRequested ApprovalGranted MemoryConfirmed

Podrán manejarse dentro de la misma aplicación.

## 38. Integration Events

Los eventos de integración representarán cambios relevantes para
consumidores externos o procesos asíncronos.

Ejemplos:

DocumentReadyForRetrieval ToolExecutionCompleted SupportTicketCreated

Deberán ser versionados cuando crucen límites persistentes.

## 39. Event Outbox

Se evaluará el patrón Transactional Outbox para eventos que deban
publicarse de forma confiable.

Será especialmente relevante para:

-   jobs;

-   tool executions;

-   integraciones externas;

-   notificaciones;

-   workflows.

Su implementación se introducirá cuando el primer caso real lo requiera.

## 40. Command Query Separation

Se distinguirá entre:

Commands Cambian estado.

Queries Consultan estado.

No se implementará CQRS con infraestructura separada inicialmente.

La separación será conceptual y de código.

## 41. Unit of Work

Los casos de uso que modifiquen estado utilizarán una unidad de trabajo.

Responsabilidades:

-   comenzar transacción;
-   confirmar;
-   revertir;
-   recolectar eventos;
-   publicar después del commit cuando corresponda.

## 42. Repository Pattern

Los repositorios representarán colecciones de entidades de dominio.

Ejemplos:

-   ConversationRepository;
-   DocumentRepository;
-   ApprovalRepository;
-   MemoryRepository.

No se crearán repositorios genéricos universales.

## 43. Data Model General

Todas las tablas empresariales deberán incluir cuando aplique:

id tenant_id created_at updated_at created_by

También podrán incluir:

version deleted_at status metadata

## 44. Identificadores

Se utilizarán identificadores opacos.

Opciones aceptables:

-   UUID;
-   UUIDv7;
-   ULID.

La decisión final se documentará en un ADR.

No se expondrán identificadores secuenciales cuando faciliten
enumeración.

## 45. Timestamps

Todos los timestamps internos se almacenarán en UTC.

La conversión a zona local ocurrirá en presentación.

## 46. Soft Delete

No será el comportamiento por defecto para todas las entidades.

Se utilizará cuando exista necesidad de:

-   recuperación;
-   auditoría;
-   retención;
-   integridad histórica.

La eliminación de documentos deberá considerar además chunks, embeddings
y archivos.

## 47. Modelo de Identity

Tablas iniciales conceptuales:

users sessions authentication_events identity_providers

users contendrá identidad global.

La relación con organizaciones estará en Membership.

## 48. Modelo de Organizations

organizations tenants memberships roles

permissions role_permissions invitations

Una membership relacionará:

-   user;
-   organization;
-   tenant;
-   role;
-   status.

## 49. Modelo de Conversations

conversations messages assistant_executions message_citations
user_feedback

Una ejecución podrá generar:

-   mensaje;
-   tool calls;
-   citas;
-   métricas;
-   auditoría.

## 50. Modelo de Knowledge

documents document_versions document_permissions document_files
ingestion_jobs chunks embedding_records

Los chunks deberán relacionarse con una versión concreta del documento.

## 51. Modelo de Retrieval

Podrá utilizar datos derivados como:

retrieval_runs retrieval_candidates retrieval_selections
context_assemblies

No todos deberán persistirse de forma permanente.

Podrán registrarse en telemetría o evaluación.

## 52. Modelo de Tools

tool_definitions tool_versions tool_permissions tool_executions
tool_execution_attempts tool_results

La versión ejecutada deberá quedar registrada.

## 53. Modelo de Approvals

approval_requests approval_decisions approval_policies approval_bindings

La aprobación deberá guardar un hash de los argumentos autorizados.

## 54. Modelo de Memory

memories memory_revisions memory_sources memory_access_events

Cada memoria deberá incluir:

-   tipo;
-   propietario;
-   tenant;
-   fuente;
-   confianza;
-   expiración;
-   estado.

## 55. Modelo de Audit

audit_events

Cada evento deberá incluir:

-   actor;
-   tenant;
-   acción;
-   recurso;
-   resultado;
-   timestamp;
-   correlation ID;
-   metadata sanitizada.

## 56. Modelo de Evaluation

evaluation_datasets evaluation_cases evaluation_runs evaluation_results

evaluation_metrics baseline_versions

Los datasets podrán mantenerse parcialmente en archivos versionados.

La base de datos almacenará ejecución y resultados cuando aporte valor.

## 57. PostgreSQL Schemas

Podrán utilizarse schemas lógicos:

identity organizations conversations knowledge tools approvals memory
audit evaluation

Su adopción dependerá de compatibilidad con migraciones y operación.

No es obligatorio separar físicamente cada módulo desde el primer día.

## 58. pgvector

pgvector almacenará embeddings vinculados a:

-   tenant;
-   document version;
-   chunk;
-   embedding model;
-   embedding dimension;
-   created_at.

No se mezclarán embeddings de modelos incompatibles en el mismo índice
sin control explícito.

## 59. Índices vectoriales

La estrategia inicial será simple.

Se evaluarán:

-   búsqueda exacta;
-   HNSW;
-   IVFFlat cuando corresponda.

La selección dependerá del volumen y benchmarks.

No se optimizará prematuramente.

## 60. Full-Text Search

PostgreSQL Full-Text Search será la primera opción para búsqueda
lexical.

Permitirá:

-   frases;
-   términos exactos;
-   códigos;
-   nombres;
-   ranking textual.

## 61. Redis

Redis se utilizará para:

-   cache;
-   rate limiting;
-   locks;
-   estados temporales;
-   streaming coordination;
-   colas ligeras si se aprueba;
-   idempotency records temporales.

No será fuente de verdad.

## 62. Object Storage

Los archivos originales y derivados se almacenarán en object storage
compatible con S3.

Rutas conceptuales:

tenants/{tenant_id}/documents/{document_id}/versions/{version_id}/original

Podrán existir derivados como:

-   extracted text;
-   previews;
-   metadata;
-   sanitized copies.

## 63. Worker Architecture

Los procesos asíncronos se ejecutarán mediante workers separados del
proceso web.

Responsabilidades iniciales:

-   document extraction;
-   chunking;
-   embeddings;
-   reindexing;
-   evaluation;
-   notificaciones futuras.

## 64. Queue Strategy

La tecnología definitiva de cola se decidirá mediante ADR.

Opciones iniciales:

-   Redis-based queue;
-   PostgreSQL-based queue;
-   task framework compatible con Python.

La decisión deberá priorizar:

-   simplicidad;

-   retries;

-   observabilidad;

-   mantenimiento;

-   compatibilidad con Docker.

## 65. Job Contract

Cada job deberá incluir:

job_id job_type tenant_id execution_id payload_version payload attempt
created_at

Los jobs deberán ser idempotentes cuando sea posible.

## 66. Job States

pending running succeeded failed retry_scheduled dead_letter cancelled

## 67. Model Gateway Architecture

Application Use Case

``` text
│
▼
```

Model Gateway

``` text
│

├── Request Normalizer
├── Provider Router
├── Prompt Resolver
├── Output Validator
├── Retry Policy
├── Fallback Policy
├── Cost Calculator
└── Telemetry
│
┌───────┴────────┐
▼                      ▼
```

OpenAI Adapter Anthropic Adapter

## 68. Model Request

Contrato conceptual:

``` text
class ModelRequest:
```

capability: str messages: list prompt_reference: str output_schema: type
\| None tools: list tenant_id: str execution_id: str constraints: dict

## 69. Model Response

Contrato conceptual:

``` text
class ModelResponse:
```

content: object provider: str model: str usage: object tool_calls: list
finish_reason: str validation_status: str

latency_ms: int estimated_cost: float

## 70. Provider Router

El Provider Router seleccionará según:

-   capability;
-   configuración;
-   disponibilidad;
-   presupuesto;
-   modelo permitido;
-   feature flag;
-   política de fallback.

La selección no será decidida libremente por el usuario final.

## 71. Prompt Registry Architecture

Cada prompt deberá tener:

prompt_key version status template variables_schema output_schema
supported_models evaluation_status created_at

Estados:

draft candidate active deprecated retired

## 72. Prompt Storage

Los prompts podrán almacenarse inicialmente en archivos versionados.

Ejemplo:

src/geem_ai/ai_runtime/prompts/

La base de datos podrá incorporarse cuando se necesite administración
dinámica.

Git será la fuente de verdad inicial.

## 73. Structured Outputs

Toda respuesta consumida programáticamente deberá validarse.

Flujo:

Model Output

``` text
│
▼
```

Schema Validation

``` text
│
├── Valid → Continue
└── Invalid
│
├── Controlled Repair
├── Retry
└── Fail Safely
```

## 74. Conversation Orchestration

El flujo inicial será determinista.

Receive Message

``` text
│
▼
```

Resolve Identity and Tenant

``` text
│
▼
```

Load Conversation

``` text
│
▼
```

Classify Required Capability

``` text
│
├── Direct
├── RAG
└── Tool
│
▼
```

Execute Capability

``` text
│
▼
```

Validate Response

``` text
│
▼
```

Persist

``` text
│
▼
```

Stream to Client

## 75. Intent Resolution

La intención podrá resolverse mediante:

-   reglas;
-   structured classification;
-   contexto;
-   herramientas disponibles.

No se utilizará un agente general para el primer flujo.

## 76. RAG Architecture

User Query

``` text
│
▼
```

Query Preparation

``` text
│

▼
```

Authorization Filters

``` text
│
├── Vector Search
└── Full-Text Search
│
▼
```

Candidate Merge

``` text
│
▼
```

Ranking

``` text
│
▼
```

Context Assembly

``` text
│
▼
```

Answer Generation

``` text
│
▼
```

Citation Validation

``` text
│
▼
```

Response

## 77. Query Preparation

Podrá incluir:

-   normalización;
-   detección de idioma;
-   expansión controlada;
-   extracción de filtros;
-   embedding;
-   clasificación de intención.

Las transformaciones deberán ser observables.

## 78. Authorization Filters

Antes de recuperar resultados deberán aplicarse:

-   tenant;

-   documento;

-   clasificación;

-   usuario;

-   rol;

-   permisos;

-   estado;

-   versión.

## 79. Candidate Merge

La búsqueda híbrida deberá combinar resultados sin perder:

-   score original;
-   estrategia;
-   documento;
-   chunk;
-   posición;
-   permisos.

El algoritmo inicial podrá usar Reciprocal Rank Fusion.

## 80. Reranking

El reranking será opcional.

Se incorporará únicamente si demuestra mejora suficiente en:

-   precisión;
-   groundedness;
-   ranking;
-   calidad final.

## 81. Context Assembly

El ensamblador deberá:

-   seleccionar evidencia;

-   eliminar duplicados;

-   ordenar;

-   conservar citas;

-   limitar tokens;

-   mantener separación documental;

-   señalar contradicciones;

-   estimar suficiencia.

## 82. Citation Validator

La validación deberá comprobar:

-   que la fuente existe;
-   que pertenece al tenant;
-   que fue recuperada;
-   que está autorizada;
-   que respalda la afirmación;
-   que la referencia es visible.

## 83. Abstention Policy

El sistema deberá abstenerse cuando:

-   no hay resultados;
-   los scores son insuficientes;
-   el contexto no cubre la pregunta;
-   existen contradicciones relevantes;
-   la información está restringida;
-   falla la validación de citas.

## 84. Tool Calling Architecture

Model Suggests Tool

``` text
│
▼
```

Tool Registry Lookup

``` text
│
▼
```

Arguments Validation

``` text
│
▼
```

Authorization

``` text
│
▼
```

Risk Evaluation

``` text
│
├── Execute Directly
└── Create Approval
│
▼
```

Decision

``` text
│
▼
```

Execute

``` text
│
▼
```

Audit

## 85. Tool Contract

Toda tool deberá declarar:

name version description input_schema output_schema risk_level
required_permissions approval_policy timeout idempotency_strategy

## 86. Tool Adapter

Las integraciones reales se implementarán mediante adapters.

Ejemplos:

-   SupportProceduresAdapter;
-   SupportTicketAdapter;
-   CRMAdapter;
-   GrestAdapter.

El modelo nunca accederá directamente al SDK o API externa.

## 87. Tool Execution Boundary

El ejecutor deberá encargarse de:

-   validar;
-   autorizar;
-   auditar;
-   aplicar timeout;
-   aplicar retry;
-   manejar idempotencia;
-   sanitizar resultado;
-   registrar métricas.

## 88. Approval Architecture

Tool Execution Request

``` text
│
▼
```

Approval Policy

``` text
│
▼
```

Approval Request

``` text
│
▼
```

User Decision

``` text
┌────┴────┐
▼           ▼
```

Approve Reject

``` text
│
▼
```

Binding Validation

``` text
│
▼
```

Tool Execution

## 89. Approval State Machine

pending approved rejected expired cancelled executed execution_failed

Una aprobación aprobada no equivale todavía a una ejecución completada.

## 90. Approval Binding

La aprobación deberá estar ligada a:

-   user;
-   tenant;
-   tool;
-   tool version;
-   argument hash;
-   execution;
-   expiration;
-   policy version.

## 91. Memory Architecture

Candidate Memory

``` text
│
▼
```

Policy Evaluation

``` text
│
├── Reject
├── Store Temporarily
└── Require Confirmation
│
▼
```

Persist Memory

``` text
│

▼
```

Future Retrieval

## 92. Memory Retrieval

La memoria deberá recuperarse según:

-   tenant;
-   usuario;
-   tipo;
-   contexto;
-   relevancia;
-   estado;
-   expiración;
-   permisos.

No se inyectará toda la memoria disponible en cada request.

## 93. MCP Architecture

MCP Client

``` text
│
▼
```

MCP Transport

``` text
│
▼
```

Authentication

``` text
│
▼
```

Tenant Resolution

``` text
│
▼
```

MCP Resource or Tool Handler

``` text
│
▼
```

Application Use Case

``` text
│
▼
```

Audit and Telemetry

## 94. MCP Resources Iniciales

Podrán incluir:

documents document_details knowledge_search conversation_history
tool_catalog

Cada recurso deberá filtrar permisos.

## 95. MCP Tools Iniciales

Podrán incluir:

search_knowledge search_support_procedures create_support_ticket

La tool de escritura seguirá requiriendo aprobación según política.

## 96. API Design

La API utilizará:

-   REST para operaciones de negocio;
-   streaming para respuestas;
-   webhooks para integraciones futuras;
-   MCP para clientes compatibles.

## 97. Versionado de API

Las rutas públicas utilizarán versionado.

Ejemplo:

``` text
/api/v1/
```

Los contratos deberán evolucionar de forma compatible cuando sea
posible.

## 98. Endpoints iniciales

POST /api/v1/auth/login GET /api/v1/me GET /api/v1/organizations POST
/api/v1/conversations GET /api/v1/conversations GET
/api/v1/conversations/{id} POST /api/v1/conversations/{id}/messages POST
/api/v1/documents GET /api/v1/documents GET /api/v1/documents/{id} POST
/api/v1/documents/{id}/retry GET /api/v1/approvals POST
/api/v1/approvals/{id}/approve POST /api/v1/approvals/{id}/reject

## 99. Streaming Protocol

La primera opción será Server-Sent Events.

Eventos conceptuales:

response.started response.delta retrieval.completed tool.requested
approval.required response.completed response.failed

## 100. Error Contract

La API deberá responder errores estructurados.

``` text
{
"error": {
"code": "DOCUMENT_PROCESSING_FAILED",
"message": "El documento no pudo procesarse.",
"correlation_id": "corr-123",
"retryable": true
}
}
```

## 101. Error Taxonomy

Categorías:

validation authentication authorization not_found conflict rate_limit
domain ai_output provider integration infrastructure security

## 102. Security Architecture

Controles principales:

-   authentication middleware;

-   tenant context;

-   policy engine;

-   repository filtering;

-   tool authorization;

-   approval binding;

-   input validation;

-   output validation;

-   audit;

-   rate limiting;

-   secret management.

## 103. Tenant Context

El tenant deberá resolverse desde:

-   sesión;
-   membership;
-   organization selection;
-   credencial de servicio;
-   token MCP.

No se confiará únicamente en un header enviado libremente por el
cliente.

## 104. Authorization Architecture

Authenticated Actor

``` text
│
▼
```

Tenant Membership

``` text
│
▼
```

Role Permissions

``` text
│
▼
```

Resource Policy

``` text
│
▼
```

Action Decision

## 105. Audit Architecture

Los casos de uso críticos emitirán eventos de auditoría.

Ejemplos:

-   login;
-   document access;
-   document upload;
-   role change;
-   tool request;
-   approval;
-   tool execution;
-   memory change;
-   export.

## 106. Observability Architecture

La instrumentación utilizará OpenTelemetry.

API / Worker / MCP

``` text
│
▼
```

OpenTelemetry SDK

``` text
│
▼
```

Collector

``` text
│
├── Traces
├── Metrics
└── Logs
```

## 107. Trace Root

Cada operación deberá tener un root span.

Ejemplos:

assistant.message document.ingestion tool.execution approval.decision

evaluation.run mcp.request

## 108. Evaluation Architecture

Las evaluaciones se ejecutarán mediante runners independientes.

Dataset

``` text
│
▼
```

Evaluation Runner

``` text
│
├── System Under Test
├── Deterministic Evaluators
├── LLM Judges
└── Human Review
│
▼
```

Evaluation Report

## 109. Evaluation Environments

Se distinguirán:

-   local;
-   CI smoke;
-   staging full;
-   production sampled.

Los datasets de producción deberán sanitizarse antes de reutilizarse.

## 110. Configuration Architecture

La configuración se dividirá entre:

Static Configuration Versionada en código.

Environment Configuration Variables por ambiente.

Dynamic Configuration Valores administrables.

Secrets Gestor seguro.

## 111. Feature Flags

Las capacidades de riesgo podrán controlarse por:

-   ambiente;
-   tenant;
-   usuario;
-   porcentaje;
-   versión.

Ejemplos:

-   hybrid retrieval;
-   reranking;
-   memory;
-   MCP;
-   secondary provider.

## 112. Deployment Architecture Inicial

Reverse Proxy

``` text
│
├── Web
├── API
└── MCP
│
┌─────┼─────────────┐
▼          ▼              ▼
```

Worker PostgreSQL Redis

``` text
│
▼
```

Object Storage

All Components

``` text
│
▼
```

OpenTelemetry Collector

## 113. Contenedores iniciales

Docker Compose podrá incluir:

web api worker mcp postgres redis object-storage otel-collector

MCP podrá compartir proceso con API inicialmente si simplifica la
primera fase.

La separación se decidirá por operación y seguridad.

## 114. Environments

development test staging production

Cada ambiente tendrá:

-   base de datos;

-   secretos;

-   buckets;

-   proveedores o credenciales;

-   telemetría;

-   configuración.

## 115. CI Pipeline

El pipeline inicial deberá ejecutar:

format check lint typecheck unit tests integration tests migration
checks security scan evaluation smoke set frontend build backend build
container build

## 116. CD Pipeline

El despliegue deberá soportar:

-   staging automático o controlado;
-   producción con aprobación;
-   migration step;
-   health checks;
-   smoke tests;
-   deployment marker;
-   rollback.

## 117. Testing Architecture

La estrategia incluirá:

-   unit tests;

-   application tests;

-   repository integration tests;

-   API tests;

-   contract tests;

-   security tests;

-   tenant isolation tests;

-   end-to-end tests;

-   evaluation tests.

## 118. Test Pyramid

E2E Integration Application Tests Unit Tests

Las evaluaciones AI coexistirán con esta pirámide.

## 119. Fixtures

Se crearán fixtures para:

-   tenants;
-   users;
-   roles;
-   documents;
-   conversations;
-   tools;
-   approvals;
-   memories;
-   evaluation cases.

No se usarán datos productivos.

## 120. Migration Strategy

Alembic será responsable de migraciones.

Reglas:

-   migraciones versionadas;

-   forward-compatible cuando sea posible;

-   pruebas en CI;

-   datos separados de esquema;

-   rollback documentado;

-   cambios destructivos en fases.

## 121. Backward Compatibility

Los cambios deberán considerar:

-   API clients;
-   workers;
-   jobs en cola;
-   prompts;
-   tool versions;
-   eventos;
-   documentos indexados;
-   embeddings existentes.

## 122. Versionado de herramientas

Las tools tendrán versiones explícitas.

Una nueva versión será necesaria cuando cambie:

-   input schema;
-   output schema;
-   semántica;
-   permisos;
-   riesgo;
-   comportamiento.

## 123. Versionado de embeddings

Cada embedding deberá registrar:

-   provider;
-   model;
-   dimension;
-   normalization;
-   version;
-   created_at.

Un cambio de modelo requerirá reindexación controlada.

## 124. Versionado de prompts

Toda ejecución deberá registrar la versión exacta del prompt utilizado.

Los prompts retirados deberán permanecer disponibles para reproducir
resultados históricos cuando sea necesario.

## 125. Versionado de agentes

Cuando se incorpore LangGraph, cada graph deberá tener:

-   graph key;
-   version;
-   nodes;
-   transitions;
-   state schema;
-   policies;
-   evaluation status.

## 126. Resiliencia

La arquitectura deberá incluir:

-   timeouts;
-   retries controlados;
-   circuit breakers;
-   fallback;
-   idempotencia;
-   dead-letter handling;
-   health checks;
-   graceful degradation.

## 127. Timeout Policy

Cada integración tendrá timeout explícito.

Ejemplos:

-   model call;
-   embedding;
-   object storage;
-   external tool;
-   database query;
-   MCP request.

No se permitirán esperas indefinidas.

## 128. Retry Policy

Se reintentará únicamente:

-   errores temporales;
-   timeouts recuperables;
-   rate limits;
-   fallos transitorios.

No se reintentará automáticamente:

-   autorización;
-   validación;
-   conflictos de dominio;
-   acciones no idempotentes sin protección.

## 129. Circuit Breaker

Se evaluará para:

-   proveedores LLM;
-   embeddings;
-   APIs externas;
-   object storage.

Cuando se abra, el sistema deberá degradar o fallar de forma clara.

## 130. Degradación controlada

Ejemplos:

-   proveedor secundario;
-   respuesta sin memoria;
-   búsqueda lexical si vector falla;
-   procesamiento diferido;
-   tool manual;
-   abstención.

## 131. Performance Budgets

Objetivos iniciales:

Operación p95

Login ≤2s

Listado simple ≤1s

Crear conversación ≤1s

Time to first token ≤3s

Consulta simple AI ≤8s

Consulta RAG ≤ 12 s

Tool de lectura ≤ 10 s

Aprobación ≤2s

Ingestión asíncrona

## 132. Scalability

La primera arquitectura deberá soportar:

-   varios tenants;
-   cientos de documentos;
-   miles de chunks;
-   múltiples conversaciones;
-   workers escalables;
-   proveedores alternos.

No se diseñará inicialmente para millones de usuarios.

## 133. Horizontal Scaling

Podrán escalarse horizontalmente:

-   API;
-   workers;
-   MCP;
-   frontend estático.

Esto requerirá evitar estado local persistente.

## 134. State Management

El estado persistente deberá vivir en:

-   PostgreSQL;
-   object storage;
-   Redis para estado temporal controlado.

No deberá depender del filesystem local del contenedor.

## 135. Frontend Architecture

El frontend se dividirá por features.

src/

``` text
├── app/
├── features/
│    ├── auth/
│    ├── conversations/
│    ├── knowledge/
│    ├── approvals/
│    ├── administration/
│    └── observability/
├── shared/
└── api/
```

## 136. Estado del frontend

Se distinguirá:

-   server state;
-   UI state;
-   form state;
-   streaming state;
-   authentication state.

No se utilizará un store global para todo.

## 137. API Client

El frontend utilizará un cliente tipado.

Los contratos podrán generarse o validarse desde OpenAPI.

## 138. Streaming UI

La interfaz deberá soportar:

-   respuesta parcial;
-   cancelación;
-   estado de retrieval;
-   estado de tool;
-   aprobación;
-   errores;
-   reintento.

## 139. Source Viewer

La interfaz de citas deberá mostrar:

-   documento;
-   fragmento;
-   ubicación;
-   versión;
-   relevancia;
-   acceso seguro.

## 140. Approval UI

La aprobación deberá distinguir claramente:

-   lo que el asistente recomienda;
-   lo que ocurrirá;
-   los datos utilizados;
-   el riesgo;
-   quién aprobará.

## 141. Administración de documentos

El panel deberá mostrar:

-   nombre;
-   versión;
-   estado;
-   tipo;
-   tamaño;
-   fecha;
-   propietario;
-   errores;
-   acciones permitidas.

## 142. Administración técnica

El modo técnico podrá mostrar:

-   execution ID;
-   modelo;
-   tokens;
-   costo;
-   latencia;
-   sources;
-   tool calls;
-   trace link.

No estará habilitado necesariamente para todos los usuarios.

## 143. ADRs iniciales requeridos

Se deberán crear al menos:

ADR-0001-modular-monolith ADR-0002-identifier-strategy
ADR-0003-multi-tenant-data-isolation ADR-0004-model-gateway
ADR-0005-prompt-storage ADR-0006-document-storage
ADR-0007-background-job-system ADR-0008-vector-search-strategy
ADR-0009-streaming-protocol ADR-0010-mcp-deployment-model

## 144. Diagramas requeridos

El proyecto deberá producir:

-   C4 System Context;
-   C4 Container;
-   C4 Component;
-   conversación sequence;
-   RAG sequence;
-   tool calling sequence;
-   approval sequence;
-   ingestion sequence;
-   deployment diagram;
-   trust boundary diagram.

## 145. Diagrama de contexto

Users

``` text
│
▼
```

GEEM AI Assistant

``` text
│
├── Model Providers
├── Object Storage
├── Enterprise Systems

├── Identity Provider
└── Observability Platform
```

## 146. Diagrama de contenedores

React Web

``` text
│
▼
```

FastAPI Application

``` text
│
├── PostgreSQL + pgvector
├── Redis
├── Object Storage
├── Worker
├── MCP Interface
├── Model Providers
└── External Tools
```

## 147. Secuencia de conversación simple

User

``` text
│
▼
```

Web

``` text
│
▼
```

API

``` text
│
▼
```

Conversation Use Case

``` text
│
▼
```

Model Gateway

``` text
│
▼
```

Provider

``` text
│
▼
```

Validator

``` text
│
▼
```

Persistence

``` text
│
▼
```

User

## 148. Secuencia de ingestión

User

``` text
│
▼
```

Upload API

``` text
│
▼
```

Validation

``` text
│
▼
```

Object Storage

``` text
│
▼
```

Document Record

``` text
│
▼
```

Queue

``` text
│
▼
```

Worker

``` text
│
├── Extract
│
├── Chunk
│
├── Embed
│
└── Index
│
▼
```

Document Available

## 149. Secuencia RAG

User

``` text
│
▼
```

Conversation

``` text
│
▼
```

Retrieval

``` text
│
├── Authorization
│
├── Vector
│
├── Full-Text
│
├── Merge
│
└── Context
│
▼
```

Model Gateway

``` text
│
▼
```

Citation Validator

``` text
│
▼
```

Response

## 150. Secuencia de tool y aprobación

User Request

``` text
│
▼
```

Model Suggests Tool

``` text
│
▼
```

Tool Registry

``` text
│
▼
```

Authorization

``` text
│
▼
```

Approval Required

``` text
│
▼
```

User Approves

``` text
│
▼
```

Binding Validation

``` text
│
▼
```

Tool Execution

``` text
│
▼
```

Audit

``` text
│
▼
```

Final Response

## 151. Primera arquitectura implementable

El primer vertical slice solo requerirá:

-   web;
-   API;
-   PostgreSQL;
-   Model Gateway;
-   OpenAI adapter;
-   conversations;
-   messages;
-   executions;
-   structured output;
-   streaming;
-   telemetry.

No deberá incluir todavía:

-   RAG;
-   tools;
-   memory;
-   MCP completo;
-   workers complejos.

## 152. Segunda arquitectura implementable

El segundo slice añadirá:

-   authentication;
-   organizations;
-   memberships;
-   roles;
-   tenant context;
-   isolation tests;
-   audit.

## 153. Tercera arquitectura implementable

El tercer slice añadirá:

-   document upload;
-   object storage;
-   ingestion job;
-   worker;
-   extraction;
-   chunking;
-   embeddings;
-   document states.

## 154. Cuarta arquitectura implementable

El cuarto slice añadirá:

-   retrieval;
-   RAG;
-   citations;
-   abstention;
-   evaluation;
-   RAG dashboard.

## 155. Quinta arquitectura implementable

El quinto slice añadirá:

-   Tool Registry;
-   tool de lectura;
-   authorization;
-   execution;
-   audit;
-   evaluation.

## 156. Sexta arquitectura implementable

El sexto slice añadirá:

-   tool de escritura;
-   approvals;
-   idempotency;
-   UI de decisión;
-   reanudación;
-   auditoría.

## 157. Séptima arquitectura implementable

El séptimo slice añadirá:

-   memory;
-   correction;
-   expiration;
-   retrieval;
-   evaluation.

## 158. Octava arquitectura implementable

El octavo slice añadirá:

-   MCP;

-   resources;

-   tools;

-   authentication;

-   authorization;

-   audit;

-   demo client.

## 159. Riesgos arquitectónicos

A-001 --- Modular Monolith sin límites reales Mitigación:

-   módulos;
-   public APIs;
-   reglas de importación;
-   revisión;
-   ownership de datos.

A-002 --- Model Gateway demasiado genérico Mitigación:

-   comenzar con capacidades reales;
-   evitar abstracciones teóricas;
-   adaptar contratos al uso.

A-003 --- RAG acoplado a proveedor Mitigación:

-   interfaces;
-   metadata;
-   versionado;
-   evaluation.

A-004 --- Exceso de tablas tempranas Mitigación:

-   implementar por vertical slice;
-   no crear entidades sin uso.

A-005 --- Workers y colas sobrediseñados Mitigación:

-   elegir solución simple;
-   medir volumen;
-   mantener contratos.

## 160. Riesgos de evolución

-   crecimiento del Prompt Registry;
-   múltiples modelos;
-   reindexación de embeddings;
-   tool versions;
-   migración de tenants;
-   memoria excesiva;
-   volumen de telemetría;
-   compatibilidad MCP;
-   retención documental.

Cada riesgo deberá convertirse en ADR o iniciativa cuando sea necesario.

## 161. Reglas de implementación

## 1. No se crearán módulos vacíos.

## 2. No se crearán interfaces sin al menos un consumidor real.

## 3. No se permitirá acceso directo entre tablas de módulos.

## 4. No se mezclará lógica AI con controllers.

## 5. No se ejecutarán tools desde prompts sin Tool Registry.

## 6. No se recuperarán documentos sin filtros de autorización.

## 7. No se almacenarán outputs sin validación cuando sean estructurados.

## 8. No se usarán SDKs externos en el dominio.

## 9. No se crearán microservicios sin ADR.

## 10. No se optimizará infraestructura sin métricas.

## 162. Criterios de validación arquitectónica

La arquitectura será válida cuando:

-   permite desarrollar vertical slices;

-   mantiene límites;

-   soporta multi-tenancy;

-   protege tools;

-   aísla proveedores;

-   soporta evaluación;

-   soporta observabilidad;

-   puede desplegarse con Docker;

-   puede explicarse claramente;

-   puede evolucionar sin reescritura inmediata.

## 163. Evidencia arquitectónica

Cada milestone deberá producir:

-   diagrama actualizado;
-   contrato;
-   ADR;
-   tests;
-   trace;
-   documentación;
-   comparación cuando exista decisión.

## 164. Preguntas de entrevista

Erick deberá poder responder:

-   ¿Por qué Modular Monolith?
-   ¿Cómo evitó acoplamiento entre módulos?
-   ¿Cómo diseñó el Model Gateway?
-   ¿Dónde vive la autorización?
-   ¿Cómo protege multi-tenancy?
-   ¿Cómo se procesan documentos?
-   ¿Cómo funciona búsqueda híbrida?
-   ¿Cómo versiona tools y prompts?
-   ¿Cómo reanuda una acción después de aprobación?
-   ¿Cómo comparte capacidades con MCP?
-   ¿Qué extraería primero a un servicio independiente?
-   ¿Cómo probaría los límites arquitectónicos?

## 165. Decisiones oficiales

Quedan aprobadas las siguientes decisiones:

## 1. GEEM AI Assistant utilizará Modular Monolith.

## 2. Los módulos tendrán propiedad lógica de sus datos.

## 3. La lógica de dominio será independiente de frameworks.

## 4. FastAPI será la capa de presentación backend.

## 5. PostgreSQL será la fuente principal de verdad.

## 6. pgvector será el almacenamiento vectorial inicial.

## 7. Redis se utilizará únicamente para estado temporal y coordinación.

## 8. Los archivos vivirán en object storage.

## 9. La ingestión se ejecutará mediante workers.

## 10. El sistema distinguirá domain events e integration events.

## 11. Los cambios de estado utilizarán Unit of Work.

## 12. Los repositorios serán específicos del dominio.

## 13. El Model Gateway aislará proveedores.

## 14. Los prompts estarán versionados y gobernados.

## 15. Structured Outputs serán obligatorios para salidas programáticas.

## 16. El flujo inicial de conversación será determinista.

## 17. RAG aplicará autorización antes de recuperación.

## 18. Tool Registry será la única puerta de ejecución de tools.

## 19. Las approvals estarán vinculadas a argumentos exactos.

## 20. La memoria se incorporará después de RAG y tools.

## 21. MCP reutilizará los casos de uso internos.

## 22. OpenTelemetry será transversal.

## 23. La evaluación tendrá runners independientes.

## 24. Las APIs públicas serán versionadas.

## 25. SSE será la opción inicial de streaming.

## 26. La arquitectura crecerá mediante vertical slices.

## 27. Las tecnologías de cola e identificadores requerirán ADR.

## 28. No se crearán módulos o abstracciones sin necesidad actual.

## 29. Toda decisión difícil de revertir deberá documentarse.

## 30. La arquitectura deberá mantenerse defendible, operable y demostrable.

## 166. Próximo documento

Documento 12 --- Project 1 Domain Model Definirá con mayor precisión:

-   entidades;

-   value objects;

-   agregados;

-   invariantes;

-   estados;

-   relaciones;

-   eventos de dominio;

-   reglas de autorización;

-   ciclos de vida;

-   ownership de datos;

-   límites transaccionales.

El documento permitirá convertir la arquitectura general en un modelo de
dominio listo para implementar.

## 167. Conclusión

La arquitectura de GEEM AI Assistant queda definida como una plataforma
empresarial modular, multi- tenant y orientada a capacidades completas.

El sistema separará claramente:

-   negocio;
-   aplicación;
-   infraestructura;
-   inteligencia artificial;
-   seguridad;
-   evaluación;
-   observabilidad.

El objetivo no será construir una abstracción perfecta desde el inicio.

Será crear una arquitectura suficientemente sólida para desarrollar,
medir y operar el primer producto del AI Engineering Lab sin perder
velocidad ni control.
