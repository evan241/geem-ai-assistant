# AI Engineering Lab

## Documento 12 --- Project 1 Domain Model

GEEM AI Assistant **Versión:** 1.0 **Estado:** Modelo de dominio oficial
**Responsable técnico:** Director de AI Engineering **Lead Engineer:**
Erick Eduardo Evangelista Velasco **Proyecto:** GEEM AI Assistant
**Estilo arquitectónico:** Domain-Oriented Modular Monolith

## 1. Propósito

Este documento define el modelo de dominio inicial de GEEM AI Assistant.

Su objetivo es establecer con precisión:

-   entidades;
-   agregados;
-   aggregate roots;
-   value objects;
-   invariantes;
-   estados;
-   ciclos de vida;
-   relaciones;
-   eventos de dominio;
-   políticas;
-   ownership de datos;
-   límites transaccionales;
-   reglas de autorización;
-   reglas multi-tenant.

Este documento será la referencia para implementar:

-   modelos de dominio;

-   casos de uso;

-   repositorios;

-   migraciones;

-   eventos;

-   pruebas;

-   contratos de aplicación.

## 2. Principio rector

El modelo de dominio representa reglas y capacidades del producto, no la
estructura accidental de la base de datos.

Las entidades no deberán diseñarse únicamente como tablas.

Cada agregado deberá proteger invariantes y controlar cambios dentro de
un límite transaccional claro.

## 3. Alcance inicial

El modelo cubrirá los siguientes dominios:

## 1. Identity

## 2. Organizations

## 3. Conversations

## 4. AI Runtime

## 5. Knowledge

## 6. Retrieval

## 7. Tools

## 8. Approvals

## 9. Memory

## 10. Audit

## 11. Evaluation

MCP, observabilidad e infraestructura consumirán estos dominios, pero no
definirán el núcleo de sus reglas.

## 4. Conceptos fundamentales

Entity Objeto con identidad persistente.

Value Object Objeto definido por sus atributos y reglas, sin identidad
propia.

Aggregate Conjunto de entidades y value objects tratados como unidad de
consistencia.

Aggregate Root Único punto autorizado para modificar el agregado.

Domain Event Hecho relevante ocurrido dentro del dominio.

Domain Policy Regla que puede involucrar varios conceptos, pero no
pertenece naturalmente a una sola entidad.

Application Service Coordina agregados, autorización, transacciones e
infraestructura.

## 5. Reglas globales del dominio

Todos los recursos empresariales deberán respetar:

-   aislamiento por tenant;
-   identidad opaca;
-   timestamps UTC;
-   cambios mediante aggregate roots;
-   autorización fuera y dentro del caso de uso;
-   auditoría en acciones críticas;
-   versionado cuando exista concurrencia relevante;
-   validación antes de persistencia.

## 6. Value Objects compartidos

El Shared Kernel podrá incluir:

UserId OrganizationId TenantId

MembershipId ConversationId MessageId ExecutionId DocumentId
DocumentVersionId ChunkId ToolId ToolVersionId ToolExecutionId
ApprovalRequestId MemoryId EvaluationRunId CorrelationId TraceId

## 7. TenantId

TenantId representa la frontera principal de aislamiento.

Invariantes:

-   no puede ser nulo;
-   no puede cambiar en un recurso existente;
-   debe coincidir con el contexto autorizado;
-   no se acepta libremente desde input no confiable;
-   debe acompañar consultas y comandos empresariales.

## 8. Actor

Value object que representa al responsable de una operación.

Actor

``` text
├── actor_id
├── actor_type
├── tenant_id
├── user_id
├── service_name
└── roles
```

Tipos:

user service system mcp_client worker

## 9. Permission

Value object que representa una capacidad autorizable.

Formato conceptual:

resource.action

Ejemplos:

documents.read documents.upload documents.delete conversations.create
tools.execute approvals.decide audit.read

## 10. RiskLevel

Value object utilizado por tools, approvals y políticas.

level_0 level_1 level_2 level_3 level_4

Interpretación:

Nivel Significado

0 Información pública

1 Lectura interna

2 Escritura reversible

3 Acción externa o impacto moderado

4 Acción crítica o difícilmente reversible

## 11. ConfidenceLevel

Value object para memoria, respuestas y clasificación.

low medium high verified

No deberá presentarse como probabilidad matemática salvo que exista una
métrica real.

## 12. DataClassification

public internal confidential restricted

Se utilizará en:

-   documentos;
-   memorias;
-   auditoría;
-   tools;
-   archivos;
-   outputs.

## 13. Domain Context: Identity

El dominio Identity gestiona identidad global y autenticación.

No administra permisos empresariales.

Los permisos pertenecen al contexto Organizations mediante memberships y
roles.

## 14. Aggregate: User

Aggregate Root

User

Responsabilidades - representar una identidad global; - controlar estado
de cuenta; - asociar proveedores de identidad; - registrar activación o
bloqueo; - proteger datos básicos de identidad.

## 15. User --- atributos

User

``` text
├── id
├── email
├── display_name
├── status
├── preferred_language
├── created_at
├── updated_at
└── version
```

## 16. UserStatus

pending active suspended disabled deleted

## 17. Invariantes de User

## 1. El email debe estar normalizado.

## 2. El email debe ser único según política de identidad.

## 3. Un usuario deshabilitado no puede iniciar sesión.

## 4. Un usuario eliminado no puede reactivarse directamente.

## 5. El cambio de email requiere verificación.

## 6. El estado no puede modificarse mediante asignación libre.

## 7. La identidad global no contiene roles de tenant.

## 18. Comportamientos de User

activate() suspend(reason) disable(reason) change_display_name(name)
request_email_change(email) confirm_email_change(token)

## 19. Eventos de User

UserRegistered UserActivated UserSuspended UserDisabled UserEmailChanged

## 20. Aggregate: Session

Una sesión podrá modelarse como agregado separado cuando se requiera
revocación persistente.

Atributos:

Session

``` text
├── id
├── user_id
├── status
├── created_at
├── expires_at
├── revoked_at
├── device_metadata
└── refresh_token_fingerprint
```

## 21. SessionStatus

active expired revoked

## 22. Invariantes de Session

-   una sesión expirada no puede renovarse sin política válida;
-   una sesión revocada no puede reactivarse;
-   no almacena refresh tokens en texto plano;
-   la expiración debe ser posterior a la creación;
-   la identidad debe seguir activa.

## 23. Domain Context: Organizations

Este dominio controla:

-   organizaciones;

-   tenants;

-   memberships;

-   roles;

-   permisos;

-   invitaciones.

## 24. Aggregate: Organization

Aggregate Root

Organization

Atributos

Organization

``` text
├── id
├── legal_name
├── display_name
├── status
├── default_tenant_id
├── created_at
├── updated_at
└── version
```

## 25. OrganizationStatus

active suspended closed

## 26. Invariantes de Organization

## 1. Toda organización debe tener nombre.

## 2. Debe existir al menos un tenant activo.

## 3. El tenant predeterminado debe pertenecer a la organización.

## 4. Una organización cerrada no acepta nuevos miembros.

## 5. Suspender organización bloquea operaciones empresariales.

## 6. Cerrar organización requiere política de retención y exportación.

## 27. Comportamientos de Organization

rename() suspend() reactivate() set_default_tenant() close()

## 28. Aggregate: Tenant

Un tenant se modelará como agregado independiente.

Atributos:

Tenant

``` text
├── id
├── organization_id
├── name
├── slug
├── status
├── settings
├── created_at
├── updated_at
└── version
```

## 29. TenantStatus

provisioning active suspended archived

## 30. Invariantes de Tenant

-   pertenece a una sola organización;
-   su organización no puede cambiar;
-   el slug debe ser único dentro de su ámbito;
-   un tenant suspendido no permite operaciones normales;
-   un tenant archivado es de solo lectura salvo procesos autorizados;
-   toda configuración debe validarse por esquema.

## 31. Eventos de Tenant

TenantProvisioned TenantActivated TenantSuspended TenantArchived
TenantSettingsChanged

## 32. Aggregate: Membership

Membership representa la relación entre usuario, organización y tenant.

Atributos:

Membership

``` text
├── id
├── user_id
├── organization_id
├── tenant_id
├── role_ids
├── status
├── joined_at
├── suspended_at
└── version
```

## 33. MembershipStatus

invited active suspended revoked

## 34. Invariantes de Membership

## 1. El tenant debe pertenecer a la organización.

## 2. El usuario debe existir y estar activo.

## 3. Los roles deben pertenecer al mismo tenant o catálogo permitido.

## 4. Una membership revocada no puede operar.

## 5. No debe quedar una organización sin owner activo.

## 6. Un usuario puede tener varias memberships.

## 7. Los permisos efectivos se derivan de roles, no se almacenan arbitrariamente en el usuario.

## 35. Comportamientos de Membership

activate() assign_role(role_id) remove_role(role_id) suspend() revoke()

## 36. Aggregate: Role

Atributos:

Role

``` text
├── id
├── tenant_id
├── name
├── key
├── permissions
├── is_system

├── status
└── version
```

## 37. Invariantes de Role

-   la clave debe ser única dentro del tenant;
-   los roles de sistema tienen restricciones de edición;
-   no puede asignarse un permiso desconocido;
-   un rol desactivado no puede asignarse;
-   el rol owner debe conservar permisos administrativos esenciales.

## 38. Política de autorización

La autorización efectiva será:

authenticated actor + active membership + active tenant + role
permissions + resource policy + domain invariant

Tener permiso general no garantiza acceso a todos los recursos.

## 39. Domain Context: Conversations

Este dominio representa interacción, mensajes y ejecuciones del
asistente.

## 40. Aggregate: Conversation

Aggregate Root

Conversation

Contenido interno - Message references; - conversation state; -
metadata; - ownership; - title.

Los mensajes podrán persistirse en tabla propia, pero conceptualmente
pertenecen al ciclo de la conversación.

## 41. Conversation --- atributos

Conversation

``` text
├── id
├── tenant_id
├── owner_user_id
├── title
├── status
├── language
├── created_at
├── updated_at
├── last_message_at
└── version
```

## 42. ConversationStatus

active archived locked deleted

## 43. Invariantes de Conversation

## 1. Pertenece a un solo tenant.

## 2. El owner debe tener membership válida al crearla.

## 3. No acepta mensajes cuando está archivada, bloqueada o eliminada.

## 4. Sus mensajes deben pertenecer al mismo tenant.

## 5. El idioma debe estar soportado.

## 6. El título puede generarse automáticamente.

## 7. Una conversación eliminada no puede reactivarse sin proceso especial.

## 8. El acceso de terceros depende de una política explícita.

## 44. Comportamientos de Conversation

add_user_message() add_assistant_message() rename() archive() restore()
lock() delete()

## 45. Entity: Message

Message

``` text
├── id
├── conversation_id
├── tenant_id
├── author_type
├── author_id
├── role
├── content
├── status
├── execution_id
├── created_at
└── metadata
```

## 46. MessageRole

user assistant system tool

El rol system no deberá utilizarse para exponer prompts internos al
usuario.

## 47. MessageStatus

pending streaming completed failed cancelled redacted

## 48. Invariantes de Message

-   pertenece a una conversación existente;
-   comparte tenant con la conversación;
-   no puede modificar contenido después de completarse salvo redacción
    auditada;
-   un mensaje de usuario no puede asociarse como resultado de tool;
-   un mensaje de tool debe estar ligado a una ejecución;
-   contenido vacío solo se permite en estados técnicos temporales
    controlados.

## 49. Aggregate: AssistantExecution

Una ejecución debe persistirse independientemente para permitir
trazabilidad.

AssistantExecution

``` text
├── id
├── tenant_id
├── conversation_id
├── user_message_id
├── assistant_message_id

├── status
├── capability
├── prompt_reference
├── model_selection
├── usage
├── cost
├── started_at
├── completed_at
├── failure
└── version
```

## 50. ExecutionStatus

created running waiting_for_approval completed failed cancelled
timed_out

## 51. ExecutionCapability

direct_response knowledge_query tool_request memory_operation workflow

## 52. Invariantes de AssistantExecution

## 1. Pertenece a una conversación y tenant.

## 2. Debe originarse en un mensaje de usuario o proceso autorizado.

## 3. Solo puede existir una ejecución activa por mensaje salvo retry explícito.

## 4. Una ejecución completada debe tener resultado o abstención.

## 5. Una ejecución fallida debe registrar categoría de error.

## 6. waiting_for_approval requiere solicitud de aprobación activa.

## 7. Costos y uso no pueden ser negativos.

## 8. El prompt y modelo usados deben quedar versionados.

## 53. State machine de AssistantExecution

created

``` text
│
▼
```

running

``` text
│
├── completed
├── failed
├── cancelled
├── timed_out
└── waiting_for_approval
│
├── running
├── cancelled
└── failed
```

## 54. Eventos de Conversation

ConversationCreated UserMessageAdded AssistantExecutionStarted
AssistantResponseCompleted AssistantExecutionFailed ConversationArchived
UserFeedbackSubmitted

## 55. Aggregate: UserFeedback

Podrá modelarse separado cuando requiera evaluación y análisis.

UserFeedback

``` text
├── id
├── tenant_id

├── execution_id
├── user_id
├── rating
├── category
├── comment
├── created_at
└── status
```

## 56. FeedbackCategory

helpful incorrect incomplete unsafe irrelevant citation_problem
tool_problem other

## 57. Domain Context: AI Runtime

AI Runtime coordina proveedores, prompts, outputs y uso.

La mayor parte de sus objetos serán contratos y value objects, no
agregados empresariales complejos.

## 58. Value Object: PromptReference

PromptReference

``` text
├── prompt_key
├── version
└── checksum
```

Invariantes:

-   la versión debe existir;

-   no puede cambiar durante una ejecución;

-   debe permitir reproducibilidad;

-   el checksum debe corresponder al contenido versionado.

## 59. Value Object: ModelSelection

ModelSelection

``` text
├── provider
├── model
├── capability
├── routing_policy_version
└── fallback_used
```

## 60. Value Object: TokenUsage

TokenUsage

``` text
├── input_tokens
├── output_tokens
├── cached_tokens
├── reasoning_tokens
└── total_tokens
```

Invariantes:

-   ningún valor es negativo;
-   total debe ser consistente;
-   campos no disponibles se representan como desconocidos, no
    inventados.

## 61. Value Object: ModelCost

ModelCost

``` text
├── amount
├── currency
├── pricing_version
└── estimated
```

## 62. Value Object: StructuredResponse

StructuredResponse

``` text
├── response_type
├── message
├── citations
├── actions
├── abstained
├── confidence
└── schema_version
```

## 63. ResponseType

direct_answer knowledge_answer clarification abstention tool_result
approval_request error

## 64. Invariantes de StructuredResponse

-   knowledge_answer requiere citas válidas;
-   abstention debe indicar falta o limitación;
-   approval_request debe relacionarse con una solicitud existente;
-   tool_result requiere ejecución de tool completada;
-   no puede contener acciones no autorizadas;
-   debe cumplir el schema versionado.

## 65. Domain Context: Knowledge

Este dominio administra el ciclo de vida documental y sus derivados.

## 66. Aggregate: Document

Aggregate Root

Document

Responsabilidades - identidad documental; - ownership; -
clasificación; - permisos; - versiones; - estado lógico; - ciclo de
vida.

## 67. Document --- atributos

Document

``` text
├── id
├── tenant_id
├── title
├── document_type
├── classification
├── owner_user_id
├── status
├── active_version_id
├── created_at
├── updated_at
└── version
```

## 68. DocumentStatus

draft processing available failed

archived deleted

## 69. DocumentType

Inicialmente:

pdf docx markdown text html

## 70. Invariantes de Document

## 1. Pertenece a un tenant inmutable.

## 2. Debe tener owner o responsable.

## 3. Solo una versión puede estar activa.

## 4. No puede marcarse disponible sin versión procesada.

## 5. Un documento eliminado no participa en retrieval.

## 6. Un documento archivado puede conservar historial, pero no necesariamente aparecer en búsqueda.

## 7. La clasificación restringe acceso.

## 8. Cambiar clasificación requiere autorización y auditoría.

## 9. Las versiones no se sobrescriben.

## 71. Entity: DocumentVersion

DocumentVersion

``` text
├── id
├── document_id
├── tenant_id
├── version_number
├── status
├── source_file
├── checksum
├── mime_type
├── size_bytes
├── extraction_metadata

├── created_by
├── created_at
└── processed_at
```

## 72. DocumentVersionStatus

uploaded validated queued extracting normalizing chunking embedding
indexing ready failed cancelled

## 73. Invariantes de DocumentVersion

-   número de versión único por documento;
-   checksum obligatorio;
-   una versión lista debe tener extracción completada;
-   no puede modificarse después de ready ;
-   una versión fallida puede reintentarse mediante nuevo intento, no
    reescribiendo historia;
-   todos sus derivados comparten tenant;
-   el archivo debe haber pasado validación.

## 74. Aggregate: IngestionJob

IngestionJob

``` text
├── id
├── tenant_id
├── document_id
├── document_version_id
├── status
├── current_stage
├── attempt

├── max_attempts
├── error
├── execution_id
├── created_at
├── started_at
└── completed_at
```

## 75. IngestionStage

validation storage extraction normalization chunking embedding indexing
completion

## 76. Invariantes de IngestionJob

## 1. Pertenece a una versión.

## 2. Solo un intento puede estar ejecutándose para la misma versión.

## 3. Los retries respetan max_attempts .

## 4. Un job completado no vuelve a ejecutarse.

## 5. El estado de la versión debe reflejar la etapa.

## 6. Cada fallo registra etapa y categoría.

## 7. La ejecución debe ser idempotente por versión e intento.

## 77. Entity: Chunk

Chunk

``` text
├── id
├── tenant_id
├── document_id
├── document_version_id
├── sequence
├── content
├── content_hash

├── token_count
├── location
├── metadata
└── status
```

## 78. Invariantes de Chunk

-   secuencia única por versión;
-   no pertenece a más de una versión;
-   debe conservar ubicación de origen;
-   no se indexa si el documento no está autorizado;
-   contenido vacío no es válido;
-   el hash permite deduplicación;
-   no debe exceder límites configurados sin estrategia de división.

## 79. Entity: EmbeddingRecord

EmbeddingRecord

``` text
├── id
├── tenant_id
├── chunk_id
├── provider
├── model
├── dimension
├── vector
├── embedding_version
├── created_at
└── status
```

## 80. Invariantes de EmbeddingRecord

-   la dimensión debe coincidir con el modelo;
-   un embedding pertenece a un chunk;
-   debe registrar modelo y versión;
-   no se mezclan índices incompatibles;
-   eliminar el chunk invalida o elimina el embedding;
-   una reindexación crea nuevo registro o versión controlada.

## 81. Aggregate: DocumentAccessPolicy

Los permisos documentales podrán modelarse como agregado independiente o
parte de Document según complejidad.

Conceptualmente:

DocumentAccessPolicy

``` text
├── document_id
├── tenant_id
├── visibility
├── allowed_role_ids
├── allowed_user_ids
├── denied_user_ids
└── version
```

## 82. DocumentVisibility

tenant restricted private

## 83. Política de acceso documental

El acceso será permitido solo si:

same tenant AND document active AND classification allowed AND
visibility policy satisfied AND actor has documents.read

Los deny explícitos tendrán prioridad.

## 84. Eventos de Knowledge

DocumentCreated DocumentVersionUploaded DocumentValidationPassed
DocumentProcessingRequested DocumentProcessingFailed
DocumentVersionReady DocumentActivated DocumentArchived DocumentDeleted
DocumentClassificationChanged

## 85. Domain Context: Retrieval

Retrieval representa una ejecución de búsqueda, no la propiedad del
conocimiento.

## 86. Aggregate: RetrievalRun

Se persistirá cuando sea necesario para evaluación, auditoría o
diagnóstico.

RetrievalRun

``` text
├── id
├── tenant_id
├── execution_id
├── query
├── strategy
├── filters
├── status
├── candidate_count
├── selected_count
├── context_token_count
├── started_at
├── completed_at
└── failure
```

## 87. RetrievalStrategy

vector full_text hybrid hybrid_reranked

## 88. Value Object: RetrievalQuery

RetrievalQuery

``` text
├── original_text
├── normalized_text
├── language
├── filters
├── top_k
└── query_hash
```

## 89. Entity: RetrievalCandidate

RetrievalCandidate

``` text
├── chunk_id
├── document_id
├── source_strategy
├── original_score
├── normalized_score
├── rank
└── authorized
```

Los candidatos no autorizados no deberán llegar al ensamblado de
contexto.

## 90. Value Object: Citation

Citation

``` text
├── document_id
├── document_version_id

├── chunk_id
├── title
├── location
├── excerpt
└── citation_key
```

## 91. Invariantes de Citation

-   referencia una fuente recuperada;
-   pertenece al tenant;
-   el actor tiene acceso;
-   la versión existe;
-   el fragmento corresponde al chunk;
-   no expone rutas internas o URLs permanentes inseguras.

## 92. Aggregate: ContextAssembly

Podrá ser objeto efímero.

ContextAssembly

``` text
├── retrieval_run_id
├── selected_citations
├── context_blocks
├── token_count
├── sufficiency
├── contradictions
└── truncation_applied
```

## 93. ContextSufficiency

insufficient partial sufficient conflicting

## 94. Política de abstención

Se deberá producir abstención si:

no authorized candidates OR context insufficient OR critical
contradiction unresolved OR citation validation failed OR requested data
unavailable

## 95. Eventos de Retrieval

RetrievalStarted RetrievalCompleted RetrievalReturnedNoEvidence
ContextAssembled CitationValidationFailed

## 96. Domain Context: Tools

Este dominio controla definición y ejecución de capacidades externas o
internas.

## 97. Aggregate: ToolDefinition

Aggregate Root

ToolDefinition

Atributos

ToolDefinition

``` text
├── id
├── tenant_scope
├── key
├── display_name
├── description
├── status
├── active_version_id
├── classification
├── created_at
└── version
```

## 98. ToolStatus

draft active disabled deprecated retired

## 99. Entity: ToolVersion

ToolVersion

``` text
├── id
├── tool_id
├── version_number
├── input_schema
├── output_schema
├── risk_level
├── required_permissions
├── approval_policy_key
├── timeout_seconds
├── retry_policy
├── idempotency_policy
├── adapter_key
└── status
```

## 100. Invariantes de ToolDefinition

## 1. La key es única en su ámbito.

## 2. Solo una versión puede estar activa.

## 3. No se ejecuta una tool deshabilitada.

## 4. Una versión publicada no se modifica.

## 5. Todo input y output debe tener schema.

## 6. Toda tool declara riesgo.

## 7. Toda tool declara permisos.

## 8. Toda tool con side effects declara idempotencia.

## 9. Toda tool de nivel alto declara política de aprobación.

## 10. El adapter no es accesible directamente por el modelo.

## 101. Aggregate: ToolExecution

ToolExecution

``` text
├── id
├── tenant_id
├── execution_id
├── tool_id
├── tool_version_id
├── requested_by
├── status
├── sanitized_arguments
├── arguments_hash
├── risk_level
├── approval_request_id
├── idempotency_key
├── result
├── failure
├── started_at
├── completed_at
└── version
```

## 102. ToolExecutionStatus

requested validating

authorization_denied approval_required approved running succeeded failed
timed_out cancelled duplicate_prevented

## 103. Invariantes de ToolExecution

-   tenant coincide con ejecución;
-   tool y versión existen;
-   argumentos cumplen schema;
-   actor tiene permisos;
-   risk level se toma de la versión;
-   una acción que requiere aprobación no puede pasar a running sin
    aprobación vinculada;
-   una idempotency key no puede ejecutar dos veces la misma acción;
-   resultados cumplen output schema;
-   argumentos sensibles no se almacenan sin protección;
-   tool desactivada no se ejecuta.

## 104. State machine de ToolExecution

requested

``` text
│
▼
```

validating

``` text
│
├── authorization_denied
├── failed
├── approval_required
│         │
│         ▼
│    approved
│         │
└───────┴─────► running
│
├── succeeded
├── failed

├── timed_out
└── cancelled
```

## 105. Entity: ToolExecutionAttempt

ToolExecutionAttempt

``` text
├── attempt_number
├── started_at
├── completed_at
├── status
├── retryable
├── error_code
└── provider_reference
```

## 106. Eventos de Tools

ToolExecutionRequested ToolAuthorizationDenied ToolApprovalRequired
ToolExecutionStarted ToolExecutionSucceeded ToolExecutionFailed
ToolExecutionTimedOut DuplicateToolExecutionPrevented

## 107. Domain Context: Approvals

Este dominio controla decisiones humanas sobre acciones.

## 108. Aggregate: ApprovalRequest

Aggregate Root

ApprovalRequest

Atributos

ApprovalRequest

``` text
├── id
├── tenant_id
├── subject_type
├── subject_id
├── requested_by
├── eligible_approvers
├── status
├── risk_level
├── summary
├── argument_hash
├── policy_version
├── created_at
├── expires_at
├── decided_at
├── executed_at
└── version
```

## 109. ApprovalStatus

pending approved rejected expired cancelled executed execution_failed

## 110. Aggregate: ApprovalDecision

La decisión puede ser entidad interna del ApprovalRequest.

ApprovalDecision

``` text
├── approver_id
├── decision
├── reason
├── decided_at
└── metadata
```

## 111. ApprovalDecisionType

approve reject

## 112. Invariantes de ApprovalRequest

## 1. El subject debe existir.

## 2. El tenant debe coincidir con el subject.

## 3. Solo un aprobador elegible puede decidir.

## 4. El solicitante no puede aprobar cuando la política lo prohíba.

## 5. Una solicitud expirada no puede aprobarse.

## 6. Solo puede decidirse una vez.

## 7. La aprobación debe vincular argumentos exactos.

## 8. Cambiar argumentos invalida la aprobación.

## 9. Aprobar no equivale a ejecutar.

## 10. La ejecución solo puede marcarse una vez.

## 11. Una solicitud rechazada no puede reutilizarse.

## 12. La policy version debe conservarse.

## 113. Comportamientos de ApprovalRequest

approve(actor, argument_hash) reject(actor, reason) expire(clock)

cancel(actor, reason) mark_executed() mark_execution_failed()

## 114. Eventos de Approvals

ApprovalRequested ApprovalGranted ApprovalRejected ApprovalExpired
ApprovalCancelled ApprovedActionExecuted ApprovedActionFailed

## 115. Domain Context: Memory

Memory administra información persistente utilizada para personalización
o continuidad.

## 116. Aggregate: Memory

Aggregate Root

Memory

Atributos

Memory

``` text
├── id
├── tenant_id
├── owner_user_id
├── type
├── content
├── status
├── confidence
├── source
├── classification

├── created_at
├── confirmed_at
├── expires_at
├── updated_at
└── version
```

## 117. MemoryType

user_preference working_context confirmed_fact

## 118. MemoryStatus

candidate confirmed active expired corrected deleted rejected

## 119. Invariantes de Memory

## 1. Pertenece a un tenant y usuario.

## 2. No puede contener secretos.

## 3. La memoria sensible requiere política explícita.

## 4. Un hecho debe registrar fuente.

## 5. Una memoria candidata no se utiliza como verdad confirmada.

## 6. Las correcciones crean revisión.

## 7. Una memoria expirada no participa en retrieval.

## 8. La eliminación debe impedir uso futuro.

## 9. No se comparte entre usuarios salvo un tipo organizacional futuro explícito.

## 10. El sistema no debe inferir atributos sensibles sin confirmación.

## 120. Entity: MemoryRevision

MemoryRevision

``` text
├── revision_number
├── previous_content
├── new_content
├── changed_by
├── reason
├── created_at
└── source
```

## 121. Comportamientos de Memory

confirm(actor) reject(actor) correct(content, actor, reason) expire()
delete(actor)

## 122. Eventos de Memory

MemoryCandidateCreated MemoryConfirmed MemoryRejected MemoryCorrected
MemoryExpired MemoryDeleted

## 123. Domain Context: Audit

Audit registra hechos relevantes con propósito de cumplimiento y
reconstrucción.

## 124. Aggregate: AuditEvent

Un evento de auditoría es inmutable después de crearse.

AuditEvent

``` text
├── id
├── tenant_id
├── actor
├── action
├── resource_type
├── resource_id
├── result
├── correlation_id
├── execution_id
├── sanitized_metadata
├── occurred_at
└── integrity_reference
```

## 125. AuditResult

success failure denied partial

## 126. Invariantes de AuditEvent

-   no se modifica;
-   registra actor y acción;
-   no contiene secretos;
-   conserva tenant;
-   usa timestamp confiable;
-   tiene correlation ID cuando aplica;
-   los eventos críticos no pueden omitirse por fallas silenciosas;
-   la persistencia de auditoría debe tener estrategia de resiliencia.

## 127. Acciones mínimas auditables

authentication.login authentication.failure membership.role_changed
document.uploaded document.accessed document.deleted tool.requested
tool.executed tool.denied approval.approved approval.rejected
memory.created memory.corrected configuration.changed export.created

## 128. Domain Context: Evaluation

Evaluation administra datasets, casos, ejecuciones y resultados.

## 129. Aggregate: EvaluationDataset

EvaluationDataset

``` text
├── id
├── key
├── version
├── purpose
├── status
├── language
├── case_count
├── created_at
├── published_at
└── checksum
```

## 130. DatasetStatus

draft validation published deprecated archived

## 131. Invariantes de EvaluationDataset

-   una versión publicada es inmutable;
-   debe tener propósito;
-   debe registrar origen de casos;
-   no debe contener datos no autorizados;
-   el checksum permite reproducibilidad;
-   un dataset deprecated puede seguir usándose para reproduccción
    histórica.

## 132. Entity: EvaluationCase

EvaluationCase

``` text
├── id
├── dataset_id
├── category
├── input
├── expected_behavior
├── reference_answer
├── reference_sources
├── tags
├── severity
└── metadata
```

## 133. Aggregate: EvaluationRun

EvaluationRun

``` text
├── id
├── dataset_reference

├── system_version
├── prompt_versions
├── model_configuration
├── status
├── started_at
├── completed_at
├── cost
├── summary
└── version
```

## 134. EvaluationRunStatus

created running completed failed cancelled

## 135. Entity: EvaluationResult

EvaluationResult

``` text
├── case_id
├── status
├── output
├── metric_values
├── evaluator_versions
├── failure_category
├── execution_id
└── review_status
```

## 136. Invariantes de EvaluationRun

-   referencia versiones exactas;

-   no modifica dataset;

-   resultados pertenecen al mismo run;

-   un run completado no acepta nuevos resultados;

-   debe registrar configuración;

-   los costos no pueden ser negativos;

-   fallos críticos deben identificarse;

-   los resultados deben permitir comparación con baseline.

## 137. Eventos de Evaluation

EvaluationDatasetPublished EvaluationRunStarted EvaluationCaseFailed
EvaluationRunCompleted EvaluationRegressionDetected BaselinePromoted

## 138. Agregados y límites transaccionales

Los principales límites serán:

Agregado Unidad transaccional

User cambios de identidad y estado

Organization estado y tenant predeterminado

Tenant configuración y ciclo de vida

Membership roles y estado de acceso

Conversation estado conversacional

AssistantExecution ciclo de ejecución

Document ciclo documental

IngestionJob procesamiento de una versión

ToolDefinition definición y versión activa

ToolExecution ciclo de ejecución de tool

ApprovalRequest decisión y binding

Memory ciclo y correcciones

EvaluationDataset publicación de dataset

EvaluationRun ejecución de evaluación

## 139. Transacciones entre agregados

Cuando un caso de uso involucre varios agregados:

-   se coordinará en Application Layer;
-   se utilizará Unit of Work;
-   se publicarán eventos después del commit;
-   se evitará introducir un agregado gigante;
-   las operaciones externas ocurrirán fuera de la transacción de base
    de datos.

## 140. Ejemplo: enviar mensaje

Agregados involucrados:

Conversation AssistantExecution

Flujo:

## 1. validar membership;

## 2. cargar conversación;

## 3. agregar mensaje de usuario;

## 4. crear AssistantExecution;

## 5. confirmar transacción;

## 6. ejecutar modelo;

## 7. persistir resultado;

## 8. agregar mensaje de asistente;

## 9. completar ejecución.

La llamada al modelo no deberá mantener una transacción de base de datos
abierta.

## 141. Ejemplo: cargar documento

Agregados involucrados:

Document DocumentVersion IngestionJob

Flujo:

## 1. validar permiso;

## 2. crear documento o nueva versión;

## 3. registrar archivo;

## 4. crear ingestion job;

## 5. confirmar;

## 6. publicar evento;

## 7. worker procesa;

## 8. actualizar estados;

## 9. activar versión cuando esté lista.

## 142. Ejemplo: tool con aprobación

Agregados involucrados:

AssistantExecution ToolExecution ApprovalRequest

Flujo:

## 1. crear ToolExecution;

## 2. validar y autorizar;

## 3. detectar aprobación requerida;

## 4. crear ApprovalRequest;

## 5. cambiar ejecución a espera;

## 6. confirmar;

## 7. usuario decide;

## 8. validar binding;

## 9. ejecutar tool;

## 10. actualizar ToolExecution;

## 11. actualizar ApprovalRequest;

## 12. reanudar AssistantExecution.

## 143. Reglas de concurrencia

Se utilizará optimistic concurrency donde exista riesgo de cambios
simultáneos.

Casos iniciales:

-   memberships;
-   roles;
-   documents;
-   approvals;
-   tool executions;
-   memories;
-   configuration.

## 144. Version field

Los agregados relevantes tendrán un campo:

version

Una actualización deberá comprobar la versión esperada.

Un conflicto deberá devolver un error controlado.

## 145. Idempotencia

Se requerirá en:

-   carga documental;
-   jobs;
-   webhooks;
-   tool executions;
-   aprobación y ejecución;
-   creación de recursos por requests repetidas.

## 146. IdempotencyKey

Value object:

IdempotencyKey

``` text
├── value
├── scope

├── tenant_id
└── expires_at
```

Una key debe ser única dentro de su scope.

## 147. Reglas de eliminación

La eliminación deberá diferenciar:

Logical Deactivation Impide uso, conserva historial.

Archival Retira de operación normal.

Soft Delete Oculta, conserva recuperabilidad.

Hard Delete Elimina datos y derivados.

Cada agregado definirá su política.

## 148. Eliminación de documento

Debe considerar:

Document DocumentVersions Files Chunks Embeddings Cache Retrieval
indexes

Signed URLs Derived artifacts

La auditoría conservará evidencia mínima permitida.

## 149. Eliminación de usuario

No deberá destruir necesariamente:

-   auditoría;
-   ejecuciones históricas;
-   acciones empresariales.

Podrá reemplazarse identidad visible por referencia anonimizada según
política.

## 150. Reglas multi-tenant de dominio

## 1. Todo agregado empresarial almacena tenant_id .

## 2. No se permiten relaciones cruzadas entre tenants.

## 3. Los repositorios requieren tenant context.

## 4. Los IDs por sí solos no autorizan acceso.

## 5. Los eventos conservan tenant.

## 6. Los jobs conservan tenant.

## 7. Las tools reciben tenant resuelto.

## 8. La memoria se filtra por tenant y usuario.

## 9. Retrieval filtra antes de devolver resultados.

## 10. Auditoría registra tenant.

## 151. Política de tenant mismatch

Cuando un recurso no coincida con el tenant autorizado:

-   no se revelará si existe;
-   se responderá como no encontrado o acceso denegado según política;
-   se generará telemetría de seguridad;
-   podrá generarse auditoría si el intento es relevante.

## 152. Reglas de autorización por agregado

Conversation - owner o permiso de lectura compartida; - misma
organización y tenant.

Document - documents.read ; - política de visibilidad; - clasificación
permitida.

ToolExecution - permiso requerido por tool; - política de riesgo; -
tenant válido.

ApprovalRequest - actor elegible; - permiso approvals.decide ; -
solicitud pendiente.

Memory - propietario o permiso administrativo específico.

## 153. Domain Services iniciales

Podrán existir:

AuthorizationPolicy TenantIsolationPolicy DocumentAccessPolicy
ApprovalEligibilityPolicy ToolRiskPolicy MemoryPersistencePolicy
RetrievalSufficiencyPolicy

CitationValidationPolicy CostBudgetPolicy

## 154. ApprovalEligibilityPolicy

Deberá evaluar:

-   permiso;
-   rol;
-   tenant;
-   riesgo;
-   alcance;
-   conflicto de interés;
-   límites de negocio;
-   política vigente.

## 155. ToolRiskPolicy

Deberá determinar:

-   ejecución directa;
-   aprobación requerida;
-   aprobación reforzada;
-   acción prohibida.

No dependerá únicamente de lo que declare el modelo.

## 156. MemoryPersistencePolicy

Evaluará:

-   tipo;
-   sensibilidad;
-   fuente;
-   confianza;
-   utilidad futura;
-   consentimiento o confirmación;
-   expiración.

Resultado:

reject temporary require_confirmation persist

## 157. RetrievalSufficiencyPolicy

Evaluará:

-   número de fuentes;
-   scores;
-   cobertura;
-   contradicciones;
-   autoridad;
-   relación con la pregunta.

No se delegará completamente al LLM.

## 158. Domain errors

Errores comunes:

InvariantViolation InvalidStateTransition TenantMismatch
ResourceNotAccessible PermissionDenied ConcurrencyConflict
ApprovalRequired ApprovalExpired ToolUnavailable DocumentNotReady
InsufficientEvidence BudgetExceeded

## 159. Regla sobre errores

Los errores de dominio deberán:

-   tener código estable;
-   no incluir datos sensibles;
-   ser traducibles;
-   mapearse a presentación;
-   distinguir condiciones esperadas de fallas técnicas.

## 160. Ownership de datos

Módulo Datos propios

Identity users, sessions, identity providers

Organizations organizations, tenants, memberships, roles

Conversations conversations, messages, executions, feedback

Knowledge documents, versions, chunks, embeddings

Retrieval retrieval runs y artefactos de búsqueda

Tools definitions, versions, executions

Approvals requests, decisions, policies

Memory memories, revisions

Audit audit events

Evaluation datasets, runs, results

## 161. Regla de acceso a datos ajenos

Un módulo no deberá consultar tablas de otro directamente.

Ejemplo:

Tools no deberá consultar memberships con SQL propio.

Deberá utilizar un contrato como:

AuthorizationService.can_execute_tool(...)

## 162. Contratos públicos iniciales

Organizations

ResolveTenantContext GetEffectivePermissions ValidateActiveMembership

Conversations

CreateConversation AddUserMessage CompleteAssistantExecution

Knowledge

GetAuthorizedDocument ListAuthorizedChunks CreateDocumentVersion

Tools

RequestToolExecution ExecuteApprovedTool

Approvals

CreateApprovalRequest DecideApproval ValidateApprovalBinding

## 163. Eventos como integración interna

Ejemplo:

DocumentVersionReady

Podrá ser consumido por:

-   Retrieval para actualizar disponibilidad;
-   Audit para registrar evento;
-   Evaluation para incluir casos;
-   Observability para métricas.

El evento no concede acceso directo a datos privados.

## 164. Event envelope

Formato conceptual:

``` text
{
"event_id": "evt-123",
"event_type": "DocumentVersionReady",
"event_version": 1,
"tenant_id": "tenant-123",
"occurred_at": "2026-01-01T00:00:00Z",
"correlation_id": "corr-123",
"payload": {}
}
```

## 165. Reglas de eventos

-   nombres en pasado;
-   representan hechos;
-   son inmutables;
-   incluyen versión;
-   no contienen secretos;
-   conservan tenant;
-   se publican después del commit;
-   los consumidores deben ser idempotentes.

## 166. Modelo inicial mínimo

El primer vertical slice solo requiere implementar:

User Organization Tenant Membership Conversation Message
AssistantExecution

Value objects:

TenantId UserId ConversationId ExecutionId PromptReference
ModelSelection TokenUsage ModelCost StructuredResponse

## 167. Segundo slice

Añadirá:

Role Permission Session AuditEvent

## 168. Tercer slice

Añadirá:

Document DocumentVersion IngestionJob Chunk EmbeddingRecord

## 169. Cuarto slice

Añadirá:

RetrievalRun RetrievalCandidate ContextAssembly Citation

## 170. Quinto slice

Añadirá:

ToolDefinition ToolVersion ToolExecution ToolExecutionAttempt

## 171. Sexto slice

Añadirá:

ApprovalRequest ApprovalDecision ApprovalPolicy

## 172. Séptimo slice

Añadirá:

Memory MemoryRevision MemorySource

## 173. Octavo slice

Añadirá:

EvaluationDataset EvaluationCase EvaluationRun EvaluationResult

## 174. Pruebas del dominio

Cada agregado deberá probar:

-   creación válida;
-   creación inválida;
-   transiciones;
-   invariantes;
-   eventos;
-   concurrencia;
-   tenant mismatch;
-   autorización cuando aplique;
-   idempotencia.

## 175. Pruebas de User

Ejemplos:

user_can_be_activated disabled_user_cannot_be_activated_directly
email_change_requires_confirmation

## 176. Pruebas de Conversation

active_conversation_accepts_message
archived_conversation_rejects_message
message_tenant_must_match_conversation
execution_cannot_complete_without_result

## 177. Pruebas de Document

document_cannot_be_available_without_ready_version
document_version_is_immutable_after_ready
deleted_document_is_not_retrievable classification_change_emits_event

## 178. Pruebas de ToolExecution

tool_requires_valid_schema unauthorized_actor_cannot_execute_tool
high_risk_tool_requires_approval approved_arguments_must_match_execution
idempotency_prevents_duplicate_action

## 179. Pruebas de ApprovalRequest

only_eligible_approver_can_decide expired_approval_cannot_be_approved

approval_cannot_be_reused argument_hash_mismatch_invalidates_approval

## 180. Pruebas de Memory

candidate_memory_is_not_used_as_confirmed_fact
expired_memory_is_not_retrieved memory_correction_creates_revision
secret_memory_is_rejected

## 181. Pruebas de tenant isolation

Como mínimo:

tenant_a_cannot_read_tenant_b_conversation
tenant_a_cannot_retrieve_tenant_b_chunk
tenant_a_cannot_approve_tenant_b_request
tenant_a_cannot_execute_tenant_b_tool
tenant_a_cannot_access_tenant_b_memory

Estas pruebas serán hard gates.

## 182. Mapeo a persistencia

Las entidades de dominio no deberán depender directamente de SQLAlchemy.

Se utilizarán:

-   persistence models;
-   mappers;
-   repositories.

Esto permitirá mantener el dominio independiente.

## 183. Mappers

Cada mapper deberá convertir:

Persistence Model ⇄ Domain Entity

Debe preservar:

-   identidad;
-   version;
-   estados;
-   value objects;
-   tenant;
-   eventos pendientes cuando corresponda.

## 184. Regla sobre entidades anémicas

No se aceptará un modelo donde toda regla viva en services y las
entidades solo almacenen datos.

Los aggregate roots deberán controlar sus transiciones.

## 185. Regla sobre agregados gigantes

Tampoco se crearán agregados que carguen colecciones ilimitadas.

Ejemplo:

Conversation no deberá cargar todos sus mensajes históricos para agregar
uno nuevo si no es necesario.

El modelo conceptual y la estrategia de persistencia deberán
equilibrarse.

## 186. Colecciones grandes

Para mensajes, chunks y resultados:

-   podrán ser entidades asociadas;

-   se manipularán mediante repositorios o servicios especializados;

-   las invariantes críticas permanecerán protegidas;

-   no se cargará toda la colección por defecto.

## 187. Modelo de consistencia

Consistencia fuerte Se requiere para:

-   autorización;
-   roles;
-   aprobaciones;
-   tool execution;
-   idempotencia;
-   estado de documentos;
-   activation de versión.

Consistencia eventual Es aceptable para:

-   métricas;
-   dashboards;
-   indexación secundaria;
-   notificaciones;
-   evaluaciones;
-   títulos automáticos.

## 188. Reglas temporales

Todo comportamiento dependiente del tiempo deberá usar un puerto:

Clock

No se llamará directamente al reloj del sistema dentro del dominio.

Esto facilita:

-   pruebas;

-   expiración;

-   reproducibilidad;

-   simulación.

## 189. Reglas monetarias

Los costos deberán utilizar un value object:

Money

``` text
├── amount
└── currency
```

No se utilizarán floats para operaciones monetarias críticas.

## 190. Reglas de idioma

El idioma se representará mediante:

LanguageCode

Inicialmente:

es en

El soporte principal será es .

## 191. Reglas de metadata

Los campos metadata :

-   deberán tener schema o límites;
-   no almacenarán lógica crítica;
-   no sustituirán columnas importantes;
-   no contendrán secretos;
-   tendrán tamaño controlado.

## 192. Reglas de estados

Los estados deberán representarse mediante enums explícitos.

No se utilizarán combinaciones ambiguas de múltiples booleanos como:

is_active is_deleted is_failed is_ready

cuando representen una sola máquina de estados.

## 193. Reglas de auditoría de cambios

Los cambios críticos deberán registrar:

-   actor;
-   estado anterior;
-   estado nuevo;
-   reason;
-   timestamp;
-   correlation ID.

## 194. Preguntas de entrevista que deberá poder

responder Erick - ¿Cómo definiste los aggregate roots? - ¿Por qué
ApprovalRequest es un agregado independiente? - ¿Cómo evitas que el LLM
ejecute tools sin autorización? - ¿Dónde se valida el tenant? - ¿Cómo
modelaste la aprobación ligada a argumentos? - ¿Por qué
AssistantExecution existe separado de Message? - ¿Cómo modelaste
versiones documentales? - ¿Qué datos son consistentes de forma
eventual? - ¿Cómo evitas agregados gigantes? - ¿Cómo se implementa
optimistic concurrency? - ¿Qué eventos de dominio utilizaste? - ¿Cómo
distingues logs de audit events?

## 195. Riesgos del modelo

D-001 --- Exceso de modelado temprano Mitigación:

-   implementar por slice;
-   no crear todas las entidades inmediatamente;
-   validar con casos de uso reales.

D-002 --- Entidades demasiado anémicas Mitigación:

-   transiciones en aggregate roots;
-   invariantes con pruebas.

D-003 --- Agregados demasiado grandes Mitigación:

-   separar ejecuciones;
-   paginar colecciones;
-   límites transaccionales pequeños.

D-004 --- Multi-tenancy solo en persistencia Mitigación:

-   TenantId dentro del dominio;
-   políticas y pruebas.

D-005 --- Estados inconsistentes entre módulos Mitigación:

-   eventos;
-   Unit of Work;
-   reconciliación;
-   observabilidad.

## 196. Criterios de aprobación del modelo

El modelo será aprobado si:

-   refleja casos de uso;
-   protege invariantes;
-   tiene límites claros;
-   soporta multi-tenancy;
-   controla tools y approvals;
-   permite trazabilidad;
-   evita acoplamiento a infraestructura;
-   puede implementarse por vertical slices;
-   puede probarse;
-   puede explicarse.

## 197. Decisiones oficiales

Quedan aprobadas las siguientes decisiones:

## 1. El modelo será orientado a agregados.

## 2. TenantId será parte explícita del dominio.

## 3. User será identidad global.

## 4. Membership representará acceso a organización y tenant.

## 5. Los permisos se derivarán de roles.

## 6. Conversation controlará su ciclo de vida.

## 7. AssistantExecution será independiente de Message.

## 8. Document será aggregate root del ciclo documental.

## 9. Las versiones documentales serán inmutables al estar listas.

## 10. IngestionJob controlará el procesamiento de una versión.

## 11. RetrievalRun representará búsquedas observables y evaluables.

## 12. Citation será un value object autorizado y verificable.

## 13. ToolDefinition y ToolExecution serán agregados independientes.

## 14. Toda tool tendrá versiones inmutables.

## 15. ToolExecution protegerá autorización, riesgo e idempotencia.

## 16. ApprovalRequest será un agregado independiente.

## 17. Las aprobaciones estarán ligadas a un hash de argumentos.

## 18. Aprobar y ejecutar serán estados diferentes.

## 19. Memory será aislada por tenant y usuario.

## 20. Las correcciones de memoria conservarán revisiones.

## 21. AuditEvent será inmutable.

## 22. EvaluationDataset será inmutable después de publicarse.

## 23. EvaluationRun registrará todas las versiones necesarias para reproducibilidad.

## 24. Las operaciones externas no mantendrán transacciones abiertas.

## 25. Se utilizará optimistic concurrency donde exista riesgo.

## 26. Los eventos se publicarán después del commit.

## 27. Los consumidores de eventos serán idempotentes.

## 28. Los módulos no accederán directamente a tablas ajenas.

## 29. La consistencia fuerte se reservará para controles críticos.

## 30. El modelo se implementará de forma incremental por vertical slices.

## 198. Próximo documento

Documento 13 --- Project 1 API and Contract Standards Definirá:

-   convenciones REST;
-   contratos de request y response;
-   versionado;
-   paginación;
-   filtros;
-   errores;
-   idempotencia;
-   streaming;
-   webhooks;
-   OpenAPI;
-   contratos internos;
-   eventos;
-   jobs;
-   tools;
-   MCP;
-   compatibilidad;
-   pruebas de contrato.

## 199. Conclusión

El modelo de dominio de GEEM AI Assistant queda definido alrededor de
límites claros de consistencia, seguridad y responsabilidad.

La arquitectura podrá ahora convertirse en código sin reducir el
producto a una colección de tablas o endpoints.

Cada agregado protegerá su propio ciclo de vida.

Cada módulo conservará ownership de sus datos.

Cada acción crítica deberá atravesar reglas explícitas.

Y cada componente AI operará dentro de un sistema empresarial gobernado,
trazable y verificable.
