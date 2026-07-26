# AI Engineering Lab

## Documento 08 — Observability Strategy

**Versión:** 1.0
**Estado:** Estrategia oficial
**Responsable técnico:** Director de AI Engineering
**Lead Engineer:** Erick Eduardo Evangelista Velasco

## 1. Propósito

Este documento define la estrategia oficial de observabilidad para todos los proyectos del AI Engineering Lab.

Su objetivo es permitir que cualquier flujo importante pueda:

- rastrearse;
- medirse;
- diagnosticarse;
- auditarse;
- compararse;
- optimizarse;
- recuperarse.

La observabilidad deberá cubrir tanto los componentes tradicionales de software como los componentes probabilísticos de inteligencia artificial.

Esto incluye:

- frontend;
- APIs;
- casos de uso;
- módulos;
- base de datos;
- Redis;
- almacenamiento;
- workers;
- colas;
- proveedores LLM;
- embeddings;
- retrieval;
- herramientas;
- agentes;
- workflows;
- MCP;
- integraciones;
- costos;
- evaluaciones.

## 2. Principio rector

> Un sistema que funciona pero no puede explicarse cuando falla no está listo para producción.

La observabilidad deberá permitir responder:

- ¿Qué ocurrió?
- ¿Cuándo ocurrió?
- ¿A quién afectó?
- ¿En qué tenant?
- ¿Qué componente falló?
- ¿Qué modelo se utilizó?
- ¿Qué fuentes fueron recuperadas?
- ¿Qué herramienta se ejecutó?
- ¿Qué costo tuvo?
- ¿Qué decisión tomó el sistema?
- ¿Cómo puede reproducirse?
- ¿Cómo puede corregirse?

## 3. Diferencia entre monitoreo y observabilidad

## Monitoreo

Responde preguntas conocidas mediante:

- dashboards;
- métricas;
- alertas;
- health checks.

Ejemplo:

> ¿La tasa de errores superó el 5%?

## Observabilidad

Permite investigar situaciones no previstas mediante:

- logs;
- traces;
- métricas;
- eventos;
- relaciones;
- contexto.

Ejemplo:

> ¿Por qué aumentaron los errores de tool calling únicamente en un tenant después de cambiar el prompt?

Ambos serán necesarios.

## 4. Objetivos de observabilidad

La estrategia deberá proporcionar:

## Visibilidad técnica

Estado de servicios, infraestructura e integraciones.

## Visibilidad AI

Modelos, prompts, retrieval, tools, agentes y evaluaciones.

## Visibilidad de negocio

Impacto real de las capacidades.

## Detección

Identificación temprana de fallos y degradaciones.

## Diagnóstico

Capacidad de localizar causas.

## Auditoría

Reconstrucción de acciones importantes.

## Optimización

Mejora de costo, latencia, calidad y disponibilidad.

## 5. Estándar principal

El estándar de instrumentación será:

# OpenTelemetry

Se utilizará para unificar:

- traces;
- metrics;
- logs cuando corresponda;
- propagación de contexto;
- instrumentación;
- exportación.

La arquitectura no dependerá de un único proveedor de observabilidad.

## 6. Arquitectura general

`text id="q5twlp" Applications     │     ├── API     ├── Web     ├── Workers     ├── MCP Server     ├── Workflows     └── AI Components             │             ▼       OpenTelemetry SDK             │             ▼       OpenTelemetry Collector             │      ┌──────┼─────────┐      ▼      ▼         ▼    Traces  Metrics    Logs      │      │         │      └──────┴─────────┘             │             ▼    Observability Backend`

## 7. Señales fundamentales

La estrategia se basará en tres señales principales.

## Logs

Eventos discretos con contexto.

## Metrics

Valores numéricos agregables.

## Traces

Recorrido completo de una ejecución.

Estas señales deberán relacionarse mediante identificadores comunes.

## 8. Señales adicionales

Para sistemas AI se registrarán también:

- prompts;
- versiones;
- modelos;
- tokens;
- costos;
- retrieval results;
- scores;
- tool calls;
- agent steps;
- approvals;
- evaluations;
- feedback.

No todos estos datos deberán almacenarse íntegramente.

Se aplicarán seguridad, redacción y retención.

## 9. Contexto de correlación

Toda ejecución relevante deberá incluir:

`text id="lz38tu" correlation_id trace_id span_id execution_id tenant_id user_id session_id`

Cuando aplique también:

`text id="gw4npz" conversation_id workflow_id agent_run_id tool_call_id document_id evaluation_run_id`

## 10. Correlation ID

El `correlation_id` identificará una operación lógica completa.

Ejemplo:

`text id="cb3p0p" User request    │    ├── API    ├── Retrieval    ├── Model    ├── Tool    └── Response`

Todos los registros relacionados deberán conservar el mismo identificador.

## 11. Trace ID

El `trace_id` será administrado por OpenTelemetry.

Representará el flujo técnico distribuido.

Permitirá seguir una solicitud a través de:

- API;
- workers;
- base de datos;
- modelos;
- tools;
- sistemas externos.

## 12. Execution ID

El `execution_id` identificará una ejecución funcional.

Ejemplos:

- una respuesta del asistente;
- una ingestión;
- un reporte;
- un workflow;
- una evaluación;
- una ejecución agéntica.

A diferencia del trace ID, podrá persistir como concepto del dominio operativo.

## 13. Propagación de contexto

Los identificadores deberán propagarse mediante:

- headers HTTP;
- metadata de colas;
- eventos;
- jobs;
- MCP;
- webhooks internos;
- logs;
- tool calls.

La pérdida de contexto entre servicios deberá considerarse un defecto de observabilidad.

## 14. Logging estructurado

Los logs deberán emitirse en formato estructurado.

Ejemplo:

`json id="5tyrm9" {   "timestamp": "2026-01-01T12:00:00Z",   "level": "INFO",   "service": "geem-ai-api",   "environment": "staging",   "event": "assistant_response_completed",   "tenant_id": "tenant-demo",   "user_id": "user-123",   "correlation_id": "corr-456",   "trace_id": "trace-789",   "execution_id": "exec-321",   "duration_ms": 4280 }`

## 15. Niveles de log

## TRACE

Detalle extremadamente fino para diagnóstico controlado.

## DEBUG

Información técnica de desarrollo.

## INFO

Eventos normales importantes.

## WARN

Condiciones anormales recuperables.

## ERROR

Fallo de una operación.

## CRITICAL

Fallo grave con impacto alto.

Producción no deberá generar DEBUG de forma permanente salvo activación controlada.

## 16. Eventos de log

Los logs deberán usar nombres consistentes.

Ejemplos:

`text id="s52rno" request_received request_completed authentication_failed authorization_denied document_uploaded document_indexed retrieval_completed model_call_completed tool_execution_requested tool_execution_failed approval_created agent_run_completed workflow_failed`

## 17. Regla sobre mensajes libres

Los mensajes de log deberán ser comprensibles.

Sin embargo, la información principal deberá estar en campos estructurados.

## Evitar

`text id="2w56n8" Something went wrong.`

## Preferir

`json id="zfr9db" {   "event": "tool_execution_failed",   "tool_name": "create_support_ticket",   "error_code": "EXTERNAL_TIMEOUT",   "retryable": true }`

## 18. Datos prohibidos en logs

No deberán registrarse directamente:

- contraseñas;
- tokens;
- API keys;
- secretos;
- cookies;
- documentos completos;
- prompts completos con información sensible;
- respuestas completas restringidas;
- datos fiscales;
- información personal innecesaria;
- credenciales OAuth;
- headers de autorización.

## 19. Redacción

La redacción deberá realizarse antes de persistir.

Campos comunes:

`text id="u79dd8" password authorization api_key access_token refresh_token client_secret cookie secret`

Los valores deberán sustituirse por una representación segura.

Ejemplo:

`text id="3f5p3p" [REDACTED]`

## 20. Hashing para correlación segura

Cuando se requiera correlacionar un dato sensible sin almacenarlo, podrá utilizarse:

- hash;
- identificador interno;
- tokenización.

No se utilizará hashing débil para datos fácilmente reversibles por diccionario sin una razón controlada.

## 21. Logging de prompts

Por defecto se registrará:

- prompt name;
- prompt version;
- template ID;
- tamaño;
- hash;
- variables no sensibles;
- clasificación de datos.

El contenido completo solo se almacenará cuando:

- exista necesidad;
- esté permitido;
- esté sanitizado;
- tenga retención limitada;
- el ambiente sea adecuado.

## 22. Logging de respuestas AI

Se registrará:

- modelo;
- proveedor;
- versión;
- finish reason;
- tokens;
- latencia;
- output schema;
- validación;
- error;
- hash del resultado.

El contenido podrá almacenarse de forma controlada para:

- evaluación;
- debugging;
- auditoría;
- feedback.

## 23. Logs de base de datos

Se registrarán:

- operación lógica;
- duración;
- filas afectadas;
- errores;
- timeouts;
- deadlocks.

No se registrará SQL completo con valores sensibles en producción por defecto.

## 24. Logs de herramientas

Toda tool deberá registrar:

- tool name;
- tool version;
- risk level;
- actor;
- tenant;
- argumentos sanitizados;
- aprobación;
- inicio;
- resultado;
- duración;
- error;
- idempotency key.

## 25. Logs de aprobaciones

Se registrará:

- solicitud;
- acción;
- riesgo;
- solicitante;
- aprobador;
- decisión;
- expiración;
- argumentos vinculados;
- resultado final.

## 26. Logs de agentes

Cada ejecución deberá registrar:

- agent name;
- agent version;
- objective;
- state ID;
- step count;
- current node;
- tools used;
- model calls;
- termination reason;
- duration;
- cost;
- outcome.

## 27. Tracing distribuido

Cada request deberá generar un trace raíz.

Los principales componentes deberán crear spans.

Ejemplo:

`text id="m6y7ra" assistant.request ├── auth.validate ├── tenant.resolve ├── conversation.load ├── retrieval.search │   ├── embedding.generate │   ├── vector.search │   ├── fulltext.search │   └── rerank ├── model.generate ├── tool.authorize ├── tool.execute └── response.persist`

## 28. Convención de nombres de spans

Los nombres deberán representar operaciones.

Ejemplos:

`text id="e1m1r3" http.request db.query cache.get retrieval.search embedding.generate llm.generate tool.execute agent.node workflow.step`

No deberán incluir IDs dinámicos en el nombre.

Los IDs deberán ir como atributos.

## 29. Atributos de spans

Atributos generales:

`text id="edbbu6" service.name deployment.environment tenant.id user.id execution.id operation.name`

Atributos AI:

`text id="b1irzj" gen_ai.provider gen_ai.model gen_ai.operation gen_ai.prompt.version gen_ai.input.tokens gen_ai.output.tokens gen_ai.cost`

Los nombres definitivos deberán alinearse con las convenciones vigentes de OpenTelemetry cuando se implemente.

## 30. Spans de proveedores AI

Cada llamada deberá incluir:

- proveedor;
- modelo;
- operación;
- prompt version;
- input tokens;
- output tokens;
- total tokens;
- latencia;
- retries;
- timeout;
- status;
- finish reason;
- costo estimado.

## 31. Spans de retrieval

Cada retrieval deberá incluir:

- estrategia;
- query hash;
- tenant;
- filtros;
- top K;
- candidatos;
- resultados;
- scores;
- latencia;
- índice;
- reranking;
- sources selected.

## 32. Spans de tools

Cada tool call deberá incluir:

- tool name;
- version;
- risk level;
- approval status;
- authorized;
- tenant;
- duration;
- result status;
- retry count;
- external system.

## 33. Spans de agentes

Cada nodo de un agente deberá crear un span.

Atributos:

- agent;
- graph version;
- node;
- step;
- transition;
- state size;
- tool;
- model;
- termination condition.

## 34. Spans de workers

Los trabajos asíncronos deberán conservar el trace parent cuando sea posible.

Si no es posible, deberán relacionarse mediante:

- links;
- correlation ID;
- execution ID.

## 35. Sampling de traces

No todos los traces deberán conservarse indefinidamente.

Se utilizará sampling basado en:

- ambiente;
- error;
- latencia;
- costo;
- tenant;
- tipo de flujo;
- riesgo.

## Reglas iniciales

### Development

Sampling alto o completo.

### Staging

Sampling alto.

### Production

Sampling controlado, preservando:

- errores;
- acciones críticas;
- tools de alto riesgo;
- latencia anormal;
- ejecuciones costosas;
- incidentes.

## 36. Tail-Based Sampling

Cuando la plataforma lo permita se evaluará tail-based sampling.

Esto permitirá conservar traces basados en el resultado final.

Ejemplos:

- todos los errores;
- requests mayores a cierto tiempo;
- costos superiores al presupuesto;
- herramientas críticas;
- fallos de seguridad.

## 37. Métricas del sistema

Métricas mínimas:

- request count;
- error rate;
- latency;
- throughput;
- active users;
- active tenants;
- queue depth;
- job failures;
- database connections;
- cache hit rate;
- storage use;
- CPU;
- memory.

## 38. RED Method

Para servicios HTTP se utilizará:

## Rate

Número de solicitudes.

## Errors

Número o proporción de errores.

## Duration

Duración de solicitudes.

## 39. USE Method

Para recursos de infraestructura se utilizará:

## Utilization

Uso del recurso.

## Saturation

Nivel de espera o cola.

## Errors

Errores asociados.

## 40. Métricas AI

Se registrarán:

- model calls;
- tokens;
- cost;
- latency;
- retries;
- output validation failures;
- tool calls;
- retrieval metrics;
- agent steps;
- evaluation results;
- abstention;
- hallucination indicators;
- feedback.

## 41. Tokens

Se medirán:

- input tokens;
- output tokens;
- cached tokens cuando aplique;
- reasoning tokens cuando el proveedor los exponga;
- total tokens.

Se agregará por:

- tenant;
- usuario;
- modelo;
- feature;
- workflow;
- día;
- versión.

## 42. Costos

El costo deberá registrarse por:

- request;
- conversación;
- documento;
- agente;
- workflow;
- tenant;
- feature;
- proveedor;
- modelo.

La estimación deberá usar una tabla de precios versionada.

## 43. Cost Attribution

Todo costo deberá poder atribuirse a una unidad funcional.

Ejemplo:

`text id="e6dzqg" tenant   └── feature       └── execution           ├── model calls           ├── embeddings           ├── reranking           └── tools`

## 44. Presupuestos

Cada flujo deberá tener límites.

Ejemplos:

- costo máximo por consulta;
- costo máximo por agente;
- tokens máximos;
- tool calls máximas;
- pasos máximos.

Se registrará cualquier exceso.

## 45. Métricas de Model Gateway

El gateway deberá medir:

- requests por proveedor;
- requests por modelo;
- success rate;
- error rate;
- timeout rate;
- retry rate;
- fallback rate;
- latency;
- tokens;
- cost;
- structured output success.

## 46. Fallback Rate

Mide la proporción de solicitudes que utilizaron un proveedor o modelo alterno.

Un aumento puede indicar:

- proveedor inestable;
- configuración incorrecta;
- límites;
- errores del modelo.

## 47. Structured Output Failure Rate

Mide las respuestas que no cumplen el esquema.

Se distinguirá:

- fallo inicial;
- éxito tras reparación;
- fallo final.

## 48. Métricas RAG

Se medirán:

- documents ingested;
- processing success;
- processing failure;
- chunk count;
- embedding count;
- retrieval latency;
- retrieval hit rate;
- context size;
- citations;
- abstention;
- source authorization;
- reindexing.

## 49. Métricas de ingestión

- uploads;
- accepted files;
- rejected files;
- extraction failures;
- indexing failures;
- processing time;
- queue wait time;
- duplicate rate;
- document size;
- pages processed.

## 50. Métricas de retrieval

- queries;
- top K;
- candidates;
- vector latency;
- full-text latency;
- rerank latency;
- results selected;
- empty retrieval rate;
- low-score rate.

## 51. Métricas de contexto

- context tokens;
- chunks included;
- documents included;
- duplicate chunks removed;
- context truncation rate;
- unauthorized source attempts.

## 52. Métricas de citas

- responses with citations;
- citation count;
- invalid citations;
- unsupported claims;
- citation click-through cuando exista interfaz;
- source availability.

## 53. Métricas de tools

- tool selection;
- tool execution;
- success;
- failure;
- unauthorized attempts;
- approvals;
- rejected approvals;
- duplicate prevention;
- retries;
- latency.

## 54. Métricas de aprobación

- requests created;
- approved;
- rejected;
- expired;
- approval time;
- execution after approval;
- bypass attempts.

## 55. Métricas de agentes

- runs;
- completion rate;
- failure rate;
- termination reason;
- step count;
- loop detection;
- tool count;
- model count;
- cost;
- latency;
- human intervention.

## 56. Métricas de workflows

- executions;
- success;
- failures;
- retries;
- duration;
- queue time;
- duplicate events;
- dead-letter count;
- compensations;
- manual interventions.

## 57. Métricas de memoria

- memories created;
- memories retrieved;
- correction rate;
- expiration rate;
- deletion rate;
- contamination attempts;
- retrieval usefulness;
- rejected memories.

## 58. Métricas de seguridad

- authentication failures;
- authorization denials;
- tenant isolation violations;
- prompt injection detections;
- tool abuse attempts;
- secret detections;
- rate limit hits;
- suspicious uploads;
- role changes;
- export events.

## 59. Métricas de negocio

La observabilidad deberá incluir métricas relacionadas con valor.

## GEEM AI Assistant

- consultas resueltas;
- consultas escaladas;
- tiempo de búsqueda;
- documentos utilizados;
- acciones completadas;
- satisfacción.

## Restaurant AI Operations

- reportes generados;
- anomalías detectadas;
- propuestas aprobadas;
- ahorros estimados;
- desperdicio identificado;
- tiempo de análisis.

## Enterprise Automation Platform

- workflows completados;
- horas ahorradas;
- errores evitados;
- tiempo de respuesta;
- tareas manuales eliminadas;
- tasa de éxito.

## 60. Labels y cardinalidad

Las métricas deberán evitar labels de alta cardinalidad.

## No recomendado

- prompt completo;
- document ID;
- user email;
- conversation ID;
- error message completo.

## Permitido con cautela

- tenant;
- model;
- provider;
- environment;
- feature;
- status.

Cuando la cantidad de tenants crezca, deberá evaluarse el impacto de incluir tenant como label.

## 61. Histograms

Las latencias deberán medirse mediante histogramas.

Se reportarán:

- p50;
- p90;
- p95;
- p99.

El promedio no será suficiente.

## 62. Dashboards

Cada proyecto deberá tener dashboards mínimos.

## System Overview

- disponibilidad;
- errores;
- latencia;
- tráfico;
- recursos.

## AI Overview

- modelos;
- tokens;
- costos;
- structured outputs;
- tools;
- retrieval.

## Security Overview

- accesos denegados;
- ataques;
- tenants;
- tools críticas;
- secretos.

## Business Overview

- uso;
- resultados;
- valor;
- adopción.

## 63. Dashboard del Model Gateway

Deberá mostrar:

- tráfico por modelo;
- latencia;
- errores;
- costo;
- tokens;
- fallback;
- retries;
- output failures.

## 64. Dashboard RAG

Deberá mostrar:

- documentos;
- estado de ingestión;
- retrieval latency;
- empty retrieval;
- citas;
- abstenciones;
- evaluaciones;
- fuentes usadas.

## 65. Dashboard de Tools

Deberá mostrar:

- calls;
- success;
- failures;
- permisos;
- aprobaciones;
- latencia;
- duplicados;
- impacto.

## 66. Dashboard de Agentes

Deberá mostrar:

- runs;
- completion;
- steps;
- loops;
- tools;
- models;
- costo;
- fallos;
- terminación.

## 67. Alertas

Las alertas deberán indicar condiciones que requieran acción.

No se crearán alertas para cada anomalía menor.

## Categorías

- availability;
- error;
- latency;
- security;
- cost;
- data;
- AI quality;
- workflow.

## 68. Severidad de alertas

## Critical

Impacto severo o riesgo de seguridad.

## High

Degradación significativa.

## Medium

Problema que requiere investigación.

## Low

Señal informativa o tendencia.

## 69. Requisitos de una alerta

Toda alerta deberá tener:

- nombre;
- condición;
- severidad;
- servicio;
- impacto;
- runbook;
- responsable;
- ventana;
- estrategia de cierre.

## 70. Alertas críticas iniciales

- servicio principal no disponible;
- tenant isolation failure;
- tool crítica sin aprobación;
- exposición de secretos;
- tasa alta de errores;
- base de datos no disponible;
- cola detenida;
- costo fuera de control;
- backups fallidos;
- vulnerabilidad crítica.

## 71. Alertas AI iniciales

- structured output failure elevado;
- fallback rate elevado;
- provider timeout elevado;
- retrieval vacío elevado;
- citation failure elevado;
- agent loop detectado;
- tool authorization denial anormal;
- costo por ejecución excedido;
- latencia de modelo elevada.

## 72. Alertas de seguridad

- intentos repetidos de acceso;
- múltiples tenants consultados;
- prompt injection masiva;
- aprobación bypass;
- secret scanning positivo;
- cambios administrativos;
- exportación inusual;
- uso anormal de tools.

## 73. Alert Fatigue

Para evitar fatiga:

- agrupar eventos;
- usar ventanas;
- limitar duplicados;
- ajustar umbrales;
- silenciar durante mantenimiento;
- revisar alertas inútiles;
- distinguir síntomas de causas.

## 74. SLI

Un Service Level Indicator será una métrica que representa el comportamiento observado.

Ejemplos:

- porcentaje de requests exitosos;
- latencia p95;
- disponibilidad;
- tool success rate;
- RAG grounded response rate.

## 75. SLO

Un Service Level Objective será el objetivo para un SLI.

Ejemplo:

`text id="7u09f1" 99.5% of assistant requests complete successfully in a 30-day window.`

## 76. SLA

Los SLA serán compromisos externos.

No deberán definirse hasta conocer:

- capacidad;
- costos;
- operación;
- soporte;
- riesgos.

Inicialmente se trabajará con SLO internos.

## 77. SLOs iniciales del sistema

Ejemplos para ambientes productivos futuros:

| SLI                    | SLO inicial |
|------------------------|-------------|
| API availability       | 99.5%       |
| Request success rate   | ≥ 99%       |
| Simple query p95       | ≤ 8 s       |
| RAG query p95          | ≤ 12 s      |
| Tool execution success | ≥ 98%       |
| Tenant isolation       | 100%        |

## 78. SLOs AI

| Indicador                 | Objetivo inicial |
|---------------------------|------------------|
| Structured output success | ≥ 98%            |
| Grounded response rate    | ≥ 90%            |
| Citation accuracy         | ≥ 95%            |
| Agent completion rate     | ≥ 90%            |
| Authorization compliance  | 100%             |
| Approval compliance       | 100%             |

## 79. Error Budget

El error budget representa la cantidad de fallos permitida según el SLO.

Si se consume demasiado presupuesto de error:

- se detienen nuevas funcionalidades;
- se prioriza confiabilidad;
- se revisan causas;
- se corrigen regresiones.

## 80. Health Checks

Cada servicio deberá exponer:

## Liveness

Indica si el proceso está vivo.

## Readiness

Indica si puede recibir tráfico.

## Startup

Indica si terminó inicialización.

## 81. Readiness Dependencies

La readiness deberá considerar dependencias críticas.

Ejemplos:

- base de datos;
- migraciones;
- configuración;
- colas.

No deberá bloquearse por dependencias opcionales si existe degradación controlada.

## 82. Synthetic Monitoring

Se podrán ejecutar consultas sintéticas para validar:

- login;
- RAG;
- tool de lectura;
- MCP;
- workflows;
- endpoints críticos.

Los datos deberán ser ficticios.

## 83. Smoke Checks

Después de un despliegue deberán ejecutarse:

- health checks;
- autenticación;
- consulta básica;
- consulta RAG;
- persistencia;
- observabilidad;
- tool segura.

## 84. Observabilidad de errores

Todo error deberá registrar:

- categoría;
- código;
- componente;
- operación;
- retryable;
- tenant;
- correlation ID;
- causa;
- stack trace interno controlado.

## 85. Error Fingerprinting

Los errores deberán agruparse mediante:

- tipo;
- código;
- stack;
- componente;
- proveedor;
- versión.

Esto evitará crear un incidente separado para cada ocurrencia idéntica.

## 86. Excepciones controladas

Las excepciones deberán convertirse a una taxonomía consistente.

Ejemplo:

`text id="ymbrq1" DomainError ValidationError AuthorizationError IntegrationError AIOutputError InfrastructureError`

## 87. Observabilidad de retries

Cada retry deberá registrar:

- intento;
- causa;
- backoff;
- proveedor;
- resultado.

Los retries ocultos dificultan el diagnóstico y aumentan costos.

## 88. Observabilidad de circuit breakers

Se registrará:

- estado;
- apertura;
- cierre;
- causa;
- proveedor;
- fallback;
- duración.

## 89. Observabilidad de degradación

Cuando el sistema utilice una alternativa deberá registrarse.

Ejemplos:

- búsqueda textual en lugar de vectorial;
- modelo secundario;
- respuesta sin memoria;
- workflow manual;
- respuesta sin tool.

## 90. Observabilidad de configuración

Los cambios importantes deberán registrar:

- feature flags;
- modelos;
- prompts;
- límites;
- herramientas;
- permisos;
- políticas.

Se conservará quién realizó el cambio y cuándo.

## 91. Versiones en telemetría

Toda telemetría relevante deberá incluir:

- app version;
- commit SHA;
- deployment version;
- prompt version;
- model version;
- agent graph version;
- tool version;
- dataset version cuando aplique.

## 92. Deployment Markers

Los despliegues deberán marcarse en dashboards.

Esto permitirá correlacionar cambios con:

- errores;
- costo;
- latencia;
- calidad;
- uso.

## 93. Feature Flags y observabilidad

Las métricas deberán permitir diferenciar comportamiento por feature flag cuando sea seguro y viable.

Cada flag deberá incluir:

- nombre;
- variante;
- propietario;
- fecha.

## 94. Observabilidad de evaluaciones

Cada evaluation run deberá registrar:

- dataset;
- versión;
- modelo;
- prompt;
- commit;
- configuración;
- resultados;
- costo;
- duración;
- errores.

## 95. Relación entre producción y evaluación

Los fallos observados en producción deberán convertirse en:

- casos de evaluación;
- pruebas;
- alertas;
- mejoras.

El flujo será:

`text id="c9d7vd" Production Signal       │       ▼ Investigation       │       ▼ Regression Case       │       ▼ Fix       │       ▼ Evaluation`

## 96. User Feedback Correlation

El feedback deberá relacionarse con:

- execution ID;
- conversation;
- modelo;
- prompt;
- sources;
- tools;
- tenant;
- timestamp.

Esto permitirá investigar respuestas útiles o incorrectas.

## 97. Observabilidad de frontend

Se medirá:

- page load;
- API failures;
- rendering errors;
- streaming interruptions;
- user actions;
- approval interactions;
- feedback;
- client version.

No se registrarán entradas sensibles completas.

## 98. Streaming

Los flujos en streaming deberán medir:

- time to first token;
- total duration;
- stream interruptions;
- chunks;
- client disconnects;
- completion status.

## 99. Time to First Token

Será una métrica importante para experiencia de usuario.

Un flujo puede tardar varios segundos en completarse, pero sentirse rápido si inicia respuesta pronto.

## 100. Observabilidad de base de datos

Se medirá:

- query latency;
- slow queries;
- connection pool;
- locks;
- deadlocks;
- transaction duration;
- errors;
- storage;
- replication cuando aplique.

## 101. Observabilidad de Redis

Se medirá:

- hit rate;
- misses;
- memory;
- evictions;
- connections;
- latency;
- expired keys;
- queue depth cuando se utilice como broker.

## 102. Observabilidad de workers

Se medirá:

- jobs received;
- jobs started;
- jobs completed;
- jobs failed;
- retries;
- queue time;
- processing time;
- dead-letter jobs;
- worker availability.

## 103. Observabilidad de object storage

Se medirá:

- uploads;
- downloads;
- failures;
- latency;
- storage use;
- signed URL generation;
- unauthorized attempts;
- deletions.

## 104. Observabilidad de MCP

Se registrará:

- client;
- authentication;
- resource requests;
- tool calls;
- permissions;
- latency;
- errors;
- payload size;
- rate limits.

## 105. Observabilidad de n8n

Se medirá:

- workflow;
- execution;
- trigger;
- success;
- failure;
- retry;
- duration;
- credential errors;
- external service errors;
- manual intervention.

## 106. Retención

Cada señal deberá tener política de retención.

Ejemplo inicial:

| Señal                   | Retención inicial         |
|-------------------------|---------------------------|
| Logs operativos         | 30 días                   |
| Traces normales         | 14 días                   |
| Traces de error         | 30–90 días                |
| Métricas agregadas      | 12 meses                  |
| Auditoría               | Según riesgo y regulación |
| AI payloads sanitizados | Periodo mínimo necesario  |
| Evaluaciones            | Largo plazo               |

Los valores definitivos se ajustarán por proyecto y costo.

## 107. Retención diferenciada

Los datos podrán conservarse según:

- ambiente;
- severidad;
- riesgo;
- tenant;
- clasificación;
- propósito.

No se conservará todo indefinidamente.

## 108. Acceso a telemetría

El acceso deberá controlarse mediante roles.

Ejemplos:

- operadores;
- desarrolladores;
- seguridad;
- administradores;
- auditores.

La telemetría puede contener información sensible derivada.

## 109. Telemetría multi-tenant

Los dashboards empresariales deberán filtrar tenant.

Los usuarios de un tenant no deberán acceder a telemetría de otro.

Los dashboards internos globales estarán restringidos.

## 110. Costo de observabilidad

La telemetría también tiene costo.

Se controlará:

- volumen de logs;
- cardinalidad;
- sampling;
- payload size;
- retención;
- métricas duplicadas;
- traces innecesarios.

## 111. Telemetry Budget

Cada proyecto deberá establecer un presupuesto aproximado de observabilidad.

La instrumentación deberá aportar valor operativo.

No se registrarán eventos sin propósito.

## 112. Proveedores de observabilidad

Se evaluarán progresivamente:

- Grafana;
- Prometheus;
- Loki;
- Tempo;
- Jaeger;
- Langfuse;
- Phoenix;
- servicios administrados.

La instrumentación con OpenTelemetry deberá permitir sustitución.

## 113. Herramientas especializadas AI

Plataformas como Langfuse o Phoenix podrán utilizarse para:

- prompts;
- traces AI;
- evaluations;
- datasets;
- feedback;
- experimentos.

No reemplazarán completamente:

- métricas del sistema;
- logs;
- seguridad;
- auditoría;
- infraestructura.

## 114. Separación entre observabilidad y auditoría

## Observabilidad

Ayuda a operar y diagnosticar.

## Auditoría

Demuestra quién hizo qué, cuándo y sobre qué recurso.

Un log operativo no reemplaza necesariamente un registro de auditoría.

## 115. Inmutabilidad de auditoría

Los eventos críticos deberán almacenarse en un sistema con controles que dificulten:

- modificación;
- eliminación;
- sobrescritura.

La estrategia exacta se definirá por proyecto.

## 116. Runbooks

Cada alerta importante deberá relacionarse con un runbook.

Ejemplos:

- modelo principal no disponible;
- costos elevados;
- cola detenida;
- retrieval vacío;
- tool fallida;
- agent loop;
- tenant isolation alert;
- base de datos saturada.

## 117. Estructura de un runbook

`text id="8y3c1g" Purpose Symptoms Impact Verification Immediate Actions Recovery Rollback Escalation Evidence Follow-up`

## 118. Postmortems

Todo incidente relevante deberá producir un postmortem.

Deberá incluir:

- impacto;
- línea de tiempo;
- detección;
- causa;
- respuesta;
- recuperación;
- aprendizajes;
- acciones.

## 119. Observability Maturity Model

## Nivel 1 — Logs básicos

Existen logs manuales.

## Nivel 2 — Correlación

Existen IDs y estructura.

## Nivel 3 — Traces y métricas

Los flujos principales se rastrean.

## Nivel 4 — Alertas y SLOs

La operación puede anticipar problemas.

## Nivel 5 — AI and Business Observability

Se relacionan calidad, costo, comportamiento y valor.

Los proyectos principales deberán alcanzar nivel 5.

## 120. Checklist de instrumentación

`text id="lkx5tv" [ ] Correlation ID [ ] Trace propagation [ ] Structured logs [ ] Sensitive data redaction [ ] Request metrics [ ] Error metrics [ ] Latency histograms [ ] Model telemetry [ ] Retrieval telemetry [ ] Tool telemetry [ ] Agent telemetry [ ] Business metrics [ ] Dashboards [ ] Alerts [ ] Runbooks`

## 121. Checklist AI

`text id="e2zs6u" [ ] Provider registered [ ] Model registered [ ] Prompt version registered [ ] Token usage measured [ ] Cost calculated [ ] Output validation recorded [ ] Retrieval sources recorded [ ] Tool calls traced [ ] Agent steps traced [ ] Evaluation linked [ ] Feedback linked [ ] Payloads sanitized`

## 122. Checklist de producción

`text id="a1jr3q" [ ] OpenTelemetry enabled [ ] Collector configured [ ] Exporters configured [ ] Sampling configured [ ] Dashboards available [ ] Critical alerts enabled [ ] Access controlled [ ] Retention configured [ ] Runbooks linked [ ] Deployment markers enabled [ ] Cost monitoring enabled [ ] Synthetic checks enabled`

## 123. Aplicación al Proyecto 1

GEEM AI Assistant deberá instrumentar inicialmente:

1.  requests HTTP;
2.  autenticación;
3.  tenant resolution;
4.  conversación;
5.  retrieval;
6.  model gateway;
7.  tool calling;
8.  aprobación;
9.  memoria;
10. ingestión;
11. evaluación;
12. MCP.

## 124. Primer trace del Proyecto 1

El primer vertical slice deberá producir un trace similar a:

`text id="fjo1gh" assistant.message ├── identity.authenticate ├── organization.resolve ├── conversation.create ├── model_gateway.generate │   └── openai.responses ├── message.persist └── response.stream`

## 125. Segundo trace del Proyecto 1

El flujo RAG deberá producir:

`text id="21kgrt" assistant.rag_query ├── authorization.validate ├── query.embed ├── retrieval.vector ├── retrieval.fulltext ├── retrieval.merge ├── context.assemble ├── model.generate ├── citations.validate └── response.persist`

## 126. Tercer trace del Proyecto 1

El flujo de herramienta deberá producir:

`text id="8f3h23" assistant.tool_action ├── model.select_tool ├── tool.validate_arguments ├── tool.authorize ├── approval.evaluate ├── tool.execute ├── audit.persist └── model.generate_final_response`

## 127. Dashboard inicial del Proyecto 1

Deberá incluir:

- request volume;
- error rate;
- p95 latency;
- tokens;
- cost;
- model usage;
- retrieval latency;
- empty retrieval;
- tool success;
- approvals;
- ingestion status;
- evaluation score.

## 128. Alertas iniciales del Proyecto 1

- API unavailable;
- database unavailable;
- model provider failure;
- structured output failure;
- retrieval empty spike;
- unauthorized tool attempt;
- tenant isolation failure;
- ingestion queue blocked;
- cost budget exceeded;
- agent execution limit reached.

## 129. Aplicación al Proyecto 2

Restaurant AI Operations deberá observar:

- integración con Grest;
- extracción de datos;
- análisis;
- agentes;
- recomendaciones;
- aprobaciones;
- reportes;
- costo por análisis;
- utilidad de propuestas.

## 130. Aplicación al Proyecto 3

Enterprise Automation Platform deberá observar:

- triggers;
- webhooks;
- OAuth;
- workflows;
- tools;
- acciones externas;
- retries;
- idempotencia;
- compensaciones;
- impacto empresarial.

## 131. Evidencia de portafolio

La observabilidad deberá producir evidencia visual para el portafolio.

Ejemplos:

- trace de un flujo RAG;
- dashboard de costos;
- ejecución de agente;
- aprobación humana;
- comparación de modelos;
- detección de error;
- recuperación;
- métricas de negocio.

Los datos deberán ser ficticios o sanitizados.

## 132. Preguntas de entrevista que deberá poder responder Erick

Al completar esta estrategia deberá poder explicar:

- cómo propagó contexto entre API y workers;
- cómo rastreó una ejecución de agente;
- cómo midió costo por tenant;
- cómo evitó alta cardinalidad;
- cómo definió SLOs;
- cómo configuró sampling;
- cómo detectó una regresión de retrieval;
- cómo relacionó feedback con una ejecución;
- cómo protegió información sensible en logs;
- cómo distinguió observabilidad de auditoría.

## 133. Criterios mínimos de aprobación

Una capacidad no se considerará Production Ready si:

- no tiene correlation ID;
- no genera logs estructurados;
- no mide errores;
- no mide latencia;
- no registra modelo y prompt;
- no registra tools;
- no protege datos sensibles;
- no puede rastrearse;
- no tiene métricas operativas;
- no tiene estrategia de alerta.

## 134. Excepciones

Una excepción de observabilidad deberá indicar:

- señal faltante;
- motivo;
- riesgo;
- mitigación;
- responsable;
- fecha de corrección.

No se aceptará como justificación permanente:

> Todavía no sabemos qué medir.

En etapas tempranas se medirá al menos:

- uso;
- errores;
- latencia;
- costo;
- resultado.

## 135. Decisiones oficiales

Quedan aprobadas las siguientes reglas:

1.  OpenTelemetry será el estándar de instrumentación.
2.  Logs, métricas y traces deberán correlacionarse.
3.  Toda ejecución relevante tendrá `execution_id`.
4.  Los logs serán estructurados.
5.  La información sensible será redactada antes de persistirse.
6.  Los prompts y outputs se registrarán de forma controlada.
7.  Toda llamada de modelo registrará tokens, costo y latencia.
8.  Retrieval registrará estrategia, filtros, resultados y tiempos.
9.  Toda tool será trazable de autorización a resultado.
10. Los agentes registrarán nodos, pasos, costos y terminación.
11. Los workflows asíncronos conservarán contexto.
12. Las métricas evitarán alta cardinalidad.
13. Se definirán dashboards técnicos, AI, de seguridad y negocio.
14. Las alertas deberán ser accionables y tener runbook.
15. Los proyectos utilizarán SLOs internos antes de ofrecer SLA.
16. Los despliegues se marcarán en observabilidad.
17. Los fallos de producción se convertirán en casos de regresión.
18. La auditoría permanecerá separada de los logs operativos.
19. La retención se definirá según propósito, costo y riesgo.
20. Los proyectos principales deberán alcanzar observabilidad de nivel 5.

## 136. Próximo documento

## Documento 09 — Development Workflow

Definirá:

- proceso completo de trabajo;
- intake;
- análisis;
- Definition of Ready;
- diseño;
- ADR;
- implementación;
- testing;
- evaluación;
- seguridad;
- Pull Request;
- revisión;
- integración;
- despliegue;
- cierre;
- retrospectiva;
- actualización de portafolio.

## 137. Conclusión

La observabilidad permitirá que los sistemas del AI Engineering Lab puedan explicar su propio comportamiento operativo.

Cada respuesta, herramienta, agente y workflow deberá dejar evidencia suficiente para determinar:

- qué recibió;
- qué ejecutó;
- qué modelo utilizó;
- qué información consultó;
- cuánto costó;
- cuánto tardó;
- qué errores encontró;
- cómo terminó.

El objetivo no será acumular logs.

Será construir una capacidad real para operar, investigar y mejorar sistemas de inteligencia artificial con disciplina de ingeniería.
