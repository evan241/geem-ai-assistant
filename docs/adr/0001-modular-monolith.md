# ADR-0001: Modular Monolith

- Estado: Accepted
- Fecha: 2026-07-25
- Responsables: AI Engineering Lead

## Contexto

GEEM AI Assistant incluye múltiples capacidades empresariales y de inteligencia
artificial:
identity, organizations, conversations, knowledge, retrieval, tools,
approvals, memory, audit, evaluation, AI runtime y observability.

El sistema necesita límites claros entre capacidades sin asumir desde el
inicio el costo operativo y distribuido de una arquitectura de microservicios.

La arquitectura oficial del proyecto define separación por módulos de negocio,
capas internas y APIs públicas explícitas entre módulos.

## Decisión

GEEM AI Assistant se implementará inicialmente como un Modular Monolith.

El código de producto residirá bajo `src/geem_ai/` y se organizará por
capacidad de negocio.

Cada módulo mantendrá, cuando aplique, las siguientes capas:

- domain;
- application;
- infrastructure;
- presentation.

Los módulos deberán interactuar mediante contratos públicos explícitos y no
mediante acceso directo a detalles internos o tablas pertenecientes a otros
módulos.

Las dependencias deberán apuntar hacia el interior:

Presentation → Application → Domain

Infrastructure implementará ports definidos por Application o Domain.

La separación física en servicios independientes solo se considerará cuando
exista evidencia operativa o de escalamiento que la justifique.

## Alternativas consideradas

### Microservicios desde el inicio

Rechazada porque introduce prematuramente:

- networking distribuido;
- despliegues múltiples;
- service discovery;
- observabilidad distribuida;
- coordinación transaccional;
- mayor complejidad operativa.

### Monolito sin límites modulares

Rechazado porque facilitaría acoplamiento entre capacidades, acceso directo a
datos ajenos y dificultad futura para evolucionar módulos independientemente.

## Consecuencias

### Positivas

- menor complejidad operativa inicial;
- transacciones locales más sencillas;
- desarrollo y debugging más simples;
- límites de dominio explícitos;
- posibilidad de extracción futura de módulos;
- despliegue inicial sencillo.

### Negativas

- los límites modulares deberán protegerse mediante disciplina y tests;
- un único deployment limita el aislamiento de fallos entre módulos;
- el escalamiento independiente por capacidad no estará disponible de inicio.

## Riesgos

- degradación gradual hacia un monolito acoplado;
- imports entre módulos que violen los límites;
- acceso directo a tablas de otros módulos;
- lógica de infraestructura filtrándose hacia Domain.

## Validación

La decisión se considerará correctamente aplicada cuando:

- cada capacidad principal exista como módulo explícito;
- las dependencias respeten la regla hacia el interior;
- Domain no importe frameworks o infraestructura;
- los módulos no consulten directamente datos privados de otros módulos;
- existan architecture boundary tests;
- los nuevos vertical slices respeten esta estructura.

## Referencias

- Documento 11 — Project 1 Architecture Definition
- Documento 12 — Project 1 Domain Model
- Documento 15 — Project 1 Application Architecture
- Issue #7 — Establish initial ADR set
- Issue #23 — Add architecture boundary tests