# Working with ChatGPT

## Fuente de verdad

El repositorio es la fuente oficial. La conversación sirve para analizar, diseñar y revisar.

## Inicio de cada sesión

Compartir:

- `PROJECT_STATE.md`;
- issue activo;
- diff de la rama;
- archivos involucrados;
- salida de pruebas.

## Plantilla

```text
Proyecto: GEEM AI Assistant
Milestone:
Issue:
Objetivo:
Archivos afectados:
Restricciones:
Criterios de aceptación:
Pruebas esperadas:
```

## Revisión

```bash
git diff main...HEAD > review.diff
```

Adjuntar `review.diff` y, cuando haga falta, los archivos completos.

## Cierre de tarea

- actualizar `PROJECT_STATE.md`;
- actualizar ADR o `DECISIONS.md`;
- registrar pruebas;
- documentar riesgos;
- vincular issue y PR.
