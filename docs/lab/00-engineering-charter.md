# AI Engineering Lab

## Documento 00 — Engineering Charter

**Versión:** 1.0
**Estado:** Aprobado para inicio
**Responsable técnico:** Director de AI Engineering
Responsable del portafolio: Erick Eduardo Evangelista Velasco
## 1. Propósito

AI Engineering Lab es un programa profesional de ingeniería orientado a diseñar, construir, desplegar y
documentar sistemas empresariales impulsados por inteligencia artificial.
El laboratorio no tendrá un enfoque académico ni estará organizado como un curso tradicional.
Su propósito es convertir experiencia previa en arquitectura de software, desarrollo full stack,
integraciones, infraestructura y sistemas empresariales en experiencia práctica, demostrable y defendible
en AI Engineering.
El resultado esperado es un portafolio técnico capaz de competir por posiciones como:
Senior AI Engineer
AI Solutions Architect
Staff AI Engineer
Technical AI Lead
AI Automation Engineer
Enterprise AI Engineer
## 2. Objetivo profesional

El objetivo principal es posicionar a Erick Eduardo Evangelista Velasco como un ingeniero senior
especializado en el diseño y construcción de productos empresariales impulsados por inteligencia artificial.
El laboratorio deberá producir evidencia suficiente para demostrar experiencia en:
- aplicaciones basadas en modelos generativos;
- integración de modelos de diferentes proveedores;
- Retrieval-Augmented Generation;
- embeddings y búsqueda vectorial;

- tool calling;
- function calling;
- MCP;
- memoria;
- agentes;
- sistemas multiagente;
- automatización empresarial;
- evaluación de sistemas de IA;
- seguridad;
- observabilidad;
- arquitectura de software;
- despliegue y operación en producción.
El objetivo salarial de referencia será competir por posiciones entre:
$70,000 y $120,000 MXN mensuales, dependiendo del rol, empresa, modalidad y nivel de responsabilidad.
## 3. Misión

Diseñar y construir tres productos empresariales de inteligencia artificial con calidad profesional,
arquitectura defendible, documentación completa, despliegue funcional y valor real de negocio.
Cada producto deberá servir simultáneamente como:
- solución empresarial;
- proyecto de portafolio;
- caso de estudio técnico;
- demostración en vivo;
- evidencia para entrevistas;
- fuente de contenido para GitHub, CV y LinkedIn.
## 4. Visión

Al finalizar el laboratorio, el portafolio deberá demostrar que su autor no solamente sabe consumir una API
de inteligencia artificial.
Deberá demostrar que puede:
- identificar un problema empresarial;
- definir una arquitectura;
- seleccionar tecnologías;
- integrar modelos con sistemas reales;
- controlar comportamiento probabilístico;

- diseñar herramientas seguras;
- evaluar resultados;
- reducir riesgos;
- desplegar infraestructura;
- monitorear costos y calidad;
- operar el producto;
- explicar decisiones técnicas ante un panel senior.
La visión final es construir uno de los portafolios de inteligencia artificial aplicada más sólidos que pueda
presentar un Software Engineer con experiencia previa en sistemas empresariales.
## 5. Principio rector

La inteligencia artificial será tratada como un componente probabilístico dentro de un
sistema de software confiable, no como sustituto de la arquitectura, las reglas de negocio o la
ingeniería.
Los modelos generativos no controlarán directamente infraestructura, bases de datos ni operaciones
críticas.
Toda capacidad de lectura o escritura deberá estar limitada por:
- contratos;
- esquemas;
- validaciones;
- permisos;
- auditoría;
- reglas de negocio;
- mecanismos de aprobación.
## 6. Alcance del laboratorio

El laboratorio incluye la construcción de tres proyectos principales.
Proyecto 1 — GEEM AI Assistant
Asistente empresarial para consultar conocimiento, clientes, servicios, procesos, documentación e
información operativa mediante:
- RAG;
- memoria;
- herramientas;
- APIs;

- MCP;
- búsqueda híbrida;
- control de acceso;
- trazabilidad.
Proyecto 2 — Restaurant AI Operations
Plataforma de inteligencia operacional para restaurantes mediante agentes especializados en:
- ventas;
- inventario;
- compras;
- menú;
- experiencia del cliente;
- anomalías;
- reportes ejecutivos;
- recomendaciones operativas.
Proyecto 3 — Enterprise Automation Platform
Plataforma de automatización empresarial basada en:
- n8n;
- APIs;
- IA;
- WhatsApp;
- correo;
- CRM;
- ERP;
- webhooks;
- procesos de aprobación;
- auditoría;
- workflows empresariales.
## 7. Fuera de alcance

El laboratorio no incluirá proyectos diseñados únicamente para practicar una tecnología.
Quedan fuera de alcance:
- clones genéricos de ChatGPT;
- chatbots sin integración empresarial;
- preguntas sobre un único PDF como proyecto final;
- demos sin autenticación ni persistencia;
- agentes sin propósito de negocio;

- múltiples agentes creados solamente para aparentar complejidad;
- notebooks aislados como entregable principal;
- proyectos sin pruebas;
- proyectos sin documentación;
- proyectos imposibles de desplegar;
- proyectos que dependan de datos falsos como única demostración;
- arquitecturas justificadas solamente por popularidad tecnológica.
## 8. Principios de ingeniería

### 8.1. Arquitectura antes de implementación

Toda funcionalidad relevante deberá partir de:
- problema;
- caso de uso;
- restricciones;
- modelo de dominio;
- flujo;
- contrato;
- riesgo;
- criterio de aceptación.
No se implementarán componentes importantes sin comprender primero su responsabilidad dentro del
sistema.
### 8.2. Simplicidad justificada

Se elegirá la solución más sencilla que cumpla correctamente los requerimientos.
Simplicidad no significa improvisación.
Significa evitar:
- dependencias innecesarias;
- abstracciones prematuras;
- microservicios sin justificación;
- agentes innecesarios;
- frameworks agregados solamente al CV.
### 8.3. Diseño basado en evidencia

Las decisiones técnicas deberán registrarse mediante Architecture Decision Records.

Toda tecnología relevante deberá responder:
- qué problema resuelve;
- qué alternativas fueron evaluadas;
- por qué fue seleccionada;
- qué riesgos introduce;
- cómo podría reemplazarse.
### 8.4. Separación de responsabilidades

Se mantendrán separadas, cuando corresponda, las capas de:
- presentación;
- aplicación;
- dominio;
- infraestructura;
- integración;
- inteligencia artificial;
- automatización;
- seguridad;
- observabilidad.
La lógica empresarial no deberá quedar oculta dentro de prompts o workflows visuales.
### 8.5. Seguridad por diseño

Cada proyecto deberá contemplar desde su diseño:
- autenticación;
- autorización;
- segregación de datos;
- gestión de secretos;
- auditoría;
- validación de entradas;
- protección contra prompt injection;
- límites de herramientas;
- aprobación humana;
- minimización de datos.
### 8.6. Evaluación continua

Ninguna funcionalidad de IA se considerará estable únicamente porque produce respuestas visualmente
correctas.
Se deberán medir:
- precisión;

- recuperación;
- consistencia;
- relevancia;
- uso correcto de herramientas;
- latencia;
- costo;
- errores;
- seguridad;
- regresiones.
### 8.7. Observabilidad obligatoria

Toda operación significativa deberá poder investigarse.
Los sistemas deberán registrar, cuando aplique:
- solicitud;
- modelo utilizado;
- versión de prompt;
- herramientas ejecutadas;
- tokens;
- latencia;
- costo estimado;
- errores;
- resultado;
- aprobación;
- identidad del usuario.
### 8.8. Human-in-the-loop

Las acciones que puedan producir consecuencias empresariales relevantes deberán incorporar aprobación
humana.
Ejemplos:
- modificar datos;
- enviar mensajes;
- emitir cotizaciones;
- realizar pedidos;
- cancelar operaciones;
- comprometer recursos;
- afectar inventario;
- ejecutar acciones externas.
### 8.9. Independencia de proveedor

Los productos deberán evitar dependencia innecesaria de un único proveedor de modelos.

Se utilizarán adaptadores y contratos propios cuando esto produzca un beneficio real.
No se intentará ocultar completamente las diferencias entre proveedores cuando dichas diferencias sean
importantes.
### 8.10. Producción antes que demostración

Toda demo deberá estar respaldada por ingeniería real.
No se aceptarán flujos que funcionen únicamente bajo condiciones preparadas.
## 9. Principios específicos de AI Engineering

### 9.1. El modelo no es la aplicación

La aplicación incluirá:
- reglas;
- herramientas;
- datos;
- permisos;
- validaciones;
- workflows;
- interfaces;
- telemetría;
- evaluación.
El modelo será solamente una parte del sistema.
### 9.2. RAG no equivale a cargar documentos

Un sistema RAG profesional deberá considerar:
- calidad documental;
- permisos;
- duplicados;
- versiones;
- metadata;
- chunking;
- embeddings;
- recuperación;
- reranking;
- referencias;
- eliminación;

- actualización;
- evaluación.
### 9.3. Memoria no equivale a historial

Se distinguirán:
- historial conversacional;
- memoria del usuario;
- estado del agente;
- conocimiento empresarial;
- contexto temporal.
Cada tipo tendrá una estrategia distinta.
### 9.4. Tool calling antes que autonomía

Primero se construirán herramientas seguras y deterministas.
Después se permitirá al modelo decidir cuándo utilizarlas.
La autonomía será incremental.
### 9.5. Workflows antes que multiagentes

Los procesos deterministas deberán modelarse como workflows.
Los agentes se utilizarán solamente cuando exista incertidumbre, interpretación, planificación o adaptación
que justifique su uso.
### 9.6. Respuestas con evidencia

Las afirmaciones basadas en documentación deberán proporcionar fuentes o referencias.
Cuando no exista evidencia suficiente, el sistema deberá reconocerlo.
### 9.7. Los prompts son código

Los prompts deberán:
- versionarse;
- revisarse;
- probarse;
- documentarse;
- relacionarse con métricas;

desplegarse de forma controlada.
## 10. Modelo de gobierno técnico

Director de AI Engineering
Responsabilidades:
- mantener la visión técnica;
- validar arquitectura;
- cuestionar decisiones;
- definir estándares;
- ordenar prioridades;
- evitar sobrearquitectura;
- aprobar puertas de calidad;
- conducir revisiones técnicas.
Lead Engineer
Responsabilidades:
- implementar;
- investigar;
- documentar;
- probar;
- mantener repositorios;
- registrar decisiones;
- presentar resultados;
- defender técnicamente cada solución.
Durante el laboratorio, Erick desempeñará la función de Lead Engineer y progresivamente asumirá también
responsabilidades de arquitectura AI.
## 11. Proceso de decisión técnica

Toda decisión relevante seguirá este proceso:
Definir el problema.
Identificar restricciones.
Proponer alternativas.
Evaluar ventajas y riesgos.
Elegir una opción.
Documentar la decisión.
1.
2.
3.
4.
5.
6.

Implementar una prueba cuando sea necesario.
Medir resultados.
Confirmar o reemplazar la decisión.
Las decisiones relevantes deberán quedar registradas en:
docs/adr/
Formato:
ADR-0001-titulo-de-la-decision.md
Cada ADR deberá incluir:
- contexto;
- problema;
- alternativas;
- decisión;
- consecuencias;
- riesgos;
- estado.
## 12. Gestión del trabajo

Cada proyecto utilizará:
- roadmap;
- milestones;
- epics;
- issues;
- pull requests;
- criterios de aceptación;
- Definition of Ready;
- Definition of Done.
Definition of Ready
Una tarea estará lista para desarrollarse cuando:
- el objetivo sea claro;
- exista contexto suficiente;
- se conozca el resultado esperado;
- las dependencias estén identificadas;
- 7.
8.
9.

- los criterios de aceptación sean verificables;
- los riesgos principales hayan sido considerados.
Definition of Done
Una tarea estará terminada cuando:
- el código funcione;
- cumpla los criterios de aceptación;
- tenga pruebas;
- pase revisión estática;
- no exponga secretos;
- mantenga compatibilidad;
- esté documentada;
- tenga observabilidad cuando corresponda;
- haya sido integrada mediante pull request.
## 13. Estrategia de repositorios

Se crearán los siguientes repositorios:
ai-engineering-playbook
geem-ai-assistant
restaurant-ai-operations
enterprise-automation-platform
ai-engineering-portfolio
Cada repositorio deberá tener:
- README profesional;
- licencia;
- arquitectura;
- instalación;
- ejecución local;
- variables de entorno;
- pruebas;
- Docker;
- CI/CD;
- documentación;
- roadmap;
- capturas;
- demo;
- decisiones técnicas.

## 14. Estrategia Git

Se utilizará una estrategia basada en ramas cortas.
Ramas principales:
main
develop
feature/*
fix/*
refactor/*
docs/*
chore/*
Las ramas deberán representar cambios pequeños y revisables.
Convención de commits:
feat:
fix:
docs:
refactor:
test:
chore:
perf:
build:
ci:
Ejemplos:
feat(rag): add hybrid retrieval pipeline
fix(auth): prevent cross-tenant document access
docs(adr): document pgvector selection
test(tools): add approval workflow scenarios
No se integrará código directamente en main sin revisión.
## 15. Documentación mínima por proyecto

Cada proyecto deberá incluir:

docs/
├── product/
├── architecture/
├── adr/
├── api/
├── security/
├── evaluation/
├── operations/
├── diagrams/
└── interviews/
Product
- problema;
- usuarios;
- casos de uso;
- métricas;
- alcance;
- roadmap.
Architecture
- C4 Context;
- C4 Container;
- componentes;
- secuencias;
- despliegue;
- datos.
Security
- threat model;
- roles;
- permisos;
- secretos;
- prompt injection;
- riesgos.
Evaluation
- datasets;
- métricas;
- pruebas;
- resultados;
- regresiones.

Operations
- despliegue;
- monitoreo;
- respaldos;
- recuperación;
- runbooks.
Interviews
- preguntas esperadas;
- decisiones defendibles;
- trade-offs;
- lecciones;
- fallos encontrados.
## 16. Estrategia de pruebas

Cada proyecto deberá utilizar diferentes niveles de pruebas.
Pruebas unitarias
Para:
- servicios;
- validadores;
- transformaciones;
- herramientas;
- reglas;
- adaptadores.
Pruebas de integración
Para:
- base de datos;
- APIs;
- proveedores;
- colas;
- almacenamiento;
- herramientas;
- autenticación.

Pruebas end-to-end
Para flujos completos desde la interfaz hasta el resultado final.
Pruebas de IA
Para evaluar:
- recuperación;
- grounding;
- relevancia;
- uso de herramientas;
- clasificación;
- extracción;
- seguridad;
- comportamiento ante falta de información.
Pruebas de regresión
Cada modificación relevante de:
- prompts;
- modelos;
- embeddings;
- chunking;
- retrieval;
- tools;
- memoria;
- deberá compararse contra un dataset de referencia.
## 17. Estrategia de seguridad

Cada sistema deberá implementar, según su alcance:
- autenticación;
- RBAC;
- tenant isolation;
- validación de esquemas;
- rate limiting;
- cifrado en tránsito;
- protección de secretos;
- auditoría;
- sanitización;

- políticas de retención;
- aprobación humana;
- protección frente a prompt injection;
- restricción de herramientas;
- timeout;
- límites de ejecución.
El modelo no podrá:
- decidir permisos;
- modificar roles;
- acceder directamente a secretos;
- ejecutar SQL libre;
- construir llamadas externas sin validación;
- saltarse reglas empresariales.
## 18. Estrategia de evaluación

Cada producto deberá definir métricas antes de considerarse listo para producción.
Ejemplos:
RAG
- recall;
- precision;
- hit rate;
- relevancia;
- groundedness;
- calidad de citas;
- tasa de abstención correcta.
Tool calling
- selección correcta;
- argumentos válidos;
- éxito de ejecución;
- tasa de reintentos;
- acciones bloqueadas correctamente.
Agentes
- finalización;
- recuperación;
- costo;

- latencia;
- pasos innecesarios;
- intervenciones humanas;
- tasa de error.
Automatizaciones
- éxito del workflow;
- duplicados;
- idempotencia;
- errores;
- reintentos;
- tiempo de resolución;
- ahorro operativo.
## 19. Estrategia de despliegue

Todos los proyectos deberán poder ejecutarse localmente mediante Docker.
Configuración base:
Docker
Docker Compose
PostgreSQL
Redis
API
Worker
Frontend
Observability
Cada repositorio deberá incluir:
.env.example
docker-compose.yml
Makefile
README.md
Los entornos serán:
- local;
- test;
- staging;
- production.

La infraestructura evolucionará según las necesidades reales.
No se implementará Kubernetes sin una justificación concreta.
## 20. Puertas de calidad

Cada fase tendrá una revisión formal antes de avanzar.
Gate 1 — Arquitectura
- problema claro;
- arquitectura comprensible;
- tecnologías justificadas;
- riesgos identificados.
Gate 2 — Implementación base
- proyecto ejecutable;
- estructura estable;
- pruebas mínimas;
- CI activo.
Gate 3 — Funcionalidad
- casos principales completos;
- errores controlados;
- seguridad inicial;
- documentación actualizada.
Gate 4 — AI Quality
- dataset de evaluación;
- métricas;
- resultados aceptables;
- regresiones controladas.
Gate 5 — Production Readiness
- observabilidad;
- seguridad;
- deployment;
- runbooks;
- costos;
- recuperación.

Gate 6 — Portfolio Readiness
- README;
- diagramas;
- demo;
- caso de estudio;
- material de entrevistas.
No se avanzará por calendario.
Se avanzará por evidencia.
## 21. Criterios de éxito del laboratorio

El laboratorio se considerará exitoso cuando existan:
- tres productos funcionales;
- tres repositorios publicables;
- documentación profesional;
- arquitectura defendible;
- demos funcionales;
- pruebas automatizadas;
- evaluaciones de IA;
- despliegues reproducibles;
- casos de estudio;
- material para entrevistas;
- narrativa profesional coherente.
El éxito no será medido por cantidad de frameworks utilizados.
Será medido por:
- calidad;
- profundidad;
- impacto;
- claridad;
- capacidad de defensa técnica.

## 22. Riesgos principales

Riesgo: ampliar excesivamente el alcance
Mitigación:
- milestones;
- entregas verticales;
- control de backlog;
- gates.
Riesgo: estudiar sin construir
Mitigación:
cada concepto deberá aparecer dentro de un entregable real.
Riesgo: sobrearquitectura
Mitigación:
- decisiones basadas en necesidad;
- ADRs;
- revisión técnica;
- extracción gradual.
Riesgo: demos frágiles
Mitigación:
- pruebas;
- datasets;
- manejo de errores;
- observabilidad.
Riesgo: proyectos interminables
Mitigación:
- versiones;
- MVP profesional;
- entregas incrementales;
- Definition of Done.

Riesgo: dependencia de proveedores
Mitigación:
- adaptadores;
- contratos;
- comparación;
- fallback cuando sea razonable.
Riesgo: portafolio técnicamente bueno pero mal presentado
Mitigación:
- documentación ejecutiva;
- videos;
- diagramas;
- casos de estudio;
- guías para entrevistas.
## 23. Regla de continuidad

El laboratorio seguirá una sola ruta.
No se iniciará el Proyecto 2 antes de alcanzar una versión publicable del Proyecto 1.
No se iniciará el Proyecto 3 antes de alcanzar una versión publicable del Proyecto 2.
Las nuevas ideas se registrarán en backlog.
No interrumpirán la fase activa salvo que resuelvan un riesgo crítico.
## 24. Orden oficial de trabajo

Fase 0
Fundamentos y estándares
Fase 1
AI Engineering Foundation
Fase 2
GEEM AI Assistant

Fase 3
Consolidación técnica y portafolio parcial
Fase 4
Restaurant AI Operations
Fase 5
Consolidación técnica y portafolio parcial
Fase 6
Enterprise Automation Platform
Fase 7
Portafolio final, CV, LinkedIn y entrevistas
## 25. Declaración de compromiso

AI Engineering Lab priorizará:
- ingeniería sobre improvisación;
- evidencia sobre apariencia;
- claridad sobre complejidad;
- seguridad sobre autonomía;
- resultados reales sobre ejemplos académicos;
- profundidad sobre velocidad;
- calidad sobre cantidad.
Cada proyecto será tratado como un producto empresarial y como una pieza profesional de portafolio.
No se avanzará solamente para marcar tecnologías como aprendidas.
Se avanzará cuando exista una capacidad práctica, documentada y defendible.
## 26. Aprobación

Con la aprobación de este documento queda formalmente iniciado:
AI Engineering Lab
El siguiente documento será:

Documento 01 — AI Engineering Skills Matrix
Su propósito será evaluar el nivel actual en:
- software engineering;
- Python;
- arquitectura;
- APIs de IA;
- RAG;
- agentes;
- automatización;
- seguridad;
- DevOps;
- evaluación;
- entrevistas.
La matriz determinará qué conocimientos deben reforzarse durante la construcción y cuáles ya pueden
considerarse fortalezas del perfil.
