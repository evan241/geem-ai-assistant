# AI Engineering Lab

## Documento 10 --- Project 1 Product Definition

GEEM AI Assistant **Versión:** 1.0 **Estado:** Definición oficial de
producto **Responsable de producto:** Erick Eduardo Evangelista Velasco
**Responsable técnico:** Director de AI Engineering **Tipo de
producto:** Enterprise AI Assistant **Fase:** Proyecto 1 del AI
Engineering Lab

## 1. Propósito del documento

Este documento define formalmente el primer producto del AI Engineering
Lab:

GEEM AI Assistant Su objetivo es establecer:

-   problema;
-   usuarios;
-   propuesta de valor;
-   visión;
-   alcance;
-   casos de uso;
-   funcionalidades;
-   límites;
-   riesgos;
-   métricas;
-   milestones;
-   estrategia técnica;
-   criterios de éxito;
-   entregables de portafolio.

Este documento será la referencia principal para evitar que el producto
crezca sin control o se transforme en una colección de demostraciones
desconectadas.

## 2. Definición del producto

GEEM AI Assistant será una plataforma empresarial de inteligencia
artificial diseñada para consultar conocimiento interno, asistir en
procesos operativos y ejecutar acciones controladas mediante
herramientas autorizadas.

Permitirá que usuarios de una organización interactúen con información y
servicios empresariales utilizando lenguaje natural.

El sistema combinará:

-   conversaciones;
-   recuperación de conocimiento;
-   RAG;
-   structured outputs;
-   tool calling;
-   human approval;
-   memoria controlada;
-   auditoría;
-   observabilidad;
-   evaluación;
-   MCP.

## 3. Visión

Convertir el conocimiento y las capacidades operativas de una empresa en
un asistente seguro, trazable y accionable.

GEEM AI Assistant no será únicamente un chatbot.

Será una capa de interacción inteligente sobre:

-   documentación;
-   procesos;
-   sistemas;
-   servicios;
-   herramientas;
-   conocimiento organizacional.

## 4. Problema principal

Las empresas acumulan información distribuida en:

-   documentos;
-   manuales;
-   mensajes;
-   correos;
-   sistemas;
-   bases de datos;
-   experiencia de personas;
-   procedimientos no estandarizados.

Como resultado:

-   encontrar información toma demasiado tiempo;
-   las respuestas dependen de personas específicas;
-   se repiten consultas;
-   los procedimientos se ejecutan de manera inconsistente;
-   existe pérdida de conocimiento;
-   los nuevos integrantes tardan en aprender;
-   la documentación se utiliza poco;
-   los sistemas permanecen aislados;
-   el soporte depende de memoria humana.

## 5. Problema inicial en Grupo GEEM

Grupo GEEM maneja información relacionada con:

-   Grest;
-   GPOS;
-   Geem Security;
-   Desarrollo de Software;
-   soporte;
-   instalaciones;
-   cotizaciones;
-   clientes;
-   procesos;
-   manuales;
-   membresías;
-   gobierno corporativo;
-   documentación técnica;
-   estrategias comerciales.

Actualmente, una parte importante de este conocimiento se encuentra
distribuida entre:

-   documentos;
-   conversaciones;
-   archivos;
-   experiencia de socios;
-   sistemas existentes;
-   procedimientos informales.

Esto dificulta:

-   localizar respuestas;
-   capacitar personal;
-   estandarizar soporte;
-   preparar propuestas;
-   consultar procesos;
-   reutilizar conocimiento;
-   escalar la operación.

## 6. Oportunidad

Una plataforma AI empresarial puede reducir la fricción entre una
persona y la información que necesita.

En lugar de buscar manualmente en múltiples fuentes, el usuario podrá
preguntar:

-   ¿Cómo se realiza este procedimiento?
-   ¿Qué incluye una membresía?
-   ¿Qué pasos siguen después de una instalación?
-   ¿Qué documentación existe sobre Grest?
-   ¿Cuál es el proceso para atender este tipo de falla?
-   ¿Qué información falta antes de cotizar?
-   ¿Qué acción puede realizarse desde el sistema?

El asistente deberá responder con:

-   información sustentada;
-   fuentes;
-   nivel de confianza;
-   límites claros;
-   acciones disponibles;
-   aprobación cuando corresponda.

## 7. Hipótesis de valor

Creemos que un asistente empresarial con recuperación de conocimiento y
herramientas controladas permitirá a Grupo GEEM:

-   reducir tiempo de búsqueda;
-   disminuir dependencia de personas específicas;
-   mejorar consistencia operativa;
-   acelerar capacitación;
-   documentar mejor procesos;
-   aumentar capacidad de respuesta;
-   conectar conocimiento con acciones empresariales.

Esto se comprobará mediante:

-   tiempo promedio para localizar información;
-   porcentaje de consultas resueltas;
-   precisión de respuestas;
-   uso de fuentes;
-   reducción de escalaciones;
-   acciones completadas;
-   satisfacción de usuarios.

## 8. Objetivo principal

Construir un asistente empresarial multi-tenant capaz de:

## 1. recibir preguntas en lenguaje natural;

## 2. consultar documentación autorizada;

## 3. generar respuestas sustentadas;

## 4. mostrar citas;

## 5. abstenerse cuando no exista evidencia;

## 6. seleccionar herramientas;

## 7. ejecutar acciones seguras;

## 8. solicitar aprobación para acciones sensibles;

## 9. mantener contexto y memoria controlada;

## 10. registrar cada ejecución;

## 11. medir calidad, costo y latencia;

## 12. exponer capacidades mediante API y MCP.

## 9. Objetivos secundarios

El proyecto también deberá:

-   demostrar arquitectura profesional de AI Engineering;
-   construir componentes reutilizables;
-   generar evidencia para portafolio;
-   servir como base para los proyectos posteriores;
-   crear experiencia defendible en entrevistas;
-   validar tecnologías del laboratorio;
-   producir un producto potencialmente utilizable por Grupo GEEM.

## 10. No objetivo

GEEM AI Assistant no buscará, en su primera versión:

-   sustituir todos los sistemas de Grupo GEEM;
-   reemplazar Grest o GPOS;
-   tomar decisiones empresariales autónomas;
-   modificar datos críticos sin aprobación;
-   conectarse desde el inicio a todas las fuentes;
-   convertirse en un agente totalmente autónomo;
-   ejecutar SQL libre;
-   automatizar cualquier proceso imaginable;
-   almacenar todo el conocimiento personal de los usuarios;
-   funcionar como asistente personal general.

## 11. Usuarios objetivo

### 11.1 Administrador de organización

Responsable de:

-   configurar la organización;
-   invitar usuarios;
-   asignar roles;
-   administrar fuentes;
-   configurar herramientas;
-   revisar auditoría;
-   controlar permisos.

### 11.2 Responsable de soporte

Utiliza el asistente para:

-   consultar procedimientos;
-   resolver dudas;
-   localizar documentación;
-   revisar antecedentes;
-   preparar respuestas;
-   crear tickets o seguimientos.

### 11.3 Responsable operativo

Utiliza el asistente para:

-   consultar procesos;
-   revisar checklists;
-   preparar instalaciones;
-   identificar información faltante;
-   ejecutar acciones permitidas.

### 11.4 Responsable comercial

Utiliza el asistente para:

-   consultar servicios;
-   preparar diagnósticos;
-   revisar propuestas;
-   identificar oportunidades;
-   recuperar información comercial.

### 11.5 Técnico o implementador

Utiliza el asistente para:

-   consultar manuales;
-   revisar procedimientos;
-   validar pasos;
-   acceder a información autorizada;
-   registrar resultados.

### 11.6 Usuario de consulta

Puede:

-   realizar preguntas;
-   consultar documentos;
-   revisar fuentes;
-   utilizar herramientas de lectura permitidas.

## 12. Persona principal

Responsable de soporte y operaciones Contexto

Necesita responder rápidamente consultas relacionadas con:

-   sistemas;
-   instalaciones;
-   procedimientos;
-   clientes;
-   soporte;
-   documentación.

Problemas

-   no sabe dónde está la información;
-   depende de otras personas;
-   pierde tiempo buscando;
-   recibe respuestas inconsistentes;
-   puede omitir pasos.

Necesidad

Obtener una respuesta rápida, sustentada y relacionada con el contexto
de la organización.

## 13. Jobs to Be Done

Consulta de conocimiento Cuando necesito resolver una duda operativa,
quiero preguntar en lenguaje natural para obtener una respuesta
sustentada sin revisar manualmente múltiples documentos.

Preparación de trabajo Cuando voy a realizar una instalación o soporte,
quiero consultar requisitos y procedimientos para evitar omisiones.

Acción empresarial Cuando necesito registrar o solicitar una acción,
quiero hacerlo desde la conversación sin navegar por múltiples sistemas.

Aprendizaje Cuando soy nuevo en la organización, quiero consultar
procesos y conceptos para aprender de manera autónoma.

Diagnóstico Cuando un problema está incompleto, quiero que el asistente
identifique la información faltante antes de recomendar una acción.

## 14. Propuesta de valor

Pregunta, encuentra, comprende y actúa sobre el conocimiento de tu
empresa desde un solo lugar.

La propuesta de valor se basa en cinco pilares:

## 1. conocimiento centralizado;

## 2. respuestas verificables;

## 3. acciones controladas;

## 4. seguridad empresarial;

## 5. mejora continua mediante evaluación.

## 15. Diferenciadores

GEEM AI Assistant se diferenciará de un chatbot común por:

-   citas verificables;
-   aislamiento multi-tenant;
-   permisos;
-   tool calling controlado;
-   human approval;
-   auditoría;
-   memoria gobernada;
-   observabilidad completa;
-   evaluación continua;
-   arquitectura independiente de proveedor;
-   MCP;
-   integración con sistemas existentes.

## 16. Principios de producto

### 16.1 Evidence First

Las respuestas empresariales deberán priorizar evidencia.

### 16.2 Safe by Default

Las acciones no autorizadas serán rechazadas.

### 16.3 Human Control

Las decisiones sensibles permanecerán bajo control humano.

### 16.4 Transparency

El usuario deberá distinguir entre:

-   información recuperada;
-   inferencia;
-   acción;
-   limitación;
-   falta de evidencia.

### 16.5 Progressive Capability

El producto crecerá mediante vertical slices completos.

### 16.6 Enterprise Compatibility

La plataforma se integrará con sistemas existentes.

No exigirá reemplazarlos.

## 17. Alcance funcional general

El producto incluirá progresivamente:

-   identidad;
-   organizaciones;
-   tenants;
-   usuarios;
-   roles;
-   conversaciones;
-   mensajes;
-   Model Gateway;
-   Prompt Registry;
-   carga documental;
-   ingestión;
-   extracción;
-   chunking;
-   embeddings;
-   búsqueda híbrida;
-   RAG;
-   citas;
-   tools;
-   aprobaciones;
-   memoria;
-   auditoría;
-   evaluaciones;
-   observabilidad;
-   MCP;
-   panel administrativo.

## 18. Alcance de la primera versión

La primera versión funcional deberá permitir:

## 1. ingresar al sistema;

## 2. seleccionar o resolver una organización;

## 3. iniciar una conversación;

## 4. enviar mensajes;

## 5. generar respuestas mediante Model Gateway;

## 6. almacenar conversaciones;

## 7. visualizar tokens, costo y latencia;

## 8. cargar documentos;

## 9. procesar documentos;

## 10. realizar búsquedas;

## 11. responder utilizando fuentes;

## 12. mostrar citas;

## 13. abstenerse sin evidencia;

## 14. ejecutar una herramienta de lectura;

## 15. solicitar aprobación para una herramienta de escritura;

## 16. registrar auditoría.

## 19. Fuera de alcance inicial

Quedan fuera de la primera versión:

-   voz;
-   llamadas telefónicas;
-   WhatsApp productivo;
-   integración completa con todos los sistemas;
-   agentes multiagente;
-   fine-tuning;
-   generación de imágenes;
-   ejecución de código libre;
-   navegación web abierta;
-   workflows empresariales complejos;
-   facturación;
-   procesamiento masivo de datos;
-   aplicación móvil;
-   personalización avanzada por cliente;
-   soporte offline.

## 20. Casos de uso principales

UC-001 --- Iniciar conversación El usuario crea una conversación dentro
de su organización.

UC-002 --- Consultar conocimiento El usuario realiza una pregunta y
recibe una respuesta basada en documentos autorizados.

UC-003 --- Revisar fuentes El usuario puede identificar qué documentos
sustentan la respuesta.

UC-004 --- Cargar documento Un usuario autorizado carga un archivo para
procesamiento.

UC-005 --- Consultar estado de documento El usuario revisa si el
documento fue procesado o falló.

UC-006 --- Ejecutar herramienta de lectura El asistente consulta
información mediante una tool autorizada.

UC-007 --- Solicitar acción El asistente propone una acción empresarial.

UC-008 --- Aprobar acción Un usuario autorizado aprueba o rechaza la
ejecución.

UC-009 --- Consultar historial El usuario revisa conversaciones
anteriores.

UC-010 --- Administrar acceso Un administrador gestiona usuarios, roles
y permisos.

## 21. Casos de uso secundarios

-   resumir un documento;
-   comparar procedimientos;
-   identificar información faltante;
-   generar checklist;
-   explicar conceptos técnicos;
-   preparar borrador de reporte;
-   clasificar una solicitud;
-   identificar el documento más relevante;
-   consultar estado de herramientas;
-   revisar actividad auditada.

## 22. Primer dominio de conocimiento

El primer dominio de prueba será:

Documentación interna de Grupo GEEM Podrá incluir documentos sanitizados
relacionados con:

-   servicios;
-   procesos;
-   soporte;
-   Grest;
-   GPOS;
-   instalaciones;
-   membresías;
-   procedimientos;
-   manuales técnicos;
-   documentación comercial.

No se utilizarán inicialmente datos confidenciales reales sin un proceso
formal de clasificación y preparación.

## 23. Tipos de documentos iniciales

La primera versión deberá priorizar:

-   PDF;
-   Markdown;
-   texto plano;
-   documentos DOCX;
-   HTML controlado.

El soporte para hojas de cálculo, imágenes y OCR quedará para fases
posteriores cuando exista justificación.

## 24. Preguntas iniciales soportadas

El producto deberá responder preguntas como:

-   ¿Qué servicios ofrece Grupo GEEM?
-   ¿Qué incluye una membresía?
-   ¿Cuál es el procedimiento para realizar una instalación?
-   ¿Qué información se necesita antes de cotizar?
-   ¿Cómo se atiende una falla común?
-   ¿Qué documento explica determinado proceso?
-   ¿Cuáles son los pasos de un levantamiento?
-   ¿Qué diferencias existen entre dos procedimientos?

## 25. Preguntas que deberán generar

abstención El asistente deberá abstenerse cuando:

-   no existe información;
-   el usuario no tiene permiso;
-   las fuentes se contradicen;
-   la pregunta requiere datos actuales no conectados;
-   solicita una acción no disponible;
-   pide información de otro tenant;
-   requiere una decisión humana;
-   busca secretos o datos restringidos.

## 26. Experiencia principal

El flujo principal será:

Logi

``` text
│
▼
```

Workspac

``` text
│
▼
```

New Conversatio

``` text
│
▼
```

User Questio

``` text
│
▼
```

Intent Analysi

``` text
│
├── Direct Respons
├── Knowledge Retrieva
├── Tool Cal
└── Approval Reques
│
▼
```

Structured Respons

``` text
│
▼
```

Sources and Action

## 27. Interfaz principal

La interfaz inicial deberá incluir:

-   navegación;
-   selector de conversación;
-   área de mensajes;
-   caja de entrada;
-   estado de respuesta;
-   fuentes;
-   tool calls;
-   solicitudes de aprobación;
-   costo y latencia en modo técnico;
-   acceso a documentos. n

e

n

s

l

n

e

s

e

t

l

## 28. Tipos de respuesta

El sistema deberá distinguir:

Direct Answer Respuesta general que no requiere conocimiento interno.

Knowledge Answer Respuesta basada en fuentes.

Clarification Solicitud de información necesaria.

Abstention Indicación de que no existe evidencia suficiente.

Tool Result Resultado de una herramienta.

Approval Request Propuesta de acción pendiente.

Error Explicación segura de una falla.

## 29. Contrato conceptual de respuesta

``` text
"response_type": "knowledge_answer"
"message": "Texto para el usuario"
"citations": []
"actions": []
{
```

,

,

,

,

``` text
"confidence": "high"
"abstained": false
"execution_id": "exec-123
```

El contrato definitivo se establecerá durante arquitectura detallada.

## 30. Conversaciones

Una conversación deberá incluir:

-   organización;
-   tenant;
-   usuario;
-   título;
-   estado;
-   mensajes;
-   ejecuciones;
-   fuentes;
-   tools;
-   fechas.

## 31. Mensajes

Los mensajes deberán identificar:

-   autor;
-   rol;
-   contenido;
-   timestamp;
-   modelo cuando aplique;
-   ejecución;
-   fuentes;
-   tool calls;
-   estado.

``` text
}
```

,

,

``` text
"
```

## 32. Model Gateway

El Model Gateway será responsable de:

-   seleccionar proveedor;
-   seleccionar modelo;
-   enviar solicitudes;
-   normalizar respuestas;
-   structured outputs;
-   tool calling;
-   streaming;
-   errores;
-   retries;
-   fallback;
-   tokens;
-   costos;
-   trazas.

## 33. Prompt Registry

El sistema deberá almacenar o identificar:

-   nombre;
-   versión;
-   propósito;
-   template;
-   variables;
-   estado;
-   fecha;
-   evaluación;
-   modelo compatible.

Los prompts no deberán quedar dispersos sin control dentro del código.

## 34. Knowledge Base

La base de conocimiento deberá administrar:

-   documentos;

-   versiones;

-   permisos;

-   metadata;

-   extracción;

-   chunks;

-   embeddings;

-   estado;

-   errores;

-   eliminación.

## 35. Pipeline de ingestión

Uploa

``` text
│
▼
```

Validatio

``` text
│
▼
```

Storag

``` text
│
▼
```

Extractio

``` text
│
▼
```

Normalizatio

``` text
│
▼
```

Chunkin

``` text
│
▼
```

Embedding

``` text
│
▼
```

Indexin

``` text
│
▼
```

Availabl d

e

g

g

e

n

n

s

n

## 36. Retrieval

La estrategia evolucionará por etapas.

Etapa 1 Búsqueda vectorial.

Etapa 2 Búsqueda híbrida.

Etapa 3 Reranking, si demuestra mejora.

Etapa 4 Filtros y estrategias avanzadas.

Cada etapa deberá compararse contra baseline.

## 37. Context Assembly

El sistema deberá:

-   seleccionar fuentes;
-   respetar permisos;
-   eliminar duplicados;
-   conservar referencias;
-   limitar tokens;
-   ordenar evidencia;
-   detectar insuficiencia.

## 38. Citas

Cada cita deberá permitir identificar:

-   documento;

-   fragmento;

-   ubicación;

-   versión;

-   relación con la respuesta.

El usuario deberá poder revisar la evidencia utilizada.

## 39. Tool Registry

El registro de herramientas deberá contener:

-   nombre;
-   descripción;
-   versión;
-   esquema;
-   riesgo;
-   permisos;
-   aprobación;
-   timeout;
-   estado.

## 40. Primera herramienta de lectura

La primera tool de lectura deberá consultar información estructurada y
ficticia o sanitizada.

Ejemplo propuesto:

search_support_procedure

Objetivo:

Buscar procedimientos mediante una API controlada.

## 41. Primera herramienta de escritura

La primera tool de escritura deberá tener impacto bajo y reversible.

Ejemplo propuesto: s

create_support_ticke

La acción deberá:

-   validar argumentos;
-   requerir autorización;
-   solicitar aprobación;
-   registrar auditoría;
-   usar idempotencia;
-   devolver resultado estructurado.

## 42. Human Approval

El flujo deberá mostrar:

-   acción propuesta;
-   parámetros;
-   motivo;
-   riesgo;
-   impacto;
-   botones de aprobar o rechazar;
-   expiración.

La ejecución solo ocurrirá después de una aprobación válida.

## 43. Memoria

La memoria se incorporará después de estabilizar:

-   conversación;
-   RAG;
-   tools;
-   permisos.

Tipos iniciales:

User Preference Preferencias no sensibles. t

Working Context Contexto temporal de una tarea.

Confirmed Fact Información confirmada y autorizada.

## 44. Límites de memoria

No se almacenará automáticamente:

-   información sensible;
-   contraseñas;
-   secretos;
-   opiniones inferidas;
-   datos no confirmados;
-   información de otros usuarios;
-   datos fuera de propósito.

## 45. MCP

El producto expondrá capacidades mediante un MCP Server.

Capacidades iniciales:

-   consultar documentos;
-   buscar conocimiento;
-   consultar conversaciones autorizadas;
-   ejecutar tools permitidas.

MCP reutilizará:

-   autenticación;
-   autorización;
-   tenant;
-   auditoría;
-   casos de uso.

## 46. Panel administrativo

El panel inicial deberá permitir progresivamente:

-   gestionar organización;
-   gestionar usuarios;
-   revisar documentos;
-   revisar estados de ingestión;
-   configurar tools;
-   revisar aprobaciones;
-   consultar auditoría;
-   revisar métricas básicas.

## 47. Multi-Tenancy

El producto será multi-tenant desde su estructura inicial.

Todo recurso empresarial deberá relacionarse con:

tenant_i

Esto incluirá:

-   usuarios;
-   conversaciones;
-   documentos;
-   chunks;
-   tools;
-   memorias;
-   auditoría;
-   configuraciones;
-   evaluaciones.

## 48. Roles iniciales

owne administrato manage operato viewe

Los permisos se definirán explícitamente. r

r

r

r

d

r

## 49. Seguridad mínima

La primera versión deberá incluir:

-   autenticación;
-   autorización;
-   multi-tenancy;
-   validación;
-   rate limiting básico;
-   gestión de secretos;
-   auditoría;
-   redacción;
-   tool allowlist;
-   aprobación;
-   pruebas negativas;
-   prompt injection testing.

## 50. Observabilidad mínima

La primera versión deberá registrar:

-   requests;
-   errores;
-   latencia;
-   modelo;
-   prompt;
-   tokens;
-   costo;
-   retrieval;
-   sources;
-   tools;
-   aprobaciones;
-   ingestión;
-   correlation ID;
-   execution ID.

## 51. Evaluación mínima

La primera versión deberá incluir datasets para:

-   respuestas directas;

-   RAG;

-   abstención;

-   citas;

-   tool selection;

-   tool arguments;

-   autorización;

-   prompt injection;

-   tenant isolation.

## 52. Métricas de producto

Uso - usuarios activos; - conversaciones; - consultas; - documentos; -
tool calls.

Calidad - consultas resueltas; - groundedness; - citation accuracy; -
abstention accuracy; - tool selection accuracy.

Operación - latencia; - errores; - disponibilidad; - costo; - ingestión.

Negocio - tiempo ahorrado; - escalaciones evitadas; - procedimientos
consultados; - acciones completadas; - satisfacción.

## 53. Métricas objetivo iniciales

Objetivo Métrica inicial Retrieval Hit Rate@5 ≥ 90% Citation Accuracy ≥
95% Groundedness ≥ 90% Abstention Accuracy ≥ 90% Tool Selection ≥ 95%
Accuracy Authorization 100% Compliance Tenant Isolation 100% Structured
Output ≥ 98% Success RAG Query p95 ≤ 12 s

## 54. Indicadores de éxito del producto

El producto se considerará exitoso cuando:

-   los usuarios encuentran información más rápido;
-   las respuestas incluyen evidencia;
-   el sistema se abstiene correctamente;
-   no existen fugas entre tenants;
-   las tools se ejecutan de forma segura;
-   las acciones sensibles requieren aprobación;
-   las ejecuciones pueden rastrearse;
-   la calidad puede medirse;
-   el producto puede demostrarse en vivo;
-   la arquitectura puede defenderse en entrevista.

## 55. Riesgos de producto

R-001 --- Falta de documentación útil El RAG no puede responder si la
documentación es insuficiente.

Mitigación

-   seleccionar dominio inicial limitado;
-   preparar documentos;
-   medir cobertura;
-   detectar preguntas sin respuesta.

R-002 --- Respuestas convincentes pero incorrectas Mitigación

-   citations;
-   abstention;
-   structured outputs;
-   evaluation;
-   review.

R-003 --- Alcance excesivo Mitigación

-   milestones;
-   vertical slices;
-   fuera de alcance explícito;
-   WIP limitado.

R-004 --- Complejidad prematura Mitigación

-   modular monolith;
-   proveedor principal;
-   pgvector;
-   un agente inicial;
-   tools limitadas.

R-005 --- Falta de uso real Mitigación

-   casos de Grupo GEEM;

-   pruebas con usuarios;

-   métricas de negocio;

-   piloto interno.

## 56. Riesgos técnicos

-   errores de proveedor;
-   variabilidad de modelos;
-   costo;
-   latencia;
-   output inválido;
-   retrieval deficiente;
-   documentos maliciosos;
-   problemas de parsing;
-   dependencias externas;
-   pérdida de contexto;
-   observabilidad insuficiente.

## 57. Riesgos de seguridad

-   fuga entre tenants;
-   tool abuse;
-   prompt injection;
-   documentos envenenados;
-   memoria contaminada;
-   secretos en logs;
-   acceso indebido;
-   bypass de aprobación;
-   URLs de archivos expuestas.

## 58. Supuestos

El proyecto asume que:

-   existe documentación inicial utilizable;
-   habrá acceso a proveedores LLM;
-   PostgreSQL soportará pgvector;
-   Docker estará disponible;
-   el producto iniciará con pocos usuarios;
-   las primeras integraciones podrán simularse;
-   Grupo GEEM servirá como dominio piloto.

## 59. Restricciones

-   presupuesto limitado;
-   desarrollo inicial por una persona;
-   necesidad de aprendizaje;
-   prioridad en portafolio;
-   evitar infraestructura excesiva;
-   necesidad de mantener sistemas actuales;
-   no exponer datos empresariales reales públicamente.

## 60. Estrategia de construcción

El producto se desarrollará mediante vertical slices.

Orden general:

Foundatio

``` text
│
▼
```

Conversation Slic

``` text
│
▼
```

Identity and Tenan

``` text
│
▼
```

Knowledge Ingestio

``` text
│
▼
```

RA

``` text
│
▼
```

Tool

``` text
│
▼
```

Approval

``` text
│
▼
```

Memor

``` text
│
▼
```

MC

``` text
│
▼
```

G

P

s

y

s

n

e

n

t

Production Readines

``` text
│
▼
```

Portfolio Releas

## 61. Milestone 0 --- Repository

Foundation Objetivo:

Crear una base reproducible y gobernada.

Incluye:

-   repositorio;
-   estructura;
-   README inicial;
-   Docker;
-   API;
-   frontend;
-   PostgreSQL;
-   Redis;
-   CI;
-   lint;
-   testing;
-   documentación;
-   ADR index.

Criterio de salida El proyecto puede clonarse, levantarse y validarse
automáticamente.

## 62. Milestone 1 --- First Conversation

Objetivo:

Implementar el primer flujo completo de conversación.

Incluye:

-   interfaz; e

s

-   endpoint;
-   Model Gateway;
-   provider adapter;
-   structured response;
-   persistencia;
-   streaming;
-   tokens;
-   costo;
-   traces.

Criterio de salida El usuario puede enviar un mensaje y recibir una
respuesta persistida, validada y observable.

## 63. Milestone 2 --- Identity and Multi-

Tenancy Objetivo:

Establecer identidad y aislamiento.

Incluye:

-   organizations;
-   tenants;
-   usuarios;
-   roles;
-   permisos;
-   tenant context;
-   pruebas de aislamiento;
-   auditoría básica.

Criterio de salida Dos tenants pueden usar el sistema sin acceder a
recursos cruzados.

## 64. Milestone 3 --- Knowledge Ingestion

Objetivo:

Cargar y procesar documentos.

Incluye:

-   upload;
-   metadata;
-   object storage;
-   extracción;
-   chunking;
-   embeddings;
-   pgvector;
-   workers;
-   estados;
-   retry;
-   observabilidad.

Criterio de salida Un documento autorizado puede cargarse, procesarse e
indexarse de forma reproducible.

## 65. Milestone 4 --- RAG and Citations

Objetivo:

Responder mediante conocimiento interno.

Incluye:

-   vector retrieval;
-   filtros;
-   context assembly;
-   generation;
-   citations;
-   abstention;
-   dataset;
-   evaluación;
-   dashboard.

Criterio de salida El usuario recibe respuestas sustentadas con citas y
el sistema se abstiene cuando no existe evidencia.

## 66. Milestone 5 --- Hybrid Retrieval

Objetivo:

Mejorar recuperación.

Incluye:

-   full-text;
-   vector;
-   merge;
-   evaluación;
-   comparison;
-   reranking spike.

Criterio de salida La estrategia híbrida demuestra mejora frente al
baseline.

## 67. Milestone 6 --- Tool Calling

Objetivo:

Conectar el asistente con capacidades empresariales.

Incluye:

-   Tool Registry;
-   tool schema;
-   tool selection;
-   autorización;
-   tool de lectura;
-   auditoría;
-   evaluación;
-   error handling.

Criterio de salida El asistente selecciona y ejecuta correctamente una
tool de lectura autorizada.

## 68. Milestone 7 --- Human Approval

Objetivo:

Controlar acciones con impacto.

Incluye:

-   tool de escritura;
-   riesgo;
-   approval request;
-   approve;
-   reject;
-   expiration;
-   idempotency;
-   audit;
-   UI.

Criterio de salida Una acción de escritura no puede ejecutarse sin
aprobación válida.

## 69. Milestone 8 --- Memory

Objetivo:

Incorporar memoria segura y útil.

Incluye:

-   memory types;

-   creation policy;

-   retrieval;

-   correction;

-   expiration;

-   deletion;

-   tenant isolation;

-   evaluation.

Criterio de salida La memoria mejora un flujo sin contaminar usuarios o
tenants.

## 70. Milestone 9 --- MCP Server

Objetivo:

Exponer capacidades a clientes compatibles.

Incluye:

-   server;
-   authentication;
-   resources;
-   tools;
-   permissions;
-   audit;
-   tests;
-   cliente de demostración.

Criterio de salida Un cliente MCP autorizado puede consultar
conocimiento y ejecutar una tool permitida.

## 71. Milestone 10 --- Production

Readiness Objetivo:

Preparar el sistema para operación controlada.

Incluye:

-   deployment;

-   CI/CD;

-   health checks;

-   dashboards;

-   alerts;

-   runbooks;

-   backups;

-   rollback;

-   security review;

-   evaluation report.

Criterio de salida El producto cumple el estándar Production Ready.

## 72. Milestone 11 --- Portfolio Release

Objetivo:

Convertir el proyecto en evidencia profesional.

Incluye:

-   repositorio sanitizado;
-   README;
-   arquitectura;
-   demo;
-   video;
-   caso de estudio;
-   métricas;
-   decisiones;
-   entrevista;
-   release.

Criterio de salida El proyecto cumple el estándar Portfolio Ready.

## 73. Priorización MoSCoW

Must Have - conversación; - Model Gateway;

-   multi-tenancy;
-   RAG;
-   citas;
-   abstención;
-   tool calling;
-   aprobación;
-   auditoría;
-   evaluación;
-   observabilidad;
-   seguridad.

Should Have - búsqueda híbrida; - memoria; - MCP; - panel
administrativo; - streaming; - feedback.

Could Have - múltiples proveedores activos; - reranking avanzado; -
recomendaciones; - dashboards de negocio; - importación desde fuentes
externas.

Won't Have Initially - multiagentes; - fine-tuning; - voz; - aplicación
móvil; - navegación web abierta; - automatizaciones empresariales
complejas.

## 74. Estrategia de datos

El producto utilizará inicialmente:

-   datos ficticios;

-   documentación sanitizada;

-   fixtures;

-   tenants demo;

-   usuarios demo;

-   ejemplos controlados.

Los datos reales se incorporarán únicamente después de:

-   clasificación;
-   aprobación;
-   políticas;
-   seguridad;
-   retención.

## 75. Estrategia de demostración

La demo principal mostrará:

## 1. inicio de sesión;

## 2. selección de organización;

## 3. consulta general;

## 4. pregunta respondida con RAG;

## 5. fuentes;

## 6. pregunta sin respuesta y abstención;

## 7. tool de lectura;

## 8. propuesta de acción;

## 9. aprobación;

## 10. ejecución;

## 11. auditoría;

## 12. trace;

## 13. dashboard;

## 14. métricas de evaluación.

## 76. Escenario de demo

Ejemplo:

Un responsable de soporte pregunta:

¿Cuál es el procedimiento para preparar una instalación de red en un
restaurante?

El sistema:

## 1. recupera documentación;

## 2. genera una respuesta;

## 3. muestra fuentes;

## 4. crea un checklist;

## 5. identifica datos faltantes;

## 6. propone crear un ticket;

## 7. solicita aprobación;

## 8. crea el registro;

## 9. muestra auditoría.

## 77. Historia técnica principal

El proyecto deberá demostrar:

Diseñé y construí un asistente empresarial multi-tenant con RAG, tool
calling, human approval, memoria, MCP, evaluación y observabilidad,
integrado mediante una arquitectura modular independiente del proveedor
de modelos.

## 78. Historias para entrevistas

El proyecto deberá permitir explicar:

-   por qué se eligió modular monolith;
-   cómo se diseñó multi-tenancy;
-   cómo se evaluó RAG;
-   cómo se evitó acceso directo del LLM a datos;
-   cómo se protegieron tools;
-   cómo se implementó aprobación;
-   cómo se midieron costos;
-   cómo se manejaron fallos;
-   cómo se construyó MCP;
-   cómo se evitó vendor lock-in.

## 79. Evidencia de portafolio

El proyecto deberá producir:

-   README profesional;

-   diagramas C4;

-   diagramas de secuencia;

-   ADRs;

-   capturas;

-   video;

-   demo;

-   evaluation report;

-   security overview;

-   traces;

-   dashboards;

-   caso de estudio;

-   release notes.

## 80. Arquitectura conceptual

Web Applicatio

``` text
│
▼
```

FastAP

``` text
│
├── Identit
├── Conversatio
├── Knowledg
├── Tool
├── Approva
├── Memor
├── Evaluatio
└── Audi
│
▼
```

AI Application Laye

``` text
│
┌──────┼───────────┐
▼      ▼           ▼
```

Model Gateway Retrieval Tool Registr

``` text
│          │           │
▼          ▼           ▼
```

Providers PostgreSQL Integration pgvecto

## 81. Stack inicial

Backend - Python; - FastAPI; - Pydantic; I

n

t

s

y

l

y

e

n

r

n

r

y

s

-   SQLAlchemy;
-   Alembic.

Frontend - React; - TypeScript; - Vite.

Data - PostgreSQL; - pgvector; - Redis; - object storage compatible con
S3.

AI - OpenAI como proveedor principal; - Anthropic como proveedor
secundario; - Model Gateway propio; - LangGraph cuando se requiera
estado agéntico.

Infrastructure - Docker; - Docker Compose; - GitHub Actions; -
OpenTelemetry.

## 82. Arquitectura de despliegue inicial

La primera versión podrá desplegarse como:

-   frontend;
-   API;
-   worker;
-   PostgreSQL;
-   Redis;
-   object storage;
-   OpenTelemetry Collector.

La infraestructura deberá mantenerse simple y reproducible.

## 83. Dependencias externas

-   proveedor LLM;
-   proveedor de embeddings;
-   almacenamiento;
-   plataforma de despliegue;
-   identidad cuando se incorpore un proveedor externo;
-   backend de observabilidad.

Cada dependencia deberá tener:

-   adapter;
-   timeout;
-   error handling;
-   fallback o degradación;
-   documentación.

## 84. Estrategia de proveedores

Proveedor principal OpenAI.

Proveedor secundario Anthropic.

Regla El producto no deberá acoplar los casos de uso directamente a SDKs
de proveedores.

## 85. Estrategia de costos

El producto deberá:

-   registrar costos;

-   establecer presupuestos;

-   limitar contexto;

-   limitar output;

-   controlar pasos;

-   utilizar modelos según tarea;

-   evitar tool calls innecesarias;

-   comparar proveedores.

## 86. Presupuestos iniciales

Valores iniciales sujetos a evaluación:

Flujo Presupuesto esperado Consulta simple ≤ USD 0.02 Consulta RAG ≤ USD
0.05 Tool de lectura ≤ USD 0.05 Acción con aprobación ≤ USD 0.10
Ingestión medido por documento

## 87. Experiencia de error

Los errores deberán comunicarse de forma:

-   clara;
-   segura;
-   accionable;
-   sin detalles internos sensibles.

Ejemplos:

-   no pude encontrar evidencia suficiente;
-   no tienes permiso para consultar ese recurso;
-   la acción requiere aprobación;
-   el documento no pudo procesarse;
-   el proveedor no está disponible temporalmente.

## 88. Degradación controlada

El sistema podrá:

-   responder sin memoria;
-   utilizar proveedor alterno;
-   usar búsqueda textual;
-   omitir tool opcional;
-   guardar solicitud para reintento;
-   solicitar acción manual.

Nunca deberá inventar resultados para ocultar una falla.

## 89. Accesibilidad y usabilidad

La interfaz deberá priorizar:

-   claridad;
-   navegación simple;
-   estados visibles;
-   mensajes comprensibles;
-   acciones confirmables;
-   fuentes accesibles;
-   uso por teclado;
-   contraste adecuado.

## 90. Idiomas

El idioma principal será español.

La arquitectura deberá permitir inglés posteriormente.

Prompts, datasets y evaluaciones deberán indicar idioma.

## 91. Criterio de MVP

El MVP estará completo cuando pueda demostrar:

-   conversación;

-   multi-tenancy;

-   ingestión;

-   RAG;

-   citas;

-   abstención;

-   tool de lectura;

-   tool de escritura;

-   aprobación;

-   auditoría;

-   evaluación;

-   observabilidad.

No se considerará MVP una interfaz conectada únicamente a un modelo.

## 92. Criterio de Production Ready

El producto será Production Ready cuando:

-   cumpla Definition of Done;
-   pase evaluación;
-   pase seguridad;
-   tenga observabilidad;
-   tenga despliegue reproducible;
-   tenga rollback;
-   tenga runbooks;
-   tenga aislamiento;
-   tenga documentación.

## 93. Criterio de Portfolio Ready

Será Portfolio Ready cuando, además:

-   tenga narrativa empresarial;
-   tenga repositorio sanitizado;
-   tenga demo;
-   tenga métricas;
-   tenga caso de estudio;
-   tenga video;
-   tenga diagramas;
-   tenga preguntas de entrevista;
-   pueda defenderse técnicamente.

## 94. Criterio para iniciar el Proyecto 2

Restaurant AI Operations no deberá comenzar hasta que GEEM AI Assistant
tenga:

-   Model Gateway estable;
-   identidad;
-   multi-tenancy;
-   RAG;
-   tools;
-   approvals;
-   evaluación;
-   observabilidad;
-   release demostrable.

## 95. Definition of Product Success

GEEM AI Assistant habrá cumplido su propósito cuando demuestre que un
asistente empresarial puede:

-   comprender una solicitud;
-   encontrar conocimiento autorizado;
-   responder con evidencia;
-   abstenerse;
-   ejecutar acciones controladas;
-   mantener contexto;
-   operar de forma trazable;
-   medir su calidad;
-   integrarse con sistemas existentes.

## 96. Decisiones oficiales

Quedan aprobadas las siguientes definiciones:

## 1. GEEM AI Assistant será el primer producto del AI Engineering Lab.

## 2. Será un Enterprise AI Assistant, no un chatbot genérico.

## 3. Grupo GEEM será el dominio piloto.

## 4. El idioma principal será español.

## 5. El producto será multi-tenant desde el inicio.

## 6. La primera fuente será documentación sanitizada.

## 7. La primera versión incluirá RAG con citas y abstención.

## 8. El producto incluirá tool calling controlado.

## 9. La primera tool de escritura requerirá aprobación.

## 10. El producto incluirá auditoría y observabilidad.

## 11. El Model Gateway será propio.

## 12. OpenAI será el proveedor principal.

## 13. Anthropic será proveedor secundario.

## 14. PostgreSQL y pgvector serán la base inicial.

## 15. La arquitectura será modular monolith.

## 16. MCP formará parte del alcance del proyecto.

## 17. La memoria se incorporará después de estabilizar RAG y tools.

## 18. Los agentes complejos y sistemas multiagente quedan fuera del MVP.

## 19. El proyecto se construirá mediante milestones y vertical slices.

## 20. Cada milestone producirá evidencia técnica y de portafolio.

## 21. No se iniciará el Proyecto 2 hasta completar una release demostrable.

## 22. La calidad se medirá mediante datasets, métricas y evaluación.

## 23. La seguridad y el aislamiento serán hard gates.

## 24. El producto deberá poder operar con datos ficticios o sanitizados.

## 25. El resultado final deberá ser defendible ante recruiters, hiring managers y Staff

Engineers.

## 97. Próximo documento

Documento 11 --- Project 1 Architecture Definition Definirá la
arquitectura específica de GEEM AI Assistant:

-   bounded contexts;
-   módulos;
-   componentes;
-   dependencias;
-   data model inicial;
-   APIs;
-   eventos;
-   workers;
-   almacenamiento;
-   Model Gateway;
-   RAG;
-   Tool Registry;
-   Approval Engine;
-   Memory;
-   MCP;
-   observabilidad;
-   despliegue;
-   diagramas C4;
-   decisiones arquitectónicas iniciales.

## 98. Conclusión

GEEM AI Assistant será el primer producto real construido bajo los
estándares del AI Engineering Lab.

No será una demostración aislada de generación de texto.

Será una plataforma empresarial que combine:

-   conocimiento;
-   inteligencia artificial;
-   herramientas;
-   seguridad;
-   evaluación;
-   observabilidad;
-   integración.

Su construcción permitirá demostrar que Erick puede diseñar, implementar
y operar sistemas modernos de AI Engineering con criterios profesionales
de arquitectura, confiabilidad y negocio.
