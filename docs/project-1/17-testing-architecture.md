# AI Engineering Lab

Engineering Handbook \## Documento 17 --- Project 1 Testing Architecture

**Versión:** 1.0 **Estado:** En desarrollo **Proyecto:** GEEM AI
Assistant

## Capítulo 1 --- Fundamentos de Calidad

## 1. Executive Summary

GEEM AI Assistant es una plataforma empresarial de Inteligencia
Artificial construida sobre una arquitectura modular que combina
software tradicional con componentes basados en Large Language Models
(LLMs).

A diferencia de un sistema convencional, la calidad del producto no
depende únicamente de que el código sea correcto. También depende de que
el modelo responda con evidencia, utilice las herramientas adecuadas,
respete las reglas de autorización, mantenga el aislamiento entre
organizaciones y opere dentro de límites aceptables de costo, latencia y
confiabilidad.

Por esta razón, la estrategia de pruebas de GEEM AI Assistant amplía la
ingeniería de calidad tradicional e incorpora un marco específico para
aplicaciones de IA.

Este documento define dicho marco.

## 2. Purpose

El propósito de este documento es definir la arquitectura oficial de
calidad y pruebas del proyecto.

Su objetivo es proporcionar un conjunto uniforme de principios,
estándares, herramientas y procedimientos que permitan validar, de
manera objetiva y reproducible, el comportamiento de todos los
componentes del sistema.

Este documento servirá como referencia obligatoria para el desarrollo,
integración, despliegue y mantenimiento del producto.

## 3. Scope

La arquitectura de pruebas definida en este documento aplica a todos los
componentes de GEEM AI Assistant, incluyendo:

-   Backend (FastAPI).
-   Frontend (React).
-   PostgreSQL y pgvector.
-   Redis.
-   Workers.
-   Model Gateway.
-   Prompt Registry.
-   Tool Registry.
-   Knowledge Base.
-   Motor RAG.
-   Memory Engine.
-   Approval Engine.
-   MCP Server.
-   APIs REST.
-   Streaming SSE.
-   Infraestructura.
-   Observabilidad.
-   Procesos CI/CD.

Asimismo, define la estrategia para validar componentes basados en IA,
incluyendo prompts, recuperación de información, uso de herramientas y
comportamiento de los modelos.

## 4. Out of Scope

Este documento no cubre:

-   Entrenamiento de modelos fundacionales.
-   Fine-tuning.
-   Investigación académica sobre modelos de IA.
-   Evaluaciones comparativas entre proveedores comerciales.
-   Pentesting manual realizado por terceros.
-   Auditorías regulatorias externas.

Estos temas serán documentados cuando formen parte del roadmap del
laboratorio.

## 5. Quality Philosophy

La calidad no será considerada una fase posterior al desarrollo.

Será un atributo arquitectónico presente desde el diseño inicial de cada
componente.

Todo comportamiento observable deberá poder verificarse mediante
evidencia objetiva.

No se aceptarán funcionalidades cuya validación dependa únicamente de
pruebas manuales o apreciaciones subjetivas.

La calidad será tratada como una responsabilidad compartida entre
arquitectura, desarrollo, pruebas e integración continua.

## 6. Testing Principles

La estrategia de calidad del proyecto se fundamenta en los siguientes
principios:

## 1. Testing First Thinking.

## 2. Automation by Default.

## 3. Fast Feedback.

## 4. Deterministic Testing.

## 5. Isolation.

## 6. Repeatability.

## 7. Risk-Based Coverage.

## 8. Evidence Over Opinion.

## 9. Continuous Evaluation.

## 10. AI Quality First.

Estos principios deberán reflejarse en todas las decisiones relacionadas
con el diseño de pruebas.

## 7. AI Quality First

Se adopta oficialmente el siguiente principio rector:

Todo componente relacionado con Inteligencia Artificial deberá demostrar
su calidad mediante pruebas automatizadas y métricas objetivas antes de
considerarse terminado.

Este principio aplica a:

-   Prompts.
-   Model Gateway.
-   RAG.
-   Tool Calling.
-   Human Approval.
-   Memoria.
-   Agentes.
-   MCP.
-   Integraciones con proveedores de IA.

Ningún componente será aceptado únicamente porque "parece funcionar".

## 8. AI Quality Pyramid

La estrategia de pruebas del laboratorio adopta una pirámide de calidad
adaptada específicamente para aplicaciones con LLMs.

Exploratory Testin

End-to-End Scenario

AI Evaluation & Benchmarkin

Integration / Contract / Securit

Domain / Application / Repository Test

Unit Test

Cada nivel incrementa el alcance funcional de las pruebas y, al mismo
tiempo, su costo de ejecución.

La mayor parte de la cobertura deberá concentrarse en la base de la
pirámide. s

s

g

y

g

s

## 9. Objetivos del Sistema de Testing

La arquitectura de pruebas deberá demostrar, como mínimo:

-   Correctitud funcional.
-   Correctitud arquitectónica.
-   Integridad de la persistencia.
-   Compatibilidad contractual.
-   Seguridad.
-   Calidad del comportamiento de IA.
-   Resiliencia.
-   Escalabilidad.
-   Ausencia de regresiones.
-   Operación segura en producción.

## Capítulo 2 --- Testing Architecture

## 10. Propósito de la arquitectura de pruebas

La arquitectura de pruebas define cómo se organizan, ejecutan, aíslan y
mantienen todas las pruebas automatizadas del proyecto.

Su objetivo no consiste únicamente en indicar qué herramientas utilizar.
También establece:

-   dónde deberá vivir cada tipo de prueba;
-   qué dependencias podrá utilizar;
-   qué componentes deberán sustituirse por dobles de prueba;
-   cuándo deberá utilizarse infraestructura real;
-   cómo deberán crearse los datos de prueba;
-   qué pruebas serán obligatorias para cada cambio;
-   cómo se integrarán las pruebas al flujo de desarrollo;
-   cómo se recopilará evidencia de calidad.

La arquitectura deberá permitir que las pruebas sean:

-   rápidas;
-   confiables;
-   reproducibles;
-   independientes;
-   legibles;
-   mantenibles;
-   ejecutables localmente;
-   ejecutables en CI;
-   compatibles con ejecución paralela.

## 11. Objetivos arquitectónicos

La arquitectura de pruebas deberá cumplir los siguientes objetivos.

### 11.1 Retroalimentación rápida

Un desarrollador deberá detectar errores básicos en segundos y no
después de ejecutar toda la suite.

Las pruebas se organizarán por niveles de velocidad y alcance.

### 11.2 Separación por responsabilidad

Las pruebas deberán reflejar la arquitectura del sistema.

Una prueba de dominio no deberá depender de FastAPI, PostgreSQL, Redis o
un proveedor externo de modelos.

### 11.3 Infraestructura reproducible

Los componentes de infraestructura utilizados durante las pruebas
deberán iniciarse de manera automatizada y consistente.

### 11.4 Independencia de proveedores

Las pruebas funcionales no deberán depender directamente de OpenAI,
Anthropic, Google, Azure u otro proveedor.

El acceso a modelos deberá realizarse mediante el ModelGateway.

### 11.5 Aislamiento de datos

Cada prueba deberá controlar los datos que crea.

Ninguna prueba podrá asumir que otra prueba ya ejecutó una operación
previa.

### 11.6 Compatibilidad local y CI

La misma suite deberá poder ejecutarse en:

-   entorno local;
-   contenedores;
-   GitHub Actions;
-   staging;
-   pipelines programados.

### 11.7 Escalabilidad de la suite

La arquitectura deberá permitir incorporar nuevos módulos sin convertir
la suite en una estructura centralizada difícil de mantener.

## 12. Modelo de capas de testing

Las pruebas se organizarán de acuerdo con las capas del sistema.

``` text
┌─────────────────────────────────────────────────────────┐
│                 End-to-End Tests                        │
├─────────────────────────────────────────────────────────┤
│ AI Evaluations │ Security │ Performance │ Chaos         │
├─────────────────────────────────────────────────────────┤
│ API │ Contract │ Integration │ Worker Tests             │
├─────────────────────────────────────────────────────────┤
│ Repository │ Infrastructure Adapter Tests               │
├─────────────────────────────────────────────────────────┤
│ Application Use Case Tests                              │
├─────────────────────────────────────────────────────────┤
│ Domain Tests                                            │
├─────────────────────────────────────────────────────────┤
│ Unit Tests                                              │
└─────────────────────────────────────────────────────────┘
```

Cada nivel tendrá un propósito específico y reglas de dependencia
claramente definidas.

## 13. Dependencias permitidas por nivel

### 13.1 Unit Tests

Podrán depender únicamente de:

-   la unidad bajo prueba;
-   objetos de valor;
-   funciones puras;
-   dobles de prueba en memoria;
-   librerías estándar.

No deberán depender de:

-   red;
-   sistema de archivos real;
-   base de datos;
-   Redis;
-   colas;
-   servicios externos;
-   reloj del sistema sin abstracción.

### 13.2 Domain Tests

Podrán depender de:

-   entidades;
-   agregados;
-   objetos de valor;
-   servicios de dominio;
-   eventos de dominio;
-   excepciones de dominio.

No deberán depender de frameworks o infraestructura.

### 13.3 Application Tests

Podrán depender de:

-   casos de uso;
-   comandos;
-   queries;
-   puertos;
-   repositorios falsos;
-   gateways falsos;
-   event bus en memoria;
-   unit of work en memoria.

No deberán depender directamente de implementaciones de infraestructura.

### 13.4 Repository Tests

Podrán depender de:

-   PostgreSQL real mediante contenedor;
-   SQLAlchemy;
-   Alembic;
-   transacciones;
-   RLS;
-   implementaciones concretas de repositorios.

### 13.5 Integration Tests

Podrán utilizar varias implementaciones reales, siempre que el objetivo
sea validar su integración.

### 13.6 End-to-End Tests

Podrán utilizar el sistema completo desplegado en un entorno controlado.

## 14. Clasificación por velocidad

Las pruebas se clasificarán en cuatro grupos de ejecución.

Grupo Tiempo objetivo por prueba Uso principal Fast Menos de 100 ms
Unit, Domain y Application Standard Menos de 2 s Repository, API y
Contract Slow Menos de 30 s Integration, AI Evaluation y E2E Extended
Variable Load, Chaos y benchmarks programados

Los tiempos son objetivos, no garantías absolutas.

Una prueba que exceda regularmente su grupo deberá revisarse o
reclasificarse.

## 15. Clasificación por dependencia

Cada prueba deberá pertenecer a una de las siguientes categorías.

Hermetic

No utiliza dependencias externas ni infraestructura compartida.

Containerized

Utiliza servicios reales levantados mediante contenedores.

Networked

Necesita acceso de red controlado.

Provider Evaluation

Realiza llamadas a un proveedor de IA real.

Environment Evaluation

Opera sobre un ambiente desplegado.

Las pruebas Provider Evaluation y Environment Evaluation no formarán
parte del pipeline obligatorio de cada commit.

## 16. Arquitectura de ejecución

La ejecución completa tendrá las siguientes etapas.

Developer Chang

``` text
│
▼
```

Static Validatio

``` text
│
▼
```

Fast Test Suit

``` text
│
▼
```

Repository and Contract Test

``` text
│
▼
```

Integration and Security Test

``` text
│
▼
```

AI Evaluation Gate

``` text
│
▼
```

End-to-End Validatio

``` text
│
▼
```

Deployment Candidat

Cada etapa deberá detener el pipeline cuando un gate obligatorio falle.
e

e

n

s

e

n

s

s

## 17. Herramientas oficiales

La primera versión del proyecto utilizará las siguientes herramientas.

Necesidad Herramienta Framework principal Pytest Cobertura pytest-cov
Ejecución paralela pytest-xdist Async testing pytest-asyncio Generación
de datos Faker Factories factory_boy Property-based testing Hypothesis
Contenedores de prueba Testcontainers Cliente HTTP HTTPX Mock HTTP
externo RESPX PostgreSQL Imagen oficial PostgreSQL Redis Imagen oficial
Redis OpenAPI validation openapi-spec-validator o equivalente aprobado
Mutation testing mutmut o equivalente aprobado Frontend unit testing
Vitest Component testing React Testing Library Browser E2E Playwright
Performance k6 Security scanning Semgrep, Bandit y herramientas
aprobadas AI evaluation Framework interno sobre datasets versionados

La incorporación de herramientas adicionales requerirá justificación
técnica.

## 18. Regla de abstracción

Toda dependencia no determinista deberá estar detrás de una abstracción.

Esto incluye:

-   reloj;
-   generación de identificadores;
-   proveedores LLM;
-   embeddings;
-   almacenamiento de objetos;
-   correo electrónico;
-   notificaciones;
-   colas;
-   servicios externos;
-   acceso a secretos.

Ejemplo conceptual:

``` text
from datetime import datetim
from typing import Protoco

class Clock(Protocol)
def now(self) -> datetime
```

..

``` text
class SystemClock
def now(self) -> datetime
return datetime.utcnow(

class FixedClock
def __init__(self, value: datetime) -> None
```

self.\_value = valu

``` text
def now(self) -> datetime
return self._valu
```

Las pruebas deberán utilizar FixedClock cuando una regla dependa del
tiempo. .

:

:

:

e

e

l

e

:

:

:

)

:

## 19. Dobles de prueba oficiales

Se reconocen los siguientes tipos de dobles.

Fake

Implementación funcional simplificada.

Ejemplo:

``` text
class InMemoryConversationRepository
def __init__(self) -> None
```

self.\_items: dict\[str, Conversation\] = {

``` text
async def save(self, conversation: Conversation) -> None
```

self.\_items\[conversation.id\] = conversatio

``` text
async def get(self, conversation_id: str) -> Conversation |
```

None

``` text
return self._items.get(conversation_id
```

Stub

Devuelve respuestas predefinidas.

Spy

Registra interacciones para verificarlas posteriormente.

Mock

Valida expectativas específicas de interacción.

Simulator

Reproduce de forma simplificada el comportamiento de un sistema
complejo.

Sandbox

Entorno real aislado proporcionado por un tercero. :

:

:

)

``` text
}
```

n

:

## 20. Criterio para elegir un doble

Se preferirá:

## 1. objeto real;

## 2. fake;

## 3. stub;

## 4. spy;

## 5. mock estricto.

Los mocks estrictos se utilizarán con moderación.

Un exceso de mocks produce pruebas acopladas a detalles internos y
dificulta la refactorización.

## 21. Arquitectura de test suites

La suite se dividirá en conjuntos independientes.

Fast Suit

``` text
├── uni
├── domai
└── applicatio
```

Standard Suit

``` text
├── repositor
├── ap
├── contrac
└── worke
```

AI Suit

``` text
├── prompt
├── ra
├── tool
├── memor
├── approva
└── model_gatewa
```

Security Suit

``` text
├── authorizatio
├── tenant_isolatio
├── prompt_injectio
└── dependency_securit
```

i

g

e

t

s

e

y

r

n

s

l

t

e

e

y

n

y

n

n

n

y

System Suit

``` text
├── integratio
├── e2
├── performanc
└── chao
```

## 22. Marcadores oficiales de Pytest

Se utilizarán marcadores para seleccionar grupos de pruebas.

``` text
[pytest
```

markers unit: pruebas unitarias rápida domain: pruebas de reglas de
domini application: pruebas de casos de us repository: pruebas de
persistenci integration: pruebas de integració api: pruebas de endpoint
contract: pruebas de contrato worker: pruebas de workers y cola
security: pruebas de segurida ai_eval: evaluaciones de componentes de I
rag: evaluaciones del pipeline RA prompt: pruebas de prompt
tool_calling: pruebas de selección y ejecución de tool e2e: pruebas
end-to-en performance: pruebas de rendimient chaos: pruebas de
resilienci slow: pruebas lenta provider: pruebas que llaman proveedores
externo

Una prueba podrá tener más de un marcador.

## 23. Comandos estándar

El proyecto deberá ofrecer comandos uniformes mediante Makefile o
herramienta equivalente.

``` text
make tes
make test-fas
make test-uni
make test-domai
make test-applicatio
```

e

``` text
]
```

=

t

s

e

t

t

e

n

n

n

s

d

s

s

a

d

s

s

s

G

n

a

o

o

o

A

s

s

``` text
make test-repositor
make test-ap
make test-contrac
make test-integratio
make test-a
make test-securit
make test-e2
make test-al
make coverag
```

Los desarrolladores no deberán memorizar comandos complejos de Pytest.

## 24. Ejecución predeterminada

El comando:

``` text
make tes
```

deberá ejecutar la suite requerida antes de abrir un Pull Request.

Inicialmente incluirá:

-   Unit Tests.
-   Domain Tests.
-   Application Tests.
-   Repository Tests.
-   API Tests.
-   Contract Tests.

No incluirá de forma predeterminada:

-   Provider Evaluations.
-   Load Tests.
-   Chaos Tests.
-   Suites extendidas.

## 25. Arquitectura para pruebas asíncronas

Dado que FastAPI, SQLAlchemy y los gateways utilizarán operaciones
asíncronas, la suite deberá soportar pruebas async.

Ejemplo:

``` text
import pytes
```

t

i

t

e

l

e

i

y

t

y

n

``` text
@pytest.mark.asynci
async def test_creates_conversation
```

create_conversation_handler conversation_repository ) command =
CreateConversationCommand tenant_id="tenant-001" user_id="user-001"
title="Nueva conversación"

result = await create_conversation_handler.handle(command

stored = await conversation_repository.get(result.conversation_id

assert stored is not Non assert stored.title == "Nueva conversación

No se deberán introducir event loops manuales dentro de las pruebas
salvo que exista una necesidad demostrable.

## 26. Arquitectura para pruebas paralelas

La suite deberá diseñarse para ser compatible con pytest-xdist

``` text
pytest -n aut
```

Para permitir ejecución paralela:

-   cada prueba utilizará datos propios;
-   los identificadores serán únicos;
-   las bases de datos deberán aislarse por worker o por esquema;
-   los puertos no deberán fijarse manualmente;
-   los archivos temporales deberán crearse mediante fixtures;
-   no se compartirán variables globales mutables.

## 27. Estrategia de aislamiento de base de datos

Se admiten tres estrategias. :

)

o

o

,

,

e

,

,

,

(

(

"

.

)

)

Estrategia A --- Transacción por prueba

Cada prueba se ejecuta dentro de una transacción que se revierte al
finalizar.

Ventajas:

-   rápida;
-   bajo consumo;
-   sencilla.

Limitaciones:

-   puede ocultar problemas relacionados con commits;
-   no valida correctamente algunos escenarios asíncronos;
-   no representa flujos con múltiples conexiones.

Estrategia B --- Esquema por worker

Cada worker paralelo utiliza un esquema independiente.

Ventajas:

-   buen aislamiento;
-   compatible con paralelismo;
-   permite commits reales.

Limitaciones:

-   configuración más compleja.

Estrategia C --- Base de datos por suite

Cada suite utiliza una base de datos temporal.

Ventajas:

-   alto realismo;
-   menor riesgo de interferencia.

Limitaciones:

-   mayor tiempo de preparación.

La estrategia inicial recomendada será:

-   transacción por prueba para Repository Tests simples;

-   esquema por worker para suites paralelas;

-   base temporal para pruebas de migraciones y RLS.

## 28. Arquitectura de Testcontainers

Testcontainers será utilizado para levantar dependencias reales durante
las pruebas.

Servicios iniciales:

-   PostgreSQL;
-   Redis;
-   almacenamiento S3 compatible cuando sea necesario.

Ejemplo conceptual:

``` text
import pytes
from testcontainers.postgres import PostgresContaine

@pytest.fixture(scope="session"
def postgres_container()
with PostgresContainer("postgres:16") as postgres
```

yield postgre

``` text
@pytest.fixture(scope="session"
def database_url(postgres_container) -> str
return postgres_container.get_connection_url(
```

La versión de la imagen deberá coincidir con la versión aprobada para
producción.

No se deberá probar contra SQLite cuando el sistema productivo utilice
PostgreSQL y la semántica pueda diferir.

## 29. Arquitectura de servicios externos

Las pruebas no deberán depender de servicios externos reales para
validar comportamiento funcional ordinario.

Ejemplo con RESPX:

``` text
import http
import resp
```

x

x

t

s

:

)

)

:

)

r

:

``` text
@respx.moc
async def test_embedding_provider_maps_response()
```

route = respx.post("https://provider.example/v1/ embeddings").mock
return_value=httpx.Response 200 json=

``` text
"data":

"embedding": [0.1, 0.2, 0.3]

}
```

provider = ExternalEmbeddingProvider(api_key="test-key"

vector = await provider.embed("document text"

assert vector == \[0.1, 0.2, 0.3 assert route.calle

Estas pruebas validan el adapter, no al proveedor.

## 30. Arquitectura de pruebas de IA

Las pruebas relacionadas con IA se dividirán en tres niveles.

Nivel A --- Deterministic Component Tests

Utilizan fakes y respuestas predefinidas.

Validan:

-   parsing;
-   rutas;
-   políticas;
-   selección de herramientas;
-   persistencia;
-   manejo de errores;
-   fallbacks. )

)

k

,

,

``` text
]
```

(

``` text
{

}

{
```

d

``` text
[
```

(

``` text
]
```

:

)

,

)

Nivel B --- Dataset Evaluations

Ejecutan casos versionados sobre componentes reales.

Validan:

-   relevancia;
-   groundedness;
-   precisión de citas;
-   selección de tools;
-   cumplimiento de instrucciones.

Nivel C --- Provider Evaluations

Utilizan modelos reales.

Validan:

-   calidad efectiva;
-   regresiones del proveedor;
-   comportamiento con prompts reales;
-   costo;
-   latencia.

Los niveles A y B serán obligatorios en CI según el tipo de cambio.

El nivel C se ejecutará de forma controlada y programada.

## 31. Quality Gates arquitectónicos

Los siguientes gates serán obligatorios.

Gate 1 --- Static Quality

-   Ruff.
-   Mypy.
-   validación de imports.
-   análisis de seguridad.
-   formato.

Gate 2 --- Fast Tests

-   Unit.

-   Domain.

-   Application.

Gate 3 --- Persistence and Contracts

-   Repository.
-   migrations.
-   API.
-   OpenAPI.
-   Contract.

Gate 4 --- Security

-   autorización;
-   aislamiento entre tenants;
-   validación de entrada;
-   RLS.

Gate 5 --- AI Quality

-   prompts;
-   RAG;
-   tools;
-   memory;
-   approval;
-   calidad mínima del dataset.

Gate 6 --- System Validation

-   integration;
-   E2E;
-   smoke;
-   deployment verification.

## 32. Fallo rápido

La ejecución deberá detenerse temprano cuando falle una etapa
fundamental.

Ejemplo:

Lint failur ↓ No ejecutar Integration Test

Domain failur e

e

s

↓ No ejecutar AI Evaluatio

Migration failur ↓ No crear artefacto desplegabl

Esto reduce tiempo y costo computacional.

## 33. Artefactos de prueba

Cada ejecución de CI deberá conservar, cuando corresponda:

-   reporte JUnit;
-   cobertura;
-   reporte de lint;
-   resultados de seguridad;
-   resultados de AI Evaluation;
-   métricas de costo;
-   métricas de latencia;
-   screenshots y videos de Playwright;
-   logs de contenedores fallidos;
-   datasets utilizados;
-   versión del modelo;
-   versión del prompt.

La evidencia deberá permitir analizar una falla sin repetir
inmediatamente toda la ejecución.

## 34. Trazabilidad de pruebas

Toda prueba deberá poder relacionarse con al menos uno de los siguientes
elementos:

-   regla de dominio;
-   caso de uso;
-   requisito;
-   riesgo;
-   incidente;
-   contrato;
-   decisión arquitectónica;
-   escenario de seguridad;
-   métrica de IA. e

n

e

No será obligatorio colocar un identificador en cada nombre de prueba,
pero la relación deberá resultar clara mediante ubicación, nombre o
metadata.

## 35. Definition of Done del capítulo

La arquitectura de pruebas se considerará implementada cuando:

-   exista la estructura oficial del repositorio;
-   Pytest esté configurado;
-   los marcadores estén registrados;
-   Testcontainers pueda levantar PostgreSQL y Redis;
-   las pruebas async funcionen;
-   la suite pueda ejecutarse en paralelo;
-   existan comandos estándar;
-   CI ejecute los quality gates definidos;
-   los resultados generen artefactos;
-   la arquitectura sea respetada por los primeros vertical slices.

## Capítulo 3 --- Repository Test

Organization \## 36. Propósito

Este capítulo define la organización oficial de las pruebas dentro del
repositorio.

La estructura deberá permitir que un ingeniero pueda identificar
inmediatamente:

-   qué se está probando;
-   qué nivel de prueba corresponde;
-   qué dependencias utiliza;
-   qué fixtures necesita;
-   qué tan costosa será su ejecución.

## 37. Estrategia general de organización

El proyecto utilizará una estrategia híbrida:

-   pruebas cercanas al contexto funcional;
-   suites transversales separadas para evaluaciones globales;
-   infraestructura compartida centralizada;
-   datasets versionados como artefactos del repositorio.

No se utilizará una única carpeta masiva con cientos de archivos sin
clasificación.

## 38. Árbol o cial inicia

repository

``` text
├── apps
│   ├── api
│   ├── worker
│   └── web
│
├── src
│   └── geem_ai
│       ├── domains
│       │   ├── conversations
│       │   ├── knowledge
│       │   ├── tools
```

/

/

/

/

/

fi /

/

/

/

l

/

/

``` text
│       │   ├── approvals
│       │   ├── memory
│       │   └── identity
│       │
│       ├── application
│       ├── infrastructure
│       ├── interfaces
│       └── shared
│
├── tests
│   ├── unit
│   ├── domain
│   ├── application
│   ├── repository
│   ├── api
│   ├── contract
│   ├── integration
│   ├── worker
│   ├── security
│   ├── ai
│   │   ├── prompts
│   │   ├── rag
│   │   ├── tools
│   │   ├── memory
│   │   ├── approvals
│   │   └── model_gateway
│   ├── e2e
│   ├── performance
│   ├── chaos
│   ├── fixtures
│   ├── factories
│   ├── fakes
│   ├── datasets
│   ├── snapshots
│   └── conftest.p
│
├── scripts
├── migrations
├── pyproject.tom
└── Makefil
```

Esta estructura podrá evolucionar mediante una decisión arquitectónica,
pero no deberá modificarse de manera improvisada. /

/

/

e

/

/

/

/

/

/

/

/

/

/

/

/

/

l

/

/

/

/

/

y

/

/

/

/

/

/

/

/

/

/

/

/

/

## 39. Organización por dominio

Cuando el volumen lo justifique, cada categoría podrá organizarse por
dominio.

tests/domain

``` text
├── conversations
│   ├── test_conversation.p
│   ├── test_message.p
│   └── test_conversation_policies.p
├── knowledge
│   ├── test_document.p
│   ├── test_chunk.p
│   └── test_ingestion_rules.p
├── tools
│   ├── test_tool_definition.p
│   └── test_tool_execution_policy.p
└── approvals
├── test_approval_request.p
└── test_approval_policy.p
```

La estructura deberá reflejar la terminología del dominio, no la del
framework.

## 40. Organización de Unit Tests

Las pruebas unitarias se utilizarán principalmente para:

-   funciones puras;
-   serializadores;
-   parsers;
-   utilidades;
-   adaptadores pequeños;
-   estrategias;
-   validadores;
-   componentes aislados.

Ejemplo:

tests/unit

``` text
├── shared
│   ├── test_token_estimator.p
│   ├── test_identifier_generator.p
│   └── test_retry_policy.p
├── infrastructure
│   ├── test_openai_response_mapper.p
```

/

/

/

/

/

/

/

/

y

y

y

y

y

y

y

y

y

y

y

y

y

y

``` text
│   └── test_s3_object_key_builder.p
└── interfaces
└── test_error_response_mapper.p
```

No deberán duplicar las pruebas de dominio.

## 41. Organización de Application Tests

Cada caso de uso relevante deberá disponer de pruebas claras.

tests/application

``` text
├── conversations
│   ├── test_create_conversation.p
│   ├── test_send_message.p
│   ├── test_archive_conversation.p
│   └── test_list_conversations.p
├── knowledge
│   ├── test_upload_document.p
│   ├── test_process_document.p
│   └── test_delete_document.p
└── approvals
├── test_request_approval.p
├── test_approve_action.p
└── test_reject_action.p
```

Cada archivo deberá concentrarse en un caso de uso o una responsabilidad
cohesionada.

## 42. Organización de Repository Tests

tests/repository

``` text
├── conversations
│   ├── test_postgres_conversation_repository.p
│   └── test_postgres_message_repository.p
├── knowledge
│   ├── test_postgres_document_repository.p
│   └── test_pgvector_chunk_repository.p
├── memory
│   └── test_postgres_memory_repository.p
└── identity
└── test_postgres_user_repository.p
```

/

/

/

/

/

/

/

/

/

/

y

y

y

y

y

y

y

y

y

y

y

y

y

y

y

y

y

y

El nombre deberá indicar la implementación concreta validada.

## 43. Organización de API Tests

tests/api

``` text
├── conversations
│   ├── test_create_conversation_endpoint.p
│   ├── test_send_message_endpoint.p
│   └── test_stream_message_endpoint.p
├── knowledge
│   ├── test_upload_document_endpoint.p
│   └── test_list_documents_endpoint.p
├── approvals
│   └── test_approval_endpoints.p
└── health
├── test_liveness.p
└── test_readiness.p
```

Las pruebas deberán validar comportamiento observable de la API, no
detalles internos del controlador.

## 44. Organización de Contract Tests

tests/contract

``` text
├── openapi
│   ├── test_openapi_schema_is_valid.p
│   ├── test_required_routes_exist.p
│   └── test_error_contracts.p
├── tools
│   ├── test_tool_input_schemas.p
│   └── test_tool_output_schemas.p
├── events
│   ├── test_domain_event_contracts.p
│   └── test_queue_message_contracts.p
└── providers
├── test_model_provider_adapter_contract.p
└── test_embedding_provider_contract.p
```

Los contratos compartidos con otros sistemas deberán mantenerse
versionados. /

/

/

/

/

/

/

/

/

/

y

y

y

y

y

y

y

y

y

y

y

y

y

y

y

y

y

## 45. Organización de Integration Tests

tests/integration

``` text
├── conversations
│   └── test_message_generation_flow.p
├── ingestion
│   └── test_document_ingestion_pipeline.p
├── rag
│   └── test_retrieval_generation_pipeline.p
├── tools
│   └── test_tool_execution_pipeline.p
└── infrastructure
├── test_postgres_redis_coordination.p
└── test_object_storage_pipeline.p
```

Las pruebas de integración deberán validar un flujo entre componentes
claramente delimitado.

No deberán convertirse automáticamente en pruebas del sistema completo.

## 46. Organización de Worker Tests

tests/worker

``` text
├── test_document_ingestion_worker.p
├── test_embedding_worker.p
├── test_cleanup_worker.p
├── test_retry_behavior.p
├── test_dead_letter_behavior.p
└── test_idempotency.p
```

Los workers deberán probarse tanto de forma aislada como integrados con
la cola cuando corresponda.

## 47. Organización de Security Tests

tests/security

``` text
├── authentication
├── authorization
├── tenant_isolation
├── row_level_security
├── prompt_injection
```

/

/

/

/

/

/

/

/

/

/

/

/

/

y

y

y

y

y

y

y

y

y

y

y

y

``` text
├── tool_permissions
├── data_exposure
└── rate_limiting
```

Las pruebas de seguridad deberán organizarse por riesgo y control, no
únicamente por componente.

## 48. Organización de AI Evaluations

tests/ai

``` text
├── prompts
│   ├── test_system_prompt_regression.p
│   ├── test_refusal_behavior.p
│   └── test_instruction_priority.p
├── rag
│   ├── test_retrieval_relevance.p
│   ├── test_groundedness.p
│   ├── test_citation_accuracy.p
│   └── test_answer_completeness.p
├── tools
│   ├── test_tool_selection.p
│   ├── test_argument_generation.p
│   └── test_no_unnecessary_tool_call.p
├── memory
│   ├── test_memory_relevance.p
│   └── test_memory_isolation.p
├── approvals
│   ├── test_approval_required.p
│   └── test_approval_bypass_prevention.p
└── model_gateway
├── test_provider_fallback.p
├── test_cost_limits.p
└── test_model_policy.p
```

## 49. Datasets versionados

Los datasets deberán almacenarse fuera de los archivos de prueba cuando
representen casos reutilizables.

tests/datasets

``` text
├── prompts
│   ├── instruction_following.v1.json
│   └── refusal_cases.v1.json
```

/

/

/

/

/

/

/

/

/

/

/

/

y

y

y

y

l

y

y

y

y

y

y

y

y

y

y

l

y

y

y

``` text
├── rag
│   ├── retrieval_cases.v1.json
│   ├── groundedness_cases.v1.json
│   └── citation_cases.v1.json
├── tools
│   ├── selection_cases.v1.json
│   └── arguments_cases.v1.json
└── security
└── prompt_injection_cases.v1.json
```

Cada dataset deberá indicar:

-   versión;
-   propósito;
-   propietario;
-   fecha de creación;
-   criterios de aprobación;
-   origen de los casos;
-   restricciones de privacidad.

## 50. Formato recomendado para datasets

Ejemplo:

``` text
"case_id": "rag-citation-001"
"question": "¿Cuál es el periodo de retención de documentos?"
"documents":

"document_id": "policy-001"
"content": "Los documentos deberán conservarse durante
```

cinco años.

``` text
]
"expected":
"answer_contains": ["cinco años"]
"required_citations": ["policy-001"]
"must_be_grounded": tru
}
"tags": ["rag", "citation", "policy"
```

Los datasets no deberán contener secretos, credenciales ni datos
personales innecesarios.

``` text
{

}
```

,

,

``` text
{

}
```

/

/

``` text
"
```

/

``` text
{

[
```

e

l

,

l

l

l

,

l

,

``` text
]
```

l

,

,

## 51. Fixtures compartidas

Las fixtures compartidas se organizarán por responsabilidad.

tests/fixtures

``` text
├── database.p
├── redis.p
├── clients.p
├── authentication.p
├── model_gateway.p
├── object_storage.p
├── clock.p
└── tenants.p
```

El archivo conftest.py raíz deberá mantenerse pequeño.

Su responsabilidad será registrar plugins o fixtures globales, no
contener toda la infraestructura de prueba.

Ejemplo:

pytest_plugins =

``` text
"tests.fixtures.database"
"tests.fixtures.redis"
"tests.fixtures.clients"
"tests.fixtures.authentication"
"tests.fixtures.model_gateway"
```

## 52. Alcance de fixtures

Se utilizarán los siguientes scopes con intención explícita.

Function

Predeterminado para datos mutables.

Class

Uso limitado para grupos cohesionados.

Module

Permitido para recursos costosos que puedan reiniciarse de manera
segura.

``` text
]
```

y

y

y

y

/

y

``` text
[
```

y

y

y

,

,

,

,

,

Session

Reservado para:

-   contenedores;
-   configuración inmutable;
-   metadata de base de datos;
-   datasets.

No deberán compartirse entidades mutables mediante fixtures de sesión.

## 53. Factories oficiales

Las factories deberán crear objetos válidos por defecto.

``` text
import factor

class ConversationFactory(factory.Factory)
class Meta
```

model = Conversatio

id = factory.Sequence(lambda n: f"conversation-{n}" tenant_id =
factory.Sequence(lambda n: f"tenant-{n}" user_id =
factory.Sequence(lambda n: f"user-{n}" title = factory.Faker("sentence",
nb_words=4

Una prueba deberá sobrescribir únicamente los datos relevantes para su
escenario.

conversation = ConversationFactory(title="Incidente de producción"

## 54. Builders para escenarios complejos

Cuando una entidad necesite múltiples pasos, se utilizará un builder.

conversation = ConversationBuilder( .for_tenant("tenant-001"
.owned_by("user-001" .with_user_message("Necesito revisar un contrato"
.with_assistant_message("Adjunta el documento." .build( )

)

)

y

:

(

)

)

n

)

:

)

)

)

)

)

)

Los builders deberán comunicar intención, no ocultar reglas importantes.

## 55. Fakes compartidos

tests/fakes

``` text
├── fake_clock.p
├── fake_model_gateway.p
├── fake_embedding_gateway.p
├── fake_event_bus.p
├── fake_object_storage.p
├── fake_notification_service.p
└── in_memory_repositories
```

Los fakes deberán respetar los mismos Protocols que las implementaciones
reales.

Esto permitirá ejecutar contract tests sobre ambas implementaciones
cuando sea apropiado.

## 56. Snapshots

Los snapshots podrán utilizarse para:

-   schemas;
-   respuestas estructuradas;
-   prompts renderizados;
-   eventos;
-   documentos JSON;
-   componentes de interfaz estables.

No deberán utilizarse para aprobar ciegamente respuestas largas
generadas por LLMs.

Toda actualización de snapshot deberá revisarse como un cambio
funcional.

## 57. Archivos temporales

Las pruebas que requieran archivos utilizarán fixtures temporales.

``` text
def test_document_parser(tmp_path)
```

document_path = tmp_path / "policy.txt
document_path.write_text("Retention period: five years." /

y

y

y

y

/

y

y

:

``` text
"
```

)

result = parse_document(document_path

assert result.text == "Retention period: five years.

No deberán escribir en carpetas compartidas del repositorio.

## 58. Convenciones de nombres

Los nombres deberán describir comportamiento.

Formato recomendado:

test\_`<behavior>`{=html}*when*\<condition

Ejemplos

``` text
def test_rejects_message_when_conversation_is_archived()
```

..

``` text
def test_requires_approval_when_tool_can_modify_customer_data()
```

..

``` text
def test_returns_only_documents_from_current_tenant()
```

..

También se permitirá el estilo:

test\_`<scenario>`{=html}\_\<expected_result

La claridad tendrá prioridad sobre la rigidez.

## 59. Estructura interna de una prueba

Se utilizará preferentemente el patrón Arrange--Act--Assert.

``` text
def test_archives_active_conversation()
```

# Arrang

conversation = ConversationFactory(status=ConversationStatus.ACTIVE

# Ac

conversation.archive( .

.

.

:

t

e

)

:

)

)

:

"

:

:

# Asser

assert conversation.status is ConversationStatus.ARCHIVE

En pruebas pequeñas podrán omitirse los comentarios cuando la estructura
sea evidente.

## 60. Un comportamiento principal por prueba

Cada prueba deberá validar un comportamiento principal.

Esto no significa limitarse a una sola aserción.

Ejemplo válido:

assert result.status_code == 20 assert result.json()\["title"\] == "New
conversation assert result.json()\["tenant_id"\] == tenant.id

Todas las aserciones pertenecen al mismo resultado observable.

## 61. Parametrización

Se utilizará parametrización para comportamientos equivalentes.

``` text
import pytes

@pytest.mark.parametrize
```

("role", "expected")

("owner", True) ("admin", True) ("member", False) ("viewer", False)

``` text
]

def test_role_can_delete_knowledge_document(role, expected)
```

assert can_delete_document(role) is expecte

No deberá utilizarse parametrización cuando haga la prueba difícil de
comprender. )

``` text
[
```

,

t

t

,

,

,

(

,

,

1

d

``` text
"
```

:

D

## 62. Property-Based Testing

Hypothesis se utilizará en componentes con gran espacio de entrada.

Casos recomendados:

-   validadores;
-   parsers;
-   serialización;
-   normalización;
-   límites de tokens;
-   chunking;
-   generación de identificadores;
-   reglas matemáticas;
-   sanitización.

Ejemplo:

``` text
from hypothesis import give
from hypothesis import strategies as s

@given(st.text()
def test_normalizer_is_idempotent(value: str)
```

normalized = normalize_text(value

assert normalize_text(normalized) == normalize

## 63. Datos sensibles

No se utilizarán copias directas de datos productivos.

Cuando sea necesario representar casos reales:

-   se anonimizarán;
-   se minimizarán;
-   se sintetizarán;
-   se revisarán antes de incorporarse.

Todo dataset de prueba deberá considerarse parte del repositorio y, por
lo tanto, potencialmente accesible por terceros autorizados. )

n

)

t

:

d

## 64. Pruebas generadas desde incidentes

Cada incidente relevante deberá producir uno o más casos de regresión.

Los casos podrán almacenarse en:

-   pruebas directas;
-   datasets;
-   escenarios E2E;
-   suites de seguridad.

La referencia al incidente deberá conservarse en metadata o
documentación, sin incluir datos sensibles.

## 65. Prohibiciones organizativas

No se permitirá:

-   almacenar pruebas únicamente junto al código sin una estrategia
    común;
-   usar test_utils.py como contenedor ilimitado;
-   crear un conftest.py monolítico;
-   depender de orden de ejecución;
-   reutilizar una base de datos manual del desarrollador;
-   utilizar credenciales reales en fixtures;
-   mezclar E2E con Unit Tests;
-   usar nombres como test_1, test_basic o test_stuff;
-   duplicar factories en múltiples carpetas;
-   crear datasets sin versión.

## 66. Checklist para agregar un nuevo módulo

Cuando se agregue un nuevo módulo, deberá determinarse:

-   dominio al que pertenece;

-   casos de uso incluidos;

-   repositories requeridos;

-   adapters externos;

-   contratos;

-   riesgos de seguridad;

-   evaluaciones de IA aplicables;

-   fixtures;

-   factories;

-   datasets;

-   pruebas E2E necesarias;

-   gates de CI afectados.

## 67. Definition of Done del capítulo

La organización del repositorio se considerará definida cuando:

-   exista la estructura base de tests/;
-   estén creadas las carpetas oficiales;
-   conftest.py registre fixtures modulares;
-   existan convenciones de nombres;
-   las factories estén centralizadas;
-   los fakes implementen Protocols;
-   los datasets tengan versiones;
-   las pruebas puedan descubrirse mediante Pytest;
-   los marcadores permitan ejecutar cada suite;
-   la estructura esté documentada en el repositorio.

## Capítulo 4 --- Testing Standards and

Conventions \## 68. Propósito

Este capítulo establece las reglas generales que deberán seguir todas
las pruebas automatizadas del proyecto.

Los estándares aquí definidos buscan evitar que la suite de pruebas se
convierta en un conjunto inconsistente de implementaciones personales.

Toda prueba deberá ser:

-   comprensible;
-   determinista;
-   aislada;
-   mantenible;
-   explícita;
-   proporcional al riesgo;
-   resistente a refactorizaciones internas;
-   útil como evidencia de comportamiento.

Una prueba no será considerada de calidad únicamente porque pase.

También deberá comunicar correctamente qué comportamiento protege.

## 69. Estándar de legibilidad

Una prueba deberá poder comprenderse sin necesidad de inspeccionar toda
la implementación interna.

El lector deberá identificar con claridad:

-   el escenario;
-   el estado inicial;
-   la acción ejecutada;
-   el resultado esperado;
-   la regla que se protege.

Ejemplo recomendado:

``` text
def test_archived_conversation_rejects_new_messages()
```

conversation = ConversationFactory status=ConversationStatus.ARCHIVED

``` text
with pytest.raises(ConversationArchivedError)
```

conversation.add_user_message("Nueva pregunta"

Ejemplo no recomendado:

``` text
def test_case_14()
```

item = create_item(2

``` text
with pytest.raises(Exception)
```

item.run("x"

El segundo ejemplo no comunica el dominio ni la intención.

## 70. Comportamiento sobre implementación

Las pruebas deberán validar resultados observables.

No deberán depender innecesariamente de:

-   métodos privados;
-   orden interno de llamadas;
-   variables internas;
-   estructura temporal de datos;
-   algoritmos específicos;
-   cantidad exacta de métodos auxiliares utilizados.

Ejemplo frágil:

mock_repository.save.assert_called_once_before(mock_event_bus.pu blish

Ese tipo de verificación solo será válido cuando el orden forme parte
del contrato real.

Ejemplo preferido:

stored = await repository.get(conversation.id

assert stored is not Non )

)

:

)

e

)

:

(

,

)

:

:

)

assert event_bus.contains(ConversationCreated(conversation.id)

## 71. Regla de intención explícita

Cada prueba deberá responder una pregunta concreta.

Ejemplos:

-   ¿Se rechaza un mensaje cuando la conversación está archivada?
-   ¿Se impide consultar documentos de otro tenant?
-   ¿Se solicita aprobación antes de ejecutar una acción destructiva?
-   ¿Se publica el evento después de guardar correctamente?
-   ¿Se conserva la idempotencia al reintentar un worker?

Las pruebas con múltiples intenciones deberán dividirse, salvo que
representen un único escenario indivisible.

## 72. Arrange--Act--Assert

La estructura recomendada será:

Arrang Ac Asser

Arrange

Prepara el estado mínimo necesario.

Act

Ejecuta una única acción principal.

Assert

Verifica el resultado observable.

Ejemplo:

``` text
def test_rejects_empty_conversation_title()
```

title = "

``` text
with pytest.raises(InvalidConversationTitleError)
```

ConversationTitle(title t

t

e

``` text
"
```

)

:

:

)

En este caso, la acción y la aserción se encuentran integradas porque se
espera una excepción.

## 73. Given--When--Then

Para escenarios de negocio complejos podrá utilizarse la estructura:

Give Whe The

Ejemplo:

``` text
def test_requires_approval_for_destructive_tool()
```

# Give

tool = ToolDefinitionFactory risk_level=ToolRiskLevel.DESTRUCTIVE

policy = ToolApprovalPolicy(

# Whe

decision = policy.evaluate(tool

# The

assert decision.requires_approval is Tru

No deberán mezclarse distintos estilos dentro de una misma prueba.

## 74. Estado mínimo necesario

Cada prueba deberá preparar únicamente el estado requerido para
demostrar su comportamiento.

Ejemplo excesivo:

conversation = ConversationBuilder().with_ten_messages().build(

Si el escenario únicamente valida el título, los mensajes son ruido
innecesario.

Ejemplo recomendado:

conversation = ConversationFactory(title="Incidente" n

n

)

n

n

n

n

)

(

)

e

,

:

)

)

Reducir el estado inicial mejora:

-   legibilidad;
-   velocidad;
-   aislamiento;
-   diagnóstico de fallas.

## 75. Valores relevantes visibles

Los valores esenciales para comprender el escenario deberán aparecer
directamente en la prueba.

Ejemplo recomendado:

limit = TokenLimit(4_000 requested_tokens = 4_00

``` text
with pytest.raises(TokenLimitExceededError)
```

limit.ensure_allowed(requested_tokens

No se deberá ocultar toda la intención detrás de factories genéricas.

Ejemplo menos claro:

``` text
with pytest.raises(TokenLimitExceededError)
```

TokenRequestFactory.invalid().validate(

Las factories pueden utilizarse, pero los valores que definen el límite
deberán ser visibles.

## 76. Reglas de aserción

Las aserciones deberán:

-   comparar resultados específicos;
-   evitar condiciones ambiguas;
-   producir mensajes útiles al fallar;
-   validar el contrato relevante;
-   evitar verificar detalles irrelevantes.

Ejemplo débil:

assert resul t

1

)

)

)

:

:

Ejemplo recomendado:

assert result.status is ApprovalStatus.PENDIN assert result.requested_by
== user_i

## 77. Igualdad de objetos de dominio

Los objetos de valor deberán implementar igualdad semántica.

Esto permitirá pruebas claras:

assert conversation.title == ConversationTitle("Incidente crítico"

No deberá ser necesario comparar manualmente cada propiedad de un objeto
de valor.

Las entidades deberán compararse por identidad cuando así lo defina el
modelo de dominio.

## 78. Colecciones

Cuando el orden no forme parte del contrato, las pruebas no deberán
asumirlo.

Ejemplo:

assert set(result.permissions) == Permission.READ_DOCUMENT
Permission.UPLOAD_DOCUMENT

Cuando el orden sí sea relevante, deberá veri carse explícitamente

assert result.messages == user_message assistant_message

## 79. Comparaciones numéricas

Para valores de punto flotante se utilizará tolerancia.

``` text
import pytes
}

]
```

)

t

,

,

``` text
[
```

,

fi ,

``` text
{
```

d

.

G

assert result.score == pytest.approx(0.85, abs=0.01

Esto aplica especialmente a:

-   métricas de similitud;
-   costos;
-   latencias agregadas;
-   puntuaciones de evaluación;
-   cálculos probabilísticos.

Los valores monetarios deberán utilizar representaciones exactas, como
Decimal, cuando corresponda.

## 80. Comparaciones temporales

Las pruebas no deberán depender de datetime.now() ejecutado en distintos
momentos.

Ejemplo incorrecto:

entity = service.create(

assert entity.created_at == datetime.now(

Ejemplo recomendado:

fixed_time = datetime 2026 7 22 12 0 tzinfo=timezone.utc

clock = FixedClock(fixed_time

entity = service.create(clock=clock

assert entity.created_at == fixed_tim

## 81. Testing de excepciones

Las pruebas deberán validar la excepción específica.

``` text
with pytest.raises(ConversationNotFoundError)
```

)

,

,

,

,

,

(

,

)

)

)

e

)

:

)

``` text
await handler.handle(command
```

No se utilizará:

``` text
with pytest.raises(Exception)
```

salvo en pruebas deliberadas de límites de infraestructura donde el tipo
concreto no sea controlado por la aplicación.

## 82. Mensajes y atributos de excepciones

Cuando una excepción forme parte del contrato, deberán validarse sus
atributos estructurados.

``` text
with pytest.raises(TenantAccessDeniedError) as error
```

policy.ensure_access actor_tenant_id="tenant-a"
resource_tenant_id="tenant-b"

assert error.value.actor_tenant_id == "tenant-a assert
error.value.resource_tenant_id == "tenant-b

No se dependerá exclusivamente del texto del mensaje si existen
atributos tipados.

## 83. Testing de códigos de error

Los errores expuestos por API deberán poseer códigos estables.

Ejemplo:

response = await client.post

``` text
"/conversations/missing/messages"
```

json={"content": "Hola"}

assert response.status_code == 40 assert
response.json()\["error"\]\["code"\] == "conversation_not_found

Los tests no deberán validar únicamente mensajes humanizados, ya que
estos pueden cambiar o traducirse. )

)

...

``` text
"
```

(

,

(

:

)

4

,

,

,

``` text
"

"
```

:

## 84. Testing de logs

Los logs deberán probarse cuando constituyan evidencia operacional
importante.

Casos recomendados:

-   denegación de autorización;
-   fallback de proveedor;
-   agotamiento de reintentos;
-   envío a dead-letter queue;
-   detección de comportamiento anómalo;
-   restauración después de una falla.

Ejemplo:

``` text
def test_logs_provider_fallback(caplog)
```

gateway = ModelGateway primary=FailingProvider()
fallback=SuccessfulProvider()

gateway.generate(request

assert "model_provider_fallback" in caplog.tex

No deberá probarse cada línea de logging ordinaria.

## 85. Logs estructurados

Cuando se utilicen logs estructurados, deberán verificarse los campos
relevantes.

assert log_record.event == "tool_execution_denied assert
log_record.tool_name =="delete_customer assert log_record.tenant_id ==
"tenant-001

No deberán registrarse:

-   prompts completos sensibles;
-   credenciales;
-   tokens de acceso;
-   documentos privados;
-   respuestas con información confidencial. )

(

)

,

,

:

``` text
"

"

"
```

t

Las pruebas de observabilidad deberán verificar también la ausencia de
datos sensibles cuando el riesgo lo justifique.

## 86. Testing de métricas

Las métricas deberán probarse cuando representen comportamientos
críticos.

Ejemplos:

-   incremento de intentos fallidos;
-   latencia de proveedor;
-   tokens consumidos;
-   herramientas ejecutadas;
-   solicitudes de aprobación;
-   fallbacks;
-   errores de recuperación;
-   mensajes enviados a DLQ.

Ejemplo conceptual:

before = metrics.counter_value

``` text
"tool_execution_total"
```

labels={"status": "denied"}

service.execute(request

after = metrics.counter_value

``` text
"tool_execution_total"
```

labels={"status": "denied"}

assert after == before +

## 87. Correlation y trace identifiers

Las pruebas de integración deberán verificar que los identificadores de
trazabilidad se propaguen entre componentes cuando corresponda.

response = await client.post

``` text
"/messages"
```

headers={"X-Correlation-ID": "corr-001"} json={"content": "Resume el
documento"} )

)

)

,

)

1

,

,

(

(

(

,

,

,

,

assert response.headers\["X-Correlation-ID"\] == "corr-001 assert
event_bus.last_event.correlation_id =="corr-001

## 88. Manejo del tiempo

El tiempo deberá abstraerse en reglas de negocio y procesos sensibles.

Casos obligatorios:

-   expiración de aprobaciones;
-   TTL de memoria;
-   retención de documentos;
-   ventanas de rate limiting;
-   vencimiento de sesiones;
-   reintentos programados;
-   timeouts;
-   períodos de gracia.

El uso directo del reloj será permitido únicamente en adapters de
infraestructura.

## 89. Zonas horarias

Las reglas internas utilizarán UTC.

Las pruebas deberán incluir escenarios relacionados con:

-   cambio de día;
-   fin de mes;
-   año bisiesto;
-   cambio de zona horaria;
-   horarios de verano cuando exista exposición al usuario;
-   fechas de expiración exactas.

Ejemplo:

expires_at = datetime 2026 7 23 0 0 tzinfo=timezone.utc )

,

,

,

,

,

(

,

``` text
"

"
```

approval = ApprovalRequestFactory(expires_at=expires_at

assert approval.is_expired at=datetime 2026 7 23 0 0 tzinfo=timezone.utc

La regla deberá definir claramente si el límite es inclusivo o
exclusivo.

## 90. Aleatoriedad

Toda aleatoriedad deberá ser controlable.

Esto incluye:

-   backoff con jitter;
-   selección de proveedor;
-   sampling;
-   generación de identificadores aleatorios;
-   orden aleatorio;
-   experimentos A/B.

Las pruebas deberán utilizar:

-   semillas fijas;
-   generadores inyectables;
-   respuestas predefinidas;
-   estrategias deterministas.

## 91. Identificadores

Los identificadores no deberán codificarse rígidamente en pruebas cuando
se generen dinámicamente.

Ejemplo:

result = await handler.handle(command )

)

,

,

,

,

,

(

(

,

)

)

assert result.conversation_id is not Non assert
id_generator.generated_ids == \[result.conversation_id

Cuando la identidad forme parte del escenario, deberá utilizarse un
generador fijo.

id_generator = FixedIdGenerator(\["conversation-001"\]

## 92. Reintentos

Las pruebas deberán validar:

-   cantidad máxima de intentos;
-   errores recuperables;
-   errores no recuperables;
-   tiempos de espera;
-   backoff;
-   jitter;
-   publicación de métricas;
-   envío a DLQ.

Ejemplo:

provider = FailingProvider failures= ProviderTimeoutError()
ProviderTimeoutError() ProviderResponse("ok")

result = await retrying_provider.generate(request

assert result.content == "ok assert provider.call_count ==

Las pruebas no deberán esperar tiempos reales prolongados.

El mecanismo de espera deberá abstraerse. )

``` text
]

[
```

(

``` text
"
```

3

,

,

,

e

)

)

``` text
]
```

## 93. Timeouts

Todo adapter externo deberá poseer pruebas de timeout.

provider = NeverRespondingProvider(

``` text
with pytest.raises(ModelProviderTimeoutError)
await gateway.generate
```

request timeout=Duration.seconds(5)

Las pruebas deberán simular el avance del tiempo o utilizar un transport
controlado.

## 94. Cancelación

Los procesos asíncronos deberán probar:

-   cancelación solicitada;
-   liberación de recursos;
-   estado final;
-   transacciones incompletas;
-   mensajes parcialmente procesados;
-   ausencia de efectos secundarios posteriores.

Esto será especialmente importante para:

-   streaming;
-   workers;
-   ingestión;
-   generación larga;
-   ejecución de herramientas.

## 95. Idempotencia

Toda operación reintentable deberá demostrar idempotencia.

Ejemplo:

command = ProcessDocumentCommand document_id="document-001"
idempotency_key="process-document-001" )

)

,

(

,

(

,

)

,

:

first_result = await handler.handle(command second_result = await
handler.handle(command

assert first_result.job_id == second_result.job_i assert
embedding_gateway.call_count ==

## 96. Concurrencia

Las pruebas deberán cubrir condiciones de carrera relevantes.

Casos iniciales:

-   dos aprobaciones simultáneas;
-   dos workers procesando el mismo mensaje;
-   actualización concurrente de conversación;
-   consumo concurrente de cuota;
-   ingestión duplicada;
-   creación repetida con la misma idempotency key.

No deberá asumirse que una prueba secuencial demuestra seguridad
concurrente.

## 97. Flaky Tests

Una prueba flaky es aquella que puede pasar o fallar sin cambios
relevantes en el código.

Las causas comunes incluyen:

-   dependencia temporal;
-   carreras;
-   infraestructura compartida;
-   orden de ejecución;
-   red externa;
-   datos aleatorios;
-   recursos insuficientes;
-   aserciones sobre latencia demasiado rígidas;
-   proveedores no deterministas.

Una prueba flaky será considerada un defecto de ingeniería. 1

)

)

d

## 98. Política contra flakiness

Cuando una prueba presente comportamiento intermitente:

## 1. deberá registrarse;

## 2. deberá investigarse;

## 3. no deberá ignorarse indefinidamente;

## 4. no deberá solucionarse agregando reintentos arbitrarios;

## 5. deberá corregirse su causa raíz.

Las pruebas podrán ponerse temporalmente en cuarentena únicamente
cuando:

-   exista un issue;
-   tenga un responsable;
-   exista una fecha objetivo;
-   no oculte un riesgo crítico.

## 99. Reintentos de pruebas

No se utilizarán plugins de reintento como sustituto de estabilidad.

Los reintentos automáticos podrán utilizarse únicamente:

-   en evaluaciones contra proveedores externos;
-   en ambientes de red controlada;
-   para recopilar evidencia adicional;
-   cuando la naturaleza probabilística esté documentada.

Una prueba funcional determinista no deberá necesitar reintentos.

## 100. Cobertura de código

La cobertura será una señal, no el objetivo principal.

Se medirán:

-   cobertura de líneas;
-   cobertura de ramas;
-   módulos no ejecutados;
-   cambios sin cobertura;
-   tendencias por dominio.

No se aceptará utilizar cobertura para justificar pruebas triviales sin
valor.

## 101. Umbral inicial de cobertura

Como punto de partida:

Cobertura mínima Área inicial Domain 95% Application 90% Shared Core 90%
Infrastructure 80% Adapters API Layer 80% Proyecto global 85%

Estos porcentajes podrán ajustarse según evidencia.

Los componentes críticos podrán requerir cobertura superior.

## 102. Cobertura de ramas

La cobertura de ramas tendrá mayor importancia en:

-   autorización;
-   políticas;
-   aprobación;
-   retries;
-   fallbacks;
-   reglas de tenant;
-   límites;
-   validaciones;
-   manejo de errores.

Ejemplo:

if tool.is_destructive and not approval.exists

``` text
raise ApprovalRequiredError(
```

No será suficiente probar únicamente el camino permitido.

También deberá probarse el rechazo. )

:

## 103. Cobertura diferencial

Cada Pull Request deberá mantener o mejorar la cobertura del código
modificado.

Un cambio no deberá aprobarse cuando agregue lógica significativa sin
pruebas correspondientes, aunque el promedio global permanezca por
encima del umbral.

## 104. Mutation Testing

Mutation testing se utilizará para evaluar si las pruebas realmente
detectan cambios defectuosos.

Ejemplos de mutaciones:

-   cambiar \> por \>=;
-   invertir condiciones;
-   eliminar validaciones;
-   alterar valores de retorno;
-   omitir excepciones;
-   modificar límites.

Una mutación sobreviviente puede indicar:

-   prueba ausente;
-   aserción débil;
-   código muerto;
-   comportamiento no especificado.

## 105. Alcance de Mutation Testing

No se ejecutará necesariamente en cada commit.

Inicialmente se aplicará a:

-   reglas de dominio críticas;
-   autorización;
-   approval policies;
-   cálculo de cuotas;
-   idempotencia;
-   selección de tools;
-   validación de citas.

Podrá ejecutarse:

-   de forma programada;
-   antes de releases;
-   sobre módulos modificados;
-   durante hardening.

## 106. Mocks

Los mocks deberán limitarse a boundaries claros.

Casos apropiados:

-   verificar que se publicó un comando externo;
-   validar llamada a un puerto;
-   simular una falla específica;
-   controlar una respuesta difícil de producir;
-   impedir comunicación externa.

No deberán utilizarse para sustituir entidades de dominio simples.

## 107. Mocking de detalles internos

No se deberá mockear:

-   métodos privados;
-   funciones auxiliares internas;
-   constructores de entidades;
-   lógica pura;
-   propiedades simples.

Ejemplo frágil:

mocker.patch.object handler

``` text
"_build_prompt"
```

return_value="prompt"

Si \_build_prompt necesita probarse separadamente, deberá extraerse a un
componente con responsabilidad clara. )

,

,

(

,

## 108. Over-Mocking

Síntomas de over-mocking:

-   pruebas con más preparación que lógica;
-   muchos assert_called_once_with
-   fallas frecuentes después de refactorizar;
-   pruebas que pasan aunque el flujo real no funcione;
-   duplicación del código productivo dentro de expectativas.

En estos casos se preferirán fakes o pruebas de integración delimitadas.

## 109. Uso de snapshots

Los snapshots serán adecuados cuando el contenido sea:

-   estructurado;
-   estable;
-   legible en revisión;
-   difícil de comparar manualmente;
-   relevante como contrato.

No serán adecuados cuando:

-   el contenido sea altamente dinámico;
-   incluya timestamps no normalizados;
-   provenga de un LLM no determinista;
-   sea demasiado grande;
-   nadie revise sus cambios.

## 110. Pruebas lentas

Toda prueba marcada como slow deberá justificar su costo.

Causas aceptables:

-   infraestructura real;
-   procesamiento de archivos;
-   evaluación de dataset;
-   navegador;
-   concurrencia;
-   performance;
-   proveedor real. ;

No será aceptable que una prueba sea lenta debido a:

-   sleep
-   creación repetida innecesaria de contenedores;
-   datasets sobredimensionados;
-   configuración deficiente;
-   dependencia accidental de red.

## 111. Uso de sleep

Se prohíbe utilizar time.sleep() o asyncio.sleep() para sincronizar
pruebas ordinarias.

Ejemplo incorrecto:

worker.start(

``` text
await asyncio.sleep(3
```

assert job.status == "completed Ejemplo recomendado:

worker.start(

``` text
await completion_event.wait(timeout=3
```

assert job.status == "completed

Los sleeps podrán utilizarse únicamente en pruebas explícitas de tiempo
real o rendimiento, con justificación.

## 112. Orden de ejecución

La suite deberá pasar:

-   en orden normal;
-   en orden aleatorio;
-   individualmente;
-   en paralelo;
-   como parte del conjunto completo.

Podrán utilizarse ejecuciones aleatorizadas programadas para detectar
dependencias ocultas. ;

)

)

)

``` text
"

"
```

)

## 113. Cleanup

Toda prueba que cree recursos deberá garantizar su limpieza.

Esto incluye:

-   archivos;
-   objetos en storage;
-   claves Redis;
-   conexiones;
-   procesos;
-   tareas asíncronas;
-   schemas;
-   registros;
-   contenedores.

La limpieza deberá ejecutarse incluso cuando la prueba falle.

Las fixtures con yield serán el mecanismo preferido.

## 114. Credenciales de prueba

Las pruebas utilizarán credenciales falsas o secretos efímeros.

No deberán contener:

-   API keys productivas;
-   contraseñas reales;
-   tokens personales;
-   certificados privados;
-   URLs internas sensibles.

Los secret scanners deberán ejecutarse también sobre los directorios de
pruebas.

## 115. Configuración de entornos de prueba

La configuración de testing deberá estar explícitamente separada.

Ejemplo:

APP_ENV=tes DATABASE_URL=postgresql+asyncpg://.. t

.

REDIS_URL=redis://.. MODEL_PROVIDER=fak OBJECT_STORAGE_PROVIDER=memor

La aplicación deberá fallar de forma segura si intenta utilizar
accidentalmente recursos productivos durante pruebas.

## 116. Protección contra recursos productivos

Antes de ejecutar migraciones, truncados o limpiezas, las fixtures
deberán validar que el recurso corresponde a un ambiente de prueba.

Ejemplo conceptual:

if database_name.endswith("\_test") is False

``` text
raise UnsafeTestDatabaseError(database_name
```

La protección deberá existir en más de una capa cuando el riesgo sea
alto.

## 117. Revisión de pruebas en Pull Requests

Todo Pull Request deberá responder:

-   ¿Qué comportamiento nuevo se agregó?
-   ¿Qué pruebas lo demuestran?
-   ¿Qué regresión se evita?
-   ¿Se introdujo flakiness?
-   ¿Se agregaron dependencias externas?
-   ¿Cambió algún dataset?
-   ¿Cambió algún threshold?
-   ¿Se modificaron snapshots?
-   ¿Se agregaron excepciones a coverage?
-   ¿Se afecta la duración del pipeline?

## 118. Criterios de rechazo en revisión

Una prueba deberá rechazarse cuando:

-   no tenga intención clara;
-   dependa del orden;
-   utilice sleeps arbitrarios;
-   use producción; e

.

y

:

)

-   compare resultados vagos;
-   duplique implementación;
-   esté excesivamente mockeada;
-   no proteja una regla real;
-   introduzca datos sensibles;
-   sea flaky;
-   incremente significativamente el tiempo sin justificación.

## 119. Definition of Done del capítulo

Los estándares de testing se considerarán adoptados cuando:

-   estén documentados en el repositorio;
-   exista configuración común;
-   la suite aplique reloj e identificadores controlables;
-   los Pull Requests incluyan revisión de pruebas;
-   se mida cobertura diferencial;
-   exista política de flaky tests;
-   se hayan definido reglas de mocks;
-   no existan sleeps arbitrarios;
-   los entornos productivos estén protegidos;
-   los primeros módulos cumplan estas convenciones.

## Capítulo 5 --- Unit Testing

## 120. Propósito

Los Unit Tests validan unidades pequeñas de comportamiento de manera
rápida, aislada y determinista.

Su propósito es proporcionar retroalimentación inmediata sobre
componentes cuya lógica puede verificarse sin infraestructura real.

Los Unit Tests constituirán la base más numerosa de la pirámide de
calidad.

## 121. Definición de unidad

Una unidad no será definida necesariamente como una sola función o
clase.

Una unidad será el conjunto más pequeño de comportamiento que pueda
validarse de forma útil y aislada.

Puede ser:

-   una función;
-   un objeto de valor;
-   una estrategia;
-   un parser;
-   un mapper;
-   una política simple;
-   un adapter pequeño;
-   un conjunto cohesionado de colaboradores en memoria.

No se dividirá artificialmente una prueba para perseguir aislamiento
extremo.

## 122. Características obligatorias

Un Unit Test deberá ser:

-   rápido;

-   hermético;

-   determinista;

-   independiente;

-   ejecutable sin Docker;

-   ejecutable sin red;

-   ejecutable sin archivos persistentes;

-   ejecutable sin variables productivas.

Objetivo inicial:

La suite unitaria completa deberá ejecutarse en segundos.

## 123. Candidatos principales

Los Unit Tests serán apropiados para:

-   normalización de texto;
-   cálculo de tokens;
-   parsing de respuestas;
-   mapeo de errores;
-   generación de object keys;
-   validación de schemas;
-   políticas de reintento;
-   selección de configuración;
-   sanitización;
-   serialización;
-   deduplicación;
-   ranking simple;
-   cálculo de costos;
-   límites de cuota.

## 124. Funciones puras

Las funciones puras deberán probarse directamente.

Ejemplo:

``` text
def test_normalizes_repeated_whitespace()
```

result = normalize_text("Hola mundo`\n`{=tex}`\nGEEM`{=tex}"

assert result == "Hola mundo GEEM

También deberán probarse:

-   entrada vacía;
-   caracteres Unicode;
-   espacios extremos;
-   contenido muy largo; "

:

)

-   comportamiento idempotente.

## 125. Parsers

Los parsers deberán probar:

-   respuesta válida;
-   campos opcionales;
-   campos desconocidos;
-   estructura incompleta;
-   tipos inválidos;
-   contenido vacío;
-   límites;
-   compatibilidad de versiones.

Ejemplo:

``` text
def test_parses_tool_call_response()
```

payload =

``` text
"name": "search_documents"
"arguments":
"query": "política de retención"
}
```

result = ToolCallParser.parse(payload

assert result.name == "search_documents assert result.arguments ==

``` text
"query": "política de retención"
```

## 126. Mappers de proveedores

Los adapters de proveedores deberán aislar el formato externo del modelo
interno.

Ejemplo:

``` text
def test_maps_provider_usage_to_internal_usage()
```

provider_usage =

``` text
"input_tokens": 120
"output_tokens": 40
}

}

}
```

,

``` text
{

{

{
```

,

,

``` text
{
```

,

:

,

)

``` text
"
```

,

:

result = UsageMapper.from_provider(provider_usage

assert result.prompt_tokens == 12 assert result.completion_tokens == 4
assert result.total_tokens == 16

Las pruebas deberán incluir cambios y omisiones esperadas del proveedor.

## 127. Cálculo de costos

El cálculo de costos deberá ser determinista y utilizar precisión
adecuada.

``` text
from decimal import Decima

def test_calculates_model_request_cost()
```

pricing = ModelPricing input_per_million=Decimal("2.50")
output_per_million=Decimal("10.00")

usage = ModelUsage prompt_tokens=1_000_000 completion_tokens=100_000

assert pricing.calculate(usage) == Decimal("3.50"

Deberán probarse:

-   cero tokens;
-   límites altos;
-   redondeo;
-   cambio de tarifa;
-   modelos sin costo configurado;
-   moneda.

## 128. Token Estimator

El estimador de tokens deberá probar:

-   texto vacío;
-   texto corto; )

)

(

(

l

,

,

0

0

:

0

,

,

)

)

-   Unicode;
-   código;
-   JSON;
-   contenido multilingüe;
-   límites máximos;
-   diferencia permitida frente al tokenizer real.

Cuando se utilice una aproximación, deberá documentarse la tolerancia.

## 129. Chunking

El chunking deberá probar:

-   tamaño máximo;
-   overlap;
-   textos menores al límite;
-   textos exactamente en el límite;
-   textos superiores;
-   preservación de orden;
-   ausencia de pérdida;
-   ausencia de duplicación no intencional;
-   metadata por chunk.

Ejemplo:

``` text
def test_chunker_preserves_full_content()
```

text = "A" \* 25 chunker = TextChunker max_characters=100
overlap_characters=10

chunks = chunker.split(text

assert chunks\[0\].position == assert chunks\[-1\].position ==
len(chunks) - assert all(len(chunk.content) \<= 100 for chunk in chunks

La reconstrucción exacta deberá considerar el overlap. )

0

(

,

,

)

0

:

1

)

## 130. Sanitización

La sanitización deberá probar entradas maliciosas y límites.

Casos:

-   HTML;
-   scripts;
-   caracteres de control;
-   null bytes;
-   rutas;
-   nombres de archivo;
-   encabezados;
-   contenido Markdown;
-   texto bidireccional;
-   payloads excesivos.

No deberá asumirse que la sanitización de interfaz sustituye la
validación del backend.

## 131. File Key Builders

Los generadores de rutas de almacenamiento deberán evitar:

-   colisiones;
-   traversal;
-   caracteres inseguros;
-   mezcla de tenants;
-   exposición del nombre original;
-   claves no deterministas cuando deban ser idempotentes.

Ejemplo:

``` text
def test_object_key_contains_tenant_partition()
```

result = ObjectKeyBuilder.build tenant_id="tenant-001"
document_id="document-001" filename="../../policy.pdf"

assert result.startswith("tenants/tenant-001/documents/ document-001/"
assert ".." not in resul )

)

t

,

,

,

(

:

## 132. Retry Policies

Las políticas de retry deberán probar:

-   errores recuperables;
-   errores definitivos;
-   intento máximo;
-   backoff;
-   límite acumulado;
-   respeto a Retry-After;
-   cancelación.

La política podrá probarse sin ejecutar esperas reales.

## 133. Circuit Breaker

Cuando se implemente un circuit breaker, sus estados deberán probarse:

Close ↓ failure Ope ↓ timeou Half-Ope ↓ succes Close

Casos:

-   apertura después del threshold;
-   rechazo mientras está abierto;
-   transición a half-open;
-   cierre después de éxito;
-   reapertura después de falla.

## 134. Rate Limit Algorithms

Los algoritmos de rate limiting deberán probar:

-   capacidad inicial;
-   consumo;
-   refill;
-   rechazo;
-   límites por tenant; n

d

d

n

t

s

s

-   límites por usuario;
-   concurrencia;
-   expiración de ventana.

La prueba del algoritmo podrá ser unitaria; la integración con Redis
pertenecerá a otra suite.

## 135. Serialización

La serialización deberá probar:

-   round-trip;
-   campos obligatorios;
-   campos opcionales;
-   enums;
-   fechas;
-   UUIDs;
-   decimals;
-   compatibilidad de versión;
-   campos desconocidos.

Ejemplo:

``` text
def test_domain_event_round_trip()
```

event = ConversationCreated conversation_id="conversation-001"
tenant_id="tenant-001"

payload = serializer.serialize(event restored =
serializer.deserialize(payload

assert restored == even

## 136. Configuración

La lógica de resolución de configuración deberá probar:

-   valores predeterminados;
-   override por ambiente;
-   ausencia de requeridos;
-   tipos inválidos;
-   combinaciones incompatibles; )

t

,

(

:

)

,

)

-   secretos faltantes;
-   restricciones de producción.

Las pruebas no deberán leer archivos personales del desarrollador.

## 137. Feature Flags

Las políticas de feature flags deberán probar:

-   flag habilitada;
-   flag deshabilitada;
-   rollout porcentual;
-   segmentación;
-   tenant específico;
-   fallback;
-   ausencia de configuración.

La asignación porcentual deberá ser estable para una misma identidad
cuando esa sea la política.

## 138. Prompt Rendering determinista

El renderizado de prompts podrá probarse unitariamente cuando no
intervenga un modelo.

Casos:

-   variables completas;
-   variables faltantes;
-   escaping;
-   orden de secciones;
-   límites;
-   contexto vacío;
-   instrucciones opcionales.

Ejemplo:

``` text
def test_renders_system_prompt_with_tenant_policy()
```

prompt = renderer.render template="assistant-system-v1" variables=

``` text
"tenant_name": "GEEM"
"policy": "No revelar datos de otros tenants."
{
```

(

,

,

:

,

``` text
}
```

assert "GEEM" in promp assert "No revelar datos de otros tenants." in
promp

## 139. Tool Schema Generation

La generación de schemas de herramientas deberá probar:

-   tipos;
-   campos obligatorios;
-   descripciones;
-   enums;
-   arrays;
-   objetos anidados;
-   defaults;
-   restricciones.

El schema generado deberá ser válido conforme al estándar elegido.

## 140. Error Mapping

Los mappers de errores deberán traducir correctamente:

-   errores de dominio;
-   errores de aplicación;
-   errores de proveedor;
-   timeouts;
-   rate limits;
-   errores desconocidos.

Ejemplo:

``` text
def test_maps_rate_limit_error_to_retryable_application_error()
```

error = ProviderRateLimitError retry_after_seconds=30

result = map_provider_error(error

assert isinstance(result, RetryableModelError assert
result.retry_after_seconds == 3 )

)

,

t

,

(

)

0

)

t

:

## 141. Property-Based Testing unitario

Hypothesis será especialmente útil en:

-   normalizadores;
-   parsers;
-   generadores de identificadores;
-   serializers;
-   chunking;
-   sanitización;
-   validadores.

Ejemplo:

``` text
@given(st.text()
def test_serialization_preserves_valid_unicode(value: str)
```

payload = serializer.serialize({"value": value} restored =
serializer.deserialize(payload

assert restored\["value"\] == valu

## 142. Límites

Toda unidad con límites deberá probar:

-   valor mínimo;
-   valor inmediatamente inferior;
-   valor exacto;
-   valor inmediatamente superior;
-   valor máximo;
-   overflow cuando corresponda.

Este patrón será obligatorio en:

-   tokens;
-   cuotas;
-   tamaño de archivos;
-   cantidad de tools;
-   longitud de prompts;
-   reintentos;
-   resultados recuperados. )

e

)

)

:

## 143. Casos vacíos

Los casos vacíos deberán considerarse explícitamente.

Ejemplos:

-   lista sin documentos;
-   conversación sin mensajes;
-   resultado sin citas;
-   tool registry vacío;
-   memoria vacía;
-   respuesta sin contenido;
-   dataset sin casos.

El comportamiento esperado deberá formar parte del contrato.

## 144. Unit Tests del frontend

Vitest y React Testing Library se utilizarán para:

-   funciones utilitarias;
-   hooks;
-   reducers;
-   formateadores;
-   validaciones;
-   componentes aislados;
-   estados de carga;
-   errores;
-   permisos.

Las pruebas deberán interactuar con componentes como lo haría el
usuario.

No deberán depender de detalles internos de React.

## 145. Consultas accesibles

React Testing Library deberá preferir:

## 1. getByRole

## 2. getByLabelText

## 3. getByText

## 4. getByTestId como último recurso.

;

;

;

Ejemplo:

render(`<ApprovalButton />`{=html})

``` text
await user.click
```

screen.getByRole("button", name: "Aprobar acción"

``` text
})
```

)

expect screen.getByText("Acción aprobada") ).toBeVisible()

## 146. Qué no debe probarse unitariamente

No deberán escribirse Unit Tests directos para:

-   comportamiento interno de FastAPI;
-   funcionalidad propia de SQLAlchemy;
-   implementación interna de Redis;
-   librerías estándar;
-   frameworks externos;
-   detalles triviales sin lógica;
-   getters y setters sin comportamiento.

El proyecto deberá probar su integración con estas herramientas, no
volver a probar las herramientas mismas.

## 147. Anti-patterns de Unit Testing

Tests excesivamente pequeños

Una prueba por cada línea o método trivial.

Mock Everything

Todos los colaboradores sustituidos sin necesidad.

White-box Testing

Dependencia de métodos internos. ;

,

(

;

(

,

;

``` text
{
```

,

Assertion-Free Test

La prueba ejecuta código, pero no demuestra comportamiento.

Duplicate Implementation

La prueba repite el algoritmo para calcular el resultado.

Magic Data

Valores sin significado.

Shared Mutable Fixture

Estado global compartido.

## 148. Checklist de Unit Testing

Antes de aprobar un Unit Test deberá verificarse:

-   ¿Es realmente una unidad útil?
-   ¿Es hermético?
-   ¿Es determinista?
-   ¿Se ejecuta rápidamente?
-   ¿El nombre explica el comportamiento?
-   ¿Los límites están cubiertos?
-   ¿Se validan errores?
-   ¿Evita detalles internos?
-   ¿Los mocks son necesarios?
-   ¿La prueba fallaría si la regla se rompe?

## 149. Definition of Done del capítulo

Unit Testing se considerará correctamente implementado cuando:

-   exista suite unitaria independiente;

-   no requiera infraestructura;

-   se ejecute en segundos;

-   cubra utilidades y políticas relevantes;

-   incluya property-based testing donde aporte valor;

-   tenga cobertura diferencial;

-   no dependa del orden;

-   no utilice red;

-   no contenga mocks innecesarios;

-   forme parte del primer quality gate.

## Capítulo 6 --- Domain Testing

## 150. Propósito

Los Domain Tests validan las reglas centrales del negocio sin depender
de frameworks ni infraestructura.

Su objetivo es demostrar que el modelo de dominio:

-   protege invariantes;
-   rechaza estados inválidos;
-   permite transiciones válidas;
-   genera eventos correctos;
-   aplica políticas;
-   conserva consistencia.

El dominio representa el conocimiento más importante del producto.

Por ello, sus pruebas tendrán uno de los niveles de cobertura y rigor
más altos del proyecto.

## 151. Alcance

Los Domain Tests cubrirán:

-   entidades;
-   agregados;
-   objetos de valor;
-   servicios de dominio;
-   políticas;
-   especificaciones;
-   eventos;
-   excepciones;
-   estados;
-   transiciones;
-   invariantes;
-   reglas multi-tenant expresadas en dominio;
-   restricciones de approval y tools.

## 152. Independencia de infraestructura

El dominio no deberá depender de:

-   FastAPI;
-   Pydantic utilizado como DTO externo;
-   SQLAlchemy;
-   Redis;
-   HTTP;
-   JSON del proveedor;
-   OpenAI SDK;
-   colas;
-   sistema de archivos;
-   variables de entorno.

Si una regla de dominio requiere uno de estos elementos, deberá
expresarse mediante información o abstracciones apropiadas.

## 153. Entidades

Las entidades deberán probar:

-   creación válida;
-   creación inválida;
-   identidad;
-   comportamiento;
-   cambios de estado;
-   protección de invariantes;
-   eventos generados.

Ejemplo:

``` text
def test_creates_active_conversation()
```

conversation = Conversation.create
conversation_id=ConversationId("conversation-001")
tenant_id=TenantId("tenant-001") owner_id=UserId("user-001")
title=ConversationTitle("Incidente")

assert conversation.status is ConversationStatus.ACTIV assert
conversation.message_count == )

,

(

:

,

0

,

E

,

## 154. Creación inválida

Toda entidad deberá rechazar estados iniciales inválidos.

``` text
@pytest.mark.parametrize
"title"

""
" "
"\n"
]

def test_rejects_blank_conversation_title(title)
with pytest.raises(InvalidConversationTitleError)
```

ConversationTitle(title

No deberán crearse entidades inválidas para validarlas después.

## 155. Objetos de valor

Los objetos de valor deberán probar:

-   validación;
-   normalización;
-   igualdad;
-   inmutabilidad;
-   representación;
-   límites.

Ejemplo:

``` text
def test_conversation_title_normalizes_whitespace()
```

title = ConversationTitle

``` text
" Incidente    crítico "
```

assert title.value == "Incidente crítico

## 156. Inmutabilidad

Cuando un objeto de valor sea inmutable, la prueba deberá demostrarlo
mediante su diseño o implementación. )

)

``` text
[
```

,

,

,

,

,

(

(

)

,

``` text
"
```

:

:

:

No deberá permitirse:

title.value = "Otro título

La inmutabilidad evita cambios no controlados dentro del agregado.

## 157. Agregados

Los agregados deberán probar:

-   boundary;
-   invariantes internas;
-   modificaciones mediante root;
-   consistencia entre entidades;
-   eventos;
-   límites de tamaño cuando existan.

Ejemplo:

``` text
def test_adds_message_through_conversation_root()
```

conversation = ConversationFactory(

message = conversation.add_user_message
message_id=MessageId("message-001") content=MessageContent("Hola")

assert message in conversation.message assert conversation.message_count
==

## 158. Invariantes

Cada invariante deberá poseer pruebas positivas y negativas.

Ejemplo de invariante:

Una conversación archivada no acepta mensajes nuevos.

Prueba negativa:

``` text
def test_archived_conversation_rejects_new_message()
```

conversation = ConversationFactory status=ConversationStatus.ARCHIVED )

)

"

(

,

)

1

,

s

(

,

:

:

``` text
with pytest.raises(ConversationArchivedError)
```

conversation.add_user_message message_id=MessageId("message-001")
content=MessageContent("Hola")

Prueba positiva:

``` text
def test_active_conversation_accepts_new_message()
```

conversation = ConversationFactory status=ConversationStatus.ACTIVE

conversation.add_user_message message_id=MessageId("message-001")
content=MessageContent("Hola")

assert conversation.message_count ==

## 159. Transiciones de estado

Toda máquina de estados deberá probar:

-   transición permitida;
-   transición prohibida;
-   transición idempotente;
-   estado final;
-   eventos;
-   metadata asociada.

Ejemplo:

PENDIN

``` text
├── approve → APPROVE
├── reject → REJECTE
└── expire → EXPIRE
```

Una solicitud aprobada no deberá poder rechazarse posteriormente. )

)

G

)

D

D

D

(

(

,

(

,

1

,

,

,

:

:

## 160. Approval Request

La entidad ApprovalRequest deberá probar al menos:

-   creación pendiente;
-   aprobación;
-   rechazo;
-   expiración;
-   identidad del aprobador;
-   motivo;
-   timestamp;
-   doble aprobación;
-   aprobación por usuario no autorizado;
-   acción posterior a expiración.

Ejemplo:

``` text
def test_approves_pending_request()
```

approval = ApprovalRequestFactory status=ApprovalStatus.PENDING

approval.approve approved_by=UserId("user-002") approved_at=FIXED_TIME

assert approval.status is ApprovalStatus.APPROVE assert
approval.decided_by == UserId("user-002"

## 161. Expiración de aprobaciones

La expiración deberá depender de un tiempo explícito.

``` text
def test_pending_approval_expires_at_deadline()
```

approval = ApprovalRequestFactory status=ApprovalStatus.PENDING
expires_at=FIXED_TIME

approval.expire(at=FIXED_TIME

assert approval.status is ApprovalStatus.EXPIRE

La regla deberá indicar claramente si expira exactamente al alcanzar el
deadline. )

)

)

(

,

,

)

:

,

(

,

(

,

:

)

D

D

## 162. Tool Definition

La entidad o agregado de Tool deberá probar:

-   nombre válido;
-   schema válido;
-   riesgo;
-   permisos requeridos;
-   necesidad de aprobación;
-   habilitación;
-   versión;
-   tenant scope;
-   idempotencia;
-   timeout.

Ejemplo:

``` text
def test_destructive_tool_requires_approval()
```

tool = ToolDefinition.create name=ToolName("delete_customer")
risk_level=ToolRiskLevel.DESTRUCTIVE required_permissions=
Permission.DELETE_CUSTOMER

``` text
}
```

assert tool.requires_approval is Tru

## 163. Tool Execution Policy

La política de ejecución deberá evaluar:

-   herramienta habilitada;
-   permisos;
-   tenant;
-   riesgo;
-   aprobación;
-   límites;
-   contexto;
-   estado del recurso. )

,

``` text
{
```

(

,

,

e

,

:

Ejemplo:

``` text
def test_denies_tool_without_required_permission()
```

tool = ToolDefinitionFactory required_permissions=
Permission.DELETE_CUSTOMER

``` text
}
```

actor = ActorFactory permissions= Permission.READ_CUSTOMER

``` text
}
```

decision = ToolExecutionPolicy().evaluate tool=tool actor=actor
approval=None

assert decision.allowed is Fals assert decision.reason is
ToolDenialReason.MISSING_PERMISSIO

## 164. Tenant Isolation en dominio

Aunque el control principal exista también en infraestructura y RLS, las
reglas de dominio deberán impedir asociaciones inválidas.

Ejemplo:

``` text
def test_rejects_document_from_different_tenant()
```

conversation = ConversationFactory tenant_id=TenantId("tenant-a")

document = KnowledgeDocumentFactory tenant_id=TenantId("tenant-b")

``` text
with pytest.raises(CrossTenantReferenceError)
```

conversation.attach_document(document

La defensa deberá aplicarse en profundidad. )

)

)

)

)

,

,

,

,

``` text
{
```

,

(

``` text
{
```

(

N

e

,

,

,

(

,

(

(

)

:

:

:

## 165. Knowledge Document

La entidad de documento deberá probar:

-   creación;
-   metadata;
-   estado;
-   transición de ingestión;
-   fallo;
-   reintento;
-   archivado;
-   eliminación;
-   ownership;
-   checksum;
-   duplicados.

Ejemplo de estados:

UPLOADE ↓ PROCESSIN

``` text
├── success → READ
└── failure → FAILE
```

No deberá permitirse pasar directamente de UPLOADED a READY si el
procesamiento es obligatorio.

## 166. Duplicidad de documentos

La regla de duplicidad deberá definirse explícitamente.

Puede considerar:

-   checksum;
-   tenant;
-   fuente;
-   versión;
-   nombre;
-   contenido. D

G

Y

D

Prueba conceptual:

``` text
def test_same_checksum_is_duplicate_within_tenant()
```

policy = DocumentDuplicationPolicy(

result = policy.evaluate existing_checksum="sha256:abc"
incoming_checksum="sha256:abc" same_tenant=True

assert result.is_duplicate is Tru

El mismo checksum en distintos tenants no deberá producir una referencia
cruzada.

## 167. Chunks

Los chunks como entidades u objetos deberán probar:

-   pertenencia al documento;
-   posición;
-   contenido;
-   metadata;
-   límites;
-   embedding status;
-   tenant;
-   ausencia de posiciones duplicadas.

## 168. Conversation

La conversación deberá probar:

-   creación;
-   título;
-   ownership;
-   mensajes;
-   archivado;
-   reapertura si se permite;
-   límites;
-   adjuntos;
-   metadata;
-   eventos. )

,

(

e

,

,

)

:

La lógica no deberá quedar dispersa entre controladores y repositorios.

## 169. Messages

Los mensajes deberán probar:

-   rol;
-   contenido;
-   orden;
-   timestamp;
-   citations;
-   tool calls;
-   token usage;
-   finish reason;
-   estado de streaming;
-   tenant;
-   conversación.

No deberá permitirse un mensaje sin conversación válida cuando el modelo
lo requiera.

## 170. Mensajes incompletos por streaming

Cuando exista streaming, deberá definirse el comportamiento de mensajes
parciales.

Estados posibles:

PENDIN STREAMIN COMPLETE FAILE CANCELLE

Las transiciones y recuperación deberán probarse.

Ejemplo:

``` text
def test_cancelled_stream_cannot_be_completed()
```

message = AssistantMessageFactory status=MessageStatus.CANCELLED

``` text
with pytest.raises(InvalidMessageTransitionError)
```

message.complete )

D

G

D

D

G

(

(

,

:

:

content="Respuesta tardía"

## 171. Memory Entry

Las entradas de memoria deberán probar:

-   creación;
-   categoría;
-   relevancia;
-   procedencia;
-   tenant;
-   usuario;
-   expiración;
-   actualización;
-   eliminación;
-   sensibilidad.

La memoria no deberá convertirse en almacenamiento irrestricto de todo
el contenido conversacional.

## 172. Política de memoria

La política deberá probar:

-   qué información puede guardarse;
-   qué información no;
-   cuándo requiere consentimiento;
-   cuánto tiempo permanece;
-   qué tenant y usuario pueden verla;
-   qué información debe eliminarse.

Ejemplo:

``` text
def test_rejects_secret_as_memory()
```

candidate = MemoryCandidate content="API key: sk-test-secret"
classification=DataClassification.SECRET

decision = MemoryPolicy().evaluate(candidate

assert decision.allowed is Fals )

)

(

e

:

,

,

)

,

## 173. Domain Events

Los eventos de dominio deberán probar:

-   tipo;
-   datos;
-   identidad;
-   timestamp;
-   correlation;
-   causation;
-   generación única;
-   orden cuando sea relevante.

Ejemplo:

``` text
def test_archiving_conversation_records_event()
```

conversation = ConversationFactory(

conversation.archive(at=FIXED_TIME

assert conversation.pull_events() == ConversationArchived
conversation_id=conversation.id tenant_id=conversation.tenant_id
occurred_at=FIXED_TIME

## 174. Pull de eventos

La operación para obtener eventos deberá definir si:

-   conserva eventos;
-   los elimina;
-   los marca;
-   permite múltiples lecturas.

La decisión deberá probarse.

Ejemplo:

events = aggregate.pull_events(

assert len(events) == assert aggregate.pull_events() == \[

``` text
]
```

)

1

(

)

,

``` text
]
```

)

)

``` text
[
```

,

,

:

## 175. Servicios de dominio

Un servicio de dominio será apropiado cuando la regla:

-   involucre varios objetos;
-   no pertenezca naturalmente a una sola entidad;
-   represente conocimiento del negocio;
-   permanezca libre de infraestructura.

Ejemplos:

-   política de aprobación;
-   selección de nivel de riesgo;
-   evaluación de acceso;
-   deduplicación;
-   retención;
-   clasificación de memoria.

## 176. Specifications

Las especificaciones reutilizables deberán probar:

-   cumplimiento;
-   rechazo;
-   composición AND;
-   composición OR;
-   negación;
-   mensajes de fallo cuando existan.

Ejemplo conceptual:

specification = ToolIsEnabled( & ActorHasPermission( &
ApprovalExistsWhenRequired(

La composición no deberá cambiar silenciosamente el significado de las
reglas.

## 177. Políticas puras

Las políticas deberán recibir toda la información necesaria como
argumentos o modelos de contexto. )

(

)

)

)

No deberán:

-   consultar base de datos directamente;
-   leer variables globales;
-   llamar proveedores;
-   publicar eventos externos;
-   acceder al reloj real.

Esto permitirá probarlas de forma determinista.

## 178. Excepciones de dominio

Las excepciones deberán representar lenguaje del dominio.

Ejemplos:

-   ConversationArchivedError
-   ApprovalExpiredError
-   ToolPermissionDeniedError
-   CrossTenantReferenceError
-   DocumentAlreadyProcessingError
-   MemoryPolicyViolationError

No deberán lanzarse excepciones genéricas para reglas conocidas.

## 179. Mensajes de error

Los mensajes deberán ser útiles, pero el contrato se apoyará en:

-   tipo;
-   código;
-   atributos.

Ejemplo:

error = ToolPermissionDeniedError tool_name=ToolName("delete_customer")
missing_permissions= Permission.DELETE_CUSTOMER

``` text
}
```

assert error.code == "tool_permission_denied )

,

;

``` text
{
```

;

;

;

.

;

(

,

,

``` text
"
```

## 180. Factories de dominio

Las factories deberán construir estados válidos por defecto.

Para probar estados inválidos, deberá utilizarse la API pública que
produce el rechazo.

No se deberán fabricar entidades imposibles modificando atributos
internos salvo en pruebas de compatibilidad o recuperación claramente
justificadas.

## 181. Builders de escenarios

Los builders serán útiles para agregados complejos, pero deberán
utilizar métodos del dominio.

Ejemplo:

conversation = ConversationScenario( .created_by("user-001"
.with_user_message("Busca el contrato"
.with_assistant_tool_call("search_documents"
.with_tool_result("document-001" .build(

El builder no deberá saltarse invariantes.

## 182. Matrices de estados

Las entidades con múltiples transiciones deberán documentarse mediante
una matriz.

Ejemplo:

Estado actual Acción Estado resultante Permitida Pending Approve
Approved Sí Pending Reject Rejected Sí Pending Expire Expired Sí
Approved Reject --- No Rejected Approve --- No )

)

(

)

)

)

)

)

Expired Approve --- No

Cada fila deberá estar cubierta por pruebas o parametrización
equivalente.

## 183. Matrices de permisos

Las reglas de acceso deberán representarse mediante matrices.

Rol Leer Escribir Eliminar Aprobar Owner Sí Sí Sí Sí Admin Sí Sí Según
política Sí Member Sí Sí No No Viewer Sí No No No

Las matrices deberán convertirse en pruebas parametrizadas.

## 184. Límites del agregado

El tamaño del agregado deberá probarse cuando exista límite.

Ejemplo:

-   máximo de mensajes cargados;
-   máximo de tools asociadas;
-   máximo de adjuntos;
-   máximo de memoria activa.

La prueba deberá demostrar el comportamiento exacto al alcanzar y
exceder el límite.

## 185. Consistencia eventual

Cuando una regla no pueda garantizarse dentro del agregado y dependa de
consistencia eventual, deberá especificarse:

-   evento emitido;

-   proceso responsable;

-   estado intermedio;

-   recuperación;

-   idempotencia;

-   tiempo esperado.

Los Domain Tests validarán la emisión y el estado; las Integration Tests
validarán el proceso completo.

## 186. Domain Testing basado en propiedades

Hypothesis podrá utilizarse para invariantes universales.

Ejemplo:

``` text
@given
```

st.integers(min_value=0, max_value=100_000)

``` text
def test_quota_never_becomes_negative(consumption)
```

quota = TokenQuota(limit=100_000

result = quota.consume(consumption

assert result.remaining \>=

Cuando el consumo exceda el límite, la estrategia deberá esperar una
excepción o rechazo según el contrato.

## 187. Domain Testing y lenguaje ubicuo

Los nombres de pruebas deberán utilizar el lenguaje del dominio.

Preferido:

``` text
def test_expired_approval_cannot_authorize_tool_execution()
```

.. No recomendado:

``` text
def test_status_three_returns_false()
```

Las pruebas también forman parte de la documentación del dominio. )

...

.

(

0

)

:

)

,

:

:

## 188. Qué no pertenece a Domain Tests

No deberá probarse dentro de esta suite:

-   consultas SQL;
-   serialización HTTP;
-   códigos de estado;
-   Redis;
-   OpenAPI;
-   adapters de proveedores;
-   autenticación JWT;
-   estructura de tablas;
-   comportamiento del framework.

Estos elementos tendrán sus propias suites.

## 189. Anti-patterns de Domain Testing

Anemic Domain Tests

Solo verifican getters y creación, pero no reglas.

Persistence-Coupled Domain

Necesita guardar para validar comportamiento.

Framework Domain

Las entidades dependen de FastAPI o SQLAlchemy.

Invalid Factory State

La factory crea entidades imposibles.

Missing Negative Paths

Solo se prueba el camino exitoso.

Rule Duplication

La prueba vuelve a implementar la política.

Database as Domain Service

La regla depende directamente de consultas.

## 190. Checklist de Domain Testing

Cada agregado deberá responder:

-   ¿Cuáles son sus invariantes?
-   ¿Cuáles son sus estados?
-   ¿Qué transiciones permite?
-   ¿Qué transiciones rechaza?
-   ¿Qué eventos produce?
-   ¿Qué límites posee?
-   ¿Qué reglas de tenant aplica?
-   ¿Qué permisos intervienen?
-   ¿Qué operaciones son idempotentes?
-   ¿Qué comportamiento depende del tiempo?
-   ¿Qué escenarios concurrentes existen?

## 191. Definition of Done del capítulo

Domain Testing se considerará correctamente implementado cuando:

-   todas las invariantes críticas tengan pruebas;
-   las máquinas de estado tengan matrices;
-   los caminos positivos y negativos estén cubiertos;
-   el dominio no dependa de infraestructura;
-   los eventos estén validados;
-   las reglas de tenant estén protegidas;
-   las políticas de tools y approval tengan cobertura alta;
-   los límites estén probados;
-   los nombres utilicen lenguaje ubicuo;
-   la cobertura del dominio cumpla el umbral establecido.

## Capítulo 7 --- Application Testin

## 192. Propósit

Los Application Tests validan la coordinación de los casos de uso del
sistema sin depender de implementaciones reales de infraestructura

Su objetivo consiste en demostrar que la capa de aplicación

-   recibe solicitudes válidas
-   coordina correctamente el dominio
-   utiliza los puertos adecuados
-   respeta permisos y políticas
-   administra transacciones
-   produce resultados consistentes
-   publica eventos
-   maneja errores
-   garantiza idempotencia cuando corresponde Los Application Tests
    deberán veri car el comportamiento del sistema desde la perspectiva
    de un caso de uso, pero sin involucrar todavía HTTP, PostgreSQL,
    Redis o proveedores externos reales

## 193. Alcanc

Los Application Tests cubrirán

-   Commands
-   Queries
-   Command Handlers
-   Query Handlers
-   Application Services
-   DTOs internos
-   Puertos de entrada
-   Puertos de salida
-   Unit of Work
-   Repositorios en memoria
-   Event Bus en memoria
-   Authorization Services
-   Idempotency Services
-   Gateways falsos
-   Coordinación entre agregados
-   Manejo de errores de dominio e infraestructura abstracta .

.

.

.

.

;

;

.

.

.

e

.

.

.

o

.

.

.

;

;

.

;

;

.

:

;

fi ;

.

.

.

:

g

## 194. Diferencia frente a Domain Test

Los Domain Tests validan reglas internas del modelo

Los Application Tests validan la coordinación necesaria para ejecutar
una intención del usuario o del sistema

Ejemplo

Domain Tes

Una conversación archivada no puede recibir mensajes

Application Tes

El caso de uso SendMessage recupera la conversación, aplica la regla de
dominio, guarda el resultado y publica los eventos correspondientes

La capa de aplicación no deberá duplicar reglas del dominio

## 195. Diferencia frente a Integration Test

Los Application Tests utilizarán implementaciones en memoria o dobles
controlados

No deberán validar

-   consultas SQL
-   con guración de Redis
-   serialización HTTP
-   conectividad de red
-   comportamiento real de proveedores
-   estructura física de tablas Estos elementos pertenecen a otras
    suites

## 196. Command

Un Command representa una intención de modi car el estado del sistema

Ejemplos fi :

:

.

;

t

:

t

;

;

;

s

.

;

.

fi .

.

.

s

.

s

.

.

-   CreateConversationCommand

-   SendMessageCommand

-   UploadDocumentCommand

-   ApproveToolExecutionCommand

-   DeleteMemoryEntryCommand

-   ArchiveConversationCommand Los Commands deberán ser

-   inmutables

-   tipados

-   explícitos

-   libres de lógica de infraestructura

-   su cientes para ejecutar el caso de uso Ejemplo conceptual

``` text
from dataclasses import dataclas

@dataclass(frozen=True
class CreateConversationCommand
```

tenant_id: st actor_id: st title: st idempotency_key: str \| None = Non

## 197. Querie

Una Query representa una solicitud de lectura sin intención de modi car
el estado funcional

Ejemplos

-   GetConversationQuery
-   ListConversationsQuery
-   SearchKnowledgeQuery
-   GetApprovalRequestQuery
-   ListMemoryEntriesQuery Una Query podrá generar actividad técnica,
    como métricas o logs, pero no deberá alterar el estado de negocio

## 198. Command Handler

Cada Command Handler deberá coordinar una responsabilidad principal fi ;

:

;

;

.

s

r

:

r

r

.

:

.

.

.

)

.

.

;

.

.

.

.

s

.

.

:

s

e

fi .

.

Ejemplo

``` text
class CreateConversationHandler
def __init__
```

self repository: ConversationRepository unit_of_work: UnitOfWork
id_generator: IdGenerator clock: Clock ) -\> None self.\_repository =
repositor self.\_unit_of_work = unit_of_wor self.\_id_generator =
id_generato self.\_clock = cloc

``` text
async def handle
```

self command: CreateConversationCommand ) -\> CreateConversationResult
conversation = Conversation.create
conversation_id=self.\_id_generator.next_id()
tenant_id=TenantId(command.tenant_id) owner_id=UserId(command.actor_id)
title=ConversationTitle(command.title) created_at=self.\_clock.now()

``` text
await self._repository.add(conversation
await self._unit_of_work.commit(

return CreateConversationResult
```

conversation_id=str(conversation.id)

El handler no deberá contener reglas de dominio duplicadas

## 199. Query Handler

Los Query Handlers podrán utilizar modelos de lectura optimizados

No será obligatorio reconstruir agregados cuando la operación sea
exclusivamente de consulta

Ejemplo

``` text
class ListConversationsHandler
```

:

:

)

)

,

,

:

(

(

,

s

k

:

:

,

:

,

y

(

.

)

,

r

k

(

,

,

,

.

)

,

,

,

,

.

``` text
def __init__
```

self query_service: ConversationQueryService ) -\> None
self.\_query_service = query_servic

``` text
async def handle
```

self query: ListConversationsQuery ) -\> ConversationPage

``` text
return await self._query_service.list_for_user
```

tenant_id=query.tenant_id user_id=query.actor_id cursor=query.cursor
limit=query.limit

## 200. Prueba básica de un Command Handle

Una prueba deberá validar

-   resultado
-   estado persistido
-   commit
-   eventos
-   efectos secundarios relevantes Ejemplo

``` text
@pytest.mark.asynci
async def test_creates_conversation()
```

repository = InMemoryConversationRepository( unit_of_work =
FakeUnitOfWork( id_generator = FixedIdGenerator

``` text
["conversation-001"]
```

clock = FixedClock(FIXED_TIME

handler = CreateConversationHandler repository=repository
unit_of_work=unit_of_work id_generator=id_generator clock=clock

result = await handler.handle )

)

;

;

:

;

)

;

,

,

:

(

:

,

o

(

.

:

,

,

,

,

(

,

,

)

)

,

(

:

,

,

(

e

r

,

)

(

CreateConversationCommand tenant_id="tenant-001" actor_id="user-001"
title="Incidente crítico"

conversation = await repository.get ConversationId("conversation-001")

assert result.conversation_id == "conversation-001 assert conversation
is not Non assert conversation.title == ConversationTitle

``` text
"Incidente crítico"
```

assert unit_of_work.committed is Tru

## 201. Estado observabl

Los tests deberán validar el resultado nal y no únicamente interacciones

No será su ciente

repository.add.assert_called_once( Cuando sea posible, deberá veri carse
el estado almacenado

stored = await repository.get(conversation_id

assert stored is not Non assert stored.owner_id == UserId("user-001" Los
spies serán útiles para efectos secundarios que no produzcan un estado
consultable

## 202. Puertos de salid

La capa de aplicación dependerá de interfaces para

-   repositorios
-   Unit of Work
-   Model Gateway
-   Embedding Gateway
-   Object Storage
-   Event Publisher )

)

)

fi ;

)

;

;

;

;

:

;

fi a

e

e

fi ,

,

(

:

)

,

e

,

(

e

:

,

)

)

.

(

``` text
"
```

.

-   Queue Publisher
-   Authorization
-   Idempotency Store
-   Noti cation Service
-   Audit Service Los Application Tests utilizarán fakes que implementen
    dichos contratos

## 203. Repositorios en memori

Los repositorios en memoria deberán reproducir la semántica esencial del
contrato

Ejemplo

``` text
class InMemoryConversationRepository
def __init__(self) -> None
```

self.items: dict ConversationId Conversation

``` text
] = {

async def add
```

self conversation: Conversation ) -\> None if conversation.id in
self.items

``` text
raise ConversationAlreadyExistsError
```

conversation.id

self.items\[conversation.id\] = deepcopy conversation

``` text
async def get
```

self conversation_id: ConversationId ) -\> Conversation \| None
conversation = self.items.get conversation_id

``` text
return deepcopy(conversation
```

El uso de copias podrá evitar que una prueba pase por referencias
compartidas que no existirían con persistencia real fi :

)

)

.

;

;

,

)

,

;

:

``` text
}
```

;

.

(

(

,

,

``` text
[
```

,

,

:

:

a

,

,

:

)

(

,

:

(

(

.

.

## 204. Contrato entre repositorios falsos y reale

Los repositorios falsos deberán respetar

-   mismos tipos de entrada

-   mismos resultados

-   mismos casos de ausencia

-   mismas reglas de duplicidad

-   comportamiento equivalente de ltros

-   semántica de tenant

-   orden y paginación documentados Cuando sea posible, una suite de
    contrato común deberá ejecutarse sobre

-   implementación en memoria

-   implementación PostgreSQL

## 205. Fake Unit of Wor

El FakeUnitOfWork deberá registrar

-   commits
-   rollbacks
-   eventos pendientes
-   transacciones iniciadas
-   estado nal Ejemplo

``` text
class FakeUnitOfWork
def __init__(self) -> None
```

self.committed = Fals self.rolled_back = Fals

``` text
async def commit(self) -> None
```

self.committed = Tru

``` text
async def rollback(self) -> None
```

self.rolled_back = Tru Para escenarios avanzados podrá implementar
snapshots del estado en memoria

## 206. Semántica transacciona

fi :

;

;

.

;

;

;

;

;

;

;

;

.

:

fi .

k

;

:

:

e

e

e

:

l

e

:

:

s

:

.

Los Application Tests deberán demostrar

-   commit después del éxito
-   ausencia de commit ante error
-   rollback cuando corresponda
-   no publicación externa antes del momento seguro
-   consistencia entre repositorios participantes Ejemplo

``` text
@pytest.mark.asynci
async def test_does_not_commit_when_domain_rule_fails()
```

unit_of_work = FakeUnitOfWork( repository =
InMemoryConversationRepository conversations= ConversationFactory
id="conversation-001" status=ConversationStatus.ARCHIVED

handler = SendMessageHandler repository=repository
unit_of_work=unit_of_work

``` text
with pytest.raises(ConversationArchivedError)
await handler.handle
```

SendMessageCommand tenant_id="tenant-001" actor_id="user-001"
conversation_id="conversation-001" content="Hola"

assert unit_of_work.committed is Fals

## 207. Publicación de evento

Los Application Tests deberán validar que los eventos correctos se
entreguen al puerto responsable

Ejemplo )

)

:

:

.

``` text
]
```

)

)

)

;

o

;

;

``` text
[
```

:

(

s

,

.

,

(

(

(

,

;

)

,

,

,

e

(

:

,

,

:

event_publisher = InMemoryEventPublisher(

``` text
await handler.handle(command
```

assert event_publisher.events == ConversationCreated
conversation_id=ConversationId

``` text
"conversation-001"
```

) tenant_id=TenantId("tenant-001") occurred_at=FIXED_TIME

La prueba deberá veri car contenido, no solo cantidad

## 208. Atomicidad entre estado y evento

Cuando el sistema utilice Outbox Pattern, los Application Tests deberán
veri car que

-   los eventos sean recolectados
-   se registren junto con la transacción
-   no se publiquen directamente antes del commit
-   permanezcan disponibles para el dispatcher Ejemplo conceptual

``` text
await handler.handle(command
```

assert unit_of_work.outbox_messages == ExpectedOutboxMessage(...

assert external_event_bus.events == \[ La publicación real del Outbox se
validará en Integration Tests

## 209. Autorización en Application Laye

La capa de aplicación deberá validar autorización antes de ejecutar
operaciones protegidas

Ejemplo

decision = await authorization_service.authorize actor=actor
action=Action.DELETE_DOCUMENT

``` text
]

]
```

)

:

,

:

fi ,

;

(

;

)

)

.

)

,

,

;

``` text
[
```

,

.

``` text
]
```

(

``` text
[
```

,

s

r

)

.

(

fi :

.

resource=document

if not decision.allowed

``` text
raise AuthorizationDeniedError
```

actor_id=actor.id action=Action.DELETE_DOCUMENT

Los tests deberán cubrir

-   actor permitido
-   actor rechazado
-   recurso de otro tenant
-   rol insu ciente
-   permiso revocado
-   política condicionada

## 210. Orden autorización--lectur

Cuando la autorización dependa del recurso, podrá ser necesario
recuperarlo antes de evaluar permisos

Sin embargo, el sistema deberá evitar ltrar la existencia de recursos de
otros tenants

Los tests deberán validar el comportamiento o cial

-   not found
-   access denied
-   respuesta uniforme
-   evento de auditoría La decisión deberá ser consistente en todos los
    casos de uso

## 211. Tenant Contex

Cada caso de uso deberá recibir o resolver un TenantContext

Ejemplo

``` text
@dataclass(frozen=True
class TenantContext
```

tenant_id: TenantI actor_id: UserI roles: frozenset\[Role )

)

fi :

.

;

;

;

;

;

;

.

;

.

;

:

:

d

t

,

)

d

:

,

``` text
]
```

fi fi a

(

:

,

.

.

.

permissions: frozenset\[Permission Los Application Tests deberán veri
car que el contexto se propague a

-   repositorios
-   gateways
-   eventos
-   auditoría
-   herramientas
-   memoria

## 212. Cross-Tenant Acces

Deberá existir una prueba negativa para cada caso de uso que opere sobre
recursos multi-tenant

Ejemplo

``` text
@pytest.mark.asynci
async def test_cannot_archive_conversation_from_other_tenant()
```

repository = InMemoryConversationRepository conversations=
ConversationFactory id="conversation-001" tenant_id="tenant-b"

handler = ArchiveConversationHandler repository=repository
unit_of_work=FakeUnitOfWork()

``` text
with pytest.raises
```

ConversationNotFoundError )

``` text
await handler.handle
```

ArchiveConversationCommand tenant_id="tenant-a" actor_id="user-001"
conversation_id="conversation-001"

La implementación deberá consultar aplicando el tenant y no recuperar
globalmente para ltrar después )

)

:

;

.

:

;

.

;

;

``` text
]
```

)

;

)

)

o

(

``` text
[
```

fi s

(

,

(

,

,

,

,

``` text
]
```

,

,

(

(

:

(

,

fi :

.

## 213. Idempotency Key

Los Commands que puedan repetirse por red, workers o clientes deberán
aceptar una clave de idempotencia

Casos

-   creación de conversaciones
-   carga de documentos
-   ejecución de tools
-   aprobación
-   procesamiento de jobs
-   operaciones económicas
-   noti caciones externas

## 214. Prueba de idempotencia exitos

``` text
@pytest.mark.asynci
async def test_repeated_command_returns_original_result()
```

idempotency_store = InMemoryIdempotencyStore(

handler = CreateConversationHandler
repository=InMemoryConversationRepository()
unit_of_work=FakeUnitOfWork() id_generator=FixedIdGenerator

``` text
["conversation-001"]
```

) idempotency_store=idempotency_store

command = CreateConversationCommand tenant_id="tenant-001"
actor_id="user-001" title="Incidente" idempotency_key="request-001"

first = await handler.handle(command second = await
handler.handle(command

assert first == secon assert handler.creation_count == fi :

)

)

;

.

,

;

;

;

.

;

;

o

s

,

d

,

,

,

1

,

(

,

a

(

(

)

)

,

)

,

:

## 215. Idempotency Key con payload diferent

La misma clave no deberá reutilizarse con una solicitud materialmente
diferente

first_command = CreateConversationCommand title="Incidente A"
idempotency_key="request-001" ..

second_command = CreateConversationCommand title="Incidente B"
idempotency_key="request-001" ..

El segundo intento deberá producir un error de con icto documentado

## 216. Commands concurrente

Los Application Tests deberán simular solicitudes concurrentes cuando el
caso de uso lo requiera

Ejemplos

-   misma idempotency key
-   aprobación simultánea
-   consumo de cuota
-   procesamiento del mismo documento
-   doble ejecución de una herramienta La garantía de nitiva dependerá
    también de PostgreSQL o Redis, pero la política deberá quedar
    probada en esta capa

## 217. Query Authorizatio

Las Queries también deberán validar permisos

No deberá asumirse que una operación de lectura es inocua

Casos sensibles

-   documentos
-   conversaciones )

)

.

.

.

:

;

fi ;

:

;

.

;

;

,

,

.

;

n

s

.

,

,

fl .

(

(

e

.

.

-   memoria
-   auditoría
-   costos
-   prompts
-   con guración
-   logs
-   herramientas disponibles

## 218. Paginació

Los Query Handlers deberán probar

-   límite predeterminado
-   límite máximo
-   cursor válido
-   cursor inválido
-   página vacía
-   siguiente cursor
-   orden estable
-   aislamiento por tenant Ejemplo

result = await handler.handle ListConversationsQuery
tenant_id="tenant-001" actor_id="user-001" limit=2

assert len(result.items) == assert result.next_cursor is not Non

## 219. Orden estable en querie

La paginación deberá utilizar un orden determinista

Ejemplo

created_at DESC, id DES Los tests deberán incluir elementos con el mismo
timestamp para comprobar el desempate )

fi ;

)

;

;

:

:

;

;

;

;

;

;

;

;

;

;

.

,

n

.

C

:

(

,

2

(

,

s

.

e

.

## 220. Casos de uso con Model Gatewa

Los Application Tests no llamarán un LLM real

Utilizarán FakeModelGateway

Ejemplo

model_gateway = FakeModelGateway responses= ModelResponse
content="Respuesta fundamentada." usage=ModelUsage prompt_tokens=100
completion_tokens=20 )

Esto permitirá validar

-   prompt enviado
-   modelo solicitado
-   respuesta procesada
-   persistencia
-   costos
-   errores
-   fallbacks coordinados

## 221. Veri cación de solicitudes al model

El fake deberá registrar las solicitudes

``` text
await handler.handle(command
```

request = model_gateway.requests\[0

assert request.tenant_id == TenantId

``` text
"tenant-001"
```

assert request.messages\[-1\].content ==

``` text
"Resume la política
```

assert request.max_output_tokens == 1_00 No deberá validarse el texto
completo del prompt cuando solo una parte sea relevante )

)

)

``` text
]
```

;

;

:

;

)

fi ;

;

,

;

``` text
[
```

:

.

,

(

``` text
"
```

.

.

(

)

.

(

,

``` text
]
```

,

(

(

y

0

o

,

.

## 222. Casos de uso RA

Los Application Tests de RAG deberán coordinar

## 1. validación del contexto

## 2. creación de consulta

## 3. recuperación

## 4. ltrado

## 5. construcción de contexto

## 6. llamada al modelo

## 7. validación de respuesta

## 8. persistencia

## 9. registro de citas

Cada componente complejo deberá tener además pruebas propias

## 223. Recuperación vací

El caso de uso deberá tener un comportamiento explícito cuando no
existan fuentes relevantes

Opciones posibles

-   responder que no existe información
-   solicitar más contexto
-   permitir respuesta general marcada
-   rechazar generación no fundamentada La prueba deberá demostrar la
    política elegida

## 224. Tool Calling Application Flo

El ujo de herramientas deberá probar

-   tools disponibles
-   selección recibida
-   validación de nombre
-   validación de argumentos
-   permisos
-   aprobación
-   ejecución
-   registro del resultado
-   nueva llamada al modelo cuando corresponda fi fl ;

;

;

;

;

;

.

;

;

:

;

;

;

;

;

;

;

;

;

G

;

;

a

.

:

.

.

:

w

.

.

## 225. Tool inexistent

model_gateway = FakeModelGateway responses= ModelResponse.tool_call
name="unknown_tool" arguments={}

``` text
with pytest.raises(UnknownToolError)
await handler.handle(command
```

El sistema no deberá intentar ejecutar nombres no registrados

## 226. Argumentos inválidos de Too

Los argumentos generados deberán validarse contra el schema antes de
ejecutar la herramienta

La prueba deberá veri car

-   rechazo
-   ausencia de ejecución
-   registro de error
-   posible recuperación o segunda solicitud al modelo

## 227. Approval Required Flo

Cuando una tool requiera aprobación

-   no deberá ejecutarse inmediatamente
-   deberá crearse una solicitud
-   deberá persistirse el contexto
-   deberá devolverse un estado pendiente
-   deberá emitirse el evento correspondiente Ejemplo

result = await handler.handle(command

assert result.status is ToolExecutionStatus.PENDING_APPROVA )

``` text
]
```

;

:

)

;

``` text
[
```

;

fi :

;

;

e

(

,

;

:

;

.

w

(

,

(

)

.

l

:

)

L

.

.

assert tool_executor.executions == \[ assert approval_repository.count
==

## 228. Reanudación después de aprobació

El caso de uso deberá probar

-   aprobación válida
-   carga del contexto original
-   validación de vigencia
-   ejecución única
-   persistencia del resultado
-   continuación del ujo conversacional La aprobación no deberá permitir
    sustituir argumentos o herramienta sin una nueva validación

## 229. Rechazo de aprobació

Cuando una solicitud sea rechazada

-   la tool no deberá ejecutarse
-   deberá persistirse el rechazo
-   el modelo podrá recibir un resultado controlado
-   el usuario deberá obtener una respuesta consistente
-   deberá registrarse auditoría

## 230. Memory Application Flo

Los casos de uso de memoria deberán probar

-   extracción candidata
-   evaluación de política
-   deduplicación
-   persistencia
-   actualización
-   recuperación relevante
-   eliminación
-   aislamiento por usuario y tenant

## 231. Errores de gateway

)

;

;

;

;

;

fl ;

;

;

;

;

;

;

.

;

;

:

.

:

.

s

n

:

w

;

;

``` text
]
```

1

n

.

Los handlers deberán traducir errores técnicos a errores de aplicación

Ejemplos

-   timeout de proveedor
-   rate limit
-   indisponibilidad
-   contenido inválido
-   fallo de embedding
-   error de storage
-   error de cola La capa de aplicación no deberá exponer excepciones
    especí cas del SDK externo

## 232. Errores recuperables y de nitivo

Los Application Tests deberán distinguir

Recuperable

-   timeout

-   rate limit temporal

-   fallo de red

-   servicio no disponible De nitivo

-   schema inválido

-   permiso denegado

-   recurso inexistente

-   con guración incompatible

-   contenido prohibido La clasi cación determinará

-   retry

-   fallback

-   rechazo

-   DLQ

-   respuesta al usuario

## 233. Compensació

Cuando un ujo no pueda ejecutarse en una sola transacción, deberá de
nirse una compensación

Ejemplo fi fi ;

;

;

;

fi ;

:

;

:

;

fl s

.

;

s

;

;

;

;

;

;

;

.

.

;

.

;

:

n

:

fi s

fi .

fi .

.

## 1. cargar archivo

## 2. registrar documento

## 3. publicar job

Si el registro falla después de cargar el archivo, podrá requerirse
eliminar el objeto

Los Application Tests deberán validar que la compensación sea solicitada

## 234. Auditorí

Las operaciones sensibles deberán producir registros de auditoría

Ejemplos

-   aprobación
-   rechazo
-   ejecución de tool
-   cambio de permisos
-   eliminación
-   lectura sensible
-   exportación
-   acceso cross-tenant rechazado Los tests deberán validar los campos
    relevantes

assert audit.entries\[0\].action ==

``` text
"tool_execution_requested
```

assert audit.entries\[0\].actor_id == "user-001 assert
audit.entries\[0\].tenant_id =="tenant-001

## 235. Application DTO

Los resultados de aplicación deberán ser modelos explícitos

Ejemplo

``` text
@dataclass(frozen=True
class CreateConversationResult
```

conversation_id: st No deberán devolverse directamente

-   modelos ORM
-   responses HTTP
-   objetos de SDK
-   diccionarios sin contrato cuando el caso sea relevante )

;

:

:

;

;

;

.

;

;

;

;

;

;

;

;

a

.

)

r

s

:

``` text
"
```

:

:

(

.

.

.

``` text
"

"
```

.

.

## 236. Validación de entrad

La validación deberá dividirse entre

Interface Laye

Formato, tipos externos y estructura

Application Laye

Permisos, existencia, contexto y precondiciones

Domain Laye

Invariantes y reglas de negocio

Los Application Tests deberán enfocarse en precondiciones del caso de
uso y no duplicar todas las validaciones sintácticas de la API

## 237. Pruebas parametrizadas de autorizació

``` text
@pytest.mark.parametrize
```

("role", "allowed")

(Role.OWNER, True) (Role.ADMIN, True) (Role.MEMBER, False) (Role.VIEWER,
False)

``` text
]

async def test_delete_document_permissions
```

role allowed ) .. La matriz deberá corresponder con la política o cial
del sistema

## 238. Application Test Fixture

)

:

``` text
[
```

,

.

,

,

r

r

r

.

,

:

(

.

.

,

,

a

,

,

s

fi .

(

.

n

Las xtures principales podrán incluir

-   handlers
-   repositories en memoria
-   fake Unit of Work
-   fake clock
-   xed ID generator
-   fake gateways
-   actors
-   tenant contexts
-   event publisher
-   audit recorder Las xtures no deberán ocultar el escenario importante

## 239. Application Test Builder

Podrán crearse builders para con gurar un entorno de caso de uso

Ejemplo

scenario = SendMessageScenario( .with_tenant("tenant-001"
.with_actor("user-001" .with_active_conversation

``` text
"conversation-001
```

.with_model_response("Respuesta" .build(

El builder deberá exponer los colaboradores para efectuar aserciones

## 240. Anti-patterns de Application Testin

Handler con reglas de negoci

El test valida lógica que debería vivir en dominio

Database-Dependent Application Tes

Necesita PostgreSQL para toda prueba de handler )

fi fi fi ;

)

;

:

;

.

;

;

;

)

(

;

;

;

fi o

)

``` text
"
```

:

)

(

)

t

s

.

.

)

.

g

.

.

Interaction-Only Tes

Solo veri ca mocks

Framework-Coupled Handle

Recibe Request, Response o sesiones HTTP

Global Tenant Contex

El contexto se obtiene de una variable global difícil de controlar

Hidden Commi

El handler modi ca estado sin Unit of Work explícito

Fire-and-Forget Side Effect

Se envían efectos externos sin control transaccional

## 241. Checklist de Application Testin

Cada caso de uso deberá responder

-   ¿Cuál es su Command o Query
-   ¿Qué permisos requiere
-   ¿Qué tenant lo ejecuta
-   ¿Qué recursos recupera
-   ¿Qué reglas de dominio activa
-   ¿Qué puertos utiliza
-   ¿Qué guarda
-   ¿Cuándo hace commit
-   ¿Qué eventos produce
-   ¿Es idempotente
-   ¿Qué errores son recuperables
-   ¿Qué auditoría genera
-   ¿Qué ocurre ante concurrencia
-   ¿Qué resultado tipado devuelve

## 242. De nition of Done del capítul

Application Testing se considerará implementado cuando fi fi ?

fi ?

t

.

?

?

?

?

?

?

?

t

t

?

?

?

?

?

s

:

r

.

.

.

o

g

:

.

-   cada caso de uso relevante tenga pruebas
-   Commands y Queries estén tipados
-   los handlers dependan de puertos
-   existan fakes reutilizables
-   la autorización esté cubierta
-   el tenant se propague explícitamente
-   la semántica transaccional esté probada
-   la idempotencia esté cubierta donde aplique
-   eventos y auditoría se validen
-   los errores de infraestructura se traduzcan correctamente
-   la suite no requiera infraestructura real ;

;

;

;

;

;

.

;

;

;

;

## Capítulo 8 --- Repository and Database

Testin \## 243. Propósit

Los Repository and Database Tests validan que la persistencia real
cumpla los contratos de nidos por el dominio y la capa de aplicación

Su objetivo consiste en demostrar que PostgreSQL, SQLAlchemy, Alembic y
pgvector preservan correctamente

-   datos
-   relaciones
-   restricciones
-   aislamiento entre tenants
-   transacciones
-   concurrencia
-   orden
-   paginación
-   búsqueda vectorial
-   integridad referencial
-   migraciones Estas pruebas utilizarán PostgreSQL real mediante
    Testcontainers

## 244. Principio de base de datos rea

No se utilizará SQLite como sustituto general de PostgreSQL

Las diferencias relevantes incluyen

-   tipos
-   constraints
-   concurrencia
-   transacciones
-   JSONB
-   arrays
-   índices
-   extensiones
-   RLS
-   locking
-   sintaxis fi ;

;

;

;

;

;

;

;

;

;

;

;

;

.

;

g

;

;

;

;

;

o

;

:

;

:

.

l

.

.

-   pgvector Las pruebas de repositorio deberán ejecutarse contra la
    misma versión mayor de PostgreSQL utilizada en producción

## 245. Alcanc

La suite cubrirá

-   modelos SQLAlchemy
-   mappings
-   repositories
-   query services
-   migrations
-   constraints
-   foreign keys
-   índices
-   transacciones
-   rollbacks
-   locks
-   aislamiento
-   RLS
-   JSONB
-   pgvector
-   Outbox
-   idempotency records
-   paginación
-   borrado
-   retención

## 246. Testcontainer de PostgreSQ

La suite deberá levantar PostgreSQL de forma automatizada

Ejemplo conceptual

``` text
import pytes
from testcontainers.postgres import
```

PostgresContainer

``` text
@pytest.fixture(scope="session"
def postgres_container()
```

)

;

;

;

;

;

;

;

;

.

;

;

;

;

;

;

.

;

;

;

:

t

e

:

;

;

.

,

:

)

L

(

.

``` text
with PostgresContainer
"pgvector/pgvector:pg16"
```

) as container yield containe La imagen deberá incluir las extensiones
necesarias

## 247. Inicialización de la bas

Al iniciar el contenedor deberán ejecutarse

## 1. creación de extensiones

## 2. migraciones Alembic

## 3. validación de versión

## 4. con guración de roles

## 5. con guración RLS

## 6. comprobación de readiness

No deberá utilizarse metadata.create_all() como sustituto permanente de
migraciones en la suite principal

## 248. Migraciones como fuente de verda

La base de pruebas deberá construirse mediante las migraciones o ciales

Esto permitirá detectar

-   migraciones incompletas
-   orden incorrecto
-   dependencias ausentes
-   diferencias entre metadata y schema
-   fallos de instalación limpia create_all() podrá utilizarse
    únicamente en herramientas auxiliares claramente separadas

## 249. Estrategia de aislamient

La estrategia inicial combinará

-   contenedor por sesión
-   schema por worker de pytest-xdist
-   transacción o limpieza por prueba
-   base independiente para migration tests destructivos fi fi ;

;

.

;

;

;

;

;

:

;

;

:

.

.

:

r

;

;

(

;

:

e

o

,

.

.

d

fi .

.

Ejemplo de schema

test_gw test_gw test_gw Cada worker deberá utilizar su propio
search_path

## 250. Fixture de sesión de base de dato

La xture de sesión será responsable de

-   iniciar PostgreSQL
-   ejecutar migraciones
-   crear schemas paralelos
-   veri car extensiones
-   cerrar recursos No deberá insertar datos funcionales compartidos
    mutables

## 251. Fixture de transacción por prueb

Ejemplo conceptual

``` text
@pytest.fixtur
async def database_session(engine)
```

connection = await engine.connect( transaction = await connection.begin(

session = AsyncSession bind=connection expire_on_commit=False

try yield sessio finally

``` text
await session.close(
await transaction.rollback(
await connection.close(
```

La estrategia deberá adaptarse cuando el código productivo cree
conexiones independientes fi fi )

0

1

2

:

.

:

;

:

:

;

;

e

;

n

,

(

:

)

,

)

:

)

.

)

.

s

a

)

.

## 252. Commits reale

Algunas pruebas deberán permitir commits reales

Casos

-   Outbox
-   workers
-   múltiples conexiones
-   locking
-   visibilidad transaccional
-   idempotencia
-   concurrencia
-   RLS por conexión
-   recuperación después de reinicio Estas pruebas no utilizarán
    rollback externo que oculte el comportamiento

## 253. Contract Tests de repositorio

Cada interfaz de repositorio deberá disponer de una suite reusable

Ejemplo

``` text
class ConversationRepositoryContract
async def test_add_and_get
```

self repository ) conversation = ConversationFactory(

``` text
await repository.add(conversation
await repository.commit(
```

restored = await repository.get conversation.id
tenant_id=conversation.tenant_id

assert restored == conversatio La misma suite podrá aplicarse a

-   repositorio en memoria
-   repositorio PostgreSQL :

.

.

:

.

:

)

.

.

,

.

.

;

.

.

,

s

.

:

,

(

)

.

s

:

n

(

)

)

.

,

.

## 254. Contrato mínimo de repositori

El contrato deberá de nir

-   creación
-   actualización
-   recuperación
-   ausencia
-   duplicidad
-   tenant scope
-   orden
-   paginación
-   concurrencia
-   errores
-   borrado
-   persistencia de eventos cuando corresponda No todos los repositorios
    deberán implementar un CRUD genérico

## 255. Persistencia de objetos de valo

Los tests deberán demostrar que los objetos de valor se guardan y
reconstruyen sin pérdida semántica

Ejemplo

conversation = ConversationFactory title=ConversationTitle

``` text
"Incidente crítico"
```

)

``` text
await repository.add(conversation
await session.commit(
```

session.expunge_all(

restored = await repository.get conversation.id conversation.tenant_id

assert restored.title == ConversationTitle

``` text
"Incidente crítico"
```

)

)

)

;

;

,

;

;

:

;

.

;

;

;

;

;

;

fi :

,

)

)

,

,

,

(

.

(

)

(

r

o

(

.

## 256. Persistencia de enum

Los enums deberán probar

-   valor almacenado

-   reconstrucción

-   nuevos valores

-   restricciones

-   compatibilidad de migraciones La estrategia o cial deberá indicar si
    se utilizan

-   enums nativos de PostgreSQL

-   strings con constraints

-   códigos internos

## 257. Fechas y zonas horaria

La persistencia deberá conservar timestamps con zona horaria

assert restored.created_at == FIXED_TIM assert
restored.created_at.tzinfo is not Non Deberán probarse

-   UTC
-   precisión
-   comparación
-   expiraciones
-   valores límite

## 258. Decimal y costo

Los costos deberán almacenarse con precisión exacta

Los tests deberán detectar

-   redondeos inesperados
-   over ow
-   escalas incorrectas
-   moneda ausente
-   valores negativos no permitidos No se utilizará float para montos
    nancieros fl ;

;

;

;

;

;

.

fi ;

;

;

.

;

:

;

;

;

:

:

;

.

.

s

fi s

s

.

:

.

E

.

e

## 259. JSON

Los campos JSONB deberán probar

-   round-trip
-   objetos anidados
-   arrays
-   Unicode
-   valores vacíos
-   schema esperado
-   consultas
-   índices cuando correspondan El uso de JSONB no deberá sustituir el
    modelado relacional sin una justi cación

## 260. Constraints NOT NUL

Los tests de migración o persistencia deberán comprobar que los campos
obligatorios no acepten NULL

No será su ciente con ar únicamente en Pydantic o en el dominio

La base deberá proteger su propia integridad

## 261. Unique Constraint

Deberán probarse restricciones únicas relevantes

Ejemplos

-   identidad externa por proveedor
-   idempotency key por tenant
-   nombre de tool por versión
-   posición de chunk por documento
-   checksum según política
-   email normalizado cuando corresponda Ejemplo

``` text
with pytest.raises(IntegrityError)
await insert_duplicate_idempotency_key(
```

La prueba deberá veri car que el repository traduzca el error cuando el
contrato así lo requiera .

;

;

:

;

:

;

fi ;

;

;

B

fi fi ;

;

;

.

;

;

:

s

.

L

.

.

:

)

.

fi .

.

## 262. Unique Constraints multi-tenan

La unicidad deberá incluir el tenant cuando el valor pueda repetirse
entre organizaciones

Ejemplo

UNIQUE (tenant_id, tool_name, version Los tests deberán demostrar

-   duplicado dentro del mismo tenant: rechazado
-   mismo valor en tenants distintos: permitido

## 263. Foreign Key

Deberán probarse

-   referencia válida
-   referencia inexistente
-   eliminación del padre
-   comportamiento CASCADE
-   comportamiento RESTRICT
-   comportamiento SET NULL La estrategia de eliminación deberá ser
    explícita por relación

## 264. Check Constraint

Las reglas simples y críticas podrán protegerse también mediante CHECK

Ejemplos

-   tokens no negativos
-   tamaño positivo
-   expires_at \> created_at
-   score dentro de rango
-   estado compatible con campos de decisión Los tests deberán demostrar
    que la base rechaza datos inválidos incluso cuando se omita la capa
    de aplicación

## 265. Constraints de estado

Cuando una solicitud esté aprobada, podrá requerirse :

:

.

;

;

:

;

;

;

;

s

;

:

.

;

;

s

s

.

.

;

:

)

t

.

.

.

-   decided_at no nulo
-   decided_by no nulo Cuando esté pendiente, esos campos deberán ser
    nulos

La base podrá aplicar un constraint

CHECK

status = 'pending AND decided_at IS NUL AND decided_by IS NUL

O

status IN ('approved', 'rejected' AND decided_at IS NOT NUL AND
decided_by IS NOT NUL

La suite deberá probar cada combinación

## 266. Índice

Los tests deberán veri car la existencia de índices críticos mediante
introspección cuando sea relevante

Ejemplos

-   tenant y fecha
-   foreign keys
-   estado de jobs
-   Outbox no publicado
-   idempotency key
-   búsqueda vectorial
-   búsqueda JSONB
-   expiraciones No será necesario probar cada índice trivial, pero sí
    los asociados a requisitos de rendimiento o integridad

## 267. Query Plan

Las consultas críticas deberán analizarse con EXPLAIN )

(

)

(

)

R

(

.

:

.

;

.

;

;

;

s

;

;

;

fi ;

.

s

:

'

.

L

L

L

L

.

.

)

Los tests de performance de base podrán comprobar que no aparezcan
planes claramente inaceptables

Ejemplo

-   secuential scan sobre una tabla masiva cuando existe un índice
    obligatorio
-   join no acotado
-   ordenamiento completo evitable Estos tests deberán ejecutarse con
    datasets representativos y no formar necesariamente parte del fast
    pipeline

## 268. Repository Ad

La operación add deberá probar

-   persistencia
-   identidad
-   valores
-   relaciones
-   eventos pendientes
-   duplicados
-   tenant
-   ush No deberá hacer commit de manera oculta si el contrato utiliza
    Unit of Work

## 269. Repository Ge

La operación get deberá probar

-   recurso existente
-   ausente
-   tenant correcto
-   tenant incorrecto
-   relaciones necesarias
-   soft delete
-   objeto reconstruido El contrato deberá de nir si devuelve None o
    lanza excepción

## 270. Repository Updat

fl .

;

;

;

:

;

;

;

;

;

.

.

;

;

;

;

;

.

;

fi t

d

.

:

:

e

.

;

.

Cuando SQLAlchemy utilice tracking, deberá probarse que

-   cambios válidos se persisten
-   versión se actualiza
-   eventos se registran
-   relaciones se sincronizan
-   cambios no autorizados no aparecen accidentalmente

## 271. Optimistic Lockin

Los agregados susceptibles a con ictos deberán utilizar una versión

Ejemplo

version INTEGER NOT NUL El UPDATE deberá incluir

WHERE id = :i AND version = :expected_versio Si ninguna la se modi ca,
deberá producirse un error de concurrencia

## 272. Prueba de Optimistic Lockin

first = await repository.get conversation_id tenant_id

second = await repository.get conversation_id tenant_id

first.rename ConversationTitle("Título A")

``` text
await repository.save(first
await unit_of_work.commit(
```

second.rename ConversationTitle("Título B") )

)

)

)

:

fi (

d

,

,

(

;

;

fi ;

:

;

,

,

fl L

g

)

)

(

(

n

,

,

.

g

:

.

.

``` text
with pytest.raises
```

ConcurrentModificationError )

``` text
await repository.save(second
```

## 273. Pessimistic Lockin

Los ujos que requieran SELECT ... FOR UPDATE deberán probar

-   bloqueo efectivo

-   espera

-   timeout

-   orden de adquisición

-   liberación después de commit

-   liberación después de rollback Casos posibles

-   aprobación única

-   consumo de cuota

-   asignación de job

-   ejecución de tool irreversible

## 274. Deadlock

Las pruebas de concurrencia deberán buscar

-   orden inconsistente de locks
-   transacciones largas
-   reintento ante deadlock
-   liberación de recursos No será necesario provocar deadlocks en cada
    pipeline, pero sí en hardening de ujos críticos

## 275. Isolation Level

Cuando el ujo dependa del nivel de aislamiento, deberá documentarse y
probarse

Opciones

-   Read Committed
-   Repeatable Read
-   Serializable La selección no deberá realizarse de forma global sin
    evaluar el costo :

fl ;

;

:

fl .

:

;

.

.

;

;

;

;

;

.

s

;

(

;

.

;

.

s

g

:

,

)

.

:

fl .

.

## 276. Rollbac

Deberá probarse que un error posterior a una escritura revierta toda la
transacción

Ejemplo

``` text
await repository.add(conversation
await outbox_repository.add(invalid_message

with pytest.raises(IntegrityError)
await unit_of_work.commit(
```

assert await repository.get conversation.id conversation.tenant_id ) is
Non

## 277. Savepoint

Los savepoints podrán utilizarse para

-   recuperación parcial
-   importaciones
-   procesamiento por lotes
-   xtures
-   operaciones opcionales Los tests deberán demostrar que una falla
    parcial no invalida más estado del permitido

## 278. Row-Level Securit

RLS constituirá una defensa obligatoria para tablas multi-tenant
seleccionadas

Las pruebas deberán ejecutarse con

-   roles reales
-   contexto de tenant
-   conexiones separadas
-   acceso permitido
-   acceso denegado
-   inserts
-   updates fi ;

;

;

:

;

e

;

;

;

;

k

;

;

.

s

;

,

:

y

:

,

(

)

)

:

)

.

.

.

-   deletes No será su ciente probar ltros ORM

## 279. Con guración del tenant en PostgreSQ

El tenant podrá establecerse mediante una variable de sesión o
transacción

Ejemplo conceptual

SET LOCAL app.current_tenant_id = 'tenant-001' Las políticas podrán
utilizar

tenant_id = current_setting 'app.current_tenant_id )::uui La con
guración de nitiva deberá documentarse en Data Architecture

## 280. RLS Select Isolatio

``` text
await set_tenant_context
```

session tenant_id="tenant-a"

rows = await session.execute select(KnowledgeDocumentModel

assert row.tenant_id for row in rows.scalars(

``` text
} == {"tenant-a"
```

La prueba deberá insertar previamente datos de al menos dos tenants

## 281. RLS Insert Protectio

Un actor no deberá insertar una la con un tenant distinto al contexto
activo

``` text
await set_tenant_context
```

session tenant_id="tenant-a" )

)

fi .

d

``` text
{
```

fi fi ,

,

:

fi

``` text
}
```

fi :

fi (

,

(

,

.

n

'

(

n

(

)

)

.

;

L

.

.

.

``` text
with pytest.raises(DatabaseAuthorizationError)
await insert_document
```

tenant_id="tenant-b"

## 282. RLS Update Protectio

Deberá probarse que

-   no se actualicen las de otro tenant
-   no pueda cambiarse tenant_id
-   el repository traduzca ausencia o denegación de acuerdo con la
    política

## 283. RLS Delete Protectio

Un tenant no deberá borrar recursos de otro tenant, incluso si conoce su
identi cador

La prueba deberá usar la misma identidad de recurso conocida para
demostrar defensa real

## 284. Bypass de RL

Los roles de aplicación ordinarios no deberán poseer

-   BYPASSRLS
-   ownership indebido de tablas
-   privilegios de superusuario La suite de seguridad de base deberá
    inspeccionar privilegios

Los procesos administrativos que necesiten bypass deberán utilizar roles
separados y auditados

## 285. Connection Pool y Tenant Leakag

Una conexión reutilizada no deberá conservar el tenant anterior

La suite deberá probar

## 1. obtener conexión

## 2. establecer tenant A

)

)

;

fi ;

;

:

:

.

;

S

;

;

(

n

,

n

:

.

e

.

:

.

fi .

.

.

## 3. devolverla al pool

## 4. obtener conexión reutilizada

## 5. establecer tenant B o limpiar contexto

## 6. comprobar ausencia de datos de A

Este escenario será crítico

## 286. Soft Delet

Cuando se utilice soft delete, deberá probarse

-   exclusión predeterminada
-   consulta administrativa
-   restauración
-   unicidad
-   RLS
-   retención
-   timestamps El soft delete no deberá aplicarse automáticamente a
    todas las entidades

## 287. Hard Delet

Las operaciones de eliminación de nitiva deberán probar

-   permisos
-   constraints
-   cascadas
-   objetos externos
-   auditoría
-   irreversibilidad
-   cumplimiento de retención

## 288. Outbox Tabl

La tabla Outbox deberá probar

-   inserción en la misma transacción
-   payload
-   tipo de evento
-   versión
-   tenant
-   correlation ID ;

;

;

;

;

;

;

;

;

;

.

;

;

;

;

;

;

e

;

e

;

.

.

e

;

:

;

.

fi ;

:

:

.

-   estado no publicado
-   intentos
-   timestamp

## 289. Atomicidad del Outbo

La creación del agregado y su mensaje Outbox deberán con rmarse o
revertirse juntos

Casos

-   ambos guardados
-   falla del Outbox
-   falla del agregado
-   rollback completo

## 290. Lectura del Outbo

Los dispatchers deberán poder reclamar mensajes sin duplicar
procesamiento

Podrán utilizar

FOR UPDATE SKIP LOCKE Las pruebas deberán ejecutar múltiples
consumidores y veri car que cada mensaje sea reclamado una sola vez por
ciclo

## 291. Idempotency Stor

La tabla de idempotencia deberá probar

-   clave única por tenant y operación
-   hash del request
-   resultado almacenado
-   expiración
-   concurrencia
-   con icto por payload distinto
-   limpieza

## 292. Jobs y colas persistente

Cuando los jobs se almacenen en PostgreSQL, deberán probar fl :

;

.

.

;

;

:

;

;

;

;

.

;

;

.

;

D

;

e

x

:

x

s

fi fi :

.

.

-   creación
-   claim
-   heartbeat
-   completion
-   failure
-   retry
-   expiración de lease
-   recuperación
-   dead-letter

## 293. pgvecto

Las pruebas de pgvector deberán utilizar la extensión real

Deberán cubrir

-   persistencia de embeddings
-   dimensión
-   tipo
-   búsqueda
-   distancia
-   ltros
-   tenant
-   índices
-   actualización
-   eliminación

## 294. Dimensión de embedding

La base deberá rechazar vectores de dimensión incorrecta

Ejemplo

``` text
with pytest.raises(EmbeddingDimensionError)
await repository.add_chunk
```

embedding=\[0.1, 0.2\]

Si la columna espera 1,536 dimensiones, el test deberá utilizar una
dimensión distinta para demostrar el constraint

## 295. Búsqueda vectorial básic

fi ;

;

;

;

)

;

;

;

;

:

;

;

;

;

.

;

.

;

;

:

;

r

.

;

,

(

a

s

.

.

:

La prueba deberá construir vectores controlados

Ejemplo conceptual

query = \[1.0, 0.0, 0.0

``` text
await repository.add
```

ChunkFactory id="chunk-a" embedding=\[0.9, 0.1, 0.0\]

``` text
await repository.add
```

ChunkFactory id="chunk-b" embedding=\[0.0, 1.0, 0.0\]

results = await repository.search query_embedding=query limit=2

assert results\[0\].chunk_id == "chunk-a No deberá utilizarse un
proveedor de embeddings real en este test

## 296. Métrica de distanci

La suite deberá re ejar la métrica o cial

-   cosine distance
-   inner product
-   Euclidean distance No deberán mezclarse índices, operadores y
    normalización incompatibles

## 297. Filtros en búsqueda vectoria

Toda búsqueda deberá respetar ltros de

-   tenant
-   documento )

)

)

)

)

;

;

;

;

,

fl .

:

(

(

,

(

,

(

fi

``` text
]
```

fi ,

a

:

:

.

,

(

,

l

``` text
"
```

.

.

-   estado
-   permisos
-   colección
-   clasi cación
-   fecha cuando corresponda Ejemplo

results = await repository.search tenant_id=TenantId("tenant-a")
query_embedding=query

assert all item.tenant_id == TenantId("tenant-a" for item in result

## 298. Hybrid Searc

Cuando se implemente búsqueda híbrida, deberán probarse

-   score vectorial
-   score textual
-   pesos
-   normalización
-   ltros
-   orden
-   desempate
-   ausencia de resultados La fórmula deberá ser determinista y
    versionada

## 299. Índices vectoriale

Las pruebas de infraestructura deberán comprobar la creación del índice
aprobado

-   HNSW

-   IVFFlat

-   otro soportado También deberán veri carse

-   operador correcto

-   dimensión

-   con guración )

fi )

fi fi ;

;

;

;

;

;

:

;

;

;

;

;

;

;

;

.

;

(

;

fi .

.

:

h

s

s

,

.

(

,

:

)

:

-   comportamiento durante migraciones

## 300. Exactitud y aproximació

Las búsquedas con índices aproximados no siempre garantizan orden exacto
en todos los datasets

Los tests deberán distinguir

Correctness Test

Pueden desactivar el índice o utilizar casos deterministas

Recall Evaluatio

Miden qué proporción de vecinos esperados recupera el índice aproximado

No deberá confundirse ausencia de orden exacto con una falla funcional
sin analizar la métrica

## 301. Query Service

Los servicios de lectura deberán probar

-   proyecciones
-   joins
-   agregaciones
-   ltros
-   orden
-   paginación
-   tenant
-   permisos
-   valores nulos No deberán reconstruir agregados cuando solo se
    necesita un DTO de lectura

## 302. N+1 Querie

Las consultas críticas deberán probar o inspeccionar que no produzcan
N+1

Podrá instrumentarse el número de queries ejecutadas

Ejemplo fi ;

;

;

;

.

:

;

;

;

;

.

n

s

s

:

s

.

:

n

.

.

.

.

.

.

``` text
with query_counter() as counter
```

result = await query_service.list_documents tenant_id

assert counter.total \<= El threshold deberá basarse en el diseño
esperado

## 303. Paginación por curso

La persistencia deberá probar

-   cursor codi cado
-   orden estable
-   límites
-   inserciones concurrentes
-   eliminación entre páginas
-   cursor de otro tenant
-   manipulación del cursor No se utilizará offset para ujos de gran
    volumen cuando pueda producir inconsistencias o degradación

## 304. Búsqueda textua

Cuando PostgreSQL proporcione full-text search, deberán probarse

-   tokenización
-   idioma
-   ranking
-   acentos
-   palabras vacías
-   ltros
-   tenant
-   índices GIN Los casos lingüísticos deberán corresponder a los
    idiomas soportados

## 305. Case Sensitivit

Los tests deberán de nir el comportamiento de fi ;

)

;

;

;

;

;

fi .

.

;

;

;

;

fi ;

.

;

,

;

fl :

y

l

3

r

:

:

.

:

.

(

-   emails
-   nombres
-   identi cadores externos
-   tags
-   tool names
-   búsquedas Cuando se utilice citext o normalización, la semántica
    deberá quedar demostrada

## 306. Unicod

La persistencia deberá probar

-   español
-   emojis
-   caracteres asiáticos
-   signos combinados
-   normalización
-   longitud
-   búsqueda No deberá asumirse que cantidad de caracteres equivale a
    cantidad de bytes

## 307. Tamaño de contenid

Las columnas y restricciones deberán probar límites para

-   mensajes
-   títulos
-   metadata
-   prompts
-   documentos extraídos
-   resultados de tools
-   errores Los contenidos muy grandes podrán almacenarse en Object
    Storage en vez de PostgreSQL, según la arquitectura

## 308. Migración U

Cada migración deberá probar que puede aplicarse desde el estado
anterior

La suite deberá ;

fi ;

;

;

.

;

;

;

;

;

;

.

.

;

;

:

;

e

;

;

.

;

;

p

:

o

:

.

.

.

## 1. crear una base en versión previa

## 2. insertar datos representativos

## 3. aplicar la migración

## 4. veri car schema

## 5. veri car datos

## 309. Migración Dow

Las migraciones reversibles deberán probar downgrade

Cuando un downgrade sea deliberadamente no soportado, deberá
documentarse

-   motivo
-   estrategia de rollback
-   restauración desde backup
-   compatibilidad temporal No deberá ngirse reversibilidad cuando
    exista pérdida de datos

## 310. Instalación limpi

Deberá existir una prueba que aplique todas las migraciones desde una
base vacía

Esto detectará

-   dependencias implícitas
-   SQL manual ausente
-   extensiones no creadas
-   orden defectuoso
-   migraciones modi cadas indebidamente

## 311. Upgrade desde versión soportad

Antes de un release deberá probarse la actualización desde las versiones
o cialmente soportadas

Ejemplo

``` text
v1.0 → v1.
v1.1 → v1.
v1.0 → v1.
```

La matriz dependerá de la política de soporte fi fi ;

:

fi :

.

1

2

2

;

;

fi ;

;

;

;

;

.

;

;

;

n

a

.

.

.

a

.

fi :

.

.

## 312. Migraciones con dato

Las migraciones que transformen datos deberán probar

-   las existentes
-   nulos
-   datos inválidos históricos
-   volumen
-   reanudación
-   idempotencia cuando aplique
-   rollback operacional

## 313. Back ll

Los back lls de gran volumen no deberán ejecutarse necesariamente como
una transacción bloqueante dentro de la migración

Los tests deberán validar

-   lotes
-   checkpoint
-   reanudación
-   concurrencia
-   compatibilidad mientras el back ll está incompleto

## 314. Expand and Contrac

Los cambios incompatibles deberán seguir cuando corresponda

## 1. expandir schema

## 2. desplegar código compatible

## 3. migrar datos

## 4. cambiar lecturas

## 5. dejar de escribir formato anterior

## 6. eliminar estructura antigua

Cada etapa deberá probarse contra versiones compatibles

## 315. Compatibilidad de despliegu

Las pruebas deberán considerar que durante un rolling deployment pueden
coexistir dos versiones de la aplicación fi ;

;

;

fi ;

;

;

;

;

;

fi ;

;

s

.

:

;

.

.

;

;

fi ;

.

t

s

.

e

:

.

:

El schema temporal deberá ser compatible con ambas cuando la
infraestructura despliegue de esa forma

## 316. Schema Drif

CI deberá detectar diferencias entre

-   modelos SQLAlchemy
-   migraciones
-   schema resultante Podrá utilizarse autogenerate como veri cación,
    pero los cambios generados deberán revisarse

Una diferencia inesperada deberá fallar el pipeline

## 317. Privilegio

La suite deberá validar que el rol de aplicación posea solo privilegios
necesarios

No deberá poder

-   crear extensiones
-   modi car policies
-   crear usuarios
-   acceder a schemas administrativos
-   saltarse RLS
-   alterar tablas en runtime Las migraciones utilizarán un rol separado

## 318. SQL Injectio

Los repositories deberán utilizar parámetros

Las pruebas de seguridad podrán incluir inputs maliciosos para demostrar
que

-   no alteran la consulta
-   no acceden a otros tenants
-   se almacenan o rechazan según política
-   no producen SQL dinámico inseguro

## 319. Observabilidad de bas

fi .

;

;

;

:

;

.

;

;

s

;

.

;

t

n

;

:

.

;

fi .

e

.

.

:

.

.

Las pruebas de integración deberán veri car cuando corresponda

-   métricas de pool
-   queries lentas
-   errores
-   timeouts
-   deadlocks
-   transacciones abiertas
-   correlation IDs No deberán loguearse parámetros sensibles sin
    redacción

## 320. Timeouts de consulta

Las consultas críticas deberán respetar límites

Podrán con gurarse

-   statement_timeout
-   timeout de adquisición del pool
-   timeout de lock
-   timeout de transacción Los tests deberán veri car traducción a
    errores controlados

## 321. Pool Exhaustio

Las pruebas de resiliencia deberán demostrar el comportamiento cuando no
existan conexiones disponibles

El sistema deberá

-   esperar dentro del límite
-   fallar de forma controlada
-   emitir métricas
-   no bloquear inde nidamente
-   recuperarse al liberar conexiones

## 322. Reconexió

La capa de infraestructura deberá probar

-   conexión cerrada
-   reinicio temporal de PostgreSQL ;

;

;

fi .

;

.

;

;

;

fi ;

:

:

;

fi .

n

;

;

;

;

;

n

.

;

fi :

s

.

.

.

:

-   conexión inválida en pool
-   recuperación
-   transacciones perdidas No se deberá reintentar automáticamente una
    transacción no idempotente sin una política explícita

## 323. Backup and Restore Validatio

La estrategia de datos deberá incluir pruebas programadas de
restauración

Una restauración se considerará válida cuando

-   la base inicia
-   las migraciones reconocen la versión
-   constraints existen
-   RLS funciona
-   datos críticos son legibles
-   checksums coinciden
-   la aplicación supera smoke tests Crear backups sin probar
    restauración no será su ciente

## 324. Datos de prueba representativo

Las pruebas de performance de repositories deberán utilizar volúmenes
cercanos a escenarios reales

Ejemplos

-   miles de conversaciones
-   millones de chunks
-   Outbox acumulado
-   múltiples tenants
-   documentos con metadata
-   distintas distribuciones de embeddings No deberán formar parte del
    pipeline rápido

## 325. Factories de persistenci

Podrán existir factories especí cas para insertar modelos ORM o xtures
masivas

Sin embargo .

.

:

:

;

;

;

;

;

;

;

;

.

;

;

;

;

fi .

;

.

.

a

:

fi n

.

s

fi .

.

-   los tests de contrato deberán usar el repository
-   la inserción directa se reservará para preparar escenarios
-   no se deberá confundir modelo ORM con entidad de dominio

## 326. Limpieza de bas

La limpieza deberá ser

-   automática

-   segura

-   compatible con paralelismo

-   independiente del orden

-   rápida Opciones

-   rollback

-   truncado por schema

-   recreación de schema

-   base temporal La estrategia deberá impedir operar sobre una base no
    identi cada como testing

## 327. Anti-patterns de Repository Testin

SQLite Substitut

Oculta diferencias de PostgreSQL

create_all() Onl

No valida migraciones

Shared Database Stat

Las pruebas dependen de registros previos

Repository Commits Internall

Rompe Unit of Work

ORM Model Leakag

La capa superior recibe modelos SQLAlchemy .

;

;

:

;

.

;

e

.

;

.

:

;

e

y

e

;

e

.

y

.

;

.

;

fi .

g

.

RLS Simulated in Pytho

No prueba políticas reales

No Concurrency Test

Asume que secuencial equivale a seguro

Production Snapsho

Utiliza datos reales sin anonimizar

Query Count Ignore

Permite N+1 y degradación silenciosa

## 328. Checklist de Repository Testin

Cada repository deberá responder

-   ¿Cumple su Protocol
-   ¿Usa PostgreSQL real
-   ¿Respeta tenant
-   ¿Funciona RLS
-   ¿Reconstruye correctamente el dominio
-   ¿Maneja duplicados
-   ¿Preserva transacciones
-   ¿Soporta concurrencia
-   ¿Tiene orden estable
-   ¿Pagina correctamente
-   ¿Traduce errores
-   ¿Posee índices críticos
-   ¿Evita N+1
-   ¿Sus migraciones están probadas
-   ¿Su limpieza es segura

## 329. De nition of Done del capítul

Repository and Database Testing se considerará implementado cuando

-   PostgreSQL se ejecute mediante Testcontainers
-   la base se construya con Alembic ?

fi ?

?

?

?

?

?

?

?

?

?

?

?

t

d

.

s

n

?

;

:

.

.

?

.

;

o

g

:

-   los repositories tengan contract tests
-   los objetos de dominio se reconstruyan correctamente
-   constraints e índices críticos estén validados
-   RLS cubra lectura y escritura
-   exista aislamiento por worker
-   concurrencia e idempotencia estén probadas
-   Outbox tenga atomicidad
-   pgvector se pruebe con la extensión real
-   las migraciones se validen desde cero y con datos
-   CI detecte schema drift
-   exista una prueba programada de restauración ;

;

;

;

;

;

;

;

.

;

;

## Capítulo 9 --- API Testin

## 330. Propósit

Los API Tests validan el comportamiento observable de las interfaces
HTTP expuestas por GEEM AI Assistant

Su objetivo es demostrar que la API

-   recibe solicitudes conforme al contrato
-   autentica y autoriza correctamente
-   traduce los datos externos a casos de uso
-   devuelve códigos HTTP apropiados
-   produce respuestas estructuradas y estables
-   protege los límites entre tenants
-   maneja errores de forma uniforme
-   soporta uploads, paginación y streaming
-   expone health checks con ables
-   evita ltrar información sensible Los API Tests deberán probar la
    interfaz de la aplicación, no la implementación interna de FastAPI

## 331. Alcanc

La suite de API cubrirá

-   rutas FastAPI
-   request models
-   response models
-   dependency injection
-   autenticación
-   autorización
-   tenant resolution
-   códigos de estado
-   headers
-   errores
-   paginación
-   ltros
-   uploads
-   downloads
-   Server-Sent Events
-   rate limiting fi fi ;

;

;

;

.

;

;

;

;

;

;

;

;

;

;

e

;

.

o

;

:

fi ;

;

.

;

;

;

:

;

;

;

;

g

-   idempotency keys
-   health checks
-   readiness
-   versionado
-   deprecaciones

## 332. Niveles de API Testin

Las pruebas de API se dividirán en tres niveles

### 332.1 API Component Test

Ejecutan la aplicación mediante ASGI sin abrir un puerto real

Utilizan

-   FastAPI
-   HTTPX
-   ASGITransport
-   dependencias reemplazadas
-   casos de uso falsos o controlados \### 332.2 API Integration Test

Ejecutan la API con implementaciones reales seleccionadas

Podrán utilizar

-   PostgreSQL
-   Redis
-   autenticación real
-   Object Storage temporal
-   workers controlados \### 332.3 Deployed API Test

Ejecutan solicitudes contra un ambiente desplegado

Se utilizarán para

-   smoke tests
-   veri cación de despliegue
-   networking
-   TLS
-   gateway
-   con guración del ambiente fi fi ;

;

:

;

;

;

;

;

;

;

;

;

.

:

:

;

;

;

.

;

;

.

;

s

s

.

s

g

.

.

.

.

## 333. Cliente HTTP o cia

Los API Tests del backend utilizarán HTTPX

Ejemplo conceptual

``` text
import pytes
from httpx import ASGITransport, AsyncClien

@pytest.fixtur
async def api_client(app)
```

transport = ASGITransport(app=app

``` text
async with AsyncClient
```

transport=transport base_url="http://test" ) as client yield clien No
será necesario iniciar Uvicorn para las pruebas ordinarias de API

## 334. Application Factor

La aplicación deberá construirse mediante una factory

Ejemplo

``` text
def create_application
```

settings: Settings container: ApplicationContainer ) -\> FastAPI app =
FastAPI(

register_routes(app register_exception_handlers(app
register_dependencies(app, container

``` text
return ap
```

Esto permitirá crear una instancia independiente para cada suite o
escenario

No se deberá depender de una aplicación global inicializada al importar
módulos :

t

:

p

:

e

:

)

t

fi ,

(

)

:

y

(

l

,

,

.

)

,

.

)

)

t

.

.

.

## 335. Dependency Override

FastAPI permite reemplazar dependencias durante pruebas

Ejemplo

app.dependency_overrides get_create_conversation_handle

``` text
] = lambda: fake_handle
```

Los overrides deberán limpiarse después de cada prueba

app.dependency_overrides.clear( No deberán ltrarse overrides entre
pruebas

## 336. Prueba básica de endpoin

``` text
@pytest.mark.asynci
async def test_creates_conversation(api_client)
```

response = await api_client.post

``` text
"/api/v1/conversations"
```

json=

``` text
"title": "Incidente crítico"
}
```

headers=

``` text
"Authorization": "Bearer test-token"
}
```

assert response.status_code == 20 assert response.json() ==

``` text
"id": "conversation-001"
"title": "Incidente crítico"
"status": "active"
```

La prueba deberá validar únicamente campos pertenecientes al contrato

## 337. Contrato de solicitude

Cada endpoint deberá probar

-   payload válido
-   ausencia de campos obligatorios )

``` text
}
```

:

fi ,

,

;

``` text
{

{
```

o

:

;

r

``` text
[
```

,

s

s

.

``` text
{
```

,

)

,

t

r

(

,

1

.

.

,

:

.

,

-   campos con tipo incorrecto
-   valores fuera de límites
-   campos desconocidos según política
-   cuerpo vacío
-   JSON inválido
-   content type incorrecto
-   tamaño máximo

## 338. Validación de campos desconocido

Los modelos externos deberán de nir una política explícita

Opciones

-   rechazar campos adicionales
-   ignorarlos
-   conservarlos de manera controlada Para APIs empresariales se
    preferirá rechazar campos desconocidos cuando puedan ocultar errores
    del cliente

Ejemplo

response = await api_client.post

``` text
"/api/v1/conversations"
```

json=

``` text
"title": "Incidente"
"unexpected": "value"
}
```

assert response.status_code == 42

## 339. Formato uniforme de errore

Los errores deberán seguir un contrato común

Ejemplo

``` text
"error":
"code": "conversation_not_found"
"message": "Conversation was not found."
"details": {}
"correlation_id": "corr-001
{
```

)

,

:

:

:

;

;

``` text
{
```

;

.

``` text
{
```

.

;

;

,

;

;

fi .

;

,

,

,

.

``` text
"
```

(

2

s

,

.

s

,

El contrato deberá separar

-   código estable
-   mensaje legible
-   detalles estructurados
-   identi cador de trazabilidad

## 340. Testing de errores de validació

Los errores de validación deberán transformarse al formato o cial

Ejemplo

response = await api_client.post

``` text
"/api/v1/conversations"
```

json=

``` text
"title": ""
}
```

body = response.json(

assert response.status_code == 42 assert body\["error"\]\["code"\] ==
"validation_error assert body\["error"\]\["details"\]\[0\]\["field"\]
=="title No deberá exponerse la estructura interna de errores de
Pydantic sin una decisión explícita

## 341. Mapeo de errores de domini

Los handlers de excepciones deberán traducir

Código Error interno HTTP Recurso inexistente 404 Autenticación ausente
o inválida 401 Autorización denegada 403 Con icto o duplicidad 409
Validación externa 422 )

``` text
}

}
```

fl fi ,

:

``` text
{
```

;

;

;

:

.

,

)

,

:

(

2

o

n

fi .

``` text
"

"
```

.

Rate limit 429 Error recuperable de 503 dependencia Timeout de
dependencia 504 Error inesperado 500

La tabla podrá ajustarse por contrato especí co

## 342. Errores inesperado

Los errores inesperados deberán

-   devolver un mensaje seguro
-   incluir correlation ID
-   registrar stack trace internamente
-   no exponer nombres de tablas
-   no exponer SQL
-   no exponer rutas del sistema
-   no exponer secretos
-   no exponer con guración interna Ejemplo

assert response.status_code == 50 assert
response.json()\["error"\]\["code"\] ==

``` text
"internal_server_error
```

assert "Traceback" not in response.tex

## 343. Autenticació

Los API Tests deberán cubrir

-   token válido
-   token ausente
-   token expirado
-   rma inválida
-   issuer incorrecto
-   audience incorrecta
-   usuario deshabilitado
-   sesión revocada
-   algoritmo no permitido )

fi :

;

;

;

;

fi ;

;

;

;

;

;

;

.

n

;

;

:

;

:

.

;

s

``` text
"
```

fi .

0

t

(

## 344. Código 40

Una respuesta 401 Unauthorized deberá incluir el header apropiado cuando
corresponda

assert response.status_code == 40 assert
response.headers\["WWW-Authenticate"\] == "Bearer No se utilizará 403
para indicar simplemente que no existen credenciales válidas

## 345. Autorizació

Cada endpoint protegido deberá probar

-   rol permitido
-   rol denegado
-   permiso especí co
-   recurso propio
-   recurso de otro usuario
-   recurso de otro tenant
-   actor deshabilitado
-   policy condicionada No deberá asumirse que la cobertura del
    Application Handler sustituye las pruebas de wiring de autorización
    en la API

## 346. Prevención de enumeració

Las APIs deberán evitar revelar la existencia de recursos de otros
tenants

Ejemplo

response = await tenant_a_client.get

``` text
"/api/v1/documents/document-from-tenant-b
```

assert response.status_code == 40 La política podrá utilizar 404 en vez
de 403 para evitar enumeración, según el recurso

## 347. Tenant Resolutio

El tenant podrá resolverse mediante )

:

;

;

;

fi ;

;

.

;

.

;

1

n

n

:

:

4

1

n

(

``` text
"
```

.

``` text
"
```

.

.

.

-   claims del token
-   subdominio
-   encabezado interno con able
-   contexto del gateway No deberá con arse en un tenant_id enviado
    libremente por el cliente sin validación

Los tests deberán intentar falsi car el tenant

## 348. Headers de tenan

Cuando exista un header de tenant, deberá probarse

-   ausencia
-   valor válido
-   valor malformado
-   valor no autorizado
-   con icto con el token
-   manipulación
-   propagación al caso de uso La fuente de autoridad deberá estar de
    nida

## 349. Idempotency-Key HTT

Los endpoints idempotentes deberán aceptar un header estandarizado

Ejemplo

Idempotency-Key: request-00 Los tests deberán cubrir

-   primera solicitud
-   repetición idéntica
-   repetición con payload diferente
-   clave ausente cuando sea obligatoria
-   longitud excesiva
-   expiración
-   concurrencia

## 350. Respuesta idempotent

La repetición de una solicitud idéntica deberá devolver el mismo
resultado funcional fl :

;

;

;

;

.

;

fi ;

;

;

;

;

;

.

;

fi :

.

;

fi ;

t

;

fi 1

e

.

.

P

:

.

.

.

La API deberá de nir si conserva también

-   status code original
-   body original
-   headers relevantes
-   identi cador del recurso

## 351. Códigos de éxit

La suite deberá validar códigos apropiados

Código Operación habitual Lectura exitosa 200 Creación 201 Acción
aceptada 202 asíncrona Operación sin body 204 Actualización completa 200
o 204 Eliminación 204

La elección deberá ser consistente por recurso

## 352. Header Locatio

Una creación podrá incluir

Location: /api/v1/conversations/conversation-00 Cuando forme parte del
contrato, deberá probarse

## 353. Respuestas 20

Una respuesta 204 No Content no deberá incluir body

assert response.status_code == 20 assert response.content == b"

## 354. Serialización de fecha

fi ;

fi ;

;

.

:

4

o

n

:

s

.

``` text
"
```

.

4

.

.

1

Las fechas deberán devolverse en ISO 8601 con zona horaria

Ejemplo

``` text
"created_at": "2026-07-22T18:00:00Z
```

Los tests deberán comprobar

-   formato
-   UTC
-   precisión
-   campos nulos
-   consistencia

## 355. Serialización de identi cadore

Los identi cadores deberán tener una representación estable

No deberán cambiar accidentalmente entre

-   UUID
-   integer
-   ULID
-   string pre jado El contrato externo no deberá depender del tipo
    físico de la base de datos

## 356. Enums en AP

Los enums deberán serializarse mediante valores documentados

Ejemplo

``` text
"status": "pending_approval
```

No deberán exponerse

-   índices numéricos internos
-   nombres de clase
-   valores no documentados

## 357. Campos opcionale

``` text
}

}

{

{
```

;

;

;

;

;

:

:

;

fi fi .

;

.

;

:

.

;

:

I

s

:

fi

``` text
"

"
```

s

.

.

.

.

Los tests deberán de nir la diferencia entre

-   campo ausente
-   campo con null
-   campo vacío
-   valor predeterminado Esto será especialmente relevante en PATCH

## 358. PUT y PATC

La semántica deberá probarse

PU

Representa reemplazo completo cuando así se de na

PATC

Representa modi cación parcial

Los tests deberán veri car que los campos ausentes en PATCH no sean
borrados involuntariamente

## 359. Paginación de AP

La respuesta paginada deberá tener un contrato estable

Ejemplo

``` text
"items": []
"page":
"next_cursor": "cursor-value"
"has_more": tru
```

Los tests deberán cubrir

-   primera página
-   página intermedia
-   última página
-   lista vacía

``` text
{

}

}
```

T

H

:

;

;

;

;

``` text
{
```

;

fi ;

;

.

,

fi .

fi :

H

e

.

.

I

:

.

fi ,

.

.

-   cursor inválido
-   límite superior
-   orden estable

## 360. Límites de paginació

El endpoint deberá aplicar

-   valor predeterminado
-   mínimo
-   máximo
-   error o normalización Ejemplo

response = await api_client.get

``` text
"/api/v1/conversations?limit=10000
```

assert response.status_code == 42 No deberá permitirse que el cliente
solicite una cantidad ilimitada

## 361. Filtro

Los tests deberán cubrir

-   ltro individual
-   combinación
-   valores inválidos
-   ltros vacíos
-   fechas
-   enums
-   tenant
-   permisos
-   campos no soportados Los ltros no deberán convertirse directamente
    en fragmentos SQL

## 362. Ordenamient

La API deberá permitir únicamente campos autorizados

Ejemplo )

fi fi fi ;

;

;

;

;

:

:

;

;

;

.

;

;

;

s

;

;

.

.

:

:

o

n

(

2

.

``` text
"
```

.

.

sort=-created_at,titl Los tests deberán rechazar

-   columnas internas
-   expresiones SQL
-   campos sensibles
-   combinaciones inválidas

## 363. Búsqued

Los endpoints de búsqueda deberán probar

-   query vacía
-   longitud mínima
-   caracteres especiales
-   Unicode
-   resultados vacíos
-   límites
-   ltros
-   permisos
-   protección contra inyección

## 364. Upload

Los endpoints de carga deberán probar

-   archivo válido
-   ausencia de archivo
-   lename vacío
-   content type inválido
-   extensión no permitida
-   tamaño excesivo
-   archivo vacío
-   nombre malicioso
-   contenido inconsistente
-   carga interrumpida

## 365. Validación de archivo

La validación no deberá con ar únicamente en

-   extensión
-   MIME enviado por el cliente fi fi ;

;

;

;

;

;

;

;

;

;

;

;

;

;

;

;

.

s

;

;

;

a

;

;

.

:

.

fi ;

e

:

s

:

:

-   nombre del archivo Podrá incluir

-   detección de tipo

-   magic bytes

-   límites

-   antivirus

-   análisis seguro Los tests deberán demostrar la política implementada

## 366. Path Traversal en upload

Ejemplo de entrada

../../../../etc/passw El nombre deberá

-   rechazarse
-   normalizarse
-   almacenarse sin afectar la ruta interna La API no deberá devolver
    rutas físicas

## 367. Upload asíncron

Cuando el procesamiento sea asíncrono, la respuesta podrá ser

202 Accepte con

``` text
"document_id": "document-001"
"status": "uploaded"
"job_id": "job-001
```

Los tests deberán validar que la solicitud no a rme que el documento ya
está listo

## 368. Download

Los downloads deberán probar

-   recurso válido

``` text
{

}
```

:

;

;

;

;

;

:

;

.

d

;

:

:

.

s

``` text
"
```

:

d

,

o

.

.

fi ,

s

.

:

.

-   recurso inexistente
-   tenant incorrecto
-   permiso insu ciente
-   lename seguro
-   content type
-   content disposition
-   range requests cuando se soporten

## 369. Signed URL

Si se utilizan URLs rmadas, deberán probarse

-   expiración
-   alcance
-   recurso
-   método permitido
-   tenant
-   manipulación
-   revocación cuando exista No deberán exponerse credenciales del
    storage

## 370. Server-Sent Event

SSE se utilizará para streaming unidireccional cuando así lo de na la
arquitectura

Los tests deberán cubrir

-   content type
-   formato de eventos
-   orden
-   nalización
-   errores
-   cancelación
-   heartbeat
-   correlation
-   reconexión cuando aplique

## 371. Content Type de SS

La respuesta deberá incluir

Content-Type: text/event-strea fi fi ;

;

;

;

;

;

;

;

;

;

;

;

fi ;

;

;

;

;

;

;

fi ;

:

.

.

:

s

.

s

E

m

.

:

fi .

Cache-Control: no-cach Podrán incluirse headers adicionales conforme al
gateway y proxy

## 372. Formato de eventos SS

Ejemplo

event: message.delt id: evt-00 data: {"content":"Hola"

event: message.complete id: evt-00 data: {"message_id":"message-001" Los
tests deberán validar que cada evento sea parseable y corresponda al
schema o cial

## 373. Orden de eventos SS

El ujo deberá respetar una secuencia válida

Ejemplo

message.starte message.delta tool.requested tool.result message.complete
No deberá enviarse message.completed antes de los deltas asociados

## 374. Errores durante streamin

Una vez iniciada la respuesta HTTP, no siempre será posible cambiar el
status code

Los errores deberán comunicarse mediante un evento estructurado

Ejemplo

event: erro data:

``` text
"code": "model_provider_timeout"
"retryable": tru
```

fl :

:

:

``` text
{
```

1

2

r

?

-   

?

d

d

e

a

e

d

``` text
}
```

E

E

.

g

``` text
}
```

,

.

.

.

fi .

.

Los tests deberán comprobar que el stream nalice de forma controlada

## 375. Cancelación del client

Al desconectarse el cliente, el sistema deberá

-   detectar cancelación
-   detener trabajo innecesario cuando sea seguro
-   liberar recursos
-   registrar el estado
-   no completar indebidamente el mensaje
-   evitar ejecutar tools posteriores

## 376. Heartbeat

Los streams largos podrán enviar heartbeats

Los tests deberán comprobar

-   intervalo
-   formato
-   que no alteren el contenido
-   que no se persistan como mensajes
-   compatibilidad con proxies Los tests ordinarios utilizarán reloj
    controlado

## 377. Reanudación del strea

Cuando se soporte Last-Event-ID, deberán probarse

-   identi cador válido
-   identi cador desconocido
-   evento expirado
-   replay
-   ausencia de duplicados
-   autorización del stream original

## 378. Rate Limitin

``` text
}
```

fi fi ;

;

;

;

;

;

;

;

;

s

;

;

.

g

:

.

.

;

;

e

m

fi .

:

;

.

:

.

Los API Tests deberán validar

-   límite por usuario
-   límite por tenant
-   límite por IP cuando aplique
-   ventanas
-   costo por endpoint
-   bypass interno autorizado
-   respuesta
-   headers

## 379. Respuesta 42

Una respuesta de rate limit deberá incluir

Retry-After: 3 y un error estructurado

assert response.status_code == 42 assert
int(response.headers\["Retry-After"\]) \> assert
response.json()\["error"\]\["code"\] ==

``` text
"rate_limit_exceeded
```

## 380. Rate Limit por cost

Las operaciones de IA podrán consumir cuotas diferentes

Ejemplo

-   consulta ordinaria: 1 unidad
-   carga de documento: 5 unidades
-   análisis largo: 10 unidades Los tests deberán veri car que el
    endpoint comunique correctamente el costo al componente responsable

## 381. COR

Las pruebas deberán validar

-   orígenes permitidos
-   orígenes rechazados )

.

:

;

;

.

S

;

;

;

;

;

0

fi .

;

.

;

:

;

9

:

;

``` text
"
```

o

:

9

.

(

0

-   métodos
-   headers
-   credentials
-   pre ight
-   con guración por ambiente No deberá utilizarse \* junto con
    credenciales en producción

## 382. CSR

Si la autenticación utiliza cookies, deberán existir pruebas de CSRF

Si utiliza exclusivamente Bearer tokens fuera de cookies, deberá
documentarse por qué el control no aplica de la misma manera

## 383. Security Header

Cuando sean responsabilidad de la API o gateway, deberán probarse

-   Content-Security-Policy
-   X-Content-Type-Options
-   Referrer-Policy
-   Strict-Transport-Security
-   políticas de frame
-   cache para contenido sensible La ubicación del control deberá estar
    documentada

## 384. Cache Header

Los endpoints sensibles deberán evitar cache compartido

Ejemplo

Cache-Control: no-stor Los endpoints públicos o inmutables podrán
utilizar cache explícito

## 385. Compresió

Cuando se habilite compresión, deberán probarse fl fi ;

:

;

;

;

F

;

;

n

.

.

.

s

e

;

s

;

;

:

.

.

.

.

.

:

-   contenido elegible
-   Accept-Encoding
-   tamaño mínimo
-   SSE excluido cuando corresponda
-   headers
-   payload reconstruido

## 386. Health Check

La API deberá exponer al menos

-   liveness

-   readiness Podrá exponer adicionalmente

-   startup

-   diagnostics internos protegidos

## 387. Livenes

Liveness deberá indicar si el proceso está vivo

No deberá depender de todos los servicios externos

Ejemplo

response = await api_client.get

``` text
"/health/live
```

assert response.status_code == 20 assert response.json()\["status"\] ==
"alive

## 388. Readines

Readiness deberá indicar si la instancia puede recibir trá co

Podrá validar

-   PostgreSQL
-   Redis
-   con guración crítica
-   migraciones )

fi ;

;

;

;

:

.

;

;

:

;

;

s

;

.

s

;

``` text
"
```

s

:

.

:

;

.

(

0

.

fi .

``` text
"
```

-   proveedores indispensables
-   storage Los checks deberán tener timeout

## 389. Readiness degradad

La política deberá de nir qué dependencias son

-   obligatorias

-   degradables

-   opcionales Ejemplo

-   PostgreSQL caído: no ready

-   proveedor secundario caído: ready degradado

-   servicio de métricas caído: posiblemente ready Los tests deberán
    veri car la matriz

## 390. Health Check segur

Los health checks públicos no deberán revelar

-   connection strings
-   nombres internos
-   versiones sensibles
-   errores completos
-   topología Podrán devolver únicamente estado general

## 391. Versionado de AP

La primera versión utilizará rutas versionadas

``` text
/api/v1
```

Los tests deberán asegurar que

-   las rutas o ciales incluyan versión
-   no existan endpoints accidentales sin versión
-   los cambios incompatibles creen nueva versión
-   las versiones soportadas permanezcan operativas .

:

.

fi /

.

;

;

;

;

;

;

fi fi ;

;

:

.

;

.

I

o

a

.

;

;

:

:

.

;

:

.

## 392. Deprecació

Una ruta o campo deprecado deberá

-   permanecer documentado durante el período acordado
-   emitir headers o metadata cuando se de na
-   tener fecha de retiro
-   conservar pruebas hasta su eliminación
-   contar con ruta de migración

## 393. Compatibilidad hacia atrá

Los API Tests deberán veri car que un cambio compatible

-   no elimine campos obligatorios existentes
-   no cambie tipos
-   no cambie semántica
-   no vuelva obligatorio un campo opcional
-   no reduzca enums válidos
-   no altere códigos HTTP sin versionado

## 394. OpenAPI en API Test

La aplicación deberá generar un documento OpenAPI válido

La suite deberá veri car

-   generación
-   rutas
-   schemas
-   seguridad
-   códigos
-   examples
-   operation IDs
-   ausencia de endpoints internos no deseados El análisis detallado
    pertenecerá al capítulo de contratos

## 395. Operation ID

Cada operación deberá poseer un identi cador estable y único

Ejemplo ;

;

;

:

;

;

;

;

;

fi ;

;

:

n

;

fi .

s

:

.

;

fi fi ;

;

s

;

.

s

;

.

:

.

.

createConversatio sendConversationMessag uploadKnowledgeDocumen
approveToolExecutio Estos IDs podrán ser utilizados por

-   clientes generados
-   SDKs
-   documentación
-   observabilidad

## 396. Pruebas de documentación interactiv

La documentación automática deberá estar

-   habilitada en entornos permitidos
-   protegida o deshabilitada en producción según política
-   alineada con OpenAPI
-   libre de rutas administrativas accidentales

## 397. Request Size Limit

La API deberá imponer límites a

-   JSON
-   uploads
-   headers
-   query strings
-   cantidad de campos
-   arrays
-   contenido de mensajes Los tests deberán veri car rechazo temprano y
    seguro

## 398. HTTP Method Restriction

Los endpoints deberán aceptar únicamente métodos documentados

Ejemplo

response = await api_client.delete

``` text
"/api/v1/health/live
```

)

;

;

;

;

;

:

;

.

;

;

;

fi ;

.

n

n

:

e

t

;

:

``` text
"
```

s

.

:

s

(

.

;

.

a

assert response.status_code == 40 El header Allow deberá ser correcto
cuando corresponda

## 399. Content Negotiatio

Cuando se soporte más de una representación, deberán probarse

-   Accept
-   tipo soportado
-   tipo no soportado
-   valor predeterminado
-   versionado por media type si se adopta Inicialmente se preferirá
    JSON para APIs ordinarias y SSE para streaming

## 400. Localizació

Los códigos de error deberán permanecer estables independientemente del
idioma

Si los mensajes se traducen, deberán probarse

-   Accept-Language
-   fallback
-   idioma no soportado
-   ausencia de traducción
-   campos estructurados

## 401. Auditoría en AP

La API deberá propagar

-   actor
-   tenant
-   IP cuando corresponda
-   user agent
-   correlation ID
-   endpoint
-   método No deberá con arse ciegamente en headers reenviados por
    clientes externos ;

;

.

;

;

;

;

;

;

fi ;

;

;

.

;

;

;

:

n

I

n

.

:

5

.

:

.

.

.

## 402. Correlation I

La API deberá

-   aceptar un correlation ID válido o generar uno
-   validarlo
-   devolverlo
-   propagarlo
-   incluirlo en errores Ejemplo

response = await api_client.get

``` text
"/api/v1/conversations"
```

headers=

``` text
"X-Correlation-ID": "corr-001"
}
```

assert response.headers

``` text
"X-Correlation-ID
] == "corr-001
```

## 403. Trusted Proxy Header

Los tests desplegados deberán validar la interpretación de

-   X-Forwarded-For
-   X-Forwarded-Proto
-   Forwarded
-   host
-   scheme Solo deberán con arse cuando provengan de proxies autorizados

## 404. API Smoke Test

Después del despliegue deberán ejecutarse pruebas rápidas

-   liveness
-   readiness
-   autenticación
-   endpoint de lectura
-   endpoint de escritura controlado
-   streaming básico )

;

.

,

;

:

;

;

;

;

;

;

:

;

fi

``` text
{
```

.

;

``` text
"
```

;

;

D

``` text
"
```

;

s

``` text
[
```

,

s

;

(

,

:

:

.

-   acceso denegado
-   versión Los smoke tests no deberán modi car datos productivos
    permanentes

## 405. Anti-patterns de API Testin

Testing FastAPI Internal

Valida comportamiento propio del framework

Direct Handler Invocatio

Se llama la función de ruta sin atravesar HTTP

Database for Every API Tes

Hace lenta toda la suite sin necesidad

Missing Negative Path

Solo prueba respuestas 200

Unstable Full-Body Assertion

Compara campos dinámicos irrelevantes

Shared Authentication Toke

Un token mutable se reutiliza entre escenarios

Tenant from Client Bod

Confía en tenant enviado libremente

Production Endpoint Testin

Pruebas destructivas ejecutadas contra producción

## 406. Checklist de API Testin

.

;

s

.

y

s

n

fi t

g

n

.

s

.

.

g

.

.

.

.

g

.

Cada endpoint deberá responder

-   ¿Qué método utiliza
-   ¿Cuál es su ruta versionada
-   ¿Qué autenticación requiere
-   ¿Qué permisos exige
-   ¿Cómo resuelve el tenant
-   ¿Cuál es el request schema
-   ¿Cuál es el response schema
-   ¿Qué códigos devuelve
-   ¿Qué errores puede producir
-   ¿Es idempotente
-   ¿Tiene límites
-   ¿Tiene rate limiting
-   ¿Expone datos sensibles
-   ¿Genera auditoría
-   ¿Tiene pruebas negativas
-   ¿Está documentado en OpenAPI

## 407. De nition of Done del capítul

API Testing se considerará implementado cuando

-   exista una application factory
-   HTTPX pruebe la aplicación mediante ASGI
-   las dependencias puedan sustituirse
-   autenticación y autorización estén cubiertas
-   el tenant no pueda falsi carse
-   exista formato uniforme de errores
-   códigos y headers estén validados
-   paginación y ltros sean deterministas
-   uploads tengan controles de seguridad
-   SSE posea contratos de eventos
-   health checks estén diferenciados
-   rate limiting esté probado
-   OpenAPI re eje las rutas reales
-   existan smoke tests desplegados fi fl fi ?

?

?

?

?

?

fi ?

?

?

?

;

?

?

?

?

?

;

;

;

;

.

:

?

;

;

;

;

;

;

;

;

:

o

## Capítulo 10 --- Contract Testin

## 408. Propósit

Los Contract Tests validan que las interfaces compartidas entre
componentes, servicios, clientes y proveedores permanezcan compatibles

Su objetivo consiste en detectar cambios incompatibles antes de que
lleguen a integración o producción

Un contrato podrá describir

-   una API HTTP
-   un evento
-   un mensaje de cola
-   una herramienta
-   un provider adapter
-   un archivo
-   un schema
-   un protocolo de streaming
-   un MCP capability Los contratos deberán ser explícitos, versionados
    y veri cables automáticamente

## 409. Tipos de contrato

La arquitectura reconocerá

### 409.1 Synchronous Contract

-   HTTP request/response

-   llamadas internas tipadas

-   adapters de proveedores

-   MCP requests \### 409.2 Asynchronous Contract

-   eventos

-   comandos de cola

-   jobs

-   Outbox messages

-   webhooks \### 409.3 Data Contract

;

;

;

.

;

;

.

.

;

;

;

;

.

;

;

o

;

;

;

s

;

:

:

s

s

s

.

fi g

.

-   JSON Schema

-   OpenAPI

-   archivos

-   datasets

-   estructuras de storage

-   schemas de tools \### 409.4 Behavioral Contract

-   idempotencia

-   errores

-   retries

-   orden

-   timeouts

-   versionado

-   semántica

## 410. Principio de compatibilida

Todo cambio de contrato deberá clasi carse como

-   compatible

-   potencialmente incompatible

-   incompatible Los cambios incompatibles requerirán

-   nueva versión

-   período de transición

-   migración

-   aprobación arquitectónica

-   comunicación a consumidores

## 411. Fuente de verda

Cada contrato deberá poseer una fuente de verdad de nida

Ejemplos

Contrato Fuente de verdad API REST OpenAPI Tool inputs JSON Schema
Schema Registry o archivos Eventos versionados ;

;

;

;

;

;

:

;

.

;

;

;

.

;

;

;

.

;

;

;

;

.

s

d

fi :

d

:

fi .

MCP Especi cación y capabilities Provider Protocol interno + contract
suite Adapter SSE Event schemas versionados

No deberán mantenerse múltiples de niciones manuales divergentes

## 412. OpenAPI Validatio

La suite deberá validar el documento OpenAPI generado

Ejemplo conceptual

``` text
from openapi_spec_validator import
```

validate_spec

``` text
def test_openapi_document_is_valid(app)
```

schema = app.openapi(

validate_spec(schema La validación deberá ejecutarse en CI

## 413. OpenAPI Completenes

La suite deberá veri car

-   título
-   versión
-   servidores permitidos
-   seguridad
-   tags
-   operation IDs
-   parámetros
-   request bodies
-   responses
-   schemas
-   examples
-   deprecaciones )

;

;

fi ;

;

;

;

;

;

;

.

;

fi :

;

:

,

)

fi )

.

n

s

(

.

:

.

## 414. Rutas no documentada

Toda ruta pública deberá aparecer en OpenAPI, salvo exclusión deliberada

La suite deberá detectar

-   rutas registradas pero no documentadas
-   rutas documentadas pero inexistentes
-   métodos ausentes
-   pre jos inconsistentes

## 415. Endpoints interno

Los endpoints internos deberán

-   estar separados
-   utilizar seguridad especí ca
-   excluirse de documentación pública cuando corresponda
-   tener contratos propios
-   no ser accesibles desde el gateway público Los tests deberán veri
    car esa separación

## 416. OpenAPI Security Scheme

Los esquemas de autenticación deberán documentarse

Ejemplo

components securitySchemes bearerAuth type: htt scheme: beare
bearerFormat: JW Cada operación protegida deberá declarar el esquema
correspondiente

## 417. Responses documentada

Cada endpoint deberá documentar

-   éxito fi ;

:

:

;

;

:

fi .

p

;

:

fi :

;

r

:

T

:

s

;

;

.

.

s

s

s

.

;

.

.

-   validación
-   autenticación
-   autorización
-   inexistencia
-   con icto
-   rate limit
-   errores relevantes No será obligatorio documentar todos los fallos
    internos impredecibles, pero sí el error general 500

## 418. Error Schem

Todos los errores deberán reutilizar el schema común

Ejemplo conceptual

ErrorResponse type: objec required - erro properties error \$ref:
"#/components/schemas/Error La suite deberá detectar endpoints con
respuestas de error divergentes

## 419. OpenAPI Snapshot

El documento OpenAPI podrá conservarse como snapshot versionado

Cada Pull Request deberá mostrar diferencias

Las modi caciones deberán revisarse para detectar

-   campos eliminados
-   tipos cambiados
-   códigos removidos
-   parámetros nuevos obligatorios
-   enums restringidos
-   rutas modi cadas

## 420. Breaking Change Detectio

fl .

;

;

fi ;

fi ;

;

;

:

r

:

;

.

.

:

;

;

;

t

:

:

a

;

s

.

n

:

.

``` text
"
```

.

.

CI deberá ejecutar una herramienta de comparación OpenAPI

Un cambio será potencialmente incompatible cuando

-   elimine endpoint
-   elimine método
-   elimine campo de respuesta
-   cambie tipo
-   vuelva obligatorio un campo
-   reduzca valores de enum
-   modi que parámetro
-   cambie código de éxito
-   cambie seguridad
-   reduzca límites aceptados

## 421. Cambios compatibles en OpenAP

Generalmente podrán considerarse compatibles

-   agregar campo opcional de respuesta
-   agregar endpoint
-   agregar código de error documentado
-   agregar parámetro opcional
-   ampliar enum aceptado en request, con cautela
-   mejorar descripciones La compatibilidad semántica deberá evaluarse
    además de la estructural

## 422. Tolerancia de consumidore

Agregar un campo a una respuesta solo será compatible cuando los
consumidores toleren campos desconocidos

Los SDKs y clientes deberán con gurarse de acuerdo con esta política

No deberá asumirse compatibilidad universal

## 423. JSON Schem

JSON Schema será utilizado para

-   inputs de tools
-   outputs de tools fi ;

.

;

;

;

;

;

;

;

.

;

;

.

;

;

a

;

fi :

;

;

.

;

:

s

:

I

.

.

.

-   eventos
-   jobs
-   archivos estructurados
-   respuestas de modelos
-   con guraciones seleccionadas La versión del estándar deberá jarse
    explícitamente

## 424. Validación de schema

Cada schema deberá probar

-   instancia válida
-   ausencia de requeridos
-   tipos inválidos
-   campos adicionales
-   límites
-   enums
-   formatos
-   objetos anidados
-   arrays
-   nulos
-   ejemplos o ciales

## 425. Schemas cerrado

Cuando no se permitan campos adicionales se utilizará

``` text
"additionalProperties": fals
```

La decisión deberá aplicarse conscientemente

En herramientas ejecutables se preferirán schemas estrictos para reducir
ambigüedad

## 426. Versionado de schema

Cada schema compartido deberá poseer

-   nombre
-   versión
-   propietario

``` text
}

{
```

fi ;

;

;

;

;

;

;

;

;

fi ;

;

;

;

.

;

;

;

;

:

.

fi s

:

s

s

e

.

.

:

.

-   estado
-   fecha
-   compatibilidad
-   ejemplos Ejemplo

tool.search_documents.input.v1.schema.jso No deberá sobrescribirse un
schema publicado con cambios incompatibles

## 427. Identi cadores de schem

Los schemas podrán incluir \$id

Ejemplo

``` text
"$id": "https://schemas.geem.ai/tools/search-documents/input/
```

v1"

``` text
"$schema": "https://json-schema.org/draft/2020-12/schema
```

La URL funcionará como identi cador aunque no necesariamente sea pública

## 428. Contratos de Tool Callin

Cada herramienta deberá de nir

-   nombre estable
-   descripción
-   input schema
-   output schema
-   permisos
-   nivel de riesgo
-   aprobación
-   timeout
-   idempotencia
-   errores
-   versión

## 429. Tool Input Contract

La suite deberá veri car que los argumentos generados

``` text
{

}
```

,

;

;

;

.

;

:

:

.

;

;

;

;

;

;

;

;

;

fi fi fi fi :

.

s

g

a

:

n

.

.

``` text
"
```

-   cumplan el schema
-   no incluyan campos inesperados
-   respeten enums
-   respeten formatos
-   tengan límites
-   no incluyan tenant manipulable cuando se obtiene del contexto

## 430. Tool Output Contract

Toda implementación deberá devolver un resultado conforme al schema

Ejemplo

result = await tool.execute(arguments

validate instance=result schema=tool.output_schema

Los errores deberán utilizar un contrato separado y no simular
resultados exitosos

## 431. Tool Contract Suit

Una suite común deberá aplicarse a cada tool

Deberá validar

-   metadata
-   schema válido
-   ejecución válida
-   argumentos inválidos
-   timeout
-   cancelación
-   permisos
-   idempotencia
-   redacción de datos sensibles
-   resultado serializable

## 432. Evolución de Tool

Un cambio incompatible deberá crear una nueva versión )

;

:

;

;

;

(

;

;

;

:

;

;

;

;

.

;

;

,

;

s

e

s

,

.

)

.

.

.

.

Ejemplo

search_documents.v search_documents.v Podrá mantenerse el mismo nombre
visible si el registry administra versiones explícitas

El modelo no deberá recibir simultáneamente versiones ambiguas sin una
política

## 433. Contratos de evento

Cada evento deberá de nir

-   event_id
-   event_type
-   event_version
-   occurred_at
-   tenant_id
-   correlation_id
-   causation_id
-   payload
-   metadata Ejemplo

``` text
"event_id": "event-001"
"event_type": "conversation.created"
"event_version": 1
"occurred_at": "2026-07-22T18:00:00Z"
"tenant_id": "tenant-001"
"correlation_id": "corr-001"
"payload":
"conversation_id": "conversation-001"
"owner_id": "user-001
```

## 434. Event Envelop

El envelope deberá permanecer estable entre tipos de evento

Esto permitirá que infraestructura común procese

-   routing

``` text
{

}

}
```

;

;

:

:

.

;

;

;

;

;

``` text
{
```

;

;

fi :

2

1

,

e

``` text
"
```

,

s

,

,

:

,

,

.

,

.

.

-   observabilidad
-   retries
-   auditoría
-   DLQ
-   replay El payload será especí co del evento

## 435. Event Type Namin

Se utilizará una convención estable

Ejemplo

conversation.create conversation.archive knowledge.document.uploade
tool.execution.requeste approval.request.approve No deberán utilizarse
nombres de clases Python como contrato externo

## 436. Event Versio

La versión deberá ser explícita

Opciones

-   campo event_version
-   tipo versionado
-   schema registry La estrategia deberá ser uniforme

## 437. Compatibilidad de evento

Agregar un campo opcional podrá ser compatible

Generalmente serán incompatibles

-   eliminar campo
-   cambiar signi cado
-   cambiar tipo
-   renombrar ;

.

;

:

;

:

;

;

fi ;

;

.

;

;

fi ;

n

d

d

.

.

d

:

.

d

.

g

d

s

.

.

-   hacer obligatorio un campo nuevo
-   cambiar unidad
-   cambiar zona horaria
-   cambiar semántica de identi cador

## 438. Upcastin

Los consumidores podrán utilizar upcasters para transformar eventos
antiguos al modelo actual

Ejemplo

ConversationCreatedV ↓ upcas ConversationCreatedV Los upcasters deberán
tener pruebas con xtures históricas

## 439. Downcastin

El downcasting será menos común y deberá evitarse cuando implique
pérdida de información

La compatibilidad con consumidores antiguos se logrará preferentemente
manteniendo la versión anterior durante la transición

## 440. Fixtures histórica

El repositorio deberá conservar ejemplos de eventos publicados

tests/contracts/events/fixtures

``` text
├── conversation.created.v1.jso
├── document.uploaded.v1.jso
└── tool.execution.requested.v1.jso
```

Los productores actuales deberán validar compatibilidad conforme a la
política

## 441. Contratos de mensajes de col

Los mensajes de jobs deberán de nir

-   tipo
-   versión ;

;

:

;

;

g

t

g

fi .

2

1

fi ;

.

s

:

fi n

/

n

n

a

.

.

.

.

.

-   job ID
-   idempotency key
-   tenant
-   intentos
-   timestamps
-   payload
-   tracing
-   prioridad cuando exista

## 442. Comandos vs evento

Un mensaje deberá identi carse como

Comman

Solicita que algo ocurra

Ejemplo

process.documen Even

Informa que algo ocurrió

Ejemplo

document.processe No deberán confundirse sus semánticas

## 443. Queue Contract Test

La suite deberá validar

-   serialización
-   deserialización
-   schema
-   headers
-   versión
-   tamaño
-   idempotencia
-   retry metadata
-   DLQ compatibility ;

t

;

;

;

;

;

;

;

;

:

:

;

d

;

;

;

;

;

.

t

:

.

.

.

fi d

:

.

s

s

## 444. Tamaño de mensaje

Los contratos deberán imponer límites

Cuando el contenido sea grande, el mensaje deberá incluir una referencia
a Object Storage en vez del payload completo

Los tests deberán rechazar mensajes superiores al límite establecido

## 445. Contratos de Outbo

El Outbox deberá conservar su ciente información para publicar el
contrato exacto

La suite deberá comparar

-   evento de dominio
-   mensaje Outbox
-   mensaje publicado No deberá perderse metadata durante las
    transformaciones

## 446. Consumer-Driven Contract Testin

Cuando existan consumidores independientes, podrán utilizarse contratos
dirigidos por consumidores

El consumidor declara

-   solicitud esperada
-   respuesta necesaria
-   campos utilizados
-   errores esperados El proveedor veri ca esos contratos en CI

## 447. Uso recomendado de Consumer-Driven Contract

Será especialmente útil cuando

-   frontend y backend evolucionen de forma independiente
-   existan microservicios
-   terceros consuman APIs .

;

.

fi ;

;

;

.

;

.

;

:

;

:

fi :

.

s

x

.

;

.

g

.

.

s

-   haya SDKs
-   varios equipos compartan eventos No será obligatorio para
    componentes mantenidos conjuntamente dentro del mismo repositorio si
    OpenAPI y las suites de integración ofrecen cobertura su ciente

## 448. Contratos frontend--backen

El frontend deberá consumir tipos generados o validados desde OpenAPI
cuando sea viable

Los tests deberán detectar

-   campos faltantes
-   enums divergentes
-   rutas cambiadas
-   errores no manejados
-   cambios de nullability No deberán mantenerse manualmente tipos
    TypeScript duplicados sin veri cación

## 449. Generación de cliente

La generación de SDKs deberá ser reproducible

CI podrá veri car que

-   el cliente generado está actualizado
-   no existen diferencias sin commit
-   los operation IDs son estables
-   los tipos compilan
-   ejemplos básicos funcionan

## 450. Contratos con proveedores de modelo

Los proveedores externos serán encapsulados detrás del ModelProvider o
ModelGateway

El contrato interno deberá de nir

-   request
-   response
-   streaming
-   tool calls
-   usage
-   nish reason fi ;

;

;

;

;

;

;

fi ;

;

;

;

;

:

.

:

.

fi ;

:

;

.

;

s

.

d

fi .

s

fi .

.

.

-   errores
-   cancelación
-   timeout

## 451. Provider Contract Suit

Cada adapter de proveedor deberá superar la misma suite

Ejemplo conceptual

``` text
class ModelProviderContract
async def test_generates_text
```

self provider ) response = await provider.generate standard_request(

assert isinstance response ModelResponse

assert response.conten La suite podrá ejecutarse contra

-   fake provider
-   sandbox
-   proveedor real controlado

## 452. Mapeo de nish reason

Los proveedores utilizan valores diferentes

El contrato interno deberá normalizarlos

Ejemplo

Proveedor Interno stop completed max_token length s tool_calls tool_call
;

:

.

;

:

;

)

)

;

,

:

,

fi .

,

:

(

,

.

:

.

)

e

s

t

(

.

(

content\_ lte blocked r

Los tests deberán cubrir todos los valores conocidos y uno desconocido

## 453. Usage Contrac

El contrato de uso deberá normalizar

-   input tokens
-   output tokens
-   cached tokens
-   reasoning tokens cuando existan
-   total
-   costo estimado
-   moneda
-   proveedor
-   modelo Los campos no proporcionados deberán tener semántica
    explícita: cero, nulo o desconocido

## 454. Streaming Provider Contrac

Todos los adapters de streaming deberán producir eventos internos
comunes

Ejemplo

GenerationStarte TextDelt ToolCallDelt UsageReporte GenerationComplete
GenerationFaile La aplicación no deberá depender del formato de chunks
especí co del proveedor

## 455. Errores de proveedore

El contrato deberá normalizar

-   autenticación
-   rate limit ;

.

;

:

fi ;

;

a

;

;

;

;

;

d

a

d

d

d

:

t

;

:

s

t

fi .

.

.

.

-   timeout
-   indisponibilidad
-   request inválido
-   contenido bloqueado
-   respuesta inválida
-   error desconocido Cada adapter deberá demostrar el mapeo

## 456. Contratos de Embedding Provider

El contrato deberá de nir

-   lista de textos
-   lista de vectores
-   dimensiones
-   modelo
-   uso
-   límites
-   orden
-   errores La cantidad y orden de embeddings deberá corresponder con la
    entrada

## 457. Dimensión del embeddin

La dimensión deberá validarse contra la con guración del índice

Un cambio de modelo con dimensión diferente será un cambio
arquitectónico y de datos, no una sustitución transparente

## 458. Contratos de Object Storag

El puerto deberá de nir

-   put
-   get
-   delete
-   exists
-   metadata
-   signed URL
-   checksum ;

;

;

;

;

;

;

.

;

;

;

;

;

;

;

;

;

;

.

;

fi ;

fi :

.

:

.

fi g

e

s

.

.

-   streaming

-   errores La suite común podrá ejecutarse sobre

-   fake in-memory

-   MinIO

-   proveedor real sandbox

## 459. Contratos de Redi

Los adapters de Redis deberán de nir

-   serialización
-   TTL
-   atomicidad
-   nombres de keys
-   tenant partition
-   locks
-   rate limits
-   idempotencia Los tests deberán ejecutarse contra Redis real en
    integración

## 460. Key Naming Contrac

Las keys deberán seguir una convención versionada

Ejemplo

geem-ai:v1:tenant:{tenant_id}:rate-limit:{actor_id No deberán incluir
contenido sensible sin hashing o normalización

## 461. Contratos MC

Cuando se implemente MCP, deberán probarse

-   handshake
-   versión
-   capabilities
-   tools
-   resources
-   prompts ;

;

;

;

.

;

;

:

;

;

;

;

;

;

;

.

;

;

;

.

P

fi s

:

:

t

:

.

.

.

``` text
}
```

-   schemas
-   errores
-   autorización
-   cancelación
-   timeouts El detalle se ampliará en el capítulo especí co de MCP
    Testing

## 462. Contract Testing de archivo

Los formatos de archivos importados o exportados deberán poseer

-   schema

-   versión

-   encoding

-   delimitador

-   campos

-   tipos

-   reglas de compatibilidad Ejemplos

-   CSV de importación

-   JSON de exportación

-   reportes

-   bundles de conocimiento

## 463. Contratos de con guració

La con guración compartida deberá validarse mediante schema

Esto incluye

-   modelos disponibles
-   políticas de routing
-   tool registry
-   prompt registry
-   límites
-   feature ags Una con guración inválida deberá rechazarse antes de
    iniciar la aplicación

## 464. Semantic Contract Test

;

;

fi ;

;

;

fl ;

;

fi ;

.

;

:

;

;

;

.

;

:

;

;

;

;

;

.

.

fi fi s

n

s

.

.

:

.

No todos los contratos pueden validarse solo estructuralmente

Ejemplos

-   created_at debe representar creación
-   score mayor signi ca más relevancia
-   has_more=false indica ausencia de página siguiente
-   aprobación no signi ca ejecución completada
-   respuesta 202 indica proceso pendiente Los tests deberán validar
    también esta semántica

## 465. Contract Testing de errore

Los consumidores deberán poder depender de

-   código
-   status
-   retryable
-   detalles permitidos
-   correlation ID Los mensajes humanizados no deberán ser el único
    contrato

## 466. Contratos y datos sensible

Los schemas y ejemplos no deberán incluir

-   tokens reales
-   secretos
-   datos personales
-   documentos privados
-   nombres productivos innecesarios Los ejemplos deberán ser sintéticos

## 467. Registro de contrato

Los contratos deberán almacenarse de forma organizada

contracts

``` text
├── openapi
│   └── geem-ai.v1.yam
```

;

;

;

;

:

;

/

.

;

/

fi ;

fi ;

l

.

.

;

.

s

;

:

;

:

.

s

s

.

;

.

.

``` text
├── events
│   ├── conversation.created.v1.jso
│   └── tool.execution.requested.v1.jso
├── tools
│   └── search_documents
│       ├── input.v1.schema.jso
│       └── output.v1.schema.jso
├── queues
├── mcp
└── files
```

## 468. Ownershi

Cada contrato deberá tener un owner responsable de

-   cambios
-   compatibilidad
-   documentación
-   consumidores
-   deprecación
-   incidentes En equipos pequeños, el ownership podrá asignarse por
    dominio

## 469. Contract Revie

Todo cambio de contrato deberá revisar

-   productores
-   consumidores
-   compatibilidad
-   rollout
-   datos existentes
-   observabilidad
-   rollback
-   documentación
-   fecha de retiro

## 470. Quality Gate de contrato

CI deberá fallar cuando

-   OpenAPI sea inválido ;

;

;

.

/

;

;

/

/

;

;

.

;

;

;

/

/

;

;

;

;

p

:

w

/

:

n

s

n

:

n

n

.

-   exista breaking change no aprobado
-   un schema no valide
-   xtures históricas fallen
-   SDK generado esté desactualizado
-   tool implementation no cumpla schema
-   event producer rompa compatibilidad
-   provider adapter rompa el Protocol

## 471. Anti-patterns de Contract Testin

Documentation-Only Contrac

El contrato existe, pero no se veri ca

Duplicate Schema

Backend, frontend y documentación mantienen copias independientes

Silent Breaking Chang

Se modi ca una respuesta sin versionar

Untyped Event

Los mensajes son diccionarios arbitrarios

Provider Leakag

La aplicación depende del JSON del proveedor

Version in Documentation Onl

La versión no aparece en el mensaje o schema

Examples as Test

Se asume que un ejemplo demuestra todos los casos

Ignore Unknown Fields Everywher

Oculta errores de clientes o modelos fi fi s

;

e

s

s

;

e

fi ;

.

;

.

.

t

;

y

.

;

.

e

.

.

.

g

.

## 472. Checklist de Contract Testin

Cada contrato deberá responder

-   ¿Cuál es su fuente de verdad
-   ¿Está versionado
-   ¿Quién lo produce
-   ¿Quién lo consume
-   ¿Qué cambios son compatibles
-   ¿Cómo se detectan breaking changes
-   ¿Tiene xtures
-   ¿Tiene ejemplos
-   ¿Se valida en CI
-   ¿Cómo se depreca
-   ¿Cómo se migra
-   ¿Contiene datos sensibles
-   ¿Tiene owner
-   ¿Incluye semántica además de estructura

## 473. De nition of Done del capítul

Contract Testing se considerará implementado cuando

-   OpenAPI sea válido y versionado
-   CI detecte cambios incompatibles
-   requests y responses compartan schemas estables
-   tools tengan contratos de entrada y salida
-   eventos posean envelope y versión
-   mensajes de cola estén tipados
-   existan xtures históricas
-   provider adapters superen una suite común
-   frontend y SDKs validen compatibilidad
-   contratos MCP estén preparados
-   exista ownership
-   ningún cambio incompatible pueda integrarse silenciosamente fi fi fi
    ?

?

?

?

?

;

?

?

?

?

;

?

?

;

?

:

;

;

;

;

?

;

?

;

;

;

g

:

o

.

## Capítulo 11. Pruebas de Integració

## 474. Introducció

Las pruebas de integración tienen como objetivo veri car que múltiples
componentes de un sistema funcionan correctamente cuando interactúan
entre sí. Mientras que las pruebas unitarias validan el comportamiento
aislado de una clase, función o módulo, las pruebas de integración
comprueban que las dependencias reales colaboran correctamente para
ofrecer el comportamiento esperado

En una plataforma moderna como GEEM AI Assistant, una sola solicitud
puede involucrar la comunicación entre la API, la autenticación,
PostgreSQL, Redis, el almacenamiento de documentos, el proveedor del
modelo de lenguaje, los servicios de embeddings, los workers en segundo
plano y los mecanismos de observabilidad. Cada uno de estos componentes
puede funcionar correctamente de manera individual y, aun así, presentar
errores cuando interactúan entre sí

Las pruebas de integración buscan precisamente detectar este tipo de
problemas antes de que lleguen a producción

A diferencia de las pruebas End-to-End, las pruebas de integración
limitan deliberadamente su alcance a un conjunto especí co de
componentes relacionados. Esto permite detectar errores de con guración,
comunicación o persistencia con una ejecución mucho más rápida y estable
que una prueba completa del sistema

Dentro de este proyecto, toda funcionalidad que interactúe con
infraestructura, servicios externos o componentes persistentes deberá
contar con pruebas de integración antes de considerarse terminada

## 475. Objetivos de las pruebas de integració

Las pruebas de integración persiguen objetivos distintos a los de las
pruebas unitarias. No pretenden demostrar que una función produce el
resultado correcto, sino que los distintos componentes del sistema
pueden colaborar de manera con able bajo condiciones similares a las de
un entorno real

Entre sus principales objetivos se encuentran

-   Validar la comunicación entre servicios.
-   Veri car la correcta persistencia de la información.
-   Detectar errores de con guración.
-   Comprobar la integración con servicios externos.
-   Validar la serialización y deserialización de datos. fi fi .

.

.

.

fi .

n

fi .

:

fi fi n

n

-   Veri car el manejo de transacciones.
-   Comprobar el comportamiento ante errores de infraestructura.
-   Detectar incompatibilidades entre versiones de librerías o
    componentes. En plataformas distribuidas, la mayoría de los errores
    críticos no provienen de algoritmos incorrectos, sino de problemas
    de integración entre componentes. Por esta razón, las pruebas de
    integración representan una de las inversiones con mayor retorno
    dentro de una estrategia de aseguramiento de calidad

## 476. Alcance de las pruebas de integració

Una prueba de integración debe involucrar únicamente los componentes
necesarios para validar una interacción especí ca

Por ejemplo, si el objetivo es comprobar que una conversación se
almacena correctamente, la prueba puede involucrar

-   API REST.
-   Capa de aplicación.
-   Repositorio.
-   PostgreSQL.
-   Sistema de migraciones. Sin embargo, no existe necesidad de incluir
    el proveedor de inteligencia arti cial, el sistema de embeddings o
    los workers en segundo plano, ya que no participan en ese ujo

Mientras menor sea el alcance de una prueba de integración, más fácil
será identi car el origen de un fallo y más rápida será su ejecución

El objetivo consiste en validar una colaboración especí ca entre
componentes, no ejecutar el sistema completo

## 477. Diferencias entre pruebas unitarias, de integración y

End-to-En Es frecuente confundir estos tres niveles de pruebas. Sin
embargo, cada uno responde a objetivos completamente distintos

Las pruebas unitarias veri can el comportamiento interno de un
componente de manera aislada. Todas sus dependencias son simuladas
mediante mocks, stubs o fakes, por lo que su ejecución suele ser
extremadamente rápida

Las pruebas de integración utilizan componentes reales siempre que sea
posible. En lugar de simular PostgreSQL, Redis o MinIO, trabajan contra
instancias reales creadas especí camente fi

d

.

fi :

.

.

fi .

.

.

fi

n

fl fi .

fi fi

para la ejecución de la prueba. Esto permite validar con guraciones,
conexiones, transacciones y contratos entre componentes

Las pruebas End-to-End representan el comportamiento completo del
sistema desde la perspectiva del usuario. Inician en la interfaz o en la
API pública y recorren toda la arquitectura hasta obtener un resultado
nal. Aunque proporcionan un alto nivel de con anza, también son las más
lentas, costosas y difíciles de mantener

Una estrategia de calidad madura utiliza los tres niveles de pruebas de
manera complementaria, evitando depender exclusivamente de cualquiera de
ellos

## 478. Principios de las pruebas de integració

Toda estrategia de pruebas de integración debe regirse por un conjunto
de principios que permitan mantener la con abilidad de los resultados y
la facilidad de mantenimiento a largo plazo

Probar componentes reale

Siempre que sea técnicamente viable, las pruebas de integración deberán
ejecutarse contra componentes reales y no sobre simulaciones

Por ejemplo

-   PostgreSQL real.
-   Redis real.
-   MinIO real.
-   RabbitMQ real.
-   Servicios HTTP simulados únicamente cuando el proveedor externo no
    pueda ejecutarse localmente. El uso de infraestructura real reduce
    signi cativamente la posibilidad de obtener falsos positivos
    provocados por diferencias entre el entorno de pruebas y el entorno
    de producción

Mantener el aislamient

Cada prueba debe ejecutarse de forma completamente independiente

Una prueba nunca deberá depender de datos creados por otra

Para lograrlo se recomienda

-   crear datos propios;
-   limpiar los recursos utilizados;
-   utilizar transacciones cuando sea posible; .

:

fi fi :

.

o

s

fi .

.

fi .

.

.

fi .

n

-   reiniciar el estado entre ejecuciones. Una prueba cuyo resultado
    depende del orden de ejecución deja de ser con able

Determinism

Una prueba debe producir exactamente el mismo resultado cada vez que se
ejecuta bajo las mismas condiciones

No deberán existir dependencias con

-   fecha y hora actual;
-   zona horaria;
-   conexiones de red impredecibles;
-   datos previamente existentes;
-   identi cadores aleatorios no controlados. Cuando sea necesario
    utilizar valores variables deberán jarse mediante mecanismos de
    control, como relojes simulados, semillas aleatorias o datos de
    prueba de nidos previamente

Velocidad razonabl

Aunque las pruebas de integración son más lentas que las unitarias,
deben seguir siendo su cientemente rápidas para ejecutarse de manera
frecuente durante el desarrollo

Como referencia

-   Unit Test: milisegundos.
-   Integration Test: segundos.
-   End-to-End: minutos. Una suite de integración excesivamente lenta
    reduce su utilidad práctica y desalienta su ejecución continua

## 479. Qué debe probar una prueba de

integració Una prueba de integración debe centrarse en validar la
interacción entre componentes, no la lógica interna de cada uno

Ejemplos de aspectos que sí deben validarse

-   persistencia correcta de la información; fi fi

o

:

.

.

n

e

.

:

:

fi fi fi .

.

.

-   ejecución de transacciones;
-   propagación de errores;
-   serialización de objetos;
-   autenticación;
-   autorización;
-   comunicación HTTP;
-   manejo de conexiones;
-   publicación de eventos;
-   consumo de mensajes;
-   almacenamiento de archivos;
-   integración con proveedores externos. Por el contrario, no
    corresponde a este nivel validar algoritmos complejos, reglas de
    negocio aisladas o cálculos internos que ya fueron cubiertos
    mediante pruebas unitarias

## 480. Qué NO debe probar una prueba de

integració Uno de los errores más comunes consiste en convertir las
pruebas de integración en pruebas End- to-End

Una prueba de integración no debe intentar validar simultáneamente

-   interfaz de usuario;
-   API;
-   autenticación;
-   base de datos;
-   almacenamiento;
-   servicios externos;
-   cola de mensajes;
-   generación de embeddings;
-   proveedor LLM. Cuando una prueba involucra demasiados componentes
    resulta extremadamente difícil determinar el origen de un fallo

Cada prueba debe validar únicamente la colaboración necesaria para
demostrar un comportamiento especí co

## 481. Arquitectura del entorno de integració

.

n

fi

.

.

:

.

n

El entorno utilizado para las pruebas de integración debe reproducir la
arquitectura de producción en la medida de lo posible, manteniendo al
mismo tiempo tiempos de ejecución aceptables

Para el proyecto GEEM AI Assistant, el entorno de integración estará
compuesto por los siguientes servicios

-   PostgreSQL.
-   Redis.
-   MinIO.
-   RabbitMQ.
-   API principal.
-   Worker.
-   Scheduler.
-   Servicio de Embeddings (simulado cuando corresponda).
-   Servicio de autenticación. Todos estos componentes deberán
    ejecutarse dentro de contenedores Docker independientes para
    garantizar aislamiento, reproducibilidad y facilidad de con guración

El uso de servicios instalados manualmente en el equipo del
desarrollador no será considerado un entorno válido para la ejecución de
pruebas de integración

## 482. Infraestructura efímer

Uno de los principios más importantes de las pruebas modernas consiste
en utilizar infraestructura efímera

Cada ejecución deberá crear un entorno limpio desde cero y destruirlo
una vez nalizadas las pruebas

Este enfoque ofrece múltiples bene cios

-   elimina dependencias entre ejecuciones;
-   evita contaminación de datos;
-   permite ejecutar pruebas en paralelo;
-   facilita la integración continua;
-   garantiza resultados reproducibles. La infraestructura efímera puede
    implementarse mediante herramientas como Docker Compose o
    Testcontainers, dependiendo del alcance y complejidad de la prueba

## 483. Docker Compose para integración loca

.

.

:

.

fi

:

.

fi a

.

.

fi l

Durante el desarrollo diario resulta conveniente disponer de un entorno
de integración permanente que permita ejecutar pruebas de manera rápida

Para ello se utilizará un archivo docker-compose.integration.yml que
levante únicamente los servicios necesarios para las pruebas

Este entorno deberá ser idéntico para todos los desarrolladores del
equipo

No se permitirá modi car manualmente con guraciones locales que alteren
el comportamiento esperado de las pruebas

Toda con guración deberá encontrarse versionada dentro del repositorio

## 484. Testcontainer

Cuando una prueba requiera un aislamiento completo, deberá utilizarse
Testcontainers

Esta tecnología permite crear contenedores Docker temporales desde el
propio código de prueba, iniciando únicamente los servicios requeridos
para cada escenario

Entre sus principales ventajas se encuentran

-   aislamiento total;
-   destrucción automática de recursos;
-   ejecución paralela;
-   independencia del entorno del desarrollador;
-   con guración reproducible. El uso de Testcontainers será preferido
    para pruebas automatizadas dentro del pipeline de integración
    continua

## 485. Con guración del entorn

Toda prueba de integración deberá ejecutarse utilizando archivos de con
guración independientes del entorno de desarrollo y de producción

La con guración incluirá, como mínimo

-   cadenas de conexión;
-   credenciales temporales;
-   rutas de almacenamiento;
-   colas de mensajes;
-   endpoints simulados; fi fi fi

fi .

fi

.

s

:

:

fi

.

.

.

o

.

fi .

.

.

-   claves de prueba;
-   límites de recursos. Bajo ninguna circunstancia las pruebas deberán
    utilizar credenciales o servicios pertenecientes a un entorno de
    producción

Las variables de entorno deberán cargarse automáticamente mediante per
les especí cos para pruebas, evitando cualquier intervención manual por
parte del desarrollador

## 486. Integración con PostgreSQ

PostgreSQL constituye el principal mecanismo de persistencia del GEEM AI
Assistant. En consecuencia, representa uno de los componentes más
críticos dentro de la estrategia de pruebas de integración

Mientras que las pruebas unitarias sustituyen el acceso a datos mediante
mocks o repositorios simulados, las pruebas de integración deberán
ejecutarse contra una instancia real de PostgreSQL con el n de validar
el comportamiento completo de la capa de persistencia

Entre los aspectos que deberán veri carse se encuentran

-   creación y actualización de registros;
-   integridad referencial;
-   restricciones de unicidad;
-   ejecución de transacciones;
-   concurrencia;
-   índices;
-   migraciones;
-   serialización de datos JSON;
-   consultas complejas;
-   manejo de errores. Una prueba de integración no debe asumir que una
    consulta SQL funciona correctamente; debe demostrarlo mediante la
    ejecución sobre un motor real

## 487. Base de datos exclusiva para prueba

Las pruebas nunca deberán ejecutarse sobre la base de datos utilizada
por el entorno de desarrollo

Cada ejecución utilizará una base de datos independiente creada especí
camente para pruebas

Esto evita

-   contaminación de información; fi

:

.

.

.

fi

.

:

L

fi fi .

.

fi s

.

-   pérdida accidental de datos;
-   dependencia del estado del entorno local;
-   interferencia con otros desarrolladores. La creación automática de
    esta base de datos deberá formar parte del proceso de inicialización
    de la suite de pruebas

Al nalizar la ejecución, toda la información podrá eliminarse sin
afectar otros entornos

## 488. Migraciones como fuente de verda

La estructura de la base de datos utilizada durante las pruebas deberá
generarse exclusivamente mediante el sistema o cial de migraciones

No está permitido

-   importar respaldos SQL manuales;
-   ejecutar scripts independientes;
-   modi car tablas directamente desde herramientas administrativas;
-   mantener esquemas paralelos para pruebas. Las migraciones
    representan la única fuente autorizada para construir la estructura
    del esquema

De esta manera se garantiza que cualquier entorno pueda reconstruirse
desde cero utilizando exactamente el mismo procedimiento

## 489. Validación de migracione

Cada nueva migración deberá validarse mediante pruebas de integración

Como mínimo deberán comprobarse los siguientes escenarios

-   aplicación sobre una base vacía;
-   aplicación sobre la versión anterior;
-   reversión (rollback);
-   recreación completa desde cero;
-   compatibilidad con datos existentes cuando corresponda. Una
    migración que funciona únicamente en el entorno del desarrollador no
    puede considerarse válida

El objetivo consiste en asegurar que cualquier instancia del sistema
pueda evolucionar entre versiones sin pérdida de información ni
inconsistencias fi fi .

:

.

fi

.

.

.

:

s

.

d

.

.

## 490. Datos de prueb

Uno de los errores más frecuentes consiste en reutilizar datos creados
manualmente durante el desarrollo

Las pruebas deberán utilizar datos diseñados especí camente para el
escenario que pretenden validar

Estos datos deberán cumplir las siguientes características

-   mínimos;
-   comprensibles;
-   reproducibles;
-   independientes;
-   fáciles de mantener. Por ejemplo, si una prueba pretende validar el
    registro de una conversación, no resulta necesario poblar cientos de
    usuarios, documentos y con guraciones

Únicamente deberán crearse los registros estrictamente necesarios para
reproducir el comportamiento esperado

## 491. Fixture

Los xtures representan conjuntos de datos reutilizables utilizados para
preparar el estado inicial de una prueba

Su objetivo consiste en evitar duplicación de código y facilitar la
construcción de escenarios repetitivos

Un xture correctamente diseñado debe ser

-   pequeño;
-   modular;
-   reutilizable;
-   independiente del orden de ejecución;
-   fácilmente extensible. Los xtures no deberán contener información
    innecesaria ni convertirse en una representación completa del
    sistema

Cada xture debe resolver una necesidad especí ca fi fi fi fi .

.

.

.

.

s

.

a

:

fi fi .

fi :

.

## 492. Seeds para integració

Es importante distinguir entre un xture y un seed

Los xtures preparan un escenario concreto para una prueba determinada

Los seeds, por el contrario, generan información base requerida por
múltiples escenarios

Ejemplos de información que puede mantenerse mediante seeds

-   países;
-   idiomas;
-   tipos de documentos;
-   catálogos;
-   con guraciones iniciales;
-   permisos predeterminados. Los seeds deberán ser determinísticos y
    producir siempre exactamente el mismo resultado

## 493. Aislamiento mediante transaccione

Siempre que sea posible, cada prueba deberá ejecutarse dentro de una
transacción independiente

Al nalizar la prueba, la transacción podrá revertirse automáticamente,
restaurando el estado original de la base de datos

Este enfoque ofrece múltiples ventajas

-   limpieza inmediata;
-   velocidad de ejecución;
-   independencia entre pruebas;
-   simplicidad de mantenimiento. Cuando una prueba requiera validar el
    comportamiento de varias conexiones simultáneas, podrá ser necesario
    utilizar mecanismos alternativos de limpieza

## 494. Limpieza del entorn

Existen diferentes estrategias para restaurar el estado de la base de
datos entre pruebas

Las más utilizadas son

-   rollback de transacciones; fi fi fi

:

.

fi :

.

o

n

.

:

.

s

.

.

.

.

-   eliminación selectiva de registros;
-   recreación completa del esquema;
-   restauración desde una imagen base. La estrategia elegida dependerá
    del nivel de aislamiento requerido y del costo de inicialización

Para el GEEM AI Assistant se priorizará el uso de transacciones cuando
resulte técnicamente posible, recurriendo a la recreación completa
únicamente en escenarios que involucren migraciones o cambios
estructurales

## 495. Validación de restriccione

Las restricciones de nidas en la base de datos forman parte de la lógica
de integridad del sistema y deberán validarse mediante pruebas especí
cas

Entre ellas destacan

-   PRIMARY KEY;
-   FOREIGN KEY;
-   UNIQUE;
-   CHECK;
-   NOT NULL;
-   restricciones de dominio. No basta con validar estas reglas desde la
    aplicación

La base de datos constituye la última línea de defensa frente a
información inconsistente y debe proteger la integridad incluso cuando
otros componentes fallen

## 496. Validación de índice

Las pruebas de integración también deberán comprobar que los índices
necesarios existen y producen el comportamiento esperado

Aunque el rendimiento detallado pertenece a las pruebas de desempeño,
resulta conveniente veri car aspectos como

-   utilización de índices en consultas críticas;
-   existencia de índices de nidos por las migraciones;
-   ausencia de duplicados innecesarios;
-   compatibilidad con las consultas utilizadas por la aplicación. Una
    consulta funcional pero incapaz de utilizar un índice adecuado puede
    convertirse en un cuello de botella conforme crece el volumen de
    información fi

:

fi :

fi

.

.

fi .

.

s

.

.

s

.

## 497. Estrategia de pruebas para Redi

Las pruebas de integración relacionadas con Redis deberán veri car el
correcto funcionamiento de todos los mecanismos que dependan de
almacenamiento en memoria, sincronización entre procesos o
administración temporal de información

Como mínimo deberán contemplarse pruebas para los siguientes escenarios

-   almacenamiento de información temporal;
-   recuperación de datos desde caché;
-   expiración automática mediante TTL;
-   invalidación de caché;
-   bloqueo distribuido;
-   publicación y suscripción de eventos;
-   manejo de pérdida de conexión;
-   recuperación posterior a una desconexión. Las pruebas deberán
    ejecutarse utilizando una instancia real de Redis

No se permitirá sustituir Redis mediante implementaciones simuladas
cuando el objetivo de la prueba sea validar el comportamiento de
integración

## 498. Validación del mecanismo de cach

Toda funcionalidad que implemente mecanismos de caché deberá contar con
pruebas que permitan veri car tanto el comportamiento esperado como los
escenarios de invalidación

Como mínimo deberán validarse los siguientes casos

-   primera consulta sin información almacenada;
-   recuperación desde caché;
-   actualización de datos;
-   invalidación posterior a una modi cación;
-   expiración automática;
-   reconstrucción del contenido almacenado. Las pruebas deberán
    demostrar que la información entregada por el sistema permanece
    consistente independientemente del origen de los datos

## 499. Validación de TT

fi

fi

L

.

.

:

.

fi .

:

s

é

.

Todo dato almacenado con tiempo de vida limitado deberá contar con
pruebas especí cas que veri quen su expiración

Las pruebas deberán comprobar

-   asignación correcta del TTL;
-   expiración dentro del intervalo esperado;
-   eliminación automática del registro;
-   comportamiento posterior a la expiración;
-   recreación del elemento cuando corresponda. No deberán utilizarse
    tiempos de espera excesivos durante las pruebas

Siempre que la herramienta utilizada lo permita, deberá emplearse
manipulación controlada del tiempo o tiempos de expiración reducidos
para disminuir la duración de la ejecución

## 500. Pruebas de bloqueo distribuid

Cuando un componente implemente mecanismos de exclusión mutua utilizando
Redis, deberán desarrollarse pruebas que validen el comportamiento bajo
acceso concurrente

Como mínimo deberán comprobarse los siguientes escenarios

-   adquisición exitosa del bloqueo;
-   intento simultáneo por múltiples procesos;
-   liberación del bloqueo;
-   expiración automática del bloqueo;
-   recuperación después de fallos inesperados;
-   prevención de condiciones de carrera. Las pruebas deberán demostrar
    que únicamente una instancia obtiene acceso al recurso protegido
    durante cada intervalo de ejecución

## 501. Pruebas de concurrenci

Las pruebas de integración deberán contemplar escenarios donde múltiples
solicitudes intenten acceder simultáneamente al mismo recurso

Entre los escenarios mínimos se incluyen

-   creación simultánea de registros;
-   modi cación concurrente;
-   eliminación concurrente;
-   acceso simultáneo a información compartida; fi fi

.

:

.

:

.

a

:

.

o

.

.

fi

-   adquisición concurrente de bloqueos. La ejecución deberá validar que
    el sistema mantiene la consistencia de los datos aun bajo
    condiciones de alta concurrencia

## 502. Validación de Pub/Su

Toda funcionalidad basada en mecanismos de publicación y suscripción
deberá demostrar el correcto intercambio de mensajes entre productores y
consumidores

Como mínimo deberán veri carse los siguientes aspectos

-   publicación del mensaje;
-   recepción por los suscriptores;
-   contenido íntegro del mensaje;
-   orden esperado de recepción cuando aplique;
-   comportamiento ante desconexiones;
-   recuperación de la comunicación. Las pruebas deberán ejecutarse
    utilizando canales independientes para evitar interferencias entre
    distintos escenarios

## 503. Manejo de errores de Redi

Las pruebas de integración deberán validar el comportamiento del sistema
cuando Redis no se encuentre disponible o responda de forma incorrecta

Como mínimo deberán contemplarse escenarios como

-   servidor detenido;
-   pérdida de conectividad;
-   tiempo de espera agotado;
-   autenticación incorrecta;
-   indisponibilidad temporal;
-   recuperación del servicio. Las pruebas deberán demostrar que el
    sistema responde de manera controlada y mantiene la estabilidad de
    la aplicación

## 504. Estrategia de pruebas para MinI

.

.

fi

.

.

:

b

:

s

.

O

Las pruebas relacionadas con almacenamiento de objetos deberán
ejecutarse utilizando una instancia compatible con la utilizada en
producción

Para el entorno de integración se empleará MinIO como implementación de
referencia

Como mínimo deberán validarse

-   carga de archivos;
-   descarga;
-   eliminación;
-   actualización de metadatos;
-   generación de URL temporales;
-   validación de permisos;
-   manejo de errores durante la transferencia. No se permitirá utilizar
    almacenamiento local del sistema operativo para sustituir estas
    pruebas cuando el objetivo sea validar la integración con el
    servicio de almacenamiento

## 505. Validación de operaciones sobre objeto

Las pruebas deberán comprobar que cada operación realizada sobre el
almacenamiento genera el resultado esperado

Como mínimo deberán veri carse

-   integridad del archivo almacenado;
-   conservación del tipo MIME;
-   tamaño del archivo;
-   metadatos asociados;
-   identi cadores generados;
-   comportamiento frente a nombres duplicados;
-   eliminación permanente cuando corresponda. Toda operación deberá
    validar tanto el resultado devuelto por la aplicación como el estado
    real del objeto dentro del almacenamiento

## 506. Limpieza del almacenamient

Al nalizar cada prueba de integración, todos los objetos creados deberán
eliminarse automáticamente

No se permitirá reutilizar archivos generados por pruebas anteriores fi
fi

.

.

fi

:

:

.

.

.

o

.

.

s

La limpieza deberá formar parte del proceso automático de la suite de
pruebas y ejecutarse independientemente del resultado obtenido durante
la prueba

El objetivo es garantizar que cada ejecución inicie sobre un entorno
limpio, evitando dependencias entre escenarios y reduciendo la
posibilidad de resultados inconsistentes

## Capítulo 12. Pruebas de Workers y Cola

## 507. Objetiv

Las pruebas de integración relacionadas con procesos asíncronos deberán
veri car que los Workers ejecutan correctamente las tareas asignadas,
mantienen la consistencia de la información y gestionan adecuadamente
los errores durante el procesamiento

Toda funcionalidad ejecutada mediante colas deberá contar con pruebas
especí cas independientes de las pruebas realizadas sobre la API

No se considerará su ciente validar únicamente la creación del mensaje
dentro de la cola

Las pruebas deberán demostrar que el proceso completo naliza
correctamente

## 508. Alcanc

Este capítulo aplica a todos los componentes responsables del
procesamiento asíncrono del sistema, incluyendo

-   Workers.
-   Schedulers.
-   Procesadores de documentos.
-   Generación de embeddings.
-   Indexación.
-   Noti caciones.
-   Procesos programados.
-   Integraciones externas.
-   Tareas en segundo plano. Todo componente cuya ejecución dependa de
    una cola deberá cumplir los criterios de nidos en este capítulo

## 509. Entorno de prueba

fi

.

e

o

:

fi

s

.

fi .

.

fi fi .

fi s

.

.

Las pruebas deberán ejecutarse utilizando la misma tecnología de
mensajería de nida para el proyecto

No deberán emplearse implementaciones simuladas cuando el objetivo sea
validar la integración completa entre el productor, la cola y el
consumidor

El entorno deberá incluir como mínimo

-   Broker de mensajes.
-   Worker.
-   Base de datos.
-   Sistema de almacenamiento cuando corresponda.
-   Servicios auxiliares involucrados en el procesamiento. La con
    guración utilizada durante las pruebas deberá ser reproducible
    mediante infraestructura automatizada

## 510. Publicación de mensaje

Toda funcionalidad responsable de publicar mensajes deberá contar con
pruebas que veri quen

-   creación del mensaje;
-   serialización correcta;
-   envío hacia la cola correspondiente;
-   asignación de prioridad cuando aplique;
-   incorporación de metadatos;
-   generación del identi cador de correlación. Las pruebas deberán
    comprobar tanto la respuesta del productor como el contenido
    efectivo almacenado dentro del broker

## 511. Consumo de mensaje

Las pruebas deberán veri car que los Workers consumen correctamente los
mensajes publicados

Como mínimo deberán validarse los siguientes escenarios

-   recepción del mensaje;
-   deserialización;
-   validación del contenido;
-   ejecución del proceso correspondiente;
-   con rmación del procesamiento. Toda prueba deberá comprobar que el
    mensaje es procesado exactamente por el Worker esperado fi fi

.

.

.

fi

fi

.

:

s

s

.

:

fi fi :

.

## 512. Con rmación de procesamiento (ACK

Todo Worker deberá con rmar explícitamente el procesamiento exitoso de
un mensaje

Las pruebas deberán demostrar

-   envío correcto del ACK;
-   eliminación del mensaje de la cola;
-   actualización del estado correspondiente;
-   inexistencia de reprocesamientos posteriores. No se permitirá
    considerar una tarea completada únicamente porque el proceso terminó
    sin errores

La con rmación del broker forma parte del criterio de éxito

## 513. Rechazo de mensajes (NACK

Las pruebas deberán validar el comportamiento del sistema cuando el
procesamiento no pueda completarse

Como mínimo deberán contemplarse

-   errores recuperables;
-   errores permanentes;
-   mensajes inválidos;
-   fallos de infraestructura;
-   excepciones inesperadas. Cada escenario deberá comprobar que el
    mensaje recibe el tratamiento de nido por la estrategia de
    reintentos del proyecto

## 514. Idempotenci

Toda tarea ejecutada mediante Workers deberá demostrar comportamiento
idempotente cuando el negocio así lo requiera

Las pruebas deberán veri car que el procesamiento repetido de un mismo
mensaje

-   no genera registros duplicados;
-   no modi ca información previamente consolidada;
-   no ejecuta acciones irreversibles múltiples veces;
-   mantiene el mismo estado nal. fi .

fi .

fi

.

fi fi

.

fi a

:

:

)

.

)

fi :

.

Este escenario resulta especialmente importante cuando existen
reintentos automáticos

## 515. Reintentos automático

Las pruebas deberán validar el mecanismo de reintentos de nido para cada
tipo de tarea

Como mínimo deberán comprobarse

-   número máximo de intentos;
-   intervalo entre reintentos;
-   incremento progresivo cuando exista backoff;
-   recuperación exitosa antes del límite;
-   agotamiento de intentos. La con guración utilizada deberá
    corresponder con la de nida para producción

## 516. Dead Letter Queu

Cuando una tarea no pueda completarse después del número máximo de
reintentos, deberá enviarse a la cola de errores correspondiente

Las pruebas deberán veri car

-   envío automático a la Dead Letter Queue;
-   conservación del mensaje original;
-   incorporación de información diagnóstica;
-   trazabilidad del error;
-   imposibilidad de perder mensajes durante el proceso. La existencia
    de una DLQ no sustituye la necesidad de registrar adecuadamente la
    causa del fallo

## 517. Orden de procesamient

Cuando el orden de ejecución forme parte de los requisitos funcionales,
las pruebas deberán demostrar que dicho orden se mantiene incluso bajo
condiciones de concurrencia

Como mínimo deberán contemplarse escenarios donde múltiples mensajes
ingresan simultáneamente a la cola

Las pruebas deberán veri car que el resultado nal respeta las reglas de
nidas por el negocio .

fi

fi fi

.

:

e

:

s

.

o

fi

fi fi fi .

.

.

.

.

Cuando el orden no constituya un requisito funcional, las pruebas
deberán demostrar que el procesamiento paralelo no afecta la
consistencia de la información

## 518. Concurrencia entre Worker

Las pruebas deberán validar el comportamiento del sistema cuando
múltiples Workers procesan simultáneamente tareas pertenecientes a una
misma cola

Como mínimo deberán veri carse

-   distribución adecuada del trabajo;
-   ausencia de duplicidad;
-   sincronización correcta;
-   consistencia de la información;
-   utilización apropiada de mecanismos de bloqueo cuando correspondan.
    Las pruebas deberán ejecutarse con más de una instancia del Worker
    para reproducir condiciones similares a producción

## 519. Validación de visibilidad de mensaje

Las pruebas deberán veri car que los mensajes permanecen ocultos para
otros consumidores mientras un Worker mantiene el control de su
procesamiento

Como mínimo deberán validarse los siguientes escenarios

-   un único Worker procesa el mensaje;
-   el mensaje permanece invisible para el resto de consumidores;
-   el mensaje vuelve a estar disponible cuando el procesamiento falla;
-   el tiempo de visibilidad se comporta conforme a la con guración
    establecida. Las pruebas deberán demostrar que no existen
    condiciones que permitan el procesamiento simultáneo de un mismo
    mensaje por múltiples Workers

## 520. Recuperación ante interrupcione

Las pruebas deberán validar el comportamiento del sistema cuando un
Worker es detenido inesperadamente durante la ejecución de una tarea

Como mínimo deberán contemplarse los siguientes escenarios

-   terminación forzada del proceso;
-   pérdida de conectividad con el broker; .

fi fi

:

.

s

fi .

.

:

.

:

.

s

s

-   reinicio del servicio;
-   interrupción del servidor;
-   agotamiento de recursos del sistema. Las pruebas deberán demostrar
    que las tareas pendientes permanecen disponibles para su
    procesamiento una vez restablecido el servicio

No deberá producirse pérdida de información como consecuencia de una
interrupción inesperada

## 521. Procesamiento de tareas de larga

duració Toda tarea cuyo tiempo de ejecución exceda el tiempo promedio
del sistema deberá contar con pruebas especí cas

Como mínimo deberán veri carse

-   mantenimiento de la conexión durante el procesamiento;
-   renovación del tiempo de visibilidad cuando aplique;
-   liberación adecuada de recursos;
-   correcta nalización de la tarea. Las pruebas deberán demostrar que
    el procesamiento prolongado no provoca duplicidad de ejecución ni
    expiración prematura del mensaje

## 522. Procesamiento concurrent

Cuando la arquitectura permita el procesamiento paralelo de tareas,
deberán ejecutarse pruebas que reproduzcan cargas concurrentes

Como mínimo deberán veri carse

-   procesamiento simultáneo por múltiples Workers;
-   estabilidad del sistema;
-   consistencia de los datos;
-   utilización adecuada de bloqueos;
-   ausencia de condiciones de carrera. La concurrencia no deberá
    comprometer la integridad de la información persistida fi .

fi n

.

fi fi

:

:

.

.

.

e

.

## 523. Validación de tareas programada

Las tareas ejecutadas mediante Scheduler deberán contar con pruebas
independientes de las pruebas de los Workers

Como mínimo deberán veri carse

-   ejecución conforme al horario de nido;
-   prevención de ejecuciones duplicadas;
-   manejo de retrasos;
-   recuperación después de reinicios;
-   comportamiento cuando una ejecución anterior permanece activa. Las
    pruebas deberán demostrar que la programación de tareas mantiene un
    comportamiento predecible bajo distintas condiciones de operación

## 524. Validación de procesamiento por lote

Las tareas que procesen múltiples elementos en una sola ejecución
deberán validar correctamente el comportamiento del lote completo

Como mínimo deberán contemplarse

-   lote completamente exitoso;
-   error parcial;
-   interrupción del procesamiento;
-   reanudación del proceso;
-   registros omitidos;
-   registros duplicados. Las pruebas deberán garantizar que cada
    elemento del lote recibe exactamente el tratamiento esperado

## 525. Manejo de excepcione

Todo Worker deberá registrar adecuadamente las excepciones producidas
durante el procesamiento

Las pruebas deberán veri car

-   captura de la excepción;
-   clasi cación del error; fi .

.

.

fi fi

:

fi :

.

:

.

s

s

s

-   registro de información diagnóstica;
-   liberación de recursos;
-   comportamiento de nido para reintentos. No se permitirá que una
    excepción provoque la terminación inesperada del proceso sin generar
    evidencia su ciente para su análisis

## 526. Validación de registros de auditorí

Toda tarea crítica ejecutada mediante procesos asíncronos deberá generar
registros de auditoría su cientes para reconstruir posteriormente su
ejecución

Las pruebas deberán comprobar que dichos registros contienen, como
mínimo

-   identi cador del mensaje;
-   identi cador de correlación;
-   fecha y hora de inicio;
-   fecha y hora de nalización;
-   resultado obtenido;
-   errores producidos;
-   duración del procesamiento. La información registrada deberá
    permitir reconstruir completamente el ciclo de vida de una tarea

## 527. Validación de trazabilida

Las pruebas deberán veri car que una solicitud puede rastrearse desde su
origen hasta la nalización del procesamiento asíncrono

Como mínimo deberán comprobarse

-   conservación del Correlation ID;
-   propagación del Trace ID;
-   relación entre productor y consumidor;
-   asociación con registros de auditoría;
-   continuidad del contexto durante toda la ejecución. La pérdida de
    trazabilidad se considerará un defecto crítico para cualquier
    componente distribuido

## 528. Pruebas de recuperació

fi fi .

fi fi .

fi fi

fi

fi

.

:

.

.

n

d

:

a

Toda estrategia de recuperación automática deberá validarse mediante
pruebas especí cas

Como mínimo deberán contemplarse

-   reinicio del Worker;
-   reinicio del broker;
-   recuperación después de pérdida temporal de red;
-   recuperación de tareas pendientes;
-   consistencia del estado nal. Las pruebas deberán demostrar que el
    sistema puede continuar procesando tareas sin intervención manual
    una vez restablecidas las condiciones normales de operación

## 529. Validación de consumo de recurso

Las pruebas deberán veri car que el procesamiento asíncrono mantiene un
consumo estable de recursos durante ejecuciones prolongadas

Como mínimo deberán monitorearse

-   memoria;
-   utilización del procesador;
-   conexiones abiertas;
-   descriptores de archivos;
-   crecimiento de colas internas. No deberán detectarse pérdidas
    progresivas de memoria (memory leaks) ni acumulación inde nida de
    recursos

## 530. Criterios mínimos de aceptació

Todo componente basado en Workers o colas únicamente podrá considerarse
apto para su liberación cuando se cumplan los siguientes criterios

-   procesamiento exitoso de tareas válidas;
-   manejo correcto de errores;
-   funcionamiento de la estrategia de reintentos;
-   validación de la idempotencia cuando corresponda;
-   ausencia de pérdida de mensajes;
-   generación de registros de auditoría;
-   conservación de la trazabilidad;
-   cumplimiento de los tiempos máximos establecidos para el
    procesamiento. El incumplimiento de cualquiera de estos criterios
    impedirá la aprobación de la funcionalidad fi

.

fi

fi

:

:

.

:

n

.

s

fi .

.

## 531. Anti-pattern

Los siguientes escenarios constituyen prácticas no aceptadas para la
implementación y validación de procesos asíncronos

Como parte de las revisiones técnicas, deberá veri carse que ninguno de
estos casos se encuentre presente

No validar el resultado del procesamient

Una prueba que únicamente veri ca que un mensaje fue publicado no
demuestra que la tarea haya sido ejecutada correctamente

Deberá comprobarse el resultado nal del procesamiento y el estado de los
recursos afectados

Compartir colas entre prueba

Las pruebas no deberán utilizar colas compartidas que puedan contener
mensajes provenientes de otras ejecuciones

Cada escenario deberá ejecutarse sobre un entorno limpio y completamente
aislado

Utilizar tiempos de espera jo

El uso de instrucciones como

-   sleep()
-   Thread.sleep()
-   time.sleep() para esperar el procesamiento de una tarea constituye
    una mala práctica

Las pruebas deberán utilizar mecanismos de sincronización o veri cación
del estado que permitan detectar objetivamente la nalización del proceso

Ignorar escenarios de erro

No deberá asumirse que un Worker siempre nalizará correctamente

Las pruebas deberán contemplar errores de negocio, errores de
infraestructura y fallos inesperados

.

.

.

:

fi r

fi fi .

.

fi s

s

s

fi fi o

.

fi .

.

.

.

Omitir pruebas de concurrenci

Todo proceso susceptible de ejecutarse simultáneamente deberá contar con
pruebas que reproduzcan dicho escenario

La ausencia de este tipo de pruebas incrementa signi cativamente el
riesgo de condiciones de carrera

No validar la idempotenci

Cuando una tarea pueda ejecutarse más de una vez, deberá demostrarse que
el resultado permanece consistente independientemente del número de
ejecuciones

No veri car la trazabilida

Toda tarea procesada deberá poder reconstruirse mediante registros de
auditoría y mecanismos de observabilidad

La ausencia de esta información di cultará el diagnóstico de incidentes
en producción

## 532. Errores comunes detectados durante

prueba Durante el desarrollo de sistemas distribuidos es frecuente
encontrar errores recurrentes cuya detección debe formar parte del
proceso de revisión

Entre los más comunes se encuentran

-   mensajes duplicados;
-   mensajes perdidos;
-   reintentos in nitos;
-   con rmaciones (ACK) enviadas antes de nalizar el procesamiento;
-   bloqueos permanentes;
-   consumo excesivo de memoria;
-   excepciones no controladas;
-   tareas ejecutadas múltiples veces;
-   inconsistencias derivadas de condiciones de carrera. Las pruebas de
    integración deberán diseñarse considerando explícitamente estos
    escenarios fi .

fi fi s

.

.

d

a

fi :

a

fi .

fi

.

.

.

## 533. Evidencia de ejecució

Toda ejecución de la suite de pruebas deberá generar evidencia su ciente
para permitir el análisis posterior de los resultados

Como mínimo deberá conservarse la siguiente información

-   fecha y hora de ejecución;
-   versión del sistema;
-   versión de la base de datos;
-   versión de los servicios involucrados;
-   resultados obtenidos;
-   registros de errores;
-   duración de las pruebas;
-   cobertura ejecutada. La evidencia deberá integrarse automáticamente
    al pipeline de Integración Continua cuando corresponda

## 534. Checklist para revisión técnic

Antes de aprobar una funcionalidad basada en procesamiento asíncrono
deberá veri carse el cumplimiento de los siguientes puntos

□ El mensaje se publica correctamente

□ El Worker consume el mensaje esperado

□ El procesamiento concluye satisfactoriamente

□ Se valida el resultado nal

□ Se registran adecuadamente los errores

□ Se valida la idempotencia

□ Se comprueba el comportamiento concurrente

□ Se veri can los reintentos

□ Se valida la Dead Letter Queue fi .

fi

.

.

.

.

.

.

.

.

.

.

.

n

:

fi a

fi

□ Se conserva la trazabilidad

## 535. Checklist para integración continu

La ejecución automática del pipeline deberá veri car, como mínimo

□ Inicialización del broker

□ Inicialización de los Workers

□ Aplicación de migraciones

□ Disponibilidad de los servicios auxiliares

□ Ejecución completa de las pruebas

□ Limpieza automática del entorno

□ Publicación de resultados

□ Generación de reportes

Ningún cambio podrá integrarse a la rama principal cuando alguna de
estas validaciones falle

## 536. Checklist previo a liberació

Antes de liberar una nueva versión deberán veri carse los siguientes
aspectos relacionados con el procesamiento asíncrono

□ No existen mensajes pendientes sin procesar

□ No existen colas bloqueadas

□ No existen tareas en estado inconsistente

□ Todos los Workers responden correctamente

□ La estrategia de recuperación fue validada

□ La observabilidad funciona correctamente .

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

fi fi :

n

a

.

□ Los mecanismos de auditoría permanecen operativos

## 537. Criterios de aceptació

Se considerará que un componente basado en Workers cumple los requisitos
de nidos por este estándar cuando

-   todas las pruebas de integración nalicen satisfactoriamente;
-   no existan errores de concurrencia;
-   la información permanezca consistente;
-   los mecanismos de recuperación funcionen correctamente;
-   la trazabilidad sea completa;
-   la auditoría permita reconstruir cada ejecución;
-   el procesamiento resulte determinístico para escenarios
    equivalentes.

## 538. Criterios de rechaz

No deberá aprobarse una implementación cuando ocurra cualquiera de las
siguientes situaciones

-   pérdida de mensajes;
-   duplicidad no controlada;
-   fallos de recuperación;
-   imposibilidad de rastrear una tarea;
-   ausencia de pruebas para escenarios críticos;
-   dependencia del orden de ejecución de las pruebas;
-   resultados inconsistentes entre ejecuciones. La presencia de
    cualquiera de estos escenarios requerirá la corrección de la
    implementación antes de continuar con el proceso de integración

## 539. Revisión periódic

La estrategia de pruebas para procesos asíncronos deberá revisarse
periódicamente como parte de las actividades de mejora continua

La incorporación de nuevos componentes, cambios en la infraestructura o
modi caciones en la arquitectura podrán requerir la actualización de los
escenarios de nidos en este capítulo

Toda modi cación deberá mantener la compatibilidad con los principios
generales establecidos en el presente documento fi :

.

fi .

a

.

o

.

n

fi

fi fi .

:

## 540. De nition of Don

Una funcionalidad basada en Workers o colas únicamente podrá
considerarse terminada cuando se cumplan todos los siguientes criterios

-   dispone de pruebas de integración automatizadas;
-   valida escenarios exitosos y escenarios de error;
-   veri ca la idempotencia cuando aplica;
-   valida reintentos y recuperación;
-   comprueba la gestión de mensajes inválidos;
-   mantiene la consistencia de los datos;
-   conserva la trazabilidad completa;
-   genera registros de auditoría;
-   puede ejecutarse de forma repetible sobre un entorno limpio;
-   forma parte del pipeline de Integración Continua;
-   todas las pruebas nalizan satisfactoriamente. El cumplimiento de
    estos criterios constituye el requisito mínimo para considerar
    aceptable una implementación basada en procesamiento asíncrono
    dentro del proyecto

## Capítulo 13. Evaluación de Sistemas de

Inteligencia Arti cia \## 541. Objetiv

Las pruebas de evaluación de Inteligencia Arti cial deberán veri car que
las funcionalidades basadas en Modelos de Lenguaje (LLM) generan
respuestas consistentes, útiles, veri cables y alineadas con los
requisitos funcionales del sistema

A diferencia de las pruebas tradicionales, este capítulo reconoce que
múltiples respuestas pueden ser válidas para una misma entrada. Por
ello, la evaluación deberá centrarse en la calidad del resultado y no en
la coincidencia exacta del texto generado

Todas las funcionalidades que incorporen modelos de IA deberán contar
con mecanismos de evaluación de nidos antes de su liberación

## 542. Alcanc

Este capítulo aplica a todos los componentes que utilicen capacidades de
Inteligencia Arti cial, incluyendo, entre otros fi fi fi fi e

o

:

fi

:

.

l

fi e

.

.

fi .

fi fi

-   generación de texto;
-   recuperación aumentada por recuperación (RAG);
-   memoria conversacional;
-   Tool Calling;
-   agentes especializados;
-   clasi cación automática;
-   extracción de información;
-   generación de resúmenes;
-   traducción;
-   análisis documental;
-   generación de código;
-   razonamiento asistido. Toda funcionalidad cuya salida dependa
    parcial o totalmente de un modelo de IA deberá cumplir los criterios
    establecidos en este capítulo

## 543. Principios de evaluació

La evaluación de sistemas de IA deberá fundamentarse en los siguientes
principios

-   objetividad;
-   reproducibilidad;
-   trazabilidad;
-   cobertura de escenarios;
-   evaluación continua;
-   comparación contra resultados esperados;
-   utilización de métricas cuanti cables cuando sea posible. No deberán
    utilizarse criterios exclusivamente subjetivos como mecanismo de
    aprobación de una funcionalidad

## 544. Naturaleza no determinístic

Los Modelos de Lenguaje presentan un comportamiento inherentemente no
determinístico

En consecuencia, las pruebas no deberán validar coincidencias literales
entre respuestas, salvo cuando el caso de uso así lo requiera

La evaluación deberá considerar aspectos como

-   exactitud;
-   relevancia;
-   consistencia;
-   cumplimiento de instrucciones; fi

.

fi

.

.

n

:

a

:

.

-   completitud;
-   utilidad para el usuario. Una respuesta diferente no constituye
    necesariamente un error

## 545. De nición de criterios de aceptació

Antes de implementar cualquier funcionalidad basada en IA deberán de
nirse explícitamente los criterios mediante los cuales será evaluada

Como mínimo deberán establecerse

-   objetivo funcional;
-   comportamiento esperado;
-   escenarios válidos;
-   restricciones;
-   condiciones de rechazo;
-   métricas de calidad;
-   evidencia requerida para la aprobación. No deberá iniciarse la
    implementación de funcionalidades de IA sin criterios de evaluación
    previamente de nidos

## 546. Conjunto de evaluación (Evaluation Dataset

Toda funcionalidad deberá disponer de un conjunto representativo de
casos de prueba que permita evaluar de forma consistente el
comportamiento del modelo

El conjunto de evaluación deberá incluir escenarios

-   normales;
-   límite;
-   ambiguos;
-   incompletos;
-   contradictorios;
-   con información insu ciente;
-   con instrucciones inválidas. El dataset deberá mantenerse versionado
    junto con el proyecto

## 547. Cobertura de escenario

Las pruebas deberán cubrir la mayor diversidad posible de interacciones
esperadas

fi

fi

fi .

:

.

s

:

.

.

n

.

fi )

.

Como mínimo deberán contemplarse

-   consultas frecuentes;
-   consultas poco comunes;
-   solicitudes extensas;
-   preguntas breves;
-   instrucciones múltiples;
-   cambios de contexto;
-   conversaciones prolongadas;
-   recuperación después de errores. La cobertura deberá revisarse
    periódicamente conforme evolucione el sistema

## 548. Versionado del conjunto de evaluació

Todo cambio en los casos de prueba deberá registrarse mediante control
de versiones

Cada modi cación deberá documentar

-   motivo del cambio;
-   fecha;
-   responsable;
-   impacto esperado;
-   versión del modelo evaluado. Los resultados históricos deberán
    conservarse para permitir comparaciones entre versiones del sistema

## 549. Automatización de la evaluació

Siempre que sea técnicamente posible, la evaluación deberá ejecutarse de
forma automatizada como parte del proceso de Integración Continua

Las pruebas automatizadas deberán permitir

-   ejecutar el conjunto completo de escenarios;
-   comparar resultados entre versiones;
-   detectar regresiones;
-   generar reportes;
-   almacenar evidencia. La evaluación manual deberá limitarse a
    escenarios donde la automatización no resulte viable

## 550. Evidencia de evaluació

.

fi

:

:

n

:

.

n

n

.

.

.

Cada ejecución del proceso de evaluación deberá generar evidencia su
ciente para permitir auditoría y análisis posterior

Como mínimo deberá conservarse

-   versión del modelo;
-   versión del prompt;
-   versión del dataset;
-   fecha y hora de ejecución;
-   parámetros utilizados;
-   respuesta generada;
-   resultado de la evaluación;
-   métricas obtenidas. La evidencia deberá almacenarse de forma que
    permita reproducir la evaluación en el futuro

## 551. Evaluación de Prompt

Toda funcionalidad basada en Modelos de Lenguaje deberá contar con
pruebas especí cas para validar el comportamiento del prompt utilizado

Las pruebas deberán demostrar que las instrucciones proporcionadas al
modelo producen respuestas alineadas con los objetivos funcionales del
sistema

La evaluación deberá realizarse utilizando el mismo prompt que será
desplegado en producción

## 552. Validación del cumplimiento de

instruccione Las pruebas deberán veri car que el modelo cumple las
instrucciones de nidas en el prompt del sistema

Como mínimo deberán evaluarse los siguientes aspectos

-   respeto del rol asignado;
-   cumplimiento de restricciones;
-   formato de respuesta requerido;
-   idioma esperado;
-   longitud cuando aplique;
-   comportamiento ante solicitudes fuera del alcance. La aprobación de
    una funcionalidad no deberá basarse únicamente en ejemplos
    individuales .

fi s

.

:

.

:

s

.

fi fi fi .

.

.

## 553. Resistencia a instrucciones con ictiva

Las pruebas deberán veri car el comportamiento del modelo cuando el
usuario proporcione instrucciones que contradigan las reglas
establecidas por el sistema

Como mínimo deberán contemplarse escenarios donde el usuario intente

-   modi car el rol del asistente;
-   ignorar instrucciones previas;
-   solicitar información restringida;
-   alterar el formato requerido;
-   inducir comportamientos no permitidos. Las pruebas deberán demostrar
    que el modelo mantiene las restricciones de nidas por el sistema

## 554. Consistencia entre ejecucione

Cuando un mismo escenario se ejecute múltiples veces bajo condiciones
equivalentes, las respuestas podrán variar en su redacción, pero deberán
conservar la misma intención funcional

Las pruebas deberán veri car que

-   la información esencial permanece consistente;
-   las restricciones continúan respetándose;
-   no aparecen respuestas contradictorias;
-   la calidad general permanece estable. La variación natural del
    lenguaje no deberá considerarse un defecto cuando el objetivo
    funcional continúe cumpliéndose

## 555. Evaluación de RA

Toda funcionalidad que utilice Recuperación Aumentada por Generación
(RAG) deberá validar la calidad de la recuperación antes de evaluar la
respuesta generada

Las pruebas deberán diferenciar claramente entre

-   errores de recuperación;
-   errores de generación;
-   errores de integración. Esta separación permitirá identi car con
    precisión el origen de cualquier defecto fi

.

fi fi

fi

:

G

:

.

.

:

s

fi fl .

s

.

.

## 556. Relevancia de los documentos

recuperado Las pruebas deberán veri car que los documentos utilizados
como contexto corresponden efectivamente a la consulta realizada por el
usuario

Como mínimo deberán comprobarse

-   pertinencia de los documentos;
-   prioridad de los resultados;
-   ausencia de información irrelevante;
-   recuperación consistente para consultas equivalentes. No deberá
    considerarse aceptable una respuesta correcta obtenida a partir de
    contexto incorrecto o accidental

## 557. Cobertura de recuperació

Las pruebas deberán validar que la recuperación incorpora toda la
información necesaria para responder adecuadamente la consulta

Como mínimo deberán contemplarse escenarios donde

-   toda la información se encuentra en un único documento;
-   la respuesta requiere múltiples documentos;
-   parte de la información no existe;
-   existen documentos parcialmente relevantes;
-   existen documentos contradictorios. La evaluación deberá veri car
    que el sistema selecciona el contexto más adecuado para cada caso

## 558. Manejo de ausencia de context

Las pruebas deberán veri car el comportamiento del sistema cuando la
información solicitada no se encuentre disponible en la base documental

En estos escenarios deberá comprobarse que el sistema

-   reconoce la ausencia de información su ciente;
-   evita presentar datos como hechos cuando no dispone de evidencia; .

.

s

fi fi fi

:

.

fi

.

.

:

:

n

o

-   comunica claramente las limitaciones del contexto disponible. No
    deberá generarse contenido que aparente estar respaldado por
    documentos inexistentes

## 559. Prevención de alucinacione

Las pruebas deberán evaluar la capacidad del sistema para evitar a
rmaciones no sustentadas por el contexto disponible

Como mínimo deberán veri carse escenarios donde

-   la información solicitada no exista;
-   la información sea ambigua;
-   existan datos incompletos;
-   existan documentos contradictorios. La aprobación requerirá
    demostrar que el sistema distingue adecuadamente entre información
    conocida, inferencias razonables y ausencia de evidencia

## 560. Criterios mínimos para la evaluación de

RA Toda funcionalidad basada en Recuperación Aumentada deberá cumplir,
como mínimo, los siguientes criterios

-   recuperación consistente de documentos relevantes;
-   utilización del contexto recuperado durante la generación;
-   identi cación adecuada de información insu ciente;
-   ausencia de alucinaciones atribuibles a errores de recuperación;
-   separación clara entre conocimiento del modelo y conocimiento
    documental;
-   trazabilidad de las fuentes utilizadas para generar la respuesta. El
    incumplimiento de cualquiera de estos criterios impedirá la
    aprobación de la funcionalidad

## 561. Evaluación de Memoria Conversaciona

Toda funcionalidad que implemente memoria conversacional deberá contar
con pruebas especí cas para validar la conservación, recuperación y
utilización del contexto durante una conversación

Las pruebas deberán demostrar que la información relevante permanece
disponible durante el tiempo de nido por las reglas del sistema fi fi G

fi .

:

.

fi

.

fi

:

.

fi s

.

.

l

## 562. Conservación del context

Las pruebas deberán veri car que el sistema conserva correctamente la
información necesaria entre interacciones consecutivas

Como mínimo deberán validarse los siguientes escenarios

-   referencias a mensajes anteriores;
-   seguimiento de instrucciones previamente proporcionadas;
-   continuidad de conversaciones prolongadas;
-   recuperación del contexto después de múltiples intercambios. La
    pérdida de información relevante deberá considerarse un defecto
    cuando afecte el comportamiento esperado

## 563. Actualización de memori

Las pruebas deberán veri car que la memoria conversacional re eja
correctamente los cambios producidos durante la interacción

Como mínimo deberán comprobarse escenarios donde

-   nueva información sustituye información anterior;
-   preferencias del usuario cambian;
-   instrucciones dejan de ser válidas;
-   el contexto evoluciona durante la conversación. La memoria utilizada
    deberá corresponder al estado más reciente de nido por el usuario o
    por las reglas del sistema

## 564. Límites de memori

Las pruebas deberán validar el comportamiento del sistema cuando la
conversación supera los límites de nidos para la memoria conversacional

Como mínimo deberán evaluarse

-   conversaciones extensas;
-   eliminación controlada de contexto antiguo;
-   conservación de información prioritaria;
-   continuidad funcional después de múltiples intercambios. fi .

fi fi

.

.

:

.

.

a

:

:

a

o

fl fi

El sistema no deberá degradar signi cativamente la calidad de las
respuestas como consecuencia del crecimiento natural de la conversación

## 565. Aislamiento entre conversacione

Las pruebas deberán demostrar que la memoria correspondiente a una
conversación no afecta el comportamiento de otras conversaciones
independientes

Como mínimo deberán veri carse los siguientes escenarios

-   múltiples usuarios simultáneos;
-   múltiples sesiones del mismo usuario cuando así esté de nido;
-   conversaciones paralelas;
-   reinicio de sesiones. No deberá producirse contaminación de contexto
    entre conversaciones distintas

## 566. Evaluación de Tool Callin

Toda integración con herramientas externas deberá contar con pruebas
especí cas que validen la correcta selección, invocación y utilización
de dichas herramientas

Las pruebas deberán evaluar el comportamiento completo del ujo de
ejecución y no únicamente la respuesta nal del modelo

## 567. Selección de herramienta

Las pruebas deberán veri car que el sistema selecciona la herramienta
adecuada para resolver cada solicitud

Como mínimo deberán contemplarse escenarios donde

-   existe una única herramienta aplicable;
-   existen múltiples herramientas disponibles;
-   ninguna herramienta resulta apropiada;
-   la consulta puede resolverse sin utilizar herramientas. La selección
    deberá corresponder con las reglas funcionales de nidas para el
    sistema fi .

fi

fi .

fi

.

:

fi .

:

fl

fi s

g

.

fi s

.

.

## 568. Validación de parámetro

Las pruebas deberán comprobar que los parámetros enviados a cada
herramienta son completos, válidos y consistentes con la solicitud del
usuario

Como mínimo deberán veri carse

-   nombres de parámetros;
-   tipos de datos;
-   valores obligatorios;
-   valores opcionales;
-   formatos esperados;
-   manejo de parámetros inválidos. La invocación no deberá realizarse
    cuando los parámetros incumplan los requisitos de nidos por la
    herramienta

## 569. Manejo de errores en herramienta

Las pruebas deberán validar el comportamiento del sistema cuando una
herramienta no puede completar correctamente su ejecución

Como mínimo deberán contemplarse escenarios donde

-   la herramienta devuelve un error;
-   la herramienta no responde;
-   ocurre un tiempo de espera excedido;
-   la respuesta recibida es inválida;
-   la herramienta devuelve información incompleta. El sistema deberá
    gestionar estos escenarios conforme a las reglas de nidas, evitando
    respuestas engañosas o inconsistentes

## 570. Validación del resultado de Tool Callin

Las pruebas deberán veri car que la respuesta presentada al usuario
incorpora correctamente la información obtenida mediante la herramienta
utilizada

Como mínimo deberán comprobarse

-   utilización efectiva del resultado;
-   consistencia entre la respuesta y los datos obtenidos; .

fi .

fi

:

:

.

.

:

.

s

fi s

fi g

-   ausencia de modi caciones no justi cadas sobre la información
    proporcionada por la herramienta;
-   conservación de la trazabilidad cuando aplique. La respuesta nal
    deberá re ejar elmente el resultado obtenido durante la ejecución
    del Tool Calling

## 571. Evaluación de múltiples herramienta

Las pruebas deberán veri car el comportamiento del sistema cuando una
solicitud requiera la utilización de más de una herramienta durante una
misma interacción

Como mínimo deberán evaluarse los siguientes escenarios

-   ejecución secuencial de herramientas;
-   ejecución dependiente del resultado de una herramienta anterior;
-   utilización de múltiples fuentes de información;
-   combinación de resultados. Las pruebas deberán demostrar que el
    sistema mantiene la consistencia durante todo el ujo de ejecución

## 572. Evaluación de decisiones del model

Cuando el sistema deba decidir entre diferentes estrategias para
resolver una solicitud, deberán ejecutarse pruebas que validen dichas
decisiones

Como mínimo deberán veri carse escenarios donde el modelo deba decidir
entre

-   responder directamente;
-   consultar el motor de recuperación;
-   utilizar una herramienta externa;
-   solicitar información adicional al usuario;
-   rechazar la solicitud por falta de información. Las decisiones
    deberán corresponder con las reglas funcionales de nidas para el
    sistema

## 573. Evaluación de recuperación ante fallo

Las pruebas deberán veri car la capacidad del sistema para continuar
operando cuando una parte del ujo de ejecución falle

Como mínimo deberán contemplarse los siguientes escenarios

-   falla parcial de una herramienta; fl .

.

fi fi

fi fi .

fl fi

fi

fi

.

:

:

o

fi s

s

.

:

fl .

-   indisponibilidad temporal de un servicio;
-   interrupción durante la recuperación documental;
-   error durante la generación de la respuesta. Las pruebas deberán
    demostrar que el sistema mantiene un comportamiento controlado y
    proporciona información su ciente al usuario cuando no sea posible
    completar la operación

## 574. Evaluación de Agentes Especializado

Todo agente especializado deberá contar con pruebas independientes de
las pruebas realizadas sobre el sistema principal

Las pruebas deberán validar el comportamiento propio del agente conforme
a las responsabilidades asignadas

No deberá asumirse que el correcto funcionamiento del sistema principal
garantiza el comportamiento adecuado de cada agente

## 575. Validación del rol del agent

Las pruebas deberán veri car que cada agente mantiene las
responsabilidades de nidas para su función

Como mínimo deberán comprobarse

-   cumplimiento del objetivo funcional;
-   respeto de las restricciones asignadas;
-   utilización adecuada del contexto recibido;
-   consistencia entre decisiones equivalentes. El agente no deberá
    ejecutar tareas que correspondan a otros componentes del sistema

## 576. Coordinación entre agente

Cuando una solicitud requiera la colaboración de múltiples agentes, las
pruebas deberán validar la correcta coordinación entre ellos

Como mínimo deberán veri carse

-   transferencia de contexto;
-   conservación de información relevante;
-   secuencia de ejecución;
-   consistencia del resultado nal; .

fi .

fi fi fi .

:

.

:

.

s

e

s

fi .

.

-   manejo de errores durante la colaboración. Las pruebas deberán
    demostrar que la cooperación entre agentes produce un resultado
    equivalente o superior al obtenido mediante una ejecución individual

## 577. Prevención de ciclos de ejecució

Las pruebas deberán veri car que el sistema evita ciclos de ejecución
involuntarios entre agentes o herramientas

Como mínimo deberán contemplarse escenarios donde

-   un agente invoque repetidamente al mismo agente;
-   múltiples agentes se invoquen mutuamente;
-   una herramienta genere una nueva solicitud equivalente. El sistema
    deberá detectar y controlar estos escenarios conforme a las
    políticas de nidas

## 578. Evaluación de límites operativo

Las pruebas deberán validar el comportamiento del sistema cuando se
alcanzan los límites operativos de nidos para la plataforma

Como mínimo deberán evaluarse

-   número máximo de herramientas por solicitud;
-   profundidad máxima de ejecución;
-   tiempo máximo de procesamiento;
-   consumo máximo de recursos;
-   número máximo de iteraciones. El sistema deberá nalizar la ejecución
    de forma controlada cuando cualquiera de estos límites sea alcanzado

## 579. Evaluación de explicabilida

Cuando el sistema proporcione mecanismos para justi car sus respuestas o
decisiones, las pruebas deberán veri car la consistencia entre la
explicación presentada y el proceso realmente ejecutado

Como mínimo deberán comprobarse

-   correspondencia entre la explicación y las acciones realizadas;
-   referencia a las fuentes utilizadas cuando aplique; .

fi .

.

fi fi fi

:

:

.

d

fi :

s

n

.

fi .

-   ausencia de explicaciones contradictorias;
-   claridad su ciente para facilitar el análisis posterior. Las
    explicaciones no deberán presentar información que no forme parte
    del proceso real de ejecución

## 580. Criterios mínimos para funcionalidades basadas en I

Toda funcionalidad basada en Inteligencia Arti cial únicamente podrá
considerarse apta para su liberación cuando se demuestre, mediante
pruebas, que

-   cumple las instrucciones de nidas para el sistema;
-   mantiene un comportamiento consistente;
-   utiliza correctamente el contexto disponible;
-   selecciona adecuadamente las herramientas requeridas;
-   maneja correctamente los errores;
-   conserva la trazabilidad del proceso;
-   respeta los límites operativos establecidos;
-   genera respuestas alineadas con los objetivos funcionales. El
    incumplimiento de cualquiera de estos criterios impedirá la
    aprobación de la funcionalidad

## 581. Exactitud factua

Toda funcionalidad basada en Inteligencia Arti cial deberá demostrar que
las a rmaciones presentadas al usuario corresponden con información veri
cable conforme al contexto disponible

Las pruebas deberán validar que los hechos, datos, cifras, nombres,
fechas y demás elementos objetivos incluidos en la respuesta son
correctos y consistentes con las fuentes utilizadas durante su
generación

La evaluación deberá diferenciar claramente entre hechos veri cables,
inferencias razonables y contenido generado sin respaldo documental

Cuando una respuesta incluya información objetivamente incorrecta, la
evaluación deberá registrar el defecto como un error de exactitud
factual

## 582. Evaluación de la exactitud factua

Las pruebas de exactitud factual deberán ejecutarse utilizando conjuntos
de evaluación cuyos resultados esperados hayan sido previamente veri
cados .

.

fi .

fi

.

l

fi fi fi

.

:

.

fi

fi fi l

A

.

Como mínimo deberán contemplarse los siguientes escenarios

-   información completamente correcta;
-   información parcialmente correcta;
-   información incorrecta;
-   información contradictoria;
-   información desactualizada;
-   ausencia de información su ciente. La evaluación deberá registrar el
    porcentaje de a rmaciones correctas respecto del total de a
    rmaciones veri cables presentes en la respuesta

## 583. Relevanci

Toda respuesta deberá atender directamente la intención identi cada en
la solicitud del usuario

Las pruebas deberán veri car que la información presentada guarda
relación con la consulta realizada y contribuye al cumplimiento del
objetivo funcional de la interacción

La incorporación de información irrelevante, aun cuando sea correcta,
deberá considerarse una disminución en la calidad de la respuesta

## 584. Evaluación de la relevanci

Las pruebas deberán veri car que la respuesta responde efectivamente a
la necesidad planteada por el usuario

Como mínimo deberán evaluarse los siguientes aspectos

-   correspondencia con la intención detectada;
-   cobertura de la consulta principal;
-   ausencia de desviaciones innecesarias;
-   prioridad de la información más importante. La evaluación podrá
    utilizar escenarios con múltiples formulaciones equivalentes para
    veri car la estabilidad del comportamiento

## 585. Completitu

Toda respuesta deberá proporcionar la información necesaria para
resolver adecuadamente la solicitud realizada por el usuario dentro del
alcance funcional del sistema fi .

fi

fi fi fi

a

.

d

.

fi .

:

:

fi a

.

.

fi .

Las pruebas deberán veri car que no existan omisiones signi cativas que
impidan alcanzar el objetivo de la interacción

La completitud deberá evaluarse considerando únicamente la información
que razonablemente debería estar disponible para el sistema

## 586. Evaluación de la completitu

Las pruebas deberán contemplar escenarios donde la respuesta requiera
integrar múltiples elementos de información

Como mínimo deberán veri carse

-   cobertura de todos los puntos solicitados;
-   identi cación de información faltante;
-   incorporación de advertencias cuando existan limitaciones;
-   diferenciación entre información conocida e información no
    disponible. No deberá penalizarse al sistema por reconocer
    explícitamente la ausencia de información

## 587. Consistenci

El sistema deberá mantener coherencia entre respuestas generadas para
escenarios equivalentes

Las pruebas deberán veri car que las respuestas no presenten
contradicciones respecto de

-   respuestas anteriores;
-   contexto vigente;
-   reglas funcionales;
-   información documental utilizada. La consistencia deberá evaluarse
    independientemente de las variaciones naturales propias del lenguaje

## 588. Evaluación de la consistenci

Las pruebas deberán ejecutar múltiples iteraciones sobre escenarios
equivalentes

Como mínimo deberán veri carse

-   estabilidad de las conclusiones; fi .

fi fi .

.

fi fi

:

:

a

.

fi d

a

.

:

.

.

-   conservación de restricciones;
-   mantenimiento del contexto;
-   ausencia de contradicciones funcionales. Las diferencias puramente
    estilísticas no deberán considerarse defectos cuando el signi cado
    permanezca inalterado

## 589. Clarida

Toda respuesta deberá presentar la información de forma comprensible
para el público objetivo de nido por el sistema

Las pruebas deberán veri car que la redacción facilita la comprensión de
la respuesta sin introducir ambigüedades innecesarias

La claridad deberá evaluarse considerando el contexto de uso y el per l
del usuario previsto para la funcionalidad

## 590. Evaluación de la clarida

Las pruebas deberán veri car, como mínimo

-   estructura lógica de la respuesta;
-   utilización consistente de la terminología;
-   ausencia de ambigüedad signi cativa;
-   organización adecuada del contenido;
-   facilidad para identi car la información principal. La evaluación
    podrá incorporar revisiones humanas cuando la automatización no
    permita medir adecuadamente este atributo

## 591. Robuste

Toda funcionalidad basada en Inteligencia Arti cial deberá mantener un
comportamiento estable cuando reciba entradas inesperadas, ambiguas,
incompletas o incorrectas

Las pruebas deberán veri car que el sistema continúa proporcionando
respuestas controladas sin comprometer la integridad del proceso, la
seguridad de la información o la experiencia del usuario

La robustez deberá evaluarse considerando escenarios que di eran signi
cativamente de las condiciones ideales previstas durante el diseño de la
funcionalidad fi .

.

fi .

.

fi fi fi d

z

.

fi

.

:

fi

fi d

.

fi fi .

fi

## 592. Evaluación de la robuste

Las pruebas deberán incluir, como mínimo, los siguientes escenarios

-   consultas con errores ortográ cos;
-   instrucciones incompletas;
-   solicitudes ambiguas;
-   información contradictoria;
-   entradas excesivamente extensas;
-   consultas excesivamente breves;
-   caracteres especiales;
-   idiomas no previstos;
-   formatos inesperados. La evaluación deberá veri car que el sistema
    mantiene un comportamiento controlado y comunica claramente
    cualquier limitación cuando no sea posible resolver la solicitud

## 593. Con abilida

Toda funcionalidad deberá producir resultados consistentes cuando sea
ejecutada repetidamente bajo condiciones equivalentes

Las pruebas deberán demostrar que las variaciones propias del modelo no
afectan el cumplimiento de los objetivos funcionales de nidos para el
sistema

La con abilidad deberá medirse considerando tanto la estabilidad de las
respuestas como la repetibilidad del comportamiento general

## 594. Evaluación de la con abilida

Las pruebas deberán ejecutar múltiples iteraciones utilizando conjuntos
de datos representativos

Como mínimo deberán veri carse

-   estabilidad de los resultados;
-   cumplimiento constante de las restricciones;
-   mantenimiento del comportamiento esperado;
-   ausencia de degradación signi cativa entre ejecuciones. La
    evaluación deberá registrar las desviaciones observadas y determinar
    si permanecen dentro de los límites aceptables de nidos para la
    funcionalidad fi fi

fi fi

fi

fi fi .

:

d

.

fi

.

fi

z

.

:

d

.

.

## 595. Trazabilida

Toda respuesta generada deberá poder relacionarse con las fuentes,
decisiones y procesos que participaron en su construcción cuando la
naturaleza de la funcionalidad así lo permita

Las pruebas deberán veri car que existe evidencia su ciente para
reconstruir el proceso seguido por el sistema durante la generación de
la respuesta

La trazabilidad constituye un requisito fundamental para facilitar el
diagnóstico de incidentes, la auditoría técnica y la mejora continua

## 596. Evaluación de la trazabilida

Las pruebas deberán comprobar, como mínimo

-   identi cación de las fuentes utilizadas;
-   conservación de identi cadores de correlación;
-   registro de herramientas ejecutadas;
-   registro del contexto recuperado;
-   evidencia del ujo de ejecución. La ausencia de mecanismos que
    permitan reconstruir razonablemente una respuesta deberá registrarse
    como una de ciencia de calidad

## 597. Transparenci

Cuando la funcionalidad requiera explicar el origen o fundamento de una
respuesta, el sistema deberá proporcionar información su ciente para
comprender cómo se obtuvo el resultado

Las pruebas deberán veri car que las explicaciones ofrecidas son
consistentes con el proceso realmente ejecutado y no introducen
información cticia o engañosa

La transparencia deberá evaluarse conforme al nivel de detalle de nido
para cada caso de uso

## 598. Evaluación de la transparenci

Las pruebas deberán validar que fi fl fi fi fi fi

:

d

fi .

a

.

:

fi .

fi fi .

d

a

.

.

.

-   las referencias corresponden a las fuentes realmente utilizadas;
-   las explicaciones son consistentes con la ejecución;
-   no se atribuyen capacidades inexistentes al sistema;
-   las limitaciones son comunicadas de forma explícita cuando
    corresponda. La evaluación no deberá exigir la exposición de
    información técnica cuya divulgación comprometa la seguridad o el
    funcionamiento interno del sistema

## 599. Utilida

Toda respuesta generada deberá contribuir al cumplimiento del objetivo
funcional de la interacción

Las pruebas deberán veri car que la información proporcionada permite al
usuario avanzar, tomar una decisión o resolver el problema planteado

Una respuesta técnicamente correcta pero incapaz de satisfacer la
necesidad del usuario deberá considerarse de utilidad insu ciente

## 600. Evaluación de la utilida

Las pruebas deberán veri car, como mínimo

-   resolución efectiva de la solicitud;
-   adecuación al contexto de uso;
-   aplicabilidad de la información proporcionada;
-   su ciencia para completar la tarea esperada;
-   ausencia de información innecesaria que di culte la comprensión. La
    utilidad deberá evaluarse considerando el objetivo funcional de la
    interacción y no únicamente la calidad lingüística de la respuesta

## 601. Arquitectura de las Suites de Evaluació

Toda funcionalidad basada en Inteligencia Arti cial deberá disponer de
una o más suites de evaluación estructuradas conforme al objetivo
funcional de la característica evaluada

Las suites deberán diseñarse de forma modular, permitiendo su ejecución
independiente y su integración dentro de procesos automatizados de
validación

Cada suite deberá evaluar una única capacidad funcional y producir
resultados independientes de otras suites fi .

.

d

fi fi fi

.

fi

:

fi

.

.

.

d

.

.

n

La aprobación de una funcionalidad requerirá la ejecución satisfactoria
de todas las suites aplicables

## 602. Clasi cación de las Suites de Evaluació

Las suites de evaluación deberán clasi carse conforme al objetivo de la
validación

Como mínimo deberán existir las siguientes categorías

-   evaluación funcional;
-   evaluación de recuperación documental;
-   evaluación conversacional;
-   evaluación de herramientas externas;
-   evaluación de memoria;
-   evaluación de robustez;
-   evaluación de seguridad;
-   evaluación de regresión. Una misma funcionalidad podrá formar parte
    de múltiples suites cuando así lo requiera su comportamiento
    esperado

## 603. Independencia de las Suite

Cada suite deberá poder ejecutarse de forma aislada

Las pruebas incluidas en una suite no deberán depender del resultado
obtenido por otra

No se permitirá la reutilización de estado entre ejecuciones salvo
cuando dicha dependencia forme parte explícita del escenario bajo
evaluación

La independencia facilitará la identi cación del origen de los defectos
y reducirá el riesgo de resultados inconsistentes

## 604. Diseño de Casos de Evaluació

Todo caso de evaluación deberá documentarse utilizando una estructura
uniforme

Como mínimo deberá incluir

-   identi cador único; fi .

fi

.

.

:

fi

fi

.

.

:

s

n

.

.

.

n

-   objetivo;
-   capacidad evaluada;
-   entrada utilizada;
-   contexto requerido;
-   resultado esperado;
-   criterios de aceptación;
-   evidencia generada. Cada caso deberá mantenerse bajo control de
    versiones junto con el resto del proyecto

## 605. Cobertura del Conjunto de Evaluació

Las suites deberán cubrir de forma representativa los distintos
escenarios esperados para la funcionalidad evaluada

Como mínimo deberán contemplarse

-   escenarios normales;
-   escenarios límite;
-   escenarios inválidos;
-   escenarios ambiguos;
-   escenarios incompletos;
-   escenarios de recuperación;
-   escenarios de error. La incorporación de nuevos escenarios deberá
    responder a incidentes reales, cambios funcionales o identi cación
    de riesgos previamente no contemplados

## 606. Datos de Evaluació

Los datos utilizados durante la evaluación deberán mantenerse separados
de los datos empleados para el entrenamiento, con guración o desarrollo
del sistema

Todo conjunto de evaluación deberá permanecer estable durante una misma
línea base de comparación

La modi cación de los datos de evaluación requerirá la generación de una
nueva versión del conjunto y la conservación del historial
correspondiente

## 607. Baselines de Evaluació

fi fi

.

.

fi

:

n

.

.

n

.

.

n

Toda funcionalidad deberá disponer de un baseline contra el cual
comparar nuevas implementaciones

El baseline deberá representar el comportamiento aceptado de la
funcionalidad en el momento de su aprobación

Las evaluaciones posteriores deberán determinar si una nueva versión

-   mantiene el comportamiento esperado;
-   mejora los resultados obtenidos;
-   introduce regresiones;
-   modi ca el comportamiento funcional. La sustitución del baseline
    requerirá aprobación formal conforme al proceso de gestión de
    cambios del proyecto

## 608. Evaluación de Regresió

Toda modi cación realizada sobre componentes de Inteligencia Arti cial
deberá ejecutarse contra el conjunto completo de pruebas de regresión
correspondiente

Las pruebas deberán veri car que los cambios introducidos no afectan
funcionalidades previamente aprobadas

La detección de una regresión impedirá la liberación de la nueva versión
hasta que el comportamiento esperado sea restablecido o el cambio sea
formalmente aceptado

## 609. Métricas de Cobertur

Toda ejecución de una suite deberá generar métricas que permitan evaluar
el grado de cobertura alcanzado

Como mínimo deberán medirse

-   cobertura de escenarios;
-   cobertura de capacidades;
-   cobertura de intenciones;
-   cobertura de herramientas cuando aplique;
-   cobertura documental para funcionalidades basadas en recuperación;
-   cobertura conversacional cuando corresponda. Las métricas deberán
    utilizarse como apoyo para identi car áreas insu cientemente
    evaluadas fi .

fi .

.

.

.

fi

:

fi a

n

fi

.

:

fi .

.

## 610. Evidencia de las Suite

Cada ejecución deberá generar evidencia su ciente para permitir la
reproducción del proceso de evaluación

Como mínimo deberá conservarse

-   versión del sistema;
-   versión del modelo;
-   versión del conjunto de evaluación;
-   identi cación de la suite ejecutada;
-   fecha y hora;
-   resultados individuales;
-   métricas agregadas;
-   incidencias detectadas. La evidencia deberá permanecer disponible
    durante el periodo de nido por la política de conservación del
    proyecto

## 611. De nición de Métricas de Evaluació

Toda suite de evaluación deberá de nir explícitamente las métricas
mediante las cuales será determinada la calidad de la funcionalidad
evaluada

Las métricas deberán ser objetivas, repetibles y comparables entre
distintas ejecuciones

No deberán utilizarse criterios ambiguos o dependientes exclusivamente
del juicio individual del evaluador

Cada métrica deberá indicar, como mínimo

-   objetivo de medición;
-   método de cálculo;
-   unidad de medida;
-   frecuencia de evaluación;
-   umbral de aceptación.

## 612. Clasi cación de las Métrica

Las métricas deberán clasi carse conforme al aspecto del sistema que
evalúan

Como mínimo podrán agruparse en las siguientes categorías

-   métricas funcionales; fi .

.

fi

fi

.

fi :

fi

:

fi .

s

:

fi s

.

n

.

-   métricas de calidad de respuesta;
-   métricas de recuperación de información;
-   métricas de desempeño;
-   métricas de estabilidad;
-   métricas operativas. La clasi cación facilitará la interpretación de
    resultados y la identi cación de áreas susceptibles de mejora

## 613. Umbrales de Aceptació

Toda métrica deberá contar con un umbral de aceptación previamente de
nido

Los umbrales deberán establecerse antes de ejecutar la evaluación y no
podrán modi carse con el propósito de aprobar una implementación especí
ca

Cuando una métrica no alcance el umbral establecido, la funcionalidad
deberá considerarse no conforme hasta que se implementen las acciones
correctivas correspondientes o se apruebe formalmente una excepción

## 614. Estabilidad Estadístic

Las métricas obtenidas deberán demostrar estabilidad entre ejecuciones
equivalentes

Las pruebas deberán ejecutarse el número de veces necesario para reducir
el impacto de la variabilidad inherente a los modelos de Inteligencia
Arti cial

Cuando se detecten diferencias estadísticamente signi cativas entre
ejecuciones equivalentes, deberá analizarse su origen antes de aprobar
la funcionalidad

La metodología utilizada para determinar la estabilidad deberá
documentarse y mantenerse consistente durante toda la vida del proyecto

## 615. Comparación entre Versione

Toda nueva versión de una funcionalidad deberá compararse contra el
baseline vigente

La comparación deberá identi car

-   mejoras funcionales; fi .

.

fi

:

.

fi .

fi fi a

n

.

.

fi s

fi .

fi .

.

-   degradaciones;
-   cambios esperados;
-   efectos secundarios;
-   nuevas limitaciones. Los resultados deberán conservarse como parte
    del historial evolutivo del sistema

## 616. Gestión de Regresione

Toda disminución de calidad detectada durante la evaluación deberá clasi
carse como una regresión potencial

Las regresiones deberán registrarse indicando, como mínimo

-   versión donde aparece;
-   funcionalidad afectada;
-   evidencia objetiva;
-   severidad;
-   impacto funcional;
-   estado de resolución. La existencia de una regresión crítica
    impedirá la liberación de la versión correspondiente

## 617. Priorización de Defecto

Los defectos identi cados durante la evaluación deberán clasi carse
conforme al impacto que producen sobre la funcionalidad

Como mínimo deberán contemplarse los siguientes niveles

-   crítico;

-   alto;

-   medio;

-   bajo. La clasi cación deberá considerar

-   impacto sobre el usuario;

-   frecuencia estimada;

-   posibilidad de recuperación;

-   riesgo operativo;

-   riesgo de información incorrecta.

fi

fi .

.

:

s

:

s

:

fi fi .

.

## 618. Gestión de Excepcione

Cuando una funcionalidad no cumpla alguno de los criterios establecidos,
únicamente podrá liberarse mediante un proceso formal de aceptación de
riesgos

Toda excepción deberá documentar

-   requisito incumplido;
-   justi cación;
-   riesgos identi cados;
-   medidas de mitigación;
-   responsable de la aprobación;
-   vigencia de la excepción. Las excepciones deberán revisarse
    periódicamente hasta su eliminación

## 619. Reportes de Evaluació

Cada ejecución de una suite deberá generar un reporte técnico
estandarizado

Como mínimo deberá incluir

-   identi cación de la ejecución;
-   versión evaluada;
-   suites ejecutadas;
-   métricas obtenidas;
-   defectos encontrados;
-   cumplimiento de umbrales;
-   recomendaciones;
-   conclusión de la evaluación. El formato del reporte deberá
    mantenerse uniforme para facilitar comparaciones históricas

## 620. Aprobación Técnic

Una funcionalidad basada en Inteligencia Arti cial únicamente podrá
considerarse aprobada cuando

-   todas las suites obligatorias hayan sido ejecutadas;
-   las métricas cumplan los umbrales establecidos;
-   no existan defectos críticos abiertos;
-   las regresiones hayan sido resueltas o aceptadas formalmente; fi fi
    :

fi

:

:

fi

a

n

s

.

.

.

.

-   la evidencia de evaluación se encuentre disponible para auditoría.
    La aprobación técnica constituirá el requisito previo para continuar
    con el proceso de liberación de nido por la organización

## 621. Integración de la Evaluación en el

Pipeline de CI/C Toda funcionalidad basada en Inteligencia Arti cial
deberá incorporar sus procesos de evaluación dentro del pipeline o cial
de Integración Continua y Entrega Continua

La ejecución de las suites de evaluación deberá formar parte del proceso
de validación previo a la integración del código y deberá producir
resultados veri cables antes de autorizar la liberación de una nueva
versión

No se permitirá omitir evaluaciones obligatorias mediante con guraciones
temporales o procedimientos manuales no autorizados

## 622. Estrategia de Ejecución por Etapa

Las suites de evaluación deberán distribuirse conforme a las distintas
etapas del ciclo de integración

Como mínimo deberán de nirse los siguientes niveles

-   evaluación durante el desarrollo local;
-   evaluación durante la Integración Continua;
-   evaluación previa a la liberación;
-   evaluación posterior al despliegue. Cada nivel deberá contener
    únicamente las pruebas necesarias para el objetivo correspondiente,
    evitando duplicidad innecesaria y optimizando el tiempo total del
    pipeline

## 623. Clasi cación por Tiempo de Ejecució

Las suites deberán clasi carse según su duración estimada

Como mínimo deberán contemplarse las siguientes categorías

-   ejecución rápida;
-   ejecución estándar; fi .

fi .

fi fi .

fi

D

.

fi :

fi .

:

fi

.

.

s

n

-   ejecución extendida. Las pruebas de ejecución rápida deberán
    proporcionar retroalimentación inmediata al desarrollador

Las pruebas de ejecución extendida podrán programarse para ejecutarse de
forma periódica o antes de una liberación mayor

La clasi cación deberá revisarse periódicamente para mantener un
equilibrio entre cobertura y tiempo de validación

## 624. Condiciones de Bloqueo del Pipelin

El pipeline deberá impedir automáticamente la promoción de una versión
cuando ocurra cualquiera de las siguientes condiciones

-   incumplimiento de métricas obligatorias;
-   fallo en suites críticas;
-   detección de regresiones críticas;
-   ausencia de evidencia requerida;
-   ejecución incompleta de las pruebas obligatorias. Las reglas de
    bloqueo deberán mantenerse bajo control de versiones y cualquier
    modi cación requerirá el mismo proceso de revisión que el código
    fuente

## 625. Ejecución Selectiva de Suite

Cuando la arquitectura del proyecto lo permita, el pipeline podrá
ejecutar únicamente las suites afectadas por los cambios introducidos

La selección deberá basarse en la relación documentada entre
funcionalidades, componentes y suites de evaluación

No deberá excluirse ninguna prueba cuya omisión pueda comprometer la
detección de defectos relevantes

La estrategia utilizada deberá documentarse y revisarse periódicamente

## 626. Paralelización de la Evaluació

fi .

.

.

.

.

.

:

.

s

.

n

e

fi

Las suites independientes deberán ejecutarse en paralelo siempre que
ello no afecte la con abilidad de los resultados

La paralelización deberá garantizar

-   aislamiento entre ejecuciones;
-   independencia de los datos de evaluación;
-   consistencia de los resultados;
-   utilización e ciente de los recursos disponibles. Las pruebas
    concurrentes no deberán introducir variabilidad adicional en las
    métricas obtenidas

## 627. Gestión de Dependencias del Entorn

Antes de iniciar la evaluación, el pipeline deberá veri car la
disponibilidad de todos los componentes requeridos para la ejecución de
las pruebas

Como mínimo deberán comprobarse

-   servicios de almacenamiento;
-   motores de recuperación;
-   herramientas externas simuladas o reales según corresponda;
-   infraestructura de observabilidad;
-   bases de datos;
-   sistemas de mensajería. La evaluación no deberá iniciarse cuando las
    dependencias críticas no se encuentren disponibles

## 628. Control de Versiones de los Activos de

Evaluació Todos los elementos utilizados durante la evaluación deberán
mantenerse bajo control de versiones

Como mínimo deberán versionarse

-   suites;
-   casos de evaluación;
-   datasets;
-   con guraciones;
-   prompts de evaluación;
-   criterios de aceptación;
-   scripts de automatización. fi fi

.

fi

n

.

:

:

:

fi .

o

.

.

La versión utilizada durante cada ejecución deberá quedar registrada
como parte de la evidencia generada

## 629. Gestión de Resultados Histórico

Los resultados obtenidos durante las evaluaciones deberán conservarse
para permitir análisis evolutivos del comportamiento del sistema

Como mínimo deberá mantenerse información sobre

-   tendencia de métricas;
-   evolución de defectos;
-   regresiones detectadas;
-   estabilidad entre versiones;
-   tiempo promedio de ejecución;
-   cumplimiento histórico de umbrales. La conservación de esta
    información permitirá identi car degradaciones graduales que podrían
    pasar desapercibidas en evaluaciones aisladas

## 630. Repetibilidad de la Evaluació

Toda ejecución del pipeline deberá ser reproducible utilizando la misma
versión del código, los mismos activos de evaluación y una con guración
equivalente

Las diferencias observadas entre ejecuciones deberán poder explicarse
mediante cambios identi cables en alguno de los componentes del proceso

La imposibilidad de reproducir una evaluación deberá considerarse un
incidente del proceso de aseguramiento de la calidad

## 631. Gobierno de los Activos de Evaluació

Todos los activos utilizados durante el proceso de evaluación deberán
estar sujetos a un proceso formal de gobierno

Se consideran activos de evaluación, entre otros

-   suites de evaluación;
-   casos de prueba;
-   datasets;
-   métricas; fi

.

.

.

fi .

.

:

:

fi .

.

n

s

n

-   umbrales;
-   criterios de aceptación;
-   scripts de automatización;
-   con guraciones de ejecución. Toda modi cación deberá ser controlada,
    documentada y trazable

## 632. Revisión de los Activos de Evaluació

Los activos de evaluación deberán revisarse mediante el mismo proceso de
revisión técnica aplicado al código fuente

La revisión deberá veri car, como mínimo

-   consistencia técnica;
-   cobertura funcional;
-   ausencia de duplicidad;
-   claridad de los criterios;
-   calidad de la documentación;
-   impacto sobre las suites existentes. No deberán incorporarse nuevos
    activos sin evidencia de revisión técnica

## 633. Trazabilidad entre Requisitos y

Evaluació Todo requisito funcional deberá poder relacionarse con uno o
más casos de evaluación

La trazabilidad deberá permitir identi car

-   requisito;
-   componente implementado;
-   suites aplicables;
-   casos de evaluación;
-   evidencia generada;
-   resultado obtenido. La ausencia de trazabilidad impedirá demostrar
    objetivamente el cumplimiento del requisito

## 634. Matriz de Cobertur

fi

fi

n

fi

.

fi :

:

a

.

.

.

n

.

El proyecto deberá mantener una matriz de cobertura que permita
visualizar la relación entre requisitos, funcionalidades y activos de
evaluación

La matriz deberá identi car, como mínimo

-   requisitos sin pruebas;
-   pruebas sin requisito asociado;
-   funcionalidades parcialmente cubiertas;
-   áreas pendientes de evaluación. La matriz deberá actualizarse como
    parte del proceso normal de desarrollo

## 635. Gestión de Cambios en los Activos de

Evaluació Toda modi cación de un activo de evaluación deberá analizar su
impacto sobre

-   métricas existentes;
-   resultados históricos;
-   suites relacionadas;
-   criterios de aceptación;
-   pipelines automatizados. Las modi caciones deberán documentarse
    antes de su incorporación al repositorio principal

## 636. Obsolescencia de Casos de Evaluació

Los casos de evaluación que dejen de representar el comportamiento
esperado deberán identi carse como obsoletos

Antes de su eliminación deberá veri carse que

-   el requisito correspondiente dejó de existir;
-   fue sustituido por otro caso equivalente;
-   no afecta la cobertura mínima establecida;
-   la decisión quedó documentada. La eliminación de casos de evaluación
    no deberá provocar pérdida de trazabilidad histórica

## 637. Auditoría de la Arquitectura de Testin

fi fi fi

n

fi

.

fi

:

:

.

.

:

n

g

.

.

La arquitectura de testing deberá auditarse periódicamente para veri car
su vigencia y e cacia

La auditoría deberá evaluar, entre otros aspectos

-   cobertura;
-   calidad de los datasets;
-   vigencia de métricas;
-   consistencia de umbrales;
-   e cacia de las suites;
-   estabilidad del pipeline;
-   cumplimiento del presente estándar. Los resultados deberán
    documentarse y dar origen, cuando corresponda, a acciones de mejora

## 638. Indicadores del Proceso de Evaluació

El proceso de evaluación deberá disponer de indicadores que permitan
medir su desempeño

Como mínimo podrán considerarse

-   porcentaje de cobertura;
-   tiempo promedio de ejecución;
-   porcentaje de regresiones detectadas;
-   defectos identi cados antes de producción;
-   estabilidad de las métricas;
-   evolución de la calidad entre versiones. Los indicadores deberán
    utilizarse para la mejora continua del proceso y no únicamente como
    mecanismos de control

## 639. Mejora Continua del Proces

La arquitectura de testing deberá evolucionar conforme cambien los
requisitos del proyecto, la tecnología utilizada y los riesgos identi
cados

Las mejoras deberán fundamentarse en evidencia objetiva obtenida durante

-   auditorías;
-   incidentes;
-   resultados históricos;
-   análisis de cobertura;
-   retroalimentación de los equipos de desarrollo y calidad. Toda
    mejora deberá incorporarse manteniendo la compatibilidad con los
    principios de nidos en este documento fi

fi .

.

:

fi

.

:

fi o

:

fi fi n

.

.

.

## 640. Principios Rectores de la Arquitectura

de Testin Toda arquitectura de testing para sistemas basados en
Inteligencia Arti cial deberá observar, como mínimo, los siguientes
principios

-   objetividad;
-   reproducibilidad;
-   automatización;
-   trazabilidad;
-   independencia;
-   mantenibilidad;
-   evidencia veri cable;
-   mejora continua;
-   gobierno de los activos de evaluación;
-   integración con el ciclo de vida del desarrollo. Estos principios
    deberán guiar el diseño, implementación, operación y evolución del
    proceso de evaluación durante toda la vida útil del sistema

## 641. Retroalimentación desde Producció

El proceso de evaluación deberá incorporar información obtenida durante
la operación del sistema para mejorar continuamente la cobertura y e
cacia de las pruebas

La información recopilada deberá analizarse periódicamente con el
propósito de identi car escenarios no contemplados durante el diseño
inicial de las suites de evaluación

La retroalimentación proveniente de producción deberá integrarse
mediante un proceso controlado y documentado

## 642. Incorporación de Incidentes al Proceso

de Evaluació Todo incidente con rmado relacionado con el comportamiento
de funcionalidades basadas en Inteligencia Arti cial deberá dar origen
al análisis de la cobertura existente

Cuando el incidente corresponda a un escenario previamente no
contemplado, deberá incorporarse un nuevo caso de evaluación que permita
evitar la reaparición del mismo defecto

fi

fi

g

fi

.

n

:

.

fi fi .

.

.

n

fi .

La resolución de un incidente no deberá considerarse completa hasta veri
car que el proceso de evaluación ha sido actualizado conforme
corresponda

## 643. Gestión de Casos Recurrente

Los incidentes que se presenten de forma repetitiva deberán analizarse
para determinar si existen de ciencias en la arquitectura de testing

Las revisiones deberán considerar, como mínimo

-   insu ciencia de cobertura;
-   criterios de aceptación inadecuados;
-   datasets incompletos;
-   métricas insu cientes;
-   limitaciones en la automatización. Las acciones correctivas deberán
    priorizar la eliminación de la causa raíz y no únicamente la
    corrección del defecto individual

## 644. Evolución del Conjunto de Evaluació

Los conjuntos de evaluación deberán evolucionar de forma controlada
conforme aumente el conocimiento adquirido durante el desarrollo y
operación del sistema

La incorporación de nuevos escenarios deberá justi carse mediante

-   cambios funcionales;
-   nuevos requisitos;
-   incidentes;
-   riesgos identi cados;
-   mejoras derivadas de revisiones técnicas. Toda modi cación deberá
    preservar la trazabilidad histórica de los resultados

## 645. Validación Continu

La evaluación de funcionalidades basadas en Inteligencia Arti cial no
deberá limitarse al momento previo a la liberación de una versión

Las suites de evaluación deberán ejecutarse periódicamente conforme a la
estrategia de nida por el proyecto, con el propósito de detectar cambios
no previstos en el comportamiento del sistema fi fi fi

fi fi

.

.

.

:

fi a

.

fi :

.

s

fi .

fi n

.

La periodicidad de dichas evaluaciones deberá documentarse como parte
del proceso de aseguramiento de la calidad

## 646. Gestión de Deriva Funciona

El proceso de evaluación deberá contemplar mecanismos para detectar
desviaciones respecto del comportamiento funcional previamente aprobado

Las pruebas periódicas deberán identi car cambios signi cativos en
aspectos tales como

-   cumplimiento de instrucciones;
-   consistencia funcional;
-   comportamiento conversacional;
-   utilización del contexto;
-   aplicación de reglas de negocio. Toda deriva funcional deberá
    analizarse antes de autorizar nuevas liberaciones

## 647. Revisión Periódica de Métrica

Las métricas utilizadas durante la evaluación deberán revisarse
periódicamente para veri car que continúan siendo representativas del
comportamiento esperado

La revisión deberá considerar

-   cambios en los objetivos funcionales;
-   evolución del sistema;
-   nuevos riesgos identi cados;
-   resultados históricos. Las modi caciones deberán aprobarse conforme
    al proceso de gestión de cambios de nido por la organización

## 648. Gestión del Conocimiento Derivado de la

Evaluació Los aprendizajes obtenidos durante la ejecución de las suites
deberán documentarse cuando aporten información relevante para la mejora
del proceso de evaluación

Como mínimo podrán registrarse fi .

fi

n

.

:

:

fi .

fi .

l

.

s

.

fi fi :

-   patrones de fallos;
-   escenarios frecuentes;
-   limitaciones identi cadas;
-   recomendaciones de mejora;
-   decisiones adoptadas. La documentación generada deberá facilitar la
    transferencia de conocimiento entre los equipos de ingeniería

## 649. Validación de Acciones Correctiva

Toda acción correctiva implementada como resultado de un incidente o una
evaluación deberá veri carse mediante nuevas pruebas antes de
considerarse concluida

La validación deberá demostrar que

-   el defecto original fue corregido;
-   no se introdujeron regresiones;
-   la cobertura continúa siendo su ciente;
-   la solución cumple los criterios establecidos por el presente
    estándar.

## 650. Mejora Continua de la Arquitectura de

Testin La Arquitectura de Testing deberá mantenerse como un proceso
evolutivo

Las mejoras deberán fundamentarse en evidencia objetiva obtenida
mediante

-   resultados de evaluación;
-   análisis de cobertura;
-   revisiones técnicas;
-   auditorías;
-   incidentes;
-   experiencia acumulada durante el desarrollo y operación del sistema.
    Toda actualización deberá preservar la coherencia con los principios
    rectores de nidos en este documento

## 651. Gobierno del Proceso de Evaluació

El proceso de evaluación deberá operar bajo un modelo de gobierno que
garantice la aplicación consistente de los principios de nidos en el
presente documento fi

.

g

.

fi

fi fi

:

.

.

.

:

fi s

n

El gobierno deberá establecer responsabilidades, mecanismos de control y
procesos de decisión que aseguren la calidad, trazabilidad y evolución
continua de la arquitectura de testing

Las decisiones relacionadas con la evaluación deberán basarse en
evidencia objetiva y criterios previamente documentados

## 652. Roles y Responsabilidade

La organización deberá de nir claramente las responsabilidades de los
participantes en el proceso de evaluación

Como mínimo deberán establecerse responsabilidades para

-   de nición de criterios de aceptación;
-   diseño de suites de evaluación;
-   mantenimiento de datasets;
-   ejecución de evaluaciones;
-   análisis de resultados;
-   aprobación técnica;
-   gestión de excepciones. Una misma persona podrá desempeñar múltiples
    funciones siempre que no se comprometa la objetividad del proceso

## 653. Separación de Responsabilidade

Siempre que la estructura del proyecto lo permita, la de nición de los
criterios de aceptación y la aprobación técnica deberán mantenerse
separadas de la implementación de la funcionalidad evaluada

Cuando dicha separación no resulte posible, deberán implementarse
mecanismos compensatorios, tales como revisiones cruzadas o aprobaciones
adicionales

El objetivo de esta separación será reducir el riesgo de sesgos durante
el proceso de evaluación

## 654. Gestión de Riesgos del Proceso de

Evaluació fi .

n

.

.

fi

.

fi :

s

.

s

.

.

El proceso de evaluación deberá incorporar un análisis periódico de los
riesgos que puedan afectar su e cacia

Como mínimo deberán identi carse riesgos relacionados con

-   cobertura insu ciente;
-   obsolescencia de datasets;
-   automatización incompleta;
-   dependencia excesiva de evaluaciones manuales;
-   métricas inadecuadas;
-   pérdida de trazabilidad. Los riesgos deberán registrarse,
    priorizarse y contar con planes de tratamiento cuando corresponda

## 655. Aprobación de Cambios Relevante

Toda modi cación que afecte signi cativamente la arquitectura de testing
deberá someterse a un proceso formal de revisión

Como mínimo deberán considerarse cambios relacionados con

-   incorporación de nuevas suites;
-   modi cación de métricas;
-   cambios en umbrales;
-   actualización de datasets;
-   rede nición de criterios de aceptación;
-   modi cación del pipeline de evaluación. Las decisiones deberán
    documentarse como parte del historial del proyecto

## 656. Gestión de Excepciones del Proces

Las excepciones concedidas durante el proceso de evaluación deberán
registrarse y revisarse periódicamente

Cada excepción deberá indicar

-   alcance;
-   motivo;
-   responsable de aprobación;
-   fecha de autorización;
-   vigencia;
-   condiciones para su eliminación. fi fi fi

fi fi .

fi .

.

.

fi :

fi

:

:

.

o

s

Las excepciones no deberán convertirse en mecanismos permanentes para
eludir los requisitos establecidos por este estándar

## 657. Revisión de la Arquitectura de Testin

La Arquitectura de Testing deberá revisarse de forma periódica para veri
car que continúa siendo adecuada para los objetivos del proyecto

La revisión deberá evaluar

-   alineación con la arquitectura del sistema;
-   e cacia de las suites;
-   evolución tecnológica;
-   cambios en los riesgos;
-   experiencia adquirida durante el desarrollo. Las conclusiones
    deberán documentarse y traducirse en acciones concretas de mejora
    cuando corresponda

## 658. Indicadores del Gobierno de Calida

El modelo de gobierno deberá de nir indicadores que permitan evaluar la
e cacia del propio proceso de aseguramiento de la calidad

Como mínimo podrán considerarse

-   porcentaje de requisitos cubiertos;
-   porcentaje de automatización;
-   tiempo promedio para detectar defectos;
-   tiempo promedio para corregir regresiones;
-   estabilidad del pipeline;
-   evolución del cumplimiento de umbrales. Estos indicadores deberán
    emplearse para orientar decisiones de mejora y no como único
    mecanismo de evaluación del desempeño individual

## 659. Gestión del Conocimiento

Organizaciona fi .

:

.

l

fi

:

.

.

.

fi fi d

g

El conocimiento generado durante el proceso de evaluación deberá
preservarse como un activo organizacional

Las lecciones aprendidas, patrones identi cados y mejoras implementadas
deberán documentarse y ponerse a disposición de los equipos de
ingeniería

La documentación deberá mantenerse actualizada y formar parte del
proceso normal de incorporación de nuevos integrantes al proyecto

## 660. Principios de Gobierno de la

Arquitectura de Testin El gobierno de la Arquitectura de Testing deberá
sustentarse, como mínimo, en los siguientes principios

-   objetividad;
-   independencia;
-   evidencia veri cable;
-   trazabilidad;
-   responsabilidad claramente de nida;
-   mejora continua;
-   transparencia en la toma de decisiones;
-   control de cambios;
-   preservación del conocimiento. Estos principios deberán orientar
    todas las actividades relacionadas con el aseguramiento de la
    calidad de funcionalidades basadas en Inteligencia Arti cial

## 661. Patrón de Evaluación Funciona

Toda nueva funcionalidad basada en Inteligencia Arti cial deberá iniciar
su proceso de evaluación mediante un patrón funcional estandarizado

El patrón funcional constituye la unidad mínima de validación y tiene
como propósito demostrar que la funcionalidad cumple los objetivos para
los cuales fue diseñada

Como mínimo deberá incluir

-   objetivo funcional;
-   alcance;
-   entradas válidas;
-   entradas inválidas;
-   comportamiento esperado;

:

fi .

:

fi

fi .

g

.

fi fi .

.

.

l

-   criterios de aceptación;
-   evidencia requerida. La utilización de este patrón será obligatoria
    para toda nueva capacidad incorporada al sistema

## 662. Estructura del Patró

Todo patrón de evaluación deberá mantener una estructura uniforme

Como mínimo deberá contener los siguientes elementos

Identi cación

-   código único;

-   nombre;

-   versión. Objetivo

-   capacidad evaluada;

-   alcance de la evaluación. Preparación

-   precondiciones;

-   con guración requerida;

-   datos necesarios. Ejecución

-   procedimiento;

-   entradas;

-   acciones. Veri cación

-   resultados esperados;

-   métricas;

-   criterios de aceptación. Evidencia

-   registros;

-   métricas;

-   resultados. La estructura deberá mantenerse consistente para
    facilitar la reutilización de los patrones fi fi fi

n

:

.

.

.

## 663. Patrón para Funcionalidades

Conversacionale Las funcionalidades conversacionales deberán evaluarse
mediante un patrón especí co orientado a validar la continuidad de la
interacción

Como mínimo deberán veri carse

-   comprensión de la intención;
-   mantenimiento del contexto;
-   continuidad de la conversación;
-   manejo de aclaraciones;
-   cierre adecuado de la interacción. El patrón deberá adaptarse al
    objetivo funcional de cada conversación sin modi car su estructura
    general

## 664. Patrón para Recuperación Documenta

Las funcionalidades que dependan de recuperación documental deberán
utilizar un patrón orientado a validar la calidad del proceso de
recuperación

Como mínimo deberán evaluarse

-   pertinencia de los documentos recuperados;
-   su ciencia del contexto;
-   ausencia de documentos irrelevantes;
-   trazabilidad de las fuentes;
-   utilización efectiva del contexto durante la respuesta. La
    evaluación deberá distinguir claramente entre errores de
    recuperación y errores de generación

## 665. Patrón para Herramientas Externa

Toda integración con herramientas externas deberá evaluarse utilizando
un patrón especí co

Como mínimo deberán veri carse

-   selección de la herramienta;
-   parámetros enviados; fi .

.

fi fi

:

:

:

s

.

.

fi fi s

fi .

l

-   tratamiento de errores;
-   utilización de la respuesta obtenida;
-   comportamiento ante indisponibilidad. El patrón deberá permitir
    evaluar cada herramienta de forma independiente

## 666. Patrón para Memoria Conversaciona

Las funcionalidades de memoria deberán evaluarse utilizando un patrón
orientado a validar la persistencia y utilización del contexto

Como mínimo deberán contemplarse

-   creación del contexto;
-   actualización;
-   recuperación;
-   eliminación;
-   aislamiento entre conversaciones;
-   expiración cuando corresponda. Las pruebas deberán demostrar que la
    memoria mantiene la coherencia funcional durante toda la
    conversación

## 667. Patrón para Clasi cació

Las funcionalidades cuyo objetivo sea clasi car información deberán
utilizar un patrón especí co de evaluación

Como mínimo deberán veri carse

-   clasi cación correcta;
-   tratamiento de ambigüedades;
-   manejo de categorías desconocidas;
-   estabilidad de la clasi cación;
-   consistencia entre ejecuciones. La evaluación deberá utilizar
    conjuntos de datos previamente validados

## 668. Patrón para Extracción de Informació

Las funcionalidades encargadas de extraer información estructurada
deberán evaluarse mediante un patrón orientado a veri car la precisión
de los datos obtenidos fi fi

.

fi

.

fi fi

:

:

.

fi fi n

.

.

.

l

n

Como mínimo deberán comprobarse

-   identi cación de entidades;
-   exactitud de los valores extraídos;
-   tratamiento de información incompleta;
-   manejo de formatos variados;
-   consistencia de la estructura resultante. La evaluación deberá
    registrar tanto los aciertos como las omisiones detectadas

## 669. Patrón para Generación de Contenid

Las funcionalidades destinadas a generar contenido deberán evaluarse
utilizando un patrón que permita veri car la calidad del resultado
conforme a los requisitos de nidos

Como mínimo deberán contemplarse

-   cumplimiento de instrucciones;
-   estructura del contenido;
-   consistencia del estilo requerido;
-   completitud;
-   restricciones funcionales. La evaluación deberá realizarse
    utilizando criterios previamente documentados

## 670. Selección del Patrón de Evaluació

Antes de diseñar una nueva suite de evaluación deberá identi carse el
patrón o conjunto de patrones aplicables a la funcionalidad
correspondiente

Cuando una funcionalidad combine múltiples capacidades, deberán
aplicarse todos los patrones pertinentes

La creación de nuevos patrones únicamente procederá cuando ninguno de
los existentes resulte adecuado para representar el comportamiento
evaluado

## 671. Catálogo de Activos de Testin

La Arquitectura de Testing deberá mantener un catálogo de los activos
utilizados durante el proceso de evaluación

El catálogo tendrá como propósito identi car, clasi car y administrar
los elementos que conforman el ecosistema de evaluación fi .

fi

.

:

:

.

fi fi .

.

fi fi g

.

.

.

n

o

Todo activo deberá contar con una identi cación única, un responsable de
nido, un ciclo de vida documentado y reglas para su mantenimiento

## 672. Activo: Suite de Evaluació

La Suite de Evaluación constituye el conjunto organizado de casos de
evaluación diseñados para validar una funcionalidad, componente o
capacidad especí ca

Toda suite deberá de nir, como mínimo

-   identi cación;
-   objetivo;
-   alcance;
-   criterios de inclusión;
-   criterios de ejecución;
-   dependencias;
-   responsable de mantenimiento. Las suites deberán mantenerse bajo
    control de versiones y formar parte del proceso o cial de evaluación

## 673. Activo: Caso de Evaluació

El Caso de Evaluación representa la unidad mínima de validación dentro
de una suite

Cada caso deberá documentar, como mínimo

-   identi cador;
-   objetivo;
-   entradas;
-   procedimiento;
-   resultado esperado;
-   criterios de aceptación;
-   evidencia requerida. Los casos deberán ser independientes siempre
    que la naturaleza de la funcionalidad lo permita

## 674. Activo: Dataset de Evaluació

El Dataset de Evaluación es el conjunto de datos utilizado para ejecutar
uno o más casos de evaluación fi fi

.

.

fi

:

fi :

.

fi .

n

n

n

fi fi .

.

Todo dataset deberá indicar

-   propósito;
-   origen;
-   versión;
-   alcance;
-   restricciones de uso;
-   fecha de actualización. Los datasets deberán conservar su integridad
    durante todo el proceso de evaluación

## 675. Activo: Patrón de Evaluació

El Patrón de Evaluación de ne una estructura reutilizable para diseñar
casos y suites de evaluación correspondientes a un tipo especí co de
funcionalidad

Todo patrón deberá especi car

-   objetivo;
-   ámbito de aplicación;
-   estructura obligatoria;
-   criterios mínimos de cobertura;
-   relaciones con otros patrones. Los patrones deberán revisarse
    periódicamente para asegurar su vigencia

## 676. Activo: Métrica de Evaluació

La Métrica de Evaluación representa una medida objetiva utilizada para
determinar el nivel de cumplimiento de un criterio previamente
establecido

Toda métrica deberá de nir

-   nombre;
-   objetivo;
-   método de cálculo;
-   unidad de medida;
-   interpretación;
-   umbral aplicable. No deberán emplearse métricas cuya interpretación
    resulte ambigua o no pueda reproducirse

fi fi fi :

:

:

fi .

.

n

n

.

.

.

## 677. Activo: Evidencia de Evaluació

La Evidencia de Evaluación corresponde al conjunto de registros que
permiten demostrar la ejecución y los resultados de una evaluación

La evidencia podrá incluir, entre otros

-   registros de ejecución;
-   resultados obtenidos;
-   métricas calculadas;
-   capturas de pantalla;
-   archivos generados;
-   reportes automatizados. Toda evidencia deberá conservarse conforme a
    la política de nida por la organización

## 678. Activo: Umbral de Aceptació

El Umbral de Aceptación establece el valor mínimo requerido para
considerar satisfactoria una evaluación

Todo umbral deberá indicar

-   métrica asociada;
-   valor requerido;
-   justi cación;
-   alcance;
-   fecha de aprobación;
-   responsable de autorización. Los umbrales deberán revisarse cuando
    cambien los objetivos del sistema o los riesgos identi cados

## 679. Activo: Reporte de Evaluació

El Reporte de Evaluación consolida los resultados obtenidos durante una
ejecución determinada

Como mínimo deberá incluir

-   identi cación de la ejecución;
-   versión evaluada;
-   suites ejecutadas; fi fi fi

.

.

:

:

:

.

fi n

n

n

.

.

-   resultados;
-   métricas;
-   incidencias detectadas;
-   conclusión. El reporte constituirá la evidencia formal para la toma
    de decisiones relacionadas con la liberación del sistema

## 680. Gestión del Ciclo de Vida de los Activo

Todos los activos de nidos por la Arquitectura de Testing deberán
administrarse durante su ciclo de vida completo

Como mínimo deberán contemplarse las siguientes etapas

-   creación;
-   revisión;
-   aprobación;
-   utilización;
-   mantenimiento;
-   versionado;
-   retiro. La gestión del ciclo de vida deberá garantizar la
    trazabilidad y consistencia de los activos utilizados durante el
    proceso de evaluación

## 681. Glosario Especí co de la Arquitectura

de Testin El presente documento establece un conjunto de términos
técnicos cuyo signi cado será el de nido en esta sección para todos los
procesos relacionados con la Arquitectura de Testing

Cuando un término también exista en el Glosario Corporativo, prevalecerá
la de nición especí ca únicamente para el contexto de este documento

## 682. De niciones Fundamentale

Para efectos del presente estándar se adoptan las siguientes de niciones

Arquitectura de Testing fi

fi

fi .

g

fi .

.

fi .

:

fi s

:

fi fi .

s

Conjunto de principios, procesos, activos y mecanismos destinados a
plani car, ejecutar, gobernar y mejorar la evaluación de sistemas
basados en Inteligencia Arti cial

Evaluación

Proceso sistemático mediante el cual se veri ca el cumplimiento de
criterios previamente establecidos

Evidencia

Información objetiva que demuestra la ejecución y el resultado de una
evaluación

Cobertura

Grado en que los requisitos, funcionalidades o riesgos se encuentran
representados por los activos de evaluación

## 683. De niciones de Activo

Para efectos del presente documento se entenderá por

Suite de Evaluación

Conjunto organizado de casos de evaluación relacionados entre sí

Caso de Evaluación

Unidad mínima de validación utilizada para comprobar un comportamiento
especí co

Dataset de Evaluación

Conjunto de datos empleado para ejecutar uno o más casos de evaluación

Patrón de Evaluación

Estructura reutilizable utilizada para diseñar evaluaciones homogéneas

## 684. De niciones de Resultado

Se adoptan las siguientes de niciones

Resultado Esperado .

fi fi .

fi :

fi :

s

s

.

.

.

fi fi .

.

fi .

Comportamiento previamente de nido como correcto

Resultado Observado

Comportamiento obtenido durante la ejecución de una evaluación

Hallazgo

Diferencia identi cada entre el resultado esperado y el observado que
requiere análisis

Regresión

Reaparición de un comportamiento incorrecto previamente corregido o
degradación de una funcionalidad existente

## 685. De niciones de Calida

Para efectos de la Arquitectura de Testing

Métrica

Medida objetiva utilizada para evaluar un criterio

Umbral

Valor mínimo o máximo requerido para considerar aceptable un resultado

Criterio de Aceptación

Condición que debe cumplirse para aprobar una evaluación

Línea Base (Baseline)

Conjunto de resultados aprobados que sirven como referencia para
comparaciones futuras

## 686. De niciones del Proces

Se entenderá por

Pipeline de Evaluación

Secuencia automatizada de actividades destinadas a ejecutar las
evaluaciones de nidas fi fi :

fi .

fi :

.

.

d

o

.

.

.

fi .

.

.

Automatización

Ejecución controlada de procesos de evaluación con mínima intervención
manual

Trazabilidad

Capacidad para relacionar requisitos, activos de evaluación, resultados
y evidencias

## 687. De niciones de Gobiern

Dentro del presente estándar

Activo de Evaluación

Elemento administrado por la Arquitectura de Testing que participa en el
proceso de evaluación

Control de Cambios

Proceso mediante el cual se autorizan y documentan modi caciones sobre
los activos

Versión

Identi cación única asignada a un activo para registrar su evolución

## 688. Interpretación de Término

Los términos de nidos en este documento deberán interpretarse de manera
consistente durante todas las actividades relacionadas con la evaluación

Cuando exista duda respecto de la interpretación de un concepto,
prevalecerá la de nición establecida por este estándar sobre cualquier
uso informal dentro del proyecto

## 689. Terminología Complementari

Los términos no de nidos expresamente en este documento deberán
interpretarse conforme a

-   el Glosario Corporativo de Ingeniería;
-   los estándares internos de la organización;
-   la documentación o cial aplicable al proyecto. fi fi fi fi fi :

.

fi o

s

.

a

.

.

fi .

.

:

.

La incorporación de nuevos términos deberá seguir el proceso de control
documental correspondiente

## 690. Mantenimiento del Glosari

Las de niciones contenidas en esta sección deberán revisarse cuando

-   se incorporen nuevos tipos de activos;
-   cambie la arquitectura de evaluación;
-   evolucionen los procesos de nidos en este estándar;
-   se detecten ambigüedades durante su aplicación. Toda modi cación
    deberá gestionarse conforme al proceso o cial de control de
    versiones

## 691. Relación con el Marco Normativo de

Ingenierí La presente Arquitectura de Testing forma parte del Marco
Normativo de Ingeniería de Software de la organización

Sus disposiciones deberán aplicarse conjuntamente con los demás
documentos técnicos que conforman dicho marco, respetando el alcance y
responsabilidad de nidos para cada uno

La aplicación de este estándar no sustituye las obligaciones
establecidas en otros documentos del handbook, sino que las complementa
dentro del ámbito especí co del aseguramiento de la calidad

## 692. Relación con Otros Documentos del

Handboo La Arquitectura de Testing mantiene relación directa con, al
menos, los siguientes documentos del handbook

-   Arquitectura Empresarial.
-   Arquitectura de Software.
-   Arquitectura Backend.
-   Arquitectura Frontend.
-   Arquitectura de APIs.
-   Arquitectura de Datos. fi .

fi :

.

.

a

k

fi

fi fi o

fi :

.

.

-   Arquitectura de Inteligencia Arti cial.
-   Arquitectura de Seguridad.
-   Arquitectura de Observabilidad.
-   Arquitectura DevSecOps.
-   Gestión de Con guración.
-   Gestión de Cambios.
-   Gestión de Riesgos. Cada documento conserva su responsabilidad
    especí ca y no deberá duplicar el contenido de nido en el presente
    estándar

## 693. Cumplimiento del Estánda

Toda funcionalidad desarrollada bajo el alcance del presente handbook
deberá cumplir las disposiciones establecidas en esta Arquitectura de
Testing

Las desviaciones únicamente podrán autorizarse mediante el proceso
formal de gestión de excepciones de nido por la organización

La ausencia de cumplimiento deberá considerarse un incumplimiento del
estándar de ingeniería correspondiente

## 694. Gestión de Versiones del Document

El presente documento deberá mantenerse bajo control de versiones
durante todo su ciclo de vida

Cada actualización deberá registrar, como mínimo

-   versión;
-   fecha de emisión;
-   responsable;
-   descripción de los cambios;
-   motivo de la actualización. Las modi caciones deberán preservar la
    coherencia con el resto del Marco Normativo de Ingeniería

## 695. Revisión Periódic

fi .

fi .

fi fi .

.

fi

.

a

:

fi .

r

o

La Arquitectura de Testing deberá revisarse periódicamente para veri car
su vigencia, consistencia y alineación con la evolución tecnológica de
la organización

La revisión podrá originarse por

-   incorporación de nuevas tecnologías;
-   cambios metodológicos;
-   modi caciones en la Arquitectura de Inteligencia Arti cial;
-   resultados de auditorías;
-   lecciones aprendidas;
-   necesidades organizacionales. Toda revisión deberá seguir el
    procedimiento o cial de control documental

## 696. Vigenci

El presente documento entrará en vigor a partir de la fecha de su
aprobación o cial

Su aplicación será obligatoria para todos los proyectos que se
encuentren bajo el alcance de nido por el Marco Normativo de Ingeniería

Las versiones anteriores quedarán derogadas en la medida en que sean
sustituidas por la versión vigente

## 697. Interpretación del Estánda

Las dudas relacionadas con la interpretación del presente documento
deberán resolverse considerando, en el siguiente orden de prioridad

## 1. El contenido de este estándar.

## 2. Los principios del Marco Normativo de Ingeniería.

## 3. Las políticas corporativas aplicables.

## 4. Los criterios técnicos aprobados por la organización.

Las interpretaciones emitidas deberán documentarse cuando puedan afectar
la aplicación futura del estándar

## 698. Mejora Continua del Estánda

La Arquitectura de Testing constituye un documento evolutivo fi .

.

a

:

.

fi :

fi

.

r

fi .

r

.

fi .

fi

Las oportunidades de mejora identi cadas durante su aplicación deberán
registrarse y evaluarse mediante el proceso o cial de mejora continua

Las actualizaciones deberán preservar la estabilidad del estándar,
evitando modi caciones incompatibles salvo que exista una justi cación
técnica documentada

## 699. Aprobació

La aprobación del presente documento corresponde a la autoridad técnica
designada por la organización conforme a su modelo de gobierno

La aprobación implica que el contenido ha sido revisado y se considera
alineado con los principios del Marco Normativo de Ingeniería

Toda modi cación posterior requerirá un nuevo proceso de revisión y
aprobación conforme a las políticas vigentes

## 700. Disposición Fina

La Arquitectura de Testing establece el marco técnico para plani car,
diseñar, ejecutar, automatizar, gobernar y mejorar el proceso de
evaluación de sistemas basados en Inteligencia Arti cial dentro de la
organización

Su nalidad es garantizar que toda funcionalidad incorporada al
ecosistema tecnológico sea evaluada mediante procesos objetivos,
reproducibles, trazables y sustentados en evidencia veri cable

Las disposiciones contenidas en este documento constituyen el estándar o
cial para la Arquitectura de Testing y deberán aplicarse de manera
consistente en todos los proyectos que formen parte del Marco Normativo
de Ingeniería fi fi fi .

fi .

fi n

.

fi fi l

.

.

.

.

fi .

fi fi
