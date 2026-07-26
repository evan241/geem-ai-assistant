# ADR-0004: Model Gateway

- Estado: Accepted
- Fecha: 2026-07-25
- Responsables: AI Engineering Lead

## Contexto

GEEM AI Assistant utilizará modelos de inteligencia artificial externos para
ejecutar capacidades como respuestas conversacionales, RAG, clasificación y
propuestas de uso de herramientas.

Los proveedores y modelos pueden cambiar con el tiempo y presentan diferencias
en:

- SDKs;
- modelos disponibles;
- structured outputs;
- tool calling;
- límites;
- precios;
- latencia;
- disponibilidad;
- formatos de error;
- políticas de retry;
- capacidades soportadas.

Los casos de uso de aplicación no deberán depender directamente de estas
diferencias ni conocer SDKs específicos de proveedores.

El sistema necesita además controlar de manera centralizada:

- routing;
- políticas de modelo;
- prompts;
- validación;
- retries;
- fallback;
- presupuesto;
- costo;
- telemetría.

## Decisión

Las capacidades de AI accederán a proveedores externos exclusivamente mediante
un Model Gateway.

Application dependerá de un port estable conceptualmente equivalente a:

`ModelGateway.execute(ModelExecutionRequest) -> ModelExecutionResult`

El Model Gateway será responsable de coordinar:

- normalización de requests;
- resolución del proveedor y modelo;
- integración con Prompt Registry;
- aplicación de límites y constraints;
- validación de structured outputs;
- retries controlados;
- fallback autorizado;
- cálculo y registro de costo;
- métricas y telemetría;
- normalización de respuestas y errores.

Los SDKs específicos de proveedores quedarán contenidos en adapters de
Infrastructure.

Ejemplos:

- OpenAI adapter;
- Anthropic adapter;
- Fake Model Gateway para desarrollo y testing.

Los casos de uso, Domain y Application no importarán directamente SDKs de
OpenAI, Anthropic u otros proveedores.

La selección de proveedor y modelo será gobernada mediante una política de
routing.

No será seleccionada libremente por el usuario final.

La política podrá considerar:

- capability;
- configuración;
- disponibilidad;
- presupuesto;
- features requeridas;
- modelos permitidos;
- feature flags;
- política de fallback.

Toda respuesta consumida programáticamente deberá validarse contra el contrato
esperado antes de ser aceptada por la aplicación.

El Model Gateway podrá devolver propuestas de tool calls, pero no ejecutará
directamente herramientas con efectos de negocio.

La autorización, riesgo, aprobación y ejecución de tools permanecerán bajo
control de la aplicación.

## Alternativas consideradas

### Integrar SDKs de proveedores directamente en cada caso de uso

Rechazada.

Provocaría:

- acoplamiento entre Application y proveedores;
- duplicación de lógica de retries y errores;
- dificultad para cambiar modelos;
- telemetría inconsistente;
- mayor dificultad para testing;
- fallback distribuido entre múltiples componentes.

### Utilizar un único proveedor sin abstracción

Rechazado como restricción arquitectónica.

Aunque la primera implementación pueda utilizar un único proveedor real,
el sistema deberá mantener una frontera que permita cambiarlo o incorporar
alternativas sin modificar los casos de uso.

### Exponer directamente las APIs de proveedores al frontend

Rechazado.

Esto expondría:

- credenciales;
- detalles de implementación;
- routing;
- prompts;
- políticas internas;
- controles de seguridad y costo.

## Consecuencias

### Positivas

- Application permanece independiente de proveedores concretos;
- incorporación de nuevos proveedores mediante adapters;
- testing determinista mediante fake gateway;
- routing y fallback centralizados;
- observabilidad consistente;
- control centralizado de costos y límites;
- structured output validation uniforme;
- menor impacto de cambios de SDK o proveedor.

### Negativas

- se introduce una capa adicional de abstracción;
- deberá mantenerse un modelo interno común entre capacidades distintas;
- algunas capacidades específicas de un proveedor requerirán extensiones
  controladas;
- fallback y normalización agregan complejidad operacional.

## Riesgos

- diseñar un contrato demasiado genérico que pierda capacidades útiles de los
  proveedores;
- filtrar tipos o excepciones específicas del proveedor fuera del adapter;
- ocultar fallos sistemáticos mediante retries excesivos;
- utilizar fallback sin respetar presupuesto, seguridad o compatibilidad;
- asumir que todos los modelos soportan las mismas tools o structured outputs;
- ejecutar tool calls propuestas por el modelo sin pasar por autorización y
  approval;
- registrar prompts o respuestas sensibles sin sanitización.

## Validación

La decisión se considerará correctamente aplicada cuando:

- Application dependa únicamente del port `ModelGateway`;
- los SDKs de proveedores aparezcan exclusivamente en Infrastructure adapters;
- exista un Fake Model Gateway para pruebas deterministas;
- las solicitudes y respuestas utilicen contratos internos estables;
- routing, timeout, retry y fallback estén centralizados;
- el proveedor y modelo utilizado queden registrados;
- usage, costo y latencia sean observables;
- structured outputs sean validados antes de persistirse;
- tool calls sean tratadas como propuestas y no como ejecución directa;
- sea posible cambiar el proveedor de una capability sin modificar su caso de
  uso.

## Referencias

- Documento 11 — Project 1 Architecture Definition
- Documento 13 — Project 1 API & Contract Standards
- Documento 15 — Project 1 Application Architecture
- Documento 16 — Project 1 Infrastructure Architecture
- Issue #7 — Establish initial ADR set