# Contributing

## Branches

- `feat/<issue>-descripcion`
- `fix/<issue>-descripcion`
- `docs/<issue>-descripcion`
- `chore/<issue>-descripcion`

## Commits

Conventional Commits:

- feat
- fix
- docs
- test
- refactor
- chore
- ci

## Regla de módulos

Un módulo no puede importar infraestructura interna de otro módulo.

Puede consumir únicamente:

- public API;
- DTOs públicos;
- application services públicos;
- eventos;
- puertos definidos.

## Definition of Done

- pruebas;
- typecheck;
- lint;
- documentación;
- seguridad;
- multi-tenancy cuando aplique;
- observabilidad;
- ADR si cambia arquitectura.
