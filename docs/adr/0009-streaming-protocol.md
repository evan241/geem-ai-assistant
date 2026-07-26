# ADR-0009: Streaming Protocol

- Estado: Accepted
- Fecha: 2026-07-25
- Responsables: AI Engineering Lead

## Contexto

GEEM AI Assistant necesita comunicar al frontend el progreso de ejecuciones de
AI y otros procesos interactivos sin esperar a que toda la respuesta final
esté disponible.

El cliente deberá poder recibir eventos como:

- inicio de ejecución;
- fragmentos parciales de respuesta;
- progreso de retrieval;
- solicitudes de tools;
- solicitudes de aprobación;
- finalización;
- fallos.

La primera versión necesita una solución simple, compatible con HTTP y fácil de
operar detrás de proxies convencionales.

No se requiere inicialmente comunicación bidireccional permanente entre
frontend y backend.

## Decisión

Server-Sent Events (SSE) será el protocolo inicial para streaming desde la API
hacia clientes web.

Los streams pertenecerán a ejecuciones identificables.

Cada evento deberá incluir o poder asociarse de forma inequívoca con:

- execution ID;
- event type;
- event ID;
- orden dentro de la ejecución;
- schema version cuando aplique.

Los eventos conceptuales iniciales podrán incluir:

- `response.started`;
- `response.delta`;
- `retrieval.started`;
- `retrieval.completed`;
- `tool.requested`;
- `approval.required`;
- `response.completed`;
- `response.failed`.

Los eventos pertenecientes a una ejecución deberán emitirse en orden.

El frontend no utilizará el stream como única fuente de verdad del estado de
una ejecución.

El estado persistente permanecerá consultable mediante APIs REST.

Por ejemplo:

`GET /api/v1/assistant-executions/{execution_id}`

La primera versión podrá no soportar reanudación mediante `Last-Event-ID`.

Cuando una conexión SSE se interrumpa, el cliente deberá poder recuperar el
estado actual de la ejecución mediante la API.

La cancelación de una ejecución utilizará un endpoint explícito y será
best-effort.

La infraestructura de proxy deberá deshabilitar buffering para conexiones SSE
y utilizar timeouts apropiados para conexiones largas.

Los contratos de eventos deberán evolucionar de forma versionada y compatible.

## Alternativas consideradas

### WebSockets

No se adoptan como protocolo inicial.

WebSockets ofrecen comunicación bidireccional, pero introducen mayor
complejidad para:

- proxies;
- balanceadores;
- reconexión;
- observabilidad;
- infraestructura;
- escalamiento de conexiones.

La primera versión necesita principalmente comunicación server-to-client.

WebSockets podrán reconsiderarse si aparecen casos de uso que requieran
comunicación bidireccional de baja latencia.

### Polling periódico

No se adopta como mecanismo principal para respuestas progresivas.

El polling:

- introduce latencia artificial;
- genera requests repetitivos;
- no ofrece una experiencia fluida para tokens o eventos parciales.

Sin embargo, REST seguirá siendo el mecanismo de recuperación y reconciliación
del estado persistente.

### Streaming propietario del proveedor AI hasta el frontend

Rechazado.

El frontend no deberá depender de protocolos, SDKs o formatos específicos de
proveedores de modelos.

El backend normalizará los eventos del proveedor dentro del contrato SSE del
producto.

## Consecuencias

### Positivas

- protocolo HTTP estándar;
- implementación simple en navegador;
- adecuado para comunicación unidireccional;
- integración razonable con FastAPI y proxies;
- menor complejidad que WebSockets;
- separación entre streaming efímero y estado persistente;
- independencia del proveedor AI.

### Negativas

- comunicación únicamente server-to-client;
- conexiones largas requieren configuración específica de proxy;
- el manejo de reconexión requiere diseño explícito;
- la primera versión no garantiza replay de eventos perdidos.

## Riesgos

- utilizar SSE como fuente de verdad del estado;
- eventos fuera de orden;
- buffering accidental en proxies;
- conexiones abandonadas sin cleanup;
- incompatibilidad de schemas entre frontend y backend;
- pérdida de eventos durante desconexiones;
- acoplar el contrato SSE a formatos de un proveedor AI;
- enviar datos sensibles en eventos que no deberían exponerse al cliente.

## Validación

La decisión se considerará correctamente aplicada cuando:

- las respuestas progresivas utilicen SSE;
- los eventos tengan tipos y contratos explícitos;
- todos los eventos puedan asociarse a una execution;
- el orden de eventos por ejecución esté protegido;
- el estado final pueda consultarse mediante REST;
- una desconexión del stream no provoque pérdida del estado persistente;
- el proxy tenga buffering deshabilitado para SSE;
- existan métricas de conexiones, duración, fallos y desconexiones;
- frontend y backend compartan contratos compatibles;
- el proveedor AI permanezca oculto detrás de la normalización del backend.

## Referencias

- Documento 11 — Project 1 Architecture Definition
- Documento 13 — Project 1 API & Contract Standards
- Documento 15 — Project 1 Application Architecture
- Documento 16 — Project 1 Infrastructure Architecture
- Issue #7 — Establish initial ADR set