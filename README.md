# GEEM AI Assistant

Proyecto 1 del AI Engineering Lab.

## Estado

Bootstrap de **Milestone 0 — Repository Foundation**.

Esta base incluye:

- FastAPI;
- React + TypeScript + Vite;
- PostgreSQL + pgvector;
- Redis;
- worker;
- MCP placeholder;
- Docker Compose;
- Ruff, MyPy y Pytest;
- ESLint y Prettier;
- GitHub Actions;
- estructura modular monolith.

## Requisitos

- Docker Desktop
- Git
- Make (opcional)

Para desarrollo local sin Docker:

- Python 3.12.13
- uv 0.11.16
- Node.js 20.20.2
- pnpm 9.15.4

Las versiones baseline están fijadas mediante `.python-version`, `.nvmrc`,
`uv.lock` y `pnpm-lock.yaml`.

## Inicio rápido

```bash
cp .env.example .env
docker compose up --build
```

Servicios:

- Web: http://localhost:5173
- API: http://localhost:8000
- API health: http://localhost:8000/health
- API docs: http://localhost:8000/docs
- MinIO console: http://localhost:9001
- PostgreSQL: localhost:5432
- Redis: localhost:6379

## Comandos

```bash
make up
make down
make logs
make test
make lint
make format
make typecheck
```

## Documentación oficial

- `docs/lab/`: documentos 00–09.
- `docs/project-1/`: documentos 10–18.
- `docs/adr/`: decisiones arquitectónicas.

No se debe introducir lógica de negocio que contradiga los documentos oficiales.
