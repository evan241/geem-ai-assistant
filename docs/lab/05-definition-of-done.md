# AI Engineering Lab

## Documento 05 — Definition of Done

**Versión:** 1.0
**Estado:** Estándar oficial
**Responsable técnico:** Director de AI Engineering
**Lead Engineer:** Erick Eduardo Evangelista Velasco
## 1. Propósito

Este documento define los criterios oficiales para considerar terminado cualquier entregable dentro del AI
Engineering Lab.
La Definition of Done se aplicará a:
- issues;
- tareas técnicas;
- componentes;
- endpoints;
- herramientas;
- prompts;
- pipelines RAG;
- agentes;
- workflows;
- integraciones;
- milestones;
- releases;
- proyectos;
- entregables de portafolio.
Su propósito es evitar que una capacidad se considere terminada solamente porque:
- funciona una vez;
- produce una respuesta convincente;
- corre en la computadora del desarrollador;
- pasa una demostración preparada;
- fue implementada visualmente;
- el modelo parece responder correctamente;
- el código fue escrito.
Una funcionalidad estará terminada cuando exista evidencia verificable de que cumple su propósito, puede
mantenerse y opera dentro de los estándares del laboratorio.

## 2. Principio rector

“Funciona” describe un resultado observado. “Terminado” describe un resultado probado,
documentado, seguro, reproducible y aceptado.
El laboratorio no medirá avance únicamente por código producido.
El avance se medirá por capacidades completas.
## 3. Definición general de terminado

Un entregable estará terminado cuando:
- resuelve el problema definido;
- cumple sus criterios de aceptación;
- está integrado correctamente;
- tiene pruebas apropiadas;
- maneja errores esperados;
- respeta seguridad y permisos;
- es observable;
- está documentado;
- puede reproducirse;
- ha sido revisado;
- no deja riesgos críticos abiertos;
- cuenta con evidencia.
## 4. Diferencia entre Done y Released

Done
El entregable está completo dentro de su alcance técnico y funcional.
Released
El entregable fue:
- versionado;
- desplegado;
- publicado;
- comunicado;
- 1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
12.

validado en el ambiente correspondiente.
Una funcionalidad puede estar Done sin haberse liberado todavía.
No puede considerarse Released si no está Done.
## 5. Diferencia entre Done y Perfect

La Definition of Done no exige perfección.
Un entregable puede considerarse terminado aun cuando existan:
- mejoras futuras;
- optimizaciones;
- funcionalidades fuera de alcance;
- limitaciones conocidas;
- deuda técnica controlada.
La condición es que dichas limitaciones estén:
- identificadas;
- documentadas;
- aceptadas;
- fuera del alcance comprometido;
- sin riesgo crítico oculto.
## 6. Niveles de completitud

Los entregables podrán pasar por cinco estados.
### 6.1. Draft

Existe una propuesta o implementación inicial.
No cumple todavía criterios de integración.
### 6.2. Functional

El flujo principal funciona bajo condiciones controladas.

### 6.3. Integrated

La capacidad está conectada correctamente con el sistema.
### 6.4. Production Ready

Cumple calidad, seguridad, observabilidad, operación y documentación.
### 6.5. Portfolio Ready

Además de estar lista para producción, puede presentarse públicamente y defenderse técnicamente.
## 7. Estado permitido por tipo de trabajo

Entregable Nivel mínimo requerido
Spike de investigación Functional
Prototipo descartable Functional
Issue técnico normal Integrated
Funcionalidad principal Production Ready
Milestone Production Ready
Release pública Portfolio Ready
Proyecto final Portfolio Ready
## 8. Definition of Done para un Issue

Un issue estará terminado cuando:
- el problema descrito fue resuelto;
- se cumplieron los criterios de aceptación;
- el alcance no fue ampliado sin documentarlo;
- existe un Pull Request integrado;
- las pruebas relacionadas pasan;
- la documentación fue actualizada;
- los riesgos encontrados fueron registrados;
- no existen subtareas críticas pendientes;
- el issue contiene evidencia o enlaces a ella;
- el estado final fue validado.

Evidencia posible
- Pull Request;
- capturas;
- logs;
- resultado de pruebas;
- métricas;
- benchmark;
- ADR;
- video;
- enlace a ambiente;
- reporte de evaluación.
## 9. Definition of Done para una tarea técnica

Una tarea técnica estará terminada cuando:
- el cambio es funcional;
- el código cumple estándares;
- se eliminaron soluciones temporales no aprobadas;
- no existen errores conocidos dentro del alcance;
- tiene pruebas;
- pasa lint y type checking;
- puede ejecutarse desde una instalación limpia;
- no contiene secretos;
- fue integrada mediante PR;
- el resultado puede explicarse técnicamente.
## 10. Definition of Done para código

El código estará terminado cuando:
- es legible;
- tiene nombres claros;
- respeta límites de módulos;
- evita duplicación injustificada;
- no contiene código muerto;
- no contiene logs temporales;
- no expone datos sensibles;
- maneja errores;
- incluye tipos;
- tiene pruebas relevantes;
- cumple contratos;

mantiene compatibilidad acordada.
No se considerará terminado si
- funciona únicamente con datos preparados;
- requiere modificar manualmente el código;
- contiene valores hardcoded no justificados;
- depende de archivos locales no versionados;
- necesita pasos no documentados;
- ignora errores del proveedor;
- no valida entradas.
## 11. Definition of Done para un módulo

Un módulo estará terminado cuando:
- tiene responsabilidad clara;
- sus límites están definidos;
- expone contratos explícitos;
- no tiene dependencias circulares;
- oculta detalles internos;
- tiene pruebas unitarias;
- tiene pruebas de integración cuando aplica;
- documenta entradas y salidas;
- maneja errores;
- incluye observabilidad;
- respeta tenant y permisos;
- puede sustituirse o evolucionar sin afectar indebidamente otros módulos.
## 12. Definition of Done para un endpoint

Un endpoint estará terminado cuando:
- tiene ruta y método correctos;
- valida la solicitud;
- autentica al usuario;
- autoriza la operación;
- resuelve el tenant;
- invoca un caso de uso;
- devuelve contrato estructurado;
- maneja errores esperados;
- utiliza códigos HTTP correctos;
- está documentado en OpenAPI;

- tiene pruebas;
- genera trazas;
- no expone información sensible.
Requisitos adicionales
Debe tener pruebas para:
- solicitud válida;
- entrada inválida;
- usuario no autenticado;
- permiso insuficiente;
- recurso inexistente;
- tenant incorrecto;
- error de integración;
- respuesta esperada.
## 13. Definition of Done para una integración

externa
Una integración estará terminada cuando:
- utiliza un adaptador;
- tiene contrato definido;
- maneja autenticación;
- configura timeouts;
- aplica retries únicamente cuando corresponde;
- maneja rate limits;
- registra trazas;
- sanitiza errores;
- cuenta con pruebas de integración;
- puede simularse en pruebas;
- documenta límites;
- tiene estrategia de degradación;
- considera idempotencia.
También deberá documentar
- propietario del sistema externo;
- ambiente de pruebas;
- credenciales requeridas;
- cuotas;
- políticas de error;
- plan de sustitución.

## 14. Definition of Done para un proveedor de

modelos
Un adaptador de modelos estará terminado cuando:
- implementa el contrato del Model Gateway;
- soporta solicitudes básicas;
- soporta streaming cuando aplica;
- soporta structured outputs;
- soporta tool calling cuando aplica;
- normaliza errores;
- registra uso;
- registra tokens;
- estima costos;
- aplica timeouts;
- maneja rate limits;
- tiene pruebas;
- cuenta con fallback o degradación definida.
Evidencia requerida
- prueba funcional;
- prueba de error;
- prueba de timeout;
- prueba de output inválido;
- comparación mínima de costo y latencia;
- documentación de modelos soportados.
## 15. Definition of Done para Structured Outputs

Un flujo estructurado estará terminado cuando:
- tiene esquema explícito;
- valida la respuesta;
- rechaza resultados incompatibles;
- maneja campos opcionales;
- limita reintentos;
- registra fallos;
- tiene pruebas con respuestas inválidas;
- no depende de parsing informal;
- documenta el contrato;
- mide tasa de éxito.

Métricas mínimas
- porcentaje de outputs válidos;
- porcentaje de reintentos;
- porcentaje de fallos;
- latencia;
- costo promedio.
## 16. Definition of Done para un Prompt

Un prompt estará terminado cuando:
- tiene propósito definido;
- tiene nombre;
- tiene versión;
- documenta variables;
- documenta formato de salida;
- separa instrucciones de datos;
- fue probado con un dataset;
- tiene métricas;
- fue comparado contra una versión anterior;
- tiene estado approved ;
- está relacionado con una funcionalidad;
- tiene estrategia de rollback.
Un prompt no estará terminado si
- únicamente “suena bien”;
- fue probado con dos o tres ejemplos favorables;
- contiene reglas empresariales críticas;
- mezcla instrucciones con documentos recuperados;
- no maneja falta de información;
- no limita el comportamiento esperado.
## 17. Definition of Done para Tool Calling

Una herramienta estará terminada cuando:
- tiene nombre y objetivo claros;
- su esquema está validado;
- los argumentos están tipados;
- tiene clasificación de riesgo;

- exige permisos;
- resuelve tenant;
- tiene timeout;
- tiene idempotencia cuando aplica;
- registra auditoría;
- devuelve resultado estructurado;
- maneja errores;
- tiene pruebas;
- define si requiere aprobación.
Pruebas obligatorias
- ejecución válida;
- argumentos inválidos;
- usuario sin permiso;
- tenant incorrecto;
- timeout;
- error externo;
- llamada duplicada;
- aprobación requerida;
- aprobación rechazada;
- auditoría generada.
## 18. Definition of Done para herramientas de

lectura
Además de los criterios generales:
- no deben modificar estado;
- deben limitar campos;
- deben respetar permisos;
- deben filtrar tenant;
- deben proteger información sensible;
- deben paginar cuando corresponda;
- deben registrar acceso.

## 19. Definition of Done para herramientas de

escritura
Además de los criterios generales:
- deben validar estado previo;
- deben verificar reglas de dominio;
- deben usar idempotencia;
- deben registrar estado anterior y nuevo;
- deben permitir compensación cuando sea posible;
- deben requerir aprobación según riesgo;
- deben producir evento o auditoría.
## 20. Definition of Done para una aprobación

humana
El flujo estará terminado cuando:
- genera solicitud de aprobación;
- muestra la acción;
- muestra los argumentos;
- muestra el impacto;
- identifica el riesgo;
- registra solicitante;
- registra aprobador;
- permite aprobar o rechazar;
- evita doble ejecución;
- maneja expiración;
- registra la decisión;
- ejecuta únicamente después de aprobación válida.
## 21. Definition of Done para ingestión documental

Un pipeline de ingestión estará terminado cuando:
- valida el archivo;
- identifica tipo y tamaño;
- verifica seguridad;
- calcula checksum;
- almacena el original;

- registra metadata;
- procesa de forma asíncrona;
- extrae contenido;
- normaliza texto;
- divide en chunks;
- genera embeddings;
- indexa;
- actualiza estado;
- maneja errores;
- permite reintentar;
- evita duplicados;
- registra trazas.
Estados mínimos
uploaded
pending
processing
indexed
failed
archived
## 22. Definition of Done para extracción documental

La extracción estará terminada cuando:
- soporta los formatos definidos;
- conserva metadata;
- maneja documentos vacíos;
- maneja texto corrupto;
- detecta errores;
- produce contenido normalizado;
- registra método de extracción;
- tiene fixtures de prueba;
- mide tasa de éxito;
- documenta formatos no soportados.

## 23. Definition of Done para Chunking

Una estrategia de chunking estará terminada cuando:
- tiene objetivo;
- define tamaño;
- define overlap;
- conserva metadata;
- mantiene relación con documento y versión;
- evita chunks vacíos;
- tiene pruebas;
- fue evaluada;
- puede reindexarse;
- tiene versión.
Evidencia mínima
Comparación con al menos una estrategia alternativa cuando el chunking afecte significativamente el
resultado.
## 24. Definition of Done para Embeddings

El componente estará terminado cuando:
- tiene proveedor;
- tiene modelo;
- registra dimensiones;
- procesa en lotes;
- maneja reintentos;
- evita duplicados;
- calcula costos;
- almacena versión;
- permite reindexación;
- tiene pruebas;
- mide latencia;
- documenta estrategia de migración.
## 25. Definition of Done para búsqueda vectorial

La búsqueda vectorial estará terminada cuando:
- filtra tenant;

- aplica permisos;
- utiliza metadata;
- devuelve score;
- limita resultados;
- maneja consultas vacías;
- tiene pruebas;
- mide recall;
- mide latencia;
- documenta índice;
- compara contra búsqueda exacta cuando usa índice aproximado.
## 26. Definition of Done para búsqueda híbrida

La búsqueda híbrida estará terminada cuando:
- combina búsqueda semántica y textual;
- normaliza resultados;
- aplica filtros;
- elimina duplicados;
- permite ponderación;
- tiene evaluación;
- mide relevancia;
- maneja códigos, nombres y lenguaje natural;
- documenta estrategia de fusión.
## 27. Definition of Done para Reranking

El reranking estará terminado cuando:
- recibe candidatos;
- devuelve orden explícito;
- limita cantidad;
- registra latencia;
- registra costo;
- tiene fallback;
- mejora métricas frente a baseline;
- tiene evaluación;
- documenta modelo o algoritmo.
No se incorporará si no demuestra mejora suficiente.

## 28. Definition of Done para Context Assembly

El ensamblado de contexto estará terminado cuando:
- respeta límite de tokens;
- prioriza fuentes;
- conserva referencias;
- elimina duplicados;
- delimita contenido;
- excluye contenido no autorizado;
- registra documentos utilizados;
- maneja contexto insuficiente;
- tiene pruebas.
## 29. Definition of Done para un Pipeline RAG

Un pipeline RAG estará terminado cuando:
- existe ingestión;
- existe versionado documental;
- existe chunking;
- existen embeddings;
- existe retrieval;
- existen filtros de tenant;
- existe búsqueda híbrida cuando esté justificada;
- existe reranking cuando aporte valor;
- existe context assembly;
- existen citas;
- existe abstención;
- existe evaluación;
- existe observabilidad;
- existen pruebas de seguridad;
- existe manejo de errores.
Métricas mínimas
- retrieval hit rate;
- recall;
- relevancia;
- groundedness;
- calidad de citas;
- abstención correcta;
- latencia;
- costo;

tasa de respuestas no sustentadas.
## 30. Criterio de abstención

El RAG deberá abstenerse cuando:
- no encuentra evidencia;
- las fuentes son contradictorias;
- el usuario no tiene permiso;
- la confianza es insuficiente;
- el documento está obsoleto;
- la pregunta está fuera de alcance.
Una respuesta inventada no se considerará éxito.
## 31. Definition of Done para citas

Las citas estarán terminadas cuando:
- identifican fuente;
- identifican fragmento o ubicación;
- corresponden al contenido;
- no apuntan a documentos no autorizados;
- se conservan durante generación;
- pueden validarse;
- se muestran en la interfaz;
- tienen pruebas.
## 32. Definition of Done para memoria

Un sistema de memoria estará terminado cuando:
- diferencia memoria de historial;
- define qué puede almacenarse;
- define fuente;
- registra confianza;
- registra propietario;
- tiene expiración;
- permite corrección;
- permite eliminación;
- respeta privacidad;

- evita contaminación entre usuarios;
- tiene pruebas;
- registra uso.
## 33. Definition of Done para una memoria

persistente
Cada registro deberá incluir:
- tenant;
- usuario;
- tipo;
- contenido;
- fuente;
- confianza;
- estado;
- fecha;
- expiración;
- versión o corrección.
No deberá guardarse automáticamente información sensible sin política explícita.
## 34. Definition of Done para conversación

El módulo estará terminado cuando:
- crea sesiones;
- guarda mensajes;
- conserva orden;
- identifica autor;
- registra modelo;
- registra herramientas;
- registra fuentes;
- permite recuperar historial;
- filtra tenant y usuario;
- maneja conversaciones extensas;
- tiene estrategia de resumen;
- tiene pruebas.

## 35. Definition of Done para un agente

Un agente estará terminado cuando:
- tiene objetivo;
- tiene entradas tipadas;
- tiene estado explícito;
- tiene herramientas limitadas;
- tiene criterio de terminación;
- tiene límite de pasos;
- tiene límite de costo;
- tiene timeout;
- maneja errores;
- puede pausarse cuando aplica;
- registra trazas;
- tiene evaluación;
- tiene pruebas de seguridad.
No estará terminado si
- funciona solamente con un prompt general;
- tiene acceso a todas las herramientas;
- depende exclusivamente del historial;
- puede entrar en ciclos ilimitados;
- no sabe abstenerse;
- no permite investigar sus decisiones operativas.
## 36. Definition of Done para un nodo de LangGraph

Un nodo estará terminado cuando:
- tiene una única responsabilidad;
- define entradas;
- define salidas;
- modifica estado de forma explícita;
- maneja errores;
- puede probarse aisladamente;
- registra trazas;
- no contiene dependencias ocultas;
- respeta idempotencia cuando aplica.

## 37. Definition of Done para un grafo agéntico

Un grafo estará terminado cuando:
- tiene estado definido;
- tiene nodos definidos;
- tiene rutas explícitas;
- tiene condiciones;
- tiene criterios de terminación;
- maneja reanudación;
- persiste checkpoints cuando aplica;
- maneja aprobaciones;
- tiene límite de ciclos;
- tiene pruebas de caminos;
- tiene evaluación;
- tiene visualización o diagrama.
Caminos mínimos a probar
- éxito;
- datos insuficientes;
- error de herramienta;
- aprobación requerida;
- aprobación rechazada;
- límite excedido;
- proveedor no disponible;
- reanudación.
## 38. Definition of Done para un sistema

multiagente
El sistema estará terminado cuando:
- cada agente tiene una especialización real;
- existe contrato entre agentes;
- existe coordinación;
- existe criterio de delegación;
- se evita trabajo duplicado;
- se evitan ciclos;
- existe supervisor o estrategia clara;
- se controlan costos;
- se registran decisiones;
- se comparó contra una solución menos compleja;

demuestra beneficio medible.
No se considerará terminado si usar varios agentes no mejora:
- calidad;
- mantenibilidad;
- especialización;
- resiliencia;
- trazabilidad.
## 39. Definition of Done para MCP

Una implementación MCP estará terminada cuando:
- expone resources o tools con propósito claro;
- implementa autenticación;
- resuelve tenant;
- aplica autorización;
- valida entradas;
- registra auditoría;
- reutiliza casos de uso existentes;
- maneja errores;
- tiene pruebas con un cliente;
- documenta capacidades;
- limita acceso;
- tiene threat model.
## 40. Definition of Done para un MCP Resource

Un resource estará terminado cuando:
- tiene URI o identificación estable;
- devuelve contenido autorizado;
- respeta tenant;
- incluye metadata;
- maneja inexistencia;
- limita tamaño;
- registra acceso;
- tiene pruebas.

## 41. Definition of Done para una MCP Tool

Además de los criterios generales de herramientas:
- cumple el contrato MCP;
- documenta argumentos;
- documenta respuesta;
- aplica autorización;
- clasifica riesgo;
- registra ejecución;
- maneja aprobación;
- tiene pruebas desde cliente MCP.
## 42. Definition of Done para evaluación AI

Una evaluación estará terminada cuando:
- define objetivo;
- tiene dataset versionado;
- tiene baseline;
- tiene métricas;
- tiene criterios de aprobación;
- puede reproducirse;
- registra modelo y configuración;
- produce reporte;
- identifica limitaciones;
- está integrada en CI cuando corresponde.
## 43. Definition of Done para un dataset de

evaluación
El dataset estará terminado cuando:
- tiene esquema;
- tiene versión;
- tiene origen documentado;
- tiene casos positivos;
- tiene casos negativos;
- incluye casos límite;
- incluye ataques o errores cuando aplica;
- evita datos sensibles;

- puede ejecutarse automáticamente;
- tiene revisión humana.
## 44. Definition of Done para LLM-as-Judge

Un evaluador basado en modelo estará terminado cuando:
- tiene rúbrica;
- tiene salida estructurada;
- registra modelo;
- registra versión de prompt;
- tiene ejemplos;
- fue comparado con evaluación humana;
- limita sesgos;
- no evalúa su propia respuesta sin controles;
- tiene estrategia de calibración;
- documenta limitaciones.
## 45. Definition of Done para observabilidad

La observabilidad estará terminada cuando:
- existen logs estructurados;
- existen trazas;
- existen métricas;
- existe correlación;
- se registran errores;
- se registran modelos;
- se registran tokens;
- se registran herramientas;
- se registran costos;
- se pueden consultar ejecuciones;
- se protegen datos sensibles.
## 46. Definition of Done para logging

Un flujo tendrá logging completo cuando:
- registra inicio;
- registra resultado;
- registra error;

- incluye correlation ID;
- incluye tenant cuando corresponde;
- evita secretos;
- evita información personal innecesaria;
- utiliza niveles correctos;
- produce mensajes accionables.
## 47. Definition of Done para tracing

Un flujo tendrá tracing completo cuando:
- existe trace raíz;
- existen spans por etapa;
- se relacionan llamadas externas;
- se relaciona retrieval;
- se relacionan model calls;
- se relacionan tool calls;
- se relacionan workers;
- se registran errores;
- puede reconstruirse el flujo.
## 48. Definition of Done para métricas

Una métrica estará terminada cuando:
- tiene nombre claro;
- tiene definición;
- tiene unidad;
- tiene dimensiones limitadas;
- evita alta cardinalidad;
- tiene propietario;
- tiene uso operativo;
- está documentada.
## 49. Definition of Done para seguridad

Una funcionalidad estará terminada en seguridad cuando:
- autentica;
- autoriza;
- valida tenant;

- valida inputs;
- protege outputs;
- controla herramientas;
- gestiona secretos;
- registra auditoría;
- tiene pruebas negativas;
- revisa riesgos de prompt injection;
- aplica mínimo privilegio;
- no deja vulnerabilidades críticas conocidas.
## 50. Definition of Done para Prompt Injection

Defense
La protección estará terminada cuando:
- diferencia instrucciones y contenido;
- delimita documentos;
- desconfía de contenido recuperado;
- restringe herramientas;
- valida outputs;
- prueba ataques directos;
- prueba ataques indirectos;
- registra intentos;
- niega acciones no autorizadas;
- documenta limitaciones.
No se afirmará que la protección es absoluta.
## 51. Definition of Done para Multi-Tenancy

Un módulo multi-tenant estará terminado cuando:
- todos los recursos tienen tenant;
- el tenant proviene de contexto validado;
- los repositorios filtran;
- los casos de uso validan;
- las tools validan;
- retrieval filtra;
- cache separa claves;
- logs incluyen tenant de forma segura;
- existen pruebas de aislamiento;
- no hay acceso cruzado.

Prueba crítica
Intentar acceder desde un tenant a recursos de otro deberá fallar en:
- API;
- repositorio;
- tool;
- retrieval;
- MCP;
- exportaciones.
## 52. Definition of Done para autenticación

La autenticación estará terminada cuando:
- valida credenciales;
- emite o verifica tokens;
- maneja expiración;
- maneja revocación cuando aplica;
- protege endpoints;
- no filtra información;
- registra eventos;
- tiene pruebas;
- documenta flujo.
## 53. Definition of Done para autorización

La autorización estará terminada cuando:
- tiene roles o políticas;
- se valida en backend;
- considera tenant;
- considera recurso;
- considera acción;
- considera herramienta;
- tiene pruebas positivas y negativas;
- registra accesos denegados;
- no depende únicamente del frontend.

## 54. Definition of Done para Docker

Un servicio estará terminado en Docker cuando:
- tiene Dockerfile;
- construye desde cero;
- usa imagen apropiada;
- utiliza multi-stage cuando aporta valor;
- no corre como root;
- tiene health check;
- no incluye secretos;
- tiene .dockerignore ;
- define puertos;
- define variables;
- tiene imagen reproducible.
## 55. Definition of Done para Docker Compose

El ambiente local estará terminado cuando:
- levanta servicios necesarios;
- configura redes;
- configura volúmenes;
- configura health checks;
- permite reiniciar;
- documenta comandos;
- evita dependencias manuales;
- funciona desde clon limpio.
## 56. Definition of Done para CI

Un pipeline estará terminado cuando:
- se ejecuta en Pull Requests;
- instala desde lockfile;
- ejecuta lint;
- ejecuta type checking;
- ejecuta pruebas;
- ejecuta seguridad;
- construye artifacts;
- falla correctamente;
- no expone secretos;

- conserva reportes útiles;
- tiene tiempo de ejecución razonable.
## 57. Definition of Done para CD

El despliegue estará terminado cuando:
- tiene ambiente objetivo;
- usa configuración separada;
- usa secretos seguros;
- tiene health checks;
- registra versión;
- valida migraciones;
- permite rollback;
- genera historial;
- tiene aprobación cuando corresponde;
- tiene smoke tests.
## 58. Definition of Done para una migración de base

de datos
Una migración estará terminada cuando:
- está versionada;
- fue probada;
- conserva datos;
- considera rollback;
- considera compatibilidad;
- no bloquea innecesariamente;
- tiene backup o mitigación cuando aplica;
- está documentada;
- se ejecutó en staging.
## 59. Definition of Done para un webhook

Un webhook estará terminado cuando:
- valida firma;
- valida timestamp;
- evita replay;

- tiene idempotencia;
- responde rápidamente;
- registra evento;
- procesa de forma asíncrona cuando aplica;
- maneja duplicados;
- maneja orden incorrecto;
- tiene retries;
- tiene dead-letter strategy;
- tiene pruebas.
## 60. Definition of Done para una automatización

n8n
Un workflow estará terminado cuando:
- tiene objetivo;
- tiene trigger;
- tiene entradas;
- tiene salidas;
- maneja errores;
- tiene retries;
- evita duplicados;
- registra ejecución;
- protege credenciales;
- usa subworkflows cuando corresponde;
- no contiene lógica empresarial crítica sin servicio;
- tiene documentación;
- tiene pruebas con datos ficticios.
## 61. Definition of Done para una integración OAuth

La integración estará terminada cuando:
- usa flujo adecuado;
- valida state;
- usa PKCE cuando corresponde;
- almacena tokens de forma segura;
- maneja expiración;
- maneja refresh;
- limita scopes;
- maneja revocación;
- registra errores;

- tiene pruebas;
- documenta permisos solicitados.
## 62. Definition of Done para documentación

Un documento estará terminado cuando:
- tiene propósito;
- tiene título;
- tiene versión o fecha;
- tiene estado;
- es consistente con implementación;
- utiliza términos definidos;
- incluye decisiones;
- incluye limitaciones;
- enlaza documentos relacionados;
- fue revisado.
## 63. Definition of Done para un ADR

Un ADR estará terminado cuando:
- define contexto;
- define problema;
- lista alternativas;
- explica decisión;
- explica consecuencias;
- explica riesgos;
- tiene estado;
- tiene fecha;
- identifica responsables;
- enlaza implementación;
- se agrega al índice.
## 64. Definition of Done para un diagrama

Un diagrama estará terminado cuando:
- tiene objetivo;
- tiene nivel de detalle adecuado;
- tiene nombres claros;

- representa el sistema real;
- indica límites;
- indica actores;
- conserva fuente editable;
- está versionado;
- fue revisado.
## 65. Definition of Done para un Threat Model

El threat model estará terminado cuando:
- identifica activos;
- identifica actores;
- identifica fronteras de confianza;
- identifica entradas;
- identifica datos sensibles;
- identifica herramientas;
- identifica amenazas;
- asigna riesgo;
- propone mitigaciones;
- registra riesgos aceptados;
- se relaciona con pruebas.
## 66. Definition of Done para un Runbook

Un runbook estará terminado cuando:
- identifica el incidente;
- muestra síntomas;
- muestra cómo verificar;
- muestra pasos de recuperación;
- muestra rollback;
- identifica riesgos;
- identifica escalamiento;
- incluye responsables;
- fue probado o simulado.

## 67. Definition of Done para un Milestone

Un milestone estará terminado cuando:
- todos los issues críticos están cerrados;
- se cumplió el objetivo;
- los criterios de salida están satisfechos;
- no existen bloqueadores;
- la integración funciona;
- las pruebas pasan;
- la documentación está actualizada;
- existe demo;
- existe revisión técnica;
- se registraron decisiones;
- se registraron lecciones;
- se actualizó la Skills Matrix.
## 68. Milestone Review

Cada cierre deberá responder:
¿Qué capacidad nueva existe?
¿Qué evidencia la demuestra?
¿Qué decisiones se tomaron?
¿Qué riesgos permanecen?
¿Qué métricas se alcanzaron?
¿Qué falló?
¿Qué aprendimos?
¿Estamos listos para avanzar?
## 69. Definition of Done para una Release interna

Una release interna estará terminada cuando:
- tiene versión;
- tiene tag;
- tiene changelog;
- puede desplegarse;
- tiene migraciones;
- tiene smoke tests;
- tiene documentación;
- tiene limitaciones;
- 1.
2.
3.
4.
5.
6.
7.
8.

- fue validada en staging;
- puede revertirse.
## 70. Definition of Done para una Release pública

Además de la release interna:
- el repositorio está sanitizado;
- el README es profesional;
- existe licencia;
- existe demo;
- existen capturas;
- existe arquitectura;
- existen instrucciones reproducibles;
- existe seguridad documentada;
- existe evaluación AI;
- existe caso de estudio;
- no hay datos reales;
- no hay secretos;
- existe release note pública.
## 71. Definition of Done para un proyecto

Un proyecto estará terminado cuando:
Producto
- resuelve un problema real;
- tiene usuarios definidos;
- tiene casos de uso completos;
- tiene demo funcional;
- tiene limitaciones claras.
Arquitectura
- tiene C4;
- tiene diagramas de secuencia;
- tiene ADRs;
- tiene contratos;
- tiene límites de dominio.

Código
- está estructurado;
- está probado;
- está tipado;
- cumple calidad;
- no contiene dependencias innecesarias.
IA
- modelos documentados;
- prompts versionados;
- evaluaciones;
- herramientas controladas;
- costos medidos;
- fallos considerados.
Seguridad
- autenticación;
- autorización;
- multi-tenancy;
- auditoría;
- threat model;
- pruebas negativas.
Operación
- Docker;
- CI/CD;
- observabilidad;
- runbooks;
- backups;
- rollback.
Portafolio
- README;
- capturas;
- video;
- caso de estudio;
- ficha técnica;
- preguntas de entrevista;
- narrativa profesional.

## 72. Definition of Done para un entregable de

portafolio
Un entregable de portafolio estará terminado cuando:
- explica el problema empresarial;
- explica la solución;
- explica la arquitectura;
- muestra evidencia;
- muestra decisiones;
- muestra resultados;
- muestra limitaciones;
- evita exageraciones;
- puede entenderlo un recruiter;
- puede revisarlo un Staff Engineer;
- puede demostrarse en vivo;
- puede defenderse en entrevista.
## 73. Caso de estudio

El caso de estudio estará terminado cuando incluye:
- contexto;
- problema;
- usuarios;
- restricciones;
- arquitectura;
- tecnologías;
- decisiones;
- implementación;
- seguridad;
- evaluación;
- observabilidad;
- resultados;
- errores;
- lecciones;
- mejoras futuras.
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
12.
13.
14.
15.

## 74. Demo técnica

Una demo estará terminada cuando:
- tiene guion;
- utiliza datos ficticios;
- puede repetirse;
- muestra flujo principal;
- muestra un error;
- muestra observabilidad;
- muestra seguridad o aprobación;
- muestra resultado medible;
- dura un tiempo razonable;
- tiene plan alternativo si falla un proveedor.
## 75. Video de portafolio

Un video estará terminado cuando:
- explica el problema;
- muestra el producto;
- muestra arquitectura;
- muestra una capacidad AI;
- muestra una decisión técnica;
- evita datos privados;
- tiene audio entendible;
- tiene duración adecuada;
- incluye enlace al repositorio.
## 76. Evidencia obligatoria

Todo entregable relevante deberá producir al menos una evidencia.
Código
- Pull Request;
- commit;
- release.

Calidad
- tests;
- cobertura;
- evaluación;
- benchmark.
Arquitectura
- ADR;
- diagrama;
- contrato.
Operación
- trace;
- dashboard;
- log;
- runbook.
Producto
- captura;
- video;
- demo;
- feedback.
## 77. Evidencia insuficiente

No serán suficientes por sí solas:
- afirmaciones;
- código sin ejecución;
- capturas aisladas;
- respuestas favorables;
- tests escritos pero no ejecutados;
- diagramas que no coinciden con el sistema;
- porcentajes sin metodología;
- benchmarks sin baseline.

## 78. Criterios de aceptación medibles

Los criterios deberán evitar expresiones ambiguas.
Incorrecto
El asistente debe responder bien.
Correcto
El asistente deberá responder correctamente al menos 85 de 100 preguntas del
dataset aprobado y citar una fuente válida en al menos 95% de las respuestas que
requieran documentación.
## 79. Excepciones a Definition of Done

Una excepción podrá aceptarse cuando:
- existe urgencia real;
- el riesgo es conocido;
- el alcance está limitado;
- hay aprobación;
- existe plan de corrección;
- existe issue;
- tiene fecha o condición de revisión.
Una excepción deberá registrar
- criterio incumplido;
- motivo;
- riesgo;
- mitigación;
- responsable;
- fecha límite.

## 80. Prohibición de excepciones implícitas

No se aceptará como excepción:
- “después lo vemos”;
- “solo es temporal”;
- “funciona en mi máquina”;
- “el modelo casi siempre responde bien”;
- “nadie va a probar eso”;
- “es solamente para la demo”.
Toda excepción deberá ser explícita.
## 81. Riesgos bloqueantes

Un entregable no podrá marcarse como Done si existe:
- vulnerabilidad crítica;
- fuga entre tenants;
- secreto expuesto;
- pérdida de datos;
- tool de alto riesgo sin aprobación;
- respuesta no sustentada en un flujo crítico;
- migración insegura;
- imposibilidad de rollback;
- dependencia no licenciada;
- falta de pruebas del flujo principal.
## 82. Riesgos no bloqueantes

Podrán registrarse como deuda:
- optimizaciones menores;
- mejoras visuales;
- cobertura adicional no crítica;
- refactor sin impacto inmediato;
- soporte a casos fuera de alcance;
- mejora de rendimiento dentro del presupuesto.

## 83. Responsabilidad de aprobación

Lead Engineer
Valida:
- implementación;
- pruebas;
- documentación;
- evidencia.
Director de AI Engineering
Valida:
- arquitectura;
- calidad AI;
- seguridad;
- cierre de milestone;
- Production Readiness;
- Portfolio Readiness.
Product Owner o usuario de negocio
Cuando aplique, valida:
- valor;
- flujo;
- lenguaje;
- utilidad;
- criterios funcionales.
## 84. Revisión técnica

Toda revisión deberá responder:
- ¿el problema quedó resuelto?;
- ¿el diseño es claro?;
- ¿hay una solución más simple?;
- ¿se respetan límites?;
- ¿se puede probar?;
- ¿se puede observar?;
- ¿se puede operar?;

- ¿es seguro?;
- ¿se puede explicar?;
¿la evidencia es suficiente?
## 85. Definition of Done y velocidad

La Definition of Done no deberá utilizarse para paralizar el proyecto.
Para mantener velocidad:
- se limitará alcance;
- se crearán vertical slices;
- se entregarán versiones;
- se separará lo esencial de lo futuro;
- se automatizarán verificaciones;
- se reutilizarán plantillas.
La velocidad se logrará reduciendo alcance, no eliminando calidad crítica.
## 86. Vertical Slice Done

Una entrega vertical estará terminada cuando atraviesa:
Interface
│
▼
API
│
▼
Application
│
▼
Domain
│
▼
Infrastructure or AI Provider
│
▼
Persistence
│

▼
Observability
Y además:
- tiene prueba;
- tiene documentación;
- tiene manejo de error;
- tiene resultado visible.
## 87. MVP Done

Un MVP profesional estará terminado cuando:
- resuelve un flujo principal;
- puede utilizarse;
- puede desplegarse;
- tiene seguridad básica;
- tiene evaluación;
- tiene observabilidad;
- tiene documentación;
- tiene limitaciones claras.
MVP no significará:
- frágil;
- inseguro;
- no probado;
- imposible de mantener.
## 88. Gate de Functional Completion

Se aprobará cuando:
- el caso de uso funciona;
- cumple aceptación;
- maneja errores principales;
- está integrado;
- tiene pruebas.

## 89. Gate de AI Quality

Se aprobará cuando:
- existe dataset;
- existe baseline;
- se cumplen métricas;
- los outputs están validados;
- las regresiones están controladas;
- los fallos están identificados.
## 90. Gate de Security

Se aprobará cuando:
- se revisaron amenazas;
- se probaron permisos;
- se probó aislamiento;
- se protegieron herramientas;
- se protegieron secretos;
- no hay riesgo crítico abierto.
## 91. Gate de Operational Readiness

Se aprobará cuando:
- puede desplegarse;
- puede observarse;
- puede recuperarse;
- puede revertirse;
- tiene runbooks;
- tiene métricas;
- tiene alertas mínimas.
## 92. Gate de Portfolio Readiness

Se aprobará cuando:
- existe narrativa;
- existe demo;

- existe README;
- existen diagramas;
- existe caso de estudio;
- existen resultados;
- existen respuestas para entrevista;
- la información puede publicarse.
## 93. Checklist general de Done

[ ] Problema resuelto
[ ] Criterios de aceptación cumplidos
[ ] Código integrado
[ ] Pruebas aprobadas
[ ] Errores manejados
[ ] Seguridad validada
[ ] Tenant validado
[ ] Observabilidad incluida
[ ] Evaluación AI actualizada
[ ] Documentación actualizada
[ ] CI en verde
[ ] Evidencia disponible
[ ] Riesgos registrados
[ ] Revisión completada
## 94. Checklist de AI Done

[ ] Modelo registrado
[ ] Prompt versionado
[ ] Output validado
[ ] Dataset disponible
[ ] Baseline definido
[ ] Métricas calculadas
[ ] Fallos documentados
[ ] Costos medidos
[ ] Latencia medida
[ ] Tools controladas
[ ] Trazas disponibles
[ ] Rollback posible

## 95. Checklist de Production Done

[ ] Despliegue reproducible
[ ] Configuración por ambiente
[ ] Secretos protegidos
[ ] Health checks
[ ] Migraciones probadas
[ ] Logs
[ ] Traces
[ ] Metrics
[ ] Alertas
[ ] Runbooks
[ ] Backups
[ ] Rollback
[ ] Smoke tests
## 96. Checklist de Portfolio Done

[ ] README profesional
[ ] Problema explicado
[ ] Arquitectura publicada
[ ] Capturas
[ ] Demo
[ ] Video
[ ] Caso de estudio
[ ] Métricas
[ ] Decisiones técnicas
[ ] Limitaciones
[ ] Repositorio sanitizado
[ ] Release pública
[ ] Material de entrevista
## 97. Definition of Done de AI Engineering Lab

El laboratorio completo estará terminado cuando:
- los tres proyectos estén finalizados;
- los tres proyectos tengan releases públicas o demostrables;
- el playbook esté consolidado;

- el portafolio esté publicado;
- la Skills Matrix esté actualizada;
- exista narrativa profesional;
- el CV esté actualizado;
- LinkedIn esté actualizado;
- existan demos;
- exista preparación de entrevistas;
- el perfil pueda defender experiencia real en AI Engineering.
## 98. Decisiones oficiales

Quedan aprobadas las siguientes reglas:
Una capacidad no se considera terminada únicamente porque funciona.
Todo entregable relevante debe producir evidencia.
Los flujos AI requieren evaluación además de pruebas tradicionales.
Los prompts requieren versión, métricas y rollback.
Las tools requieren permisos, riesgo, auditoría e idempotencia.
Los pipelines RAG requieren ingestión, retrieval, citas y evaluación.
Los agentes requieren estado, límites y criterios de terminación.
Los sistemas multiagente deberán justificar su complejidad.
Todo flujo empresarial deberá respetar multi-tenancy.
No puede existir Production Readiness sin seguridad y observabilidad.
No puede existir Portfolio Readiness sin narrativa y evidencia.
Las excepciones deberán documentarse explícitamente.
Los riesgos críticos bloquean el cierre.
Los milestones se cerrarán por evidencia, no por fecha.
La velocidad se conseguirá reduciendo alcance, no omitiendo controles esenciales.
## 99. Próximo documento

Documento 06 — Evaluation Strategy
Definirá:
- filosofía de evaluación;
- tipos de evaluación;
- datasets;
- golden sets;
- métricas RAG;
- métricas de tools;
- métricas de agentes;
- evaluación humana;
- 1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
12.
13.
14.
15.

- LLM-as-judge;
- regression testing;
- evaluación offline;
- evaluación online;
- quality gates;
- reportes;
- integración con CI/CD.
## 100. Conclusión

La Definition of Done convierte el avance del laboratorio en evidencia verificable.
A partir de este documento no se considerará completa una funcionalidad solamente porque:
- responde;
- ejecuta;
- compila;
- se ve bien;
- funciona en una demostración.
Cada entrega deberá demostrar:
- valor;
- corrección;
- seguridad;
- confiabilidad;
- evaluación;
- observabilidad;
- reproducibilidad;
- capacidad de operación.
El laboratorio no buscará producir mucho código.
Buscará producir sistemas completos y defendibles.
