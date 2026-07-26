# AI Engineering Lab

## Documento 13 --- Project 1 API & Contract Standards

GEEM AI Assistant **Versión:** 1.0 **Estado:** Estándar oficial de
contratos **Responsable técnico:** Director de AI Engineering **Lead
Engineer:** Erick Eduardo Evangelista Velasco **Proyecto:** GEEM AI
Assistant **Backend:** Python + FastAPI + Pydantic **Frontend:** React +
TypeScript **Estilo principal:** REST + SSE + eventos asíncronos + MCP

## 1. Propósito

Este documento define los estándares oficiales para diseñar,
implementar, versionar y validar los contratos de GEEM AI Assistant.

Incluye los contratos utilizados entre:

-   frontend y backend;
-   módulos internos;
-   API y workers;
-   productores y consumidores de eventos;
-   AI Runtime y proveedores;
-   Model Gateway y casos de uso;
-   Tool Registry y tools;
-   sistema y clientes MCP;
-   servicios internos e integraciones externas.

El objetivo es eliminar ambigüedad y evitar que cada componente
interprete los datos de forma distinta.

## 2. Principio rector

Todo límite del sistema deberá estar definido mediante un contrato
explícito, versionado y verificable.

Un contrato no es solamente una estructura JSON.

También define:

-   significado;
-   reglas;
-   permisos;
-   estados;
-   errores;
-   compatibilidad;
-   versionado;
-   expectativas de comportamiento.

## 3. Contract First

Antes de implementar una integración relevante deberán definirse:

## 1. propósito;

## 2. consumidor;

## 3. productor;

## 4. request;

## 5. response;

## 6. errores;

## 7. autorización;

## 8. idempotencia;

## 9. versionado;

## 10. observabilidad.

No se implementará primero un endpoint para después descubrir qué
contrato debía tener.

## 4. Tipos de contratos

GEEM AI Assistant utilizará:

Contratos HTTP REST y streaming.

Contratos internos Commands, queries, DTOs y puertos.

Contratos AI Requests, respuestas estructuradas y tool calls.

Contratos de eventos Domain events e integration events.

Contratos de jobs Mensajes procesados por workers.

Contratos MCP Resources, prompts y tools.

Contratos de proveedor Adapters externos.

## 5. Fuentes de verdad

Las fuentes de verdad serán:

Contrato Fuente principal

REST API OpenAPI generado por FastAPI

DTO backend Pydantic

Tipos frontend Generados o derivados de OpenAPI

Structured Outputs JSON Schema + Pydantic

Tools Tool Registry + JSON Schema

Eventos Schemas versionados

Jobs Schemas versionados

MCP Definiciones MCP + casos de uso

Base de datos Migraciones Alembic

No deberán existir copias manuales inconsistentes del mismo contrato.

## 6. API Style

La API pública utilizará principalmente:

REST

Para respuestas progresivas se utilizará:

Server-Sent Events

Para integraciones externas podrán utilizarse:

Webhooks

Para clientes AI compatibles:

Model Context Protocol

## 7. Base URL

La API utilizará:

``` text
/api/v1
```

Ejemplo:

https://assistant.geem.example/api/v1/conversations

## 8. Versionado

El versionado principal estará en la URL.

``` text
/api/v1
/api/v2
```

No se creará una nueva versión por cada cambio menor.

Una versión mayor será necesaria cuando exista un cambio incompatible
que no pueda resolverse mediante evolución aditiva.

## 9. Cambios compatibles

Se consideran compatibles:

-   agregar un campo opcional;
-   agregar un endpoint;
-   agregar un valor de enum cuando el consumidor esté preparado;
-   agregar metadata;
-   agregar filtros;
-   agregar una nueva variante de respuesta documentada;
-   agregar eventos opcionales.

## 10. Cambios incompatibles

Se consideran incompatibles:

-   eliminar un campo;
-   renombrar un campo;
-   cambiar su tipo;
-   convertir un campo opcional en obligatorio;
-   cambiar significado;
-   eliminar valores de enum;
-   cambiar estructura de errores;
-   modificar semántica de idempotencia;
-   modificar permisos de forma inesperada.

## 11. Convenciones de URL

Las rutas deberán:

-   utilizar sustantivos;

-   usar plural;

-   usar kebab-case cuando exista más de una palabra;

-   evitar verbos innecesarios;

-   representar recursos y relaciones.

Correcto

``` text
GET /api/v1/conversations
GET /api/v1/documents/{document_id}
POST /api/v1/approval-requests/{approval_id}/decisions
```

Evitar

``` text
GET /api/v1/getConversations
POST /api/v1/createDocument
POST /api/v1/approveActionNow
```

## 12. Acciones que no son CRUD

Cuando una acción no pueda representarse claramente mediante CRUD se
podrá utilizar una subruta de acción.

Ejemplos:

``` text
POST /api/v1/documents/{document_id}/retry
POST /api/v1/conversations/{conversation_id}/archive
POST /api/v1/tool-executions/{execution_id}/cancel
```

Estas acciones deberán representar una transición real del dominio.

## 13. Métodos HTTP

Método Uso

GET Consultar sin modificar estado

POST Crear recurso o ejecutar comando

PUT Reemplazo completo excepcional

Método Uso

PATCH Actualización parcial

``` text
DELETE      Eliminar o solicitar eliminación
```

GET nunca deberá producir efectos empresariales.

## 14. Códigos HTTP

Código Significado

200 Operación exitosa

201 Recurso creado

202 Operación aceptada para procesamiento

204 Operación exitosa sin body

400 Request inválido

401 No autenticado

403 No autorizado

404 Recurso no encontrado o no visible

409 Conflicto

412 Precondición fallida

422 Validación semántica

429 Rate limit

500 Error interno

502 Fallo de proveedor

503 Servicio no disponible

504 Timeout de dependencia

## 15. 400 vs 422

400 Bad Request Se usará cuando:

-   el request no puede interpretarse;
-   existen headers inválidos;
-   el JSON está mal formado;
-   existe una combinación general inválida.

422 Unprocessable Entity Se usará cuando:

-   el JSON es válido;
-   pero los datos violan reglas de esquema o negocio de entrada.

## 16. Naming Convention

Los campos JSON usarán:

snake_case

Ejemplo:

``` text
{
"conversation_id": "01J...",
"created_at": "2026-07-20T20:00:00Z"
}
```

Esta convención coincidirá con Python.

El frontend podrá consumirla directamente o transformarla de manera
centralizada, pero no campo por campo.

## 17. Identificadores

Los identificadores se representarán como strings opacos.

``` text
{
"id": "01J2KPX9Z3M6Y7S8A4B5C6D7E8"
}
```

Los clientes no deberán inferir información a partir del formato.

## 18. Fechas

Todas las fechas se enviarán en ISO 8601 con zona horaria.

2026-07-20T18:45:00Z

No se enviarán timestamps ambiguos.

## 19. Duraciones

Las duraciones cortas podrán representarse mediante unidades explícitas.

``` text
{
"latency_ms": 1840
}
```

Para duraciones configurables podrá utilizarse formato ISO 8601 cuando
aporte claridad.

## 20. Dinero

Los valores monetarios deberán incluir monto y moneda.

``` text
{
"amount": "0.0245",
"currency": "USD"
}
```

El monto se representará como string decimal, no float.

## 21. Booleanos

Los booleanos deberán expresar condiciones claras.

Correcto

``` text
{
"requires_approval": true
}
```

Evitar

``` text
{
"status": true
}
```

## 22. Enums

Los enums usarán valores en snake_case.

``` text
{
"status": "waiting_for_approval"
}
```

Los consumidores deberán manejar valores desconocidos de forma segura
cuando sea posible.

## 23. Campos opcionales

Un campo opcional deberá distinguir entre:

-   ausente;
-   nulo;
-   vacío.

No se usarán de forma indistinta.

Ejemplo:

-   ausente: no fue solicitado;
-   null : se conoce que no existe;
-   \[\] : existe una colección sin elementos.

## 24. Request metadata

La metadata técnica deberá viajar preferentemente en headers.

Headers iniciales:

Authorization Content-Type Accept X-Request-Id X-Correlation-Id
Idempotency-Key If-Match

## 25. X-Request-Id

Identifica una request HTTP individual.

El cliente podrá enviarlo.

Si no existe, el servidor lo generará.

## 26. X-Correlation-Id

Relaciona múltiples operaciones pertenecientes a un mismo flujo.

Ejemplo:

-   request inicial;
-   job;
-   tool execution;
-   approval;
-   webhook.

El servidor deberá propagarlo.

## 27. Execution ID

Las capacidades AI tendrán adicionalmente:

execution_id

Este identificador representará una ejecución completa del asistente.

No sustituye al trace ID ni al request ID.

## 28. Response metadata

Las respuestas relevantes podrán incluir:

``` text
{
"data": {},
"meta": {
"request_id": "req_123",
"correlation_id": "corr_123"
}
}
```

Sin embargo, para recursos simples se permitirá devolver directamente el
recurso y colocar los identificadores técnicos en headers.

La API deberá elegir una convención consistente por categoría.

## 29. Envelope de recursos

Para colecciones se utilizará un envelope.

``` text
{
"items": [],
"pagination": {},

"meta": {}
}
```

Para un recurso individual se devolverá directamente el objeto, salvo
que exista necesidad de incluir datos relacionados de primer nivel.

## 30. Pagination Strategy

La paginación preferida será por cursor.

Se usará para:

-   conversaciones;
-   mensajes;
-   documentos;
-   auditoría;
-   ejecuciones;
-   aprobaciones.

## 31. Request de paginación

``` text
GET /api/v1/conversations?limit=25&after=cursor_value
```

Campos:

limit after before

No se utilizarán simultáneamente after y before .

## 32. Response de paginación

``` text
{
"items": [],
"pagination": {
"limit": 25,

"next_cursor": "next_cursor_value",
"previous_cursor": null,
"has_more": true
}
}
```

## 33. Page-number pagination

Solo se utilizará cuando:

-   el dataset sea pequeño;
-   exista necesidad clara de navegación por páginas;
-   el orden sea estable;
-   el costo de offsets sea aceptable.

No será la opción predeterminada.

## 34. Sorting

Formato:

sort=-created_at,title

Reglas:

-   -   indica descendente;
-   sin prefijo indica ascendente;
-   solo se aceptan campos permitidos;
-   el orden deberá ser estable;
-   se agregará un criterio secundario por ID cuando sea necesario.

## 35. Filtering

Los filtros simples usarán query parameters.

``` text
GET /api/v1/documents?status=available&document_type=pdf
```

Para filtros complejos podrá utilizarse una sintaxis documentada o un
endpoint de búsqueda mediante POST.

## 36. Search endpoints

Las búsquedas semánticas o con criterios complejos podrán utilizar:

``` text
POST /api/v1/knowledge/search
```

Request:

``` text
{
"query": "procedimiento de instalación de red",
"filters": {
"document_types": ["pdf", "markdown"],
"classification": ["internal"]
},
"limit": 10
}
```

## 37. Sparse fieldsets

No se incorporarán inicialmente.

Se priorizarán DTOs específicos sobre respuestas genéricas con selección
arbitraria de campos.

## 38. Resource expansion

Cuando se requiera información relacionada se podrá utilizar:

include=sources,permissions

Solo se permitirán relaciones aprobadas.

No se aceptará expansión recursiva ilimitada.

## 39. Error Contract

La API utilizará un contrato inspirado en RFC 7807, extendido para las
necesidades del producto.

``` text
{
"type": "https://errors.geem.example/document-not-ready",
"title": "Document not ready",
"status": 409,
"detail": "El documento todavía no está disponible para consulta.",
"code": "DOCUMENT_NOT_READY",
"instance": "/api/v1/documents/01J...",
"request_id": "req_123",
"correlation_id": "corr_123",
"retryable": false,
"errors": []
}
```

## 40. Campos del error

Campo Uso

type Identificador documental del tipo de error

title Nombre breve

status Código HTTP

detail Mensaje seguro

code Código estable para software

instance Recurso o request

request_id Request concreta

correlation_id Flujo relacionado

retryable Indica si podría reintentarse

errors Detalles de validación

## 41. Validation errors

``` text
{
"type": "https://errors.geem.example/validation-error",
"title": "Validation error",
"status": 422,
"detail": "Uno o más campos son inválidos.",
"code": "VALIDATION_ERROR",
"request_id": "req_123",
"retryable": false,
"errors": [
{
"field": "title",
"code": "required",
"message": "El título es obligatorio."
}
]
}
```

## 42. Error codes

Los códigos usarán uppercase snake case.

CONVERSATION_NOT_FOUND DOCUMENT_NOT_READY TENANT_ACCESS_DENIED
APPROVAL_EXPIRED TOOL_ARGUMENTS_INVALID MODEL_PROVIDER_UNAVAILABLE
STRUCTURED_OUTPUT_INVALID RATE_LIMIT_EXCEEDED

## 43. Seguridad de errores

Los errores no deberán revelar:

-   stack traces;

-   SQL;

-   rutas internas;

-   nombres de tablas;

-   secretos;

-   IDs de otros tenants;

-   prompts internos;

-   payloads sensibles.

## 44. Localización

El campo code será estable e independiente del idioma.

title , detail y mensajes de validación podrán localizarse.

## 45. Idempotency

Las operaciones de creación o ejecución con riesgo de duplicidad deberán
aceptar:

Idempotency-Key

Ejemplos:

-   cargar documento;
-   crear tool execution;
-   crear ticket;
-   procesar webhook;
-   iniciar job;
-   registrar pago futuro.

## 46. Idempotency behavior

Cuando se repita una request con la misma key y mismo payload:

-   deberá devolverse el resultado previo;
-   no se repetirá el efecto.

Cuando se repita la key con payload diferente:

409 IDEMPOTENCY_KEY_CONFLICT

## 47. Idempotency response headers

Podrán incluir:

Idempotency-Replayed: true

## 48. Concurrency Control

Para recursos con optimistic concurrency se utilizará:

ETag If-Match

Ejemplo:

ETag: "version-7"

Request:

If-Match: "version-7"

Si la versión cambió:

412 PRECONDITION_FAILED

## 49. Request DTOs vs Domain Models

Los modelos HTTP no serán entidades de dominio.

Ejemplo:

``` text
class CreateConversationRequest(BaseModel):
```

title: str \| None = Field(default=None, max_length=160) language:
Literal\["es", "en"\] = "es"

Este DTO será transformado en un command.

## 50. Response DTOs

Los response DTOs deberán:

-   ocultar campos internos;
-   exponer solo información autorizada;
-   usar tipos explícitos;
-   ser estables;
-   evitar retornar modelos ORM.

## 51. Ejemplo de response DTO

``` text
from datetime import datetime
from typing import Literal
from pydantic import BaseModel

class ConversationResponse(BaseModel):
```

id: str title: str status: Literal\["active", "archived", "locked"\]
language: Literal\["es", "en"\] created_at: datetime updated_at:
datetime

## 52. Pydantic Standards

Se utilizará Pydantic para:

-   request validation;

-   response serialization;

-   structured outputs;

-   eventos;

-   jobs;

-   tool schemas;

-   configuración.

## 53. Reglas Pydantic

Los modelos deberán:

-   prohibir campos inesperados cuando el riesgo lo amerite;
-   declarar límites;
-   utilizar enums;
-   utilizar tipos específicos;
-   incluir ejemplos;
-   separar input de output;
-   evitar diccionarios sin esquema.

## 54. Configuración base recomendada

``` text
from pydantic import BaseModel, ConfigDict

class ContractModel(BaseModel):
```

model_config = ConfigDict( extra="forbid", str_strip_whitespace=True,
validate_assignment=True, )

No será obligatorio usar validate_assignment en DTOs inmutables si no
aporta valor.

## 55. Strings

Todo string deberá considerar:

-   longitud mínima;

-   longitud máxima;

-   normalización;

-   caracteres permitidos;

-   sensibilidad;

-   sanitización de presentación.

Ejemplo:

title: str = Field(min_length=1, max_length=160)

## 56. Metadata schemas

Se evitará:

metadata: dict

Se preferirá:

``` text
class DocumentMetadata(BaseModel):
```

source: str \| None = None category: str \| None = None tags:
list\[str\] = \[\]

Cuando metadata sea extensible se usarán límites explícitos.

## 57. OpenAPI

FastAPI generará OpenAPI.

La especificación deberá incluir:

-   summaries;
-   descriptions;
-   tags;
-   operation IDs;
-   ejemplos;
-   errores;
-   seguridad;
-   schemas;
-   deprecaciones.

## 58. Operation IDs

Los operation IDs serán explícitos y estables.

Ejemplos:

create_conversation list_conversations send_conversation_message
upload_document approve_request

Servirán para generación de clientes.

## 59. OpenAPI quality gate

Un endpoint no estará listo si OpenAPI no permite entender:

-   qué hace;
-   qué recibe;
-   qué responde;
-   qué permisos necesita;
-   qué errores puede generar.

## 60. SDK Generation

El frontend deberá consumir tipos generados o derivados automáticamente
de OpenAPI.

Opciones:

-   openapi-typescript;
-   Orval;
-   herramienta equivalente aprobada.

No se duplicarán manualmente todos los DTOs en TypeScript.

## 61. API Client

El cliente frontend deberá centralizar:

-   base URL;
-   autenticación;
-   headers;
-   correlation IDs;
-   errores;
-   refresh;
-   retries permitidos;
-   parsing;
-   cancelación.

## 62. Retry del cliente

El frontend solo deberá reintentar automáticamente:

-   GET idempotentes;
-   errores de red temporales;
-   502, 503 o 504 controlados;
-   429 respetando Retry-After .

No deberá reintentar POST con efectos sin idempotency key.

## 63. Authentication Contract

Header:

Authorization: Bearer `<access_token>`{=html}

El token deberá representar identidad.

El tenant activo se resolverá mediante membership y contexto autorizado.

## 64. Endpoint GET /me

Response conceptual:

``` text
{
"user": {
"id": "usr_123",
"email": "erick@example.com",
"display_name": "Erick Evangelista",
"preferred_language": "es"
},
"active_context": {
"organization_id": "org_123",
"tenant_id": "ten_123",
"membership_id": "mem_123",
"roles": ["owner"],
"permissions": [
"conversations.create",
"documents.read"
]
}
}
```

## 65. Tenant switching

El cambio de tenant deberá realizarse mediante un caso de uso
autorizado.

Ejemplo:

``` text
POST /api/v1/session/active-context
```

Request:

``` text
{
"tenant_id": "ten_456"
}
```

No bastará con enviar arbitrariamente X-Tenant-Id .

## 66. Conversation API

Endpoints iniciales:

``` text
POST /api/v1/conversations
GET /api/v1/conversations
GET /api/v1/conversations/{conversation_id}
PATCH /api/v1/conversations/{conversation_id}
POST /api/v1/conversations/{conversation_id}/archive
POST /api/v1/conversations/{conversation_id}/messages
```

## 67. Crear conversación

Request:

``` text
{
"title": "Consulta sobre instalación",
"language": "es"
}
```

Response 201 :

``` text
{
"id": "conv_123",
"title": "Consulta sobre instalación",
"status": "active",
"language": "es",
"created_at": "2026-07-20T20:00:00Z",
"updated_at": "2026-07-20T20:00:00Z"
}
```

## 68. Enviar mensaje

Endpoint:

``` text
POST /api/v1/conversations/{conversation_id}/messages
```

Request:

``` text
{
"content": "¿Cuál es el procedimiento para instalar una red?",

"response_mode": "stream",
"capability_hint": null
}
```

## 69. Response no streaming

``` text
{
"user_message": {
"id": "msg_user_123",
"role": "user",
"content": "¿Cuál es el procedimiento para instalar una red?",
"status": "completed",
"created_at": "2026-07-20T20:01:00Z"
},
"assistant_execution": {
"id": "exec_123",
"status": "completed",
"capability": "knowledge_query"
},
"assistant_message": {
"id": "msg_assistant_123",
"role": "assistant",
"response": {
"response_type": "knowledge_answer",
"message": "El procedimiento comienza con...",
"citations": [],
"actions": [],
"confidence": "high",
"abstained": false,
"schema_version": "1.0"
},
"status": "completed",
"created_at": "2026-07-20T20:01:04Z"
}
}
```

## 70. Streaming con SSE

El cliente deberá enviar:

Accept: text/event-stream

El servidor responderá:

Content-Type: text/event-stream Cache-Control: no-cache Connection:
keep-alive

## 71. Formato SSE

Cada evento tendrá:

id: `<event_id>`{=html} event: `<event_type>`{=html} data:
`<json>`{=html}

Ejemplo:

id: evt_001 event: response.started data: {"execution_id":"exec_123"}

## 72. Eventos SSE

response.started

``` text
{
"execution_id": "exec_123",
"message_id": "msg_assistant_123"
}
```

response.delta

``` text
{
"execution_id": "exec_123",

"delta": "El procedimiento"
}
```

retrieval.started

``` text
{
"execution_id": "exec_123"
}
```

retrieval.completed

``` text
{
"execution_id": "exec_123",
"sources_found": 5,
"sources_selected": 3
}
```

tool.requested

``` text
{
"execution_id": "exec_123",
"tool_execution_id": "tool_exec_123",
"tool_key": "create_support_ticket"
}
```

approval.required

``` text
{
"execution_id": "exec_123",
"approval_request_id": "approval_123"
}
```

response.completed

``` text
{
"execution_id": "exec_123",
"response": {}
}
```

response.failed

``` text
{
"execution_id": "exec_123",
"error": {
"code": "MODEL_PROVIDER_UNAVAILABLE",
"retryable": true
}
}
```

## 73. SSE ordering

Los eventos de una ejecución deberán enviarse en orden.

Cada evento deberá tener:

-   event ID;
-   execution ID;
-   timestamp implícito o explícito;
-   schema version cuando sea necesario.

## 74. SSE reconnect

La primera versión podrá no reanudar streams interrumpidos.

Sin embargo, el cliente podrá consultar el estado de la ejecución:

``` text
GET /api/v1/assistant-executions/{execution_id}
```

La reanudación mediante Last-Event-ID podrá incorporarse posteriormente.

## 75. Cancelación de ejecución

``` text
POST /api/v1/assistant-executions/{execution_id}/cancel
```

La cancelación será best effort.

Response:

``` text
{
"id": "exec_123",
"status": "cancelled"
}
```

## 76. Assistant Execution Contract

``` text
class AssistantExecutionResponse(ContractModel):
```

id: str conversation_id: str status: Literal\[

``` text
"created",
"running",
"waiting_for_approval",
"completed",
"failed",
"cancelled",
"timed_out",
]
```

capability: str prompt_reference: str \| None model: str \| None
provider: str \| None latency_ms: int \| None cost: MoneyResponse \|
None error: ErrorSummary \| None

## 77. Structured AI Response

Modelo conceptual:

``` text
from typing import Literal

class CitationResponse(ContractModel):
```

citation_key: str document_id: str

document_version_id: str title: str location: str \| None excerpt: str

``` text
class SuggestedAction(ContractModel):
```

action_type: str label: str tool_key: str \| None = None
requires_approval: bool = False

``` text
class AssistantStructuredResponse(ContractModel):
```

schema_version: Literal\["1.0"\] response_type: Literal\[

``` text
"direct_answer",
"knowledge_answer",
"clarification",
"abstention",
"tool_result",
"approval_request",
"error",
]
```

message: str citations: list\[CitationResponse\] actions:
list\[SuggestedAction\] confidence: Literal\["low", "medium", "high",
"verified"\] abstained: bool

## 78. Structured Response invariants

-   knowledge_answer requiere al menos una cita;
-   abstention requiere abstained=true ;
-   respuestas no abstinentes requieren abstained=false ;
-   approval_request requiere acción relacionada;
-   tool_result requiere referencia a tool execution;
-   verified solo podrá utilizarse cuando exista validación determinista
    suficiente.

## 79. AI Request Contract

Contrato interno conceptual:

``` text
class ModelMessage(ContractModel):
```

role: Literal\["system", "user", "assistant", "tool"\] content: str
name: str \| None = None tool_call_id: str \| None = None

``` text
class ModelExecutionRequest(ContractModel):
```

capability: str messages: list\[ModelMessage\] prompt_key: str
prompt_version: str output_schema_name: str \| None tool_keys:
list\[str\] tenant_id: str execution_id: str max_output_tokens: int
temperature: float \| None timeout_ms: int

## 80. Model Gateway Response

``` text
class ModelUsage(ContractModel):
```

input_tokens: int \| None output_tokens: int \| None cached_tokens: int
\| None reasoning_tokens: int \| None total_tokens: int \| None

``` text
class ModelExecutionResult(ContractModel):
```

provider: str model: str content: dict \| str \| None tool_calls:
list\["ModelToolCall"\] finish_reason: str usage: ModelUsage latency_ms:
int estimated_cost: MoneyResponse fallback_used: bool validation_status:
Literal\["valid", "repaired", "invalid"\]

## 81. Provider adapters

Los adapters traducirán entre:

ModelExecutionRequest

y el SDK particular.

El resto del sistema no deberá utilizar objetos nativos de OpenAI o
Anthropic.

## 82. Tool Definition Contract

``` text
class ToolDefinitionContract(ContractModel):
```

key: str version: str display_name: str description: str input_schema:
dict output_schema: dict risk_level: Literal\[

``` text
"level_0",
"level_1",
"level_2",
"level_3",
"level_4",
]
```

required_permissions: list\[str\] approval_policy_key: str \| None
timeout_seconds: int idempotency_required: bool

## 83. Regla de Tool Schema

Los schemas deberán:

-   usar JSON Schema;

-   prohibir propiedades desconocidas cuando sea posible;

-   describir cada campo;

-   establecer límites;

-   marcar required;

-   incluir ejemplos;

-   evitar argumentos genéricos.

## 84. Tool input example

Tool:

create_support_ticket

Schema conceptual:

``` text
{
"type": "object",
"additionalProperties": false,
"properties": {
"title": {
"type": "string",
"minLength": 5,
"maxLength": 160
},
"description": {
"type": "string",
"minLength": 10,
"maxLength": 4000
},
"priority": {
"type": "string",
"enum": ["low", "normal", "high", "urgent"]
},
"customer_reference": {
"type": ["string", "null"],
"maxLength": 120
}
},
"required": [
"title",
"description",
"priority"
]
}
```

## 85. Tool Call Contract

``` text
class ModelToolCall(ContractModel):
```

tool_call_id: str tool_key: str tool_version: str arguments: dict

El modelo propone.

El sistema valida y autoriza.

## 86. Tool Execution Request

``` text
{
"tool_key": "create_support_ticket",
"tool_version": "1.0",
"arguments": {
"title": "Falla de impresión en cocina",
"description": "La impresora no responde desde esta mañana.",
"priority": "high",
"customer_reference": "REST-001"
},
"source_execution_id": "exec_123"
}
```

## 87. Tool Execution Response

``` text
{
"id": "tool_exec_123",
"tool_key": "create_support_ticket",
"tool_version": "1.0",
"status": "approval_required",
"risk_level": "level_2",
"requires_approval": true,
"approval_request_id": "approval_123",
"created_at": "2026-07-20T20:05:00Z"
}
```

## 88. Tool Result Contract

``` text
class ToolResultContract(ContractModel):
```

schema_version: str status: Literal\["succeeded", "failed", "partial"\]
data: dict \| None error: ErrorSummary \| None external_reference: str
\| None

## 89. Approval Request API

Endpoints:

``` text
GET /api/v1/approval-requests
GET /api/v1/approval-requests/{approval_id}
POST /api/v1/approval-requests/{approval_id}/decisions
```

## 90. Approval response

``` text
{
"id": "approval_123",
"status": "pending",
"risk_level": "level_2",
"summary": "Crear un ticket de soporte de prioridad alta.",
"subject": {
"type": "tool_execution",
"id": "tool_exec_123"
},
"requested_by": {
"type": "user",
"id": "usr_123"
},
"action_preview": {
"tool_key": "create_support_ticket",
"arguments": {
"title": "Falla de impresión en cocina",
"priority": "high"

}
},
"expires_at": "2026-07-20T20:20:00Z",
"created_at": "2026-07-20T20:05:00Z"
}
```

## 91. Approval decision

Request:

``` text
{
"decision": "approve",
"reason": "La información fue confirmada con el técnico."
}
```

Response:

``` text
{
"id": "approval_123",
"status": "approved",
"decided_by": "usr_456",
"decided_at": "2026-07-20T20:07:00Z"
}
```

## 92. Approval contract rules

La API no aceptará que el cliente envíe:

-   argument hash;
-   approver eligibility;
-   tool risk;
-   policy version;
-   tenant.

Estos valores serán resueltos por el servidor.

## 93. Knowledge API

Endpoints iniciales:

``` text
POST /api/v1/documents
GET /api/v1/documents
GET /api/v1/documents/{document_id}
POST /api/v1/documents/{document_id}/versions
GET /api/v1/documents/{document_id}/versions
POST /api/v1/document-versions/{version_id}/retry
POST /api/v1/knowledge/search
```

## 94. Document upload

Se utilizará multipart/form-data .

Campos:

file title classification document_type metadata

El archivo deberá validarse por contenido y no solo por extensión.

## 95. Upload response

Response 202 :

``` text
{
"document": {
"id": "doc_123",
"title": "Manual de instalación",
"status": "processing",
"classification": "internal"
},
"version": {

"id": "doc_ver_123",
"version_number": 1,
"status": "queued"
},
"ingestion_job": {
"id": "job_123",
"status": "pending"
}
}
```

## 96. Document response

``` text
{
"id": "doc_123",
"title": "Manual de instalación",
"document_type": "pdf",
"classification": "internal",
"status": "available",
"active_version": {
"id": "doc_ver_123",
"version_number": 1,
"status": "ready",
"created_at": "2026-07-20T18:00:00Z",
"processed_at": "2026-07-20T18:02:00Z"
},
"created_at": "2026-07-20T18:00:00Z",
"updated_at": "2026-07-20T18:02:00Z"
}
```

## 97. Ingestion Job Contract

``` text
class IngestionJobMessage(ContractModel):
```

schema_version: Literal\["1.0"\] job_id: str job_type:
Literal\["document_ingestion"\] tenant_id: str document_id: str
document_version_id: str execution_id: str

attempt: int requested_at: datetime

## 98. Job result

``` text
class IngestionJobResult(ContractModel):
```

schema_version: Literal\["1.0"\] job_id: str status:
Literal\["succeeded", "failed", "retry_scheduled"\] completed_stage: str
\| None chunks_created: int embeddings_created: int error: ErrorSummary
\| None

## 99. Job rules

Los jobs deberán:

-   incluir schema version;
-   incluir tenant;
-   incluir correlation o execution ID;
-   ser idempotentes;
-   validar payload;
-   registrar intento;
-   no confiar en datos sin verificar;
-   manejar mensajes duplicados.

## 100. Dead-letter contract

Cuando un job agote reintentos se registrará:

``` text
{
"job_id": "job_123",
"job_type": "document_ingestion",
"status": "dead_letter",
"attempts": 5,
"last_error": {
"code": "DOCUMENT_EXTRACTION_FAILED",

"retryable": false
}
}
```

## 101. Retrieval Search Contract

Request:

``` text
{
"query": "¿Qué pasos se siguen antes de instalar una red?",
"strategy": "hybrid",
"filters": {
"document_ids": [],
"document_types": ["pdf", "markdown"],
"classifications": ["internal"],
"tags": []
},
"limit": 10,
"include_debug": false
}
```

## 102. Retrieval response

``` text
{
"retrieval_run_id": "ret_123",
"query": "¿Qué pasos se siguen antes de instalar una red?",
"strategy": "hybrid",
"results": [
{
"rank": 1,
"score": 0.91,
"citation": {
"citation_key": "src_1",
"document_id": "doc_123",
"document_version_id": "doc_ver_123",
"title": "Manual de instalación",
"location": "Página 4",
"excerpt": "Antes de iniciar se debe realizar..."
}
}

],
"sufficiency": "sufficient"
}
```

## 103. Debug retrieval

La información detallada de scores, filtros internos y estrategias solo
estará disponible para usuarios autorizados en modo técnico.

No se expondrá por defecto.

## 104. Citation contract

Las citas visibles no deberán contener:

-   storage keys;
-   rutas físicas;
-   embeddings;
-   metadata restringida;
-   URLs permanentes sin autorización.

## 105. Memory API

Endpoints futuros:

``` text
GET /api/v1/memories
POST /api/v1/memories
PATCH /api/v1/memories/{memory_id}
DELETE /api/v1/memories/{memory_id}
POST /api/v1/memories/{memory_id}/confirm
POST /api/v1/memories/{memory_id}/reject
```

## 106. Memory response

``` text
{
"id": "memory_123",

"type": "user_preference",
"content": "Prefiere respuestas técnicas en español.",
"status": "confirmed",
"confidence": "verified",
"classification": "internal",
"source": {
"type": "user_confirmation",
"reference_id": "msg_123"
},
"created_at": "2026-07-20T20:00:00Z",
"expires_at": null
}
```

## 107. Audit API

Endpoints:

``` text
GET /api/v1/audit-events
GET /api/v1/audit-events/{audit_event_id}
```

Será de lectura y requerirá permisos elevados.

## 108. Audit response

``` text
{
"id": "audit_123",
"action": "tool.executed",
"actor": {
"type": "user",
"id": "usr_123"
},
"resource": {
"type": "tool_execution",
"id": "tool_exec_123"
},
"result": "success",
"correlation_id": "corr_123",
"execution_id": "exec_123",
"occurred_at": "2026-07-20T20:07:10Z"
}
```

## 109. Internal Commands

Los commands expresarán intención de cambio.

Ejemplo:

``` text
@dataclass(frozen=True)
class CreateConversationCommand:
```

actor: Actor title: str \| None language: str

## 110. Internal Queries

``` text
@dataclass(frozen=True)
class GetConversationQuery:
```

actor: Actor conversation_id: ConversationId

## 111. Command results

Los handlers podrán devolver DTOs de aplicación.

No deberán devolver directamente:

-   ORM models;
-   HTTP responses;
-   SDK objects;
-   provider responses.

## 112. Internal contract naming

Convenciones:

CreateConversationCommand CreateConversationResult GetConversationQuery
ConversationView DocumentUploadedEvent DocumentIngestionJob

## 113. Domain Event Contract

Los domain events podrán ser objetos internos.

Ejemplo:

``` text
@dataclass(frozen=True)
class ConversationCreated:
```

event_id: str tenant_id: str conversation_id: str owner_user_id: str
occurred_at: datetime

## 114. Integration Event Envelope

``` text
class IntegrationEventEnvelope(ContractModel):
```

event_id: str event_type: str event_version: int tenant_id: str
occurred_at: datetime correlation_id: str causation_id: str \| None
producer: str payload: dict

## 115. Event example

``` text
{
"event_id": "evt_123",
"event_type": "document.version.ready",
"event_version": 1,
"tenant_id": "ten_123",
"occurred_at": "2026-07-20T20:00:00Z",
"correlation_id": "corr_123",
"causation_id": "job_123",
"producer": "knowledge",
"payload": {
"document_id": "doc_123",
"document_version_id": "doc_ver_123",
"chunks_created": 84
}
}
```

## 116. Event naming

Los eventos externos usarán:

domain.entity.event

Ejemplos:

document.version.ready tool.execution.succeeded
approval.request.approved evaluation.run.completed

## 117. Event versioning

event_version representa la versión del schema del evento.

No representa la versión de la entidad.

## 118. Event compatibility

Los consumidores deberán:

-   ignorar campos desconocidos;
-   validar campos obligatorios;
-   rechazar versiones no soportadas;
-   ser idempotentes;
-   registrar eventos inválidos.

## 119. Causation and correlation

correlation_id Relaciona el flujo completo.

causation_id Indica qué evento, command o job causó el evento actual.

Esto permitirá reconstruir cadenas.

## 120. Webhook Contract

Los webhooks futuros utilizarán un envelope similar al de eventos.

Headers:

X-GEEM-Event-Id X-GEEM-Event-Type X-GEEM-Signature X-GEEM-Timestamp

## 121. Webhook security

Los webhooks deberán incluir:

-   firma;
-   timestamp;
-   prevención de replay;
-   retries;
-   idempotencia;
-   timeout;
-   allowlist cuando aplique.

## 122. Webhook response

El consumidor deberá responder rápidamente.

2xx

significa aceptado.

El procesamiento pesado deberá realizarse de forma asíncrona.

## 123. MCP Contract Principles

MCP expondrá capacidades existentes.

No creará lógica empresarial paralela.

Todo MCP tool o resource deberá mapear a:

-   query;
-   command;
-   application service;
-   Tool Registry.

## 124. MCP Resource URI

Ejemplos conceptuales:

geem://documents/{document_id} geem://conversations/{conversation_id}
geem://knowledge/search

Los URIs no conceden autorización por sí mismos.

## 125. MCP resource response

``` text
{
"uri": "geem://documents/doc_123",
"mimeType": "application/json",
"text": "{\"id\":\"doc_123\",\"title\":\"Manual de instalación\"}"
}
```

El contenido deberá estar sanitizado y autorizado.

## 126. MCP Tool Definition

Ejemplo conceptual:

``` text
{
"name": "search_knowledge",
"description": "Busca información autorizada en la base documental.",
"inputSchema": {
"type": "object",
"additionalProperties": false,
"properties": {
"query": {
"type": "string",
"minLength": 3,
"maxLength": 2000
}
},
"required": ["query"]
}
}
```

## 127. MCP tool execution

MCP no deberá evadir:

-   permisos;
-   tenant;
-   riesgo;
-   aprobación;
-   auditoría;
-   rate limit;
-   idempotencia.

## 128. MCP errors

Los errores deberán mapearse a respuestas MCP seguras.

No se enviarán stack traces ni detalles internos.

## 129. Contract Testing

Se realizarán:

-   schema tests;
-   OpenAPI validation;
-   provider contract tests;
-   consumer contract tests cuando aplique;
-   event schema tests;
-   tool schema tests;
-   compatibility tests;
-   MCP conformance tests.

## 130. API tests

Cada endpoint deberá probar:

-   success;

-   authentication;

-   authorization;

-   tenant isolation;

-   validation;

-   not found;

-   conflict;

-   idempotency;

-   error shape;

-   observability headers.

## 131. Schema snapshots

Los schemas públicos podrán almacenarse como artefactos de CI.

Los cambios deberán compararse para detectar incompatibilidades.

## 132. OpenAPI diff

El pipeline deberá evaluar cambios en OpenAPI.

Un cambio incompatible deberá:

-   fallar el quality gate;
-   requerir versión;
-   o tener aprobación explícita y plan de migración.

## 133. Event schema registry

Inicialmente podrá ser un directorio versionado:

contracts/events/

Ejemplo:

contracts/events/document-version-ready/v1.json

## 134. Tool schema registry

contracts/tools/

``` text
├── search-support-procedures/
│     └── v1.json
└── create-support-ticket/
└── v1.json
```

El Tool Registry de runtime podrá construirse a partir de estos
contratos.

## 135. Job schema registry

contracts/jobs/

``` text
└── document-ingestion/
├── request-v1.json
└── result-v1.json
```

## 136. Contract directory

Estructura inicial:

contracts/

``` text
├── openapi/
├── events/
├── jobs/
├── tools/
├── ai/
├── mcp/
└── examples/
```

No se duplicarán automáticamente schemas generados si no existe un
propósito claro.

## 137. Backward Compatibility Policy

Toda evolución deberá responder:

## 1. ¿Quién consume el contrato?

## 2. ¿Puede ignorar campos nuevos?

## 3. ¿Existe despliegue coordinado?

## 4. ¿Hay mensajes antiguos en cola?

## 5. ¿Hay tools o prompts antiguos?

## 6. ¿Puede hacerse migración progresiva?

## 138. Deprecation Policy

Un contrato deprecated deberá incluir:

-   fecha de deprecación;
-   reemplazo;
-   guía de migración;
-   fecha estimada de retiro;
-   métricas de uso.

## 139. Deprecation headers

La API podrá utilizar:

Deprecation: true Sunset: Wed, 31 Dec 2027 23:59:59 GMT Link:
`</api/v2/...>`{=html}; rel="successor-version"

## 140. Contract changelog

Los cambios públicos deberán registrarse.

Ejemplo:

Added optional field `confidence`. Deprecated `source_url`. No breaking
changes.

## 141. Security contracts

Los contratos sensibles deberán documentar:

-   permisos;
-   clasificación;
-   campos redactados;
-   campos no auditables;
-   riesgo;
-   autorización;
-   rate limit;
-   approval policy.

## 142. Sensitive fields

Los siguientes campos nunca deberán regresar de forma directa:

-   password hashes;
-   refresh tokens;
-   API keys;
-   internal storage paths;
-   provider credentials;
-   raw prompts privados;
-   secret tool arguments;
-   unrestricted signed URLs.

## 143. Signed URLs

Cuando se necesite acceso a un archivo:

-   se generará una URL temporal;
-   con alcance mínimo;
-   con expiración corta;
-   después de verificar autorización.

## 144. Rate limit headers

La API podrá responder:

RateLimit-Limit RateLimit-Remaining RateLimit-Reset Retry-After

## 145. Rate limit errors

``` text
{
"title": "Rate limit exceeded",
"status": 429,
"code": "RATE_LIMIT_EXCEEDED",
"detail": "Se alcanzó el límite temporal de solicitudes.",
"retryable": true
}
```

## 146. Observability headers

Las respuestas deberán incluir al menos:

X-Request-Id X-Correlation-Id

Los trace IDs podrán exponerse únicamente cuando sea seguro y útil.

## 147. Logging contracts

Los logs no son contratos de negocio, pero deberán usar nombres de
eventos estables.

Ejemplo:

``` text
{
"event": "assistant.execution.completed",
"execution_id": "exec_123",
"tenant_id": "ten_123",
"latency_ms": 4100,
"status": "completed"
}
```

## 148. Contract documentation

Cada contrato relevante deberá indicar:

-   propósito;
-   productor;
-   consumidor;
-   schema;
-   ejemplo;
-   errores;
-   permisos;
-   versionado;
-   observabilidad;
-   owner.

## 149. API endpoint checklist

Antes de implementar:

``` text
[ ] Resource identified
[ ] Use case defined
[ ] Method and path selected
[ ] Authentication defined
[ ] Permissions defined
[ ] Tenant resolution defined
[ ] Request schema defined
[ ] Response schema defined
[ ] Errors defined
[ ] Idempotency reviewed
[ ] Concurrency reviewed
[ ] Observability defined
[ ] OpenAPI examples prepared
```

## 150. Tool contract checklist

``` text
[ ] Business purpose defined
[ ] Tool key defined
[ ] Version defined
[ ] Input schema defined
[ ] Output schema defined
[ ] Additional properties forbidden
[ ] Risk classified
[ ] Permissions defined
[ ] Approval policy defined
[ ] Timeout defined
[ ] Retry policy defined
[ ] Idempotency defined
[ ] Audit fields defined
[ ] Evaluation cases defined
```

## 151. Event contract checklist

``` text
[ ] Event represents a fact
[ ] Name is stable
[ ] Schema version exists
[ ] Tenant included
[ ] Correlation included
[ ] Payload minimized
[ ] Sensitive fields excluded
[ ] Consumer idempotency defined
[ ] Compatibility reviewed
[ ] Failure handling defined
```

## 152. Job contract checklist

``` text
[ ] Job ID
[ ] Job type
[ ] Schema version
[ ] Tenant ID
[ ] Correlation ID

[ ] Attempt number
[ ] Idempotency
[ ] Retry classification
[ ] Dead-letter behavior
[ ] Result schema
[ ] Telemetry
```

## 153. AI contract checklist

``` text
[ ] Capability defined
[ ] Prompt version defined
[ ] Model policy defined
[ ] Output schema defined
[ ] Tool allowlist defined
[ ] Token budget defined
[ ] Timeout defined
[ ] Validation strategy defined
[ ] Repair strategy defined
[ ] Evaluation dataset defined
[ ] Cost tracking defined
```

## 154. API Definition of Done

Un endpoint estará terminado cuando:

-   OpenAPI está actualizado;
-   schemas están tipados;
-   permisos funcionan;
-   tenant isolation está probado;
-   errores cumplen contrato;
-   pruebas pasan;
-   frontend puede consumirlo;
-   observabilidad está presente;
-   ejemplos están documentados;
-   no existen breaking changes no declarados.

## 155. Contract Definition of Done

Un contrato estará terminado cuando:

-   tiene owner;
-   tiene versión;
-   tiene schema;
-   tiene ejemplos válidos;
-   tiene pruebas;
-   tiene política de compatibilidad;
-   tiene errores;
-   tiene documentación;
-   tiene consumidores identificados;
-   puede reproducirse.

## 156. Primer conjunto implementable

Para el primer vertical slice solo deberán implementarse estos
contratos:

HTTP

``` text
GET /api/v1/health/live
GET /api/v1/health/ready
POST /api/v1/conversations
GET /api/v1/conversations/{conversation_id}
POST /api/v1/conversations/{conversation_id}/messages
GET /api/v1/assistant-executions/{execution_id}
POST /api/v1/assistant-executions/{execution_id}/cancel
```

Internos

CreateConversationCommand SendConversationMessageCommand
CreateAssistantExecution CompleteAssistantExecution
FailAssistantExecution

AI

ModelExecutionRequest ModelExecutionResult AssistantStructuredResponse

Streaming

response.started response.delta response.completed response.failed

## 157. Contratos diferidos

No deberán implementarse todavía:

-   memory API;
-   MCP completo;
-   webhooks;
-   múltiples versiones públicas;
-   filtros complejos;
-   administración dinámica de prompts;
-   schemas de tools no utilizadas;
-   eventos sin consumidor.

## 158. Estructura inicial de código

src/geem_ai/

``` text
├── shared/
│    └── contracts/
│         ├── base.py
│         ├── errors.py
│         ├── pagination.py
│         └── money.py
├── conversations/
│    ├── application/
│    │    ├── commands.py
│    │    ├── queries.py

│   │   └── dto.py
│   └── presentation/
│       └── api/
│           ├── routes.py
│           └── schemas.py
└── ai_runtime/
├── application/
│   └── contracts.py
└── infrastructure/
└── providers/
```

## 159. Ejemplo completo de endpoint FastAPI

``` text
from typing import Annotated
from fastapi import APIRouter, Depends, status
```

router = APIRouter(prefix="/conversations", tags=\["conversations"\])

``` text
@router.post(
"",
```

response_model=ConversationResponse,
status_code=status.HTTP_201_CREATED, operation_id="create_conversation",
summary="Create a conversation", )

``` text
async def create_conversation(
```

request: CreateConversationRequest, actor: Annotated\[ActorContext,
Depends(get_actor_context)\], handler:
Annotated\[CreateConversationHandler, Depends()\], ) -\>
ConversationResponse: command = CreateConversationCommand(
actor=actor.to_domain_actor(), title=request.title,
language=request.language, )

result = await handler.handle(command)

``` text
return ConversationResponse.model_validate(result)
```

## 160. Ejemplo de manejo de error

``` text
class ConversationNotFoundError(DomainError):
```

code = "CONVERSATION_NOT_FOUND"

``` text
@app.exception_handler(ConversationNotFoundError)
async def handle_conversation_not_found(
```

request: Request, exc: ConversationNotFoundError, ) -\> JSONResponse:
problem = ProblemDetails(
type="https://errors.geem.example/conversation-not-found",
title="Conversation not found", status=404, detail="La conversación
solicitada no existe o no está disponible.", code=exc.code,
instance=str(request.url.path), request_id=request.state.request_id,
correlation_id=request.state.correlation_id, retryable=False,
errors=\[\], )

``` text
return JSONResponse(
```

status_code=problem.status, content=problem.model_dump(mode="json"), )

## 161. Ejemplo de contrato TypeScript generado

export interface ConversationResponse { id: string; title: string;
status: "active" \| "archived" \| "locked"; language: "es" \| "en";
created_at: string; updated_at: string;

``` text
}
```

Este tipo no deberá escribirse manualmente si puede generarse desde
OpenAPI.

## 162. Ejemplo de consumer frontend

export async function createConversation( input:
CreateConversationRequest, ): Promise`<ConversationResponse>`{=html} {
const response = await apiClient.post`<ConversationResponse>`{=html}(

``` text
"/api/v1/conversations",
```

input, );

``` text
return response.data;
}
```

## 163. Casos de contrato obligatorios en CI

El pipeline inicial deberá comprobar:

OpenAPI generates successfully OpenAPI schema is valid Frontend types
generate successfully No unapproved breaking changes Pydantic examples
validate Tool schemas validate Event schemas validate Structured
response fixtures validate

## 164. Anti-patterns

Generic Payload

``` text
{
"data": {}
}
```

sin schema definido.

Boolean Status

``` text
{
"success": true
}
```

como única respuesta.

HTTP 200 para todo Oculta errores y estados reales.

ORM Leakage Retornar modelos de persistencia directamente.

Provider Leakage Exponer respuestas nativas del proveedor.

Action by URL Guessing Crear rutas inconsistentes por cada operación.

Silent Contract Changes Modificar payloads sin versionado.

Tenant from User Input Confiar en un tenant enviado libremente.

Unbounded Metadata Aceptar diccionarios arbitrarios sin límites.

Tool Arguments as Text Ejecutar tools interpretando texto libre sin
schema.

## 165. Decisiones oficiales

Quedan aprobadas las siguientes decisiones:

## 1. Todo límite relevante tendrá contrato explícito.

## 2. Se seguirá Contract First.

## 3. REST será el estilo principal de API.

## 4. SSE será el protocolo inicial de streaming.

## 5. MCP reutilizará casos de uso internos.

## 6. La API pública utilizará /api/v1 .

## 7. Los recursos utilizarán sustantivos plurales.

## 8. Los campos JSON utilizarán snake_case.

## 9. Las fechas utilizarán ISO 8601 con zona.

## 10. El dinero utilizará decimal como string y moneda.

## 11. Los recursos utilizarán identificadores opacos.

## 12. La paginación por cursor será la opción principal.

## 13. Los errores seguirán un contrato extendido de RFC 7807.

## 14. Los códigos de error serán estables e independientes del idioma.

## 15. Se utilizarán request ID, correlation ID y execution ID.

## 16. Las operaciones sensibles usarán idempotency key.

## 17. La concurrencia optimista utilizará ETag e If-Match.

## 18. Los modelos HTTP serán independientes del dominio.

## 19. Pydantic será la fuente principal de schemas backend.

## 20. OpenAPI será la fuente de contratos HTTP.

## 21. Los tipos frontend deberán generarse desde OpenAPI.

## 22. Los SDKs de proveedores no cruzarán el Model Gateway.

## 23. Structured Outputs tendrán schema y versión.

## 24. Las tools tendrán input y output JSON Schema.

## 25. El modelo solo propondrá tool calls.

## 26. El sistema validará, autorizará y ejecutará tools.

## 27. Las approvals no aceptarán datos de seguridad calculados por el cliente.

## 28. Los jobs serán versionados e idempotentes.

## 29. Los eventos usarán envelope con tenant, correlation y versión.

## 30. Los consumidores de eventos deberán ser idempotentes.

## 31. Los webhooks futuros estarán firmados.

## 32. Los contratos MCP no evadirán permisos ni approvals.

## 33. Se ejecutarán contract tests en CI.

## 34. OpenAPI se analizará para detectar breaking changes.

## 35. Los contratos públicos tendrán política de deprecación.

## 36. No se implementarán contratos sin consumidor real.

## 37. No se utilizarán payloads genéricos sin esquema.

## 38. No se retornarán ORM models desde endpoints.

## 39. No se confiará en tenant enviado libremente.

## 40. El primer slice implementará únicamente los contratos necesarios para conversación y Model

Gateway.

## 166. Próximo documento

Documento 14 --- Project 1 Data Architecture Definirá de forma
implementable:

-   modelo relacional inicial;
-   tablas;
-   columnas;
-   claves;
-   constraints;
-   índices;
-   schemas PostgreSQL;
-   estrategia multi-tenant;
-   Row-Level Security;
-   pgvector;
-   full-text search;
-   migraciones;
-   transacciones;
-   locking;
-   outbox;
-   idempotencia;
-   retención;
-   backups;
-   anonimización;
-   fixtures;
-   datasets de evaluación;
-   ejemplos SQLAlchemy y Alembic.

## 167. Conclusión

GEEM AI Assistant tendrá contratos explícitos desde la interfaz hasta
los procesos internos, tools, workers, eventos y clientes MCP.

Esto permitirá que:

-   frontend y backend evolucionen de forma coordinada;
-   los proveedores AI puedan sustituirse;
-   las tools operen con seguridad;
-   los workers procesen mensajes confiables;
-   los errores sean consistentes;
-   los cambios incompatibles se detecten antes de llegar a producción.

A partir de este documento, los contratos dejan de ser una conversación
informal entre componentes.

Se convierten en activos de ingeniería versionados, probados y
gobernados.
