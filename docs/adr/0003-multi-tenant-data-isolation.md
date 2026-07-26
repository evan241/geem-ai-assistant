# ADR-0003: Multi-Tenant Data Isolation

- Estado: Accepted
- Fecha: 2026-07-25
- Responsables: AI Engineering Lead

## Contexto

GEEM AI Assistant será una plataforma multi-tenant.

Los datos pertenecientes a diferentes organizaciones deberán permanecer
aislados incluso cuando compartan infraestructura, procesos de aplicación y
almacenamiento.

El aislamiento no puede depender únicamente de que cada desarrollador recuerde
agregar filtros por tenant en cada consulta.

Una falla de aislamiento podría exponer conversaciones, documentos, memoria,
ejecuciones, herramientas, aprobaciones u otros datos empresariales de una
organización a otra.

La arquitectura necesita por tanto una estrategia explícita de aislamiento que
se aplique de forma consistente desde el contexto de aplicación hasta la
persistencia.

## Decisión

La estrategia inicial utilizará una base de datos PostgreSQL compartida y un
schema principal compartido.

Las entidades y tablas que contengan datos pertenecientes a un tenant deberán
incluir explícitamente:

`tenant_id`

El tenant activo deberá resolverse mediante un contexto autenticado y
autorizado.

El `tenant_id` utilizado para acceder o modificar datos no deberá confiar en
un valor arbitrario proporcionado por el cliente cuando el contexto pueda
derivarse de la identidad autenticada.

El aislamiento se aplicará mediante defensa en profundidad:

1. contexto de tenant explícito en Application;
2. autorización y políticas de dominio cuando corresponda;
3. repositories y queries tenant-aware;
4. constraints e índices apropiados;
5. PostgreSQL Row-Level Security para tablas tenant-scoped;
6. pruebas específicas de aislamiento entre tenants.

RLS será una barrera adicional de seguridad y no sustituirá las reglas de
autorización de la aplicación.

Los módulos no podrán acceder directamente a tablas privadas pertenecientes a
otros módulos para evitar eludir sus políticas de acceso.

Los recursos globales que deliberadamente no pertenezcan a un tenant deberán
modelarse explícitamente como globales. No se utilizará `tenant_id = NULL`
como mecanismo implícito para representar alcance global.

## Alternativas consideradas

### Base de datos independiente por tenant

No se adopta inicialmente.

Proporciona un fuerte aislamiento físico, pero incrementa significativamente:

- aprovisionamiento;
- migraciones;
- conexiones;
- observabilidad;
- backups;
- mantenimiento;
- operación local y de desarrollo.

Podrá reconsiderarse para requisitos regulatorios o clientes con necesidades
especiales de aislamiento.

### Schema PostgreSQL independiente por tenant

No se adopta inicialmente porque incrementaría la complejidad de migraciones,
permisos, tooling y operación sin una necesidad demostrada en la primera
versión.

### Aislamiento únicamente mediante filtros de aplicación

Rechazado.

Depender exclusivamente de cláusulas como:

`WHERE tenant_id = ...`

hace que una consulta incorrecta pueda convertirse directamente en una fuga de
datos entre tenants.

## Consecuencias

### Positivas

- infraestructura inicial sencilla;
- modelo multi-tenant explícito;
- defensa en profundidad;
- RLS proporciona una barrera adicional ante errores de consulta;
- operación y migraciones centralizadas;
- aislamiento verificable mediante tests.

### Negativas

- todas las operaciones tenant-scoped deberán transportar contexto de tenant;
- RLS agrega complejidad a migraciones, debugging y pruebas;
- queries, índices y constraints deberán diseñarse considerando `tenant_id`;
- procesos administrativos cross-tenant requerirán rutas explícitas y
  privilegiadas.

## Riesgos

- tablas tenant-scoped creadas sin `tenant_id`;
- políticas RLS ausentes o incorrectas;
- conexiones de base de datos ejecutándose con privilegios que permitan
  eludir RLS;
- jobs asíncronos perdiendo el contexto de tenant;
- cache keys sin namespace de tenant;
- object storage paths sin aislamiento de tenant;
- herramientas o integraciones externas ejecutándose con un tenant incorrecto;
- tests que validen funcionalidad pero no aislamiento negativo.

## Validación

La decisión se considerará correctamente aplicada cuando:

- toda tabla tenant-scoped declare `tenant_id`;
- las foreign keys y constraints preserven el aislamiento cuando corresponda;
- las tablas tenant-scoped tengan políticas RLS;
- exista evidencia automatizada de que un tenant no puede acceder a datos de
  otro tenant;
- los repositories reciban o deriven explícitamente el contexto de tenant;
- los jobs persistentes incluyan `tenant_id`;
- cache y object storage utilicen namespaces tenant-aware;
- las rutas administrativas cross-tenant estén explícitamente autorizadas;
- las migraciones incorporen las políticas de aislamiento junto con las tablas.

## Referencias

- Documento 11 — Project 1 Architecture Definition
- Documento 12 — Project 1 Domain Model
- Documento 14 — Project 1 Data Architecture
- Documento 15 — Project 1 Application Architecture
- Issue #7 — Establish initial ADR set