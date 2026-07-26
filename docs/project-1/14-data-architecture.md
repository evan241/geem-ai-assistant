# AI Engineering Lab

## Documento 14 --- Project 1 Data Architecture

GEEM AI Assistant **Versión:** 1.0 **Estado:** Arquitectura de datos
oficial **Responsable técnico:** Director de AI Engineering **Lead
Engineer:** Erick Eduardo Evangelista Velasco **Proyecto:** GEEM AI
Assistant Motor principal: PostgreSQL Extensiones iniciales: pgvector
ORM: SQLAlchemy 2.x Migraciones: Alembic

## 1. Propósito

Este documento define la arquitectura de datos implementable de GEEM AI
Assistant.

Su objetivo es convertir el modelo de dominio en una estructura
persistente concreta que permita:

-   aislamiento multi-tenant;
-   consistencia transaccional;
-   trazabilidad;
-   búsqueda documental;
-   búsqueda vectorial;
-   procesamiento asíncrono;
-   idempotencia;
-   control de concurrencia;
-   evaluación;
-   auditoría;
-   evolución mediante migraciones.

Este documento será la referencia oficial para:

-   modelos SQLAlchemy;

-   migraciones Alembic;

-   repositorios;

-   políticas Row-Level Security;

-   índices;

-   consultas;

-   fixtures;

-   respaldos;

-   retención;

-   crecimiento futuro.

## 2. Principio rector

La base de datos protege integridad y aislamiento, pero no reemplaza al
modelo de dominio.

Las reglas críticas deberán existir en más de una capa cuando
corresponda:

-   dominio;
-   aplicación;
-   constraints;
-   índices;
-   Row-Level Security;
-   pruebas.

No se confiará únicamente en validaciones de frontend o en convenciones
de código.

## 3. Tecnología oficial

La arquitectura inicial utilizará:

PostgreSQL SQLAlchemy 2.x Alembic pgvector PostgreSQL Full-Text Search

Redis y object storage formarán parte de la arquitectura general, pero
no serán fuentes de verdad empresariales.

## 4. Razones para PostgreSQL

PostgreSQL permite integrar:

-   modelo relacional;

-   transacciones ACID;

-   JSONB controlado;

-   full-text search;

-   pgvector;

-   Row-Level Security;

-   índices avanzados;

-   constraints;

-   advisory locks;

-   particionamiento futuro;

-   extensiones;

-   observabilidad madura.

Esto reduce la necesidad de incorporar múltiples almacenes
especializados desde la primera versión.

## 5. Fuentes de verdad

Tipo de información Fuente de verdad

Usuarios y acceso PostgreSQL

Organizaciones y tenants PostgreSQL

Conversaciones y mensajes PostgreSQL

Documentos y estados PostgreSQL

Archivos originales Object storage

Texto extraído PostgreSQL u object storage según tamaño

Chunks PostgreSQL

Embeddings PostgreSQL + pgvector

Tools y ejecuciones PostgreSQL

Aprobaciones PostgreSQL

Memoria PostgreSQL

Auditoría PostgreSQL inicial

Cache Redis

Jobs temporales Cola seleccionada

Prompts iniciales Git

Datasets de evaluación Git y PostgreSQL según uso

## 6. Estrategia de schemas

Se utilizará inicialmente un schema principal:

public

Las tablas utilizarán prefijos funcionales o nombres claros.

No se dividirán inmediatamente en múltiples PostgreSQL schemas, porque
esto puede añadir complejidad a:

-   Alembic;
-   permisos;
-   debugging;
-   testing;
-   tooling;
-   despliegues.

La separación por módulos será primero lógica y de código.

## 7. Revisión futura de schemas

Podrán incorporarse schemas físicos cuando exista una necesidad
demostrada, por ejemplo:

identity organizations knowledge audit evaluation

La decisión requerirá ADR.

## 8. Convenciones de nombres

Tablas Plural y snake_case.

users organizations assistant_executions document_versions

Columnas Snake case.

tenant_id created_at arguments_hash

Primary keys

pk\_
```{=html}
<table>
```
Foreign keys

fk\_
```{=html}
<table>
```
\_\_`<referenced_table>`{=html}

Unique constraints

uq\_
```{=html}
<table>
```
\_\_`<columns>`{=html}

Check constraints

ck\_
```{=html}
<table>
```
\_\_`<rule>`{=html}

Índices

ix\_
```{=html}
<table>
```
\_\_`<columns_or_purpose>`{=html}

## 9. Identificadores

La estrategia recomendada será:

UUIDv7

Razones:

-   opaco;
-   distribuible;
-   ordenable aproximadamente por tiempo;
-   menor fragmentación que UUIDv4;
-   compatible con PostgreSQL;
-   útil para eventos y jobs.

La decisión definitiva deberá documentarse en ADR-0002.

## 10. Tipo de identificador en PostgreSQL

Se utilizará:

uuid

No se almacenarán UUIDs como varchar .

## 11. Generación de IDs

Los IDs se generarán preferentemente en la aplicación.

Ventajas:

-   entidad con identidad antes de persistir;
-   eventos previos al commit;
-   menor dependencia de defaults;
-   facilidad en pruebas;
-   compatibilidad con outbox.

## 12. Timestamps

Las columnas temporales utilizarán:

timestamptz

Columnas comunes:

created_at updated_at deleted_at started_at completed_at expires_at

Todos los valores se almacenarán en UTC.

## 13. Columnas comunes

Las tablas empresariales incluirán cuando aplique:

id tenant_id created_at updated_at version

También podrán incluir:

created_by updated_by deleted_at status metadata

## 14. Optimistic concurrency

Los aggregate roots con riesgo de concurrencia utilizarán:

version integer not null default 1

Cada actualización ejecutará conceptualmente:

``` text
UPDATE table
```

SET ..., version = version + 1 WHERE id = :id AND version =
:expected_version;

Si no se modifica ninguna fila, se producirá:

CONCURRENCY_CONFLICT

## 15. Estrategia multi-tenant

El sistema utilizará inicialmente:

Shared Database + Shared Schema + tenant_id por fila

## 16. Razones para shared schema

-   operación sencilla;
-   migraciones centralizadas;
-   menor costo;
-   consultas administrativas posibles;
-   onboarding rápido;
-   escala suficiente para el producto inicial.

## 17. Defensa multi-tenant por capas

El aislamiento se aplicará mediante:

## 1. tenant context autenticado;

## 2. application policies;

## 3. repositorios tenant-aware;

## 4. foreign keys compuestas cuando aporte valor;

## 5. índices por tenant;

## 6. Row-Level Security;

## 7. pruebas de aislamiento;

## 8. auditoría.

## 18. Tenant context en la conexión

Antes de ejecutar operaciones empresariales se establecerá una variable
de sesión:

SET LOCAL app.tenant_id = 'tenant-uuid';

También podrá establecerse:

SET LOCAL app.user_id = 'user-uuid';

SET LOCAL limitará el contexto a la transacción actual.

## 19. Helper SQL para tenant actual

``` text
CREATE FUNCTION current_tenant_id()
```

RETURNS uuid LANGUAGE sql STABLE AS \$\$

``` text
SELECT NULLIF(current_setting('app.tenant_id', true), '')::uuid
```

\$\$;

Esta función deberá definirse de manera segura y probarse.

## 20. Row-Level Security

RLS se utilizará en tablas empresariales con tenant_id .

Ejemplo:

``` text
ALTER TABLE conversations ENABLE ROW LEVEL SECURITY;
ALTER TABLE conversations FORCE ROW LEVEL SECURITY;
```

Policy:

``` text
CREATE POLICY conversations_tenant_isolation
```

ON conversations USING (tenant_id = current_tenant_id()) WITH CHECK
(tenant_id = current_tenant_id());

## 21. FORCE ROW LEVEL SECURITY

Se utilizará para evitar que el owner de la tabla ignore RLS
accidentalmente.

Las migraciones y tareas administrativas deberán utilizar un rol
específico con privilegios controlados.

## 22. Roles de base de datos

Se definirán conceptualmente:

geem_migrator geem_app geem_worker geem_readonly geem_admin

geem_migrator Ejecuta migraciones.

geem_app Uso normal de API.

geem_worker Procesamiento asíncrono.

geem_readonly Consultas de soporte o analítica controlada.

geem_admin Operación extraordinaria auditada.

## 23. Regla de bypass RLS

El rol de aplicación no tendrá:

BYPASSRLS

El bypass solo podrá existir en roles administrativos extraordinarios y
auditados.

## 24. Tenant en tablas globales

Algunas tablas no tendrán tenant_id .

Ejemplos:

users identity_providers organizations system_permissions

Su acceso seguirá controlado mediante aplicación y policies específicas.

## 25. Relaciones tenant-safe

Cuando dos recursos empresariales se relacionen, deberá garantizarse que
pertenecen al mismo tenant.

Ejemplo conceptual:

UNIQUE (tenant_id, id)

y foreign key compuesta:

FOREIGN KEY (tenant_id, conversation_id) REFERENCES conversations
(tenant_id, id)

Esto podrá utilizarse en relaciones de alto riesgo.

## 26. Costo de foreign keys compuestas

No se aplicarán indiscriminadamente.

Se priorizarán en:

-   mensajes y conversaciones;
-   chunks y documentos;
-   tool executions y approvals;
-   memories y users tenant-scoped;
-   entidades donde un mismatch sea crítico.

## 27. Identity tables

users

``` text
CREATE TABLE users (
```

id uuid PRIMARY KEY, email varchar(320) NOT NULL, normalized_email
varchar(320) NOT NULL, display_name varchar(160) NOT NULL,
preferred_language varchar(8) NOT NULL DEFAULT 'es', status varchar(32)
NOT NULL,

created_at timestamptz NOT NULL, updated_at timestamptz NOT NULL,
version integer NOT NULL DEFAULT 1,

CONSTRAINT uq_users\_\_normalized_email UNIQUE (normalized_email),

CONSTRAINT ck_users\_\_status CHECK (status IN ( 'pending', 'active',
'suspended', 'disabled', 'deleted' )) );

## 28. Índices de users

``` text
CREATE INDEX ix_users__status
```

ON users (status);

El índice único por email normalizado cubre la búsqueda de login.

## 29. sessions

``` text
CREATE TABLE sessions (
```

id uuid PRIMARY KEY, user_id uuid NOT NULL, status varchar(32) NOT NULL,
refresh_token_fingerprint varchar(255) NOT NULL, device_metadata jsonb
NOT NULL DEFAULT '{}'::jsonb, created_at timestamptz NOT NULL,
expires_at timestamptz NOT NULL, revoked_at timestamptz NULL,

CONSTRAINT fk_sessions\_\_users FOREIGN KEY (user_id) REFERENCES users
(id),

CONSTRAINT ck_sessions\_\_status

CHECK (status IN ('active', 'expired', 'revoked')),

CONSTRAINT ck_sessions\_\_expiration CHECK (expires_at \> created_at) );

## 30. Índices de sessions

``` text
CREATE INDEX ix_sessions__user_status
```

ON sessions (user_id, status);

``` text
CREATE INDEX ix_sessions__expires_at
```

ON sessions (expires_at) WHERE status = 'active';

## 31. organizations

``` text
CREATE TABLE organizations (
```

id uuid PRIMARY KEY, legal_name varchar(200) NOT NULL, display_name
varchar(160) NOT NULL, status varchar(32) NOT NULL, default_tenant_id
uuid NULL, created_at timestamptz NOT NULL, updated_at timestamptz NOT
NULL, version integer NOT NULL DEFAULT 1,

CONSTRAINT ck_organizations\_\_status CHECK (status IN ('active',
'suspended', 'closed')) );

La foreign key de default_tenant_id se agregará después de crear tenants
.

## 32. tenants

``` text
CREATE TABLE tenants (
```

id uuid PRIMARY KEY,

organization_id uuid NOT NULL, name varchar(160) NOT NULL, slug
varchar(120) NOT NULL, status varchar(32) NOT NULL, settings jsonb NOT
NULL DEFAULT '{}'::jsonb, created_at timestamptz NOT NULL, updated_at
timestamptz NOT NULL, version integer NOT NULL DEFAULT 1,

CONSTRAINT fk_tenants\_\_organizations FOREIGN KEY (organization_id)
REFERENCES organizations (id),

CONSTRAINT uq_tenants\_\_organization_slug UNIQUE (organization_id,
slug),

CONSTRAINT ck_tenants\_\_status CHECK (status IN ( 'provisioning',
'active', 'suspended', 'archived' )) );

## 33. Foreign key de default tenant

``` text
ALTER TABLE organizations
```

ADD CONSTRAINT fk_organizations\_\_default_tenant FOREIGN KEY
(default_tenant_id) REFERENCES tenants (id);

La aplicación deberá validar que el tenant pertenece a la organización.

Podrá añadirse una restricción más fuerte mediante trigger o rediseño si
el riesgo lo justifica.

## 34. memberships

``` text
CREATE TABLE memberships (
```

id uuid PRIMARY KEY,

user_id uuid NOT NULL, organization_id uuid NOT NULL, tenant_id uuid NOT
NULL, status varchar(32) NOT NULL, joined_at timestamptz NULL,
suspended_at timestamptz NULL, created_at timestamptz NOT NULL,
updated_at timestamptz NOT NULL, version integer NOT NULL DEFAULT 1,

CONSTRAINT fk_memberships\_\_users FOREIGN KEY (user_id) REFERENCES
users (id),

CONSTRAINT fk_memberships\_\_organizations FOREIGN KEY (organization_id)
REFERENCES organizations (id),

CONSTRAINT fk_memberships\_\_tenants FOREIGN KEY (tenant_id) REFERENCES
tenants (id),

CONSTRAINT uq_memberships\_\_user_tenant UNIQUE (user_id, tenant_id),

CONSTRAINT ck_memberships\_\_status CHECK (status IN ( 'invited',
'active', 'suspended', 'revoked' )) );

## 35. Índices de memberships

``` text
CREATE INDEX ix_memberships__tenant_status
```

ON memberships (tenant_id, status);

``` text
CREATE INDEX ix_memberships__user_status
```

ON memberships (user_id, status);

## 36. roles

``` text
CREATE TABLE roles (
```

id uuid PRIMARY KEY, tenant_id uuid NOT NULL, name varchar(120) NOT
NULL, key varchar(100) NOT NULL, is_system boolean NOT NULL DEFAULT
false, status varchar(32) NOT NULL, created_at timestamptz NOT NULL,
updated_at timestamptz NOT NULL, version integer NOT NULL DEFAULT 1,

CONSTRAINT fk_roles\_\_tenants FOREIGN KEY (tenant_id) REFERENCES
tenants (id),

CONSTRAINT uq_roles\_\_tenant_key UNIQUE (tenant_id, key),

CONSTRAINT ck_roles\_\_status CHECK (status IN ('active', 'disabled'))
);

## 37. permissions

Los permisos serán inicialmente un catálogo global.

``` text
CREATE TABLE permissions (
```

id uuid PRIMARY KEY, key varchar(160) NOT NULL, description varchar(500)
NOT NULL, created_at timestamptz NOT NULL,

CONSTRAINT uq_permissions\_\_key UNIQUE (key) );

## 38. role_permissions

``` text
CREATE TABLE role_permissions (
```

role_id uuid NOT NULL, permission_id uuid NOT NULL,

PRIMARY KEY (role_id, permission_id),

CONSTRAINT fk_role_permissions\_\_roles FOREIGN KEY (role_id) REFERENCES
roles (id) ON DELETE CASCADE,

CONSTRAINT fk_role_permissions\_\_permissions FOREIGN KEY
(permission_id) REFERENCES permissions (id) ON DELETE CASCADE );

## 39. membership_roles

``` text
CREATE TABLE membership_roles (
```

membership_id uuid NOT NULL, role_id uuid NOT NULL, tenant_id uuid NOT
NULL,

PRIMARY KEY (membership_id, role_id),

CONSTRAINT fk_membership_roles\_\_memberships FOREIGN KEY
(membership_id) REFERENCES memberships (id) ON DELETE CASCADE,

CONSTRAINT fk_membership_roles\_\_roles FOREIGN KEY (role_id) REFERENCES
roles (id) ON DELETE CASCADE );

La coherencia de tenant deberá reforzarse con aplicación, pruebas y,
cuando sea conveniente, foreign keys compuestas.

## 40. Conversations tables

conversations

``` text
CREATE TABLE conversations (
```

id uuid PRIMARY KEY, tenant_id uuid NOT NULL, owner_user_id uuid NOT
NULL, title varchar(160) NOT NULL, status varchar(32) NOT NULL, language
varchar(8) NOT NULL DEFAULT 'es', created_at timestamptz NOT NULL,
updated_at timestamptz NOT NULL, last_message_at timestamptz NULL,
deleted_at timestamptz NULL, version integer NOT NULL DEFAULT 1,

CONSTRAINT fk_conversations\_\_tenants FOREIGN KEY (tenant_id)
REFERENCES tenants (id),

CONSTRAINT fk_conversations\_\_users FOREIGN KEY (owner_user_id)
REFERENCES users (id),

CONSTRAINT uq_conversations\_\_tenant_id_id UNIQUE (tenant_id, id),

CONSTRAINT ck_conversations\_\_status CHECK (status IN ( 'active',
'archived', 'locked', 'deleted' )),

CONSTRAINT ck_conversations\_\_language CHECK (language IN ('es', 'en'))
);

## 41. Índices de conversations

``` text
CREATE INDEX ix_conversations__tenant_owner_updated
```

ON conversations ( tenant_id, owner_user_id, updated_at DESC, id DESC )
WHERE deleted_at IS NULL;

``` text
CREATE INDEX ix_conversations__tenant_status
```

ON conversations (tenant_id, status);

El primer índice soportará paginación por cursor.

## 42. messages

``` text
CREATE TABLE messages (
```

id uuid PRIMARY KEY, tenant_id uuid NOT NULL, conversation_id uuid NOT
NULL, author_type varchar(32) NOT NULL, author_id uuid NULL, role
varchar(32) NOT NULL, content text NOT NULL, status varchar(32) NOT
NULL, execution_id uuid NULL, metadata jsonb NOT NULL DEFAULT
'{}'::jsonb, created_at timestamptz NOT NULL, completed_at timestamptz
NULL,

CONSTRAINT fk_messages\_\_conversation_tenant FOREIGN KEY (tenant_id,
conversation_id) REFERENCES conversations (tenant_id, id),

CONSTRAINT uq_messages\_\_tenant_id_id UNIQUE (tenant_id, id),

CONSTRAINT ck_messages\_\_author_type CHECK (author_type IN ( 'user',
'assistant',

'system', 'tool' )),

CONSTRAINT ck_messages\_\_role CHECK (role IN ( 'user', 'assistant',
'system', 'tool' )),

CONSTRAINT ck_messages\_\_status CHECK (status IN ( 'pending',
'streaming', 'completed', 'failed', 'cancelled', 'redacted' )) );

La foreign key a assistant_executions podrá agregarse después de crear
esa tabla para evitar dependencia circular.

## 43. Índices de messages

``` text
CREATE INDEX ix_messages__tenant_conversation_created
```

ON messages ( tenant_id, conversation_id, created_at ASC, id ASC );

## 44. assistant_executions

``` text
CREATE TABLE assistant_executions (
```

id uuid PRIMARY KEY, tenant_id uuid NOT NULL,

conversation_id uuid NOT NULL, user_message_id uuid NULL,
assistant_message_id uuid NULL, status varchar(40) NOT NULL, capability
varchar(40) NOT NULL, prompt_key varchar(160) NULL, prompt_version
varchar(40) NULL, prompt_checksum varchar(128) NULL, provider
varchar(80) NULL, model varchar(160) NULL, routing_policy_version
varchar(40) NULL, fallback_used boolean NOT NULL DEFAULT false,
input_tokens integer NULL, output_tokens integer NULL, cached_tokens
integer NULL, reasoning_tokens integer NULL, total_tokens integer NULL,
cost_amount numeric(18, 8) NULL, cost_currency char(3) NULL, latency_ms
integer NULL, failure_code varchar(120) NULL, failure_detail text NULL,
started_at timestamptz NULL, completed_at timestamptz NULL, created_at
timestamptz NOT NULL, updated_at timestamptz NOT NULL, version integer
NOT NULL DEFAULT 1,

CONSTRAINT fk_assistant_executions\_\_conversation_tenant FOREIGN KEY
(tenant_id, conversation_id) REFERENCES conversations (tenant_id, id),

CONSTRAINT ck_assistant_executions\_\_status CHECK (status IN (
'created', 'running', 'waiting_for_approval', 'completed', 'failed',
'cancelled', 'timed_out' )),

CONSTRAINT ck_assistant_executions\_\_capability CHECK (capability IN (
'direct_response', 'knowledge_query', 'tool_request',

'memory_operation', 'workflow' )),

CONSTRAINT ck_assistant_executions\_\_token_values CHECK (
COALESCE(input_tokens, 0) \>= 0 AND COALESCE(output_tokens, 0) \>= 0 AND
COALESCE(cached_tokens, 0) \>= 0 AND COALESCE(reasoning_tokens, 0) \>= 0
AND COALESCE(total_tokens, 0) \>= 0 ),

CONSTRAINT ck_assistant_executions\_\_cost CHECK (cost_amount IS NULL OR
cost_amount \>= 0),

CONSTRAINT ck_assistant_executions\_\_latency CHECK (latency_ms IS NULL
OR latency_ms \>= 0) );

## 45. Índices de assistant_executions

``` text
CREATE INDEX ix_assistant_executions__tenant_conversation_created
```

ON assistant_executions ( tenant_id, conversation_id, created_at DESC );

``` text
CREATE INDEX ix_assistant_executions__tenant_status
```

ON assistant_executions (tenant_id, status);

``` text
CREATE INDEX ix_assistant_executions__created_running
```

ON assistant_executions (created_at) WHERE status IN ('created',
'running', 'waiting_for_approval');

## 46. Relación de messages con executions

Después de crear ambas tablas:

``` text
ALTER TABLE messages
```

ADD CONSTRAINT fk_messages\_\_assistant_executions FOREIGN KEY
(execution_id) REFERENCES assistant_executions (id);

Las referencias user_message_id y assistant_message_id podrán agregarse
sin cascadas destructivas.

## 47. message_citations

``` text
CREATE TABLE message_citations (
```

id uuid PRIMARY KEY, tenant_id uuid NOT NULL, message_id uuid NOT NULL,
citation_key varchar(80) NOT NULL, document_id uuid NOT NULL,
document_version_id uuid NOT NULL, chunk_id uuid NOT NULL, title
varchar(300) NOT NULL, location varchar(300) NULL, excerpt text NOT
NULL, created_at timestamptz NOT NULL,

CONSTRAINT uq_message_citations\_\_message_key UNIQUE (message_id,
citation_key) );

Las foreign keys se agregarán después de crear tablas documentales.

## 48. user_feedback

``` text
CREATE TABLE user_feedback (
```

id uuid PRIMARY KEY, tenant_id uuid NOT NULL, execution_id uuid NOT
NULL, user_id uuid NOT NULL, rating smallint NULL, category varchar(40)
NOT NULL, comment text NULL, status varchar(32) NOT NULL DEFAULT
'active',

created_at timestamptz NOT NULL,

CONSTRAINT fk_user_feedback\_\_executions FOREIGN KEY (execution_id)
REFERENCES assistant_executions (id),

CONSTRAINT fk_user_feedback\_\_users FOREIGN KEY (user_id) REFERENCES
users (id),

CONSTRAINT ck_user_feedback\_\_rating CHECK (rating IS NULL OR rating
BETWEEN 1 AND 5),

CONSTRAINT ck_user_feedback\_\_category CHECK (category IN ( 'helpful',
'incorrect', 'incomplete', 'unsafe', 'irrelevant', 'citation_problem',
'tool_problem', 'other' )) );

## 49. Knowledge tables

documents

``` text
CREATE TABLE documents (
```

id uuid PRIMARY KEY, tenant_id uuid NOT NULL, title varchar(300) NOT
NULL, document_type varchar(32) NOT NULL, classification varchar(32) NOT
NULL, visibility varchar(32) NOT NULL DEFAULT 'tenant', owner_user_id
uuid NOT NULL, status varchar(32) NOT NULL, active_version_id uuid NULL,
metadata jsonb NOT NULL DEFAULT '{}'::jsonb, created_at timestamptz NOT
NULL, updated_at timestamptz NOT NULL, deleted_at timestamptz NULL,

version integer NOT NULL DEFAULT 1,

CONSTRAINT fk_documents\_\_tenants FOREIGN KEY (tenant_id) REFERENCES
tenants (id),

CONSTRAINT fk_documents\_\_users FOREIGN KEY (owner_user_id) REFERENCES
users (id),

CONSTRAINT uq_documents\_\_tenant_id_id UNIQUE (tenant_id, id),

CONSTRAINT ck_documents\_\_document_type CHECK (document_type IN (
'pdf', 'docx', 'markdown', 'text', 'html' )),

CONSTRAINT ck_documents\_\_classification CHECK (classification IN (
'public', 'internal', 'confidential', 'restricted' )),

CONSTRAINT ck_documents\_\_visibility CHECK (visibility IN ( 'tenant',
'restricted', 'private' )),

CONSTRAINT ck_documents\_\_status CHECK (status IN ( 'draft',
'processing', 'available', 'failed', 'archived', 'deleted' )) );

## 50. Índices de documents

``` text
CREATE INDEX ix_documents__tenant_status_updated
```

ON documents ( tenant_id, status, updated_at DESC, id DESC ) WHERE
deleted_at IS NULL;

``` text
CREATE INDEX ix_documents__tenant_classification
```

ON documents (tenant_id, classification);

``` text
CREATE INDEX ix_documents__metadata_gin
```

ON documents USING gin (metadata);

El índice JSONB solo deberá conservarse si las consultas reales lo
justifican.

## 51. document_versions

``` text
CREATE TABLE document_versions (
```

id uuid PRIMARY KEY, tenant_id uuid NOT NULL, document_id uuid NOT NULL,
version_number integer NOT NULL, status varchar(32) NOT NULL,
storage_key text NOT NULL, checksum_sha256 char(64) NOT NULL, mime_type
varchar(160) NOT NULL, size_bytes bigint NOT NULL, source_filename
varchar(500) NOT NULL, extraction_metadata jsonb NOT NULL DEFAULT
'{}'::jsonb, created_by uuid NOT NULL, created_at timestamptz NOT NULL,
processed_at timestamptz NULL,

CONSTRAINT fk_document_versions\_\_document_tenant FOREIGN KEY
(tenant_id, document_id) REFERENCES documents (tenant_id, id),

CONSTRAINT fk_document_versions\_\_users FOREIGN KEY (created_by)
REFERENCES users (id),

CONSTRAINT uq_document_versions\_\_document_number UNIQUE (document_id,
version_number),

CONSTRAINT uq_document_versions\_\_tenant_id_id UNIQUE (tenant_id, id),

CONSTRAINT ck_document_versions\_\_number CHECK (version_number \> 0),

CONSTRAINT ck_document_versions\_\_size CHECK (size_bytes \> 0),

CONSTRAINT ck_document_versions\_\_status CHECK (status IN ( 'uploaded',
'validated', 'queued', 'extracting', 'normalizing', 'chunking',
'embedding', 'indexing', 'ready', 'failed', 'cancelled' )) );

## 52. Active version foreign key

Después de crear document_versions :

``` text
ALTER TABLE documents
```

ADD CONSTRAINT fk_documents\_\_active_version FOREIGN KEY
(active_version_id) REFERENCES document_versions (id);

La aplicación deberá validar que la versión activa pertenece al mismo
documento y está en estado ready .

Podrá reforzarse mediante trigger si fuera necesario.

## 53. Inmutabilidad de versiones listas

Una versión en estado ready no deberá modificarse, salvo metadatos
operativos explícitamente permitidos.

Esta regla se protegerá principalmente en dominio y repositorio.

Podrá incorporarse un trigger si se detecta riesgo operativo.

## 54. document_access_roles

``` text
CREATE TABLE document_access_roles (
```

tenant_id uuid NOT NULL, document_id uuid NOT NULL, role_id uuid NOT
NULL,

PRIMARY KEY (document_id, role_id),

CONSTRAINT fk_document_access_roles\_\_documents FOREIGN KEY (tenant_id,
document_id) REFERENCES documents (tenant_id, id) ON DELETE CASCADE,

CONSTRAINT fk_document_access_roles\_\_roles FOREIGN KEY (role_id)
REFERENCES roles (id) ON DELETE CASCADE );

## 55. document_access_users

``` text
CREATE TABLE document_access_users (
```

tenant_id uuid NOT NULL, document_id uuid NOT NULL, user_id uuid NOT
NULL, access_type varchar(16) NOT NULL,

PRIMARY KEY (document_id, user_id),

CONSTRAINT fk_document_access_users\_\_documents FOREIGN KEY (tenant_id,
document_id) REFERENCES documents (tenant_id, id) ON DELETE CASCADE,

CONSTRAINT fk_document_access_users\_\_users FOREIGN KEY (user_id)
REFERENCES users (id),

CONSTRAINT ck_document_access_users\_\_access_type CHECK (access_type IN
('allow', 'deny')) );

Los deny explícitos tendrán prioridad en la política de aplicación.

## 56. ingestion_jobs

``` text
CREATE TABLE ingestion_jobs (
```

id uuid PRIMARY KEY, tenant_id uuid NOT NULL, document_id uuid NOT NULL,
document_version_id uuid NOT NULL, status varchar(32) NOT NULL,
current_stage varchar(32) NOT NULL, attempt integer NOT NULL DEFAULT 0,
max_attempts integer NOT NULL DEFAULT 5, execution_id uuid NULL,
error_code varchar(120) NULL, error_detail text NULL, created_at
timestamptz NOT NULL, started_at timestamptz NULL, completed_at
timestamptz NULL, updated_at timestamptz NOT NULL, version integer NOT
NULL DEFAULT 1,

CONSTRAINT fk_ingestion_jobs\_\_document_tenant FOREIGN KEY (tenant_id,
document_id) REFERENCES documents (tenant_id, id),

CONSTRAINT fk_ingestion_jobs\_\_version_tenant FOREIGN KEY (tenant_id,
document_version_id) REFERENCES document_versions (tenant_id, id),

CONSTRAINT ck_ingestion_jobs\_\_status CHECK (status IN ( 'pending',
'running', 'succeeded', 'failed', 'retry_scheduled', 'dead_letter',
'cancelled' )),

CONSTRAINT ck_ingestion_jobs\_\_stage CHECK (current_stage IN (
'validation', 'storage', 'extraction', 'normalization', 'chunking',
'embedding', 'indexing', 'completion' )),

CONSTRAINT ck_ingestion_jobs\_\_attempt CHECK ( attempt \>= 0 AND
max_attempts \> 0 AND attempt \<= max_attempts ) );

## 57. Índices de ingestion_jobs

``` text
CREATE INDEX ix_ingestion_jobs__status_created
```

ON ingestion_jobs (status, created_at) WHERE status IN ('pending',
'retry_scheduled');

``` text
CREATE INDEX ix_ingestion_jobs__tenant_version
```

ON ingestion_jobs (tenant_id, document_version_id);

## 58. Evitar jobs simultáneos por versión

Podrá utilizarse un índice único parcial:

``` text
CREATE UNIQUE INDEX uq_ingestion_jobs__active_version
```

ON ingestion_jobs (document_version_id) WHERE status IN ('pending',
'running', 'retry_scheduled');

Esto evita múltiples jobs activos para una misma versión.

## 59. chunks

``` text
CREATE TABLE chunks (
```

id uuid PRIMARY KEY, tenant_id uuid NOT NULL, document_id uuid NOT NULL,
document_version_id uuid NOT NULL, sequence integer NOT NULL, content
text NOT NULL, content_hash char(64) NOT NULL, token_count integer NOT
NULL, page_number integer NULL, section_title varchar(500) NULL,
start_offset integer NULL, end_offset integer NULL, metadata jsonb NOT
NULL DEFAULT '{}'::jsonb, search_vector tsvector NULL, status
varchar(32) NOT NULL DEFAULT 'active', created_at timestamptz NOT NULL,

CONSTRAINT fk_chunks\_\_document_tenant FOREIGN KEY (tenant_id,
document_id) REFERENCES documents (tenant_id, id),

CONSTRAINT fk_chunks\_\_version_tenant FOREIGN KEY (tenant_id,
document_version_id) REFERENCES document_versions (tenant_id, id),

CONSTRAINT uq_chunks\_\_version_sequence UNIQUE (document_version_id,
sequence),

CONSTRAINT uq_chunks\_\_tenant_id_id

UNIQUE (tenant_id, id),

CONSTRAINT ck_chunks\_\_sequence CHECK (sequence \>= 0),

CONSTRAINT ck_chunks\_\_token_count CHECK (token_count \> 0),

CONSTRAINT ck_chunks\_\_status CHECK (status IN ('active', 'superseded',
'deleted')),

CONSTRAINT ck_chunks\_\_offsets CHECK ( start_offset IS NULL OR
end_offset IS NULL OR end_offset \>= start_offset ) );

## 60. Full-text search vector

El campo search_vector podrá calcularse mediante generated column:

search_vector tsvector GENERATED ALWAYS AS ( to_tsvector( 'spanish',
coalesce(section_title, '') \|\|' ' \|\| content ) ) STORED

La configuración exacta deberá evaluar documentos en español e inglés.

## 61. Estrategia multilenguaje full-text

La primera versión podrá:

-   usar spanish para documentos en español;
-   almacenar language en chunk o documento;
-   generar vectores según idioma mediante aplicación;
-   utilizar simple cuando existan códigos o términos técnicos.

No se mezclará ciegamente toda la información en una sola configuración.

## 62. Índice full-text

``` text
CREATE INDEX ix_chunks__search_vector
```

ON chunks USING gin (search_vector);

Las consultas siempre deberán combinarse con filtro por tenant y estado.

## 63. Índices relacionales de chunks

``` text
CREATE INDEX ix_chunks__tenant_version_sequence
```

ON chunks ( tenant_id, document_version_id, sequence );

``` text
CREATE INDEX ix_chunks__tenant_document
```

ON chunks (tenant_id, document_id);

``` text
CREATE INDEX ix_chunks__content_hash
```

ON chunks (tenant_id, content_hash);

## 64. Extensión pgvector

Migración:

``` text
CREATE EXTENSION IF NOT EXISTS vector;
```

La disponibilidad deberá validarse en:

-   development;
-   CI;
-   staging;
-   production.

## 65. embedding_records

La dimensión depende del modelo.

La primera implementación deberá elegir una dimensión concreta mediante
configuración y ADR.

Ejemplo conceptual con dimensión 1536:

``` text
CREATE TABLE embedding_records (
```

id uuid PRIMARY KEY, tenant_id uuid NOT NULL, chunk_id uuid NOT NULL,
provider varchar(80) NOT NULL, model varchar(160) NOT NULL, dimension
integer NOT NULL, embedding_version varchar(40) NOT NULL, vector
vector(1536) NOT NULL, status varchar(32) NOT NULL DEFAULT 'active',
created_at timestamptz NOT NULL,

CONSTRAINT fk_embedding_records\_\_chunk_tenant FOREIGN KEY (tenant_id,
chunk_id) REFERENCES chunks (tenant_id, id) ON DELETE CASCADE,

CONSTRAINT uq_embedding_records\_\_chunk_model_version UNIQUE (
chunk_id, provider, model, embedding_version ),

CONSTRAINT ck_embedding_records\_\_dimension CHECK (dimension = 1536),

CONSTRAINT ck_embedding_records\_\_status CHECK (status IN ('active',
'superseded', 'failed')) );

## 66. Restricción de dimensión

PostgreSQL requiere una dimensión fija por columna vectorial.

Si en el futuro se utilizan modelos con dimensiones diferentes, se
evaluará:

-   tablas separadas por familia;
-   columnas separadas;
-   reindexación completa;
-   almacenamiento alternativo.

No se diseñará una abstracción prematura para todas las dimensiones
posibles.

## 67. Índice vectorial inicial

Durante las primeras pruebas podrá utilizarse búsqueda exacta sin índice
aproximado.

Cuando el volumen lo requiera:

``` text
CREATE INDEX ix_embedding_records__vector_hnsw
```

ON embedding_records USING hnsw (vector vector_cosine_ops);

## 68. Búsqueda vectorial tenant-aware

Ejemplo conceptual:

SELECT er.chunk_id, 1 - (er.vector \<=\> :query_vector) AS similarity
FROM embedding_records er JOIN chunks c ON c.id = er.chunk_id WHERE
er.tenant_id = :tenant_id AND er.status = 'active' AND c.status =
'active' ORDER BY er.vector \<=\> :query_vector LIMIT :limit;

RLS seguirá aplicando como defensa adicional.

## 69. Importancia del filtro tenant en ANN

Los índices aproximados pueden evaluar candidatos globales antes de
aplicar filtros.

Por ello deberá medirse:

-   precisión;
-   latencia;
-   distribución por tenant;
-   costo de filtros.

Si el volumen multi-tenant genera problemas, se evaluarán:

-   particiones;
-   índices parciales;
-   recuperación de más candidatos;
-   almacenes separados;
-   vector database externa.

## 70. Retrieval tables

retrieval_runs

``` text
CREATE TABLE retrieval_runs (
```

id uuid PRIMARY KEY, tenant_id uuid NOT NULL, execution_id uuid NOT
NULL, original_query text NOT NULL, normalized_query text NOT NULL,
query_hash char(64) NOT NULL, strategy varchar(32) NOT NULL, filters
jsonb NOT NULL DEFAULT '{}'::jsonb, status varchar(32) NOT NULL,
candidate_count integer NOT NULL DEFAULT 0, selected_count integer NOT
NULL DEFAULT 0, context_token_count integer NOT NULL DEFAULT 0,
sufficiency varchar(32) NULL, started_at timestamptz NOT NULL,
completed_at timestamptz NULL, failure_code varchar(120) NULL,

CONSTRAINT fk_retrieval_runs\_\_executions FOREIGN KEY (execution_id)
REFERENCES assistant_executions (id),

CONSTRAINT ck_retrieval_runs\_\_strategy CHECK (strategy IN ( 'vector',
'full_text', 'hybrid', 'hybrid_reranked' )),

CONSTRAINT ck_retrieval_runs\_\_status CHECK (status IN ( 'running',
'completed', 'failed' )),

CONSTRAINT ck_retrieval_runs\_\_counts CHECK ( candidate_count \>= 0 AND
selected_count \>= 0 AND context_token_count \>= 0 ) );

## 71. retrieval_candidates

La persistencia completa podrá estar deshabilitada por defecto en
producción debido al volumen.

Cuando se habilite:

``` text
CREATE TABLE retrieval_candidates (
```

id uuid PRIMARY KEY, tenant_id uuid NOT NULL, retrieval_run_id uuid NOT
NULL, chunk_id uuid NOT NULL, source_strategy varchar(32) NOT NULL,
original_score double precision NULL, normalized_score double precision
NULL, rank integer NOT NULL, selected boolean NOT NULL DEFAULT false,

created_at timestamptz NOT NULL );

Su retención deberá ser corta.

## 72. Citation foreign keys

Después de crear documentos, versions y chunks:

``` text
ALTER TABLE message_citations
```

ADD CONSTRAINT fk_message_citations\_\_documents FOREIGN KEY (tenant_id,
document_id) REFERENCES documents (tenant_id, id);

``` text
ALTER TABLE message_citations
```

ADD CONSTRAINT fk_message_citations\_\_versions FOREIGN KEY (tenant_id,
document_version_id) REFERENCES document_versions (tenant_id, id);

``` text
ALTER TABLE message_citations
```

ADD CONSTRAINT fk_message_citations\_\_chunks FOREIGN KEY (tenant_id,
chunk_id) REFERENCES chunks (tenant_id, id);

## 73. Tools tables

tool_definitions

``` text
CREATE TABLE tool_definitions (
```

id uuid PRIMARY KEY, tenant_id uuid NULL, key varchar(160) NOT NULL,
display_name varchar(200) NOT NULL, description text NOT NULL,
classification varchar(32) NOT NULL, status varchar(32) NOT NULL,
active_version_id uuid NULL, created_at timestamptz NOT NULL, updated_at
timestamptz NOT NULL, version integer NOT NULL DEFAULT 1,

CONSTRAINT ck_tool_definitions\_\_classification CHECK (classification
IN ( 'public', 'internal', 'confidential', 'restricted' )),

CONSTRAINT ck_tool_definitions\_\_status CHECK (status IN ( 'draft',
'active', 'disabled', 'deprecated', 'retired' )) );

tenant_id NULL representará una definición global.

La unicidad deberá considerar herramientas globales y de tenant.

## 74. Índices de tool definitions

``` text
CREATE UNIQUE INDEX uq_tool_definitions__global_key
```

ON tool_definitions (key) WHERE tenant_id IS NULL;

``` text
CREATE UNIQUE INDEX uq_tool_definitions__tenant_key
```

ON tool_definitions (tenant_id, key) WHERE tenant_id IS NOT NULL;

## 75. tool_versions

``` text
CREATE TABLE tool_versions (
```

id uuid PRIMARY KEY, tool_id uuid NOT NULL, version_number varchar(40)
NOT NULL, input_schema jsonb NOT NULL,

output_schema jsonb NOT NULL, risk_level varchar(16) NOT NULL,
required_permissions jsonb NOT NULL, approval_policy_key varchar(160)
NULL, timeout_seconds integer NOT NULL, retry_policy jsonb NOT NULL
DEFAULT '{}'::jsonb, idempotency_policy jsonb NOT NULL DEFAULT
'{}'::jsonb, adapter_key varchar(160) NOT NULL, status varchar(32) NOT
NULL, checksum char(64) NOT NULL, created_at timestamptz NOT NULL,

CONSTRAINT fk_tool_versions\_\_definitions FOREIGN KEY (tool_id)
REFERENCES tool_definitions (id),

CONSTRAINT uq_tool_versions\_\_tool_version UNIQUE (tool_id,
version_number),

CONSTRAINT ck_tool_versions\_\_risk_level CHECK (risk_level IN (
'level_0', 'level_1', 'level_2', 'level_3', 'level_4' )),

CONSTRAINT ck_tool_versions\_\_timeout CHECK (timeout_seconds \> 0),

CONSTRAINT ck_tool_versions\_\_status CHECK (status IN ( 'draft',
'active', 'deprecated', 'retired' )) );

## 76. Tool schema validation

PostgreSQL almacenará JSON Schema, pero la validación profunda se
ejecutará en aplicación.

La base de datos protegerá únicamente:

-   presencia;
-   tipo JSONB;
-   checksum;
-   estado;
-   relación.

## 77. tool_permissions

Podrán almacenarse normalizadas si se requiere consulta eficiente.

Inicialmente podrán permanecer dentro de required_permissions como
JSONB, porque son parte inmutable de la versión de la tool.

La autorización usará el contrato cargado y validado.

## 78. tool_executions

``` text
CREATE TABLE tool_executions (
```

id uuid PRIMARY KEY, tenant_id uuid NOT NULL, assistant_execution_id
uuid NOT NULL, tool_id uuid NOT NULL, tool_version_id uuid NOT NULL,
requested_by_type varchar(32) NOT NULL, requested_by_id uuid NULL,
status varchar(40) NOT NULL, sanitized_arguments jsonb NOT NULL,
encrypted_arguments bytea NULL, arguments_hash char(64) NOT NULL,
risk_level varchar(16) NOT NULL, approval_request_id uuid NULL,
idempotency_key varchar(255) NULL, result jsonb NULL, failure_code
varchar(120) NULL, failure_detail text NULL, started_at timestamptz
NULL, completed_at timestamptz NULL, created_at timestamptz NOT NULL,
updated_at timestamptz NOT NULL, version integer NOT NULL DEFAULT 1,

CONSTRAINT fk_tool_executions\_\_assistant_execution FOREIGN KEY
(assistant_execution_id) REFERENCES assistant_executions (id),

CONSTRAINT fk_tool_executions\_\_tool FOREIGN KEY (tool_id) REFERENCES
tool_definitions (id),

CONSTRAINT fk_tool_executions\_\_tool_version FOREIGN KEY
(tool_version_id) REFERENCES tool_versions (id),

CONSTRAINT ck_tool_executions\_\_status CHECK (status IN ( 'requested',
'validating', 'authorization_denied', 'approval_required', 'approved',
'running', 'succeeded', 'failed', 'timed_out', 'cancelled',
'duplicate_prevented' )),

CONSTRAINT ck_tool_executions\_\_risk CHECK (risk_level IN ( 'level_0',
'level_1', 'level_2', 'level_3', 'level_4' )) );

## 79. Idempotencia de tool executions

``` text
CREATE UNIQUE INDEX uq_tool_executions__tenant_idempotency
```

ON tool_executions (tenant_id, idempotency_key) WHERE idempotency_key IS
NOT NULL;

El scope podrá refinarse por tool si existe necesidad.

## 80. Índices de tool executions

``` text
CREATE INDEX ix_tool_executions__tenant_status_created
```

ON tool_executions ( tenant_id, status, created_at DESC );

``` text
CREATE INDEX ix_tool_executions__assistant_execution
```

ON tool_executions (assistant_execution_id);

## 81. tool_execution_attempts

``` text
CREATE TABLE tool_execution_attempts (
```

id uuid PRIMARY KEY, tenant_id uuid NOT NULL, tool_execution_id uuid NOT
NULL, attempt_number integer NOT NULL, status varchar(32) NOT NULL,
retryable boolean NOT NULL DEFAULT false, error_code varchar(120) NULL,
provider_reference varchar(500) NULL, started_at timestamptz NOT NULL,
completed_at timestamptz NULL,

CONSTRAINT fk_tool_execution_attempts\_\_execution FOREIGN KEY
(tool_execution_id) REFERENCES tool_executions (id) ON DELETE CASCADE,

CONSTRAINT uq_tool_execution_attempts\_\_number UNIQUE
(tool_execution_id, attempt_number),

CONSTRAINT ck_tool_execution_attempts\_\_attempt CHECK (attempt_number
\> 0) );

## 82. Approvals tables

approval_requests

``` text
CREATE TABLE approval_requests (
```

id uuid PRIMARY KEY, tenant_id uuid NOT NULL, subject_type varchar(64)
NOT NULL, subject_id uuid NOT NULL, requested_by_type varchar(32) NOT
NULL, requested_by_id uuid NULL, status varchar(32) NOT NULL, risk_level
varchar(16) NOT NULL, summary text NOT NULL, arguments_hash char(64) NOT
NULL, policy_key varchar(160) NOT NULL, policy_version varchar(40) NOT
NULL, created_at timestamptz NOT NULL, expires_at timestamptz NOT NULL,
decided_at timestamptz NULL, executed_at timestamptz NULL, updated_at
timestamptz NOT NULL, version integer NOT NULL DEFAULT 1,

CONSTRAINT ck_approval_requests\_\_status CHECK (status IN ( 'pending',
'approved', 'rejected', 'expired', 'cancelled', 'executed',
'execution_failed' )),

CONSTRAINT ck_approval_requests\_\_risk CHECK (risk_level IN (
'level_0', 'level_1', 'level_2', 'level_3', 'level_4' )),

CONSTRAINT ck_approval_requests\_\_expiration

CHECK (expires_at \> created_at) );

## 83. approval_eligible_approvers

``` text
CREATE TABLE approval_eligible_approvers (
```

approval_request_id uuid NOT NULL, tenant_id uuid NOT NULL, user_id uuid
NOT NULL,

PRIMARY KEY (approval_request_id, user_id),

CONSTRAINT fk_approval_eligible_approvers\_\_request FOREIGN KEY
(approval_request_id) REFERENCES approval_requests (id) ON DELETE
CASCADE,

CONSTRAINT fk_approval_eligible_approvers\_\_user FOREIGN KEY (user_id)
REFERENCES users (id) );

## 84. approval_decisions

``` text
CREATE TABLE approval_decisions (
```

id uuid PRIMARY KEY, tenant_id uuid NOT NULL, approval_request_id uuid
NOT NULL, approver_user_id uuid NOT NULL, decision varchar(16) NOT NULL,
reason text NULL, metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
decided_at timestamptz NOT NULL,

CONSTRAINT fk_approval_decisions\_\_request FOREIGN KEY
(approval_request_id) REFERENCES approval_requests (id),

CONSTRAINT fk_approval_decisions\_\_user FOREIGN KEY (approver_user_id)

REFERENCES users (id),

CONSTRAINT uq_approval_decisions\_\_request UNIQUE
(approval_request_id),

CONSTRAINT ck_approval_decisions\_\_decision CHECK (decision IN
('approve', 'reject')) );

## 85. Índices de approvals

``` text
CREATE INDEX ix_approval_requests__tenant_pending_expires
```

ON approval_requests ( tenant_id, expires_at, created_at DESC ) WHERE
status = 'pending';

``` text
CREATE INDEX ix_approval_requests__subject
```

ON approval_requests ( tenant_id, subject_type, subject_id );

## 86. Evitar múltiples approvals activas

Para una tool execution podrá aplicarse:

``` text
CREATE UNIQUE INDEX uq_approval_requests__pending_subject
```

ON approval_requests ( tenant_id, subject_type, subject_id ) WHERE
status = 'pending';

## 87. Relación tool execution approval

Después de crear approvals:

``` text
ALTER TABLE tool_executions
```

ADD CONSTRAINT fk_tool_executions\_\_approval_request FOREIGN KEY
(approval_request_id) REFERENCES approval_requests (id);

## 88. Memory tables

memories

``` text
CREATE TABLE memories (
```

id uuid PRIMARY KEY, tenant_id uuid NOT NULL, owner_user_id uuid NOT
NULL, memory_type varchar(40) NOT NULL, content text NOT NULL,
content_hash char(64) NOT NULL, status varchar(32) NOT NULL, confidence
varchar(16) NOT NULL, source_type varchar(40) NOT NULL,
source_reference_id uuid NULL, classification varchar(32) NOT NULL,
created_at timestamptz NOT NULL, confirmed_at timestamptz NULL,
expires_at timestamptz NULL, updated_at timestamptz NOT NULL, deleted_at
timestamptz NULL, version integer NOT NULL DEFAULT 1,

CONSTRAINT fk_memories\_\_users FOREIGN KEY (owner_user_id) REFERENCES
users (id),

CONSTRAINT ck_memories\_\_type CHECK (memory_type IN (
'user_preference', 'working_context', 'confirmed_fact' )),

CONSTRAINT ck_memories\_\_status CHECK (status IN ( 'candidate',
'confirmed', 'active', 'expired', 'corrected', 'deleted', 'rejected' )),

CONSTRAINT ck_memories\_\_confidence CHECK (confidence IN ( 'low',
'medium', 'high', 'verified' )),

CONSTRAINT ck_memories\_\_classification CHECK (classification IN (
'public', 'internal', 'confidential', 'restricted' )) );

## 89. Índices de memories

``` text
CREATE INDEX ix_memories__tenant_user_status
```

ON memories ( tenant_id, owner_user_id, status, updated_at DESC );

``` text
CREATE INDEX ix_memories__tenant_user_hash
```

ON memories ( tenant_id, owner_user_id,

content_hash );

## 90. memory_revisions

``` text
CREATE TABLE memory_revisions (
```

id uuid PRIMARY KEY, tenant_id uuid NOT NULL, memory_id uuid NOT NULL,
revision_number integer NOT NULL, previous_content text NOT NULL,
new_content text NOT NULL, changed_by uuid NOT NULL, reason text NOT
NULL, source_type varchar(40) NOT NULL, source_reference_id uuid NULL,
created_at timestamptz NOT NULL,

CONSTRAINT fk_memory_revisions\_\_memory FOREIGN KEY (memory_id)
REFERENCES memories (id),

CONSTRAINT fk_memory_revisions\_\_user FOREIGN KEY (changed_by)
REFERENCES users (id),

CONSTRAINT uq_memory_revisions\_\_number UNIQUE (memory_id,
revision_number),

CONSTRAINT ck_memory_revisions\_\_number CHECK (revision_number \> 0) );

## 91. Audit table

``` text
CREATE TABLE audit_events (
```

id uuid PRIMARY KEY, tenant_id uuid NULL, actor_type varchar(32) NOT
NULL, actor_id uuid NULL,

action varchar(160) NOT NULL, resource_type varchar(100) NOT NULL,
resource_id uuid NULL, result varchar(24) NOT NULL, correlation_id
varchar(160) NULL, execution_id uuid NULL, request_id varchar(160) NULL,
sanitized_metadata jsonb NOT NULL DEFAULT '{}'::jsonb, occurred_at
timestamptz NOT NULL, integrity_reference varchar(255) NULL,

CONSTRAINT ck_audit_events\_\_actor_type CHECK (actor_type IN ( 'user',
'service', 'system', 'mcp_client', 'worker' )),

CONSTRAINT ck_audit_events\_\_result CHECK (result IN ( 'success',
'failure', 'denied', 'partial' )) );

## 92. Índices de audit

``` text
CREATE INDEX ix_audit_events__tenant_occurred
```

ON audit_events ( tenant_id, occurred_at DESC, id DESC );

``` text
CREATE INDEX ix_audit_events__resource
```

ON audit_events ( tenant_id, resource_type, resource_id, occurred_at
DESC

);

``` text
CREATE INDEX ix_audit_events__correlation
```

ON audit_events (correlation_id) WHERE correlation_id IS NOT NULL;

``` text
CREATE INDEX ix_audit_events__action
```

ON audit_events ( tenant_id, action, occurred_at DESC );

## 93. Inmutabilidad de auditoría

El rol de aplicación tendrá:

-   INSERT;
-   SELECT limitado;
-   no UPDATE;
-   no DELETE.

La retención será gestionada mediante procesos administrativos
separados.

## 94. Evaluation tables

evaluation_datasets

``` text
CREATE TABLE evaluation_datasets (
```

id uuid PRIMARY KEY, key varchar(160) NOT NULL, version varchar(40) NOT
NULL, purpose text NOT NULL, status varchar(32) NOT NULL, language
varchar(8) NOT NULL, checksum char(64) NOT NULL, case_count integer NOT
NULL DEFAULT 0, created_at timestamptz NOT NULL, published_at
timestamptz NULL,

CONSTRAINT uq_evaluation_datasets\_\_key_version UNIQUE (key, version),

CONSTRAINT ck_evaluation_datasets\_\_status CHECK (status IN ( 'draft',
'validation', 'published', 'deprecated', 'archived' )),

CONSTRAINT ck_evaluation_datasets\_\_case_count CHECK (case_count \>= 0)
);

## 95. evaluation_cases

``` text
CREATE TABLE evaluation_cases (
```

id uuid PRIMARY KEY, dataset_id uuid NOT NULL, category varchar(100) NOT
NULL, input jsonb NOT NULL, expected_behavior jsonb NOT NULL,
reference_answer text NULL, reference_sources jsonb NOT NULL DEFAULT
'\[\]'::jsonb, tags jsonb NOT NULL DEFAULT '\[\]'::jsonb, severity
varchar(16) NOT NULL, metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
created_at timestamptz NOT NULL,

CONSTRAINT fk_evaluation_cases\_\_dataset FOREIGN KEY (dataset_id)
REFERENCES evaluation_datasets (id) ON DELETE CASCADE,

CONSTRAINT ck_evaluation_cases\_\_severity CHECK (severity IN ( 'low',
'medium', 'high', 'critical' )) );

## 96. evaluation_runs

``` text
CREATE TABLE evaluation_runs (
```

id uuid PRIMARY KEY, dataset_id uuid NOT NULL, dataset_version
varchar(40) NOT NULL, system_version varchar(80) NOT NULL,
prompt_versions jsonb NOT NULL, model_configuration jsonb NOT NULL,
status varchar(32) NOT NULL, cost_amount numeric(18, 8) NULL,
cost_currency char(3) NULL, summary jsonb NOT NULL DEFAULT '{}'::jsonb,
started_at timestamptz NULL, completed_at timestamptz NULL, created_at
timestamptz NOT NULL, version integer NOT NULL DEFAULT 1,

CONSTRAINT fk_evaluation_runs\_\_dataset FOREIGN KEY (dataset_id)
REFERENCES evaluation_datasets (id),

CONSTRAINT ck_evaluation_runs\_\_status CHECK (status IN ( 'created',
'running', 'completed', 'failed', 'cancelled' )),

CONSTRAINT ck_evaluation_runs\_\_cost CHECK (cost_amount IS NULL OR
cost_amount \>= 0) );

## 97. evaluation_results

``` text
CREATE TABLE evaluation_results (
```

id uuid PRIMARY KEY, evaluation_run_id uuid NOT NULL, evaluation_case_id
uuid NOT NULL, status varchar(32) NOT NULL,

output jsonb NULL, metric_values jsonb NOT NULL DEFAULT '{}'::jsonb,
evaluator_versions jsonb NOT NULL DEFAULT '{}'::jsonb, failure_category
varchar(120) NULL, execution_id uuid NULL, review_status varchar(32) NOT
NULL DEFAULT 'not_reviewed', created_at timestamptz NOT NULL,

CONSTRAINT fk_evaluation_results\_\_run FOREIGN KEY (evaluation_run_id)
REFERENCES evaluation_runs (id) ON DELETE CASCADE,

CONSTRAINT fk_evaluation_results\_\_case FOREIGN KEY
(evaluation_case_id) REFERENCES evaluation_cases (id),

CONSTRAINT uq_evaluation_results\_\_run_case UNIQUE (evaluation_run_id,
evaluation_case_id) );

## 98. Outbox pattern

Se implementará Transactional Outbox cuando existan consumidores
asíncronos relevantes.

Tabla:

``` text
CREATE TABLE outbox_events (
```

id uuid PRIMARY KEY, tenant_id uuid NULL, event_type varchar(200) NOT
NULL, event_version integer NOT NULL, aggregate_type varchar(100) NOT
NULL, aggregate_id uuid NOT NULL, correlation_id varchar(160) NULL,
causation_id varchar(160) NULL, payload jsonb NOT NULL, status
varchar(32) NOT NULL DEFAULT 'pending', attempt integer NOT NULL DEFAULT
0, available_at timestamptz NOT NULL, created_at timestamptz NOT NULL,
published_at timestamptz NULL, last_error text NULL,

CONSTRAINT ck_outbox_events\_\_status CHECK (status IN ( 'pending',
'publishing', 'published', 'failed', 'dead_letter' )),

CONSTRAINT ck_outbox_events\_\_attempt CHECK (attempt \>= 0) );

## 99. Índices de outbox

``` text
CREATE INDEX ix_outbox_events__pending_available
```

ON outbox_events ( available_at, created_at ) WHERE status IN
('pending', 'failed');

## 100. Flujo de outbox

Dentro de una misma transacción:

## 1. modificar agregado;

## 2. insertar evento en outbox;

## 3. commit.

Después:

## 1. worker reclama eventos;

## 2. publica;

## 3. marca como publicado;

## 4. reintenta fallos;

## 5. envía a dead letter cuando corresponde.

## 101. Reclamo seguro de outbox

Podrá utilizarse:

``` text
SELECT id
```

FROM outbox_events WHERE status IN ('pending', 'failed') AND
available_at \<= now() ORDER BY created_at FOR UPDATE SKIP LOCKED LIMIT
:batch_size;

Esto permite múltiples workers.

## 102. Inbox pattern

Cuando se consuman eventos externos o mensajes que puedan duplicarse se
utilizará una inbox.

``` text
CREATE TABLE inbox_messages (
```

message_id varchar(200) PRIMARY KEY, consumer_name varchar(160) NOT
NULL, received_at timestamptz NOT NULL, processed_at timestamptz NULL,
status varchar(32) NOT NULL, payload_hash char(64) NOT NULL, last_error
text NULL );

## 103. Idempotency records HTTP

``` text
CREATE TABLE idempotency_records (
```

id uuid PRIMARY KEY, tenant_id uuid NOT NULL, scope varchar(160) NOT
NULL, idempotency_key varchar(255) NOT NULL, request_hash char(64) NOT
NULL, status varchar(32) NOT NULL, response_status integer NULL,
response_body jsonb NULL,

resource_type varchar(100) NULL, resource_id uuid NULL, created_at
timestamptz NOT NULL, completed_at timestamptz NULL, expires_at
timestamptz NOT NULL,

CONSTRAINT uq_idempotency_records\_\_tenant_scope_key UNIQUE (tenant_id,
scope, idempotency_key),

CONSTRAINT ck_idempotency_records\_\_status CHECK (status IN (
'processing', 'completed', 'failed' )),

CONSTRAINT ck_idempotency_records\_\_expiration CHECK (expires_at \>
created_at) );

## 104. Idempotency flow

## 1. calcular hash del request;

## 2. intentar insertar registro;

## 3. si ya existe:

## 4. mismo hash y completado: devolver respuesta;

## 5. mismo hash y procesando: informar conflicto temporal;

## 6. hash diferente: IDEMPOTENCY_KEY_CONFLICT ;

## 7. ejecutar operación;

## 8. persistir respuesta segura;

## 9. marcar completado.

## 105. Advisory locks

PostgreSQL advisory locks podrán utilizarse para coordinación puntual.

Ejemplos:

-   activar versión documental;

-   reindexación;

-   tareas administrativas;

-   procesos únicos.

No sustituirán a constraints ni idempotencia.

## 106. Transacciones

La política predeterminada será:

READ COMMITTED

Se utilizarán niveles superiores solo cuando exista una razón concreta.

## 107. No mantener transacciones abiertas

No se mantendrán transacciones abiertas mientras se ejecutan:

-   llamadas LLM;
-   embeddings;
-   object storage;
-   tools externas;
-   webhooks;
-   notificaciones.

El flujo se dividirá en etapas persistentes.

## 108. Patrón para llamadas externas

Persist request state ↓ Commit ↓ Execute external dependency ↓ Open new
transaction ↓ Persist result

## 109. Locking de approvals

La decisión de una aprobación deberá:

## 1. seleccionar approval con lock;

## 2. validar status pending ;

## 3. validar expiración;

## 4. validar approver;

## 5. insertar decisión;

## 6. actualizar status;

## 7. commit.

Podrá utilizar:

``` text
SELECT ...
```

FOR UPDATE;

## 110. Locking de tool execution

Antes de pasar una tool a running :

-   bloquear fila;
-   validar estado;
-   validar approval;
-   validar hash;
-   validar idempotencia;
-   cambiar a running;
-   commit.

Después se ejecutará la integración externa.

## 111. Cursor pagination

Los cursores deberán representar un orden estable.

Ejemplo para conversaciones:

updated_at DESC, id DESC

El cursor podrá codificar:

``` text
{
"updated_at": "2026-07-20T20:00:00Z",
"id": "uuid"
}
```

Se firmará o codificará de manera que el cliente no dependa de su
contenido.

## 112. Query de cursor

Conceptualmente:

WHERE tenant_id = :tenant_id AND ( updated_at \< :cursor_updated_at OR (
updated_at = :cursor_updated_at AND id \< :cursor_id ) ) ORDER BY
updated_at DESC, id DESC LIMIT :limit_plus_one;

## 113. SQLAlchemy Base

Ejemplo:

``` text
from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
```

pass

``` text
class TimestampMixin:
```

created_at: Mapped\[datetime\] = mapped_column( DateTime(timezone=True),

nullable=False, ) updated_at: Mapped\[datetime\] = mapped_column(
DateTime(timezone=True), nullable=False, )

``` text
class VersionMixin:
```

version: Mapped\[int\] = mapped_column( Integer, nullable=False,
default=1, )

## 114. SQLAlchemy model example

``` text
from uuid import UUID

from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column

class ConversationModel(Base, TimestampMixin, VersionMixin):
```

**tablename** = "conversations"

id: Mapped\[UUID\] = mapped_column( PGUUID(as_uuid=True),
primary_key=True, )

tenant_id: Mapped\[UUID\] = mapped_column( PGUUID(as_uuid=True),
ForeignKey("tenants.id"), nullable=False, index=True, )

owner_user_id: Mapped\[UUID\] = mapped_column( PGUUID(as_uuid=True),
ForeignKey("users.id"), nullable=False, )

title: Mapped\[str\] = mapped_column( String(160), nullable=False, )

status: Mapped\[str\] = mapped_column( String(32), nullable=False, )

language: Mapped\[str\] = mapped_column( String(8), nullable=False,
default="es", )

## 115. ORM models no son entidades

Los modelos SQLAlchemy:

-   representan persistencia;
-   no contienen toda la lógica de dominio;
-   no se retornan desde API;
-   no se comparten con frontend;
-   no se entregan al Model Gateway.

## 116. Repository query example

``` text
from sqlalchemy import select

async def get_by_id(
```

self, tenant_id: TenantId, conversation_id: ConversationId, ) -\>
Conversation \| None: statement = ( select(ConversationModel) .where(
ConversationModel.id == conversation_id.value,
ConversationModel.tenant_id == tenant_id.value,

) )

result = await self.\_session.execute(statement) model =
result.scalar_one_or_none()

``` text
return self._mapper.to_domain(model) if model else None
```

Aunque RLS esté habilitado, el filtro explícito sigue siendo
obligatorio.

## 117. Unit of Work

Ejemplo conceptual:

``` text
class SqlAlchemyUnitOfWork:
async def __aenter__(self):
```

self.session = self.\_session_factory()

``` text
await self._set_tenant_context()
```

self.conversations = SqlConversationRepository(self.session)
self.documents = SqlDocumentRepository(self.session)

``` text
return self

async def commit(self):
await self.session.commit()

async def rollback(self):
await self.session.rollback()

async def __aexit__(self, exc_type, exc, tb):
```

if exc:

``` text
await self.rollback()
await self.session.close()
```

## 118. Configuración de tenant con SQLAlchemy

``` text
from sqlalchemy import text

async def set_tenant_context(
```

session,

tenant_id: str, user_id: str, ) -\> None:

``` text
await session.execute(
```

text("SET LOCAL app.tenant_id = :tenant_id"),

``` text
{"tenant_id": tenant_id},
```

)

``` text
await session.execute(
```

text("SET LOCAL app.user_id = :user_id"),

``` text
{"user_id": user_id},
```

)

El soporte de parámetros en SET LOCAL deberá probarse; si el driver lo
limita, se usará set_config .

## 119. Opción segura con set_config

``` text
SELECT set_config('app.tenant_id', :tenant_id, true);
SELECT set_config('app.user_id', :user_id, true);
```

El tercer argumento true hace la configuración local a la transacción.

## 120. Alembic standards

Cada migración deberá:

-   tener propósito claro;
-   ser pequeña;
-   ser revisable;
-   tener downgrade cuando sea seguro;
-   evitar operaciones destructivas directas;
-   incluir índices;
-   incluir constraints;
-   probarse desde base vacía;
-   probarse sobre una base previa representativa.

## 121. Naming de migraciones

20260720_001_create_identity_tables.py
20260720_002_create_organization_tables.py
20260720_003_create_conversation_tables.py

El identificador real seguirá el mecanismo de Alembic.

El nombre deberá describir la intención.

## 122. Migraciones por vertical slice

Las migraciones se crearán conforme se implementen slices.

No se generarán desde ahora todas las tablas documentadas.

Primer slice:

users organizations tenants memberships conversations messages
assistant_executions

## 123. Auto-generation de Alembic

alembic revision --autogenerate podrá utilizarse como ayuda.

Nunca se aplicará una migración autogenerada sin revisión manual.

## 124. Migration quality checks

CI deberá validar:

Upgrade from empty database Upgrade from previous revision Downgrade
when supported No multiple heads Models match migrations Required
extensions exist RLS policies exist Indexes exist

## 125. Cambios destructivos

Se aplicará Expand and Contract.

Ejemplo para renombrar columna:

## 1. agregar nueva columna;

## 2. escribir en ambas;

## 3. migrar datos;

## 4. cambiar lectores;

## 5. dejar de escribir antigua;

## 6. eliminar en release posterior.

## 126. Cambios de enum

Se preferirán check constraints sobre PostgreSQL enum nativo
inicialmente.

Razones:

-   migraciones más sencillas;
-   menor fricción para agregar valores;
-   mejor control en pruebas;
-   menor acoplamiento al tipo físico.

## 127. JSONB

JSONB podrá utilizarse para:

-   metadata;

-   configuraciones no críticas;

-   schemas;

-   outputs externos;

-   resultados de evaluación;

-   payloads de eventos.

## 128. Reglas JSONB

JSONB no deberá utilizarse para ocultar:

-   relaciones;
-   estados principales;
-   tenant;
-   permisos efectivos;
-   campos consultados frecuentemente;
-   dinero;
-   timestamps críticos;
-   invariantes esenciales.

## 129. Límites de JSONB

Los contratos de aplicación deberán limitar:

-   claves;
-   profundidad;
-   tamaño;
-   valores;
-   clasificación.

No se aceptará metadata ilimitada.

## 130. Encriptación de datos

La primera línea de protección será:

-   TLS;
-   cifrado del volumen;
-   object storage cifrado;
-   secret manager;
-   acceso mínimo.

Los campos altamente sensibles podrán cifrarse a nivel de aplicación.

## 131. Argumentos sensibles de tools

Se almacenarán:

-   versión sanitizada para auditoría;
-   hash para binding;
-   payload cifrado solo cuando sea necesario para ejecución diferida.

No se almacenarán secretos visibles en JSONB.

## 132. Hashes

Se utilizará SHA-256 para:

-   checksums;
-   content hashes;
-   argument binding;
-   request hashes;
-   schema checksums.

No se utilizará SHA-256 directamente para passwords.

## 133. Passwords

En caso de autenticación local se utilizará un algoritmo moderno de
password hashing, como Argon2id.

La autenticación podrá delegarse a un proveedor externo.

## 134. Retención de datos

Cada categoría tendrá política.

Dato Política inicial

Sesiones expiradas limitada

Conversaciones según tenant

Mensajes según tenant

Dato Política inicial

Archivos mientras documento exista

Chunks y embeddings ciclo del documento

Retrieval candidates corta

Auditoría prolongada

Idempotency records limitada

Outbox publicado limitada

Evaluaciones prolongada

Logs limitada por plataforma

## 135. Retención inicial propuesta

Valores por definir operativamente:

sessions expiradas: 30--90 días idempotency records: 24 horas--30 días
retrieval candidates: 7--30 días outbox publicado: 7--30 días logs
detallados: 14--30 días audit events: 1--7 años según política

No se fijarán definitivamente sin considerar obligaciones legales y
costos.

## 136. Eliminación documental

Al eliminar un documento se deberá:

## 1. marcar solicitud;

## 2. retirar de retrieval;

## 3. eliminar o invalidar chunks;

## 4. eliminar embeddings;

## 5. eliminar archivos;

## 6. limpiar cache;

## 7. conservar auditoría mínima;

## 8. verificar finalización;

## 9. registrar resultado.

## 137. Derecho de eliminación y anonimización

La arquitectura deberá permitir:

-   localizar datos de usuario;
-   anonimizar identidad visible;
-   eliminar memorias;
-   eliminar conversaciones cuando proceda;
-   conservar registros legales mínimos;
-   generar evidencia del proceso.

## 138. Backups

PostgreSQL deberá tener:

-   backups automáticos;
-   cifrado;
-   retención;
-   restauración probada;
-   Point-in-Time Recovery cuando el entorno lo permita;
-   aislamiento del entorno de producción.

## 139. Regla de backup

Un backup no se considera confiable hasta que una restauración ha sido
probada.

## 140. Recovery objectives

Se definirán posteriormente:

RPO RTO

La primera versión productiva deberá documentar valores realistas.

## 141. Object storage backups

Se deberá considerar:

-   versioning;
-   lifecycle rules;
-   cifrado;
-   bloqueo contra borrado accidental;
-   replicación si el riesgo lo exige.

## 142. Integridad entre PostgreSQL y object storage

No existe una transacción distribuida.

Se utilizarán estados y reconciliación.

Ejemplo de upload:

## 1. crear registro pending;

## 2. subir archivo;

## 3. confirmar checksum;

## 4. actualizar registro;

## 5. iniciar ingestión.

Si falla un paso, un proceso de limpieza detectará recursos huérfanos.

## 143. Reconciliation jobs

Podrán existir procesos para detectar:

-   archivos sin registro;
-   registros sin archivo;
-   documentos sin versión activa;
-   chunks sin embedding;
-   embeddings huérfanos;
-   outbox estancado;
-   approvals expiradas;
-   tool executions bloqueadas;
-   jobs running demasiado tiempo.

## 144. Health data checks

El readiness check no deberá ejecutar consultas pesadas.

Se crearán checks administrativos separados para integridad profunda.

## 145. Fixtures

Los fixtures deberán incluir:

-   organización;
-   tenant;
-   usuarios;
-   roles;
-   permisos;
-   memberships;
-   conversaciones;
-   documentos;
-   tool definitions;
-   approvals;
-   datasets de evaluación.

## 146. Fixtures deterministas

Los fixtures de test deberán utilizar:

-   IDs conocidos;
-   timestamps controlados;
-   Clock de prueba;
-   datos no sensibles;
-   estados explícitos.

## 147. Seed data

Se diferenciará entre:

Reference Data Necesario para operar.

Ejemplo:

-   permisos del sistema.

Demo Data Solo para desarrollo.

Test Fixtures Solo para pruebas.

No se mezclarán en una sola migración.

## 148. Permisos iniciales

Ejemplos:

conversations.create conversations.read conversations.manage
documents.upload documents.read documents.manage tools.execute
approvals.read approvals.decide audit.read administration.manage

El catálogo deberá estar versionado.

## 149. Roles iniciales

owner admin support operations sales

technician viewer

Los permisos exactos se definirán mediante seed versionado.

## 150. Test database

Las pruebas de integración utilizarán PostgreSQL real.

SQLite no será sustituto para pruebas de:

-   RLS;
-   pgvector;
-   JSONB;
-   locking;
-   constraints;
-   full-text;
-   transacciones;
-   índices.

## 151. Estrategia de tests

Unit tests Sin base de datos.

Repository tests PostgreSQL real.

Migration tests PostgreSQL vacío y actualización.

RLS tests Roles y tenants reales.

Concurrency tests Dos sesiones independientes.

Retrieval tests Full-text y pgvector.

## 152. Testcontainers

Podrá utilizarse Testcontainers para levantar:

-   PostgreSQL;
-   pgvector;
-   Redis;
-   object storage compatible.

Esto facilitará reproducibilidad local y CI.

## 153. Pruebas RLS obligatorias

tenant_a_cannot_select_tenant_b_rows tenant_a_cannot_insert_for_tenant_b
tenant_a_cannot_update_tenant_b tenant_a_cannot_delete_tenant_b
missing_tenant_context_returns_no_business_rows
admin_bypass_is_not_available_to_app_role

## 154. Pruebas de constraints

message_tenant_must_match_conversation chunk_tenant_must_match_document
duplicate_document_version_is_rejected
duplicate_tool_idempotency_key_is_rejected
second_approval_decision_is_rejected
multiple_active_ingestion_jobs_are_rejected

## 155. Pruebas de concurrencia

stale_conversation_version_fails only_one_approval_decision_wins
only_one_tool_execution_starts outbox_workers_do_not_claim_same_event
idempotency_key_prevents_duplicate_creation

## 156. Pruebas vectoriales

Se deberán validar:

-   dimensión correcta;
-   modelo y versión;
-   filtros por tenant;
-   chunks activos;
-   orden aproximado esperado;
-   comportamiento sin índice;
-   comportamiento con HNSW;
-   reindexación.

## 157. Query observability

Las consultas críticas deberán medir:

-   duración;
-   filas leídas;
-   filas devueltas;
-   tenant;
-   operación;
-   timeout;
-   errores.

No se registrarán parámetros sensibles.

## 158. Slow query monitoring

Se utilizarán:

-   pg_stat_statements ;
-   logs de consultas lentas;
-   métricas de pool;
-   EXPLAIN ANALYZE en staging;
-   dashboards.

## 159. Connection pooling

La API utilizará pool controlado.

Se definirán:

-   pool size;
-   max overflow;
-   timeout;
-   recycle;
-   health checks.

El número de workers deberá coordinarse con las conexiones disponibles.

## 160. PgBouncer

Se evaluará cuando:

-   existan múltiples réplicas;
-   el número de conexiones crezca;
-   el proveedor lo recomiende;
-   las conexiones sean un cuello de botella.

No será obligatorio en el primer desarrollo local.

## 161. Statement timeout

Las conexiones de aplicación deberán configurar timeouts razonables.

Ejemplo:

SET LOCAL statement_timeout = '10s';

Los procesos batch podrán usar límites distintos.

## 162. Idle transaction timeout

Se deberá impedir que una transacción permanezca abierta
accidentalmente.

Ejemplo:

idle_in_transaction_session_timeout

La configuración dependerá del entorno.

## 163. Índices: principio general

Cada índice deberá responder:

-   qué consulta soporta;
-   qué selectividad tiene;
-   cuál es su costo de escritura;
-   si puede ser parcial;
-   si el orden coincide con la consulta;
-   si es realmente utilizado.

No se indexará cada columna automáticamente.

## 164. Índices compuestos

El orden de columnas deberá seguir las consultas.

Ejemplo:

tenant_id status created_at DESC id DESC

Esto soporta aislamiento, filtro y cursor.

## 165. Índices parciales

Se preferirán cuando la consulta se enfoca en estados activos.

Ejemplos:

-   approvals pending;
-   outbox pending;
-   sesiones active;
-   documentos no eliminados;
-   jobs pendientes.

## 166. Índices JSONB

Solo se crearán si existen consultas reales sobre metadata.

No se utilizará GIN por costumbre.

## 167. Particionamiento

No se incorporará inicialmente.

Candidatos futuros:

-   audit_events;
-   messages;
-   assistant_executions;
-   retrieval_runs;
-   outbox_events.

Se evaluará según volumen y retención.

## 168. Réplicas de lectura

No serán necesarias inicialmente.

Podrán incorporarse para:

-   reportes;
-   auditoría;
-   analítica;
-   evaluaciones;
-   administración.

No deberán utilizarse en flujos que requieran lectura inmediata después
de escritura sin considerar replica lag.

## 169. Data warehouse

No forma parte del MVP.

Los eventos y tablas deberán diseñarse para permitir exportación futura
a:

-   warehouse;
-   lake;
-   BI;
-   análisis de costos;
-   calidad AI.

## 170. Datos de evaluación

Los datasets deberán evitar:

-   información sensible no autorizada;
-   datos de otros tenants;
-   secretos;
-   documentos completos innecesarios.

Los casos derivados de producción deberán sanitizarse.

## 171. Datos para demos

El portafolio deberá usar:

-   empresa ficticia o información sanitizada;

-   documentos de ejemplo;

-   usuarios ficticios;

-   herramientas sandbox;

-   tickets no reales.

## 172. Estado de datos de producción

No se permitirá copiar producción completa a desarrollo.

Cuando se requiera reproducir un error:

-   extraer caso mínimo;
-   anonimizar;
-   sanitizar;
-   documentar autorización.

## 173. Reglas de acceso administrativo

Las consultas cross-tenant serán:

-   excepcionales;
-   autorizadas;
-   auditadas;
-   ejecutadas mediante roles separados;
-   preferentemente read-only.

## 174. Data access from AI

El LLM nunca tendrá:

-   conexión a PostgreSQL;
-   credenciales SQL;
-   generación y ejecución libre de SQL;
-   acceso a tablas;
-   acceso a snapshots.

Toda consulta pasará por:

-   application service;
-   repository;
-   Retrieval;
-   Tool Registry.

## 175. SQL generation

No se incorporará text-to-SQL libre en el Proyecto 1.

Cualquier futura capacidad deberá:

-   usar schemas permitidos;
-   consultas read-only;
-   parser;
-   allowlist;
-   límites;
-   sandbox;
-   aprobación cuando aplique;
-   auditoría.

## 176. Primer esquema implementable

El Milestone 0 y 1 deberán crear únicamente:

users organizations tenants memberships roles permissions
membership_roles role_permissions conversations messages
assistant_executions idempotency_records audit_events

## 177. Datos diferidos

No se crearán todavía:

-   memory tables;

-   evaluation tables completas;

-   retrieval_candidates;

-   inbox;

-   particiones;

-   read replicas;

-   múltiples dimensiones vectoriales;

-   schemas físicos por módulo.

## 178. Orden recomendado de migraciones

001 extensions 002 identity 003 organizations_and_tenants 004
authorization 005 conversations 006 assistant_executions 007 audit 008
idempotency 009 rls_foundation 010 knowledge 011 pgvector 012 retrieval
013 tools 014 approvals 015 memory 016 evaluation 017 outbox

El orden final dependerá de los vertical slices.

## 179. RLS migration example

``` text
from alembic import op

def upgrade() -> None:
```

op.execute(

``` text
"""
ALTER TABLE conversations
```

ENABLE ROW LEVEL SECURITY

``` text
"""
```

)

op.execute(

``` text
"""
ALTER TABLE conversations
```

FORCE ROW LEVEL SECURITY

``` text
"""
```

)

op.execute(

``` text
"""
CREATE POLICY conversations_tenant_isolation
```

ON conversations USING (tenant_id = current_tenant_id()) WITH CHECK
(tenant_id = current_tenant_id())

``` text
"""
```

)

``` text
def downgrade() -> None:
```

op.execute(

``` text
"""
```

DROP POLICY IF EXISTS conversations_tenant_isolation ON conversations

``` text
"""
```

)

op.execute(

``` text
"""
ALTER TABLE conversations
```

DISABLE ROW LEVEL SECURITY

``` text
"""
```

)

## 180. pgvector SQLAlchemy example

``` text
from pgvector.sqlalchemy import Vector
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class EmbeddingRecordModel(Base):
```

**tablename** = "embedding_records"

provider: Mapped\[str\] = mapped_column( String(80),

nullable=False, )

model: Mapped\[str\] = mapped_column( String(160), nullable=False, )

vector: Mapped\[list\[float\]\] = mapped_column( Vector(1536),
nullable=False, )

## 181. Vector query SQLAlchemy example

statement = ( select( EmbeddingRecordModel.chunk_id, ( 1 -
EmbeddingRecordModel.vector.cosine_distance( query_vector )
).label("similarity"), ) .where( EmbeddingRecordModel.tenant_id ==
tenant_id, EmbeddingRecordModel.status == "active", ) .order_by(
EmbeddingRecordModel.vector.cosine_distance( query_vector ) )
.limit(limit) )

## 182. Full-text query example

SELECT id, document_id, ts_rank_cd( search_vector,
websearch_to_tsquery('spanish', :query) ) AS rank FROM chunks WHERE
tenant_id = :tenant_id AND status = 'active' AND search_vector @@
websearch_to_tsquery( 'spanish', :query ) ORDER BY rank DESC LIMIT
:limit;

## 183. Hybrid retrieval

El merge de resultados vectoriales y lexicales se ejecutará inicialmente
en aplicación.

Flujo:

## 1. recuperar top K vectorial;

## 2. recuperar top K lexical;

## 3. aplicar autorización;

## 4. normalizar rankings;

## 5. Reciprocal Rank Fusion;

## 6. seleccionar candidatos;

## 7. ensamblar contexto.

## 184. Reciprocal Rank Fusion

Ejemplo conceptual:

score = Σ 1 / (k + rank)

El valor de k deberá configurarse y evaluarse.

No se persistirá como regla inmutable sin experimentación.

## 185. Query timeouts de retrieval

Las consultas vectoriales y full-text tendrán timeout explícito.

Si una estrategia falla, podrá degradarse de forma controlada:

``` text
hybrid → full_text
hybrid → vector
vector → abstention
```

La degradación deberá registrarse.

## 186. Data architecture checklist

Antes de crear una tabla:

``` text
[ ] Owner module defined
[ ] Aggregate identified
[ ] Tenant scope defined
[ ] Primary key defined
[ ] Foreign keys defined
[ ] Constraints defined
[ ] Status model defined
[ ] Timestamps defined
[ ] Concurrency reviewed
[ ] RLS reviewed
[ ] Index queries identified
[ ] Retention defined
[ ] Sensitive data reviewed
[ ] Audit requirements defined
[ ] Migration plan defined
[ ] Tests defined
```

## 187. Migration checklist

``` text
[ ] Upgrade works on empty database
[ ] Upgrade works on previous revision
[ ] Downgrade decision documented
[ ] No destructive step without plan
[ ] Indexes reviewed
[ ] Constraints named
[ ] RLS enabled where required
[ ] Data backfill reviewed
[ ] Lock duration reviewed
[ ] CI test added
```

## 188. Query checklist

``` text
[ ] Tenant filter present
[ ] RLS context present
[ ] Authorization applied
[ ] Order stable
[ ] Limit present
[ ] Index available
[ ] Sensitive values excluded from logs
[ ] Timeout defined
[ ] Result size controlled
```

## 189. Hard gates

El proyecto no podrá considerarse listo si:

-   una tabla empresarial no tiene tenant;

-   RLS no está probado;

-   una relación permite tenant mismatch;

-   una migración no funciona desde cero;

-   un índice crítico falta;

-   un worker no es idempotente;

-   una approval puede decidirse dos veces;

-   una tool puede ejecutarse dos veces;

-   un embedding no registra modelo y versión;

-   una cita puede apuntar a otro tenant;

-   producción no tiene backup probado.

## 190. Riesgos

DA-001 --- RLS mal configurado Mitigación:

-   FORCE RLS;
-   roles separados;
-   pruebas;
-   filtros explícitos;
-   revisión de migraciones.

DA-002 --- Índices vectoriales sin buen aislamiento Mitigación:

-   benchmarks;
-   filtros;
-   candidate expansion;
-   particionamiento futuro;
-   evaluación por tenant.

DA-003 --- JSONB convertido en cajón de sastre Mitigación:

-   schemas;
-   límites;
-   revisión;
-   columnas para datos críticos.

DA-004 --- Auditoría creciendo sin control Mitigación:

-   retención;
-   particionamiento;
-   archivado;
-   índices.

DA-005 --- Migraciones destructivas Mitigación:

-   Expand and Contract;
-   pruebas;
-   backups;
-   rollback operativo.

DA-006 --- Estado inconsistente con object storage Mitigación:

-   state machine;
-   reconciliación;
-   checksums;
-   jobs de limpieza.

DA-007 --- Outbox atascada Mitigación:

-   métricas;
-   retries;
-   dead letter;
-   alertas;
-   reconciliación.

## 191. Preguntas de entrevista

Erick deberá poder responder:

-   ¿Por qué shared database y shared schema?

-   ¿Cómo implementaste Row-Level Security?

-   ¿Por qué mantienes filtros por tenant si ya existe RLS?

-   ¿Cómo evitas relaciones cruzadas entre tenants?

-   ¿Por qué elegiste UUIDv7?

-   ¿Cómo manejas optimistic concurrency?

-   ¿Cómo evitas ejecutar dos veces una tool?

-   ¿Cómo implementas Transactional Outbox?

-   ¿Cómo manejas consistencia con object storage?

-   ¿Por qué utilizas PostgreSQL Full-Text Search y pgvector?

-   ¿Cómo combinarías búsqueda lexical y vectorial?

-   ¿Qué problema puede existir con ANN y filtros por tenant?

-   ¿Cómo pruebas migraciones?

-   ¿Por qué no usas SQLite en integración?

-   ¿Cuándo considerarías particionamiento?

## 192. Decisiones oficiales

Quedan aprobadas las siguientes decisiones:

## 1. PostgreSQL será la fuente principal de verdad.

## 2. SQLAlchemy 2.x será el ORM.

## 3. Alembic administrará migraciones.

## 4. pgvector será el almacén vectorial inicial.

## 5. PostgreSQL Full-Text Search será la búsqueda lexical inicial.

## 6. Se utilizará shared database y shared schema.

## 7. Todo dato empresarial incluirá tenant cuando aplique.

## 8. RLS será una defensa obligatoria.

## 9. La aplicación seguirá filtrando explícitamente por tenant.

## 10. El rol de aplicación no tendrá BYPASSRLS.

## 11. Las tablas utilizarán snake_case y nombres plurales.

## 12. Los identificadores se almacenarán como UUID.

## 13. UUIDv7 será la estrategia recomendada pendiente de ADR.

## 14. Los timestamps utilizarán timestamptz en UTC.

## 15. Los aggregate roots relevantes utilizarán version para concurrencia.

## 16. Se utilizarán foreign keys compuestas donde el riesgo de tenant mismatch lo justifique.

## 17. Los estados se protegerán con check constraints.

## 18. Los permisos serán catálogo global y los roles tenant-scoped.

## 19. Las conversaciones y mensajes tendrán orden estable para cursor pagination.

## 20. Las versiones documentales serán inmutables al estar listas.

## 21. Los chunks conservarán ubicación y hash.

## 22. Cada embedding registrará proveedor, modelo, dimensión y versión.

## 23. La primera dimensión vectorial será fija por tabla.

## 24. HNSW se incorporará solo cuando benchmarks lo justifiquen.

## 25. El merge híbrido se realizará inicialmente en aplicación.

## 26. Las tools almacenarán schemas versionados.

## 27. Las ejecuciones sensibles usarán idempotency key.

## 28. Las approvals tendrán una sola decisión.

## 29. Los argumentos aprobados se vincularán mediante hash.

## 30. Audit events serán inmutables.

## 31. Se incorporará Transactional Outbox cuando exista mensajería asíncrona real.

## 32. Los consumidores externos utilizarán Inbox para deduplicación.

## 33. Las operaciones externas no mantendrán transacciones abiertas.

## 34. Se utilizará Expand and Contract para cambios destructivos.

## 35. Se preferirán check constraints sobre PostgreSQL enums inicialmente.

## 36. JSONB no sustituirá datos relacionales críticos.

## 37. Las pruebas de integración utilizarán PostgreSQL real.

## 38. RLS, pgvector y full-text tendrán pruebas específicas.

## 39. Los backups deberán probarse mediante restauración.

## 40. Las tablas se implementarán gradualmente por vertical slices.

## 193. Próximo documento

Documento 15 --- Project 1 Application Architecture Definirá de forma
implementable:

-   casos de uso;
-   commands;
-   queries;
-   handlers;
-   Unit of Work;
-   repositorios;
-   domain events;
-   application events;
-   pipelines;
-   middleware;
-   autorización;
-   idempotencia;
-   transacciones;
-   orchestration;
-   dependency injection;
-   errores;
-   retries;
-   ejemplos completos en Python;
-   estructura del primer vertical slice.

## 194. Conclusión

La arquitectura de datos de GEEM AI Assistant queda definida sobre
PostgreSQL como una plataforma relacional, multi-tenant, observable y
preparada para inteligencia artificial.

La base de datos no será un simple depósito de información.

Será una barrera adicional para proteger:

-   aislamiento;

-   integridad;

-   concurrencia;

-   idempotencia;

-   trazabilidad;

-   evolución.

Al mismo tiempo, la lógica empresarial seguirá perteneciendo al dominio
y a la aplicación.

Con este equilibrio podremos construir una plataforma sólida sin
convertir PostgreSQL en un conjunto de tablas débiles ni en un sistema
lleno de lógica difícil de mantener.
