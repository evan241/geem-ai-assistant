# ADR-0010: MCP Deployment Model

- Estado: Accepted
- Fecha: 2026-07-25
- Responsables: AI Engineering Lead

## Contexto

GEEM AI Assistant expondrá capacidades mediante Model Context Protocol para
clientes AI compatibles.

MCP podrá ofrecer resources, prompts y tools relacionados con capacidades como:

- consulta de documentos;
- búsqueda de conocimiento;
- historial de conversaciones;
- catálogo de tools;
- operaciones autorizadas mediante tools.

MCP introduce una nueva frontera de transporte, autenticación y contratos, pero
no debe convertirse en una segunda implementación de la lógica empresarial.

La arquitectura necesita definir si MCP:

- vive dentro del proceso HTTP principal;
- se despliega como proceso independiente;
- replica reglas de negocio;
- reutiliza los mismos casos de uso y políticas del sistema.

## Decisión

MCP se implementará como un entry point y proceso independiente bajo:

`apps/mcp/`

MCP no será propietario de lógica de negocio.

Los handlers MCP deberán reutilizar los mismos contratos públicos y casos de
uso de Application utilizados por otros entry points.

La arquitectura conceptual será:

MCP Client
→ MCP Transport
→ Authentication
→ Tenant Resolution
→ MCP Resource or Tool Handler
→ Application Use Case
→ Audit and Telemetry

MCP deberá reutilizar:

- autenticación;
- autorización;
- tenant context;
- application use cases;
- Tool Registry;
- approval policies;
- Audit;
- Observability.

Un MCP resource deberá mapearse a una query o application service existente.

Una MCP tool deberá mapearse a:

- command;
- application service;
- Tool Registry;
- o coordinador explícitamente autorizado.

MCP no podrá acceder directamente a repositories o tablas para evitar las
políticas de Application.

Los URIs MCP identificarán recursos, pero no concederán autorización por sí
mismos.

Todo acceso deberá resolver actor, tenant y permisos antes de recuperar o
modificar información.

Las MCP tools no podrán evitar:

- permisos;
- tenant isolation;
- risk classification;
- approval;
- audit;
- rate limits;
- idempotency.

Las tools con efectos de negocio continuarán siguiendo el mismo flujo de
ToolExecution y Approval utilizado por el resto de la aplicación.

Los errores internos deberán mapearse a errores MCP seguros.

No se expondrán:

- stack traces;
- credenciales;
- detalles internos de infraestructura;
- datos no autorizados.

El proceso MCP podrá desplegarse, escalarse o deshabilitarse independientemente
del proceso API cuando la infraestructura lo permita.

Esta independencia de deployment no implica independencia de dominio ni
duplicación de lógica.

## Alternativas consideradas

### Ejecutar MCP dentro del proceso API

No se adopta como modelo principal.

Compartir el mismo proceso simplificaría inicialmente el despliegue, pero
acoplaría:

- ciclo de vida;
- escalamiento;
- exposición de red;
- configuración;
- observabilidad;
- superficie de seguridad.

Un entry point separado mantiene fronteras operativas más claras.

### Crear un microservicio MCP con lógica empresarial propia

Rechazado.

Duplicaría:

- autorización;
- tenant resolution;
- reglas de negocio;
- Tool Registry;
- approvals;
- auditoría.

Además aumentaría el riesgo de que API y MCP produzcan comportamientos
diferentes para la misma operación.

### Permitir acceso MCP directo a persistence

Rechazado.

El acceso directo a repositories o tablas podría evitar:

- autorización;
- reglas de dominio;
- aislamiento tenant;
- auditoría;
- invariantes;
- políticas de approval.

## Consecuencias

### Positivas

- frontera MCP explícita;
- reutilización de lógica empresarial;
- comportamiento consistente entre API y MCP;
- despliegue independiente cuando sea útil;
- menor riesgo de bypass de autorización;
- observabilidad específica del transporte;
- posibilidad de limitar o deshabilitar MCP por ambiente.

### Negativas

- existe un proceso adicional que operar;
- requiere autenticación y configuración específicas;
- los contratos MCP deberán mantenerse junto con los contratos de Application;
- algunos use cases podrán requerir adapters de presentación específicos para
  MCP.

## Riesgos

- duplicar lógica dentro de handlers MCP;
- permitir acceso directo a infraestructura;
- confiar en un URI como mecanismo de autorización;
- ejecutar tools sin approval;
- resolver incorrectamente el tenant desde credenciales MCP;
- exponer demasiado contenido mediante resources;
- diferencias de comportamiento entre MCP y API;
- logs o errores MCP conteniendo información sensible;
- ampliar la superficie pública sin controles de rate limiting.

## Validación

La decisión se considerará correctamente aplicada cuando:

- exista un entry point MCP separado;
- MCP reutilice Application y APIs públicas de módulos;
- ningún handler MCP implemente reglas de negocio propias;
- MCP no consulte tablas de negocio directamente;
- authentication, authorization y tenant resolution se ejecuten en cada
  operación aplicable;
- resources filtren información según permisos;
- tools respeten riesgo, approval, audit e idempotencia;
- errores MCP no filtren detalles internos;
- existan MCP conformance/contract tests;
- las operaciones equivalentes mantengan comportamiento consistente entre API
  y MCP;
- el proceso MCP pueda habilitarse y desplegarse independientemente cuando sea
  necesario.

## Referencias

- Documento 11 — Project 1 Architecture Definition
- Documento 13 — Project 1 API & Contract Standards
- Documento 15 — Project 1 Application Architecture
- Documento 16 — Project 1 Infrastructure Architecture
- Issue #7 — Establish initial ADR set