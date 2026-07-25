# AI Engineering Lab

## Documento 15 --- Project 1 Application Architecture

GEEM AI Assistant **Versión:** 1.0 **Estado:** Arquitectura de
aplicación oficial **Responsable técnico:** Director de AI Engineering
**Lead Engineer:** Erick Eduardo Evangelista Velasco **Proyecto:** GEEM
AI Assistant **Backend:** Python + FastAPI Arquitectura: Modular
Monolith + DDD + Ports and Adapters Patrón de implementación: Vertical
Slices

## 1. Propósito

Este documento define la arquitectura de aplicación de GEEM AI
Assistant.

Su objetivo es establecer cómo se coordinarán:

-   casos de uso;
-   commands;
-   queries;
-   handlers;
-   entidades de dominio;
-   repositorios;
-   Unit of Work;
-   autorización;
-   idempotencia;
-   eventos;
-   procesos asíncronos;
-   proveedores de inteligencia artificial;
-   tools;
-   approvals;
-   observabilidad;
-   persistencia.

La capa de aplicación será responsable de convertir una intención
externa en una operación empresarial segura, consistente, trazable y
comprobable.

## 2. Principio rector

La capa de aplicación coordina el caso de uso, pero no reemplaza al
dominio ni contiene detalles de infraestructura.

La capa de aplicación decidirá:

-   qué caso de uso ejecutar;
-   qué agregado cargar;
-   qué políticas consultar;
-   cuándo iniciar o confirmar una transacción;
-   qué eventos publicar;
-   qué dependencias externas invocar;
-   qué resultado devolver.

No deberá contener:

-   SQL;
-   llamadas directas a SDKs;
-   lógica HTTP;
-   modelos ORM;
-   detalles de FastAPI;
-   reglas empresariales que pertenecen al dominio.

## 3. Responsabilidades por capa

Presentation Responsable de:

-   HTTP;
-   FastAPI;
-   autenticación de entrada;
-   parsing;
-   DTOs;
-   serialización;
-   códigos de estado;
-   headers;
-   SSE;
-   mapping de errores.

Application Responsable de:

-   casos de uso;
-   commands;
-   queries;
-   handlers;
-   autorización de aplicación;
-   coordinación;
-   transacciones;
-   idempotencia;
-   publicación de eventos;
-   orquestación.

Domain Responsable de:

-   entidades;
-   agregados;
-   value objects;
-   invariantes;
-   estados;
-   políticas de dominio;
-   eventos de dominio.

Infrastructure Responsable de:

-   PostgreSQL;
-   SQLAlchemy;
-   proveedores LLM;
-   Redis;
-   object storage;
-   email;
-   colas;
-   tracing;
-   adapters;
-   implementaciones de repositorios.

## 4. Regla de dependencias

Las dependencias deberán apuntar hacia el interior.

Presentation ↓ Application ↓ Domain

Infrastructure ↑ Ports defined by Application or Domain

El dominio no importará:

-   FastAPI;
-   SQLAlchemy;
-   OpenAI;
-   Anthropic;
-   Redis;
-   PostgreSQL;
-   boto3;
-   librerías de observabilidad.

## 5. Unidad principal: Use Case

Cada intención empresarial deberá representarse como un caso de uso
explícito.

Ejemplos:

CreateConversation SendConversationMessage ArchiveConversation
UploadDocument SearchKnowledge RequestToolExecution DecideApproval
ConfirmMemory

No se utilizarán services genéricos con decenas de métodos sin límites
claros.

## 6. Commands

Un command representa una intención de modificar el estado del sistema.

Ejemplos:

CreateConversationCommand SendConversationMessageCommand
ArchiveConversationCommand UploadDocumentCommand DecideApprovalCommand

Características:

-   expresa intención;
-   es inmutable;
-   contiene datos necesarios;
-   incluye actor;
-   no contiene lógica;
-   no depende de HTTP;
-   no contiene modelos ORM.

## 7. Queries

Una query representa una solicitud de información sin efectos
empresariales.

Ejemplos:

GetConversationQuery ListConversationsQuery GetAssistantExecutionQuery
ListApprovalRequestsQuery SearchAuditEventsQuery

Una query no deberá modificar agregados.

## 8. Command example

``` text
from dataclasses import dataclass

from geem_ai.shared.domain.actor import Actor
from geem_ai.shared.domain.ids import TenantId

@dataclass(frozen=True, slots=True)
class CreateConversationCommand:
```

actor: Actor title: str \| None language: str idempotency_key: str \|
None = None

## 9. Query example

``` text
from dataclasses import dataclass

from geem_ai.shared.domain.actor import Actor
from geem_ai.conversations.domain.ids import ConversationId

@dataclass(frozen=True, slots=True)
class GetConversationQuery:
```

actor: Actor conversation_id: ConversationId

## 10. Handlers

Cada command o query tendrá un handler principal.

Convención:

CreateConversationHandler GetConversationHandler
SendConversationMessageHandler

El handler:

## 1. valida contexto;

## 2. consulta autorización;

## 3. abre Unit of Work;

## 4. carga o crea agregados;

## 5. invoca comportamiento de dominio;

## 6. persiste;

## 7. registra eventos;

## 8. confirma;

## 9. devuelve un resultado.

## 11. Un handler por caso de uso

No se utilizará un único handler genérico para todos los commands.

La regla general será:

``` text
1 command → 1 primary handler
1 query → 1 primary handler
```

Podrán existir decoradores y pipelines compartidos.

## 12. Command result

Los handlers devolverán resultados explícitos.

Ejemplo:

``` text
from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True, slots=True)
class CreateConversationResult:
```

conversation_id: str title: str status: str language: str

created_at: datetime version: int

No devolverán:

-   Response de FastAPI;
-   modelos ORM;
-   sesiones SQLAlchemy;
-   objetos nativos del proveedor LLM.

## 13. Application DTOs

Los DTOs de aplicación podrán representar vistas o resultados.

Ejemplos:

ConversationView MessageView AssistantExecutionView DocumentView
ApprovalRequestView

Los DTOs no deberán adquirir lógica empresarial.

## 14. Separación entre DTOs

Se distinguirán:

HTTP Request DTO Application Command Domain Entity Persistence Model
Application Result HTTP Response DTO

No se reutilizará un mismo objeto para todas las capas.

## 15. Flujo de un command

HTTP Request ↓ Request Schema ↓ Command ↓ Command Handler ↓
Authorization ↓ Unit of Work ↓ Domain Aggregate ↓ Repository ↓ Commit ↓
Application Result ↓ HTTP Response

## 16. Flujo de una query

HTTP Request ↓ Query Schema ↓ Application Query ↓ Query Handler ↓
Authorization ↓ Read Model / Repository ↓ Application View ↓ HTTP
Response

## 17. CQRS pragmático

El proyecto utilizará separación conceptual entre commands y queries.

No se implementará inicialmente:

-   bases de datos separadas;
-   buses complejos;
-   proyecciones distribuidas;
-   event sourcing completo.

La separación servirá para:

-   claridad;
-   permisos;
-   optimización;
-   pruebas;
-   evolución.

## 18. Repositories

Los repositorios representan colecciones de agregados.

Ejemplos:

ConversationRepository DocumentRepository MembershipRepository
ToolExecutionRepository ApprovalRequestRepository

No se crearán repositorios genéricos universales.

## 19. Repository interface

``` text
from typing import Protocol

from geem_ai.conversations.domain.conversation import Conversation
from geem_ai.conversations.domain.ids import ConversationId

from geem_ai.shared.domain.ids import TenantId

class ConversationRepository(Protocol):
async def add(self, conversation: Conversation) -> None:
```

...

``` text
async def get_by_id(
```

self, tenant_id: TenantId, conversation_id: ConversationId, ) -\>
Conversation \| None: ...

``` text
async def exists(
```

self, tenant_id: TenantId, conversation_id: ConversationId, ) -\> bool:
...

## 20. Repositories tenant-aware

Todo repositorio empresarial deberá recibir o conservar TenantId.

No se aceptará:

get_by_id(conversation_id)

cuando el recurso sea multi-tenant.

Se requerirá:

get_by_id(tenant_id, conversation_id)

aunque RLS esté habilitado.

## 21. Queries optimizadas

Las queries de lectura podrán utilizar read repositories específicos.

Ejemplo:

``` text
class ConversationReadRepository(Protocol):
async def get_view(
```

self, tenant_id: TenantId, conversation_id: ConversationId, ) -\>
ConversationView \| None: ...

``` text
async def list_for_user(
```

self, tenant_id: TenantId, user_id: UserId, cursor: ConversationCursor
\| None, limit: int, ) -\> ConversationPage: ...

No será obligatorio reconstruir un agregado para una consulta de solo
lectura.

## 22. Unit of Work

Unit of Work delimita la transacción de un caso de uso.

Responsabilidades:

-   abrir sesión;
-   establecer tenant context;
-   exponer repositorios;
-   commit;
-   rollback;
-   recopilar eventos;
-   cerrar recursos.

## 23. Unit of Work interface

``` text
from typing import Protocol, Self

class UnitOfWork(Protocol):
```

conversations: ConversationRepository memberships: MembershipRepository
executions: AssistantExecutionRepository audit_events:
AuditEventRepository outbox: OutboxRepository

``` text
async def __aenter__(self) -> Self:
```

...

``` text
async def __aexit__(
```

self, exc_type, exc, traceback, ) -\> None: ...

``` text
async def commit(self) -> None:
```

...

``` text
async def rollback(self) -> None:
```

...

## 24. Tenant-aware Unit of Work

La factoría deberá recibir contexto resuelto:

uow_factory.create( tenant_id=actor.tenant_id, user_id=actor.user_id, )

El Unit of Work configurará:

-   app.tenant_id ;
-   app.user_id ;
-   transaction timeout;
-   correlation context.

## 25. Regla de commit

El commit deberá ser explícito.

No se confirmará automáticamente al salir del context manager.

Ejemplo:

``` text
async with self._uow_factory.create(actor) as uow:
```

...

``` text
await uow.commit()
```

Si el handler termina sin commit, el Unit of Work hará rollback.

## 26. Regla de transacción corta

Una transacción no deberá envolver:

-   llamada a LLM;
-   embeddings;
-   tool externa;
-   object storage;
-   webhook;
-   email;
-   espera de aprobación;
-   streaming completo.

Estas operaciones se dividirán en etapas.

## 27. Transaction Script vs Domain Model

Los casos de uso simples podrán tener handlers pequeños.

Sin embargo, las transiciones y reglas críticas deberán ejecutarse
mediante agregados.

Ejemplo incorrecto:

model.status = "archived"

Ejemplo correcto:

conversation.archive(actor, clock.now())

## 28. Application Services

Se utilizarán para coordinación reusable que no pertenece a un solo
handler.

Ejemplos:

AuthorizationService IdempotencyService AssistantExecutionOrchestrator
DocumentIngestionCoordinator ToolExecutionCoordinator
ApprovalCoordinator

No deberán convertirse en contenedores de lógica indiscriminada.

## 29. Domain Services

Los domain services se utilizarán cuando una regla:

-   pertenece al dominio;
-   involucra más de una entidad;
-   no encaja naturalmente en un agregado;
-   no depende de infraestructura.

Ejemplos:

ToolRiskPolicy ApprovalEligibilityPolicy RetrievalSufficiencyPolicy
MemoryPersistencePolicy

## 30. Application vs Domain policy

Application Policy Evalúa contexto del caso de uso.

Ejemplo:

¿Tiene este actor permiso para invocar el caso de uso?

Domain Policy Evalúa una regla del negocio.

Ejemplo:

¿Esta tool requiere aprobación por su riesgo y contexto?

## 31. Authorization pipeline

Toda operación protegida seguirá:

Authentication ↓ Active tenant context ↓ Active membership ↓ Permission
check ↓ Resource access policy ↓ Domain invariant

## 32. AuthorizationService

Contrato conceptual:

``` text
class AuthorizationService(Protocol):
async def require_permission(
```

self, actor: Actor, permission: Permission, ) -\> None: ...

``` text
async def can_access_resource(
```

self, actor: Actor, resource: ResourceReference, action: str, ) -\>
bool: ...

## 33. Deny by default

Toda capacidad estará prohibida salvo que exista una autorización
explícita.

No se inferirán permisos a partir de:

-   interfaz visible;
-   nombre del endpoint;
-   rol enviado por el cliente;
-   tenant enviado por header arbitrario;
-   tool sugerida por el modelo.

## 34. Resource-level authorization

Tener documents.read no implica poder leer cualquier documento.

El handler deberá consultar:

permission + tenant + classification + visibility

-   allow/deny policy

## 35. Actor Context

El contexto de actor se resolverá una vez por request.

``` text
@dataclass(frozen=True, slots=True)
class ActorContext:
```

actor_id: str actor_type: str user_id: str \| None tenant_id: str
organization_id: str membership_id: str \| None roles: frozenset\[str\]
permissions: frozenset\[str\] correlation_id: str request_id: str

Los handlers recibirán un Actor de dominio o aplicación derivado de este
contexto.

## 36. No confiar en el command

El command podrá contener actor, pero ese actor deberá provenir del
contexto autenticado.

Nunca se construirá a partir de JSON enviado por el cliente.

## 37. Idempotency pipeline

Las operaciones compatibles con idempotencia seguirán:

## 1. validar key;

## 2. calcular request hash;

## 3. buscar registro;

## 4. detectar replay o conflicto;

## 5. registrar procesamiento;

## 6. ejecutar handler;

## 7. guardar resultado seguro;

## 8. marcar completado.

## 38. Idempotency decorator

Podrá implementarse como decorador de handler.

``` text
class IdempotentCommandHandler:
def __init__(
```

self, inner, idempotency_service, ): self.\_inner = inner
self.\_idempotency = idempotency_service

``` text
async def handle(self, command):
return await self._idempotency.execute(
```

scope=type(command).\_\_name\_\_, key=command.idempotency_key,
payload=command, operation=lambda: self.\_inner.handle(command), )

La implementación real deberá evitar serializar secretos.

## 39. Commands sin idempotency key

No todos los commands la requieren.

Ejemplos que sí la requieren:

-   upload de documento;
-   creación de ticket;
-   ejecución de tool;
-   recepción de webhook;
-   comandos iniciados por sistemas externos.

Crear conversación podrá aceptarla, aunque no sea obligatoria en el
primer slice.

## 40. Validation pipeline

La validación ocurrirá en varios niveles.

Presentation validation - formato; - campos; - límites; - tipos.

Application validation - contexto; - existencia; - permisos; -
combinación de datos.

Domain validation - invariantes; - estados; - transiciones.

Infrastructure validation - constraints; - integridad física; -
proveedor.

## 41. No duplicar mensajes de error internos

Cada capa podrá detectar errores distintos.

No se intentará reutilizar mensajes de Pydantic como errores de dominio.

Los errores se mapearán a códigos estables.

## 42. Error hierarchy

``` text
class ApplicationError(Exception):
```

code: str retryable: bool = False

``` text
class NotFoundError(ApplicationError):
```

pass

``` text
class PermissionDeniedError(ApplicationError):
```

pass

``` text
class ConflictError(ApplicationError):
```

pass

``` text
class PreconditionFailedError(ApplicationError):
```

pass

``` text
class DependencyUnavailableError(ApplicationError):
```

retryable = True

## 43. Errores de dominio

Los errores de dominio deberán conservar su significado.

Ejemplos:

ConversationAlreadyArchived InvalidExecutionTransition ApprovalExpired
ToolExecutionAlreadyStarted InsufficientEvidence

Presentation los mapeará al contrato HTTP.

## 44. Exception mapping

La capa Presentation tendrá un registro centralizado.

Domain/Application Error ↓ Problem Details ↓ HTTP Status

Los handlers no devolverán códigos HTTP.

## 45. Event collection

Los agregados podrán acumular eventos pendientes.

``` text
class AggregateRoot:
def __init__(self) -> None:
```

self.\_domain_events: list\[DomainEvent\] = \[\]

``` text
def record_event(self, event: DomainEvent) -> None:
```

self.\_domain_events.append(event)

``` text
def pull_events(self) -> list[DomainEvent]:
```

events = self.\_domain_events.copy() self.\_domain_events.clear()

``` text
return events
```

## 46. Domain event flow

Aggregate changes ↓ Domain event recorded ↓ Repository persists
aggregate ↓ Unit of Work collects events ↓ Outbox records integration
events

↓ Commit ↓ Dispatcher handles post-commit work

## 47. Domain events vs integration events

Domain Event Uso interno al dominio o módulo.

Ejemplo:

ConversationCreated

Integration Event Contrato estable para otros módulos o workers.

Ejemplo:

conversation.created.v1

No todos los domain events deberán convertirse en integration events.

## 48. Event handlers

Un domain event podrá tener handlers internos.

Ejemplo:

ConversationCreated

``` text
├── CreateAuditRecord
└── ScheduleTitleGeneration
```

Las acciones críticas que deben ser atómicas se ejecutarán dentro de la
transacción.

Las acciones asíncronas se enviarán mediante outbox.

## 49. Post-commit execution

No se enviarán mensajes externos antes del commit.

Incorrecto:

send event commit database

Correcto:

write aggregate write outbox commit publish asynchronously

## 50. Command Bus

El primer slice podrá invocar handlers directamente mediante dependency
injection.

No es obligatorio implementar un bus desde el primer día.

Podrá incorporarse un Command Bus ligero cuando permita:

-   decoradores;
-   logging;
-   métricas;
-   validación;
-   autorización;
-   idempotencia.

## 51. Query Bus

Se aplicará la misma regla.

No se incorporará una librería compleja solo para simular arquitectura
empresarial.

## 52. Handler decorators

Podrán utilizarse decoradores para capacidades transversales:

Logging Tracing Metrics Authorization Validation Idempotency Transaction
Retry

El orden deberá ser explícito.

## 53. Pipeline recomendado para commands

Tracing ↓ Logging ↓ Authentication Context ↓ Authorization ↓ Validation
↓ Idempotency ↓ Transaction ↓ Handler ↓ Metrics

No todas las responsabilidades deberán implementarse como decorador.

## 54. Pipeline recomendado para queries

Tracing ↓ Logging ↓ Authentication Context ↓ Authorization ↓ Validation
↓ Query Handler ↓ Metrics

## 55. Retry policy

Los handlers no reintentarán indiscriminadamente.

Se podrán reintentar:

-   errores temporales;
-   deadlocks;
-   serialización;
-   proveedor no disponible;
-   timeouts controlados;
-   operaciones idempotentes.

No se reintentarán automáticamente:

-   permisos;
-   validación;
-   conflictos empresariales;
-   tools sin idempotencia;
-   aprobación rechazada.

## 56. Retry location

Los retries se ubicarán cerca de la dependencia que falla.

Ejemplos:

-   adapter LLM;
-   publisher outbox;
-   worker;
-   tool adapter.

No se reejecutará todo el handler si eso puede duplicar efectos.

## 57. Dependency Injection

Se utilizará inyección explícita.

FastAPI podrá resolver dependencias en Presentation, pero los handlers
no dependerán de Depends .

Ejemplo:

``` text
class CreateConversationHandler:
def __init__(
```

self, uow_factory: UnitOfWorkFactory, authorization:
AuthorizationService, clock: Clock, id_generator: IdGenerator, ) -\>
None: ...

## 58. Composition Root

La construcción del sistema ocurrirá en un punto central.

bootstrap/

``` text
├── container.py
├── providers.py
├── repositories.py
├── handlers.py
└── routes.py
```

El composition root conectará interfaces con implementaciones.

## 59. No Service Locator

Los handlers no consultarán un contenedor global.

Incorrecto:

container.resolve("conversation_repository")

Correcto:

CreateConversationHandler( uow_factory=uow_factory,
authorization=authorization, )

## 60. Clock port

``` text
from datetime import datetime
from typing import Protocol

class Clock(Protocol):
def now(self) -> datetime:
```

...

Infraestructura:

``` text
class SystemClock:
def now(self) -> datetime:
return datetime.now(timezone.utc)
```

## 61. ID generator port

``` text
class IdGenerator(Protocol):
def new_uuid(self) -> UUID:
```

...

Esto permite pruebas deterministas.

## 62. Transaction boundary

La transacción normalmente pertenecerá al handler de command.

Las queries podrán usar:

-   sesión read-only;
-   transacción corta;
-   conexión dedicada.

## 63. No nested Unit of Work

Un handler no deberá abrir Unit of Work anidados sin razón explícita.

Los application services recibirán el Unit of Work actual cuando deban
participar en la misma transacción.

## 64. Caso de uso: CreateConversation

Responsabilidades:

## 1. requerir conversations.create ;

## 2. validar tenant activo;

## 3. normalizar título;

## 4. crear agregado;

## 5. persistir;

## 6. registrar evento;

## 7. crear auditoría;

## 8. commit;

## 9. devolver resultado.

## 65. CreateConversation command

``` text
@dataclass(frozen=True, slots=True)
class CreateConversationCommand:
```

actor: Actor title: str \| None language: LanguageCode idempotency_key:
str \| None = None

## 66. CreateConversation handler

``` text
class CreateConversationHandler:
def __init__(
```

self, uow_factory: UnitOfWorkFactory, authorization:
AuthorizationService, id_generator: IdGenerator, clock: Clock, ) -\>
None: self.\_uow_factory = uow_factory self.\_authorization =
authorization self.\_id_generator = id_generator self.\_clock = clock

``` text
async def handle(
```

self, command: CreateConversationCommand, ) -\>
CreateConversationResult:

``` text
await self._authorization.require_permission(
```

command.actor, Permission("conversations.create"), )

conversation = Conversation.create( conversation_id=ConversationId(
self.\_id_generator.new_uuid() ), tenant_id=command.actor.tenant_id,
owner_user_id=command.actor.user_id, title=command.title,
language=command.language, created_at=self.\_clock.now(),

)

``` text
async with self._uow_factory.create(
```

command.actor ) as uow:

``` text
await uow.conversations.add(conversation)
await uow.commit()

return CreateConversationResult.from_domain(
```

conversation )

La auditoría y outbox podrán incorporarse dentro del Unit of Work
mediante eventos.

## 67. Conversation.create

Ejemplo conceptual:

``` text
@classmethod
def create(
```

cls, conversation_id, tenant_id, owner_user_id, title, language,
created_at, ): normalized_title = normalize_title( title or "Nueva
conversación" )

conversation = cls( id=conversation_id, tenant_id=tenant_id,
owner_user_id=owner_user_id, title=normalized_title,
status=ConversationStatus.ACTIVE, language=language,
created_at=created_at, updated_at=created_at, version=1, )

conversation.record_event( ConversationCreated(
conversation_id=conversation.id, tenant_id=conversation.tenant_id,
owner_user_id=conversation.owner_user_id, occurred_at=created_at, ) )

``` text
return conversation
```

## 68. Caso de uso: GetConversation

Responsabilidades:

## 1. requerir permiso;

## 2. consultar vista;

## 3. ocultar existencia de otros tenants;

## 4. devolver DTO.

## 69. GetConversation handler

``` text
class GetConversationHandler:
def __init__(
```

self, repository: ConversationReadRepository, authorization:
AuthorizationService, ) -\> None: self.\_repository = repository
self.\_authorization = authorization

``` text
async def handle(
```

self, query: GetConversationQuery, ) -\> ConversationView:

``` text
await self._authorization.require_permission(
```

query.actor, Permission("conversations.read"), )

conversation = await self.\_repository.get_view(
tenant_id=query.actor.tenant_id,

conversation_id=query.conversation_id, )

if conversation is None:

``` text
raise ConversationNotFoundError()
```

if not await self.\_authorization.can_access_resource( query.actor,
ResourceReference( type="conversation", id=query.conversation_id.value,
owner_user_id=conversation.owner_user_id, ),

``` text
"read",
```

):

``` text
raise ConversationNotFoundError()

return conversation
```

## 70. Caso de uso: SendConversationMessage

Este será el caso de uso central del primer producto.

Se dividirá en varias etapas para evitar una transacción larga.

## 71. Flujo general de mensaje

Create user message ↓ Create AssistantExecution ↓ Commit ↓ Start AI
orchestration ↓ Call Model Gateway ↓ Persist assistant result ↓ Complete
execution

↓ Emit response

## 72. Etapa 1: aceptar mensaje

Dentro de una transacción:

## 1. validar permiso;

## 2. cargar conversación;

## 3. validar estado;

## 4. crear mensaje del usuario;

## 5. crear AssistantExecution;

## 6. actualizar last_message_at ;

## 7. persistir;

## 8. outbox assistant.execution.requested ;

## 9. commit.

## 73. SendConversationMessage command

``` text
@dataclass(frozen=True, slots=True)
class SendConversationMessageCommand:
```

actor: Actor conversation_id: ConversationId content: str response_mode:
str capability_hint: str \| None idempotency_key: str

La idempotency key será obligatoria para evitar mensajes duplicados por
reintentos del cliente.

## 74. SendConversationMessage result

``` text
@dataclass(frozen=True, slots=True)
class SendConversationMessageResult:
```

user_message_id: str assistant_execution_id: str assistant_message_id:
str

execution_status: str stream_url: str \| None

## 75. Handler de aceptación

``` text
class SendConversationMessageHandler:
def __init__(
```

self, uow_factory: UnitOfWorkFactory, authorization:
AuthorizationService, id_generator: IdGenerator, clock: Clock, ) -\>
None: ...

``` text
async def handle(
```

self, command: SendConversationMessageCommand, ) -\>
SendConversationMessageResult:

``` text
await self._authorization.require_permission(
```

command.actor, Permission("conversations.write"), )

now = self.\_clock.now()

``` text
async with self._uow_factory.create(
```

command.actor ) as uow: conversation = await
uow.conversations.get_by_id( command.actor.tenant_id,
command.conversation_id, )

if conversation is None:

``` text
raise ConversationNotFoundError()
```

user_message = conversation.add_user_message( message_id=MessageId(
self.\_id_generator.new_uuid() ), author_user_id=command.actor.user_id,
content=command.content, created_at=now,

)

execution = AssistantExecution.create( execution_id=ExecutionId(
self.\_id_generator.new_uuid() ), tenant_id=command.actor.tenant_id,
conversation_id=conversation.id, user_message_id=user_message.id,
assistant_message_id=MessageId( self.\_id_generator.new_uuid() ),
capability_hint=command.capability_hint, created_at=now, )

``` text
await uow.messages.add(user_message)
await uow.executions.add(execution)
await uow.conversations.save(conversation)

await uow.outbox.add(
```

AssistantExecutionRequestedV1.from_execution( execution ) )

``` text
await uow.commit()

return SendConversationMessageResult(
```

user_message_id=str(user_message.id),
assistant_execution_id=str(execution.id), assistant_message_id=str(
execution.assistant_message_id ),
execution_status=execution.status.value,
stream_url=build_stream_url(execution.id), )

## 76. Etapa 2: ejecutar AI

Un worker o proceso asíncrono consumirá:

assistant.execution.requested

Flujo:

## 1. reclamar ejecución;

## 2. cambiar a running;

## 3. cargar contexto;

## 4. seleccionar prompt;

## 5. seleccionar modelo;

## 6. invocar Model Gateway;

## 7. validar salida;

## 8. persistir mensaje;

## 9. completar ejecución;

## 10. emitir eventos.

## 77. AssistantExecutionOrchestrator

``` text
class AssistantExecutionOrchestrator:
def __init__(
```

self, uow_factory, model_gateway, prompt_registry,
conversation_context_loader, structured_output_validator,
event_publisher, clock, ) -\> None: ...

No será un agregado.

Será un coordinador de aplicación.

## 78. Orchestration stages

claim_execution load_context resolve_capability resolve_prompt
resolve_tools select_model execute_model

validate_output persist_result publish_completion

Cada etapa deberá ser observable.

## 79. Claim execution

Antes de llamar al modelo:

## 1. abrir transacción;

## 2. cargar ejecución con lock;

## 3. validar estado created ;

## 4. cambiar a running ;

## 5. registrar started_at ;

## 6. commit.

Esto evita que dos workers ejecuten el mismo request.

## 80. Claim implementation

``` text
async def claim_execution(
```

self, actor: Actor, execution_id: ExecutionId, ) -\> AssistantExecution:

``` text
async with self._uow_factory.create(actor) as uow:
```

execution = await uow.executions.get_for_update( actor.tenant_id,
execution_id, )

if execution is None:

``` text
raise AssistantExecutionNotFoundError()
```

execution.start(self.\_clock.now())

``` text
await uow.executions.save(execution)
await uow.commit()

return execution
```

## 81. Load conversation context

El contexto inicial incluirá:

-   system policy;
-   prompt version;
-   mensajes recientes;
-   resumen si existe;
-   configuración de tenant;
-   capabilities permitidas.

No se cargará toda la conversación sin límites.

## 82. Context window policy

La selección de mensajes deberá considerar:

-   límite de tokens;
-   prioridad;
-   último mensaje;
-   mensajes de tool relevantes;
-   summary;
-   privacidad;
-   costo.

Esta política pertenecerá a AI Runtime.

## 83. Model Gateway port

``` text
class ModelGateway(Protocol):
async def execute(
```

self, request: ModelExecutionRequest, ) -\> ModelExecutionResult: ...

El orchestrator no conocerá SDKs específicos.

## 84. Prompt Registry port

``` text
class PromptRegistry(Protocol):
async def get_active(
```

self, prompt_key: str, capability: str, ) -\> PromptDefinition: ...

En la primera versión los prompts podrán vivir en Git y cargarse al
iniciar.

## 85. Model routing policy

``` text
class ModelRoutingPolicy(Protocol):
async def select(
```

self, capability: str, tenant_id: TenantId, budget: ExecutionBudget,
required_features: set\[str\], ) -\> ModelSelection: ...

## 86. Structured output validation

El output deberá pasar por:

## 1. parse;

## 2. schema validation;

## 3. invariant validation;

## 4. citation validation cuando aplique;

## 5. tool validation cuando aplique.

## 87. Repair strategy

Si el output no cumple el schema:

## 1. intentar parse determinista;

## 2. intentar una reparación limitada;

## 3. revalidar;

## 4. fallar si continúa inválido.

La reparación:

-   tendrá máximo de intentos;
-   registrará costo;
-   registrará validación;
-   no ocultará fallos sistemáticos.

## 88. Persist result

En una nueva transacción:

## 1. cargar ejecución con lock;

## 2. verificar que siga running;

## 3. crear assistant message;

## 4. guardar usage;

## 5. guardar costo;

## 6. guardar modelo y prompt;

## 7. completar ejecución;

## 8. registrar citas;

## 9. insertar auditoría;

## 10. commit.

## 89. CompleteAssistantExecution command

Podrá representarse internamente como:

``` text
@dataclass(frozen=True, slots=True)
class CompleteAssistantExecutionCommand:
```

actor: Actor execution_id: ExecutionId result:
AssistantStructuredResponse provider: str

model: str usage: ModelUsage cost: Money latency_ms: int
prompt_reference: PromptReference

## 90. Completion handler

``` text
class CompleteAssistantExecutionHandler:
async def handle(
```

self, command: CompleteAssistantExecutionCommand, ) -\> None:

``` text
async with self._uow_factory.create(
```

command.actor ) as uow: execution = await uow.executions.get_for_update(
command.actor.tenant_id, command.execution_id, )

if execution is None:

``` text
raise AssistantExecutionNotFoundError()
```

assistant_message = execution.complete( response=command.result,
provider=command.provider, model=command.model, usage=command.usage,
cost=command.cost, latency_ms=command.latency_ms,
prompt_reference=command.prompt_reference,
completed_at=self.\_clock.now(), )

``` text
await uow.messages.add(assistant_message)
await uow.executions.save(execution)
```

for citation in command.result.citations:

``` text
await uow.citations.add(
```

MessageCitation.from_contract( tenant_id=execution.tenant_id,
message_id=assistant_message.id, citation=citation,

) )

``` text
await uow.commit()
```

## 91. Failure handling

Cuando el proveedor o validación falle:

## 1. clasificar error;

## 2. determinar retryable;

## 3. registrar intento;

## 4. aplicar retry policy;

## 5. fallar ejecución si se agota;

## 6. persistir mensaje de error seguro si aplica;

## 7. emitir evento;

## 8. notificar stream.

## 92. FailAssistantExecution

``` text
@dataclass(frozen=True, slots=True)
class FailAssistantExecutionCommand:
```

actor: Actor execution_id: ExecutionId error_code: str safe_detail: str
retryable: bool provider: str \| None

## 93. Cancellation

Cancelar una ejecución será una transición de dominio.

El handler deberá:

-   validar ownership o permiso;

-   cargar ejecución con lock;

-   solicitar cancelación;

-   commit;

-   enviar señal best effort al proceso activo.

La persistencia será la fuente de verdad.

## 94. Streaming architecture

SSE no deberá depender únicamente del socket activo.

Los eventos de streaming podrán publicarse mediante un canal temporal.

Orchestrator ↓ Execution Event Publisher ↓ Redis Pub/Sub or Streams ↓
SSE Endpoint ↓ Frontend

## 95. Eventos de streaming

No son necesariamente domain events.

Son eventos de presentación en tiempo real.

Ejemplos:

response.started response.delta retrieval.started retrieval.completed
approval.required response.completed response.failed

## 96. Persistencia vs streaming

Los deltas de texto no deberán persistirse individualmente por defecto.

Se persistirá:

-   mensaje final;
-   ejecución;
-   uso;
-   errores;
-   citas;
-   tool calls.

Los deltas son transporte efímero.

## 97. Recuperación tras desconexión

El frontend podrá consultar:

``` text
GET /assistant-executions/{execution_id}
```

La base de datos deberá permitir reconstruir el estado final aunque se
pierda el stream.

## 98. Caso de uso: UploadDocument

Etapa síncrona:

## 1. autorizar;

## 2. validar metadata;

## 3. crear documento y versión;

## 4. reservar storage key;

## 5. commit.

Etapa de infraestructura:

## 1. subir archivo;

## 2. validar checksum;

## 3. actualizar versión;

## 4. crear ingestion job;

## 5. outbox;

## 6. commit.

## 99. Upload no atómico con storage

No existe una sola transacción entre PostgreSQL y object storage.

Se utilizarán estados:

draft uploaded validated queued processing ready failed

Un reconciliador resolverá inconsistencias.

## 100. DocumentIngestionCoordinator

Responsabilidades:

-   reclamar job;
-   extraer;
-   normalizar;
-   crear chunks;
-   generar embeddings;
-   indexar;
-   marcar versión ready;
-   activar versión;
-   emitir eventos.

Cada etapa podrá confirmarse de forma independiente.

## 101. Checkpointing de ingestión

El job deberá registrar la etapa actual.

Esto permitirá:

-   reintentar desde una etapa segura;

-   evitar repetir uploads;

-   diagnosticar fallos;

-   medir duración;

-   limitar duplicados.

## 102. Chunk creation transaction

La creación de chunks podrá ejecutarse en lotes.

No deberá mantener todos los chunks en memoria cuando el documento sea
grande.

La activación de versión ocurrirá únicamente cuando:

-   extracción terminó;
-   chunks están completos;
-   embeddings requeridos están listos;
-   índices están disponibles.

## 103. Caso de uso: SearchKnowledge

El handler deberá:

## 1. autorizar;

## 2. validar filtros;

## 3. crear RetrievalRun;

## 4. ejecutar búsqueda;

## 5. aplicar autorización documental;

## 6. fusionar resultados;

## 7. evaluar suficiencia;

## 8. devolver citas;

## 9. registrar métricas.

## 104. SearchKnowledgeQuery

``` text
@dataclass(frozen=True, slots=True)
class SearchKnowledgeQuery:
```

actor: Actor query: str strategy: str filters: KnowledgeFilters

limit: int include_debug: bool

## 105. RetrievalService

``` text
class RetrievalService:
def __init__(
```

self, lexical_retriever, vector_retriever, authorization_filter,
rank_fusion, sufficiency_policy, context_assembler, ) -\> None: ...

## 106. Authorization before context

Los candidatos no autorizados deberán descartarse antes de construir el
contexto para el modelo.

No bastará con ocultar la cita en la respuesta final.

## 107. Caso de uso: RequestToolExecution

Flujo:

## 1. recibir propuesta del modelo;

## 2. resolver tool version;

## 3. validar schema;

## 4. validar permisos;

## 5. calcular riesgo;

## 6. calcular arguments hash;

## 7. determinar approval;

## 8. crear ToolExecution;

## 9. crear ApprovalRequest si aplica;

## 10. commit.

## 108. El modelo no ejecuta

El Model Gateway únicamente devolverá:

tool call proposal

El ToolExecutionCoordinator decidirá si se permite continuar.

## 109. ToolExecutionCoordinator

``` text
class ToolExecutionCoordinator:
def __init__(
```

self, tool_registry, authorization, risk_policy, approval_policy,
uow_factory, id_generator, clock, ) -\> None: ...

## 110. Tool execution stages

requested ↓ validating ↓ authorized ↓ approval_required or approved ↓
running ↓ succeeded / failed

## 111. Tool adapter port

``` text
class ToolAdapter(Protocol):
async def execute(
```

self, context: ToolExecutionContext, arguments: dict, ) -\> ToolResult:
...

Cada adapter implementará una tool o familia controlada.

## 112. Tool Registry

``` text
class ToolRegistry(Protocol):
async def get_active(
```

self, tenant_id: TenantId, tool_key: str, ) -\> ToolDefinition: ...

``` text
async def get_adapter(
```

self, adapter_key: str, ) -\> ToolAdapter: ...

## 113. Tool execution transaction split

Antes de llamada externa:

## 1. bloquear tool execution;

## 2. validar approval;

## 3. cambiar a running;

## 4. commit.

Después:

## 1. ejecutar adapter;

## 2. abrir transacción nueva;

## 3. persistir result;

## 4. marcar succeeded o failed;

## 5. commit.

## 114. Tool result sanitization

El resultado externo deberá pasar por:

-   schema validation;
-   redacción;
-   normalización;
-   clasificación;
-   límite de tamaño;
-   auditoría.

No se devolverá sin revisión al modelo.

## 115. Caso de uso: DecideApproval

Flujo:

## 1. requerir approvals.decide ;

## 2. cargar request con lock;

## 3. validar pendiente;

## 4. validar expiración;

## 5. validar elegibilidad;

## 6. validar conflicto;

## 7. registrar decisión;

## 8. actualizar estado;

## 9. outbox;

## 10. commit.

## 116. Approval side effect

La aprobación no ejecutará directamente la tool dentro de la misma
transacción.

Publicará:

approval.request.approved

Un coordinador reanudará la tool execution.

## 117. Expiration worker

Un worker periódico podrá:

## 1. buscar approvals pendientes expiradas;

## 2. reclamar filas con SKIP LOCKED ;

## 3. cambiar a expired;

## 4. emitir eventos;

## 5. actualizar ejecuciones relacionadas.

## 118. Application event handlers

Ejemplos:

ApprovalGrantedHandler

``` text
→ ResumeToolExecution
```

DocumentVersionReadyHandler

``` text
→ MakeDocumentRetrievable
```

AssistantExecutionCompletedHandler

``` text
→ UpdateConversationTimestamp
```

MemoryConfirmedHandler

``` text
→ RefreshMemoryIndex
```

## 119. Procesos largos

Los procesos largos deberán tener:

-   identidad;

-   estado;

-   intentos;

-   timestamps;

-   error;

-   timeout;

-   idempotencia;

-   métricas.

No se ejecutarán como funciones anónimas imposibles de rastrear.

## 120. Background tasks de FastAPI

BackgroundTasks podrá utilizarse solo para tareas pequeñas no críticas.

No se utilizará para:

-   ingestión documental;
-   tool execution;
-   workflows importantes;
-   procesos que deban sobrevivir reinicios.

## 121. Worker architecture

La interfaz de worker deberá estar desacoplada de la tecnología de cola.

``` text
class MessageConsumer(Protocol):
async def consume(self, message: IntegrationMessage) -> None:
```

...

Podrá implementarse inicialmente con una solución sencilla y evolucionar
después.

## 122. Job handler

Cada tipo de job tendrá handler explícito.

DocumentIngestionJobHandler OutboxPublicationJobHandler
ApprovalExpirationJobHandler AssistantExecutionJobHandler

## 123. Job idempotency

El handler deberá verificar:

-   message ID;
-   job status;
-   attempt;
-   recurso actual;
-   resultado previo.

Recibir el mismo mensaje dos veces no deberá duplicar efectos.

## 124. Inbox flow

Receive message ↓ Insert inbox record ↓

``` text
If duplicate → acknowledge
```

↓ Execute handler ↓ Mark processed

## 125. Observability context

Cada handler deberá conocer:

-   request ID;
-   correlation ID;
-   causation ID;
-   execution ID cuando aplique;
-   tenant ID;
-   actor type.

Estos datos se propagarán a:

-   logs;

-   traces;

-   eventos;

-   jobs;

-   auditoría.

## 126. Tracing spans

Spans sugeridos:

command.create_conversation command.send_message assistant.execution
model.gateway.execute retrieval.hybrid tool.execute approval.decide
repository.conversation.get uow.commit

## 127. Métricas de application layer

Se medirán:

-   duración por handler;
-   éxito y fallo;
-   errores por código;
-   commits;
-   rollbacks;
-   retries;
-   conflictos;
-   idempotency replays;
-   commands por tenant;
-   queries lentas;
-   ejecuciones activas.

## 128. Logging

Cada handler deberá emitir logs estructurados.

Inicio:

``` text
{
"event": "command.started",
"command": "SendConversationMessageCommand",
"tenant_id": "ten_123",
"correlation_id": "corr_123"
}
```

Final:

``` text
{
"event": "command.completed",
"command": "SendConversationMessageCommand",
"duration_ms": 84,
"status": "success"
}
```

## 129. No loggear payloads completos

No se registrarán por defecto:

-   mensajes completos;
-   documentos;
-   tool arguments;
-   prompts;
-   tokens;
-   respuestas sensibles.

Se registrarán:

-   hashes;
-   tamaños;
-   IDs;
-   clasificación;
-   códigos;
-   métricas.

## 130. Audit from application

La aplicación decidirá qué acciones requieren auditoría.

Ejemplo:

audit_event = AuditEvent.record( actor=command.actor,
action="conversation.created", resource_type="conversation",
resource_id=conversation.id, result="success", occurred_at=now, )

La auditoría crítica se persistirá dentro de la misma transacción cuando
sea posible.

## 131. Audit de operaciones denegadas

Las operaciones denegadas podrán registrarse fuera de la transacción
empresarial.

Ejemplos:

-   tool no autorizada;
-   tenant mismatch;
-   aprobación por actor no elegible;
-   intento repetido sospechoso.

## 132. Configuración

Los handlers recibirán configuración tipada.

No leerán directamente variables de entorno.

Ejemplo:

``` text
@dataclass(frozen=True)
class AssistantExecutionSettings:
```

timeout_seconds: int max_output_tokens: int max_repair_attempts: int

## 133. Feature Flags

Las capacidades progresivas podrán protegerse con feature flags.

Ejemplos:

rag_enabled tool_calling_enabled approvals_enabled memory_enabled
mcp_enabled

Las flags no deberán sustituir autorización.

## 134. FeatureFlagService

``` text
class FeatureFlagService(Protocol):
async def is_enabled(
```

self, key: str, tenant_id: TenantId, ) -\> bool: ...

## 135. Budget enforcement

Antes de invocar AI se podrá evaluar:

-   presupuesto del tenant;
-   límite diario;
-   máximo por ejecución;
-   modelo permitido;
-   tokens máximos.

## 136. CostBudgetPolicy

``` text
class CostBudgetPolicy(Protocol):
async def authorize_execution(
```

self, tenant_id: TenantId, estimated_cost: Money, capability: str, ) -\>
BudgetDecision: ...

Una ejecución podrá:

-   permitirse;
-   degradar modelo;
-   reducir tokens;
-   rechazarse.

## 137. Application-level timeouts

Todo handler que invoque infraestructura tendrá timeout.

Ejemplos:

database query model provider tool adapter object storage event
publisher

Los timeouts deberán configurarse por dependencia.

## 138. Graceful degradation

La aplicación podrá degradar capacidades controladamente.

Ejemplos:

``` text
RAG unavailable → direct abstention
Primary model unavailable → approved fallback
Streaming unavailable → polling
Audit async unavailable → critical operation blocked when required
```

No se ocultará una degradación crítica.

## 139. Health use cases

Se distinguirán:

Liveness El proceso está vivo.

Readiness Dependencias mínimas disponibles.

Deep health Integridad más amplia para operación.

Los endpoints health no usarán handlers empresariales normales.

## 140. Application module structure

src/geem_ai/

``` text
├── conversations/
│    ├── domain/
│    ├── application/
│    │     ├── commands/
│    │     ├── queries/
│    │     ├── handlers/
│    │     ├── dto/
│    │     ├── ports/
│    │     ├── services/
│    │     └── errors.py

│    ├── infrastructure/
│    └── presentation/
```

## 141. Commands directory

application/

``` text
└── commands/
├── create_conversation.py
├── send_conversation_message.py
├── archive_conversation.py
└── cancel_assistant_execution.py
```

Cada archivo podrá contener:

-   command;
-   result;
-   handler.

O podrán separarse cuando crezcan.

## 142. Queries directory

application/

``` text
└── queries/
├── get_conversation.py
├── list_conversations.py
└── get_assistant_execution.py
```

## 143. Ports directory

application/

``` text
└── ports/
├── unit_of_work.py
├── repositories.py
├── model_gateway.py
├── event_publisher.py

├── clock.py
└── id_generator.py
```

## 144. Services directory

application/

``` text
└── services/
├── authorization_service.py
├── assistant_execution_orchestrator.py
├── idempotency_service.py
└── conversation_context_loader.py
```

## 145. Shared application layer

Solo se compartirán capacidades verdaderamente transversales.

shared/

``` text
└── application/
├── actor_context.py
├── errors.py
├── pagination.py
├── idempotency.py
└── transaction.py
```

No se colocará toda la lógica en shared .

## 146. Primer vertical slice

El primer slice oficial será:

Create Conversation

Deberá incluir:

-   endpoint;

-   request schema;

-   command;

-   handler;

-   aggregate;

-   repository;

-   Unit of Work;

-   SQLAlchemy model;

-   migration;

-   RLS;

-   response;

-   tests;

-   OpenAPI;

-   observabilidad.

## 147. Objetivo del primer slice

Validar de extremo a extremo:

FastAPI

``` text
→ Application
→ Domain
→ SQLAlchemy
→ PostgreSQL
→ RLS
→ Response
```

No incluirá todavía una llamada a LLM.

## 148. Segundo vertical slice

Get and List Conversations

Validará:

-   query handlers;
-   cursor pagination;
-   ownership;
-   read repositories;
-   tenant isolation.

## 149. Tercer vertical slice

Send Message and Persist AssistantExecution

Validará:

-   messages;
-   idempotencia;
-   outbox;
-   ejecución pendiente;
-   SSE inicial.

Aún podrá utilizar un proveedor fake.

## 150. Cuarto vertical slice

First Model Gateway Response

Validará:

-   provider adapter;
-   prompt;
-   structured output;
-   tokens;
-   costo;
-   persistencia;
-   failure handling.

## 151. Quinto vertical slice

Authentication and Membership Enforcement

Aunque el modelo de datos exista desde el inicio, la integración
completa de identidad podrá desarrollarse como slice.

En ambientes iniciales se podrá usar un actor de desarrollo controlado.

Nunca en producción.

## 152. Sexto vertical slice

Document Upload and Ingestion Job

Validará:

-   object storage;
-   estados;
-   worker;
-   checksum;
-   outbox;
-   reconciliación.

## 153. Séptimo vertical slice

RAG with Citations

Validará:

-   chunks;
-   embeddings;
-   retrieval;
-   autorización;
-   context assembly;
-   citation validation;
-   abstention.

## 154. Octavo vertical slice

Read Tool

Tool inicial:

search_support_procedures

Permitirá validar Tool Registry sin side effects.

## 155. Noveno vertical slice

Write Tool with Human Approval

Tool:

create_support_ticket

Validará:

-   arguments;
-   riesgo;
-   idempotencia;
-   approval;
-   ejecución;
-   auditoría.

## 156. TDD por vertical slice

Cada slice deberá comenzar con pruebas de aceptación.

Ejemplo:

Given an active user and tenant When the user creates a conversation
Then the conversation is persisted And belongs to the active tenant And
another tenant cannot read it And an audit event exists

## 157. Tests de handlers

Los handlers deberán probarse con:

-   fakes;

-   in-memory repositories para unit tests;

-   clocks deterministas;

-   ID generators deterministas;

-   policies controladas.

## 158. Repository integration tests

Los repositorios se probarán con PostgreSQL real.

No se confiará únicamente en mocks para verificar:

-   queries;
-   RLS;
-   constraints;
-   locking;
-   concurrencia;
-   mapping.

## 159. Fake Model Gateway

Para los primeros slices:

``` text
class FakeModelGateway:
def __init__(
```

self, result: ModelExecutionResult, ) -\> None: self.result = result
self.requests = \[\]

``` text
async def execute(self, request):
```

self.requests.append(request)

``` text
return self.result
```

Esto permite pruebas deterministas.

## 160. Fake Clock

``` text
class FrozenClock:
def __init__(self, value):
```

self.\_value = value

``` text
def now(self):
return self._value
```

## 161. Fake ID Generator

``` text
class SequenceIdGenerator:
def __init__(self, values):
```

self.\_values = iter(values)

``` text
def new_uuid(self):
return next(self._values)
```

## 162. Test naming

Ejemplos:

test_create_conversation_persists_active_conversation
test_create_conversation_requires_permission
test_archived_conversation_rejects_new_message
test_send_message_replays_same_idempotent_result
test_second_worker_cannot_claim_running_execution

## 163. Application acceptance criteria

Un caso de uso estará terminado cuando:

-   command o query existe;
-   handler existe;
-   autorización existe;
-   tenant está protegido;
-   transacción está definida;
-   errores están definidos;
-   idempotencia fue evaluada;
-   eventos fueron evaluados;
-   observabilidad existe;
-   pruebas pasan;
-   contrato HTTP funciona.

## 164. Handler checklist

``` text
[ ] Intent is explicit
[ ] Actor is authenticated
[ ] Permission is checked
[ ] Tenant context is resolved
[ ] Input is validated
[ ] Aggregate is loaded or created
[ ] Domain methods are used
[ ] Transaction boundary is clear
[ ] External calls are outside DB transaction
[ ] Idempotency is reviewed
[ ] Events are recorded
[ ] Audit is reviewed
[ ] Errors are mapped
[ ] Metrics and traces exist
[ ] Tests exist
```

## 165. Orchestrator checklist

``` text
[ ] Process has persistent identity
[ ] Stages are explicit
[ ] Current state is persisted
[ ] Retries are bounded
[ ] Timeouts exist
[ ] Duplicate execution is prevented
[ ] External calls are isolated
[ ] Results are validated
[ ] Failure is persisted
[ ] Telemetry exists
[ ] Recovery is possible
```

## 166. Query checklist

``` text
[ ] No business side effects
[ ] Permission checked
[ ] Tenant filter present

[ ] RLS context present
[ ] Result size bounded
[ ] Stable ordering
[ ] Pagination defined
[ ] Sensitive fields excluded
[ ] Query plan reviewed
[ ] Not-found behavior defined
```

## 167. Anti-patterns

Fat Controller Endpoint con lógica empresarial.

Generic Service Un AssistantService con todos los casos de uso.

ORM as Domain Modificar modelos SQLAlchemy directamente.

Hidden Transaction Commit implícito difícil de controlar.

Long Transaction Mantener DB abierta durante llamadas externas.

Direct SDK Usage Handlers llamando OpenAI o Anthropic.

Authorization in UI Confiar en que el botón no aparece.

Tenant from Request Body Aceptar tenant arbitrario.

Fire-and-Forget Critical Task Tarea importante sin estado persistente.

Retry Whole Workflow Repetir efectos ya realizados.

Event Before Commit Publicar antes de confirmar datos.

Catch Exception Capturar todo y devolver error genérico.

## 168. Riesgos

AA-001 --- Application layer demasiado gruesa Mitigación:

-   mover invariantes al dominio;
-   dividir casos de uso;
-   evitar services genéricos.

AA-002 --- Orchestrator monolítico Mitigación:

-   etapas explícitas;
-   ports;
-   handlers por fase;
-   state machine persistente.

AA-003 --- Demasiados decoradores Mitigación:

-   pipeline mínimo;
-   orden documentado;
-   debugging claro.

AA-004 --- Reintentos duplicando efectos Mitigación:

-   idempotencia;
-   retries locales;
-   estados persistentes;
-   inbox/outbox.

AA-005 --- Autorización inconsistente Mitigación:

-   servicio central;
-   resource policies;
-   pruebas por handler;
-   deny by default.

AA-006 --- Fugas de infraestructura Mitigación:

-   ports;
-   composition root;
-   revisión de imports;
-   architecture tests.

## 169. Architecture tests

Podrán implementarse pruebas que verifiquen:

-   domain no importa infrastructure;
-   application no importa presentation;
-   handlers no importan FastAPI;
-   domain no importa SQLAlchemy;
-   provider SDKs solo aparecen en adapters;
-   módulos no acceden a modelos ORM ajenos.

## 170. Ejemplo de regla con import-linter

Domain must not import: - fastapi - sqlalchemy - openai - anthropic -
redis - boto3

Podrá utilizarse:

-   import-linter;
-   pytest-archon;
-   herramienta equivalente.

## 171. Preguntas de entrevista

Erick deberá poder explicar:

-   ¿Qué diferencia existe entre command, query y domain event?
-   ¿Por qué un handler no debe llamar directamente al ORM?
-   ¿Qué responsabilidad tiene Unit of Work?
-   ¿Por qué el commit es explícito?
-   ¿Cómo evitas una transacción larga durante una llamada LLM?
-   ¿Cómo separas aceptar un mensaje de generar la respuesta?
-   ¿Cómo evitas que dos workers ejecuten el mismo assistant execution?
-   ¿Dónde se aplica autorización?
-   ¿Cómo modelas idempotencia?
-   ¿Qué diferencia existe entre domain event e integration event?
-   ¿Por qué utilizar outbox?
-   ¿Cómo reanudas una ejecución después de una aprobación?
-   ¿Cuándo utilizarías un domain service?
-   ¿Cómo pruebas un handler sin PostgreSQL?
-   ¿Cómo pruebas los repositorios y RLS?
-   ¿Por qué no necesitas un command bus complejo desde el principio?

## 172. Decisiones oficiales

Quedan aprobadas las siguientes decisiones:

## 1. La aplicación se organizará por casos de uso explícitos.

## 2. Los cambios utilizarán commands.

## 3. Las lecturas utilizarán queries.

## 4. Cada command o query tendrá un handler principal.

## 5. Se aplicará CQRS pragmático.

## 6. Los handlers no dependerán de FastAPI.

## 7. Los handlers no utilizarán modelos ORM directamente como dominio.

## 8. Los repositorios serán específicos por agregado.

## 9. Los repositorios empresariales serán tenant-aware.

## 10. Las queries podrán usar read repositories optimizados.

## 11. Unit of Work delimitará las transacciones.

## 12. El commit será explícito.

## 13. No se mantendrán transacciones abiertas durante llamadas externas.

## 14. La autorización se aplicará antes del acceso al recurso.

## 15. El sistema utilizará deny by default.

## 16. Los recursos tendrán autorización adicional a los permisos generales.

## 17. El actor provendrá del contexto autenticado.

## 18. La idempotencia se implementará como capacidad transversal.

## 19. No todos los commands requerirán idempotency key.

## 20. Los agregados registrarán domain events.

## 21. Los integration events se publicarán mediante outbox.

## 22. No se publicarán eventos externos antes del commit.

## 23. No será obligatorio implementar command bus en el primer slice.

## 24. La inyección de dependencias será explícita.

## 25. Existirá un composition root.

## 26. No se utilizará Service Locator.

## 27. Clock e IdGenerator serán ports.

## 28. SendConversationMessage se dividirá en aceptación y ejecución.

## 29. AssistantExecution será reclamado antes de invocar el modelo.

## 30. El resultado del modelo será validado antes de persistirse.

## 31. Los fallos AI quedarán persistidos y clasificados.

## 32. El streaming será transporte efímero, no fuente de verdad.

## 33. La recuperación después de una desconexión usará el estado persistido.

## 34. Los procesos largos tendrán estado e identidad.

## 35. FastAPI BackgroundTasks no se usará para tareas críticas.

## 36. Los workers serán idempotentes.

## 37. Las tool calls serán propuestas por el modelo y ejecutadas por la aplicación.

## 38. Tool execution y llamadas externas usarán transacciones separadas.

## 39. Aprobar una acción no equivale a ejecutarla.

## 40. La aprobación reanudará la ejecución mediante evento.

## 41. La observabilidad se propagará por cada caso de uso.

## 42. Los payloads sensibles no se registrarán completos.

## 43. Los feature flags no sustituirán autorización.

## 44. Los presupuestos AI se controlarán antes de ejecutar.

## 45. Los casos de uso se implementarán mediante vertical slices.

## 46. El primer slice será Create Conversation.

## 47. El primer acceso AI utilizará un Fake Model Gateway antes del proveedor real.

## 48. Las pruebas unitarias usarán fakes deterministas.

## 49. Las pruebas de repositorios utilizarán PostgreSQL real.

## 50. Se incorporarán architecture tests para proteger dependencias.

## 173. Próximo documento

Documento 16 --- Project 1 Infrastructure Architecture Definirá de forma
implementable:

-   configuración de entornos;
-   Docker;
-   PostgreSQL;
-   Redis;
-   object storage;
-   workers;
-   colas;
-   proveedores AI;
-   Model Gateway adapters;
-   secret management;
-   networking;
-   reverse proxy;
-   CI/CD;
-   despliegue;
-   health checks;
-   resiliencia;
-   backups;
-   desarrollo local;
-   staging;
-   producción;
-   estructura Docker Compose;
-   ejemplos de configuración.

## 174. Conclusión

La arquitectura de aplicación de GEEM AI Assistant queda estructurada
alrededor de casos de uso explícitos, límites transaccionales claros y
dependencias controladas.

Cada operación deberá responder con precisión:

-   quién la solicitó;
-   qué permiso requiere;
-   qué agregado modifica;
-   qué transacción utiliza;
-   qué evento produce;
-   qué sucede si falla;
-   cómo evita duplicados;
-   cómo puede observarse;
-   cómo puede probarse.

La inteligencia artificial no será una excepción dentro de la
arquitectura.

Será una dependencia coordinada por casos de uso, gobernada por
políticas, validada mediante contratos y contenida dentro de procesos
persistentes y recuperables.

Con este documento ya existe una ruta directa para implementar el primer
vertical slice sin improvisar responsabilidades ni mezclar capas.
