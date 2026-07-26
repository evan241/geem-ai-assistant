# AI Engineering Lab

## Documento 03 — Architecture Standards

**Versión:** 1.0
**Estado:** Estándar arquitectónico inicial
**Responsable técnico:** Director de AI Engineering
**Lead Engineer:** Erick Eduardo Evangelista Velasco
## 1. Propósito

Este documento define los estándares de arquitectura que deberán seguir todos los proyectos del AI
Engineering Lab.
Su objetivo es evitar que las soluciones evolucionen hacia:
- controladores con demasiadas responsabilidades;
- lógica empresarial dentro de prompts;
- agentes con acceso irrestricto;
- integraciones acopladas;
- workflows imposibles de probar;
- dependencias directas entre dominio y proveedores;
- sistemas difíciles de observar;
- repositorios sin límites claros.
Los proyectos deberán conservar una arquitectura comprensible, verificable y defendible.
## 2. Principio arquitectónico central

La inteligencia artificial deberá integrarse dentro de una arquitectura de software, no
sustituirla.
Cada sistema deberá diferenciar claramente entre:
- reglas deterministas;
- decisiones probabilísticas;
- datos;
- permisos;
- integraciones;
- herramientas;
- automatizaciones;

- interfaces;
- observabilidad.
El modelo no será tratado como una capa omnipotente.
## 3. Estilo arquitectónico inicial

La arquitectura base será un:
Modular Monolith
Cada proyecto comenzará como una aplicación modular desplegable de forma unificada.
Ventajas
- menor complejidad operativa;
- transacciones más sencillas;
- desarrollo local reproducible;
- despliegue más simple;
- límites de dominio explícitos;
- posibilidad de extraer servicios posteriormente;
- menor costo de infraestructura.
Restricción
Modular monolith no significa una aplicación sin estructura.
Cada módulo deberá:
- tener responsabilidad clara;
- exponer contratos;
- ocultar detalles internos;
- evitar dependencias circulares;
- controlar acceso a sus datos;
- publicar eventos cuando sea necesario.
## 4. Evolución hacia servicios independientes

Un módulo podrá extraerse como servicio cuando exista al menos una de estas razones:
- necesidad de escalado independiente;
- requerimientos de seguridad distintos;

- carga intensiva especializada;
- ciclo de despliegue separado;
- dependencia tecnológica diferente;
- frontera de dominio estable;
- necesidad de aislamiento de fallos;
- reutilización por múltiples productos.
No se crearán microservicios únicamente para demostrar experiencia con arquitectura distribuida.
## 5. Capas arquitectónicas

La estructura lógica de referencia será:
Presentation
Application
Domain
Infrastructure
AI
Integration
Observability
No todos los módulos deberán contener físicamente todas las capas.
Sí deberán respetar sus responsabilidades.
## 6. Presentation Layer

Responsabilidad
Recibir y presentar información.
Incluye:
- endpoints HTTP;
- WebSockets;
- Server-Sent Events;
- interfaces gráficas;
- comandos;
- webhooks de entrada;
- serialización;
- validación superficial.

Puede hacer
- validar formato;
- autenticar;
- convertir solicitudes;
- invocar casos de uso;
- transformar respuestas;
- establecer códigos HTTP.
No puede hacer
- contener reglas de negocio;
- consultar directamente repositorios;
- llamar directamente proveedores de modelos;
- ejecutar SQL;
- construir prompts;
- tomar decisiones empresariales.
Ejemplo
POST /api/v1/assistant/messages
│
▼
SendAssistantMessageUseCase
El controlador deberá delegar inmediatamente al caso de uso.
## 7. Application Layer

Responsabilidad
Orquestar casos de uso.
Incluye:
- comandos;
- consultas;
- servicios de aplicación;
- coordinación;
- transacciones;
- autorización contextual;
- publicación de eventos;
- invocación de herramientas.

Ejemplos
- enviar una pregunta al asistente;
- registrar un documento;
- iniciar una indexación;
- aprobar una acción;
- consultar el historial;
- ejecutar una evaluación;
- crear un reporte.
Puede hacer
- coordinar dominio e infraestructura;
- iniciar transacciones;
- validar permisos;
- llamar puertos;
- publicar eventos;
- gestionar idempotencia.
No puede hacer
- contener detalles de proveedores;
- construir SQL;
- depender directamente de SDKs externos;
- esconder reglas dentro de prompts.
## 8. Domain Layer

Responsabilidad
Representar reglas y conceptos del negocio.
Incluye:
- entidades;
- value objects;
- agregados;
- políticas;
- servicios de dominio;
- eventos de dominio;
- invariantes;
- excepciones de dominio.

Ejemplos de entidades
GEEM AI Assistant
Organization
User
Document
KnowledgeSource
Conversation
MemoryRecord
ToolDefinition
ApprovalRequest
Restaurant AI Operations
Restaurant
Branch
SalesPeriod
InventorySnapshot
PurchaseProposal
OperationalInsight
AgentExecution
Enterprise Automation Platform
Workflow
WorkflowExecution
Integration
Trigger
Approval
AutomationAction
Regla
El dominio no deberá depender de:
- FastAPI;
- SQLAlchemy;
- OpenAI;
- Anthropic;
- Redis;
- n8n;
- LangGraph;
- librerías de infraestructura.

## 9. Infrastructure Layer

Responsabilidad
Implementar acceso a recursos externos.
Incluye:
- repositorios SQL;
- Redis;
- almacenamiento S3;
- colas;
- proveedores de identidad;
- clientes HTTP;
- SDKs;
- telemetría;
- correo;
- WhatsApp;
- CRM;
- ERP.
Ejemplos
PostgresDocumentRepository
RedisConversationCache
S3ObjectStorage
OpenAIModelProvider
AnthropicModelProvider
N8nWorkflowClient
La infraestructura implementará contratos definidos en capas superiores.
## 10. AI Layer

Responsabilidad
Concentrar capacidades específicas de inteligencia artificial.
Incluye:
- model gateway;
- prompt registry;

- structured outputs;
- retrieval;
- embeddings;
- reranking;
- tool selection;
- memory processing;
- agent orchestration;
- evaluation;
- guardrails.
Regla
La capa AI no podrá decidir por sí misma:
- permisos;
- reglas de facturación;
- políticas comerciales;
- límites de negocio;
- acceso a tenants;
- aprobación de acciones críticas.
Estas decisiones deberán provenir del dominio o la aplicación.
## 11. Integration Layer

Responsabilidad
Conectar dominios y sistemas externos mediante contratos explícitos.
Incluye:
- REST clients;
- webhooks;
- MCP;
- adapters;
- anti-corruption layers;
- mapeadores;
- integración con sistemas heredados.
Ejemplo
GEEM AI Assistant no deberá consultar directamente tablas internas de Grest.
Deberá utilizar una interfaz como:

RestaurantDataGateway
Implementada por:
GrestApiRestaurantDataGateway
Esto evita que la nueva plataforma dependa de estructuras heredadas.
## 12. Observability Layer

Responsabilidad
Registrar y correlacionar comportamiento del sistema.
Incluye:
- logs;
- traces;
- metrics;
- costos;
- tokens;
- tool calls;
- retrieval;
- errores;
- evaluaciones;
- tiempos.
Regla
La observabilidad deberá atravesar todas las capas sin contaminar la lógica de negocio.
Se utilizarán:
- correlation IDs;
- trace IDs;
- execution IDs;
- user IDs;
- tenant IDs.

## 13. Estructura base del repositorio

project/
├── apps/
│ ├── api/
│ ├── web/
│ ├── worker/
│ └── mcp_server/
│
├── src/
│ ├── modules/
│ ├── shared/
│ └── bootstrap/
│
├── tests/
│ ├── unit/
│ ├── integration/
│ ├── e2e/
│ └── evaluation/
│
├── docs/
├── infrastructure/
├── scripts/
├── docker/
├── .github/
├── docker-compose.yml
├── Makefile
└── README.md
## 14. Estructura modular recomendada

src/modules/
├── identity/
├── organizations/
├── knowledge/
├── conversations/
├── memory/
├── tools/
├── approvals/
├── agents/

├── evaluations/
└── audit/
Cada módulo podrá estructurarse como:
knowledge/
├── domain/
│ ├── entities/
│ ├── value_objects/
│ ├── services/
│ ├── events/
│ └── exceptions/
│
├── application/
│ ├── commands/
│ ├── queries/
│ ├── handlers/
│ ├── dto/
│ └── ports/
│
├── infrastructure/
│ ├── persistence/
│ ├── providers/
│ └── mappers/
│
└── presentation/
├── api/
└── schemas/
## 15. Shared Kernel

La carpeta shared deberá mantenerse pequeña.
Podrá contener:
- tipos comunes;
- errores base;
- utilidades de tiempo;
- identificadores;
- eventos;
- contratos de observabilidad;
- configuración.

No deberá convertirse en un contenedor genérico de código sin propietario.
Regla
Si una pieza pertenece claramente a un módulo, deberá permanecer en ese módulo.
## 16. Dependency Rule

Las dependencias deberán apuntar hacia el interior.
Presentation
│
▼
Application
│
▼
Domain
La infraestructura dependerá de interfaces internas:
Infrastructure ───► Application Ports
Infrastructure ───► Domain Interfaces
El dominio nunca dependerá de infraestructura.
## 17. Ports and Adapters

Se utilizará el patrón Ports and Adapters cuando exista dependencia externa relevante.
Ejemplo
ModelProvider
├── OpenAIProvider
└── AnthropicProvider

Puerto
ModelProvider
Adaptadores
OpenAIModelProvider
AnthropicModelProvider
Esto permitirá:
- pruebas;
- sustitución;
- comparación;
- aislamiento;
- control de proveedores.
## 18. Anti-Corruption Layer

Los sistemas heredados deberán integrarse mediante una capa de adaptación.
Problema
Sistemas existentes pueden contener:
- nombres inconsistentes;
- tablas heredadas;
- estados ambiguos;
- formatos antiguos;
- reglas acopladas.
Solución
Crear modelos internos limpios.
Ejemplo:
Legacy Grest Sale
│
▼

GrestSaleMapper
│
▼
RestaurantSale
La arquitectura nueva no heredará directamente los defectos del modelo anterior.
## 19. Contracts First

Toda integración importante deberá definirse mediante contrato antes de la implementación.
Tipos de contrato
- OpenAPI;
- JSON Schema;
- Pydantic models;
- eventos;
- tool schemas;
- MCP resources;
- MCP tools;
- DTOs;
- webhooks.
Ventaja
- reduce ambigüedad;
- facilita pruebas;
- permite mocks;
- desacopla equipos;
- mejora documentación.
## 20. Domain Models vs DTOs

Las entidades de dominio no deberán exponerse directamente como respuestas de API.
Se utilizarán:
- request models;
- response models;
- command DTOs;
- query DTOs;
- integration DTOs.

Razón
Evitar:
- acoplamiento;
- fuga de campos;
- cambios accidentales;
- exposición de información sensible.
## 21. Command Query Separation

Se diferenciarán:
Commands
Cambian estado.
Ejemplos:
RegisterDocument
CreateMemory
ApproveToolExecution
StartWorkflow
Queries
Solo leen.
Ejemplos:
GetConversation
SearchKnowledge
ListPendingApprovals
GetExecutionTrace
No se implementará CQRS distribuido por defecto.
Sí se utilizará separación conceptual entre lectura y escritura.
## 22. Domain Events

Los eventos de dominio representarán hechos relevantes.

Ejemplos:
DocumentRegistered
DocumentIndexed
ConversationStarted
ToolExecutionRequested
ToolExecutionApproved
InsightGenerated
WorkflowCompleted
Uso
- desacoplar módulos;
- disparar procesos;
- registrar auditoría;
- ejecutar tareas asíncronas.
Regla
Los eventos deberán describir hechos en pasado.
No deberán contener lógica.
## 23. Integration Events

Los eventos enviados a sistemas externos deberán estar versionados.
Ejemplo:
geem.document.indexed.v1
restaurant.insight.generated.v1
automation.workflow.completed.v1
Contenido mínimo
- event_id;
- event_type;
- version;
- timestamp;
- tenant_id;
- correlation_id;
- payload.

## 24. Eventos internos y externos

No todo evento de dominio deberá publicarse externamente.
Evento interno
Sirve para coordinar módulos dentro de la aplicación.
Evento externo
Forma parte de un contrato con otro sistema.
La conversión deberá ser explícita.
Domain Event
│
▼
Integration Event Mapper
│
▼
External Event
## 25. Transacciones

Los casos de uso que modifiquen múltiples entidades relacionadas deberán ejecutarse dentro de una
transacción.
Regla
La capa Application controlará el límite transaccional.
Evitar
- transacciones abiertas durante llamadas a modelos;
- transacciones largas;
- llamadas HTTP dentro de transacciones;
- bloqueo de tablas mientras se espera aprobación humana.

## 26. Unit of Work

Cuando sea necesario se utilizará Unit of Work para coordinar:
- repositorios;
- transacciones;
- eventos;
- persistencia.
Ejemplo conceptual:
with unit_of_work:
document = repository.get(...)
document.mark_indexed()
unit_of_work.commit()
No será obligatorio si el ORM y el caso de uso ya mantienen claridad suficiente.
## 27. Repository Pattern

Los repositorios se utilizarán para agregados y conceptos de dominio.
Ejemplo:
DocumentRepository
ConversationRepository
ApprovalRepository
WorkflowRepository
No se crearán repositorios genéricos universales como:
BaseRepository<T>
cuando oculten consultas importantes o produzcan abstracciones débiles.
## 28. Service Boundaries

Cada módulo deberá tener una responsabilidad principal.

Ejemplo GEEM AI Assistant
Knowledge
- documentos;
- fuentes;
- versiones;
- indexación;
- recuperación.
Conversations
- sesiones;
- mensajes;
- contexto;
- historial.
Memory
- recuerdos;
- expiración;
- corrección;
- confianza.
Tools
- definición;
- ejecución;
- permisos;
- resultados.
Approvals
- solicitudes;
- aprobadores;
- decisiones;
- expiración.
Audit
- eventos;
- cambios;
- accesos;
- ejecuciones.

## 29. Model Gateway Architecture

Application Use Case
│
▼
Model Gateway
│
├── Provider Selection
├── Prompt Resolution
├── Output Schema
├── Retry Policy
├── Cost Tracking
└── Telemetry
│
┌───────┴────────┐
▼ ▼
OpenAI Adapter Anthropic Adapter
Responsabilidades
- normalización mínima;
- selección;
- errores;
- trazas;
- uso;
- costos.
No deberá contener
- reglas de negocio;
- permisos;
- acceso directo a datos;
- lógica de dominio.
## 30. Prompt Architecture

Los prompts deberán separarse del código de aplicación.

Estructura sugerida
prompts/
├── assistant/
│ ├── system/
│ ├── retrieval/
│ └── tools/
├── evaluation/
└── versions/
Cada prompt deberá registrar
- nombre;
- versión;
- objetivo;
- variables;
- modelo recomendado;
- fecha;
- autor;
- dataset de evaluación;
- estado.
Estados
- draft;
- testing;
- approved;
- deprecated.
## 31. Prompt Composition

Los prompts podrán componerse de:
- instrucciones del sistema;
- políticas;
- contexto del usuario;
- conocimiento recuperado;
- herramientas;
- restricciones;
- formato de salida.

Regla
El contenido recuperado deberá estar claramente delimitado y tratado como datos.
No deberá mezclarse con instrucciones del sistema.
## 32. Tool Architecture

Agent
│
▼
Tool Registry
│
├── Authorization
├── Validation
├── Risk Classification
├── Approval Check
├── Execution
└── Audit
Componentes
Tool Definition
Describe:
- nombre;
- propósito;
- esquema;
- permisos;
- riesgo.
Tool Executor
Ejecuta la operación real.
Tool Policy
Determina:
- quién puede usarla;
- en qué tenant;
- bajo qué condiciones;

si requiere aprobación.
Tool Result
Devuelve un resultado estructurado.
## 33. Tool Risk Levels

Level 0 — Informational
No accede a datos sensibles.
Ejemplo:
consultar catálogo público.
Level 1 — Internal Read
Accede a datos internos autorizados.
Ejemplo:
consultar cliente.
Level 2 — Controlled Write
Crea o modifica información reversible.
Ejemplo:
crear una tarea.
Level 3 — External Action
Produce una acción fuera del sistema.
Ejemplo:
enviar un correo.
Level 4 — Critical Action
Puede producir impacto financiero, legal u operativo.

Ejemplo:
- ordenar una compra;
- cancelar una operación;
- modificar inventario.
Los niveles 3 y 4 requerirán políticas reforzadas.
## 34. Human Approval Architecture

Agent Requests Action
│
▼
Policy Evaluation
│
├── Allowed Automatically
│
└── Approval Required
│
▼
Approval Request
│
┌───────┴───────┐
▼ ▼
Approved Rejected
│ │
▼ ▼
Execute Tool Close Request
La aprobación deberá registrar
- solicitante;
- acción;
- argumentos;
- riesgo;
- aprobador;
- decisión;
- fecha;
- resultado.

## 35. Retrieval Architecture

User Query
│
▼
Query Processing
│
├── Tenant Filter
├── Permission Filter
├── Query Rewrite
└── Metadata Extraction
│
▼
Hybrid Retrieval
├── Vector Search
└── Full-Text Search
│
▼
Reranking
│
▼
Context Assembly
│
▼
Model Response
│
▼
Citation Validation
## 36. Ingestion Architecture

Document Upload
│
▼
Security Validation
│
▼
Object Storage
│
▼
Document Registration

│
▼
Background Processing
│
├── Extraction
├── Normalization
├── Classification
├── Chunking
├── Embeddings
└── Indexing
Estados sugeridos
- uploaded;
- pending;
- processing;
- indexed;
- failed;
- archived.
## 37. Memory Architecture

La memoria se dividirá en módulos distintos.
Conversation History
Mensajes de una sesión.
Working Memory
Estado temporal de una ejecución.
User Memory
Preferencias o hechos persistentes.
Organizational Knowledge
Documentación y conocimiento empresarial.

Workflow State
Estado durable de un proceso.
No se almacenarán todos estos conceptos en la misma tabla ni con la misma estrategia.
## 38. Memory Record

Cada recuerdo persistente deberá incluir:
- id;
- tenant_id;
- user_id;
- type;
- content;
- source;
- confidence;
- created_at;
- expires_at;
- corrected_at;
- status.
Estados
- active;
- superseded;
- expired;
- deleted;
- disputed.
## 39. Agent Architecture

Los agentes deberán tener:
- objetivo;
- entradas;
- herramientas;
- estado;
- límites;
- salida estructurada;
- criterio de terminación;
- política de error;

métricas.
Regla
Un agente no podrá tener acceso a todas las herramientas por defecto.
Aplicará principio de menor privilegio.
## 40. Agent State

El estado deberá ser explícito.
Ejemplo:
RestaurantOperationsState
├── tenant_id
├── restaurant_id
├── period
├── requested_analysis
├── sales_findings
├── inventory_findings
├── purchase_proposal
├── warnings
├── approvals
└── final_report
No se dependerá únicamente del historial textual para conservar estado.
## 41. Agent Termination

Todo agente deberá tener criterios de terminación.
Ejemplos:
- objetivo completado;
- herramienta fallida;
- límite de pasos;
- presupuesto excedido;
- aprobación requerida;
- información insuficiente;
- intervención humana.

No se permitirán ciclos ilimitados.
## 42. Deterministic vs Probabilistic Logic

Deterministic
Debe implementarse en código cuando exista una regla exacta.
Ejemplos:
- cálculo de impuestos;
- permisos;
- límites;
- saldos;
- estados;
- validaciones.
Probabilistic
Puede delegarse a modelos cuando exista interpretación.
Ejemplos:
- clasificación;
- resumen;
- detección de intención;
- generación de recomendaciones;
- explicación de anomalías.
Regla
Nunca se utilizará un modelo para reemplazar una regla que pueda expresarse claramente en código.
## 43. Error Taxonomy

Los errores deberán clasificarse.
Domain Errors
- regla inválida;
- estado no permitido;
- entidad inexistente.

Validation Errors
- formato incorrecto;
- campo faltante;
- esquema inválido.
Authorization Errors
- permiso insuficiente;
- tenant incorrecto;
- herramienta bloqueada.
Integration Errors
- proveedor externo;
- timeout;
- autenticación externa;
- respuesta inválida.
AI Errors
- output inválido;
- tool call incorrecto;
- contexto insuficiente;
- modelo no disponible.
Infrastructure Errors
- base de datos;
- Redis;
- almacenamiento;
- red.
## 44. Error Contract

Las APIs deberán devolver errores estructurados.
{
"error": {
"code": "TOOL_APPROVAL_REQUIRED",
"message": "The requested action requires human approval.",
"correlation_id": "..."

}
}
No deberán exponerse:
- stack traces;
- secretos;
- prompts internos;
- datos sensibles;
- detalles de infraestructura.
## 45. Retry Policy

Los reintentos deberán aplicarse solo a errores transitorios.
Reintentables
- timeout;
- rate limit;
- error temporal del proveedor;
- red intermitente.
No reintentables
- permisos;
- esquema inválido;
- regla de negocio;
- credenciales inválidas;
- acción rechazada.
Requisitos
- backoff;
- jitter;
- límite;
- trazabilidad;
- idempotencia.

## 46. Circuit Breaker

Las integraciones críticas deberán considerar circuit breaker cuando:
- el proveedor pueda fallar repetidamente;
- los errores generen cascadas;
- existan alternativas;
- sea posible degradar funcionalidad.
Ejemplo:
Primary Model Failure
│
▼
Circuit Open
│
├── Fallback Model
└── Controlled Degradation
## 47. Idempotency

Toda operación externa deberá considerar duplicados.
Ejemplos:
- webhooks;
- correos;
- tareas;
- pagos;
- actualizaciones;
- acciones de agentes.
Estrategia
- idempotency key;
- event ID;
- execution ID;
- estado previo;
- constraint única;
- registro de resultados.

## 48. Multi-Tenancy

Todo recurso empresarial deberá pertenecer a un tenant.
Campos mínimos
tenant_id
created_by
created_at
updated_at
Regla
No se aceptarán consultas empresariales sin contexto de tenant.
Controles
- filtro en repositorios;
- validación en casos de uso;
- pruebas;
- auditoría;
- políticas de base de datos cuando aplique.
## 49. Tenant Context

El contexto de tenant deberá resolverse mediante autenticación o integración autorizada.
No deberá recibirse libremente desde el frontend sin validación.
Ejemplo
Authenticated User
│
▼
Tenant Membership
│
▼
Tenant Context
│

▼
Use Case
## 50. Row-Level Security

PostgreSQL Row-Level Security será evaluado después de implementar correctamente el aislamiento en
aplicación.
Razón
RLS añade una defensa adicional, pero no reemplaza:
- autorización;
- filtros;
- pruebas;
- diseño correcto.
Se documentará mediante ADR antes de activarse.
## 51. Authentication

La autenticación deberá estar separada de la autorización.
Authentication
Determina quién es el usuario.
Authorization
Determina qué puede hacer.
Estándares
- OAuth 2.0;
- OpenID Connect;
- JWT;
- scopes;
- roles;
- permisos.

## 52. Authorization

La autorización se evaluará en diferentes niveles.
Nivel de endpoint
¿Puede acceder a esta operación?
Nivel de tenant
¿Pertenece a esta organización?
Nivel de recurso
¿Puede acceder a este documento o entidad?
Nivel de herramienta
¿Puede ejecutar esta herramienta?
Nivel de campo
¿Puede ver información sensible?
## 53. RBAC and Policies

RBAC será la base.
Ejemplos de roles:
- owner;
- administrator;
- manager;
- analyst;
- operator;
- viewer.
Para reglas complejas podrán utilizarse políticas contextuales.
Ejemplo:

Un manager puede aprobar acciones de nivel 2 dentro de su sucursal, pero no acciones
financieras de nivel 4.
## 54. Secrets Management

Los secretos deberán mantenerse fuera del código.
Prohibido
- API keys en repositorios;
- credenciales en Dockerfiles;
- tokens en logs;
- archivos .env versionados.
Aprobado
- variables de entorno;
- secret manager;
- secretos de CI/CD;
- rotación;
- permisos mínimos.
## 55. Audit Architecture

Toda acción importante deberá producir un registro de auditoría.
Campos
- actor;
- tenant;
- action;
- resource;
- previous state;
- new state;
- timestamp;
- origin;
- correlation_id;
- tool execution;
- approval.

Regla
Los registros de auditoría no deberán modificarse de forma ordinaria.
## 56. Logging Standards

Los logs deberán ser estructurados.
Campos recomendados
- timestamp;
- level;
- service;
- environment;
- tenant_id;
- user_id;
- correlation_id;
- trace_id;
- event;
- message.
Prohibido
- documentos completos;
- prompts con datos sensibles;
- contraseñas;
- tokens;
- claves;
- información personal innecesaria.
## 57. Tracing

Cada flujo deberá poder seguirse de extremo a extremo.
Ejemplo:
HTTP Request
└── Use Case
├── Retrieval
├── Model Call
├── Tool Selection

├── Tool Execution
└── Response
Cada etapa deberá producir spans relacionados.
## 58. Metrics

Métricas mínimas:
Sistema
- requests;
- errores;
- latencia;
- CPU;
- memoria;
- colas.
IA
- tokens;
- costo;
- modelo;
- tool calls;
- retries;
- output errors;
- retrieval latency;
- citation failures.
Negocio
- preguntas resueltas;
- escalaciones;
- automatizaciones completadas;
- tiempo ahorrado;
- aprobaciones;
- fallos evitados.
## 59. API Versioning

Las APIs públicas o compartidas deberán versionarse.

Ejemplo:
/api/v1/
Los cambios incompatibles requerirán nueva versión.
No se crearán versiones innecesarias para endpoints internos que puedan evolucionar coordinadamente.
## 60. Event Versioning

Los eventos externos deberán incluir versión en su nombre o esquema.
Ejemplo:
workflow.completed.v1
Un cambio incompatible requerirá:
workflow.completed.v2
## 61. Schema Evolution

Las migraciones deberán ser:
- versionadas;
- reversibles cuando sea posible;
- compatibles con despliegues;
- probadas.
Estrategia segura
- agregar campo;
- desplegar código compatible;
- migrar datos;
- activar nueva lógica;
- retirar campo anterior.
1.
2.
3.
4.
5.

## 62. Configuration Architecture

La configuración deberá diferenciar:
Static Configuration
- puertos;
- URLs;
- feature flags;
- límites.
Business Configuration
- reglas;
- permisos;
- thresholds;
- políticas.
Prompt Configuration
- versiones;
- modelos;
- temperatura;
- parámetros.
No se mezclarán todos estos conceptos en una sola tabla genérica.
## 63. Feature Flags

Los cambios de comportamiento importantes podrán utilizar feature flags.
Ejemplos:
- nuevo modelo;
- nuevo retriever;
- nuevo prompt;
- nueva herramienta;
- nuevo workflow.
Regla
Todo feature flag deberá tener:
- propietario;

- fecha de creación;
- propósito;
- plan de retiro.
## 64. Background Jobs

Los procesos largos deberán ejecutarse fuera del request principal.
Ejemplos:
- ingestión;
- embeddings;
- evaluación;
- reportes;
- análisis;
- sincronización.
Requisitos
- estado;
- retries;
- timeout;
- cancelación;
- progreso;
- idempotencia;
- observabilidad.
## 65. Workflow State

Los workflows durables deberán persistir:
- estado actual;
- pasos completados;
- errores;
- aprobaciones;
- entradas;
- resultados;
- timestamps.
No deberán depender únicamente de memoria del proceso.

## 66. Webhook Architecture

External Provider
│
▼
Webhook Endpoint
│
├── Signature Validation
├── Replay Protection
├── Idempotency
└── Event Registration
│
▼
Async Processing
El endpoint deberá responder rápidamente.
El procesamiento completo ocurrirá fuera de la solicitud cuando sea necesario.
## 67. MCP Architecture

AI Client
│
▼
MCP Server
│
├── Authentication
├── Tenant Resolution
├── Resource Registry
├── Tool Registry
├── Authorization
└── Audit
Regla
MCP deberá reutilizar servicios de aplicación existentes.
No contendrá una segunda implementación paralela de la lógica de negocio.

## 68. Frontend Architecture

La interfaz web deberá organizarse por features.
src/
├── app/
├── features/
│ ├── chat/
│ ├── documents/
│ ├── approvals/
│ ├── evaluations/
│ └── settings/
├── shared/
└── infrastructure/
Regla
No se utilizará una estructura global basada únicamente en:
components/
services/
utils/
cuando esto oculte los límites funcionales.
## 69. Frontend Data Access

El frontend deberá utilizar una capa de API.
No realizará:
- llamadas dispersas;
- manejo inconsistente de tokens;
- transformación duplicada;
- lógica de permisos local como única defensa.
La autorización real siempre se validará en backend.

## 70. Streaming UI

Las interfaces de agentes deberán mostrar estados comprensibles.
Ejemplos:
- buscando documentación;
- analizando datos;
- preparando acción;
- esperando aprobación;
- generando respuesta.
No deberán exponer razonamiento interno del modelo.
Sí deberán mostrar eventos operativos y trazables.
## 71. Testing Architecture

Unit Tests
- dominio;
- políticas;
- herramientas;
- validación;
- parsers;
- mappers.
Integration Tests
- PostgreSQL;
- Redis;
- providers;
- APIs;
- object storage;
- MCP.
Contract Tests
- webhooks;
- tools;
- APIs;
- eventos.

End-to-End
- flujos completos;
- aprobación;
- chat;
- documentos;
- automatización.
Evaluation Tests
- RAG;
- prompts;
- modelos;
- agentes;
- herramientas.
## 72. Test Doubles

Se utilizarán:
- fakes;
- stubs;
- mocks;
- test containers.
Regla
Las pruebas unitarias no deberán depender de proveedores reales.
Las pruebas de integración controladas sí podrán utilizar servicios externos mediante entornos separados.
## 73. Architecture Decision Records

Toda decisión relevante deberá documentarse.
Ejemplos:
ADR-0001-use-modular-monolith
ADR-0002-use-postgresql-and-pgvector
ADR-0003-select-model-gateway

ADR-0004-use-sse-for-streaming
ADR-0005-tool-approval-policy
Estados
- proposed;
- accepted;
- superseded;
- rejected;
- deprecated.
## 74. Diagram Standards

Cada proyecto deberá incluir:
C4 Context
Actores y sistemas externos.
C4 Container
Aplicaciones, bases, colas y servicios.
Component Diagram
Módulos internos relevantes.
Sequence Diagrams
Flujos críticos.
Deployment Diagram
Infraestructura.
Data Flow Diagram
Datos sensibles y límites de confianza.

## 75. Sequence Diagrams Required

Como mínimo deberán documentarse:
- conversación con RAG;
- ingestión documental;
- tool calling;
- aprobación humana;
- ejecución agéntica;
- webhook;
- workflow automatizado;
- error y recuperación.
## 76. Threat Modeling

Cada proyecto deberá crear un threat model.
Elementos
- activos;
- actores;
- fronteras;
- entradas;
- datos;
- herramientas;
- integraciones;
- amenazas;
- mitigaciones.
Riesgos específicos
- prompt injection;
- indirect prompt injection;
- tool abuse;
- data leakage;
- tenant escape;
- excessive agency;
- poisoned documents;
- replay attacks;
- credential theft.

## 77. Performance Standards

Cada flujo importante deberá definir presupuesto de:
- latencia;
- tokens;
- costo;
- pasos;
- retries;
- memoria.
Ejemplo
Simple knowledge query:
p95 latency: < 8 seconds
tool calls: <= 2
model calls: <= 2
Los objetivos exactos se establecerán por proyecto.
## 78. Cost Architecture

Los costos de IA deberán relacionarse con:
- tenant;
- usuario;
- proyecto;
- feature;
- modelo;
- workflow;
- ejecución.
Esto permitirá:
- presupuestos;
- límites;
- análisis;
- chargeback;
- optimización.

## 79. Data Retention

Cada tipo de dato deberá definir retención.
Ejemplos:
- mensajes;
- documentos;
- embeddings;
- trazas;
- auditoría;
- prompts;
- tool results;
- evaluaciones.
No se conservarán datos indefinidamente por defecto.
## 80. Privacy by Design

Se aplicarán:
- minimización;
- propósito definido;
- retención;
- anonimización;
- redacción;
- consentimiento cuando corresponda;
- acceso restringido.
Los datasets de evaluación no deberán contener información sensible innecesaria.
## 81. Failure Modes

Cada componente deberá documentar:
- cómo falla;
- impacto;
- detección;
- recuperación;
- degradación.

Ejemplo
Vector Search Failure
- registrar error;
- intentar búsqueda textual;
- informar menor precisión;
- evitar respuesta inventada.
Model Provider Failure
- retry controlado;
- fallback;
- cola;
- mensaje al usuario;
- trazabilidad.
## 82. Graceful Degradation

El sistema deberá continuar ofreciendo valor cuando una capacidad secundaria falle.
Ejemplos:
- sin embeddings, usar búsqueda textual;
- sin proveedor principal, usar proveedor alterno;
- sin memoria, continuar conversación actual;
- sin herramienta externa, responder con conocimiento disponible;
- sin n8n, registrar tarea pendiente.
## 83. Architecture Review Checklist

Antes de aprobar un módulo deberá verificarse:
- responsabilidad clara;
- límites definidos;
- dependencias correctas;
- contratos;
- seguridad;
- multi-tenancy;
- errores;
- pruebas;
- observabilidad;
- costos;

- documentación;
- recuperación.
## 84. Violaciones arquitectónicas

Se considerarán violaciones:
- SDK de OpenAI dentro de controladores;
- SQL generado libremente por el modelo;
- prompt con reglas empresariales críticas;
- acceso directo entre módulos sin contrato;
- datos sin tenant;
- herramientas sin autorización;
- acciones externas sin idempotencia;
- errores sin correlación;
- workflows sin estado persistente;
- prompts sin versión;
- modelos sin trazabilidad.
## 85. Excepciones

Una excepción arquitectónica podrá aprobarse cuando:
- exista una razón concreta;
- reduzca riesgo o complejidad;
- esté limitada;
- tenga pruebas;
- sea documentada mediante ADR;
- incluya estrategia de revisión.
## 86. Estándar de madurez arquitectónica

Nivel 1 — Functional
El flujo funciona.
Nivel 2 — Structured
Existe separación de responsabilidades.

Nivel 3 — Reliable
Existen pruebas, errores y observabilidad.
Nivel 4 — Secure
Existen controles, aislamiento y auditoría.
Nivel 5 — Production Ready
Existen métricas, recuperación, documentación y operación.
Los proyectos no se considerarán terminados antes del nivel 5 en sus flujos principales.
## 87. Aplicación al Proyecto 1

GEEM AI Assistant comenzará con los módulos:
identity
organizations
knowledge
conversations
retrieval
memory
tools
approvals
providers
evaluations
audit
Arquitectura inicial
React Web
│
▼
FastAPI
│
├── Identity
├── Knowledge
├── Conversations
├── Retrieval

├── Tools
├── Memory
└── Evaluation
│
├── PostgreSQL
├── pgvector
├── Redis
├── Object Storage
├── OpenAI
└── Anthropic
## 88. Aplicación al Proyecto 2

Restaurant AI Operations deberá separar:
restaurants
sales
inventory
purchasing
menu_intelligence
customer_experience
agents
approvals
reports
evaluations
Los agentes consumirán servicios de aplicación.
No accederán directamente a tablas operativas.
## 89. Aplicación al Proyecto 3

Enterprise Automation Platform deberá separar:
workflows
triggers
integrations
executions
approvals
notifications

credentials
audit
ai_decisions
n8n actuará como orquestador externo.
La lógica central permanecerá en servicios versionados.
## 90. Decisiones oficiales

Quedan aprobadas las siguientes reglas:
La arquitectura inicial será modular monolith.
Las capas tendrán responsabilidades explícitas.
El dominio no dependerá de infraestructura.
Los proveedores externos se integrarán mediante adapters.
Las integraciones heredadas utilizarán anti-corruption layers.
Los contratos se definirán antes de implementaciones críticas.
Commands y Queries se separarán conceptualmente.
Los eventos externos estarán versionados.
Las transacciones no permanecerán abiertas durante llamadas AI.
Tool calling pasará por registro, políticas y auditoría.
Las acciones de alto impacto requerirán aprobación humana.
RAG tendrá pipelines separados de ingestión y consulta.
Memoria, conversación y conocimiento serán conceptos distintos.
Los agentes tendrán estado y criterios de terminación.
La lógica determinista permanecerá en código.
Los errores tendrán taxonomía y contrato.
Todas las operaciones externas deberán considerar idempotencia.
Todo recurso empresarial deberá pertenecer a un tenant.
La observabilidad será transversal.
Toda decisión importante se documentará mediante ADR.
## 91. Próximo documento

Documento 04 — Repository Standards
Definirá:
- estructura física;
- nombres;
- ramas;
- 1.
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

- commits;
- pull requests;
- issues;
- milestones;
- versionado;
- releases;
- documentación;
- automatización;
- políticas de seguridad;
- estándares de publicación.
## 92. Conclusión

Los proyectos del AI Engineering Lab deberán demostrar algo más que integración con modelos.
Deberán demostrar capacidad para diseñar sistemas donde:
- el dominio permanece protegido;
- las reglas son visibles;
- las herramientas son controladas;
- los agentes tienen límites;
- los datos están aislados;
- las integraciones son reemplazables;
- los errores son investigables;
- las decisiones son documentadas;
- la operación es reproducible.
La arquitectura deberá permitir que cada sistema crezca sin perder claridad.
El objetivo no será construir aplicaciones que solamente funcionen.
Será construir productos que puedan mantenerse, auditarse, evaluarse y defenderse técnicamente.
