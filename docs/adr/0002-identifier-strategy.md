# ADR-0002: Identifier Strategy

- Estado: Accepted
- Fecha: 2026-07-25
- Responsables: AI Engineering Lead

## Contexto

GEEM AI Assistant necesita identificadores que puedan generarse de forma
independiente de la base de datos y utilizarse consistentemente en entidades,
eventos, jobs y contratos.

Los identificadores deben ser:

- opacos;
- globalmente únicos;
- compatibles con generación distribuida;
- eficientes para almacenamiento e indexación en PostgreSQL;
- adecuados para pruebas deterministas;
- disponibles antes de persistir una entidad.

La estrategia también debe evitar que las entidades de dominio dependan de
detalles específicos de PostgreSQL para adquirir identidad.

## Decisión

Los identificadores principales del sistema utilizarán UUIDv7.

En PostgreSQL se almacenarán utilizando el tipo nativo:

`uuid`

No se almacenarán UUIDs como `varchar` o tipos equivalentes de texto.

Los IDs se generarán preferentemente en la aplicación antes de persistir la
entidad.

La generación de identificadores será expuesta mediante un port explícito,
por ejemplo:

`IdGenerator`

El dominio no dependerá directamente de una implementación concreta del
generador.

Las pruebas podrán utilizar generadores deterministas para producir IDs
conocidos.

La estrategia podrá utilizar diferentes representaciones públicas cuando un
contrato específico lo requiera, pero la identidad interna canónica continuará
siendo UUID.

## Alternativas consideradas

### UUIDv4

Rechazado como estrategia principal porque, aunque proporciona unicidad y
generación distribuida, su aleatoriedad produce peor localidad de inserción e
indexación que UUIDv7.

### Identificadores autoincrementales

Rechazados como estrategia principal porque:

- requieren persistencia para obtener identidad;
- dificultan generación distribuida;
- exponen secuencias predecibles;
- complican eventos creados antes del commit;
- generan mayor acoplamiento con la base de datos.

### ULID

Considerado por su capacidad de ordenamiento temporal y representación
compacta.

No se adopta inicialmente porque PostgreSQL ofrece soporte nativo para UUID y
UUIDv7 satisface las necesidades del proyecto sin introducir un tipo o
convención adicional.

## Consecuencias

### Positivas

- identidad disponible antes de persistir;
- generación distribuida;
- menor acoplamiento con la base de datos;
- buena compatibilidad con eventos y jobs;
- mejor localidad temporal que UUIDv4;
- uso del tipo `uuid` nativo de PostgreSQL;
- pruebas deterministas mediante `IdGenerator`.

### Negativas

- los identificadores son más grandes que enteros secuenciales;
- las herramientas y librerías utilizadas deberán soportar UUIDv7;
- deberá existir una implementación controlada del generador.

## Riesgos

- utilizar accidentalmente UUIDv4 u otra estrategia en algunos módulos;
- generar IDs directamente mediante librerías concretas dentro del dominio;
- convertir UUIDs a texto innecesariamente en persistencia;
- mezclar múltiples estrategias sin una decisión arquitectónica explícita.

## Validación

La decisión se considerará correctamente aplicada cuando:

- los identificadores persistidos definidos por esta estrategia utilicen
  PostgreSQL `uuid`;
- las entidades reciban su identidad antes de persistirse;
- exista un port `IdGenerator`;
- la infraestructura proporcione la implementación real del generador;
- las pruebas puedan utilizar generadores deterministas;
- no existan UUIDs almacenados como `varchar`;
- la estrategia sea consistente entre módulos, eventos y jobs.

## Referencias

- Documento 12 — Project 1 Domain Model
- Documento 14 — Project 1 Data Architecture
- Documento 15 — Project 1 Application Architecture
- Issue #7 — Establish initial ADR set