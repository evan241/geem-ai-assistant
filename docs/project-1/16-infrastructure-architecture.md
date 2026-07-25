# AI Engineering Lab

## Documento 16 --- Project 1 Infrastructure Architecture

GEEM AI Assistant **Versión:** 1.0 **Estado:** Arquitectura de
infraestructura oficial **Responsable técnico:** Director de AI
Engineering **Lead Engineer:** Erick Eduardo Evangelista Velasco
**Proyecto:** GEEM AI Assistant Arquitectura: Modular Monolith + Workers
Contenedores: Docker **Base de datos:** PostgreSQL + pgvector Cache y
coordinación: Redis Archivos: Object Storage compatible con S3
**Observabilidad:** OpenTelemetry **CI/CD:** GitHub Actions

## 1. Propósito

Este documento define la infraestructura implementable de GEEM AI
Assistant.

Su objetivo es establecer cómo se ejecutará, configurará, desplegará y
operará el sistema en:

-   desarrollo local;
-   pruebas;
-   integración continua;
-   staging;
-   producción.

La arquitectura deberá soportar:

-   API FastAPI;

-   frontend React;

-   workers;

-   PostgreSQL;

-   pgvector;

-   Redis;

-   object storage;

-   proveedores de inteligencia artificial;

-   procesos asíncronos;

-   streaming;

-   observabilidad;

-   backups;

-   recuperación;

-   despliegues seguros.

## 2. Principio rector

La infraestructura debe ser reproducible, observable, segura y
sustituible.

Ningún entorno crítico deberá depender de configuraciones manuales no
documentadas.

Toda configuración importante deberá existir como:

-   código;
-   variable de entorno;
-   secreto administrado;
-   migración;
-   workflow;
-   manifiesto;
-   política documentada.

## 3. Objetivos de infraestructura

La infraestructura deberá permitir:

## 1. levantar el proyecto localmente;

## 2. ejecutar pruebas en CI;

## 3. desplegar staging;

## 4. desplegar producción;

## 5. ejecutar migraciones;

## 6. procesar jobs;

## 7. almacenar documentos;

## 8. ejecutar búsquedas vectoriales;

## 9. entregar streaming SSE;

## 10. registrar logs, métricas y traces;

## 11. restaurar datos;

## 12. rotar secretos;

## 13. sustituir proveedores.

## 4. No objetivos iniciales

La primera versión no requerirá:

-   Kubernetes;
-   service mesh;
-   multi-region activo-activo;
-   múltiples clusters PostgreSQL;
-   autoescalado complejo;
-   infraestructura multi-cloud;
-   Kafka;
-   data lake;
-   GPU propia;
-   entrenamiento de modelos;
-   despliegues de decenas de microservicios.

Estas capacidades solo se incorporarán cuando exista necesidad
demostrada.

## 5. Topología inicial

Internet ↓ Reverse Proxy / Load Balancer

``` text
├── Frontend
└── API
├── PostgreSQL + pgvector
├── Redis
├── Object Storage
├── AI Providers
└── Observability Collector
```

Worker

``` text
├── PostgreSQL
├── Redis / Queue
├── Object Storage
├── AI Providers
└── Observability Collector
```

## 6. Componentes de ejecución

El sistema estará compuesto por:

frontend api worker postgres redis object-storage otel-collector
reverse-proxy

En desarrollo podrán ejecutarse en Docker Compose.

En producción algunos componentes podrán ser servicios administrados.

## 7. Estrategia de despliegue inicial

La recomendación inicial será:

Contenedores administrados + PostgreSQL administrado + Redis
administrado + Object Storage administrado

Esto reduce el riesgo operativo de administrar manualmente:

-   backups;
-   replicación;
-   actualizaciones;
-   discos;
-   recuperación;
-   disponibilidad.

## 8. Modular Monolith en infraestructura

Aunque la aplicación sea modular, inicialmente se desplegará como:

1 API deployment 1 Worker deployment 1 Frontend deployment

API y worker podrán utilizar la misma imagen backend con comandos de
inicio distintos.

## 9. Imágenes de contenedor

Se construirán al menos:

geem-ai-api geem-ai-frontend

El worker podrá reutilizar:

geem-ai-api

ejecutando un entrypoint diferente.

## 10. Reproducibilidad

La construcción deberá fijar:

-   versión de Python;
-   versión de Node;
-   lockfiles;
-   dependencias;
-   imagen base;
-   herramientas;
-   comandos;
-   migraciones.

No se utilizará:

latest

como tag en producción.

## 11. Versionado de imágenes

Las imágenes deberán etiquetarse con:

commit SHA release version environment alias opcional

Ejemplo:

geem-ai-api:sha-a13f992 geem-ai-api:v0.1.0

## 12. Dockerfile del backend

Ejemplo conceptual:

FROM python:3.12-slim AS builder

``` text
WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN pip install --no-cache-dir uv
```

&& uv sync --frozen --no-dev

FROM python:3.12-slim AS runtime

``` text
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN groupadd --system app
```

&& useradd --system --gid app app

``` text
COPY --from=builder /app/.venv /app/.venv
COPY src ./src
COPY alembic.ini .
COPY migrations ./migrations

ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH="/app/src"
```

USER app

``` text
CMD ["uvicorn", "geem_ai.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

La implementación final deberá probar que todas las librerías nativas
necesarias están presentes.

## 13. Usuario no root

Los contenedores de aplicación deberán ejecutarse con usuario no root.

Excepciones deberán justificarse.

## 14. Multi-stage builds

Se utilizarán builds multietapa para:

-   reducir tamaño;
-   excluir herramientas de compilación;
-   evitar dependencias de desarrollo;
-   disminuir superficie de ataque.

## 15. Dockerfile del frontend

Ejemplo conceptual:

FROM node:22-alpine AS builder

``` text
WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

COPY . .
RUN npm run build
```

FROM nginx:alpine AS runtime

``` text
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
```

EXPOSE 80

La imagen final no deberá incluir Node cuando el frontend sea estático.

## 16. Docker Compose de desarrollo

El entorno local incluirá:

services: api: worker: frontend: postgres: redis: minio: otel-collector:

Podrán agregarse herramientas de debugging mediante profiles.

## 17. Profiles de Docker Compose

Ejemplos:

core observability debug evaluation

Esto permitirá no levantar todos los componentes siempre.

## 18. Ejemplo conceptual de Compose

services: postgres:

image: pgvector/pgvector:pg16 environment: POSTGRES_DB: geem_ai
POSTGRES_USER: geem POSTGRES_PASSWORD: geem_local ports: - "5432:5432"
volumes: - postgres_data:/var/lib/postgresql/data healthcheck: test:
\["CMD-SHELL", "pg_isready -U geem -d geem_ai"\] interval: 5s timeout:
5s retries: 10

redis: image: redis:7-alpine ports: - "6379:6379" healthcheck: test:
\["CMD", "redis-cli", "ping"\]

minio: image: minio/minio command: server /data --console-address
":9001" environment: MINIO_ROOT_USER: geem MINIO_ROOT_PASSWORD:
geem_local_password ports: - "9000:9000" - "9001:9001"

api: build: context: . dockerfile: docker/backend.Dockerfile command: \>
uvicorn geem_ai.main:app --host 0.0.0.0 --port 8000 --reload env_file: -
.env.local depends_on: postgres: condition: service_healthy redis:
condition: service_healthy

Los secretos locales del ejemplo nunca se reutilizarán en otros
entornos.

## 19. Volúmenes locales

Se utilizarán volúmenes persistentes para:

-   PostgreSQL;
-   MinIO;
-   datos de herramientas locales.

El código podrá montarse como bind mount durante desarrollo.

## 20. Comandos estándar

El repositorio deberá ofrecer comandos simples.

Ejemplos:

``` text
make up
make down
make logs
make test
make lint
make migrate
make migration
make seed
make reset-db
make openapi
```

Podrá utilizarse Make, Taskfile o herramienta equivalente.

## 21. Regla de onboarding

Un nuevo desarrollador deberá poder levantar el entorno con:

README + archivo de ejemplo de variables

-   un comando principal

No deberá necesitar instrucciones transmitidas verbalmente.

## 22. Configuración por entornos

Existirán:

local test ci staging production

Cada entorno tendrá valores distintos, pero el mismo modelo de
configuración.

## 23. Variables de entorno

Convención:

GEEM\_`<COMPONENT>`{=html}\_`<SETTING>`{=html}

Ejemplos:

GEEM_APP_ENV GEEM_DATABASE_URL GEEM_REDIS_URL GEEM_STORAGE_ENDPOINT
GEEM_STORAGE_BUCKET GEEM_OPENAI_API_KEY GEEM_OTEL_ENDPOINT

## 24. Configuración tipada

La aplicación utilizará configuración tipada.

Ejemplo:

``` text
from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
```

app_env: str = Field(alias="GEEM_APP_ENV") database_url: str =
Field(alias="GEEM_DATABASE_URL") redis_url: str =
Field(alias="GEEM_REDIS_URL") storage_bucket: str =
Field(alias="GEEM_STORAGE_BUCKET")

model_config = {

``` text
"env_file": ".env.local",
"extra": "ignore",
}
```

## 25. Validación al iniciar

La aplicación deberá fallar al iniciar cuando falte una configuración
crítica.

No deberá descubrir durante una operación de usuario que:

-   falta bucket;
-   falta clave;
-   falta URL;
-   el entorno es inválido.

## 26. Archivos .env

Se permitirá:

.env.example .env.local .env.test

Solo .env.example podrá versionarse.

No se versionarán secretos reales.

## 27. Secret management

En staging y producción los secretos deberán vivir en:

-   secret manager del proveedor;
-   vault;
-   gestor equivalente.

No deberán almacenarse en:

-   repositorio;
-   Dockerfile;
-   imagen;
-   logs;
-   frontend;
-   archivos compartidos manualmente.

## 28. Clasificación de secretos

Ejemplos:

database credentials Redis credentials object storage credentials OpenAI
API key Anthropic API key JWT signing keys OAuth client secrets webhook
signing keys encryption keys

## 29. Rotación

Todo secreto deberá tener:

-   owner;
-   fecha de creación;
-   estrategia de rotación;
-   capacidad de revocación;
-   alcance mínimo.

## 30. Rotación sin interrupción

Cuando sea posible se utilizará:

current key + next key

durante la transición.

Esto aplica especialmente a:

-   JWT;
-   firmas;
-   webhooks;
-   credenciales de integración.

## 31. PostgreSQL por entorno

Local Contenedor.

CI Contenedor efímero.

Staging Servicio administrado.

Producción Servicio administrado con backups y monitoreo.

## 32. Extensiones PostgreSQL

La infraestructura deberá habilitar:

vector pg_stat_statements

Otras extensiones requerirán revisión.

## 33. Migraciones

Las migraciones se ejecutarán como un job separado.

No se recomienda que todas las réplicas de API intenten migrar al
iniciar.

Flujo:

Build

``` text
→ Test
→ Migration Job
→ Deploy API
→ Deploy Worker
```

## 34. Migration job

Ejemplo:

alembic upgrade head

El job deberá:

-   usar rol migrator;
-   tener timeout;
-   registrar revisión aplicada;
-   fallar el despliegue si la migración falla.

## 35. Compatibilidad durante despliegue

Las migraciones deberán ser compatibles temporalmente con:

-   versión anterior;

-   versión nueva.

Esto permite rolling deployment.

## 36. PostgreSQL connection pool

Se configurará explícitamente:

pool_size max_overflow pool_timeout pool_recycle pool_pre_ping

Los valores dependerán del límite del servicio administrado.

## 37. Presupuesto de conexiones

Se calculará:

API replicas × pool máximo + worker replicas × pool máximo +
migrations + administración \< límite PostgreSQL

No se configurarán pools de forma aislada.

## 38. Redis

Redis se utilizará inicialmente para:

-   cache de corta duración;

-   rate limiting;

-   coordinación;

-   publicación de eventos SSE;

-   locks no críticos;

-   posible cola inicial.

No será fuente de verdad empresarial.

## 39. Datos que no vivirán solo en Redis

No se almacenarán únicamente en Redis:

-   conversaciones;
-   mensajes finales;
-   approvals;
-   tool executions;
-   auditoría;
-   documentos;
-   estados de jobs críticos.

## 40. Redis namespaces

Convención conceptual:

geem:`<environment>`{=html}:`<module>`{=html}:`<purpose>`{=html}:`<id>`{=html}

Ejemplos:

geem:staging:sse:execution:exec_123 geem:prod:rate-limit:user:usr_123
geem:prod:cache:permissions:mem_123

## 41. TTL obligatorio

Toda clave de cache o coordinación temporal deberá tener TTL.

No se crearán claves efímeras sin expiración, salvo justificación.

## 42. Redis Pub/Sub vs Streams

Pub/Sub Adecuado para deltas SSE efímeros.

Streams Adecuado para mensajes que requieren:

-   persistencia temporal;
-   consumer groups;
-   relectura;
-   acknowledgements.

La primera versión podrá usar:

Pub/Sub para streaming Streams o cola dedicada para jobs

## 43. Tecnología de cola

La arquitectura deberá desacoplarse de una tecnología específica.

Opciones iniciales:

-   Redis Streams;
-   Dramatiq;
-   Celery;
-   ARQ;
-   servicio administrado.

La decisión se registrará mediante ADR antes de implementar workers
críticos.

## 44. Criterios para elegir cola

Se evaluará:

-   entrega al menos una vez;

-   retries;

-   scheduling;

-   dead letter;

-   observabilidad;

-   concurrencia;

-   soporte async;

-   complejidad operativa;

-   idempotencia;

-   mantenimiento.

## 45. Recomendación inicial de workers

Para el primer producto se preferirá una solución sencilla compatible
con Python asíncrono y Redis.

La lógica de aplicación no dependerá directamente de ella.

## 46. Worker deployment

El worker utilizará la misma versión de código que la API.

Ejemplo de comando:

python -m geem_ai.worker

## 47. Tipos de worker

Podrán existir procesos separados:

assistant-worker ingestion-worker maintenance-worker outbox-worker

Inicialmente podrán ejecutarse en un solo deployment con colas
diferenciadas.

## 48. Separación futura

Se separarán cuando difieran en:

-   carga;
-   memoria;
-   CPU;
-   permisos;
-   escalamiento;
-   dependencias;
-   riesgo.

## 49. Concurrencia del worker

La concurrencia deberá configurarse por tipo de job.

Ejemplos:

-   ingestión documental: limitada por memoria y proveedor;
-   assistant executions: limitada por rate limits;
-   outbox: alta pero controlada;
-   maintenance: baja.

## 50. Graceful shutdown

Los workers deberán:

## 1. dejar de reclamar nuevos jobs;

## 2. terminar o liberar el job actual;

## 3. guardar estado;

## 4. cerrar conexiones;

## 5. finalizar dentro del periodo de gracia.

## 51. Job lease

Los jobs reclamados deberán tener:

-   owner;

-   claimed_at;

-   lease expiration;

-   heartbeat cuando aplique.

Esto permite recuperar jobs de workers muertos.

## 52. Dead letter

Los jobs que agoten reintentos deberán:

-   cambiar a dead letter;
-   conservar error;
-   generar alerta;
-   permitir inspección;
-   permitir replay controlado.

## 53. Object storage

Se utilizará almacenamiento compatible con S3.

Local:

MinIO

Staging y producción:

servicio administrado compatible

## 54. Buckets

Podrán existir:

documents exports evaluation-artifacts temporary

La separación física dependerá de permisos y lifecycle.

## 55. Estructura de objetos

Convención:

`<environment>`{=html}/`<tenant_id>`{=html}/`<resource_type>`{=html}/`<resource_id>`{=html}/`<version>`{=html}/`<filename>`{=html}

Ejemplo:

prod/ten_123/documents/doc_456/v1/source.pdf

## 56. No confiar en el path

El storage key no será utilizado como mecanismo de autorización.

El acceso siempre pasará por la aplicación.

## 57. Signed URLs

Las signed URLs deberán:

-   tener expiración corta;
-   limitar operación;
-   limitar objeto;
-   generarse después de autorización;
-   no registrarse completas en logs.

## 58. Upload strategy

Para archivos pequeños podrá usarse:

``` text
cliente → API → object storage
```

Para archivos mayores podrá usarse:

``` text
cliente → signed upload URL → object storage
```

seguido de confirmación en API.

## 59. Validación de archivos

La infraestructura y aplicación deberán validar:

-   tamaño;
-   MIME real;
-   extensión;
-   checksum;
-   malware cuando se incorpore;
-   contenido soportado;
-   límites por tenant.

## 60. Lifecycle de archivos temporales

Los archivos temporales deberán eliminarse automáticamente mediante
lifecycle rules.

Ejemplo:

temporary objects expire after 24--72 hours

## 61. Versioning de object storage

En producción se recomienda versioning para documentos críticos.

La política deberá equilibrar:

-   recuperación;
-   costos;
-   derecho de eliminación;
-   retención.

## 62. AI Provider architecture

Los proveedores externos se integrarán únicamente mediante adapters.

Application ↓ Model Gateway ↓ Provider Adapter

``` text
├── OpenAI
└── Anthropic
```

## 63. Provider credentials

Cada proveedor tendrá credenciales separadas por entorno.

No se compartirá una misma API key entre:

-   desarrollo;
-   staging;
-   producción.

## 64. Provider configuration

Ejemplo:

provider model timeout max_retries rate_limit cost table capabilities
fallback order

## 65. Model Gateway infrastructure

La implementación deberá incluir:

-   selección de adapter;
-   timeout;
-   retries limitados;
-   circuit breaker;
-   métricas;
-   costos;
-   validación;
-   fallback;
-   normalización.

## 66. Provider adapter contract

``` text
class ModelProviderAdapter(Protocol):
async def execute(
```

self, request: ProviderRequest, ) -\> ProviderResponse: ...

``` text
async def health(self) -> ProviderHealth:
```

...

## 67. Rate limits de proveedor

El sistema deberá manejar:

-   requests por minuto;
-   tokens por minuto;
-   límites por modelo;
-   errores 429;
-   Retry-After ;
-   cuotas por tenant.

## 68. Retry de proveedores AI

Se permitirán retries para:

-   timeout;
-   conexión;
-   429;
-   500;
-   502;
-   503;
-   504. 

No se reintentará indefinidamente.

## 69. Backoff

Se utilizará:

exponential backoff + jitter + maximum delay + maximum attempts

## 70. Circuit breaker

Un proveedor con fallos repetidos podrá marcarse temporalmente como no
disponible.

Estados conceptuales:

closed open half_open

La primera implementación podrá ser simple.

## 71. Fallback

Un fallback solo se utilizará cuando:

-   el capability lo permite;
-   el modelo alternativo soporta herramientas necesarias;
-   el output schema es compatible;
-   el costo está permitido;
-   la política lo autoriza.

## 72. Embedding provider

La generación de embeddings deberá pasar por un port separado.

``` text
class EmbeddingGateway(Protocol):
async def embed(
```

self, inputs: list\[str\], model: str, ) -\> EmbeddingBatchResult: ...

## 73. Batching de embeddings

El ingestion worker deberá agrupar entradas respetando:

-   límite de tokens;
-   límite de elementos;
-   tamaño de request;
-   timeout;
-   rate limit.

## 74. Cache de embeddings

Podrá reutilizarse un embedding cuando coincidan:

content_hash provider model embedding_version normalization_version

## 75. Reverse proxy

El reverse proxy será responsable de:

-   TLS;
-   routing;
-   compresión;
-   límites básicos;
-   headers;
-   timeout;
-   forwarding;
-   soporte SSE.

## 76. SSE proxy configuration

Deberá evitar buffering.

Ejemplo Nginx conceptual:

location /api/v1/streams/ { proxy_pass http://api:8000;
proxy_http_version 1.1; proxy_set_header Connection ""; proxy_buffering
off; proxy_cache off; proxy_read_timeout 3600s; add_header
X-Accel-Buffering no;

``` text
}
```

## 77. Timeouts del proxy

Se configurarán por tipo de endpoint.

No todos los endpoints tendrán timeouts largos.

Ejemplos:

REST normal: corto upload: moderado SSE: largo health: muy corto

## 78. Request size limits

Se definirán límites para:

-   JSON;
-   uploads;
-   headers;
-   tool results.

Los archivos grandes deberán utilizar carga directa a object storage.

## 79. TLS

Staging y producción utilizarán HTTPS.

No se permitirá tráfico HTTP externo sin redirección o terminación
segura.

## 80. Network segmentation

Los componentes internos no deberán exponerse directamente a internet.

Solo serán públicos:

frontend reverse proxy API mediante reverse proxy

PostgreSQL, Redis y object storage interno deberán permanecer en red
privada.

## 81. Egress control

Cuando el entorno lo permita, se limitará salida a:

-   proveedores AI;
-   object storage;
-   servicios autorizados;
-   telemetry;
-   integraciones registradas.

Esto reduce el impacto de SSRF y herramientas comprometidas.

## 82. DNS y dominios

Ejemplo:

app.assistant.geem.example api.assistant.geem.example

Staging utilizará dominio independiente.

## 83. CORS

CORS será restrictivo.

Se permitirán únicamente orígenes configurados.

No se utilizará:

-   

con credenciales.

## 84. Security headers

El frontend y proxy deberán considerar:

Content-Security-Policy Strict-Transport-Security X-Content-Type-Options
Referrer-Policy Permissions-Policy

## 85. CI pipeline

El pipeline inicial deberá ejecutar:

checkout dependency install format check lint type check unit tests
architecture tests integration tests migration tests OpenAPI validation
contract compatibility security scan build images

## 86. CI backend

Ejemplo conceptual:

jobs: backend: runs-on: ubuntu-latest

services: postgres: image: pgvector/pgvector:pg16 redis: image:
redis:7-alpine

steps:

-   uses: actions/checkout@v4
-   name: Install dependencies run: uv sync --frozen
-   name: Lint run: uv run ruff check .
-   name: Type check run: uv run mypy src
-   name: Test run: uv run pytest

La versión exacta de cada action deberá fijarse y revisarse.

## 87. CI frontend

Deberá ejecutar:

npm ci lint typecheck tests build

## 88. Dependency scanning

El pipeline deberá revisar:

-   dependencias Python;
-   dependencias Node;
-   imágenes;
-   secretos;
-   licencias cuando aplique.

## 89. Secret scanning

Se utilizarán controles para detectar:

-   API keys;

-   passwords;

-   private keys;

-   tokens;

-   archivos .env .

## 90. Container scanning

Las imágenes deberán escanearse antes de desplegar.

Vulnerabilidades críticas deberán bloquear el release salvo excepción
documentada.

## 91. SBOM

Las releases productivas deberán generar Software Bill of Materials
cuando la capacidad esté disponible.

## 92. Artefactos de CI

El pipeline conservará:

-   resultados de pruebas;
-   coverage;
-   OpenAPI;
-   reportes de seguridad;
-   imágenes;
-   migrations report;
-   evaluation report cuando aplique.

## 93. Branch protection

La rama principal requerirá:

-   CI exitoso;
-   revisión;
-   sin conflictos;
-   checks obligatorios;
-   commits firmados cuando se adopte;
-   prohibición de push directo.

## 94. CD a staging

El merge a rama principal podrá desplegar automáticamente a staging.

Flujo:

merge

``` text
→ build immutable images
→ push registry
→ migrate staging
→ deploy staging
→ smoke tests
```

## 95. CD a producción

Producción requerirá:

-   release aprobada;
-   artefactos ya probados;
-   migration review;
-   backup verificado;
-   despliegue controlado;
-   smoke tests;
-   capacidad de rollback.

## 96. Artefactos inmutables

La imagen desplegada en producción deberá ser la misma probada en
staging.

No se reconstruirá entre entornos.

## 97. Estrategia de despliegue

Inicialmente:

rolling deployment

Podrá evolucionar a:

blue-green canary

cuando exista necesidad.

## 98. Orden de despliegue

## 1. validar backup

## 2. ejecutar migración compatible

## 3. desplegar API

## 4. desplegar workers

## 5. desplegar frontend

## 6. ejecutar smoke tests

## 7. observar métricas

El orden podrá variar según compatibilidad.

## 99. Rollback

El rollback deberá distinguir:

Application rollback Regresar imagen.

Database rollback No siempre será seguro.

Por eso las migraciones deberán ser compatibles hacia adelante.

## 100. Roll forward

Ante migraciones no reversibles se preferirá:

fix forward

con plan probado.

## 101. Feature flags y despliegue

Una capacidad riesgosa podrá desplegarse deshabilitada.

Flujo:

deploy code

``` text
→ validate
→ enable internal tenant
→ observe
→ expand rollout
```

## 102. Staging

Staging deberá parecerse a producción en:

-   topología;
-   versiones;
-   TLS;
-   secretos;
-   servicios;
-   migraciones;
-   observabilidad.

Podrá usar tamaños menores.

## 103. Datos de staging

Staging utilizará datos:

-   ficticios;
-   sanitizados;
-   limitados;
-   no productivos.

## 104. Producción

Producción requerirá:

-   backups;
-   monitoreo;
-   alertas;
-   TLS;
-   secret manager;
-   roles separados;
-   migraciones controladas;
-   almacenamiento persistente;
-   políticas de retención.

## 105. Health endpoints

La API expondrá:

``` text
GET /api/v1/health/live
GET /api/v1/health/ready
```

## 106. Liveness

Liveness deberá responder si el proceso puede atender.

No deberá depender de todos los servicios externos.

## 107. Readiness

Readiness verificará dependencias mínimas:

-   PostgreSQL;
-   migración compatible;
-   configuración válida.

Redis u object storage podrán ser requeridos según la capacidad
desplegada.

## 108. Provider health

No se llamará constantemente a un proveedor AI desde readiness.

Su estado se manejará mediante:

-   métricas;
-   circuit breaker;
-   probes administrativas;
-   resultados recientes.

## 109. Worker health

Los workers deberán exponer o reportar:

-   heartbeat;
-   última actividad;
-   colas;
-   jobs activos;
-   versión desplegada.

## 110. Observability Collector

Se utilizará OpenTelemetry Collector como punto de salida para:

-   traces;
-   metrics;
-   logs cuando aplique.

Esto evita acoplar la aplicación a un backend específico.

## 111. OpenTelemetry resource attributes

Cada proceso incluirá:

service.name service.version

deployment.environment service.instance.id

## 112. Propagación

Se propagarán:

traceparent tracestate baggage controlado X-Correlation-Id

No se colocarán secretos en baggage.

## 113. Logs de contenedor

Los contenedores escribirán logs estructurados a stdout/stderr.

No se dependerá de archivos locales dentro del contenedor.

## 114. Métricas de infraestructura

Se medirán:

-   CPU;
-   memoria;
-   reinicios;
-   uso de disco;
-   conexiones PostgreSQL;
-   query latency;
-   Redis memory;
-   queue depth;
-   job age;
-   object storage errors;
-   provider errors;
-   network latency.

## 115. Métricas de deployment

Se registrarán:

-   versión;
-   commit;
-   hora;
-   entorno;
-   migración;
-   resultado;
-   rollback.

## 116. Alertas iniciales

Se deberán crear alertas para:

API error rate high API latency high readiness failing worker heartbeat
missing queue depth growing oldest job too old PostgreSQL connections
near limit disk near capacity outbox stuck dead-letter messages AI
provider failure rate high cost anomaly backup failed

## 117. Alert fatigue

No se crearán alertas sin:

-   owner;
-   severidad;
-   umbral;
-   acción esperada;
-   runbook.

## 118. Runbooks

Cada alerta crítica deberá incluir:

-   significado;
-   impacto;
-   diagnóstico;
-   pasos;
-   rollback;
-   escalamiento.

## 119. Backups PostgreSQL

Producción deberá tener:

-   backups automáticos;
-   cifrado;
-   retención;
-   PITR cuando esté disponible;
-   restauración probada.

## 120. Backup frequency

La frecuencia dependerá de RPO y proveedor.

No se definirá solo por comodidad.

## 121. Restore drills

Se ejecutarán restauraciones periódicas en un entorno aislado.

Se verificará:

-   integridad;
-   migraciones;
-   permisos;
-   RLS;
-   extensiones;
-   object storage relacionado.

## 122. Backup de object storage

La estrategia podrá incluir:

-   versioning;
-   lifecycle;
-   replicación;
-   protección contra borrado;
-   inventario de objetos.

## 123. Redis recovery

Redis no será fuente de verdad.

Su pérdida podrá causar:

-   cache miss;
-   streams temporales perdidos;
-   reconexión SSE;
-   reprogramación de jobs según la cola.

Los procesos críticos deberán recuperarse desde PostgreSQL.

## 124. Disaster recovery

El plan deberá responder:

## 1. ¿Cómo se restaura PostgreSQL?

## 2. ¿Cómo se restauran documentos?

## 3. ¿Cómo se recuperan jobs?

## 4. ¿Cómo se reconstruyen embeddings?

## 5. ¿Cómo se reanudan tools?

## 6. ¿Cómo se validan approvals?

## 7. ¿Cómo se rotan secretos comprometidos?

## 125. Rebuildable data

Se consideran reconstruibles:

-   caches;
-   search indexes;
-   embeddings, si existe texto fuente;
-   proyecciones;
-   métricas derivadas.

No por eso deberán tratarse sin cuidado.

## 126. Infrastructure as Code

La infraestructura de staging y producción deberá definirse como código
cuando se seleccione proveedor.

Podrá utilizarse:

-   Terraform;
-   OpenTofu;
-   herramienta nativa;
-   Pulumi.

La elección requerirá ADR.

## 127. Módulos de IaC

Ejemplo:

network database redis storage container-runtime secrets observability
dns

## 128. Estado de IaC

El state deberá:

-   almacenarse remotamente;
-   cifrarse;
-   bloquearse;
-   tener acceso restringido;
-   no contener secretos innecesarios.

## 129. Entornos IaC

Se mantendrán separados:

staging production

No se compartirán recursos críticos entre ambos.

## 130. Least privilege

Cada componente tendrá permisos mínimos.

Ejemplos:

-   API puede leer/escribir documentos autorizados;
-   worker de ingestión accede al bucket documental;
-   frontend no conoce secretos;
-   migrator puede alterar schema;
-   app role no puede alterar schema;
-   readonly no puede escribir.

## 131. Service identities

Los deployments deberán usar identidades de servicio cuando el proveedor
lo permita.

Se evitarán credenciales humanas permanentes.

## 132. Local development authentication

El entorno local podrá utilizar un actor de desarrollo configurable.

Deberá:

-   estar explícitamente habilitado;
-   funcionar solo en local o test;
-   no compilarse como bypass silencioso;
-   fallar en producción.

## 133. Environment guard

Ejemplo:

if settings.dev_auth_enabled and settings.app_env == "production":

``` text
raise RuntimeError(
"Development authentication cannot run in production."
```

)

## 134. Desarrollo sin proveedor AI

El sistema deberá poder ejecutarse localmente con:

FakeModelGateway

Esto permite:

-   pruebas;
-   onboarding;
-   desarrollo sin costo;
-   CI determinista.

## 135. Desarrollo con proveedor real

La activación deberá requerir:

GEEM_MODEL_PROVIDER_MODE=live

y una clave local no versionada.

## 136. Modo sandbox de tools

Las tools con efectos deberán ofrecer un adapter sandbox para:

-   demo;
-   pruebas;
-   portafolio;
-   staging.

Ejemplo:

create_support_ticket

``` text
→ local support ticket simulator
```

## 137. Cost control de entornos

Local y CI no deberán consumir proveedores reales por defecto.

Staging tendrá límites bajos.

Producción tendrá:

-   presupuestos;
-   alertas;
-   cuotas;
-   modelos autorizados.

## 138. Resource limits

Los contenedores deberán definir:

-   CPU request;

-   CPU limit;

-   memory request;

-   memory limit;

-   restart policy.

Los valores se ajustarán con métricas.

## 139. Evitar OOM en ingestión

Los documentos deberán procesarse mediante:

-   streaming;
-   archivos temporales limitados;
-   batches;
-   límites de tamaño;
-   concurrencia controlada.

## 140. Temporary storage

Los contenedores podrán usar espacio temporal para extracción.

Deberá:

-   tener límite;
-   limpiarse;
-   no persistir secretos;
-   no ser fuente de verdad.

## 141. Autoscaling

No será requisito inicial.

Podrá evaluarse para:

-   API por CPU y latencia;
-   workers por queue depth;
-   ingestión por backlog;
-   assistant workers por rate limits.

## 142. Escalamiento y proveedores

Aumentar workers no siempre aumenta capacidad si el límite está en:

-   proveedor AI;
-   PostgreSQL;
-   Redis;
-   object storage;
-   presupuesto.

El escalamiento deberá considerar toda la cadena.

## 143. Maintenance jobs

Existirán jobs periódicos para:

expire approvals clean idempotency records clean temporary uploads retry
outbox detect stale executions reconcile storage refresh cost tables
validate backups

## 144. Scheduler

El scheduler podrá ser:

-   servicio de cron administrado;
-   worker scheduler;
-   plataforma de jobs.

No se dependerá de cron dentro de cada réplica de API.

## 145. Stale execution detection

Un job periódico buscará ejecuciones en:

running waiting_for_approval

que excedan límites.

No deberá marcarlas fallidas sin evaluar su estado real.

## 146. Outbox publication

El outbox worker deberá:

-   reclamar batches;
-   publicar;
-   marcar resultado;
-   reintentar;
-   emitir métricas;
-   manejar dead letter.

## 147. Build cache

CI podrá utilizar cache para:

-   dependencias Python;
-   dependencias Node;
-   capas Docker.

La cache no deberá comprometer reproducibilidad.

## 148. Local architecture commands

Ejemplo:

``` text
make bootstrap
make up
make migrate
make seed-demo
make test
make down
```

## 149. Bootstrap local

``` text
make bootstrap podrá:
```

## 1. verificar Docker;

## 2. copiar .env.example ;

## 3. construir imágenes;

## 4. iniciar dependencias;

## 5. ejecutar migraciones;

## 6. crear seed;

## 7. verificar health.

## 150. Smoke tests

Después de desplegar se probará:

liveness readiness create conversation read conversation database
write/read Redis connectivity object storage connectivity fake or safe
AI capability

Producción no deberá ejecutar una tool con efecto real como smoke test.

## 151. Synthetic monitoring

Podrán ejecutarse pruebas periódicas con tenant sintético.

Ejemplos:

-   crear conversación;
-   generar respuesta controlada;
-   consultar documento de prueba;
-   verificar cita.

## 152. Release metadata endpoint

La API podrá exponer internamente:

version commit_sha build_time environment database_revision

No deberá exponer secretos.

## 153. Infrastructure repository structure

infra/

``` text
├── docker/
│   ├── backend.Dockerfile
│   ├── frontend.Dockerfile
│   └── nginx/
├── compose/
│   ├── compose.yaml
│   └── compose.observability.yaml
├── terraform/
│   ├── modules/
│   ├── staging/
│   └── production/
├── observability/
│   ├── otel-collector.yaml
│   ├── dashboards/
│   └── alerts/
└── scripts/
├── migrate.sh
├── smoke-test.sh
└── restore-test.sh
```

## 154. GitHub Actions structure

.github/

``` text
└── workflows/
├── backend-ci.yml
├── frontend-ci.yml
├── contract-ci.yml
├── security-ci.yml
├── build-images.yml
├── deploy-staging.yml
└── release-production.yml
```

## 155. Environment protection

GitHub Environments podrá utilizarse para:

-   staging;
-   production;
-   secretos;
-   approvals;
-   reglas de deployment.

## 156. Production approval

El despliegue productivo deberá requerir aprobación explícita al menos
durante las primeras releases.

## 157. Dependency update policy

Las dependencias deberán actualizarse regularmente.

No se actualizarán automáticamente a producción sin:

-   CI;
-   revisión;
-   pruebas;
-   changelog;
-   evaluación de breaking changes.

## 158. Base image updates

Las imágenes base deberán reconstruirse periódicamente aunque el código
no cambie.

Esto permite recibir parches de seguridad.

## 159. Infrastructure testing

Se probarán:

-   Docker builds;
-   Compose boot;
-   health checks;
-   migrations;
-   RLS;
-   storage;
-   Redis;
-   provider fake;
-   worker claiming;
-   graceful shutdown;
-   restore.

## 160. Chaos scenarios iniciales

En staging deberán probarse escenarios como:

Redis unavailable AI provider timeout worker restart duplicate job
database connection interruption object storage timeout SSE disconnect
migration failure

## 161. Comportamiento sin Redis

La API deberá seguir operando en capacidades que no dependan de Redis.

Podrán degradarse:

-   streaming en tiempo real;
-   cache;
-   rate limiting sofisticado;
-   jobs basados en Redis.

El estado persistido deberá conservarse.

## 162. Comportamiento sin proveedor AI

El sistema deberá:

-   aceptar o rechazar nuevas ejecuciones según política;
-   marcar error seguro;
-   utilizar fallback autorizado;
-   conservar conversaciones;
-   no perder mensajes;
-   alertar.

## 163. Comportamiento sin object storage

El sistema podrá seguir permitiendo:

-   login;
-   conversaciones existentes;
-   administración no documental.

Deberá bloquear o degradar:

-   upload;
-   ingestión;
-   descarga.

## 164. Comportamiento sin PostgreSQL

La API no estará ready.

No se intentará operar usando cache como fuente alternativa.

## 165. Infrastructure Definition of Done

La infraestructura estará lista para una release cuando:

-   imágenes construyen;
-   usuario no root funciona;
-   configuración está validada;
-   migraciones funcionan;
-   health checks funcionan;
-   staging despliega;
-   smoke tests pasan;
-   logs, métricas y traces llegan;
-   secrets no están en código;
-   backups existen;
-   restore fue probado;
-   rollback está documentado;
-   alertas críticas tienen runbook.

## 166. Checklist de servicio

``` text
[ ] Image pinned
[ ] Non-root user
[ ] Health checks
[ ] Resource limits
[ ] Graceful shutdown
[ ] Structured logs
[ ] Metrics
[ ] Traces
[ ] Secrets managed
[ ] Network access restricted
[ ] Timeouts configured
[ ] Retry policy defined
[ ] Deployment strategy defined
[ ] Runbook exists
```

## 167. Checklist de entorno

``` text
[ ] Environment isolated
[ ] Database isolated
[ ] Redis isolated

[ ] Buckets isolated
[ ] Provider credentials isolated
[ ] Domain and TLS configured
[ ] Backups configured
[ ] Monitoring configured
[ ] Alerts configured
[ ] Deployment permissions configured
[ ] Data policy documented
```

## 168. Checklist de release

``` text
[ ] CI green
[ ] Images scanned
[ ] OpenAPI compatible
[ ] Migrations reviewed
[ ] Backup verified
[ ] Staging validated
[ ] Evaluation gate passed
[ ] Security gate passed
[ ] Release notes prepared
[ ] Production approval granted
[ ] Smoke test prepared
[ ] Rollback or fix-forward plan prepared
```

## 169. Anti-patterns

Mutable Server Configurar producción manualmente por SSH.

Latest Tags No saber qué versión se ejecuta.

Secrets in Image Incluir claves durante build.

Database Migration on Every Replica Crear carreras durante startup.

Redis as Source of Truth Perder procesos al limpiar cache.

Unbounded Worker Concurrency Saturar proveedores y base de datos.

Public Database Exponer PostgreSQL a internet.

Shared Credentials Usar la misma clave en todos los entornos.

Unmonitored Background Task Proceso crítico sin estado ni métricas.

Rebuild Between Environments Probar una imagen y desplegar otra.

Backup Without Restore Asumir que un archivo de backup funciona.

Production Data in Staging Copiar datos sensibles sin sanitización.

## 170. Riesgos

IA-001 --- Complejidad operativa prematura Mitigación:

-   contenedores simples;
-   servicios administrados;
-   no Kubernetes inicial;
-   una sola aplicación modular.

IA-002 --- Dependencia excesiva de Redis Mitigación:

-   PostgreSQL como fuente de verdad;
-   procesos recuperables;
-   TTL;
-   degradación controlada.

IA-003 --- Costos AI sin control Mitigación:

-   cuotas;
-   métricas;
-   presupuestos;
-   límites por entorno;
-   fake gateway.

IA-004 --- Migraciones bloqueantes Mitigación:

-   expand and contract;
-   revisión;
-   staging;
-   timeouts;
-   migrator separado.

IA-005 --- Workers duplicando efectos Mitigación:

-   idempotencia;

-   inbox;

-   leases;

-   locks;

-   estados persistidos.

IA-006 --- Pérdida de documentos Mitigación:

-   object versioning;
-   backups;
-   checksums;
-   reconciliación.

IA-007 --- Falta de visibilidad Mitigación:

-   OpenTelemetry;
-   dashboards;
-   alertas;
-   runbooks;
-   release metadata.

IA-008 --- Lock-in de proveedor Mitigación:

-   adapters;
-   contratos;
-   IaC modular;
-   object storage compatible;
-   OpenTelemetry.

## 171. Preguntas de entrevista

Erick deberá poder explicar:

-   ¿Por qué no utilizar Kubernetes desde el inicio?

-   ¿Por qué API y worker pueden compartir imagen?

-   ¿Cómo evitas migraciones concurrentes?

-   ¿Cómo calculas el pool de conexiones?

-   ¿Qué información pondrías en Redis y cuál no?

-   ¿Cuándo usarías Pub/Sub y cuándo Streams?

-   ¿Cómo recuperas un job si el worker muere?

-   ¿Cómo manejas consistencia entre PostgreSQL y object storage?

-   ¿Cómo configuras SSE detrás de Nginx?

-   ¿Cómo implementas fallback entre proveedores AI?

-   ¿Qué diferencia existe entre retry y circuit breaker?

-   ¿Cómo evitas consumir proveedores reales en CI?

-   ¿Por qué staging debe parecerse a producción?

-   ¿Cómo despliegas una migración incompatible?

-   ¿Qué significa que una imagen sea inmutable?

-   ¿Cómo pruebas un backup?

-   ¿Cómo opera el sistema si Redis falla?

-   ¿Qué infraestructura debe estar definida como código?

-   ¿Cómo aplicarías least privilege?

-   ¿Qué métricas usarías para escalar workers?

## 172. Decisiones oficiales

Quedan aprobadas las siguientes decisiones:

## 1. Docker será el estándar de ejecución.

## 2. API y worker compartirán inicialmente la imagen backend.

## 3. El frontend se desplegará como artefacto estático.

## 4. Las imágenes tendrán versiones inmutables.

## 5. Producción no utilizará tags latest .

## 6. Los contenedores se ejecutarán como usuarios no root.

## 7. Se utilizarán builds multietapa.

## 8. Docker Compose será el entorno local inicial.

## 9. La configuración será tipada.

## 10. Los secretos no se almacenarán en el repositorio.

## 11. Staging y producción usarán secret management.

## 12. PostgreSQL administrado será la opción productiva preferida.

## 13. Las migraciones se ejecutarán como job separado.

## 14. Las migraciones deberán soportar rolling deployments.

## 15. Redis será cache y coordinación, no fuente de verdad.

## 16. Toda clave temporal de Redis tendrá TTL.

## 17. Pub/Sub podrá utilizarse para streaming efímero.

## 18. La tecnología de cola quedará detrás de un adapter.

## 19. Los workers tendrán estado, retries y dead letter.

## 20. Los workers deberán soportar graceful shutdown.

## 21. Object storage compatible con S3 será el estándar.

## 22. MinIO será el object storage local.

## 23. Los storage keys no otorgarán autorización.

## 24. Las signed URLs tendrán expiración corta.

## 25. El Model Gateway será el único acceso a proveedores LLM.

## 26. Las credenciales AI estarán separadas por entorno.

## 27. Los retries AI serán limitados y con backoff.

## 28. Los fallos repetidos podrán activar circuit breaker.

## 29. Los fallbacks deberán cumplir capabilities y presupuesto.

## 30. El reverse proxy deberá soportar SSE sin buffering.

## 31. PostgreSQL, Redis y storage no serán públicos.

## 32. CORS será restrictivo.

## 33. CI validará backend, frontend, contratos, seguridad e imágenes.

## 34. Staging se desplegará automáticamente desde main cuando sea viable.

## 35. Producción utilizará releases aprobadas.

## 36. La misma imagen se promoverá entre entornos.

## 37. El despliegue inicial será rolling.

## 38. Las migraciones destructivas utilizarán expand and contract.

## 39. OpenTelemetry Collector desacoplará la observabilidad.

## 40. Los logs estructurados irán a stdout.

## 41. Las alertas críticas tendrán owner y runbook.

## 42. Los backups deberán probarse mediante restore.

## 43. Redis no será parte del plan de recuperación de datos empresariales.

## 44. La infraestructura productiva se administrará como código.

## 45. Los entornos tendrán recursos y secretos separados.

## 46. Se aplicará least privilege.

## 47. El desarrollo local utilizará FakeModelGateway por defecto.

## 48. Las tools tendrán adapters sandbox.

## 49. Los entornos no productivos tendrán límites de costos AI.

## 50. Los procesos periódicos usarán un scheduler controlado.

## 51. Los smoke tests no producirán efectos empresariales reales.

## 52. La infraestructura deberá soportar degradación controlada.

## 53. PostgreSQL será requisito de readiness.

## 54. Proveedores AI no serán consultados desde cada readiness probe.

## 55. El primer despliegue no requerirá Kubernetes.

## 173. Próximo documento

Documento 17 --- Project 1 Testing Architecture Definirá de forma
implementable:

-   estrategia de pruebas;

-   pirámide de testing;

-   unit tests;

-   domain tests;

-   application tests;

-   repository tests;

-   API tests;

-   contract tests;

-   RLS tests;

-   worker tests;

-   provider adapter tests;

-   RAG evaluation;

-   tool evaluation;

-   approval tests;

-   security tests;

-   performance tests;

-   fixtures;

-   testcontainers;

-   CI gates;

-   coverage;

-   flaky tests;

-   datasets;

-   ejemplos completos con Pytest.

## 174. Conclusión

La infraestructura de GEEM AI Assistant queda definida como una
plataforma reproducible, contenida y preparada para evolucionar.

La primera versión evitará complejidad innecesaria, pero incorporará
desde el inicio las bases que distinguen a un producto experimental de
un sistema profesional:

-   configuración tipada;
-   imágenes inmutables;
-   procesos persistentes;
-   aislamiento de entornos;
-   administración de secretos;
-   migraciones controladas;
-   observabilidad;
-   backups;
-   recuperación;
-   despliegues verificables.

La infraestructura no será una colección de servidores configurados
manualmente.

Será un sistema versionado y operable que permitirá ejecutar la
arquitectura definida en los documentos anteriores sin perder seguridad,
trazabilidad ni capacidad de evolución.
