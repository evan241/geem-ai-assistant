# Architecture Decision Records

Los Architecture Decision Records (ADRs) documentan decisiones arquitectónicas
significativas de GEEM AI Assistant.

## Formato

`NNNN-titulo.md`

## Estados

- Proposed
- Accepted
- Superseded
- Deprecated
- Rejected

## ADRs

| ADR | Decisión | Estado |
|---|---|---|
| [ADR-0001](0001-modular-monolith.md) | Modular Monolith | Accepted |
| [ADR-0002](0002-identifier-strategy.md) | Identifier Strategy | Accepted |
| [ADR-0003](0003-multi-tenant-data-isolation.md) | Multi-Tenant Data Isolation | Accepted |
| [ADR-0004](0004-model-gateway.md) | Model Gateway | Accepted |
| [ADR-0005](0005-prompt-storage.md) | Prompt Storage | Accepted |
| [ADR-0006](0006-document-storage.md) | Document Storage | Accepted |
| [ADR-0007](0007-background-job-system.md) | Background Job System | Accepted |
| [ADR-0008](0008-vector-search-strategy.md) | Vector Search Strategy | Accepted |
| [ADR-0009](0009-streaming-protocol.md) | Streaming Protocol | Accepted |
| [ADR-0010](0010-mcp-deployment-model.md) | MCP Deployment Model | Accepted |

## Reglas

Un ADR deberá crearse cuando una decisión:

- cambie límites arquitectónicos;
- introduzca infraestructura relevante;
- defina una estrategia transversal;
- altere contratos fundamentales;
- tenga alternativas razonables con consecuencias significativas.

Los ADRs aceptados no deberán reescribirse para ocultar decisiones anteriores.

Cuando una decisión cambie de forma significativa, deberá crearse un nuevo ADR
que marque explícitamente al anterior como `Superseded`.

Los documentos de arquitectura definen el diseño general.

Los ADRs registran decisiones concretas tomadas durante la construcción del
sistema.