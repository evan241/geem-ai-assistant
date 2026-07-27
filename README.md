# GEEM AI Assistant

Proyecto 1 del AI Engineering Lab.

GEEM AI Assistant es una plataforma de asistente empresarial con arquitectura
modular, diseñada para integrar conversaciones, conocimiento, memoria,
herramientas, aprobaciones y capacidades de inteligencia artificial de forma
segura, trazable y multi-tenant.

## Estado

En desarrollo activo.

- **Milestone 0 — Repository Foundation:** completado.
- **Milestone 1 — First Conversation:** en progreso.

Actualmente el proyecto cuenta con la infraestructura base y el dominio inicial
necesarios para construir el primer flujo completo de conversación.

## Stack principal

### Backend

- Python 3.12
- FastAPI
- SQLAlchemy 2
- Alembic
- PostgreSQL
- pgvector
- Redis
- Pytest
- Ruff
- MyPy

### Frontend

- React
- TypeScript
- Vite
- pnpm

### Infraestructura

- Docker Compose
- MinIO / almacenamiento compatible con S3
- OpenTelemetry
- GitHub Actions
- worker
- MCP

## Arquitectura

El backend sigue una arquitectura de **modular monolith** organizada por
bounded contexts.

Entre los módulos principales se encuentran:

- conversations
- knowledge
- memory
- retrieval
- ai_runtime
- tools
- approvals
- identity
- organizations
- administration
- audit
- evaluation
- observability
- shared

La separación principal dentro de cada módulo sigue las capas:

```text
domain
application
infrastructure
presentation
```

La lógica de dominio no debe depender de infraestructura ni de frameworks de
presentación.

## Persistencia

La persistencia principal utiliza PostgreSQL y SQLAlchemy.

Las modificaciones al esquema se administran mediante Alembic:

```bash
uv run alembic current
uv run alembic upgrade head
uv run alembic check
```

El proyecto utiliza migraciones versionadas y convenciones de nombres para
constraints e índices.

## Requisitos

### Desarrollo con Docker

- Docker Desktop
- Git
- Make (opcional)

### Desarrollo local

- Python 3.12.13
- uv 0.11.32
- Node.js 20.20.2
- pnpm 9.15.4

Las versiones baseline están fijadas mediante:

- `.python-version`
- `.nvmrc`
- `uv.lock`
- `pnpm-lock.yaml`

## Inicio rápido

```bash
cp .env.example .env
docker compose up --build
```

Servicios locales:

- Web: `http://localhost:5173`
- API: `http://localhost:8000`
- API health: `http://localhost:8000/health`
- API docs: `http://localhost:8000/docs`
- MinIO console: `http://localhost:9001`
- PostgreSQL: `localhost:5432`
- Redis: `localhost:6379`

## Comandos de desarrollo

```bash
make up
make down
make logs
make test
make lint
make format
make typecheck
```

También pueden ejecutarse directamente las herramientas del backend:

```bash
uv run pytest
uv run ruff format .
uv run ruff check .
uv run mypy src apps
uv run pre-commit run --all-files
```

## Migraciones

Para aplicar las migraciones pendientes:

```bash
uv run alembic upgrade head
```

Para comprobar que los modelos ORM y el esquema versionado están sincronizados:

```bash
uv run alembic check
```

La variable `GEEM_DATABASE_URL` debe estar configurada antes de ejecutar
operaciones de Alembic.

## Pruebas

El proyecto contiene pruebas:

- unitarias;
- de integración;
- de arquitectura;
- de API;
- de infraestructura.

Ejemplo:

```bash
uv run pytest
```

La suite incluye validaciones sobre los límites arquitectónicos entre módulos y
capas.

## Calidad

Antes de integrar cambios se espera ejecutar:

```bash
uv run ruff format .
uv run ruff check .
uv run mypy src apps
uv run pytest
uv run pre-commit run --all-files
```

Los Pull Requests también son validados mediante CI.

## Documentación oficial

La arquitectura y las decisiones del proyecto se encuentran en:

- `docs/lab/` — documentación base del AI Engineering Lab.
- `docs/project-1/` — especificación arquitectónica de GEEM AI Assistant.
- `docs/adr/` — Architecture Decision Records.

La documentación oficial define las restricciones arquitectónicas del proyecto.

No se debe introducir lógica de negocio, infraestructura o decisiones de diseño
que contradigan dichos documentos sin actualizar primero la decisión
arquitectónica correspondiente.

## Desarrollo actual

El trabajo actual corresponde a:

**M1 — First Conversation**

El objetivo del milestone es completar el primer flujo vertical de conversación,
desde la creación de una conversación hasta la generación y entrega de una
respuesta del asistente.

El progreso detallado y los criterios de aceptación se mantienen en las issues
del milestone correspondiente.
