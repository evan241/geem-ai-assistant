# Project State

## Producto

GEEM AI Assistant

## Fase

Milestone 0 — Repository Foundation

## Estado actual

**Milestone 0 completado.**

La base del repositorio está establecida y validada contra la documentación
oficial del proyecto.

El repositorio cuenta con una arquitectura inicial definida, infraestructura
de desarrollo reproducible, persistencia base, validaciones automatizadas de
calidad y seguridad, pruebas de integración y documentación arquitectónica.

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
- CI con format, lint, typecheck, tests, coverage, dependency audits,
  container security scans y builds.
- GitHub Actions fijadas a referencias inmutables.
- Rama `main` protegida mediante GitHub Rulesets.

## Milestone 0 — Criterios completados

- [x] Incorporar documentos 00–18 en Markdown.
- [x] Revisar bootstrap contra documentos 12–18.
- [x] Definir ADR para identificadores.
- [x] Definir ADR para queue strategy.
- [x] Configurar Alembic.
- [x] Agregar migración inicial.
- [x] Implementar smoke tests de PostgreSQL y Redis.
- [x] Agregar pre-commit hooks completos.
- [x] Validar Docker en macOS.
- [x] Proteger rama `main`.
- [x] Crear GitHub Project y Milestone M0.

## Evidencia de cierre

Durante M0 se establecieron y validaron:

- documentación oficial AI Engineering Lab 00–09;
- documentación del Proyecto 1 10–18;
- Architecture Decision Records (ADR);
- revisión de cumplimiento arquitectónico de M0;
- configuración tipada de aplicación;
- baseline de persistencia y migraciones;
- PostgreSQL con pgvector;
- Redis;
- almacenamiento de objetos;
- health y readiness endpoints;
- pruebas de límites arquitectónicos;
- estrategia reproducible de dependencias;
- builds reproducibles de contenedores;
- pipeline CI de calidad y seguridad;
- exportación y validación del contrato OpenAPI;
- umbral mínimo de cobertura de pruebas del 85 %;
- escaneo de dependencias y contenedores;
- detección automatizada de secretos.

## Próxima fase

El repositorio queda preparado para iniciar el siguiente milestone del
GEEM AI Assistant.

Las nuevas capacidades funcionales deberán desarrollarse sobre las
decisiones arquitectónicas, estándares y controles establecidos durante M0.
