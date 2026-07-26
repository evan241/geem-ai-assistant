# AI Engineering Lab

## Documento 07 — Security Baseline

**Versión:** 1.0
**Estado:** Estándar oficial
**Responsable técnico:** Director de AI Engineering
**Lead Engineer:** Erick Eduardo Evangelista Velasco

## 1. Propósito

Este documento define la línea base de seguridad para todos los proyectos del AI Engineering Lab.

Su objetivo es establecer los controles mínimos obligatorios para proteger:

- usuarios;
- organizaciones;
- tenants;
- datos;
- documentos;
- memoria;
- prompts;
- herramientas;
- agentes;
- integraciones;
- modelos;
- credenciales;
- infraestructura;
- auditoría;
- operación.

La seguridad deberá incorporarse desde el diseño.

No será una actividad agregada al final del proyecto.

## 2. Principio rector

> Ningún modelo, agente, herramienta o integración deberá recibir más acceso del estrictamente necesario para cumplir su función.

Este principio se aplicará mediante:

- mínimo privilegio;
- separación de responsabilidades;
- autorización explícita;
- aislamiento de tenants;
- validación de entradas;
- aprobación humana;
- auditoría;
- límites de ejecución;
- defensa en profundidad.

## 3. Alcance

Este estándar aplica a:

- APIs;
- aplicaciones web;
- workers;
- MCP servers;
- pipelines RAG;
- herramientas;
- agentes;
- workflows n8n;
- bases de datos;
- cache;
- almacenamiento de archivos;
- proveedores de modelos;
- webhooks;
- OAuth;
- CI/CD;
- ambientes;
- repositorios;
- observabilidad.

## 4. Objetivos de seguridad

La estrategia deberá proteger:

## Confidencialidad

Solo usuarios y servicios autorizados pueden acceder a la información.

## Integridad

Los datos y decisiones no pueden modificarse sin autorización.

## Disponibilidad

Los sistemas deben mantenerse operables y recuperables.

## Trazabilidad

Las acciones importantes deben poder reconstruirse.

## Aislamiento

Los datos y operaciones de un tenant no deben mezclarse con los de otro.

## Control de agencia

La inteligencia artificial no debe ejecutar acciones fuera de límites autorizados.

## 5. Modelo de responsabilidad

La seguridad será responsabilidad compartida.

## Director de AI Engineering

Responsable de:

- estrategia;
- threat modeling;
- aprobación de riesgos;
- controles AI;
- revisión de arquitectura.

## Lead Engineer

Responsable de:

- implementación;
- pruebas;
- secretos;
- auditoría;
- hardening;
- corrección de vulnerabilidades.

## Product Owner

Responsable de:

- clasificación de datos;
- definición de impacto;
- autorización funcional;
- aceptación de riesgos de negocio.

## Usuario administrador del tenant

Responsable de:

- usuarios;
- roles;
- integraciones;
- aprobaciones;
- configuración operativa.

## 6. Security by Design

Toda funcionalidad deberá responder antes de implementarse:

1.  ¿Qué datos procesa?
2.  ¿Quién puede acceder?
3.  ¿Qué acciones puede ejecutar?
4.  ¿Cuál es el impacto de una falla?
5.  ¿Qué controles necesita?
6.  ¿Qué debe auditarse?
7.  ¿Cómo se recupera?
8.  ¿Qué pruebas negativas requiere?

## 7. Threat Modeling

Cada proyecto deberá tener un threat model.

Se utilizará una combinación de:

- diagramas de flujo de datos;
- trust boundaries;
- análisis de activos;
- casos de abuso;
- STRIDE cuando sea útil;
- riesgos específicos de sistemas AI.

## 8. Activos protegidos

Como mínimo se identificarán:

- credenciales;
- tokens;
- documentos;
- embeddings;
- conversaciones;
- memorias;
- datos operativos;
- configuraciones;
- prompts;
- tool results;
- aprobaciones;
- auditoría;
- código;
- imágenes;
- backups;
- integraciones;
- información de clientes.

## 9. Actores

El análisis considerará:

- usuario legítimo;
- administrador;
- operador;
- desarrollador;
- servicio interno;
- proveedor externo;
- atacante externo;
- usuario malicioso;
- tenant comprometido;
- documento malicioso;
- modelo comprometido o defectuoso;
- integración comprometida.

## 10. Trust Boundaries

Deberán identificarse límites entre:

- navegador y backend;
- backend e identidad;
- backend y base de datos;
- backend y Redis;
- backend y object storage;
- backend y proveedores LLM;
- backend y n8n;
- backend y sistemas heredados;
- MCP client y MCP server;
- tenant y tenant;
- aplicación y herramientas;
- aplicación y workers;
- CI/CD y producción.

## 11. Clasificación de datos

Los datos se clasificarán en:

## Public

Puede publicarse sin daño.

## Internal

Uso interno de la organización.

## Confidential

Información empresarial sensible.

## Restricted

Información cuyo acceso indebido puede causar daño grave.

## 12. Ejemplos de clasificación

## Public

- documentación pública;
- material promocional;
- demos sanitizadas.

## Internal

- procesos internos;
- documentación operativa general;
- configuraciones no sensibles.

## Confidential

- clientes;
- ventas;
- contratos;
- reportes;
- conversaciones internas;
- costos.

## Restricted

- contraseñas;
- API keys;
- tokens;
- datos fiscales;
- datos personales sensibles;
- secretos comerciales críticos;
- credenciales de infraestructura.

## 13. Data Minimization

El sistema solo deberá recopilar los datos necesarios.

No se almacenará información “por si acaso”.

Cada dato deberá tener:

- propósito;
- propietario;
- clasificación;
- retención;
- control de acceso.

## 14. Authentication

La autenticación deberá utilizar estándares reconocidos.

Tecnologías aprobadas:

- OAuth 2.0;
- OpenID Connect;
- JWT;
- sesiones seguras cuando correspondan.

## Requisitos mínimos

- credenciales protegidas;
- expiración;
- rotación;
- revocación cuando aplique;
- MFA para cuentas privilegiadas;
- protección contra fuerza bruta;
- eventos auditables.

## 15. Password Security

Si el sistema maneja contraseñas:

- nunca se almacenarán en texto plano;
- se utilizará hashing fuerte;
- se aplicará salt;
- se evitarán algoritmos obsoletos;
- habrá política de recuperación segura;
- no se enviarán contraseñas por correo.

## 16. Multi-Factor Authentication

MFA será obligatorio para:

- administradores;
- acceso a producción;
- gestores de secretos;
- cuentas de infraestructura;
- repositorios críticos;
- proveedores cloud.

Para usuarios comunes podrá activarse según riesgo.

## 17. Session Security

Las sesiones deberán:

- expirar;
- invalidarse al cerrar sesión;
- protegerse contra robo;
- utilizar cookies seguras cuando aplique;
- usar `HttpOnly`;
- usar `Secure`;
- usar `SameSite`;
- rotar identificadores;
- limitar sesiones simultáneas cuando corresponda.

## 18. JWT Security

Los JWT deberán:

- tener expiración corta;
- validar emisor;
- validar audiencia;
- validar firma;
- validar algoritmo;
- evitar datos sensibles;
- manejar revocación o rotación;
- usar claves separadas por ambiente.

No se confiará en claims sin validación.

## 19. Authorization

La autorización deberá ocurrir en backend.

Se evaluará en:

- endpoint;
- tenant;
- recurso;
- acción;
- herramienta;
- campo;
- workflow.

No se aceptará autorización basada únicamente en la interfaz.

## 20. RBAC

Roles iniciales:

`text id="9g3x2a" owner administrator manager analyst operator viewer`

Cada rol deberá tener permisos explícitos.

No se utilizarán permisos implícitos ambiguos.

## 21. Policy-Based Authorization

Para acciones complejas se utilizarán políticas.

Ejemplo:

`text id="jn7wq9" A manager may approve a level 2 action only inside assigned branches and only below the configured amount.`

Las políticas deberán estar en código o configuración versionada.

No dentro de prompts.

## 22. Least Privilege

Cada usuario, servicio, agente y herramienta deberá tener el mínimo acceso necesario.

## Ejemplos

- una tool de consulta no debe tener permisos de escritura;
- un worker de embeddings no debe acceder a facturación;
- un agente de ventas no debe consultar secretos;
- n8n no debe usar credenciales administrativas globales.

## 23. Deny by Default

Toda acción no autorizada explícitamente deberá rechazarse.

Este principio aplica a:

- endpoints;
- documentos;
- tools;
- MCP;
- integraciones;
- workflows;
- roles;
- recursos.

## 24. Multi-Tenancy Security

El aislamiento de tenants será un control crítico.

Todo recurso empresarial deberá incluir:

`text id="59chf0" tenant_id`

El tenant deberá resolverse desde un contexto autenticado.

No deberá aceptarse libremente desde el cliente.

## 25. Tenant Isolation Controls

El aislamiento deberá aplicarse en:

- casos de uso;
- repositorios;
- queries;
- cache;
- object storage;
- embeddings;
- retrieval;
- memoria;
- tools;
- MCP;
- auditoría;
- exportaciones;
- workers.

## 26. Tenant Isolation in Database

Las consultas deberán incluir tenant de forma obligatoria.

Ejemplo conceptual:

`text id="m181zd" WHERE tenant_id = :authorized_tenant`

Se evitarán métodos que consulten recursos solamente por ID global sin tenant.

## 27. Tenant Isolation in Cache

Las claves deberán incorporar tenant.

Ejemplo:

`text id="a17uz4" tenant:{tenant_id}:conversation:{conversation_id}`

No se compartirán caches empresariales sin separación.

## 28. Tenant Isolation in Object Storage

Los archivos deberán organizarse por tenant.

Ejemplo:

`text id="l43i37" tenants/{tenant_id}/documents/{document_id}/original.pdf`

Las URLs firmadas deberán:

- expirar;
- validar permisos;
- limitar operación;
- evitar enumeración.

## 29. Tenant Isolation in Vector Search

Cada vector deberá conservar:

- tenant;
- documento;
- versión;
- permisos;
- metadata.

Toda consulta vectorial deberá aplicar filtros antes de devolver resultados.

## 30. Row-Level Security

PostgreSQL Row-Level Security podrá utilizarse como defensa adicional.

No reemplazará:

- autorización;
- validación;
- pruebas;
- repositorios correctamente diseñados.

Su adopción requerirá ADR y pruebas específicas.

## 31. Input Validation

Toda entrada deberá validarse.

Incluye:

- API requests;
- uploads;
- webhooks;
- prompts;
- tool arguments;
- MCP inputs;
- parámetros de búsqueda;
- variables de workflows;
- URLs;
- nombres de archivos.

## 32. Validation Rules

Se deberán validar:

- tipo;
- longitud;
- rango;
- formato;
- enumeraciones;
- campos obligatorios;
- relaciones;
- permisos;
- estado;
- tamaño.

La validación sintáctica no sustituye la validación de negocio.

## 33. Output Validation

Las salidas AI consumidas por software deberán validarse con:

- Pydantic;
- JSON Schema;
- tipos;
- reglas de dominio.

Una respuesta inválida no deberá ejecutarse ni persistirse automáticamente.

## 34. Injection Prevention

La aplicación deberá protegerse contra:

- SQL injection;
- command injection;
- template injection;
- path traversal;
- LDAP injection;
- header injection;
- prompt injection.

Los modelos no deberán construir consultas ejecutables sin controles.

## 35. SQL Security

El LLM no tendrá acceso directo a la base de datos.

Las consultas deberán realizarse mediante:

- repositorios;
- servicios;
- queries parametrizadas;
- vistas autorizadas;
- herramientas específicas.

## Prohibido

`text id="om9icr" Generate arbitrary SQL and execute it against production.`

## 36. File Upload Security

Los uploads deberán validar:

- extensión;
- MIME real;
- tamaño;
- checksum;
- nombre;
- contenido;
- duplicados;
- propietario;
- tenant.

Los nombres originales no deberán usarse directamente como rutas internas.

## 37. Malware Scanning

Los archivos deberán analizarse cuando el riesgo lo requiera.

Se considerará:

- antivirus;
- sandboxing;
- bloqueo de formatos ejecutables;
- rechazo de macros;
- revisión de archivos comprimidos.

## 38. File Processing Isolation

La extracción documental deberá ejecutarse en procesos aislados cuando:

- use parsers complejos;
- procese documentos no confiables;
- acepte formatos con riesgo;
- consuma recursos significativos.

Se establecerán:

- timeout;
- memoria;
- CPU;
- tamaño;
- número de páginas;
- profundidad de archivos comprimidos.

## 39. Path Traversal Prevention

El sistema deberá evitar rutas controladas por usuario.

Los archivos deberán identificarse mediante IDs internos.

No mediante rutas proporcionadas directamente.

## 40. Document Security

Cada documento deberá tener:

- tenant;
- propietario;
- clasificación;
- permisos;
- fuente;
- versión;
- estado;
- retención.

La indexación no deberá eliminar estos controles.

## 41. Poisoned Documents

Se considerará que un documento puede contener:

- instrucciones maliciosas;
- datos falsos;
- contenido manipulado;
- enlaces peligrosos;
- secretos;
- ataques indirectos.

El contenido documental será tratado como datos no confiables.

## 42. Prompt Injection

La seguridad deberá asumir que los usuarios y documentos pueden intentar modificar el comportamiento del sistema.

Ejemplos:

- ignorar instrucciones previas;
- revelar prompts;
- ejecutar herramientas;
- cambiar tenant;
- obtener secretos;
- eludir aprobaciones.

## 43. Prompt Hierarchy

Las instrucciones deberán separarse por prioridad:

1.  políticas del sistema;
2.  políticas de seguridad;
3.  reglas de aplicación;
4.  instrucciones del usuario;
5.  contenido recuperado.

El contenido recuperado nunca deberá elevarse a nivel de instrucción.

## 44. Context Delimitation

El contexto recuperado deberá delimitarse claramente.

Ejemplo conceptual:

`text id="6ttysn" BEGIN_UNTRUSTED_DOCUMENT ... END_UNTRUSTED_DOCUMENT`

Esto no será una defensa completa, pero ayudará a mantener separación.

## 45. Instruction/Data Separation

Los prompts deberán distinguir:

- instrucciones;
- datos;
- ejemplos;
- herramientas;
- restricciones.

Los documentos no deberán concatenarse directamente sin estructura.

## 46. Prompt Leakage

El sistema no deberá revelar:

- prompts internos;
- políticas privadas;
- credenciales;
- configuración;
- instrucciones de seguridad;
- razonamiento interno.

Podrá explicar de forma general cómo funciona sin exponer contenido sensible.

## 47. Tool Security

Toda herramienta deberá pasar por:

`text id="mfb6vt" Authentication Authorization Tenant Validation Risk Classification Input Validation Approval Policy Execution Audit`

El modelo no ejecutará herramientas directamente fuera de este flujo.

## 48. Tool Allowlist

Cada agente tendrá una lista explícita de herramientas permitidas.

No se utilizará una lista global compartida por todos.

## 49. Tool Risk Classification

## Level 0

Información pública.

## Level 1

Lectura interna.

## Level 2

Escritura reversible.

## Level 3

Acción externa.

## Level 4

Acción crítica.

Las políticas serán más estrictas conforme aumente el nivel.

## 50. Tool Argument Validation

Los argumentos deberán validarse antes de ejecutar.

Se verificará:

- formato;
- tenant;
- recurso;
- estado;
- permisos;
- límites;
- duplicados;
- intención.

Una llamada bien formada puede seguir siendo no autorizada.

## 51. Human Approval

Las acciones de nivel 3 o 4 requerirán aprobación cuando exista impacto significativo.

La aprobación deberá mostrar:

- acción;
- argumentos;
- objetivo;
- impacto;
- riesgo;
- solicitante;
- expiración.

## 52. Approval Binding

La aprobación deberá quedar ligada exactamente a:

- herramienta;
- argumentos;
- tenant;
- usuario;
- ejecución;
- versión.

No deberá reutilizarse para una acción diferente.

## 53. Approval Expiration

Las aprobaciones deberán expirar.

Una aprobación antigua no deberá permitir una acción nueva.

## 54. Idempotency

Las tools con efectos secundarios deberán utilizar:

- idempotency keys;
- execution IDs;
- constraints;
- registros de resultado.

Esto evitará acciones duplicadas por:

- retries;
- timeouts;
- webhooks repetidos;
- reanudación de agentes.

## 55. Tool Output Security

Los resultados de tools deberán:

- limitar campos;
- ocultar secretos;
- respetar permisos;
- evitar datos innecesarios;
- estar estructurados;
- registrarse de forma segura.

## 56. Agent Security

Los agentes deberán tener:

- objetivo limitado;
- herramientas específicas;
- presupuesto;
- límite de pasos;
- timeout;
- criterio de terminación;
- estado explícito;
- auditoría.

No se permitirán agentes con autonomía irrestricta.

## 57. Excessive Agency

Se deberá prevenir que un agente:

- ejecute acciones no necesarias;
- amplíe su objetivo;
- cree nuevas herramientas;
- modifique políticas;
- ignore aprobaciones;
- delegue fuera de límites.

## 58. Agent Sandboxing

Cuando un agente ejecute código o procese archivos, deberá utilizar ambientes aislados.

Se limitarán:

- red;
- sistema de archivos;
- CPU;
- memoria;
- tiempo;
- comandos;
- credenciales.

## 59. Agent Budget Controls

Cada agente deberá tener límites de:

- pasos;
- tokens;
- costo;
- tiempo;
- herramientas;
- retries.

Exceder límites deberá producir terminación controlada.

## 60. Memory Security

La memoria persistente deberá proteger:

- privacidad;
- tenant;
- usuario;
- retención;
- corrección;
- eliminación.

No deberá almacenar información sensible sin necesidad y política explícita.

## 61. Memory Poisoning

Se deberá prevenir que entradas maliciosas creen recuerdos falsos.

La persistencia podrá requerir:

- fuente confiable;
- confirmación;
- clasificación;
- nivel de confianza;
- aprobación para datos sensibles.

## 62. Memory Retrieval Security

La recuperación deberá filtrar:

- tenant;
- usuario;
- tipo;
- estado;
- expiración;
- permisos.

Nunca deberá usar memoria de otro usuario o tenant.

## 63. RAG Security

El pipeline RAG deberá proteger:

- ingestión;
- extracción;
- metadata;
- chunks;
- embeddings;
- retrieval;
- contexto;
- citas.

## 64. Retrieval Authorization

La autorización deberá aplicarse antes de devolver contenido al modelo.

No deberá recuperarse información prohibida para posteriormente intentar ocultarla.

## 65. Embedding Security

Los embeddings deberán considerarse datos derivados sensibles.

Se protegerán con:

- control de acceso;
- tenant;
- cifrado cuando aplique;
- retención;
- eliminación sincronizada;
- backups protegidos.

## 66. Citation Security

Las citas no deberán revelar:

- rutas privadas;
- identificadores internos sensibles;
- nombres de archivos restringidos;
- contenido sin permisos;
- URLs permanentes sin autorización.

## 67. MCP Security

Todo MCP server deberá implementar:

- autenticación;
- autorización;
- resolución de tenant;
- allowlist de tools;
- validación;
- auditoría;
- rate limiting;
- límites de tamaño;
- manejo de errores.

## 68. MCP Resource Security

Los resources deberán:

- validar permisos;
- limitar contenido;
- proteger metadata;
- manejar paginación;
- evitar enumeración;
- registrar acceso.

## 69. MCP Tool Security

Las tools MCP deberán reutilizar las mismas políticas del backend.

No tendrán una implementación paralela menos segura.

## 70. MCP Client Trust

No se asumirá que el cliente MCP es confiable.

El servidor deberá validar todas las solicitudes.

## 71. Model Provider Security

Las integraciones con proveedores LLM deberán:

- usar credenciales separadas;
- limitar permisos;
- aplicar timeouts;
- registrar uso;
- evitar datos innecesarios;
- respetar políticas de retención;
- controlar regiones cuando aplique.

## 72. Provider Data Minimization

Solo se enviará al proveedor:

- contexto necesario;
- datos autorizados;
- fragmentos mínimos;
- información sanitizada cuando sea posible.

No se enviarán documentos completos cuando basten fragmentos.

## 73. Model Input Redaction

Se evaluará redacción de:

- contraseñas;
- tokens;
- datos fiscales;
- información personal;
- identificadores sensibles.

La redacción deberá conservar utilidad sin exponer datos innecesarios.

## 74. Model Output Filtering

Las respuestas deberán revisarse cuando exista riesgo de:

- secretos;
- datos personales;
- instrucciones inseguras;
- contenido no autorizado;
- acciones críticas.

No se aplicará filtrado genérico ciego que destruya respuestas legítimas.

## 75. Provider Isolation

Las claves de proveedores deberán separarse por:

- ambiente;
- proyecto;
- propósito;
- tenant cuando sea necesario.

No se utilizará una clave global para todo el laboratorio sin control.

## 76. Secrets Management

Los secretos deberán almacenarse en:

- secret manager;
- plataforma de despliegue;
- GitHub Actions Secrets;
- variables protegidas.

No se almacenarán en:

- código;
- repositorios;
- imágenes;
- issues;
- logs;
- prompts;
- screenshots.

## 77. Secret Rotation

Los secretos deberán tener:

- propietario;
- fecha de creación;
- fecha de rotación;
- alcance;
- mecanismo de revocación.

Se rotarán inmediatamente si existe sospecha de exposición.

## 78. Secret Scanning

Se aplicará detección automática en:

- pre-commit;
- CI;
- historial antes de publicar;
- imágenes de contenedor cuando sea posible.

## 79. Environment Separation

Los ambientes deberán separarse:

`text id="prx0sv" development test staging production`

Cada uno deberá tener:

- credenciales distintas;
- datos distintos;
- configuración distinta;
- acceso distinto;
- recursos distintos cuando sea posible.

## 80. Production Access

El acceso a producción deberá:

- limitarse;
- utilizar MFA;
- registrarse;
- evitar cuentas compartidas;
- aplicar mínimo privilegio;
- tener proceso de revocación.

## 81. Database Security

La base de datos deberá:

- no exponerse públicamente;
- usar usuarios separados;
- usar permisos mínimos;
- utilizar conexiones cifradas;
- registrar eventos importantes;
- tener backups;
- aplicar actualizaciones;
- limitar conexiones.

## 82. Database Roles

Se crearán roles distintos para:

- aplicación;
- migraciones;
- lectura;
- auditoría;
- administración.

La aplicación no deberá utilizar credenciales de superusuario.

## 83. Redis Security

Redis deberá:

- permanecer en red privada;
- usar autenticación cuando corresponda;
- separar ambientes;
- aplicar expiración;
- evitar datos restringidos innecesarios;
- proteger backups;
- limitar comandos peligrosos.

## 84. Object Storage Security

El almacenamiento deberá:

- ser privado por defecto;
- usar cifrado;
- utilizar URLs firmadas;
- controlar expiración;
- registrar acceso;
- separar tenants;
- impedir listado público.

## 85. Encryption in Transit

Las comunicaciones deberán utilizar TLS.

Incluye:

- frontend-backend;
- backend-proveedores;
- backend-base de datos;
- backend-object storage;
- webhooks;
- MCP remoto;
- integraciones.

## 86. Encryption at Rest

Se aplicará cifrado en reposo a:

- bases de datos;
- object storage;
- backups;
- discos;
- secretos.

Cuando exista información especialmente sensible se evaluará cifrado adicional a nivel de aplicación.

## 87. Logging Security

Los logs no deberán contener:

- contraseñas;
- tokens;
- API keys;
- documentos completos;
- prompts con datos sensibles;
- tool arguments restringidos;
- respuestas completas innecesarias.

## 88. Log Redaction

Se implementará redacción para campos conocidos.

Ejemplos:

`text id="p5lk83" authorization password api_key access_token refresh_token secret`

La redacción deberá aplicarse antes de persistir.

## 89. Audit Logging

Se auditarán:

- inicios de sesión;
- cambios de roles;
- acceso a documentos sensibles;
- tool executions;
- aprobaciones;
- cambios de configuración;
- cambios de prompts;
- cambios de modelos;
- exportaciones;
- incidentes;
- acciones administrativas.

## 90. Audit Integrity

Los registros de auditoría deberán:

- ser append-only cuando sea viable;
- incluir timestamps;
- incluir actor;
- incluir tenant;
- incluir correlation ID;
- protegerse contra modificación;
- tener retención definida.

## 91. Rate Limiting

Se aplicará rate limiting por:

- IP;
- usuario;
- tenant;
- endpoint;
- tool;
- proveedor;
- workflow.

Los límites deberán considerar:

- abuso;
- costo;
- disponibilidad;
- experiencia del usuario.

## 92. Abuse Prevention

Se deberán detectar patrones como:

- intentos masivos;
- enumeración;
- extracción progresiva;
- múltiples accesos denegados;
- abuso de tools;
- consumo anormal;
- scraping;
- ataques de prompt.

## 93. Quotas

Podrán establecerse cuotas por tenant:

- tokens;
- consultas;
- documentos;
- almacenamiento;
- workflows;
- tool calls;
- costo.

Las cuotas deberán ser visibles y configurables.

## 94. Denial of Service Protection

Se establecerán límites de:

- tamaño de request;
- longitud de prompt;
- documentos;
- concurrencia;
- tiempo;
- memoria;
- pasos de agente;
- cantidad de tools;
- profundidad de archivos.

## 95. Webhook Security

Los webhooks deberán:

- validar firma;
- validar timestamp;
- prevenir replay;
- aplicar idempotencia;
- limitar tamaño;
- responder rápido;
- registrar eventos;
- procesar asíncronamente;
- proteger secretos.

## 96. OAuth Security

Las integraciones OAuth deberán:

- validar `state`;
- utilizar PKCE cuando corresponda;
- limitar scopes;
- almacenar tokens cifrados;
- manejar expiración;
- manejar refresh;
- permitir revocación;
- separar tenants.

## 97. n8n Security

n8n deberá:

- ejecutarse en ambiente protegido;
- restringir acceso administrativo;
- usar MFA o SSO cuando sea posible;
- proteger credenciales;
- limitar community nodes;
- versionar workflows;
- separar ambientes;
- auditar cambios;
- evitar lógica crítica oculta.

## 98. Third-Party Integrations

Cada integración deberá evaluarse en:

- permisos;
- datos enviados;
- retención;
- seguridad;
- disponibilidad;
- cumplimiento;
- revocación;
- plan de salida.

## 99. Dependency Security

Las dependencias deberán:

- tener versiones controladas;
- revisarse;
- escanearse;
- actualizarse;
- contar con licencia compatible;
- evitar paquetes abandonados.

## 100. Supply Chain Security

Se considerará:

- lockfiles;
- hashes;
- imágenes firmadas;
- procedencia;
- dependencias transitivas;
- acciones de GitHub fijadas por versión;
- acceso de maintainers;
- protección de releases.

## 101. Container Security

Las imágenes deberán:

- usar bases mínimas;
- correr sin root;
- no contener secretos;
- escanear vulnerabilidades;
- fijar versiones;
- reducir paquetes;
- usar multi-stage;
- incluir health checks.

## 102. CI/CD Security

Los pipelines deberán:

- limitar permisos;
- proteger secretos;
- evitar ejecución no confiable;
- separar ambientes;
- requerir aprobación para producción;
- registrar despliegues;
- proteger artifacts.

## 103. GitHub Actions Permissions

Los workflows deberán usar permisos mínimos.

No se utilizará acceso de escritura global cuando solo se necesite lectura.

## 104. Repository Security

Los repositorios deberán aplicar:

- branch protection;
- secret scanning;
- dependency scanning;
- revisión de PR;
- CODEOWNERS;
- MFA;
- acceso mínimo;
- historial limpio.

## 105. Backup Security

Los backups deberán:

- cifrarse;
- protegerse;
- separarse de producción;
- tener retención;
- probar restauración;
- respetar tenant y privacidad;
- eliminarse al vencer.

## 106. Recovery

Se deberán definir:

- RPO;
- RTO;
- procedimientos;
- responsables;
- pruebas;
- comunicación.

Los objetivos exactos se definirán por proyecto.

## 107. Data Retention

Cada dato deberá tener política de retención.

Ejemplos:

- conversaciones;
- documentos;
- embeddings;
- logs;
- auditoría;
- tool results;
- backups;
- evaluaciones.

## 108. Secure Deletion

Cuando se elimine información deberán considerarse:

- registro principal;
- chunks;
- embeddings;
- caches;
- backups;
- object storage;
- índices;
- memoria.

La eliminación deberá ser consistente.

## 109. Privacy

Los proyectos deberán aplicar:

- minimización;
- propósito;
- acceso;
- corrección;
- eliminación;
- retención;
- transparencia.

No se utilizarán datos reales en demos públicas.

## 110. Personal Data

Los datos personales deberán:

- identificarse;
- clasificarse;
- limitarse;
- protegerse;
- auditarse;
- eliminarse cuando corresponda.

## 111. Evaluation Data Security

Los datasets de evaluación deberán:

- evitar datos reales innecesarios;
- utilizar información ficticia;
- sanitizar ejemplos;
- controlar acceso;
- versionarse;
- documentar origen.

## 112. Security Testing

La estrategia incluirá:

- unit tests;
- integration tests;
- authorization tests;
- tenant isolation tests;
- injection tests;
- prompt injection tests;
- tool abuse tests;
- webhook tests;
- dependency scanning;
- container scanning.

## 113. Negative Testing

Cada flujo crítico deberá probar:

- usuario sin autenticación;
- usuario sin permiso;
- tenant incorrecto;
- input inválido;
- recurso inexistente;
- intento de bypass;
- tool no autorizada;
- aprobación inválida;
- replay;
- duplicado.

## 114. Security Evaluation Dataset

Se mantendrá un dataset adversarial con:

- prompt injection;
- indirect prompt injection;
- data exfiltration;
- tenant escape;
- role escalation;
- tool misuse;
- secret extraction;
- approval bypass;
- malicious documents.

## 115. Security Hard Gates

Una release será bloqueada si existe:

- acceso cruzado entre tenants;
- ejecución de tool no autorizada;
- bypass de aprobación;
- secreto expuesto;
- vulnerabilidad crítica conocida;
- SQL injection;
- command injection;
- acceso administrativo indebido;
- pérdida de auditoría crítica.

## 116. Vulnerability Management

Las vulnerabilidades se clasificarán:

## Critical

Atención inmediata.

## High

Prioridad máxima de corrección.

## Medium

Plan de corrección.

## Low

Backlog controlado.

## 117. Security Issue Handling

Los issues de seguridad deberán:

- mantenerse privados cuando corresponda;
- limitar detalles;
- asignar responsable;
- incluir impacto;
- incluir mitigación;
- incluir prueba de regresión;
- generar postmortem si el impacto fue relevante.

## 118. Incident Response

El proceso será:

`text id="jbdxv4" Detection    │    ▼ Containment    │    ▼ Investigation    │    ▼ Eradication    │    ▼ Recovery    │    ▼ Postmortem`

## 119. Incident Classification

## Severity 1

Compromiso crítico, datos o producción.

## Severity 2

Impacto alto limitado.

## Severity 3

Impacto moderado.

## Severity 4

Problema menor o preventivo.

## 120. Incident Evidence

Durante un incidente deberán conservarse:

- logs;
- traces;
- timestamps;
- cambios;
- usuarios;
- IPs cuando sea legal y útil;
- tool executions;
- eventos;
- versiones;
- configuración.

## 121. Credential Exposure Response

Ante exposición de credenciales:

1.  revocar;
2.  rotar;
3.  revisar uso;
4.  contener acceso;
5.  limpiar historial;
6.  revisar logs;
7.  crear regresión;
8.  documentar incidente.

Eliminar la credencial del último commit no será suficiente.

## 122. Model Failure Response

Si un modelo produce comportamiento inseguro:

- desactivar versión;
- aplicar feature flag;
- cambiar proveedor;
- limitar tools;
- aumentar aprobación;
- ejecutar evaluación;
- revisar prompts;
- restaurar versión anterior.

## 123. Security Monitoring

Se monitoreará:

- accesos fallidos;
- cambios de roles;
- tool denials;
- intentos de prompt injection;
- costos anormales;
- tenants anómalos;
- exportaciones;
- errores;
- uso de secretos;
- cambios administrativos.

## 124. Alerts

Las alertas deberán ser:

- accionables;
- priorizadas;
- relacionadas con runbooks;
- libres de datos sensibles;
- probadas.

## 125. Security Metrics

Métricas mínimas:

- intentos de acceso denegado;
- incidentes;
- vulnerabilidades abiertas;
- tiempo de corrección;
- tool authorization failures;
- approval bypass attempts;
- tenant isolation failures;
- secret detections;
- prompt injection detections;
- dependencias vulnerables.

## 126. Secure Development Lifecycle

Cada feature seguirá:

`text id="st5w41" Design   │   ▼ Threat Review   │   ▼ Implementation   │   ▼ Security Tests   │   ▼ Code Review   │   ▼ Deployment   │   ▼ Monitoring`

## 127. Security Review by Change Type

## Low Risk

- documentación;
- UI sin datos;
- refactor interno.

## Medium Risk

- nuevo endpoint;
- nueva integración de lectura;
- cambio de modelo.

## High Risk

- tool de escritura;
- OAuth;
- MCP;
- datos restringidos;
- nuevos permisos;
- cambios multi-tenant.

Los cambios de alto riesgo requerirán revisión reforzada.

## 128. Security ADRs

Se documentarán decisiones como:

`text id="8d5j1r" ADR-SEC-0001-tenant-isolation-strategy ADR-SEC-0002-tool-approval-model ADR-SEC-0003-secret-management ADR-SEC-0004-document-processing-isolation`

## 129. Security Documentation

Cada proyecto deberá mantener:

`text id="ra6a0g" docs/security/ ├── threat-model.md ├── data-classification.md ├── access-control.md ├── tool-security.md ├── incident-response.md └── security-testing.md`

## 130. Security Checklist para Pull Requests

`text id="kjc81v" [ ] Inputs validated [ ] Outputs validated [ ] Authentication reviewed [ ] Authorization reviewed [ ] Tenant isolation verified [ ] Secrets protected [ ] Logs sanitized [ ] Tools classified [ ] Approvals enforced [ ] Negative tests added [ ] Threat model updated [ ] Dependencies reviewed`

## 131. Production Security Checklist

`text id="5vn4zx" [ ] TLS enabled [ ] Secrets separated [ ] MFA enabled [ ] Database private [ ] Backups encrypted [ ] Logs sanitized [ ] Alerts configured [ ] Access reviewed [ ] Vulnerability scan passed [ ] Containers hardened [ ] Incident runbook available [ ] Rollback tested`

## 132. AI Security Checklist

`text id="thn39v" [ ] Prompt injection tested [ ] Indirect injection tested [ ] Tools allowlisted [ ] Tool permissions enforced [ ] Approval binding validated [ ] Model outputs validated [ ] Sensitive data minimized [ ] Memory isolated [ ] Retrieval authorized [ ] Agent limits configured [ ] Security dataset passed`

## 133. Aplicación al Proyecto 1

GEEM AI Assistant deberá implementar primero:

1.  autenticación;
2.  organizations;
3.  tenant context;
4.  RBAC;
5.  document permissions;
6.  retrieval filters;
7.  tool registry;
8.  approval flow;
9.  audit log;
10. prompt injection tests;
11. MCP authorization;
12. secret scanning.

## 134. Primer Threat Model del Proyecto 1

Deberá cubrir:

- carga de documentos maliciosos;
- acceso cruzado entre tenants;
- prompt injection directo;
- prompt injection indirecto;
- extracción de prompts;
- tool abuse;
- memoria contaminada;
- exposición de documentos;
- credenciales de proveedores;
- MCP client malicioso.

## 135. Aplicación al Proyecto 2

Restaurant AI Operations deberá proteger:

- ventas;
- inventarios;
- costos;
- compras;
- recomendaciones;
- aprobaciones;
- acciones operativas;
- integración con Grest.

Los agentes no podrán modificar datos operativos directamente.

## 136. Aplicación al Proyecto 3

Enterprise Automation Platform deberá proteger especialmente:

- OAuth;
- webhooks;
- credenciales;
- WhatsApp;
- correo;
- CRM;
- ERP;
- workflows;
- acciones externas;
- idempotencia;
- auditoría.

## 137. Criterios mínimos de aprobación

Una capacidad no será aprobada si:

- no tiene propietario de seguridad;
- no clasifica datos;
- no valida tenant;
- no prueba accesos negativos;
- no protege secretos;
- no controla herramientas;
- no registra acciones críticas;
- no tiene estrategia de recuperación.

## 138. Riesgo aceptado

Un riesgo podrá aceptarse cuando:

- esté identificado;
- tenga impacto conocido;
- tenga probabilidad estimada;
- exista mitigación;
- exista propietario;
- tenga fecha de revisión;
- no viole un hard gate.

## 139. Excepciones

Las excepciones deberán documentar:

- control omitido;
- motivo;
- riesgo;
- duración;
- mitigación;
- responsable;
- fecha de expiración.

No existirán excepciones permanentes sin revisión.

## 140. Decisiones oficiales

Quedan aprobadas las siguientes reglas:

1.  La seguridad se diseñará desde el inicio.
2.  Todo acceso aplicará mínimo privilegio.
3.  Toda acción no autorizada explícitamente será rechazada.
4.  El aislamiento de tenants será un hard gate.
5.  Los modelos no accederán directamente a bases de datos.
6.  Los documentos se tratarán como contenido no confiable.
7.  Toda tool pasará por autorización, riesgo, validación y auditoría.
8.  Las acciones críticas requerirán aprobación humana.
9.  Los agentes tendrán límites de herramientas, pasos, tiempo y costo.
10. La memoria estará aislada por tenant y usuario.
11. RAG aplicará autorización antes de enviar contexto al modelo.
12. MCP reutilizará las políticas del backend.
13. Los proveedores recibirán únicamente datos necesarios.
14. Los secretos nunca se almacenarán en repositorios o logs.
15. Los ambientes tendrán credenciales separadas.
16. Se aplicará cifrado en tránsito y en reposo.
17. Se realizarán pruebas adversariales.
18. Las vulnerabilidades críticas bloquearán releases.
19. Todo incidente relevante producirá aprendizaje y regresión.
20. Las excepciones deberán ser explícitas, temporales y aprobadas.

## 141. Próximo documento

## Documento 08 — Observability Strategy

Definirá:

- logs;
- traces;
- metrics;
- correlation;
- telemetry AI;
- costos;
- dashboards;
- alertas;
- SLOs;
- incident detection;
- data redaction;
- retención;
- observabilidad de agentes;
- observabilidad de RAG;
- observabilidad de tools;
- integración con OpenTelemetry.

## 142. Conclusión

La seguridad del AI Engineering Lab no dependerá de confiar en el modelo.

Dependerá de controles verificables alrededor del modelo.

Los sistemas deberán asumir que:

- los usuarios pueden equivocarse;
- los documentos pueden ser maliciosos;
- las integraciones pueden fallar;
- los modelos pueden inventar;
- los agentes pueden exceder objetivos;
- las tools pueden producir impacto real;
- las credenciales pueden filtrarse;
- los tenants deben mantenerse aislados.

Por ello, cada capacidad deberá operar dentro de límites técnicos, permisos explícitos, auditoría, evaluación y recuperación.

El objetivo no será construir sistemas que parezcan seguros.

Será construir sistemas donde la seguridad pueda demostrarse.
