# ADR-0006: Document Storage

- Estado: Accepted
- Fecha: 2026-07-25
- Responsables: AI Engineering Lead

## Contexto

GEEM AI Assistant deberá almacenar documentos originales y artefactos
derivados utilizados por capacidades como knowledge ingestion, retrieval,
evaluation y exportación.

Estos archivos pueden variar significativamente en tamaño y no deben depender
del filesystem local de los contenedores.

El almacenamiento necesita:

- persistencia independiente del ciclo de vida de la aplicación;
- compatibilidad con ejecución local y ambientes administrados;
- separación por tenant;
- soporte para cargas directas cuando sea necesario;
- URLs firmadas de corta duración;
- políticas de lifecycle;
- versioning cuando aporte valor;
- autorización controlada por la aplicación.

## Decisión

Los documentos originales y artefactos binarios se almacenarán en object
storage compatible con S3.

La implementación inicial utilizará:

- MinIO para desarrollo local;
- un servicio administrado compatible con S3 para staging y producción.

El almacenamiento físico no será considerado fuente de autorización.

El acceso a objetos deberá pasar por casos de uso y políticas de autorización
de la aplicación.

Las claves de objetos seguirán una convención tenant-aware.

Una estructura conceptual será:

`<environment>/<tenant_id>/<resource_type>/<resource_id>/<version>/<filename>`

Los nombres físicos de buckets podrán separar categorías como:

- documents;
- exports;
- evaluation-artifacts;
- temporary.

La separación en buckets distintos dependerá de permisos, lifecycle y
necesidades operativas.

Para archivos pequeños podrá utilizarse:

`client -> API -> object storage`

Para archivos grandes podrá utilizarse:

`client -> signed upload URL -> object storage`

seguido de una confirmación mediante API.

Las signed URLs deberán:

- generarse únicamente después de autorización;
- tener expiración corta;
- limitar la operación;
- limitar el objeto;
- no registrarse completas en logs.

Los archivos temporales deberán tener políticas de expiración.

En producción se evaluará versioning para documentos críticos considerando:

- recuperación;
- costos;
- retención;
- derecho de eliminación.

La metadata de negocio, ownership, estado y autorización permanecerá en
PostgreSQL.

El object storage almacenará contenido y artefactos, no sustituirá el modelo
de dominio ni la fuente de verdad de permisos.

## Alternativas consideradas

### Almacenar archivos directamente en PostgreSQL

No se adopta como estrategia principal.

Aunque simplificaría algunas transacciones, incrementaría:

- tamaño de backups;
- carga de base de datos;
- complejidad operativa;
- costo de almacenamiento;
- dificultad para servir archivos grandes.

### Almacenar archivos en el filesystem local del contenedor

Rechazado.

El filesystem local:

- no es una fuente persistente confiable;
- dificulta escalamiento horizontal;
- complica recuperación;
- genera dependencia del host;
- no es adecuado para deployments inmutables.

### Utilizar un proveedor propietario sin interfaz compatible con S3

No se adopta como requisito inicial.

La compatibilidad S3 permite desarrollo local con MinIO y reduce el
acoplamiento con un proveedor específico.

## Consecuencias

### Positivas

- persistencia independiente de los contenedores;
- desarrollo local reproducible mediante MinIO;
- posibilidad de utilizar servicios administrados;
- soporte natural para archivos grandes;
- signed URLs;
- lifecycle y versioning;
- aislamiento de rutas por tenant;
- menor carga sobre PostgreSQL.

### Negativas

- se introduce una dependencia adicional;
- la consistencia entre PostgreSQL y object storage deberá coordinarse;
- uploads incompletos o huérfanos requerirán limpieza;
- signed URLs agregan consideraciones de seguridad;
- las políticas de lifecycle deberán administrarse explícitamente.

## Riesgos

- confiar en storage keys como mecanismo de autorización;
- objetos almacenados bajo el tenant incorrecto;
- signed URLs con alcance o duración excesiva;
- registrar signed URLs completas;
- archivos huérfanos después de fallos de transacción;
- objetos temporales sin lifecycle;
- permitir tipos o tamaños de archivo no autorizados;
- exponer directamente credenciales del object storage al cliente.

## Validación

La decisión se considerará correctamente aplicada cuando:

- desarrollo local utilice MinIO o almacenamiento S3-compatible;
- staging y producción utilicen almacenamiento persistente compatible;
- ninguna funcionalidad dependa del filesystem local del contenedor;
- las claves de objetos incluyan contexto tenant-aware;
- el acceso a documentos pase por autorización de aplicación;
- las signed URLs sean temporales y de mínimo alcance;
- exista validación de tamaño, tipo y checksum cuando aplique;
- los objetos temporales tengan lifecycle;
- existan pruebas de conectividad y aislamiento del object storage;
- PostgreSQL mantenga metadata y ownership del recurso.

## Referencias

- Documento 11 — Project 1 Architecture Definition
- Documento 14 — Project 1 Data Architecture
- Documento 16 — Project 1 Infrastructure Architecture
- Issue #7 — Establish initial ADR set
- Issue #22 — Add object storage smoke test