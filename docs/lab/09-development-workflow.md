# AI Engineering Lab

## Documento 09 — Development Workflow

**Versión:** 1.0
**Estado:** Proceso oficial
**Responsable técnico:** Director de AI Engineering
**Lead Engineer:** Erick Eduardo Evangelista Velasco
## 1. Propósito

Este documento define el flujo oficial de desarrollo para todos los proyectos del AI Engineering Lab.
Su objetivo es establecer un proceso único, repetible y verificable desde que surge una idea hasta que una
capacidad:
- se diseña;
- se implementa;
- se prueba;
- se evalúa;
- se protege;
- se integra;
- se despliega;
- se documenta;
- se convierte en evidencia de portafolio.
Este proceso deberá impedir:
- iniciar trabajo sin definición;
- construir soluciones sin problema real;
- adoptar tecnología sin evaluación;
- mezclar múltiples objetivos;
- dejar funcionalidades parcialmente terminadas;
- publicar código sin calidad;
- declarar éxito sin evidencia.
## 2. Principio rector

El trabajo no avanza por cantidad de código producido, sino por capacidades completas que
atraviesan todos los controles de ingeniería.

Cada capacidad deberá recorrer un flujo definido.
No se permitirá saltar directamente de una idea a implementación sin pasar por análisis, alcance y criterios
de aceptación.
## 3. Flujo general

Opportunity
│
▼
Intake
│
▼
Analysis
│
▼
Definition of Ready
│
▼
Design
│
▼
Planning
│
▼
Implementation
│
▼
Testing
│
▼
Evaluation
│
▼
Security Review
│
▼
Pull Request
│
▼
Integration
│
▼
Deployment

│
▼
Validation
│
▼
Documentation
│
▼
Portfolio Evidence
│
▼
Review and Learning
## 4. Tipos de trabajo

Todo trabajo deberá clasificarse antes de comenzar.
Feature
Nueva capacidad funcional.
Bug
Corrección de comportamiento incorrecto.
Architecture
Cambio estructural o decisión técnica.
Security
Control, corrección o investigación de seguridad.
Evaluation
Dataset, métrica, evaluador o regresión.
Technical Debt
Mejora interna sin cambio funcional principal.

Research Spike
Investigación limitada para tomar una decisión.
Documentation
Creación o actualización documental.
Operations
Despliegue, observabilidad, infraestructura o soporte operativo.
Portfolio
Material público, caso de estudio, demo o narrativa profesional.
## 5. Fuentes de trabajo

El trabajo podrá originarse en:
- roadmap;
- necesidad de usuario;
- problema empresarial;
- incidente;
- feedback;
- evaluación fallida;
- riesgo;
- deuda técnica;
- observabilidad;
- investigación;
- oportunidad de portafolio.
Toda fuente deberá convertirse en un issue antes de implementación relevante.
## 6. Intake

El intake es la entrada formal de una necesidad al sistema de trabajo.
Deberá capturar:
- problema;
- solicitante;

- usuario afectado;
- contexto;
- impacto;
- urgencia;
- evidencia;
- resultado esperado.
Ejemplo
Problema:
Los responsables de soporte tardan demasiado en encontrar
procedimientos dentro de múltiples manuales.
Usuario:
Personal de soporte de Grupo GEEM.
Impacto:
Mayor tiempo de respuesta y dependencia de personas específicas.
Resultado esperado:
Consultar procedimientos mediante lenguaje natural con citas verificables.
## 7. Rechazo temprano

Una solicitud podrá rechazarse o devolverse a backlog cuando:
- no resuelve un problema real;
- duplica una capacidad existente;
- contradice la estrategia;
- requiere acceso inseguro;
- no tiene usuario definido;
- no aporta valor suficiente;
- introduce complejidad desproporcionada;
- está fuera del roadmap actual.
Rechazar trabajo débil protege el enfoque del laboratorio.
## 8. Análisis del problema

Antes de diseñar se deberá analizar:
¿Quién tiene el problema?
1.

¿Qué ocurre actualmente?
¿Cuál es el impacto?
¿Qué resultado necesita?
¿Cómo se resuelve hoy?
¿Por qué la solución actual es insuficiente?
¿Se requiere realmente IA?
¿Qué riesgos existen?
¿Cómo se medirá el éxito?
## 9. AI Necessity Check

Toda feature AI deberá justificar el uso de inteligencia artificial.
Se deberá preguntar:
¿El problema es probabilístico?
¿Requiere lenguaje natural?
¿Requiere síntesis?
¿Requiere clasificación flexible?
¿Requiere recuperación semántica?
¿Existen reglas deterministas suficientes?
¿Una búsqueda tradicional resolvería el problema?
Regla
La IA no se utilizará cuando una solución determinista sea:
- más segura;
- más barata;
- más rápida;
- más fácil de mantener;
- igualmente efectiva.
## 10. Value Hypothesis

Toda feature importante deberá definir una hipótesis de valor.
Formato:
Creemos que [capacidad]
para [usuario]
2.
3.
4.
5.
6.
7.
8.
9.

producirá [resultado]
y lo comprobaremos mediante [métrica].
Ejemplo:
Creemos que un asistente RAG para soporte
reducirá el tiempo necesario para localizar procedimientos
y lo comprobaremos midiendo tiempo promedio de respuesta
y porcentaje de consultas resueltas sin escalamiento.
## 11. Alcance

Cada issue deberá definir:
In Scope
Lo que será entregado.
Out of Scope
Lo que no será entregado.
Future Considerations
Posibles extensiones posteriores.
Esto evitará que una tarea crezca durante la implementación.
## 12. Criterios de aceptación

Los criterios deberán ser:
- claros;
- verificables;
- medibles;
- relacionados con el problema;
- independientes de detalles innecesarios.

Ejemplo
[ ] El usuario puede cargar un documento PDF válido.
[ ] El documento queda disponible para búsqueda después del procesamiento.
[ ] Los resultados respetan tenant y permisos.
[ ] Los errores de extracción pueden reintentarse.
[ ] El procesamiento genera trazas y métricas.
## 13. Definition of Ready

Un issue estará Ready cuando:
- el problema es claro;
- existe usuario;
- existe resultado esperado;
- tiene alcance;
- tiene criterios de aceptación;
- tiene prioridad;
- tiene dependencias identificadas;
- tiene riesgos;
- tiene evidencia esperada;
- puede implementarse sin decisiones fundamentales pendientes.
## 14. Trabajo no listo

Un issue no deberá pasar a implementación si:
- depende de preguntas críticas sin respuesta;
- no tiene alcance;
- mezcla múltiples capacidades;
- no tiene criterio de éxito;
- requiere arquitectura no decidida;
- requiere acceso no autorizado;
- no tiene datos o ambiente necesarios.
Permanecerá en:
Backlog
o:

Blocked
## 15. Refinement

El refinement deberá:
- aclarar alcance;
- dividir trabajo;
- identificar riesgos;
- validar dependencias;
- estimar complejidad;
- confirmar criterios;
- determinar si requiere ADR;
- identificar pruebas y evaluaciones.
## 16. Tamaño de trabajo

Una tarea deberá ser suficientemente pequeña para:
- comprenderse;
- implementarse en una rama;
- revisarse en un PR;
- probarse;
- generar evidencia.
Señales de que es demasiado grande
- involucra varios módulos;
- requiere múltiples decisiones arquitectónicas;
- contiene varios flujos de usuario;
- necesita semanas sin integración;
- no puede explicarse en un PR.
## 17. División vertical

Las features deberán dividirse preferentemente por valor vertical.

Correcto
Upload de documento PDF
├── Endpoint
├── Caso de uso
├── Persistencia
├── Job
├── Estado visible
└── Observabilidad
Evitar
Crear todos los modelos
Crear todos los repositorios
Crear todos los servicios
Crear todos los endpoints
La división por capas puede producir mucho código sin capacidad ejecutable.
## 18. Investigación previa

Se creará un Research Spike cuando exista incertidumbre material.
Ejemplos:
- elegir vector database;
- comparar modelos;
- evaluar estrategia de chunking;
- comparar sistemas de colas;
- validar una integración.
El spike deberá ser:
- limitado;
- medible;
- documentado;
- orientado a decisión.

## 19. Salida de un Spike

Todo spike deberá producir:
- pregunta;
- alternativas;
- experimento;
- resultados;
- métricas;
- riesgos;
- recomendación;
- decisión o siguiente paso.
Un spike no se considerará terminado solo por haber creado código experimental.
## 20. Diseño técnico

Antes de implementar una feature relevante se deberá definir:
- módulos involucrados;
- flujo;
- contratos;
- datos;
- permisos;
- errores;
- observabilidad;
- evaluación;
- despliegue;
- rollback.
La profundidad del diseño será proporcional al riesgo.
## 21. Design Note

Las features medianas podrán usar una nota técnica breve.
Contenido:
Problem
Proposed Solution
Affected Modules
Contracts

Data Changes
Security
Evaluation
Observability
Risks
## 22. ADR obligatorio

Se requerirá ADR cuando la decisión:
- cambie arquitectura;
- agregue tecnología significativa;
- afecte varios módulos;
- sea difícil de revertir;
- modifique seguridad;
- cree dependencia externa importante;
- cambie estrategia de datos;
- introduzca agentes o workflows complejos.
## 23. Diagramas requeridos

Se utilizarán diagramas cuando ayuden a explicar:
- nuevos flujos;
- integraciones;
- agentes;
- trust boundaries;
- eventos;
- estados;
- despliegue.
Tipos recomendados:
- C4;
- secuencia;
- flujo;
- estados;
- datos.

## 24. Revisión de diseño

Antes de implementación de alto riesgo se revisará:
- simplicidad;
- alineación arquitectónica;
- límites;
- seguridad;
- multi-tenancy;
- costos;
- operación;
- reversibilidad;
- alternativas.
## 25. Plan de implementación

La implementación deberá dividirse en pasos ordenados.
Ejemplo:
1. Definir contratos.
2. Crear migración.
3. Implementar dominio.
4. Implementar caso de uso.
5. Crear adaptador.
6. Exponer endpoint.
7. Agregar pruebas.
8. Agregar telemetría.
9. Actualizar documentación.
10. Ejecutar evaluación.
## 26. Orden de dependencias

El trabajo deberá comenzar por los contratos y reglas internas.
Orden recomendado:
Contracts
│

▼
Domain
│
▼
Application
│
▼
Infrastructure
│
▼
Presentation
En vertical slices pequeños podrá avanzarse iterativamente entre capas.
## 27. Creación de rama

Una vez Ready, se creará una rama.
Formato:
type/short-description
Ejemplo:
feature/document-upload
La rama deberá corresponder a un issue concreto.
## 28. Inicio de trabajo

Al mover un issue a In Progress se deberá:
- asignar responsable;
- crear rama;
- registrar dependencias;
- confirmar criterios;
- actualizar tablero.
Solo deberá existir una tarea principal de implementación activa por responsable, salvo necesidad
justificada.

## 29. Work in Progress Limit

Para el trabajo individual inicial:
- una feature principal;
- una tarea secundaria de documentación o investigación;
- un bug crítico adicional solo si bloquea el trabajo.
No se iniciará una nueva feature principal antes de integrar o pausar formalmente la actual.
## 30. Desarrollo incremental

La implementación deberá realizarse en incrementos verificables.
Cada incremento deberá:
- compilar;
- mantener pruebas;
- evitar romper la rama;
- producir commits comprensibles;
- acercarse a una capacidad completa.
## 31. Test-First cuando aporte valor

Se escribirán pruebas antes del código cuando:
- exista regla de dominio;
- exista contrato;
- se corrija un bug;
- se implemente seguridad;
- se implementen transformaciones;
- exista output estructurado.
No se impondrá TDD mecánico para cada línea.
## 32. Bug Workflow

Todo bug deberá seguir:

Reproduction
│
▼
Failing Test
│
▼
Root Cause
│
▼
Minimal Fix
│
▼
Regression Test
│
▼
Validation
No se corregirá un bug sin comprender su causa cuando sea materialmente posible.
## 33. Implementación de AI

Toda capacidad AI deberá incluir desde el inicio:
- baseline;
- dataset;
- prompt versionado;
- output estructurado;
- telemetría;
- costo;
- límites;
- fallbacks;
- evaluación.
No se dejarán estos elementos para el final.
## 34. Prompt Workflow

El flujo para modificar un prompt será:
Problem Case
│

▼
Dataset Update
│
▼
Prompt Candidate
│
▼
Offline Evaluation
│
▼
Comparison
│
▼
Approval
│
▼
Version Update
│
▼
Deployment
## 35. Model Change Workflow

Un cambio de modelo deberá incluir:
- motivo;
- modelo actual;
- candidato;
- dataset;
- calidad;
- costo;
- latencia;
- seguridad;
- compatibilidad;
- fallback.
No se cambiará un modelo solamente porque apareció una versión más nueva.

## 36. RAG Change Workflow

Cambios en:
- chunking;
- embeddings;
- retrieval;
- top K;
- filtros;
- reranking;
- context assembly;
- deberán medirse por componente y de extremo a extremo.
## 37. Tool Development Workflow

Una nueva tool deberá seguir:
Business Action
│
▼
Risk Classification
│
▼
Permission Definition
│
▼
Contract
│
▼
Implementation
│
▼
Approval Policy
│
▼
Audit
│
▼
Tests
│

▼
Evaluation
## 38. Agent Development Workflow

Un agente deberá construirse progresivamente.
Fase 1
Workflow determinista.
Fase 2
Modelo en decisiones concretas.
Fase 3
Tool calling controlado.
Fase 4
Estado y recuperación.
Fase 5
Evaluación completa.
No se comenzará con autonomía amplia.
## 39. Guardrails durante desarrollo

Cada flujo deberá considerar:
- límites de tokens;
- límites de costo;
- límites de tiempo;
- límites de tools;
- límites de pasos;
- validación;
- permisos;

- aprobación;
- terminación.
## 40. Commits

Los commits deberán ser:
- atómicos;
- claros;
- relacionados con el issue;
- libres de secretos;
- técnicamente coherentes.
Se utilizará Conventional Commits.
## 41. Verificación local

Antes de abrir un PR se deberá ejecutar:
format
lint
typecheck
unit tests
integration tests
security checks
evaluation smoke set
build
Cuando aplique también:
docker build
migration test
frontend tests
end-to-end tests
## 42. Self-Review

El autor deberá revisar el diff completo.

Preguntas:
¿Hay archivos accidentales?
¿Hay datos sensibles?
¿El cambio cumple el alcance?
¿Existen soluciones temporales?
¿Faltan pruebas?
¿Falta observabilidad?
¿Falta documentación?
¿Se agregó complejidad innecesaria?
## 43. Pull Request

El PR deberá incluir:
- problema;
- solución;
- cambios;
- pruebas;
- evaluación;
- seguridad;
- observabilidad;
- evidencia;
- riesgos;
- issue relacionado.
## 44. Draft Pull Request

Podrá abrirse como Draft cuando:
- se necesite feedback temprano;
- exista una decisión en revisión;
- el cambio sea extenso;
- se quiera validar dirección.
Un Draft PR no significa que el trabajo esté terminado.

## 45. Revisión automatizada

El CI deberá validar:
- formato;
- lint;
- tipos;
- pruebas;
- build;
- dependencias;
- secretos;
- vulnerabilidades;
- evaluación mínima.
## 46. Revisión humana

La revisión deberá evaluar:
Funcionalidad
¿Resuelve el problema?
Diseño
¿Respeta arquitectura?
Calidad
¿Es mantenible?
Seguridad
¿Protege datos y permisos?
AI
¿Tiene evaluación y límites?
Operación
¿Puede observarse y recuperarse?

## 47. Comentarios de revisión

Los comentarios deberán clasificarse cuando sea útil.
Blocking
Debe corregirse antes de integrar.
Important
Requiere atención o justificación.
Suggestion
Mejora opcional.
Question
Busca comprender una decisión.
## 48. Respuesta a revisión

Cada comentario deberá:
- resolverse;
- contestarse;
- justificarse;
- convertirse en issue si queda fuera de alcance.
No deberá marcarse como resuelto sin atenderlo.
## 49. Cambios durante revisión

Si el PR cambia significativamente:
- se volverán a ejecutar pruebas;
- se actualizará evidencia;
- se solicitará nueva revisión cuando aplique;
- se revisarán nuevamente seguridad y evaluación.

## 50. Gate funcional

Se aprobará cuando:
- cumple criterios;
- el flujo funciona;
- los errores se manejan;
- la integración es correcta;
- las pruebas pasan.
## 51. Gate de arquitectura

Se aprobará cuando:
- respeta módulos;
- respeta contratos;
- no introduce dependencias indebidas;
- las decisiones están documentadas;
- la complejidad está justificada.
## 52. Gate de AI Quality

Se aprobará cuando:
- existe baseline;
- existe dataset;
- pasan métricas;
- no hay regresión crítica;
- se registran costo y latencia;
- los outputs se validan.
## 53. Gate de seguridad

Se aprobará cuando:
- inputs y outputs están validados;
- permisos funcionan;
- tenant está aislado;
- tools están controladas;
- secretos están protegidos;

pasan pruebas negativas.
## 54. Gate de observabilidad

Se aprobará cuando:
- existen logs;
- existe trace;
- existen métricas;
- los errores son diagnosticables;
- los datos sensibles se redactan;
- se puede relacionar la ejecución.
## 55. Definition of Merge

Un PR podrá integrarse cuando:
- todos los gates pasan;
- el CI está en verde;
- los comentarios están resueltos;
- la documentación está actualizada;
- no existen riesgos críticos;
- el PR está aprobado;
- la rama está actualizada cuando sea necesario.
## 56. Estrategia de merge

La estrategia inicial será:
Squash and Merge
El mensaje final deberá representar claramente el cambio.

## 57. Después del merge

Después de integrar se deberá:
- cerrar issue;
- actualizar tablero;
- verificar main ;
- ejecutar CI;
- desplegar a staging cuando corresponda;
- eliminar rama;
- actualizar changelog si aplica.
## 58. Despliegue a staging

Toda feature relevante deberá validarse en staging.
Staging deberá permitir:
- datos ficticios;
- integraciones seguras;
- evaluación;
- smoke tests;
- pruebas manuales;
- observabilidad.
## 59. Migraciones

Antes del despliegue se deberá validar:
- orden;
- compatibilidad;
- tiempo;
- datos;
- rollback;
- backups;
- ejecución en staging.
## 60. Feature Flags

Las features riesgosas podrán desplegarse desactivadas.

Los feature flags se usarán para:
- activación progresiva;
- pruebas;
- rollback funcional;
- tenants piloto;
- comparación.
No deberán convertirse en configuración permanente abandonada.
## 61. Smoke Tests

Después de desplegar se ejecutarán:
- health checks;
- autenticación;
- flujo principal;
- persistencia;
- observabilidad;
- permisos;
- integración crítica.
## 62. Validación funcional

La validación deberá utilizar los criterios de aceptación originales.
No se aceptará una validación distinta para justificar el resultado obtenido.
## 63. Validación AI

Se deberá ejecutar:
- smoke evaluation;
- casos críticos;
- seguridad;
- costo;
- latencia;
- output validation.
Para releases se ejecutará la suite completa.

## 64. Validación operativa

Se verificará:
- logs;
- traces;
- métricas;
- dashboards;
- alertas;
- jobs;
- colas;
- health checks;
- rollback.
## 65. Validación de negocio

Cuando aplique, un usuario de negocio deberá confirmar:
- utilidad;
- lenguaje;
- flujo;
- resultado;
- restricciones.
La validación técnica no sustituye completamente la aceptación del usuario.
## 66. Release Decision

Una release deberá responder:
¿Qué capacidad contiene?
¿Qué riesgos permanecen?
¿Qué métricas alcanza?
¿Puede revertirse?
¿Está documentada?
¿Está lista para usuarios?
¿Está lista para portafolio?
1.
2.
3.
4.
5.
6.
7.

## 67. Release Checklist

[ ] Version assigned
[ ] Changelog updated
[ ] Full tests passed
[ ] Full evaluation passed
[ ] Security gates passed
[ ] Migration validated
[ ] Rollback available
[ ] Documentation updated
[ ] Demo validated
[ ] Release notes prepared
## 68. Despliegue a producción

El flujo será:
Approved Release
│
▼
Deployment
│
▼
Health Validation
│
▼
Smoke Tests
│
▼
Metrics Review
│
▼
Release Confirmed
## 69. Canary o piloto

Las capacidades AI de mayor riesgo podrán liberarse primero a:
- usuarios internos;

- tenant demo;
- tenant piloto;
- porcentaje reducido;
- modo shadow.
## 70. Monitoreo posterior

Después de una release se observarán:
- errores;
- latencia;
- costo;
- feedback;
- calidad;
- tools;
- seguridad;
- uso.
El periodo de observación dependerá del riesgo.
## 71. Rollback

Se realizará rollback cuando:
- exista riesgo de seguridad;
- se rompa funcionalidad crítica;
- aumenten errores significativamente;
- exista regresión AI crítica;
- el costo sea incontrolable;
- se afecten datos;
- no pueda mitigarse rápidamente.
## 72. Cierre de issue

El issue se cerrará cuando:
- la capacidad está integrada;
- la validación terminó;
- existe evidencia;
- la documentación está actualizada;
- no quedan criterios pendientes;

los riesgos están registrados.
## 73. Evidencia de cierre

Se deberá enlazar:
- PR;
- release;
- pruebas;
- evaluación;
- capturas;
- traces;
- dashboard;
- documentación.
## 74. Actualización documental

Cada feature deberá evaluar cambios necesarios en:
- README;
- arquitectura;
- ADR;
- API;
- seguridad;
- evaluación;
- runbooks;
- changelog;
- manuales.
## 75. Actualización del portafolio

Una capacidad relevante deberá producir progresivamente:
- captura;
- diagrama;
- decisión;
- métrica;
- historia técnica;
- evidencia visual;
- explicación de negocio.

No se esperará hasta el final del proyecto para reconstruir el caso de estudio.
## 76. Portfolio Evidence Pipeline

Engineering Work
│
▼
Evidence Capture
│
▼
Technical Narrative
│
▼
Case Study
│
▼
Portfolio Asset
│
▼
Interview Story
## 77. Registro de aprendizajes

Al cerrar una capacidad importante se documentará:
- qué se esperaba;
- qué ocurrió;
- qué falló;
- qué se aprendió;
- qué se cambiaría;
- qué habilidad se desarrolló.
## 78. Actualización de Skills Matrix

La matriz deberá actualizarse al cerrar milestones.
Se registrará evidencia de:
- conocimiento;

- implementación;
- operación;
- dominio defendible.
## 79. Retrospectiva

Cada milestone deberá tener retrospectiva.
Preguntas:
¿Qué funcionó?
¿Qué retrasó?
¿Qué fue innecesario?
¿Qué riesgo no vimos?
¿Qué automatizaremos?
¿Qué estándar debe ajustarse?
¿Qué no volveremos a hacer?
## 80. Acciones de retrospectiva

Cada acción deberá:
- tener responsable;
- tener prioridad;
- convertirse en issue;
- tener criterio de cierre.
Una retrospectiva sin acciones no produce mejora.
## 81. Incidentes

Cuando ocurra un incidente:
Detect
│
▼
Contain
│
▼
Recover

│
▼
Investigate
│
▼
Postmortem
│
▼
Regression Case
El trabajo normal podrá pausarse según severidad.
## 82. Producción de casos de regresión

Todo bug o incidente importante deberá producir:
- test;
- evaluación;
- alerta;
- control;
- documentación;
- según corresponda.
## 83. Trabajo urgente

Una urgencia podrá utilizar un flujo abreviado.
Sin embargo, seguirá requiriendo:
- issue;
- revisión de riesgo;
- prueba mínima;
- PR;
- observabilidad;
- seguimiento.
Los controles omitidos deberán registrarse como excepción temporal.

## 84. Hotfix Workflow

Incident
│
▼
Hotfix Branch
│
▼
Regression Test
│
▼
Minimal Change
│
▼
Fast Review
│
▼
Deploy
│
▼
Validate
│
▼
Postmortem
## 85. Gestión de bloqueos

Un issue se marcará Blocked cuando dependa de:
- decisión;
- proveedor;
- credencial;
- datos;
- ambiente;
- persona;
- integración;
- incidente.
Deberá registrarse:
- causa;
- responsable;
- siguiente acción.

## 86. Pausar trabajo

Una tarea podrá pausarse únicamente de forma explícita.
Antes de pausarla se deberá:
- guardar estado;
- documentar avance;
- registrar pendientes;
- mantener rama;
- actualizar issue;
- explicar condición de reanudación.
Esto evitará trabajo abandonado sin contexto.
## 87. Cancelación de trabajo

Una feature podrá cancelarse cuando:
- perdió valor;
- fue sustituida;
- no es viable;
- el riesgo es excesivo;
- contradice estrategia;
- no justifica costo.
La cancelación deberá documentar la razón y aprendizaje.
## 88. Política de un solo camino

El laboratorio mantendrá una ruta principal.
No se abrirán proyectos paralelos que compitan por atención sin decisión formal.
El orden oficial será:
Foundation
│
▼
GEEM AI Assistant

│
▼
Restaurant AI Operations
│
▼
Enterprise Automation Platform
│
▼
Portfolio Consolidation
## 89. Excepciones al roadmap

Solo se aceptará trabajo fuera de secuencia cuando:
- desbloquee la ruta principal;
- resuelva una urgencia empresarial;
- produzca aprendizaje necesario;
- tenga alcance corto;
- no abandone el trabajo actual.
## 90. Control de ideas nuevas

Las ideas nuevas deberán ir al backlog.
No deberán interrumpir automáticamente el trabajo activo.
Cada idea podrá:
- priorizarse;
- aplazarse;
- descartarse;
- convertirse en spike.
## 91. Weekly Engineering Review

Se realizará una revisión periódica con:
- avance;
- bloqueos;
- métricas;

- riesgos;
- decisiones;
- deuda;
- siguiente entrega.
Pregunta central
¿Cuál es la siguiente capacidad completa que debemos terminar?
## 92. Daily Execution Rule

Al iniciar una sesión de trabajo se deberá identificar:
- issue actual;
- criterio pendiente;
- siguiente cambio verificable;
- evidencia esperada.
Al finalizar:
- actualizar issue;
- ejecutar pruebas relevantes;
- registrar bloqueo;
- dejar siguiente paso explícito.
## 93. Status Communication

Los avances deberán comunicarse en términos de resultado.
Evitar
Trabajé en la API.
Preferir
El endpoint de carga de documentos ya valida tenant,
almacena metadata y genera el job de procesamiento.
Falta validar extracción y agregar pruebas de fallo.
1.
2.
3.
4.
1.
2.
3.
4.

## 94. Métricas del proceso

Se medirán progresivamente:
- cycle time;
- lead time;
- issues completados;
- PR size;
- review time;
- defect rate;
- reopen rate;
- deployment frequency;
- change failure rate;
- recovery time;
- evaluation regressions.
## 95. Cycle Time

Tiempo desde In Progress hasta Done .
Un ciclo excesivo puede indicar:
- alcance grande;
- bloqueos;
- arquitectura poco clara;
- falta de pruebas;
- demasiadas tareas paralelas.
## 96. Lead Time

Tiempo desde el registro de una necesidad hasta su entrega.
Ayudará a detectar acumulación de backlog y refinamiento insuficiente.
## 97. Change Failure Rate

Porcentaje de cambios que generan:
- rollback;
- incidente;

- hotfix;
- regresión;
- error crítico.
## 98. Mean Time to Recovery

Tiempo necesario para restaurar una capacidad después de un fallo.
## 99. Calidad del flujo

No se buscará maximizar velocidad aislada.
Se buscará optimizar:
Value
Quality
Learning
Flow
## 100. Workflow mínimo para tareas pequeñas

Una tarea pequeña deberá seguir:
Issue
│
▼
Ready
│
▼
Branch
│
▼
Implementation
│
▼
Tests
│
▼

PR
│
▼
Merge
│
▼
Validation
## 101. Workflow completo para features AI

Problem
│
▼
Value Hypothesis
│
▼
Dataset
│
▼
Baseline
│
▼
Design
│
▼
Implementation
│
▼
Testing
│
▼
Evaluation
│
▼
Security
│
▼
Observability
│
▼
PR
│
▼

Staging
│
▼
Release
│
▼
Production Signals
## 102. Workflow para ADR

Problem
│
▼
Alternatives
│
▼
Spike
│
▼
Measurement
│
▼
Decision
│
▼
ADR
│
▼
Implementation
│
▼
Review
## 103. Workflow para evaluación

Failure or Requirement
│
▼
Dataset Case
│

▼
Evaluator
│
▼
Baseline
│
▼
Candidate
│
▼
Comparison
│
▼
Decision
## 104. Workflow para seguridad

Threat
│
▼
Risk Assessment
│
▼
Control
│
▼
Negative Test
│
▼
Monitoring
│
▼
Review
## 105. Workflow para portafolio

Completed Capability
│
▼
Evidence Selection

│
▼
Sanitization
│
▼
Business Explanation
│
▼
Technical Explanation
│
▼
Public Asset
│
▼
Interview Preparation
## 106. Checklist de inicio

[ ] Problem defined
[ ] User identified
[ ] Value hypothesis
[ ] Scope defined
[ ] Acceptance criteria
[ ] Risks identified
[ ] Dependencies available
[ ] Issue Ready
[ ] Branch created
## 107. Checklist de implementación

[ ] Contracts defined
[ ] Domain rules implemented
[ ] Errors handled
[ ] Tests added
[ ] AI evaluation added
[ ] Security controls added
[ ] Tenant isolation verified
[ ] Observability added
[ ] Documentation updated

## 108. Checklist de Pull Request

[ ] Issue linked
[ ] Problem explained
[ ] Solution explained
[ ] Tests pass
[ ] Evaluation passes
[ ] Security reviewed
[ ] Observability reviewed
[ ] Evidence included
[ ] Risks documented
[ ] Self-review completed
## 109. Checklist de despliegue

[ ] Release approved
[ ] Configuration validated
[ ] Secrets validated
[ ] Migration tested
[ ] Backup available
[ ] Rollback available
[ ] Health checks ready
[ ] Smoke tests ready
[ ] Dashboards ready
[ ] Alerts ready
## 110. Checklist de cierre

[ ] Acceptance criteria validated
[ ] Issue closed
[ ] Changelog updated
[ ] Documentation updated
[ ] Evidence captured
[ ] Portfolio impact reviewed
[ ] Skills Matrix reviewed
[ ] Lessons recorded
[ ] Next step defined

## 111. Aplicación al Proyecto 1

El GEEM AI Assistant deberá iniciar con el siguiente flujo:
Repository Foundation
│
▼
First Vertical Slice
│
▼
Identity and Tenant Context
│
▼
Model Gateway
│
▼
Conversation
│
▼
Knowledge Ingestion
│
▼
Retrieval
│
▼
Tool Calling
│
▼
Memory
│
▼
MCP
│
▼
Production Readiness
│
▼
Portfolio Release

## 112. Primer vertical slice

El primer vertical slice deberá permitir:
- abrir la interfaz;
- enviar un mensaje;
- autenticar o identificar un usuario demo;
- crear una conversación;
- llamar al Model Gateway;
- validar respuesta estructurada;
- guardar el intercambio;
- transmitir la respuesta;
- generar trace;
- medir tokens, costo y latencia.
## 113. Criterio para avanzar al siguiente módulo

No se avanzará al módulo siguiente hasta que el vertical slice actual:
- funcione;
- tenga pruebas;
- tenga observabilidad;
- esté integrado;
- esté documentado;
- cumpla Definition of Done.
## 114. Evidencia del Proyecto 1

Cada milestone deberá producir:
- release interna;
- demo;
- trace;
- dashboard;
- ADR;
- reporte de evaluación;
- actualización del caso de estudio.
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

## 115. Aplicación al Proyecto 2

Restaurant AI Operations comenzará después de completar la base del Proyecto 1.
Reutilizará:
- Model Gateway;
- Prompt Registry;
- Tool Registry;
- observabilidad;
- evaluación;
- seguridad;
- identidad;
- multi-tenancy.
No deberá duplicar infraestructura ya validada.
## 116. Aplicación al Proyecto 3

Enterprise Automation Platform deberá comenzar cuando exista experiencia comprobada en:
- tools;
- approvals;
- agentes;
- workflows;
- auditoría;
- integraciones.
Su desarrollo seguirá un enfoque de automatizaciones pequeñas y verificables.
## 117. Definition of Workflow Success

El flujo de desarrollo será exitoso cuando:
- reduce trabajo abandonado;
- detecta riesgos temprano;
- genera entregas pequeñas;
- produce evidencia continua;
- mantiene un camino principal;
- facilita revisión;
- mejora calidad;
- aumenta aprendizaje defendible.

## 118. Anti-Patterns

Quedan prohibidos los siguientes patrones:
Coding Before Definition
Comenzar a programar sin problema ni criterios.
Architecture Astronautics
Diseñar infraestructura avanzada sin necesidad.
Endless Research
Investigar sin tiempo ni decisión.
Prompt Guessing
Modificar prompts sin dataset.
Demo-Driven Quality
Considerar buena una feature porque una demo salió bien.
Parallel Project Drift
Abrir múltiples proyectos sin terminar el actual.
Hidden Work
Trabajar sin issue, PR o evidencia.
Documentation Afterthought
Intentar reconstruir toda la documentación al final.
Permanent Temporary Fix
Dejar soluciones temporales sin issue ni fecha.

## 119. Excepciones al workflow

Una excepción deberá registrar:
- etapa omitida;
- motivo;
- riesgo;
- mitigación;
- responsable;
- fecha de regularización.
Las excepciones no deberán convertirse en el proceso habitual.
## 120. Decisiones oficiales

Quedan aprobadas las siguientes reglas:
Todo trabajo relevante comenzará con un issue.
Ningún issue entrará a desarrollo sin Definition of Ready.
Toda feature AI justificará la necesidad de IA.
Toda capacidad importante tendrá hipótesis de valor.
El alcance deberá definir explícitamente qué queda fuera.
Las features se dividirán mediante vertical slices.
Las decisiones importantes requerirán ADR.
Los spikes estarán limitados y deberán producir una decisión.
Solo existirá una tarea principal de implementación activa.
La evaluación AI se diseñará junto con la feature.
Los cambios de prompts y modelos deberán compararse contra baseline.
Toda tool tendrá riesgo, permisos, pruebas y auditoría.
Los agentes se construirán progresivamente.
Todo cambio relevante utilizará Pull Request.
Ningún PR se integrará sin calidad, seguridad y observabilidad.
Toda feature relevante se validará en staging.
Toda release deberá poder revertirse.
Todo incidente importante producirá regresión.
La evidencia de portafolio se capturará durante el desarrollo.
No se iniciará el siguiente módulo hasta completar el actual.
Las ideas nuevas irán al backlog y no interrumpirán automáticamente el trabajo.
El roadmap oficial se seguirá hasta completar los tres proyectos.
El progreso se comunicará mediante capacidades terminadas, no actividad.
Las retrospectivas deberán producir acciones concretas.
La calidad se mantendrá reduciendo alcance, no eliminando controles esenciales.
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
16.
17.
18.
19.
20.
21.
22.
23.
24.
25.

## 121. Próximo documento

Documento 10 — Project 1 Product Definition
Definirá formalmente el producto GEEM AI Assistant:
- problema;
- usuarios;
- propuesta de valor;
- casos de uso;
- alcance;
- fuera de alcance;
- funcionalidades;
- módulos;
- riesgos;
- métricas;
- roadmap;
- milestones;
- criterios de éxito;
- estrategia de demo;
- evidencia de portafolio.
Este documento marcará la transición entre la fase Foundation y la construcción del primer producto real
del AI Engineering Lab.
## 122. Conclusión

El Development Workflow convierte todos los estándares anteriores en una forma única de trabajo.
A partir de este documento, cada capacidad recorrerá un camino visible:
- problema;
- definición;
- diseño;
- implementación;
- pruebas;
- evaluación;
- seguridad;
- observabilidad;
- integración;
- despliegue;
- evidencia;
- aprendizaje.

El objetivo no será avanzar rápido en muchas direcciones.
Será avanzar de forma constante en una sola dirección hasta producir sistemas completos, profesionales y
defendibles.
