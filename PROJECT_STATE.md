# Project State

## Producto

GEEM AI Assistant

## Fase

Milestone 0 — Repository Foundation

## Estado actual

Bootstrap inicial creado.

## Decisiones aplicadas

- Modular monolith.
- Backend FastAPI.
- Frontend React + TypeScript + Vite.
- PostgreSQL + pgvector.
- Redis como infraestructura temporal, no fuente de verdad.
- Aplicaciones separadas: API, Web, Worker y MCP.
- Código de dominio bajo `src/geem_ai`.
- Módulos con API pública explícita.
- Git como fuente de verdad inicial.
- CI con format, lint, typecheck, tests y builds.

## Pendientes antes de considerar M0 completo

- [ ] Incorporar documentos 00–18 en Markdown.
- [ ] Revisar bootstrap contra documentos 12–18.
- [ ] Definir ADR para identificadores.
- [ ] Definir ADR para queue strategy.
- [ ] Configurar Alembic.
- [ ] Agregar migración inicial.
- [ ] Implementar smoke test de PostgreSQL y Redis.
- [ ] Agregar pre-commit hooks completos.
- [ ] Validar Docker en macOS.
- [ ] Proteger rama `main`.
- [ ] Crear GitHub Project y Milestone M0.
