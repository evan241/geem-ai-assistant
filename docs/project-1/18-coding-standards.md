DOCUMENTO 1 Coding Standards (GEEM Engineering Handbook Versión

Introducció Propósit Este documento establece los estándares o ciales
para la construcción de software dentro de la organización

Su objetivo es que cualquier integrante del equipo, humano o agente de
Inteligencia Arti cial, produzca código consistente, mantenible y
alineado con la arquitectura de nida para el proyecto

Las reglas aquí descritas deberán aplicarse independientemente del
lenguaje de programación utilizado, salvo que un estándar tecnológico
especí co establezca una adaptación

Mani esto de Ingenierí Engineering Manifest

## 1. El software existe para resolver problemas del negocio

La tecnología es un medio, no un n

Toda decisión técnica deberá contribuir al cumplimiento de un objetivo
de negocio claramente identi cable fi 2

fi .

.

o

n

fi o

.

8

fi a

fi )

fi .

fi .

.

## 2. La simplicidad es una decisión de ingeniería

Las soluciones deberán ser tan simples como sea razonablemente posible,
pero no más simples de lo necesario

La complejidad deberá introducirse únicamente cuando aporte un bene cio
demostrable

## 3. La calidad se construye desde el inicio

La calidad no depende únicamente de pruebas, revisiones o auditorías

Cada decisión tomada durante el diseño y la implementación contribuye al
resultado nal

## 4. Todo código será mantenido por alguien en el futuro

Las decisiones deberán facilitar la comprensión, evolución y
mantenimiento del software

La legibilidad tiene prioridad sobre la creatividad

## 5. Los contratos representan compromisos

Las interfaces públicas deberán diseñarse y evolucionarse considerando
el impacto sobre quienes dependen de ellas

## 6. La evidencia tiene prioridad sobre la opinión

Las decisiones técnicas deberán sustentarse en evidencia, mediciones,
análisis o experiencia veri cable

Las preferencias personales no constituyen criterios de ingeniería

## 7. La seguridad es responsabilidad de todos

La protección del software, la información y los usuarios forma parte
del trabajo diario de ingeniería fi .

.

.

.

.

.

.

.

.

.

fi .

.

fi .

.

.

.

No constituye una actividad aislada ni exclusiva de un equipo
especializado

## 8. Automatizamos siempre que sea posible

Las tareas repetitivas deberán automatizarse para reducir errores,
aumentar la consistencia y permitir que las personas concentren su
esfuerzo en decisiones que requieren criterio profesional

## 9. El juicio profesional no puede automatizarse

Las herramientas pueden asistir, sugerir o acelerar el trabajo

La responsabilidad sobre las decisiones de ingeniería permanece en las
personas

## 10. La mejora continua forma parte del desarrollo

Los sistemas evolucionan

Las prácticas de ingeniería también

Toda experiencia obtenida durante el desarrollo constituye una
oportunidad para fortalecer los estándares de la organización

## 11. Construimos para evolucionar, no solo para entregar

Cada solución deberá considerar no únicamente el problema actual, sino
también la capacidad del sistema para adaptarse a necesidades futuras
con un costo razonable

## 12. La ingeniería es una responsabilidad compartida

La calidad del software no depende de una sola persona ni de un único
rol

Cada integrante del equipo contribuye al diseño, construcción, revisión,
operación y evolución del sistema .

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

## 0. Cómo usar este Engineering Handboo

### 0.1 Propósito del Engineering Handboo

Objetiv Establecer un marco común de decisiones de ingeniería que
permita desarrollar software de manera consistente, segura, mantenible y
alineada con los estándares de la organización

Filosofí El propósito de este Engineering Handbook no es enseñar un
lenguaje de programación, un framework o una herramienta especí ca

Su propósito es capturar los principios de ingeniería que permanecen
vigentes independientemente de la tecnología utilizada

Las tecnologías evolucionan

Los principios de ingeniería permanecen

Por esta razón, las reglas contenidas en este documento describen qué
decisiones deben tomarse y qué criterios deben utilizarse, evitando
depender de plataformas, lenguajes o herramientas particulares

¿Qué representa este documento Este Engineering Handbook constituye la
referencia o cial para el desarrollo de software dentro de la
organización

De ne los criterios mínimos de calidad que deberán aplicarse durante el
diseño, implementación, revisión, evolución y mantenimiento del software

Su cumplimiento busca asegurar que todos los equipos construyan
soluciones con un nivel homogéneo de calidad, independientemente de la
experiencia individual de sus integrantes fi a

o

.

.

.

fi .

.

.

.

?

fi k

k

.

.

### 0.2 Alcanc

Este handbook aplica a

-   Desarrollo de software.
-   APIs.
-   Servicios.
-   Aplicaciones web.
-   Aplicaciones móviles.
-   Sistemas distribuidos.
-   Automatizaciones.
-   Integraciones.
-   Componentes reutilizables.
-   Librerías internas. Siempre que un proyecto desarrolle software bajo
    responsabilidad de la organización, este documento será aplicable

Fuera del alcanc Este documento no de ne

-   Arquitecturas especí cas.
-   Frameworks.
-   Lenguajes.
-   Herramientas.
-   Infraestructura.
-   Con guración de plataformas.
-   Procedimientos operativos. Estos temas deberán documentarse en los
    estándares técnicos correspondientes

### 0.3 Audienci

Este handbook está dirigido a todas las personas que participan en el
ciclo de vida del software

Incluye, entre otros

-   Desarrolladores.
-   Arquitectos.
-   Líderes técnicos.
-   Revisores de código.
-   Ingenieros de calidad. fi

:

fi

e

fi

:

.

:

a

e

.

.

-   Ingenieros DevOps.
-   Equipos de plataforma.
-   Ingenieros de IA.
-   Personal técnico responsable del mantenimiento y evolución del
    software. Cada rol utilizará el documento desde una perspectiva
    distinta, pero todos compartirán los mismos criterios de ingeniería

### 0.4 Cómo interpretar las regla

Todas las reglas incluidas en este handbook pertenecen a uno de los
siguientes niveles

🔴 Regla Obligatori Representa un requisito mínimo de ingeniería

Su incumplimiento deberá justi carse formalmente o impedir la aprobación
del cambio cuando así lo establezca el proceso de revisión

🟡 Heurístic Describe una práctica que normalmente conduce a mejores
resultados

Podrá existir una solución diferente siempre que esté técnicamente justi
cada

🔵 Recomendació Representa una práctica deseable que mejora la calidad
del software

Su incumplimiento no implica necesariamente un defecto

### 0.5 Cómo utilizar este document

Este handbook no está diseñado para leerse de principio a n como un
libro

a

n

.

fi a

.

.

.

fi s

.

o

.

fi

.

.

.

Cada capítulo responde a un conjunto especí co de decisiones de
ingeniería

Durante el trabajo diario, el desarrollador deberá consultar el capítulo
correspondiente a la decisión que está tomando

Por ejemplo

Capítul Decisión o ¿Cómo nombro esto? NAM ¿Debo crear una nueva clase?
CLS ¿Dónde debe vivir esta lógica? DEP ¿Cómo manejo este error? ERR
¿Debo registrar un log? LOG ¿Cómo protejo esta SEC información?
¿Necesito optimizar este código? PER ¿Cómo diseño este contrato? API
¿Cómo pruebo este cambio? TST ¿Debo refactorizar? MNT ¿Cómo reviso este
Pull Request? REV

El objetivo es que cualquier decisión frecuente pueda resolverse
consultando una única sección del documento

### 0.6 Relación con otros documento

El Engineering Handbook forma parte del marco documental de ingeniería
de la organización

No sustituye otros documentos especializados

Debe utilizarse conjuntamente con

-   Manual de Arquitectura.
-   Manual de Desarrollo Backend.
-   Manual de Desarrollo Frontend.
-   Manual de Testing.
-   Manual de DevOps.
-   Manual de Seguridad. :

.

.

:

fi .

s

.

.

-   Manual de IA.
-   Estándares tecnológicos especí cos. Cada documento aborda un nivel
    distinto de detalle y todos son complementarios

### 0.7 Excepcione

Las reglas obligatorias únicamente podrán omitirse cuando exista una
justi cación técnica documentada y la aprobación de la autoridad de nida
por la organización

Toda excepción deberá

-   describir el motivo;
-   evaluar los riesgos;
-   establecer medidas de mitigación cuando correspondan;
-   indicar si la excepción es temporal o permanente. Las excepciones no
    constituyen nuevos estándares ni modi can las reglas generales del
    handbook

### 0.8 Evolución del Engineering Handboo

El Engineering Handbook es un documento vivo

Las reglas podrán modi carse cuando existan cambios signi cativos en las
prácticas de ingeniería, en la estrategia tecnológica de la organización
o cuando la experiencia acumulada demuestre la necesidad de mejorar un
estándar existente

Toda modi cación deberá seguir el proceso formal de revisión, aprobación
y control documental de nido por la organización

El objetivo es mantener un conjunto de reglas estable, pero en evolución
continua fi .

fi

:

fi .

fi s

fi .

.

fi fi .

fi .

.

k

## Capítulo 1. Organización del Códig

Regla 1. ¿Cómo debo organizar un proyecto Objetiv De nir una estructura
que permita localizar, comprender y mantener el código de manera e
ciente

Regl Todo proyecto deberá seguir una estructura uniforme y consistente
con la arquitectura de nida para la solución

La organización del código deberá facilitar la identi cación de
responsabilidades, reducir la complejidad y favorecer la evolución del
sistema

No deberán coexistir múltiples criterios de organización dentro del
mismo proyecto sin una justi cación arquitectónica

Cuándo aplic ✅ Al crear un nuevo proyecto

✅ Al incorporar un nuevo módulo

✅ Durante una refactorización importante

Cuándo no aplic ❌ No utilizar esta regla para decidir la estructura
interna de una clase o un método fi fi fi a

.

o

.

a

a

.

.

.

.

.

fi o

.

fi ?

Checklis Antes de crear un nuevo directorio o módulo veri ca

-   ¿Existe un estándar para este tipo de componente?
-   ¿La estructura facilita encontrar el código?
-   ¿Respeta la arquitectura del proyecto?
-   ¿Evita duplicar responsabilidades?
-   ¿Será comprensible para un desarrollador nuevo?

Indicadores de alert ⚠ Existen varios directorios con el mismo propósito

⚠ Es difícil encontrar dónde implementar una funcionalidad

⚠ Cada desarrollador organiza los archivos de forma distinta

⚠ Los nombres de las carpetas no re ejan responsabilidades claras

Automatizació Parcial

Las herramientas pueden validar parte de la estructura, pero la
organización arquitectónica requiere revisión técnica

Relación con otros estándare - Arquitectura de Software. - Arquitectura
Backend. - Arquitectura Frontend. - Code Review.

Regla 2. ¿Cómo debo organizar los módulos Objetiv .

o

t

n

.

a

fl

s

fi

.

:

.

.

.

?

Mantener una separación clara entre las distintas capacidades del
sistema

Regl Los módulos deberán organizarse conforme a la arquitectura de nida
para el proyecto, procurando que cada uno represente una responsabilidad
claramente identi cable

Siempre que resulte adecuado, se recomienda agrupar el código por
dominio funcional o capacidad de negocio, favoreciendo una alta cohesión
y un bajo acoplamiento

El criterio de organización elegido deberá mantenerse de forma
consistente en todo el proyecto

Cuándo aplic ✅ Al crear un nuevo módulo

✅ Al dividir un sistema existente

✅ Durante procesos de modularización

Cuándo no aplic ❌ No utilizar esta regla para decidir la ubicación de
funciones dentro de una clase

Checklis Antes de crear un módulo veri ca

-   ¿Representa una responsabilidad claramente de nida?
-   ¿Tiene límites bien establecidos?
-   ¿Evita depender innecesariamente de otros módulos?
-   ¿Su nombre describe la capacidad que ofrece?
-   ¿Puede evolucionar sin afectar componentes no relacionados?

Indicadores de alert a

t

a

a

.

fi a

:

.

.

fi

fi .

fi .

.

.

.

⚠ Módulos con responsabilidades mezcladas

⚠ Dependencias circulares

⚠ Cambios pequeños obligan a modi car varios módulos

⚠ El nombre del módulo no re eja su propósito

Automatizació Baja

Puede apoyarse con herramientas de análisis de dependencias, pero
requiere revisión de arquitectura

Relación con otros estándare - Arquitectura de Software. - Gestión de
Dependencias. - Arquitectura Empresarial

NAM-00 ¿Cómo debo nombrar una clase Objetiv Garantizar que el nombre de
una clase describa claramente su responsabilidad y facilite su identi
cación dentro del sistema

Regl Toda clase deberá recibir un nombre que represente el concepto o
responsabilidad que modela dentro del dominio de la aplicación .

fi a

.

o

1

n

.

.

fl .

.

fi .

s

.

.

?

El nombre deberá comunicar qué es o qué hace la clase, evitando
referencias a detalles de implementación, abreviaturas ambiguas o
nombres genéricos

Siempre que sea posible, deberá emplearse el vocabulario del dominio del
negocio

Buenas práctica ✔ Utilizar nombres descriptivos

✔ Emplear sustantivos o conceptos del dominio

✔ Mantener consistencia con el resto del proyecto

✔ Evitar nombres excesivamente largos

Evita ✘ Manage

✘ Helpe

✘ Uti

✘ Commo

✘ Mis

✘ Dat

✘ Proces

✘ Class

✘ Test

Checklis Antes de nombrar una clase veri ca

-   ¿El nombre describe su responsabilidad?
-   ¿Un desarrollador nuevo entendería su propósito?
-   ¿Representa un concepto del negocio o de la arquitectura? l

a

c

2

1

r

r

s

r

n

t

s

fi .

:

.

.

.

.

.

-   ¿Evita abreviaturas innecesarias?
-   ¿Es consistente con el resto del proyecto?

Indicadores de alert ⚠ El nombre necesita explicarse verbalmente

⚠ El nombre contiene palabras como "Helper" o "Manager" sin contexto

⚠ La clase termina realizando tareas distintas a las sugeridas por su
nombre

Automatizació Parcial

Las herramientas pueden detectar ciertos patrones de nombres, pero la
validación semántica requiere revisión técnica

Relación con otros estándare - CLS - REV - Arquitectura de Software

NAM-00 ¿Cómo debo nombrar un método Objetiv Garantizar que el nombre del
método describa claramente la acción que realiza

Regl

.

a

o

2

n

.

a

s

.

?

.

.

.

Todo método deberá nombrarse utilizando un verbo o una frase verbal que
represente la operación ejecutada

El nombre deberá permitir comprender el comportamiento esperado sin
necesidad de revisar su implementación

Cuando un método realice más de una acción importante, deberá evaluarse
su división

Buenas práctica ✔ getCustomer(

✔ calculateDiscount(

✔ validateInvoice(

✔ sendNoti cation(

✔ generateReport(

Evita ✘ process(

✘ execute(

✘ run(

✘ handle(

✘ doIt(

✘ action(

Estos nombres solo son aceptables cuando el contexto arquitectónico les
da un signi cado inequívoco (por ejemplo, un método execute() en un
patrón Command)

Checklis Antes de nombrar un método veri ca

-   ¿Empieza con un verbo? )

)

r

)

)

)

)

fi t

.

)

)

)

.

)

)

s

fi :

.

fi .

-   ¿Describe exactamente lo que hace?
-   ¿No promete más de lo que realiza?
-   ¿No oculta varias responsabilidades?
-   ¿Es consistente con el resto del proyecto?

Indicadores de alert ⚠ El nombre requiere comentarios para entenderse

⚠ Contiene verbos demasiado genéricos

⚠ El método realiza acciones que no aparecen re ejadas en su nombre

Automatizació Media

Puede validarse parcialmente mediante herramientas de análisis estático
y convenciones del lenguaje

Relación con otros estándare - FUN - CLS - REV

NAM-00 ¿Cómo debo nombrar una variable Objetiv Facilitar la comprensión
inmediata de los datos utilizados durante la ejecución del programa

.

.

o

3

n

a

.

s

fl .

.

?

.

Regl Toda variable deberá recibir un nombre que represente claramente la
información que almacena

El nombre deberá expresar el signi cado del dato y no únicamente su tipo
o forma de implementación

Se recomienda utilizar nombres su cientemente descriptivos para evitar
interpretaciones ambiguas, manteniendo un equilibrio que preserve la
legibilidad

Buenas práctica ✔ totalAmoun

✔ customerEmai

✔ activeUser

✔ expirationDat

✔ paymentStatu

Evita ✘ dat

✘ valu

✘ tem

✘ au

✘ va

✘

✘ ob

✘ inf

Checklis x

r

x

j

o

a

p

e

a

r

s

t

t

.

e

s

l

s

fi fi .

.

Antes de declarar una variable veri ca

-   ¿Describe el dato que contiene?
-   ¿Evita abreviaturas ambiguas?
-   ¿No depende exclusivamente del contexto inmediato?
-   ¿Resulta comprensible fuera del bloque donde se declara?
-   ¿Es consistente con el vocabulario del proyecto?

Indicadores de alert ⚠ Variables llamadas data, value, temp o obj que
sobreviven más allá de unas pocas líneas

⚠ Variables con un solo carácter fuera de contextos muy acotados (por
ejemplo, índices de un bucle)

⚠ Variables cuyo nombre re eja el tipo (string1, list2) en lugar de su
signi cado

Automatizació Parcial

Las herramientas pueden detectar patrones problemáticos, pero la calidad
semántica del nombre requiere revisión humana

Relación con otros estándare - REV - CLS - FU

CLS-00 ¿Cuándo debo crear una clase Objetiv N

.

.

.

o

1

n

.

fl

a

fi :

s

?

fi .

De nir cuándo una nueva clase aporta valor al diseño del sistema y
cuándo únicamente incrementa la complejidad

Regl Una clase deberá crearse cuando represente una responsabilidad
claramente diferenciada dentro del dominio o de la arquitectura del
sistema

No deberá crearse una clase únicamente para encapsular una pequeña
cantidad de código, seguir una moda arquitectónica o cumplir una
convención sin un bene cio identi cable

La incorporación de una nueva clase deberá simpli car la comprensión,
reutilización o evolución del software

Crear una clase cuand ✅ Modela un concepto del negocio

✅ Encapsula comportamiento con estado relacionado

✅ Tiene una responsabilidad claramente de nida

✅ Será reutilizada por otros componentes

✅ Reduce el acoplamiento o mejora la organización del código

Evitar crear una clase cuand ❌ Solo contiene una función sin estado

❌ Existe únicamente para "tener más orden"

❌ Se utiliza una sola vez y no mejora la claridad

❌ Su responsabilidad puede incorporarse coherentemente en un componente
existente fi a

.

.

o

.

.

.

.

fi o

.

.

.

fi .

fi .

fi .

.

Checklis Antes de crear una clase veri ca

-   ¿Representa una responsabilidad propia?
-   ¿Mejora la organización del sistema?
-   ¿Reduce la complejidad?
-   ¿Facilita futuras modi caciones?
-   ¿Evita duplicación?

Indicadores de alert ⚠ Clases creadas únicamente porque "cada archivo
debe tener una clase"

⚠ Clases con nombres como SomethingManager o SomethingHelper

⚠ Muchas clases con muy poco comportamiento

Automatizació No

Requiere criterio de diseño

Justi cación de ingenierí Cada clase añade una unidad más al sistema:
debe comprenderse, mantenerse, probarse y evolucionar. Crear clases sin
una necesidad real incrementa el costo de mantenimiento y di culta la
navegación del código

Relación con otros estándare CL

FU

RE .

S

V

N

fi t

fi n

.

.

fi a

:

a

s

.

.

.

fi

Arquitectura de Softwar

CLS-00 ¿Cómo sé si una clase tiene demasiadas responsabilidades Objetiv
Identi car oportunamente clases cuya complejidad compromete la
mantenibilidad del sistema

Regl Una clase deberá concentrarse en una responsabilidad principal

Cuando un mismo componente deba modi carse por razones distintas o
participe en procesos independientes, deberá evaluarse su división

El criterio principal no será el número de líneas, sino la diversidad de
responsabilidades que concentra

Señales de una posible clase sobrecargad ⚠ Tiene varios motivos de
cambio

⚠ Contiene lógica de negocio, acceso a datos y validaciones

⚠ Es utilizada por módulos sin relación entre sí

⚠ Resulta difícil describir su responsabilidad en una sola frase

⚠ Requiere múltiples regiones o comentarios para separar comportamientos
fi a

.

o

2

e

.

?

fi .

.

.

.

.

a

.

.

Checklis Antes de aceptar una clase veri ca

-   ¿Puedo describir su propósito en una oración?
-   ¿Todos sus métodos colaboran para el mismo objetivo?
-   ¿Una modi cación afecta solo esa responsabilidad?
-   ¿No concentra lógica de distintos dominios?

Indicadores de alert ⚠ Clases de más de mil líneas

⚠ Más de veinte o treinta métodos públicos (el número exacto depende del
contexto, pero un crecimiento sostenido merece revisión)

⚠ Dependencias hacia numerosos servicios o módulos

⚠ Cambios frecuentes por motivos no relacionados

Automatizació Parcial

Las herramientas pueden medir tamaño y dependencias, pero no la calidad
de la responsabilidad

Justi cación de ingenierí Una clase con responsabilidades mezcladas
suele ser más difícil de probar, comprender y modi car. Detectar este
problema de forma temprana reduce la deuda técnica

Relación con otros estándare FU

DE N

P

fi .

fi fi t

n

.

fi a

:

.

a

s

.

.

.

.

RE

Testin

CLS-00 ¿Cuándo debo dividir una clase Objetiv Establecer criterios para
separar responsabilidades sin fragmentar innecesariamente el diseño

Regl Una clase deberá dividirse cuando la separación permita reducir la
complejidad sin afectar la comprensión del sistema

La división deberá responder a límites funcionales claros y no
únicamente al tamaño del archivo

Dividir una clase cuand ✅ Existen responsabilidades independientes

✅ Diferentes equipos modi can partes distintas

✅ Algunas funcionalidades evolucionan a ritmos diferentes

✅ Parte del comportamiento puede reutilizarse

Evitar dividir una clase cuand ❌ Solo se busca reducir el número de
líneas

❌ Las nuevas clases tendrían responsabilidades arti ciales V

g

a

o

3

.

fi o

.

.

.

o

.

fi .

.

?

.

.

❌ La separación aumenta el acoplamiento

Checklis Antes de dividir veri ca

-   ¿Cada nueva clase tendrá una responsabilidad clara?
-   ¿La división simpli ca el diseño?
-   ¿Se mantienen límites comprensibles?
-   ¿La colaboración entre clases sigue siendo sencilla?

Indicadores de alert ⚠ Después de dividir aparecen muchas clases
diminutas que dependen unas de otras para completar una operación
sencilla

⚠ Es necesario abrir varios archivos para entender una regla de negocio
simple

Automatizació No

Requiere criterio arquitectónico

Justi cación de ingenierí Dividir una clase no siempre mejora el diseño.
Una fragmentación excesiva puede hacer que el sistema sea más difícil de
comprender que una clase bien estructurada

Relación con otros estándare CL

DE

RE .

S

V

P

fi t

fi fi n

:

.

a

.

a

.

s

.

.

Arquitectura de Softwar

FUN-00 ¿Cuándo debo crear un método Objetiv De nir cuándo una porción de
lógica merece convertirse en un método independiente

Regl Un método deberá extraerse cuando represente una operación con un
propósito claramente identi cable y aporte claridad, reutilización o
encapsulamiento al diseño

No deberá dividirse el código únicamente para reducir el número de
líneas si la fragmentación di culta comprender el ujo principal

Crear un método cuand ✅ Existe una operación claramente identi cable

✅ El nombre del método explica mejor la intención que el bloque de
código

✅ La lógica puede reutilizarse

✅ Simpli ca la lectura del método principal

Evitar crear un método cuand ❌ Solo contiene una o dos instrucciones
sin signi cado propio

❌ La extracción obliga a saltar constantemente entre archivos o métodos
para entender un proceso sencillo fi fi fi a

fi o

.

1

fl e

.

.

o

fi .

o

.

fi .

?

.

.

.

❌ El nuevo método solo existe para cumplir una métrica

Checklis Antes de extraer un método veri ca

-   ¿Tiene un objetivo único?
-   ¿El nombre explica claramente lo que hace?
-   ¿Mejora la lectura del código?
-   ¿Reduce duplicación?
-   ¿No rompe la continuidad del ujo principal?

Indicadores de alert ⚠ Métodos con nombres como step1(), processA() o
helper()

⚠ Métodos extremadamente pequeños cuya única nalidad es reducir el
tamaño del método principal

⚠ Una secuencia de llamadas donde es necesario abrir diez métodos para
entender una operación simple

Automatizació No

La decisión depende del contexto y del diseño

Justi cación de ingenierí Extraer un método es una herramienta para
mejorar la claridad del código, no un objetivo en sí mismo. Una
extracción innecesaria puede fragmentar el ujo de lectura y aumentar el
esfuerzo cognitivo

Relación con otros estándare .

fi .

.

t

.

n

fl

a

fi :

a

s

.

fi fl .

.

CL

RE

Arquitectura de Softwar

FUN-00 ¿Cómo sé si un método hace demasiadas cosas Objetiv Identi car
métodos que concentran múltiples responsabilidades y di cultan su
mantenimiento

Regl Un método deberá ejecutar una única operación lógica desde la
perspectiva del negocio o de la arquitectura

La existencia de múltiples pasos internos no implica necesariamente que
el método tenga varias responsabilidades

Lo relevante es que todos los pasos colaboren para un mismo objetivo

Señales de un método sobrecargad ⚠ Valida datos

⚠ Consulta información

⚠ Aplica reglas de negocio

⚠ Envía noti caciones

⚠ Registra logs S

V

fi a

?

.

o

fi .

.

2

.

.

e

.

.

o

fi .

.

⚠ Actualiza la base de datos

Todo dentro del mismo método

Checklis Antes de aprobar un método veri ca

-   ¿Existe un único objetivo?
-   ¿Todos los pasos contribuyen a ese objetivo?
-   ¿Podría describirse el método con una sola frase?
-   ¿Los cambios futuros afectarían una única responsabilidad?

Indicadores de alert ⚠ Bloques separados por comentarios del tipo

// valida

// guarda

// enviar corre

// actualizar inventari

⚠ Múltiples bloques claramente independientes

⚠ Cambios frecuentes por motivos distintos

Automatizació Parcial

La complejidad ciclomática puede ayudar, pero no sustituye el análisis
de responsabilidades

Justi cación de ingenierí .

fi r

r

t

o

n

.

.

a

fi o

:

a

.

:

.

.

La responsabilidad de un método no se mide por el número de
instrucciones, sino por la unidad lógica que representa. Mantener un
propósito claro facilita el mantenimiento y las pruebas

Relación con otros estándare CL

Testin

RE

FUN-00 ¿Cuántos parámetros debería recibir un método Objetiv Mantener
interfaces simples y fáciles de comprender

Regl Un método deberá recibir únicamente los parámetros necesarios para
realizar su operación

Un número elevado de parámetros puede indicar que el método concentra
demasiada información o que existe un concepto del dominio que aún no ha
sido modelado

No existe un límite absoluto de parámetros, pero cada parámetro
adicional deberá justi carse

Buenas práctica ✔ Agrupar datos relacionados en un objeto cuando
representen un mismo concepto del dominio

✔ Mantener consistencia entre métodos equivalentes S

V

g

a

o

?

3

s

s

.

.

.

fi .

.

.

.

✔ Evitar parámetros opcionales que alteren signi cativamente el
comportamiento

Evita ✘ Métodos con largas listas de parámetros sin relación clara

✘ Banderas booleanas (true/false) que cambian el ujo principal, salvo
cuando representen una característica esencial y bien documentada

✘ Parámetros cuyo valor siempre es el mismo en todas las llamadas

Checklis Antes de aprobar un método veri ca

-   ¿Todos los parámetros son necesarios?
-   ¿Existe un concepto del dominio que deba modelarse?
-   ¿El orden de los parámetros resulta intuitivo?
-   ¿Cada parámetro tiene un signi cado evidente?

Indicadores de alert ⚠ Cinco, seis o más parámetros no implican
automáticamente un error, pero sí merecen una revisión de diseño

⚠ Es fácil equivocarse con el orden de los argumentos

⚠ Se pasan repetidamente los mismos grupos de datos

Automatizació Parcial

Las herramientas pueden detectar el número de parámetros, pero no si el
diseño es el adecuado

Justi cación de ingenierí .

fi r

t

.

n

fi a

fi :

a

.

fi

.

.

fl .

.

.

.

Reducir el número de parámetros simpli ca el uso de los métodos,
disminuye errores y suele revelar oportunidades para mejorar el modelo
del dominio

Relación con otros estándare CL

DE

RE

DEP-00 ¿Dónde debe vivir una regla de negocio Clasi cación: 🔴
Obligatori

Objetiv Garantizar que las reglas de negocio se implementen en el
componente responsable del dominio y no queden dispersas entre capas
técnicas

Regl Toda regla de negocio deberá implementarse en el componente que
represente el dominio o servicio responsable de dicha lógica

Las capas de presentación, infraestructura o persistencia no deberán
contener reglas de negocio que pertenezcan al dominio de la aplicación

La ubicación de una regla deberá responder a su responsabilidad
funcional y no a la conveniencia de acceso a los datos

¿Cuándo aplica ✅ Validaciones del negocio S

V

P

fi a

o

1

?

.

a

.

.

fi .

.

s

.

?

✅ Cálculos

✅ Políticas

✅ Restricciones

✅ Procesos del dominio

¿Cuándo NO aplica ❌ Formato de datos para la interfaz

❌ Conversión entre modelos

❌ Acceso a base de datos

❌ Comunicación con APIs externas

Ejempl Incorrecto

Controlle

-   valida descuent
-   calcula impuesto
-   guarda pedid
-   envía corre

El controlador concentra responsabilidades de negocio

Correcto

Controlle ↓ OrderServic ↓ Repositor o

.

.

y

r

r

e

.

o

o

.

o

.

s

.

?

.

.

.

El controlador coordina, el servicio aplica las reglas del negocio y el
repositorio persiste la información

Checklis Antes de escribir una regla veri ca

-   ¿Pertenece al negocio o a la infraestructura?
-   ¿Podría reutilizarse desde otro punto del sistema?
-   ¿Su ubicación respeta la arquitectura?
-   ¿Está mezclada con acceso a datos o presentación?

Indicadores de alert ⚠ Controladores con cientos de líneas

⚠ Consultas SQL mezcladas con cálculos

⚠ Validaciones duplicadas en distintos puntos

⚠ Reglas repetidas en varios módulos

Automatizació Parcial

El análisis estático puede detectar ciertas dependencias, pero la
ubicación correcta requiere criterio arquitectónico

Justi cación de ingenierí Una regla de negocio mal ubicada suele
terminar duplicándose, di culta las pruebas y complica la evolución del
sistema

Relación con otros estándare .

fi .

t

.

n

.

fi a

:

.

.

a

.

s

.

fi

Arquitectura Backen

Testin

Code Revie

DEP-00 ¿Dónde deben realizarse las validaciones Clasi cación: 🟡
Heurístic

Objetiv De nir una estrategia consistente para validar información sin
duplicar responsabilidades

Regl Las validaciones deberán ejecutarse en la capa que tenga la
responsabilidad de garantizar la integridad de la información
correspondiente

No todas las validaciones pertenecen al mismo lugar

Es recomendable distinguir entre

-   validaciones de entrada;
-   validaciones del dominio;
-   validaciones de persistencia. Cada una protege un aspecto distinto
    del sistema

Distribución recomendad Entrada

-   formato;
-   tipos;
-   campos obligatorios. Dominio fi fi

g

a

w

o

2

d

a

:

a

.

.

.

?

.

-   reglas del negocio;

-   políticas;

-   restricciones. Persistencia

-   integridad referencial;

-   restricciones propias del almacenamiento.

Evita ❌ Validar la misma regla en cuatro lugares distintos

❌ Con ar únicamente en el frontend

❌ Llevar reglas del negocio a la base de datos cuando deben permanecer
en el dominio

Checklis Antes de agregar una validación veri ca

-   ¿Qué estoy protegiendo?
-   ¿Existe ya esa validación en otra capa?
-   ¿La responsabilidad corresponde realmente a este componente?

Indicadores de alert ⚠ Código repetido de validación

⚠ Mensajes distintos para la misma regla

⚠ Inconsistencias entre API y aplicación

Automatizació Media

Puede veri carse parcialmente mediante pruebas y análisis estático .

fi r

fi

t

n

a

.

fi .

:

.

.

.

.

.

Justi cación de ingenierí Distribuir correctamente las validaciones
evita duplicidad, reduce inconsistencias y mejora la mantenibilidad

Relación con otros estándare Testin

Segurida

Arquitectura Backen

DEP-00 ¿Dónde debe realizarse el acceso a datos Clasi cación: 🔴
Obligatori

Objetiv Mantener el acceso a fuentes de datos aislado de la lógica del
negocio

Regl El acceso a bases de datos, sistemas de archivos, servicios
externos u otros mecanismos de persistencia deberá concentrarse en los
componentes de nidos por la arquitectura para tal n

Los componentes del dominio no deberán depender directamente de
tecnologías especí cas de almacenamiento cuando la arquitectura
establezca una capa de acceso dedicada

¿Cuándo aplica fi g

a

fi d

o

.

3

d

?

a

a

s

fi .

.

?

fi fi .

✅ Bases de datos

✅ APIs externas

✅ Caché

✅ Archivos

✅ Colas

Evita ❌ Consultas SQL dentro de componentes de presentación

❌ Acceso directo al almacenamiento desde reglas del negocio

❌ Mezclar persistencia con cálculos del dominio

Ejempl Incorrecto

Controlle ↓ SQ

Correcto

Controlle ↓ Servicio de Domini ↓ Repositori ↓ Base de dato L

r

.

.

o

.

r

r

o

.

s

.

o

.

.

.

Checklis Antes de acceder a datos veri ca

-   ¿Existe un componente responsable?
-   ¿Estoy mezclando persistencia con negocio?
-   ¿El cambio de tecnología afectaría esta clase?

Indicadores de alert ⚠ Consultas repetidas

⚠ SQL distribuido por todo el proyecto

⚠ Cambiar la base de datos implica modi car múltiples componentes

Automatizació Alta

Las dependencias entre capas pueden veri carse con herramientas de
análisis estático y reglas arquitectónicas

Justi cación de ingenierí Separar la persistencia del dominio facilita
las pruebas, reduce el acoplamiento y permite evolucionar la
infraestructura sin afectar las reglas de negocio

Relación con otros estándare Arquitectura de Dato

Arquitectura Backen

Testin

DEP-00 .

g

fi t

.

4

d

s

.

n

fi a

:

a

.

fi fi

s

.

.

¿Cuándo debe depender una clase de otra Clasi cación: 🔴 Obligatori

Objetiv Establecer criterios para crear dependencias únicamente cuando
exista una necesidad funcional claramente identi cada

Regl Una clase solo deberá depender de otra cuando necesite colaborar
directamente con ella para cumplir su responsabilidad

No deberán agregarse dependencias por conveniencia, anticipación de
funcionalidades futuras o reutilización forzada

Cada dependencia incrementa el acoplamiento del sistema y deberá justi
carse

Es recomendable cuand ✅ Existe una colaboración real

✅ La responsabilidad requiere información externa

✅ La interacción forma parte del diseño arquitectónico

Evita ❌ Agregar servicios "por si algún día se necesitan"

❌ Inyectar dependencias que nunca se utilizan

❌ Compartir una dependencia únicamente porque otra clase ya la posee fi
a

r

o

fi .

.

.

a

.

o

.

.

.

.

fi .

.

?

Checklis Antes de agregar una dependencia veri ca

-   ¿La clase realmente la necesita?
-   ¿Existe otra forma de resolver el problema?
-   ¿Incrementa innecesariamente el acoplamiento?
-   ¿La dependencia representa una colaboración del dominio?

Indicadores de alert ⚠ Constructores con muchas dependencias

⚠ Dependencias utilizadas en un solo método de forma excepcional

⚠ Eliminando una dependencia no cambia el comportamiento de la clase

Automatizació Media

Puede detectarse el número de dependencias, pero no la necesidad de cada
una

Justi cación de ingenierí Cada dependencia incrementa el acoplamiento
del sistema. Mantener únicamente las necesarias facilita la evolución,
las pruebas y la comprensión del código

Relación con otros estándare CL

Arquitectur

Testin S

g

.

fi a

t

n

a

fi a

:

.

s

.

.

.

.

DEP-00 ¿Cómo identi car una dependencia innecesaria Clasi cación: 🟡
Heurístic

Objetiv Detectar dependencias que aumentan la complejidad sin aportar
valor

Regl Una dependencia deberá eliminarse cuando no participe activamente
en la responsabilidad principal del componente

La existencia de una dependencia no utilizada o utilizada únicamente en
escenarios excepcionales deberá revisarse

Señales comune ⚠ Nunca se utiliza

⚠ Solo aparece durante la inicialización

⚠ Se utiliza únicamente para acceder a otra dependencia

⚠ Solo sirve para registrar logs secundarios

⚠ Existe porque fue copiada desde otra clase

Checklis Antes de conservar una dependencia veri ca fi a

o

t

5

.

?

s

.

a

fi .

.

fi .

:

.

.

.

-   ¿Es utilizada regularmente?
-   ¿Pertenece realmente a esta responsabilidad?
-   ¿Puede obtenerse desde otro componente?
-   ¿La arquitectura sigue siendo coherente si desaparece?

Indicadores de alert ⚠ Constructores excesivamente largos

⚠ Dependencias comentadas

⚠ Dependencias marcadas como "para futuro"

Automatizació Alta

Las herramientas de análisis pueden detectar dependencias no utilizadas

Justi cación de ingenierí Las dependencias innecesarias incrementan el
acoplamiento, di cultan las pruebas y hacen más compleja la lectura del
código

Relación con otros estándare Code Revie

Arquitectur

Testin

DEP-00 ¿Cómo evitar dependencias circulares .

g

fi a

w

6

n

.

.

a

.

a

s

.

fi .

?

Clasi cación: 🔴 Obligatori

Objetiv Prevenir ciclos de dependencias que di culten el mantenimiento y
la evolución del sistema

Regl Los componentes no deberán depender mutuamente de forma directa ni
indirecta

Cuando dos componentes necesiten colaborar de manera bidireccional
deberá evaluarse una reorganización de responsabilidades, la
introducción de una abstracción o la creación de un componente
intermedio

Ejempl Incorrect

↓

↓

↓

Correct

↓

↓ A

B

C

A

A

B

C o A

fi a

o

o

o

o

.

a

fi .

.

↓

Contrat

↑

Checklis Antes de crear una dependencia veri ca

-   ¿Genera un ciclo?
-   ¿Puede invertirse la dependencia?
-   ¿Existe una interfaz que reduzca el acoplamiento?
-   ¿La colaboración puede reorganizarse?

Indicadores de alert ⚠ Importaciones cruzadas

⚠ Módulos imposibles de probar por separado

⚠ Cambiar una clase obliga a recompilar muchas otras

Automatizació Alta

Las herramientas de análisis arquitectónico pueden detectar dependencias
circulares automáticamente

Justi cación de ingenierí Las dependencias circulares di cultan el
mantenimiento, impiden la modularidad y suelen indicar responsabilidades
mal distribuidas B

.

fi o

t

.

n

.

fi a

fi

a

:

.

.

.

Relación con otros estándare Arquitectur

Módulo

Code Revie

DEP-00 ¿Cuántas dependencias son demasiadas Clasi cación: 🟡 Heurístic

Objetiv Detectar clases cuya cantidad de colaboraciones puede indicar un
problema de diseño

Regl No existe un número máximo universal de dependencias aceptables

Sin embargo, una clase con un número elevado de colaboradores deberá
revisarse para determinar si concentra responsabilidades excesivas

El análisis deberá considerar la complejidad del dominio y no únicamente
una métrica numérica

Señales de revisió 🟡 Cinco dependencias

🟡 Ocho dependencias

🟡 Diez dependencias

No implican automáticamente un error fi a

s

a

w

o

7

.

.

.

n

a

.

s

.

.

?

.

.

Sí justi can una revisión de diseño

Preguntas de revisió - ¿Todas colaboran activamente? - ¿Existen
responsabilidades mezcladas? - ¿Puedo dividir la clase? - ¿Alguna
dependencia solo está para un caso excepcional?

Indicadores de alert ⚠ Constructores de veinte líneas

⚠ La mitad de las dependencias solo se usan una vez

⚠ Es difícil describir la responsabilidad de la clase

Automatizació Alta para métricas

Baja para interpretar si el diseño es correcto

Justi cación de ingenierí Una clase con muchas dependencias suele
indicar una responsabilidad demasiado amplia. Sin embargo, el número por
sí solo no determina la calidad del diseño

Relación con otros estándare CL

RE

Arquitectur S

V

fi fi a

.

n

a

n

.

.

a

.

s

.

.

.

DEP-00 ¿Debo depender de implementaciones concretas o de contratos Clasi
cación: 🔴 Obligatori

Objetiv Favorecer un diseño exible y desacoplado que permita sustituir
implementaciones sin afectar a los consumidores

Regl Cuando la arquitectura del proyecto lo requiera, los componentes
deberán depender de contratos (interfaces o abstracciones) y no de
implementaciones concretas

Esta regla no implica crear interfaces para todas las clases. Las
abstracciones deberán introducirse únicamente cuando aporten un bene cio
claro, como facilitar la sustitución de implementaciones, las pruebas o
la evolución del sistema

Es recomendable cuand ✅ Existen varias implementaciones posibles

✅ Se requiere sustituir componentes según el entorno

✅ Se desea aislar dependencias externas

✅ Las pruebas necesitan reemplazar colaboraciones por dobles de prueba
(mocks, stubs o fakes)

Evita fi .

a

r

o

8

.

fl a

o

.

.

fi ?

.

.

.

❌ Crear interfaces para clases que nunca tendrán otra implementación
solo por seguir un patrón

❌ Introducir abstracciones que no aportan claridad ni exibilidad

Checklis Antes de crear una interfaz veri ca

-   ¿Existe una necesidad real de desacoplar?
-   ¿Se espera más de una implementación?
-   ¿Facilita las pruebas o la evolución?
-   ¿Reduce el acoplamiento sin añadir complejidad innecesaria?

Indicadores de alert ⚠ Interfaces con una única implementación durante
años sin un motivo arquitectónico

⚠ Clases e interfaces que evolucionan siempre juntas y nunca se utilizan
de forma independiente

Automatizació Baja

Las herramientas pueden detectar dependencias concretas, pero no decidir
cuándo una abstracción aporta valor

Justi cación de ingenierí Las abstracciones son una herramienta para
reducir el acoplamiento, no un objetivo. Introducirlas solo cuando
resuelven un problema concreto mantiene el diseño simple y facilita su
evolución

Relación con otros estándare IN T

.

.

fi t

.

n

.

fi a

:

a

s

fl

.

.

.

Testin

Arquitectur

ERR --- Manejo de Errore

ERR-00 ¿Cuándo debo generar un error Clasi cación: 🔴 Obligatori

Objetiv Garantizar que los errores representen situaciones excepcionales
que impidan continuar la operación de forma segura o correcta

Regl Un error deberá generarse únicamente cuando el sistema no pueda
continuar la operación respetando las reglas del negocio, la integridad
de los datos o la estabilidad del proceso

Los errores no deberán utilizarse como mecanismo habitual de control de
ujo

Es correcto generar un error cuand ✅ Falta información indispensable

✅ Se incumple una regla del negocio

✅ Existe corrupción de datos

✅ Falla una dependencia crítica

✅ La operación no puede completarse correctamente fi g

a

a

o

1

a

.

.

.

.

.

.

s

o

?

fl .

.

Evita ❌ Utilizar excepciones para salir de ciclos

❌ Reemplazar condiciones normales por manejo de errores

❌ Lanzar errores para controlar decisiones esperadas

Checklis Antes de lanzar un error veri ca

-   ¿La operación realmente no puede continuar?
-   ¿Existe una alternativa segura?
-   ¿El error representa una condición excepcional?
-   ¿La causa puede describirse claramente?

Indicadores de alert ⚠ Métodos que lanzan excepciones constantemente
durante escenarios normales

⚠ Uso de excepciones para lógica de negocio cotidiana

Automatizació Media

Las herramientas pueden detectar ciertos patrones, pero la intención
requiere revisión técnica

Justi cación de ingenierí Las excepciones representan eventos
extraordinarios. Utilizarlas como mecanismo de control normal hace el
código más difícil de entender, probar y mantener .

fi r

t

n

fi

a

:

a

.

.

.

.

.

.

.

Relación con otros estándare Testin

Loggin

Code Revie

ERR-00 ¿Cuándo debo capturar un error Clasi cación: 🔴 Obligatori

Objetiv Capturar errores únicamente cuando el componente pueda
manejarlos de manera útil

Regl Un error solo deberá capturarse cuando el componente tenga la
capacidad de recuperarse, transformarlo, agregar contexto o realizar una
acción compensatoria

Si no puede hacer ninguna de esas acciones, el error deberá propagarse
al componente responsable

Es correcto capturar cuand ✅ Puede reintentarse la operación

✅ Puede registrarse información adicional

✅ Puede ejecutarse una compensación

✅ Puede traducirse a un error del dominio fi g

g

a

w

.

o

2

a

.

.

.

.

o

s

.

?

.

Evita ❌ Capturar únicamente para ignorar el error

❌ Capturar para imprimir un mensaje y continuar

❌ Capturar sin aportar ningún valor

Ejempl Incorrect

tr guardar(

catc // no hacer nad

Correct

tr guardar(

catc registrar context ejecutar compensació propagar erro

Checklis - ¿Puedo resolver el problema? - ¿Puedo agregar contexto? -
¿Puedo compensar la operación? - ¿Si no hago nada, es mejor propagarlo?

Indicadores de alert y

y

h

h

o

r

o

o

t

)

)

r

a

o

a

n

.

.

.

⚠ Bloques catch vacíos

⚠ Comentarios como

// ignora

// nunca pas

Automatizació Alta

Los analizadores estáticos detectan bloques vacíos y capturas inútiles

Justi cación de ingenierí Capturar un error sin actuar sobre él oculta
problemas y di culta el diagnóstico de fallos en producción

Relació Loggin

Observabilida

Testin

ERR-00 ¿Qué información debe contener un error Clasi cación: 🔴
Obligatori .

fi g

g

fi .

n

r

d

3

a

:

n

.

a

a

fi .

?

Objetiv Facilitar el diagnóstico de fallos proporcionando información
útil y su ciente

Regl Todo error deberá comunicar claramente qué ocurrió y, cuando sea
posible, aportar el contexto necesario para su análisis

La información incluida deberá ayudar a comprender el problema sin
exponer datos sensibles

Un buen error respond - ¿Qué ocurrió? - ¿Dónde ocurrió? - ¿Qué operación
se estaba realizando? - ¿Qué condición lo provocó?

Evita ❌

Erro

❌

Falló

❌

Exceptio

❌

Unknown erro r

a

.

r

n

o

r

.

e

fi .

.

Checklis - ¿Describe el problema? - ¿Incluye contexto? - ¿Evita
información sensible? - ¿Puede entenderse semanas después?

Indicadores de alert ⚠ Mensajes genéricos

⚠ Errores imposibles de reproducir

⚠ Falta de contexto

Automatizació Media

Puede veri carse parcialmente mediante pruebas y revisiones

Justi cació Los errores son una de las principales fuentes de
información para diagnosticar incidentes. Un mensaje pobre incrementa
signi cativamente el tiempo de resolución

Relació Loggin

Observabilida .

g

fi fi n

t

d

n

.

.

n

fi a

.

.

.

ERR-00 ¿Qué información NO debe contener un error Clasi cación: 🔴
Obligatori

Objetiv Proteger información sensible y evitar fugas de datos mediante
mensajes de error

Regl Los errores expuestos fuera del límite de con anza del sistema no
deberán revelar información técnica o sensible que pueda comprometer la
seguridad, la privacidad o el funcionamiento de la aplicación

Los detalles técnicos completos deberán registrarse en mecanismos
internos de diagnóstico, no mostrarse directamente al usuario

Nunca expone ❌ Contraseñas

❌ Tokens

❌ Llaves privadas

❌ Cadenas de conexión

❌ Consultas SQL completas

❌ Rutas internas del servidor

❌ Stack traces en producción fi a

.

.

?

o

.

4

.

r

.

a

.

.

.

.

fi .

❌ Datos personales innecesarios

Es correcto mostra ✅ Un identi cador del incidente

✅ Una descripción funcional del problema

✅ Pasos siguientes para el usuario, cuando aplique

Checklis Antes de devolver un error veri ca

-   ¿Revela información sensible?
-   ¿Expone detalles internos de la infraestructura?
-   ¿Ayuda al usuario sin comprometer la seguridad?
-   ¿Existe un identi cador para correlacionar el incidente con los
    registros internos?

Indicadores de alert ⚠ Stack trace visible en producción

⚠ Mensajes con SQL o rutas del servidor

⚠ Exposición de credenciales en registros o respuestas

Automatizació Alta

Existen herramientas capaces de detectar patrones comunes de exposición
de información sensible

Justi cación de ingenierí .

fi .

fi t

fi n

r

fi a

.

.

:

.

a

.

.

.

.

Un mensaje de error es también una interfaz del sistema. Debe ser útil
para el usuario y para el equipo técnico, pero nunca convertirse en una
fuente de información para un atacante

Relació Segurida

Loggin

Observabilida

ERR-00 ¿Cuándo debo reintentar una operación Clasi cación: 🟡 Heurístic

Objetiv Aplicar reintentos únicamente cuando aumenten la probabilidad de
éxito sin generar efectos secundarios indeseados

Regl Los reintentos deberán utilizarse solo frente a errores
transitorios, como fallos temporales de red o indisponibilidad
momentánea de un servicio

No deberán emplearse sobre errores permanentes ni sobre operaciones que
puedan producir efectos duplicados, salvo que exista un mecanismo de
idempotencia

Es recomendable reintenta ✅ Timeouts temporales

✅ Errores de comunicación fi g

a

d

n

o

d

5

.

.

a

.

r

.

.

?

.

✅ Servicios externos con recuperación automática

Evita ❌ Reintentar errores de validación

❌ Reintentar credenciales inválidas

❌ Reintentar reglas de negocio incumplidas

❌ Reintentar operaciones no idempotentes sin protección

Checklis - ¿El error es transitorio? - ¿El reintento puede causar
duplicados? - ¿Existe un límite de intentos? - ¿Hay una estrategia de
espera progresiva (backoff) cuando corresponda?

Indicadores de alert ⚠ Bucles in nitos de reintentos

⚠ Saturación de servicios externos

⚠ Creación accidental de registros duplicados

Automatizació Media

Las herramientas pueden detectar patrones de reintento, pero la decisión
depende del contexto operativo .

r

.

fi t

n

a

.

.

.

.

.

.

.

.

Justi cación de ingenierí Los reintentos mejoran la resiliencia
únicamente cuando se aplican a fallos temporales. Utilizarlos
indiscriminadamente incrementa la carga del sistema y puede agravar un
incidente

Relació Arquitectura Distribuid

Observabilida

Testin

LOG --- Registro de Eventos (Logging

LOG-00 ¿Cuándo debo registrar un evento Clasi cación: 🔴 Obligatori

Objetiv Registrar únicamente los eventos que aporten valor para la
operación, el diagnóstico o la auditoría del sistema

Regl Todo evento registrado deberá tener un propósito claro

Los registros deberán facilitar la comprensión del comportamiento del
sistema sin generar ruido innecesario

Registrar información porque "algún día podría servir" no constituye un
motivo su ciente fi g

a

fi .

n

o

d

1

.

a

a

a

.

?

)

fi .

.

Es recomendable registra ✅ Inicio de procesos relevantes

✅ Finalización de procesos importantes

✅ Errores

✅ Advertencias

✅ Cambios de estado

✅ Integraciones externas

✅ Eventos de seguridad

Evita ❌ Registrar cada línea ejecutada

❌ Registrar información repetitiva

❌ Registrar eventos sin utilidad operacional

Checklis Antes de agregar un log veri ca

-   ¿Alguien utilizará esta información?
-   ¿Facilita diagnosticar un problema?
-   ¿Ayuda a operar el sistema?
-   ¿Podría eliminarse sin perder información relevante?

Indicadores de alert ⚠ Miles de registros sin utilidad r

.

t

.

.

.

.

fi :

a

.

.

.

.

r

.

.

⚠ Di cultad para encontrar eventos importantes

⚠ Costos elevados de almacenamiento

Automatizació No

La utilidad de un registro requiere criterio de ingeniería

Justi cació Un exceso de registros genera ruido, incrementa costos y di
culta localizar información importante durante un incidente

Relació Observabilida

Operació

Code Revie

LOG-00 ¿Qué información debe contener un registro Clasi cación: 🔴
Obligatori

Objetiv Garantizar que cada registro proporcione contexto su ciente para
comprender el evento ocurrido .

fi fi fi n

w

n

o

d

2

n

n

a

.

.

.

fi .

fi ?

.

Regl Todo registro deberá responder, en la medida de lo posible, las
siguientes preguntas

-   ¿Qué ocurrió?
-   ¿Cuándo ocurrió?
-   ¿Dónde ocurrió?
-   ¿Quién realizó la acción?
-   ¿Sobre qué recurso ocurrió?
-   ¿Cuál fue el resultado?

Información recomendad ✅ Fecha y hora

✅ Identi cador de la operación

✅ Usuario (cuando aplique)

✅ Recurso afectado

✅ Resultado

✅ Contexto relevante

Evita ❌ Mensajes ambiguos

❌ Registros sin contexto

❌ Información redundante

Ejempl Mal o

a

r

fi o

.

.

.

.

.

.

.

.

.

a

:

Guardado

Buen

Pedido 5821 actualizado por usuario 104 **Estado:** Confirmado Duración:
182 ms

Checklis - ¿Describe claramente el evento? - ¿Incluye contexto su
ciente? - ¿Es entendible semanas después? - ¿Facilita reproducir el
problema?

Indicadores de alert ⚠ Mensajes genéricos

⚠ Registros imposibles de interpretar

Automatizació Parcial

Puede veri carse la estructura, no la calidad semántica

Justi cació El contexto convierte un registro en información útil. Sin
contexto, un log rara vez ayuda a resolver un incidente

Relació o

.

fi fi n

.

t

n

fi .

.

n

.

.

a

.

.

.

Observabilida

ER

LOG-00 ¿Qué información nunca debe registrarse Clasi cación: 🔴
Obligatori

Objetiv Evitar la exposición de información sensible mediante los
mecanismos de registro

Regl Los registros no deberán contener información cuya divulgación
pueda comprometer la seguridad, la privacidad o el cumplimiento
normativo

Cuando sea necesario registrar información relacionada con un dato
sensible, deberá utilizarse una representación protegida, anonimizada o
enmascarada

Nunca registra ❌ Contraseñas

❌ Tokens

❌ Llaves privadas

❌ Números completos de tarjetas

❌ Datos biométricos

❌ Información médica R

fi a

.

o

d

.

3

.

.

r

.

a

.

.

.

.

?

❌ Datos personales innecesarios

❌ Secretos de infraestructura

Es recomendable registra ✅ Identi cadores internos

✅ Referencias

✅ Versiones enmascaradas

✅ Hashes cuando correspondan

Checklis - ¿Contiene datos sensibles? - ¿Puede anonimizarse? - ¿Existe
una política de protección de datos aplicable? - ¿El registro cumple con
los requisitos legales y corporativos?

Indicadores de alert ⚠ Logs con credenciales

⚠ Información personal visible

⚠ Tokens copiados en texto plano

Automatizació Alta

Existen herramientas capaces de detectar patrones de datos sensibles .

fi t

.

n

.

.

.

.

.

a

.

.

.

r

.

Justi cació Los registros suelen almacenarse durante largos periodos y
ser accesibles para distintos equipos. Una ltración a través de los logs
puede tener un impacto tan grave como una vulnerabilidad en la
aplicación

Relació Segurida

Complianc

ER

LOG-00 ¿Qué nivel de severidad debo utilizar Clasi cación: 🔴 Obligatori

Objetiv Clasi car los registros de forma consistente para facilitar el
monitoreo y el diagnóstico

Regl Todo registro deberá utilizar un nivel de severidad acorde con el
impacto real del evento

El uso incorrecto de los niveles reduce la efectividad de las
herramientas de monitoreo y di culta la atención de incidentes

Niveles recomendado DEBU R

fi fi fi a

fi G

d

e

n

o

.

4

n

.

a

s

?

.

.

fi

Información útil únicamente durante el desarrollo o el análisis
detallado de un problema

INF

Eventos normales de operación

Inicio de procesos

Finalización

Cambios esperados

WAR

Situaciones anómalas que no impiden continuar

ERRO

Fallos que afectan una operación especí ca

FATAL / CRITICA

Errores que comprometen la continuidad del sistema o requieren atención
inmediata

Evita ❌ Registrar todo como ERROR

❌ Utilizar INFO para errores

❌ Utilizar DEBUG en producción sin necesidad

Checklis - ¿El nivel re eja el impacto? O

N

R

r

fl .

t

.

.

L

.

.

.

fi .

.

.

.

.

-   ¿Generará alertas innecesarias?
-   ¿La clasi cación es consistente con el resto del sistema?

Indicadores de alert ⚠ Miles de errores que realmente son advertencias

⚠ Alertas constantes por eventos normales

Automatizació Alta

Puede veri carse mediante políticas de observabilidad

Justi cació La severidad adecuada permite priorizar incidentes, reducir
falsas alarmas y mejorar la capacidad de respuesta del equipo

Relació Observabilida

Operació

Monitore

LOG-00 ¿Cómo debo relacionar los registros de una misma operación .

fi fi n

o

fi n

d

5

n

n

.

a

?

.

.

.

Clasi cación: 🔴 Obligatori

Objetiv Permitir reconstruir el recorrido completo de una operación a
través de múltiples componentes o servicios

Regl Todos los registros pertenecientes a una misma operación deberán
compartir un identi cador de correlación (Correlation ID o equivalente)

Este identi cador deberá propagarse entre procesos, servicios y
componentes para facilitar el seguimiento de la ejecución

Es recomendable inclui ✅ Correlation ID

✅ Request ID

✅ Trace ID

✅ Session ID cuando corresponda

Checklis - ¿Cada operación posee un identi cador único? - ¿El identi
cador se propaga entre componentes? - ¿Permite reconstruir el ujo
completo?

Indicadores de alert ⚠ Es imposible relacionar dos registros del mismo
proceso

⚠ Cada componente genera identi cadores distintos para la misma
solicitud fi a

.

fi fi o

.

t

.

.

fl .

a

a

fi fi .

r

.

.

.

fi

Automatizació Alta

Las plataformas modernas de observabilidad permiten validar y propagar
automáticamente estos identi cadores

Justi cació En sistemas distribuidos, un incidente rara vez ocurre en un
único componente. El identi cador de correlación permite seguir una
operación completa y reduce drásticamente el tiempo de diagnóstico

Relació Observabilida

Tracin

Arquitectura Distribuid

CFG --- Con guració

CFG-00 ¿Qué debe considerarse con guración Clasi cación: 🔴 Obligatori

Objetiv Distinguir claramente entre el comportamiento del software y los
valores que pueden variar según el entorno o la operación .

fi fi g

fi .

n

o

d

.

1

n

n

a

fi a

.

n

fi ?

fi

Regl Todo valor que pueda cambiar entre entornos, clientes, despliegues
o con guraciones operativas deberá tratarse como con guración y no
formar parte del código fuente

La lógica del sistema deberá permanecer estable; la con guración
permitirá adaptar su comportamiento sin modi car la implementación

Normalmente es con guració ✅ URLs de servicios

✅ Puertos

✅ Cadenas de conexión

✅ Claves de API

✅ Credenciales

✅ Parámetros de infraestructura

✅ Límites con gurables

✅ Banderas de funcionalidades (feature ags)

Normalmente NO es con guració ❌ Reglas del negocio permanentes

❌ Algoritmos

❌ Flujo de la aplicación

❌ Decisiones arquitectónicas a

.

.

fi .

.

.

fi .

.

.

fi .

fi .

.

fi fl n

.

.

n

fi .

fi

Checklis Antes de escribir un valor veri ca

-   ¿Podría cambiar entre ambientes?
-   ¿Podría variar para otro cliente?
-   ¿Requerirá ajustes operativos?
-   ¿Estoy obligando a recompilar para cambiarlo?

Indicadores de alert ⚠ URLs escritas directamente en el código

⚠ Credenciales incrustadas

⚠ Valores repetidos en varios archivos

Automatizació Alta

Las herramientas pueden detectar constantes sospechosas y secretos
incrustados

Justi cació Separar con guración y código facilita el despliegue, reduce
errores operativos y permite adaptar el sistema sin modi car su
implementación

Relació Segurida

DevOp

Arquitectur .

s

fi d

a

fi n

t

n

fi n

.

fi

a

:

.

.

.

.

CFG-00 ¿Dónde debe almacenarse la con guración Clasi cación: 🔴
Obligatori

Objetiv Centralizar la con guración para facilitar su administración y
evitar inconsistencias

Regl La con guración deberá almacenarse utilizando los mecanismos de
nidos por la arquitectura del proyecto, manteniendo una única fuente de
verdad para cada valor con gurable

Los componentes no deberán de nir con guraciones duplicadas ni mantener
copias locales de parámetros globales

Es recomendable utiliza ✅ Variables de entorno

✅ Archivos de con guración

✅ Gestores de secretos

✅ Servicios centralizados de con guración cuando la arquitectura lo
requiera

Evita ❌ Con guración distribuida en múltiples archivos

❌ Valores duplicados fi fi a

fi r

o

2

fi .

fi .

.

.

a

.

fi fi r

fi .

fi fi fi .

.

.

?

❌ Con guración generada dinámicamente sin control

Checklis - ¿Existe una única fuente de verdad? - ¿Es fácil localizar el
valor? - ¿Puede modi carse sin recompilar? - ¿La ubicación respeta la
arquitectura?

Indicadores de alert ⚠ El mismo parámetro aparece en cinco archivos

⚠ Nadie sabe cuál valor es el correcto

⚠ Cambiar una con guración implica modi car múltiples componentes

Automatizació Alta

Es posible detectar duplicaciones y con guraciones inconsistentes
mediante herramientas de análisis y despliegue

Justi cació Una con guración centralizada reduce errores, simpli ca el
mantenimiento y facilita la administración de múltiples entornos

Relació DevOp

Arquitectur .

s

fi fi fi a

n

fi t

n

fi .

n

a

.

.

fi fi .

fi .

.

CFG-00 ¿Cómo deben manejarse los secretos Clasi cación: 🔴 Obligatori

Objetiv Proteger credenciales y datos sensibles durante todo su ciclo de
vida

Regl Los secretos nunca deberán almacenarse en el código fuente,
repositorios públicos, archivos de ejemplo o registros de eventos

La gestión de secretos deberá realizarse mediante mecanismos seguros de
nidos por la organización

Se consideran secreto ✅ Contraseñas

✅ Tokens

✅ Certi cados

✅ Llaves privadas

✅ API Keys

✅ Secretos de cifrado

Nunca hace fi a

fi .

o

.

.

.

.

3

r

.

.

a

.

s

.

fi ?

❌ Hardcodearlos

❌ Compartirlos por correo o mensajería sin protección

❌ Incluirlos en ejemplos o documentación pública

❌ Registrarlos en logs

Checklis - ¿El secreto está protegido? - ¿Puede rotarse sin modi car el
código? - ¿Su acceso está restringido? - ¿Existe un proceso para
revocarlo?

Indicadores de alert ⚠ Claves visibles en commits

⚠ Secretos enviados por chat

⚠ Archivos .env compartidos sin control

Automatizació Muy alta

Existen herramientas especializadas para detectar secretos expuestos
antes de integrar cambios al repositorio

Justi cació La exposición de un secreto puede comprometer todo un
sistema. La prevención es signi cativamente menos costosa que la
respuesta a un incidente fi fi .

.

t

n

.

n

.

fi

.

.

a

.

.

.

.

Relació Segurida

DevSecOp

Loggin

CFG-00 ¿Cuándo debo utilizar valores por defecto Clasi cación: 🟡
Heurístic

Objetiv Proporcionar un comportamiento predecible sin ocultar errores de
con guración

Regl Los valores por defecto deberán utilizarse únicamente cuando exista
un comportamiento seguro y razonable en ausencia de una con guración
explícita

Nunca deberán ocultar con guraciones obligatorias ni permitir que el
sistema opere silenciosamente con parámetros incorrectos

Es recomendabl ✅ Valores seguros

✅ Con guración de desarrollo

✅ Parámetros opcionales fi g

a

fi d

s

n

o

4

.

e

.

fi a

.

fi .

.

fi .

?

Evita ❌ Credenciales por defecto

❌ Con guraciones inseguras

❌ Valores que oculten errores de despliegue

Checklis - ¿El valor por defecto es seguro? - ¿El sistema puede operar
correctamente con él? - ¿El usuario sabrá que se utilizó?

Indicadores de alert ⚠ Producción funcionando con valores de desarrollo

⚠ Con guraciones críticas sustituidas silenciosamente

Automatizació Media

Las herramientas pueden detectar con guraciones por defecto, pero no
siempre determinar si son apropiadas

Justi cació Un valor por defecto bien diseñado mejora la experiencia de
desarrollo; uno incorrecto puede provocar fallos difíciles de detectar
en producción

Relació .

fi fi fi r

.

n

t

n

n

.

.

a

fi .

.

.

.

DevOp

Segurida

CFG-00 ¿Cómo debo utilizar Feature Flags Clasi cación: 🟡 Heurístic

Objetiv Permitir habilitar o deshabilitar funcionalidades de forma
controlada sin afectar la estabilidad del sistema

Regl Las Feature Flags deberán utilizarse para controlar la
disponibilidad de funcionalidades en desarrollo, despliegues progresivos
o experimentos

No deberán convertirse en mecanismos permanentes que compliquen la
lógica de negocio

Es recomendabl ✅ Despliegues graduales

✅ Pruebas A/B

✅ Activación por cliente

✅ Funcionalidades experimentales

Evita fi s

a

.

r

d

o

.

5

e

.

.

a

.

.

?

.

❌ Mantener ags obsoletas durante meses o años

❌ Anidar múltiples ags que di culten seguir el ujo del código

❌ Utilizarlas para reemplazar decisiones permanentes de diseño

Checklis - ¿La ag tiene un propósito de nido? - ¿Existe una fecha o
condición para retirarla? - ¿Está documentada? - ¿Se supervisa su uso?

Indicadores de alert ⚠ Código lleno de condiciones relacionadas con ags
antiguas

⚠ Funcionalidades que nunca abandonan el estado experimental

⚠ Nadie sabe qué ags siguen activas

Automatizació Alta

Es posible detectar ags sin uso, expiradas o inconsistentes mediante
herramientas de análisis y gestión de con guración

Justi cació Las Feature Flags son una herramienta poderosa para reducir
riesgos durante el despliegue, pero una mala gestión incrementa la
complejidad y la deuda técnica

Relació .

fl fi n

t

fl fi n

fl fl

fl

n

.

fi a

fi

.

fl fl .

.

.

.

.

.

DevOp

Arquitectur

Testin

DOC --- Documentación del Códig

DOC-00 ¿Cuándo debo escribir un comentario Clasi cación: 🟡 Heurístic

Objetiv Utilizar comentarios únicamente cuando aporten información que
no pueda expresarse claramente mediante el propio código

Regl Un comentario deberá escribirse únicamente cuando agregue
conocimiento que no sea evidente a partir de la estructura, los nombres
o la arquitectura del código

Los comentarios no deberán utilizarse para compensar código confuso o
nombres poco descriptivos

Cuando un bloque requiera muchos comentarios para entenderse, deberá
evaluarse una mejora del diseño

Es recomendable comenta ✅ Decisiones arquitectónicas

✅ Restricciones del negocio poco evidentes fi g

s

a

.

a

.

o

1

a

.

.

r

.

.

o

?

✅ Supuestos importantes

✅ Algoritmos complejos

✅ Soluciones temporales justi cadas

Evita ❌ Explicar línea por línea lo que hace el código

❌ Repetir el nombre del método

❌ Describir operaciones obvias

❌ Utilizar comentarios para ocultar problemas de diseño

Ejempl Incorrect

// Incrementar contado

contador+

Correct

// Se utiliza un contador independiente porqu // el proveedor externo
puede enviar eventos duplicados

Checklis Antes de escribir un comentario veri ca

-   ¿Aporta información nueva?
-   ¿Explica una decisión?
-   ¿Podría eliminarse mejorando el código? o

r

o

o

-   

t

.

.

fi .

r

.

fi .

:

.

.

e

.

-   ¿Seguirá siendo útil dentro de un año?

Indicadores de alert ⚠ Comentarios que describen instrucciones evidentes

⚠ Comentarios que contradicen el código

⚠ Comentarios más largos que el propio método

Automatizació Media

Puede detectarse la presencia de comentarios, pero no su calidad

Justi cació Los comentarios deben preservar conocimiento, no sustituir
un diseño claro. Un comentario innecesario incrementa el esfuerzo de
mantenimiento y puede quedar desactualizado

Relació RE

CL

FU

DOC-00 ¿Cuándo debo documentar una decisión de arquitectura V

S

N

.

fi n

2

n

n

?

a

.

.

.

.

.

Clasi cación: 🔴 Obligatori

Objetiv Preservar el razonamiento detrás de decisiones técnicas
relevantes

Regl Toda decisión arquitectónica que tenga impacto signi cativo en el
diseño, mantenimiento o evolución del sistema deberá documentarse fuera
del código mediante el mecanismo de nido por la organización (por
ejemplo, ADR, especi cación técnica o manual de arquitectura)

El código implementa la decisión

La documentación explica por qué se tomó

Debe documentars ✅ Cambio de arquitectura

✅ Selección de tecnología

✅ Restricciones técnicas

✅ Trade-offs importantes

✅ Decisiones difíciles de revertir

No documentar únicamente en comentario ❌ Arquitectura completa

❌ Decisiones corporativas

❌ Justi caciones extensas fi a

fi o

.

.

.

.

.

.

.

a

e

.

.

fi .

fi .

s

.

fi

Checklis - ¿La decisión afecta el diseño? - ¿Otra persona entenderá por
qué se tomó? - ¿Existe un documento o cial donde registrarla?

Indicadores de alert ⚠ "Nadie recuerda por qué hicimos esto.

⚠ Decisiones críticas explicadas únicamente en un comentario dentro del
código

Automatizació No

Requiere criterio de arquitectura

Justi cació Las decisiones sobreviven mucho más tiempo que las
implementaciones. Documentarlas evita repetir discusiones y reduce el
riesgo de revertir soluciones correctamente justi cadas

Relació Arquitectur

AD

Engineering Handboo

DOC-00 ¿Cómo debo documentar una API .

R

fi a

n

t

3

n

k

n

fi

a

.

``` text
"
```

?

fi .

.

Clasi cación: 🔴 Obligatori

Objetiv Garantizar que las interfaces públicas sean comprensibles y
utilizables por otros equipos o sistemas

Regl Toda API pública deberá contar con documentación su ciente para
permitir su consumo sin necesidad de revisar el código fuente

La documentación deberá mantenerse sincronizada con la implementación

Debe inclui ✅ Propósito

✅ Parámetros

✅ Respuestas

✅ Errores

✅ Requisitos de autenticación

✅ Ejemplos de uso

Evita ❌ Documentación desactualizada

❌ Ejemplos que ya no funcionan

❌ Omitir códigos de error fi a

.

r

.

o

.

.

.

r

.

.

a

.

.

.

.

fi .

Checklis - ¿Puede utilizarse sin leer el código? - ¿Los ejemplos siguen
siendo válidos? - ¿Los errores están documentados? - ¿Existe versionado
cuando aplica?

Indicadores de alert ⚠ El consumidor necesita preguntar cómo usar la API

⚠ La documentación contradice el comportamiento real

Automatizació Alta

Puede integrarse con herramientas que generan documentación a partir de
contratos u especi caciones

Justi cació Una API es un contrato. Una documentación incompleta genera
integraciones frágiles y aumenta el costo de soporte

Relació Arquitectura Backen

Testin

Integracione

DOC-00 .

g

fi fi n

s

t

.

4

n

.

d

n

a

.

.

¿Qué documentación debe mantenerse junto al código Clasi cación: 🟡
Heurístic

Objetiv Mantener cerca del código únicamente la documentación que
evoluciona al mismo ritmo que él

Regl La documentación ubicada dentro del repositorio deberá describir
aspectos directamente relacionados con la implementación y mantenerse
sincronizada con ella

La documentación organizacional, de procesos o de negocio deberá
mantenerse en los repositorios documentales correspondientes

Es recomendable mantener en el repositori ✅ README

✅ Guías de instalación

✅ Guías de desarrollo

✅ Ejemplos de con guración

✅ Convenciones especí cas del proyecto

Mantener fuera del repositori ❌ Manuales corporativos

❌ Políticas organizacionales fi a

o

.

?

fi .

.

fi .

a

.

.

.

.

o

o

.

.

❌ Procedimientos administrativos

Checklis - ¿La documentación cambia junto con el código? - ¿Está en el
lugar adecuado? - ¿Forma parte del proceso de desarrollo?

Indicadores de alert ⚠ README desactualizado

⚠ Documentos duplicados en distintas ubicaciones

⚠ Información contradictoria

Automatizació Media

Puede veri carse la existencia y estructura, pero no la vigencia del
contenido

Justi cació Cada tipo de documentación tiene un ciclo de vida distinto.
Mantenerla en el lugar adecuado facilita su actualización y evita
inconsistencias

Relació Engineering Handboo

Arquitectur

DevOp .

s

fi fi a

n

t

n

k

n

.

.

a

.

.

.

.

DOC-00 ¿Cómo debo documentar código generado por IA Clasi cación: 🔴
Obligatori

Objetiv Garantizar que el código generado con asistencia de IA sea
mantenible y comprensible sin depender de la herramienta que lo produjo

Regl El código generado o asistido por Inteligencia Arti cial deberá
cumplir exactamente los mismos estándares de calidad que el código
escrito manualmente

No deberá identi carse mediante comentarios del tipo "Generado por IA",
salvo que exista un requisito legal, contractual o de auditoría

Cuando la IA proponga una solución no evidente, la decisión de aceptarla
deberá documentarse mediante los mecanismos normales de ingeniería si
introduce una arquitectura, algoritmo o compromiso técnico relevante

Es recomendabl ✅ Revisar el código antes de integrarlo

✅ Refactorizar cuando sea necesario

✅ Validar con pruebas

✅ Veri car el cumplimiento de los estándares del proyecto fi a

fi o

?

fi 5

.

e

a

.

.

.

.

.

fi .

.

Evita ❌ Con ar en el código sin revisión

❌ Mantener estructuras innecesariamente complejas porque "así lo generó
la IA"

❌ Crear comentarios indicando únicamente el origen del código

Checklis - ¿Entiendo completamente este código? - ¿Podría explicarlo
durante un Code Review? - ¿Cumple los estándares del proyecto? -
¿Existen pruebas que respalden su funcionamiento?

Indicadores de alert ⚠ Código aceptado sin revisión

⚠ Fragmentos que nadie del equipo comprende

⚠ Estilos inconsistentes dentro del mismo módulo

Automatizació Media

Las herramientas pueden detectar estilo y complejidad, pero la
comprensión sigue siendo responsabilidad del equipo

Justi cació La responsabilidad sobre el código siempre recae en el
equipo de ingeniería, independientemente de la herramienta utilizada
para producirlo .

fi fi r

t

n

n

.

a

.

.

.

.

.

.

.

Relació A

Testin

Code Revie

REV --- Code Revie

REV-00 ¿Cuál es el objetivo de un Code Review Clasi cación: 🔴
Obligatori

Objetiv Garantizar que todo cambio incorporado al sistema cumpla los
estándares de calidad, arquitectura y mantenibilidad de nidos por la
organización

Regl El propósito del Code Review no es encontrar errores de sintaxis ni
validar el funcionamiento básico del software

Su nalidad es evaluar si la solución propuesta representa una decisión
de ingeniería adecuada para el sistema

El proceso deberá centrarse en la calidad del cambio y no en la persona
que lo realizó

Durante un Code Review debe evaluars ✅ Arquitectura I

fi fi g

a

w

n

o

.

.

1

.

a

fi w

.

e

?

.

✅ Responsabilidades

✅ Legibilidad

✅ Seguridad

✅ Testing

✅ Impacto sobre el sistema

✅ Consistencia con los estándares

No es el objetiv ❌ Criticar el estilo personal del desarrollador

❌ Reescribir código únicamente por preferencias individuales

❌ Utilizar el proceso como mecanismo de evaluación personal

Checklis Antes de aprobar un cambio veri ca

-   ¿Resuelve correctamente el problema?
-   ¿Respeta la arquitectura?
-   ¿Es mantenible?
-   ¿Es consistente con el resto del proyecto?
-   ¿Puede comprenderse fácilmente?

Indicadores de alert ⚠ Comentarios subjetivos

⚠ Discusiones basadas únicamente en gustos personales

⚠ Revisiones enfocadas solo en formato .

t

.

.

.

o

.

.

a

fi

.

:

.

.

.

.

.

Automatizació No

El juicio de ingeniería requiere revisión humana

Justi cació El Code Review protege la calidad del sistema, transmite
conocimiento y reduce la deuda técnica. Su objetivo es mejorar el
software, no evaluar a las personas

Relació Todos los estándares del Engineering Handbook

REV-00 ¿Qué debo revisar primero Clasi cación: 🔴 Obligatori

Objetiv Establecer un orden consistente durante la revisión para
priorizar los aspectos de mayor impacto

Regl La revisión deberá comenzar por la arquitectura y avanzar
progresivamente hacia los detalles de implementación

Los problemas estructurales deberán resolverse antes que cuestiones
menores de estilo .

fi a

fi n

o

.

2

n

n

a

.

.

?

.

.

.

Orden recomendad 1. Arquitectur ↓

2.  Responsabilidade ↓

3.  Dependencia ↓

4.  Segurida ↓

5.  Errore ↓

6.  Testin ↓

7.  Legibilida ↓

8.  Format

Evita ❌ Comenzar revisando espacios o indentación

❌ Dedicar la mayor parte del tiempo al formato g

s

o

r

d

d

a

s

s

o

.

.

Checklis - ¿La solución arquitectónica es correcta? - ¿La distribución
de responsabilidades es adecuada? - ¿Existen riesgos técnicos? - ¿Los
detalles menores pueden revisarse después?

Indicadores de alert ⚠ Revisiones con decenas de comentarios de formato
y ninguno sobre diseño

Automatizació Alta para formato

Baja para arquitectura

Justi cació Resolver primero los problemas de diseño evita invertir
tiempo en detalles que podrían desaparecer tras una refactorización

Relació Arquitectur

CL

FU

DE

REV-00 S

N

P

fi a

n

t

3

.

n

.

n

a

.

.

¿Cómo debo escribir un comentario durante una revisión Clasi cación: 🔴
Obligatori

Objetiv Promover revisiones constructivas que faciliten la mejora
continua y el intercambio de conocimiento

Regl Los comentarios deberán centrarse en el código, explicar el motivo
de la observación y, cuando sea posible, proponer una alternativa o
formular una pregunta que invite a la re exión

El lenguaje utilizado deberá ser profesional, respetuoso y orientado a
la mejora del software

Es recomendabl ✅ Explicar el riesgo

✅ Citar el estándar aplicable

✅ Proponer alternativas

✅ Formular preguntas cuando existan varias soluciones válidas

Evita ❌

``` text
"No me gusta.
```

❌ fi a

r

o

.

``` text
"
```

.

.

e

?

a

.

.

fl .

.

``` text
"Está mal.
```

❌

``` text
"Yo lo hago diferente.
```

Es preferibl

``` text
"Esta implementación parece mezclar responsabilidades (CLS-002). ¿Crees que separar la lógica
```

facilitaría su mantenimiento?

Checklis - ¿El comentario explica el motivo? - ¿Hace referencia a un
criterio objetivo? - ¿Ayuda al autor a mejorar?

Indicadores de alert ⚠ Comentarios subjetivos

⚠ Discusiones personales

⚠ Falta de justi cación

Automatizació No

La comunicación efectiva requiere criterio humano

Justi cació Una buena revisión mejora tanto el código como el
conocimiento compartido del equipo. Comentarios vagos o personales
generan fricción y aportan poco valor .

fi

``` text
"
```

t

fi n

e

``` text
"
```

n

.

.

.

``` text
"
```

a

.

.

Relació Comunicación Técnic

Engineering Cultur

REV-00 ¿Cuándo debo solicitar cambios Clasi cación: 🔴 Obligatori

Objetiv De nir criterios consistentes para decidir cuándo un cambio no
debe integrarse todavía

Regl Deberán solicitarse cambios cuando el código incumpla un estándar
obligatorio, introduzca riesgos relevantes o reduzca la calidad del
sistema

Las observaciones relacionadas con preferencias personales o
recomendaciones menores no deberán bloquear la integración si no
comprometen la calidad del software

Debe bloquear el merg ✅ Riesgos de seguridad

✅ Violaciones arquitectónicas

✅ Errores funcionales

✅ Ausencia de pruebas obligatorias fi fi a

n

o

4

e

a

.

.

a

.

e

.

.

?

.

.

✅ Exposición de secretos

✅ Deuda técnica crítica

Normalmente NO debe bloquea 🟡 Nombres discutibles

🟡 Posibles optimizaciones futuras

🟡 Diferencias menores de estilo

🟡 Refactorizaciones opcionales

Checklis - ¿El problema compromete el sistema? - ¿Existe riesgo para
producción? - ¿Incumple una regla obligatoria? - ¿Puede resolverse
posteriormente sin afectar la calidad?

Indicadores de alert ⚠ Merges bloqueados por cuestiones estéticas

⚠ Falta de criterios comunes entre revisores

Automatizació Media

Las herramientas pueden bloquear reglas objetivas; las decisiones de
diseño requieren revisión humana .

.

t

n

.

.

.

a

.

.

.

.

.

r

Justi cació Bloquear una integración debe reservarse para problemas que
realmente comprometan la calidad, la seguridad o la mantenibilidad. De
lo contrario, el proceso pierde credibilidad y se vuelve
innecesariamente lento

Relació Todos los estándares

REV-00 ¿Cuándo puedo aprobar un cambio Clasi cación: 🔴 Obligatori

Objetiv De nir las condiciones mínimas para integrar un cambio al
repositorio principal

Regl Un cambio podrá aprobarse cuando cumpla los estándares obligatorios
de nidos por la organización, los riesgos identi cados hayan sido
atendidos y el revisor tenga con anza razonable en que la modi cación
mantiene o mejora la calidad del sistema

La aprobación no implica que el código sea perfecto, sino que cumple el
nivel de calidad esperado para ser integrado

Antes de aproba Debe cumplirse

✅ Arquitectura consistente fi fi a

fi n

o

:

5

n

.

.

fi r

.

.

a

fi fi .

?

.

fi

✅ Responsabilidades claras

✅ Sin problemas críticos de seguridad

✅ Manejo adecuado de errores

✅ Pruebas su cientes

✅ Documentación actualizada cuando corresponda

✅ Sin deuda técnica crítica introducida por el cambio

Checklis - ¿Firmaría personalmente este cambio para producción? -
¿Entiendo completamente la solución propuesta? - ¿Los riesgos residuales
son aceptables? - ¿El bene cio del cambio supera su complejidad?

Indicadores de alert ⚠ Aprobar cambios que el propio revisor no
comprende

⚠ Aprobar "para avanzar rápido" dejando problemas críticos abiertos

Automatizació Baja

La decisión nal requiere juicio de ingeniería

Justi cació La aprobación es un compromiso profesional con la calidad
del software. Debe basarse en evidencia técnica y no únicamente en el
paso de veri caciones automáticas .

fi fi fi t

fi n

.

n

.

a

.

.

.

.

fi .

.

.

.

Relació CI/C

Testin

Arquitectur

TST --- Desarrollo Orientado a Prueba

TST-00 ¿Cuándo debo escribir pruebas Clasi cación: 🔴 Obligatori

Objetiv Garantizar que las funcionalidades críticas cuenten con
evidencia veri cable de su correcto funcionamiento

Regl Todo cambio deberá incorporar las pruebas necesarias para demostrar
que el comportamiento esperado funciona correctamente y que no se
introducen regresiones relevantes

La profundidad y el tipo de pruebas dependerán del impacto del cambio y
de la estrategia de nida en la Arquitectura de Testing

Es obligatorio cuand ✅ Se incorpora una nueva funcionalidad fi D

fi g

a

a

n

o

1

.

a

o

.

.

?

fi .

s

✅ Se modi ca una regla de negocio

✅ Se corrige un defecto

✅ Se cambia un contrato público

Puede no ser necesario cuand 🟡 Cambios exclusivamente documentales

🟡 Refactorizaciones internas completamente cubiertas por pruebas
existentes

🟡 Cambios de formato sin impacto funcional

Checklis Antes de nalizar un cambio veri ca

-   ¿Existe evidencia de que funciona?
-   ¿Las pruebas cubren el comportamiento esperado?
-   ¿El cambio puede romper funcionalidades existentes?
-   ¿La cobertura es proporcional al riesgo?

Indicadores de alert ⚠ Cambios grandes sin nuevas pruebas

⚠ Corrección de errores sin prueba que reproduzca el problema

⚠ Funcionalidades críticas sin evidencia veri cable

Automatizació Alta

Puede integrarse con CI/CD y políticas de cobertura .

fi fi t

n

.

a

fi .

:

.

.

.

fi .

o

.

.

.

.

Justi cació Las pruebas proporcionan evidencia objetiva del
comportamiento del sistema y reducen el riesgo de regresiones durante la
evolución del software

Relació Arquitectura de Testin

CI/C

RE

TST-00 ¿Qué debe probar una prueba Clasi cación: 🔴 Obligatori

Objetiv Enfocar las pruebas en el comportamiento observable del sistema
y no en los detalles internos de implementación

Regl Las pruebas deberán veri car el comportamiento esperado desde la
perspectiva del contrato o de la funcionalidad

No deberán depender innecesariamente de detalles internos cuya modi
cación no altere el resultado esperado

Es recomendable proba V

D

fi a

fi n

o

2

.

.

n

.

g

fi a

r

.

?

fi

✅ Reglas del negocio

✅ Contratos públicos

✅ Casos límite

✅ Escenarios de error

✅ Comportamientos críticos

Evita ❌ Probar variables internas

❌ Depender de la estructura privada de una clase

❌ Veri car detalles que pueden cambiar sin afectar la funcionalidad

Checklis - ¿La prueba valida el comportamiento? - ¿Podría sobrevivir a
una refactorización? - ¿Representa un escenario real?

Indicadores de alert ⚠ Pruebas que fallan tras una refactorización sin
cambios funcionales

⚠ Pruebas excesivamente acopladas a la implementación

Automatizació No

La selección del comportamiento requiere criterio del desarrollador .

fi r

t

.

.

.

.

n

.

.

a

.

.

.

.

.

Justi cació Una prueba valiosa protege el comportamiento del sistema.
Cuando depende demasiado de la implementación, se vuelve frágil y pierde
utilidad

Relació Arquitectura de Testin

CL

FU

TST-00 ¿Cómo debo nombrar una prueba Clasi cación: 🟡 Heurístic

Objetiv Facilitar la comprensión inmediata del propósito de cada prueba

Regl El nombre de una prueba deberá describir claramente el escenario
evaluado y el comportamiento esperado

Cualquier integrante del equipo deberá comprender qué valida la prueba
sin necesidad de revisar su implementación

Es recomendabl S

N

fi a

fi .

n

o

3

n

.

g

e

a

.

.

?

✅ describir el escenario

✅ indicar el resultado esperado

✅ utilizar un criterio consistente en todo el proyecto

Evita ❌ test

❌ pruebaNuev

❌ validarTod

❌ caso

Checklis - ¿Describe el escenario? - ¿Describe el resultado? - ¿Es
consistente con las demás pruebas?

Indicadores de alert ⚠ Nombres genéricos

⚠ Pruebas imposibles de distinguir

Automatizació Media

Las herramientas pueden validar convenciones, no la claridad del nombre
.

1

A

r

t

o

a

.

n

;

a

;

.

.

.

Justi cació Los nombres de las pruebas forman parte de la documentación
viva del sistema y facilitan el diagnóstico cuando una prueba falla

Relació Testin

RE

TST-00 ¿Cuándo debo utilizar dobles de prueba (Mocks, Stubs o Fakes)
Clasi cación: 🟡 Heurístic

Objetiv Aislar el comportamiento que se desea veri car sin introducir
dependencias innecesarias

Regl Los dobles de prueba deberán utilizarse cuando una dependencia
externa di culte veri car el comportamiento del componente evaluado o
haga la prueba lenta, costosa o poco determinista

No deberán emplearse para ocultar problemas de diseño ni para reemplazar
indiscriminadamente todas las colaboraciones

Es recomendabl ✅ Servicios externos V

fi g

a

fi n

o

4

n

.

.

e

a

.

fi ?

fi fi .

.

✅ APIs

✅ Sistemas de archivos

✅ Correo electrónico

✅ Integraciones

Evita ❌ Simular todo el sistema

❌ Crear pruebas que únicamente validen el comportamiento del mock

❌ Utilizar mocks para compensar un alto acoplamiento

Checklis - ¿La dependencia externa aporta ruido a la prueba? - ¿El doble
simpli ca el escenario? - ¿La prueba sigue representando un caso real?

Indicadores de alert ⚠ Más código de mocks que de prueba

⚠ Pruebas extremadamente difíciles de comprender

Automatizació No

La decisión depende del contexto de diseño .

r

.

t

fi .

.

n

.

.

a

.

.

.

.

.

Justi cació Los dobles de prueba son una herramienta para aislar
comportamientos, no un objetivo. Su uso excesivo puede producir pruebas
arti ciales y difíciles de mantener

Relació Arquitectura de Testin

DE

TST-00 ¿Cuándo una prueba está lista para integrarse Clasi cación: 🔴
Obligatori

Objetiv De nir los criterios mínimos de calidad para aceptar una prueba
dentro del repositorio

Regl Una prueba estará lista para integrarse cuando sea con able,
repetible, comprensible y aporte evidencia útil sobre el comportamiento
del sistema

Una prueba que falla aleatoriamente, depende del entorno o requiere
intervención manual no deberá incorporarse como parte de la validación
automática

Debe se ✅ Determinista fi P

fi a

fi n

o

r

5

.

n

?

g

a

fi .

fi .

.

.

✅ Repetible

✅ Comprensible

✅ Independiente

✅ Mantenible

Evita ❌ Pruebas intermitentes ( aky tests)

❌ Dependencias del reloj del sistema sin control

❌ Dependencias de datos compartidos

❌ Intervención manual

Checklis - ¿Produce siempre el mismo resultado bajo las mismas
condiciones? - ¿Puede ejecutarse automáticamente? - ¿Es fácil comprender
qué valida? - ¿Aporta con anza al equipo?

Indicadores de alert ⚠ Pruebas que "a veces fallan"

⚠ Equipos acostumbrados a ignorar fallos del pipeline

⚠ Reejecutar varias veces hasta que pase

Automatizació r

fi .

t

.

.

.

n

.

fl

.

a

.

.

.

.

.

Alta

Los pipelines pueden detectar estabilidad, tiempos de ejecución y
resultados repetitivos

Justi cació Una prueba inestable reduce la con anza en toda la suite de
validación. Cuando el equipo deja de creer en las pruebas, pierde una de
sus principales herramientas de aseguramiento de calidad

Relació Arquitectura de Testin

CI/C

RE

MNT --- Mantenibilida

MNT-00 ¿Cuándo debo refactorizar Clasi cación: 🔴 Obligatori

Objetiv Mantener el código simple, comprensible y fácil de evolucionar
mediante mejoras continuas de su estructura interna

Regl La refactorización deberá realizarse cuando mejore la
mantenibilidad del software sin alterar su comportamiento observable V

.

D

fi a

fi n

o

1

n

.

g

.

a

fi d

?

.

.

No deberá utilizarse como justi cación para introducir cambios
funcionales no relacionados

Siempre que sea posible, la refactorización deberá estar respaldada por
pruebas automatizadas

Es recomendable refactorizar cuand ✅ Se identi ca duplicación signi
cativa

✅ Una clase concentra demasiadas responsabilidades

✅ Un método resulta difícil de comprender

✅ El cambio actual sería considerablemente más sencillo con una mejora
previa de la estructura

Evita ❌ Refactorizar todo el módulo para corregir un error menor

❌ Mezclar refactorización con nuevas funcionalidades sin una justi
cación clara

❌ Reescribir componentes estables únicamente por preferencias
personales

Checklis Antes de refactorizar veri ca

-   ¿El comportamiento permanecerá igual?
-   ¿Existen pruebas su cientes?
-   ¿El bene cio supera el riesgo?
-   ¿La mejora facilita cambios futuros?

Indicadores de alert ⚠ Refactorizaciones masivas sin necesidad r

fi .

fi t

fi fi :

fi a

fi

.

.

.

.

o

.

fi .

.

.

.

⚠ Cambios funcionales ocultos dentro de una refactorización

⚠ Ausencia de pruebas antes de modi car componentes críticos

Automatizació Media

Las herramientas pueden sugerir oportunidades, pero la decisión requiere
criterio de ingeniería

Justi cació La refactorización preserva la capacidad de evolución del
software. Retrasarla inde nidamente incrementa la deuda técnica;
realizarla sin criterio aumenta el riesgo operativo

Relació CL

FU

Testin

RE

MNT-00 ¿Cómo identi car deuda técnica Clasi cación: 🟡 Heurístic

Objetiv Detectar oportunamente decisiones de implementación que
incrementan el costo futuro de mantenimiento S

V

N

fi g

.

fi n

o

.

2

n

n

a

fi fi .

.

?

.

fi .

Regl Se considerará deuda técnica toda decisión que reduzca la calidad
del software a cambio de un bene cio inmediato y que requiera una
corrección futura identi cable

No toda solución temporal constituye una mala práctica; la deuda técnica
deberá ser consciente, documentada y gestionada

Señales comune ⚠ Duplicación

⚠ Complejidad creciente

⚠ Dependencias innecesarias

⚠ Soluciones temporales permanentes

⚠ Código difícil de probar

⚠ Violaciones conocidas a la arquitectura

Checklis - ¿La solución es temporal? - ¿Existe una alternativa mejor? -
¿Está documentada? - ¿Existe un plan para eliminarla?

Indicadores de alert ⚠ Comentarios como

// TODO arreglar despué fi a

t

.

:

s

.

.

.

.

a

s

.

.

fi .

// solución tempora

que permanecen durante meses

Automatizació Media

Las herramientas detectan síntomas, no la deuda en sí

Justi cació La deuda técnica no desaparece sola. Gestionarla
explícitamente permite tomar decisiones conscientes sobre el equilibrio
entre velocidad y calidad

Relació RE

Arquitectur

Engineering Managemen

MNT-00 ¿Cuándo debo eliminar código Clasi cación: 🔴 Obligatori

Objetiv Reducir la complejidad del sistema eliminando componentes que ya
no aportan valor

Regl V

fi .

a

fi a

n

o

3

n

n

t

l

a

.

.

.

?

.

El código que ha dejado de cumplir una función deberá eliminarse una vez
que exista evidencia su ciente de que no será utilizado

Mantener código obsoleto incrementa la complejidad, di culta la
comprensión y aumenta el costo de mantenimiento

Es recomendable elimina ✅ Funcionalidades retiradas

✅ Flags expiradas

✅ Métodos sin uso

✅ Componentes reemplazados

Evita ❌ Conservar código comentado "por si acaso"

❌ Mantener implementaciones antiguas inde nidamente

❌ Duplicar funcionalidades activas

Checklis - ¿Existe evidencia de que ya no se utiliza? - ¿Las pruebas
siguen siendo válidas? - ¿La documentación fue actualizada? - ¿El cambio
afecta compatibilidad?

Indicadores de alert ⚠ Grandes bloques comentados

⚠ Archivos marcados como "old", "backup" o "nuevo2" fi r

t

.

.

.

.

a

.

.

.

.

r

fi .

fi .

.

⚠ Código muerto que nadie reconoce como propio

Automatizació Alta

El análisis estático puede detectar referencias y código no utilizado

Justi cació Cada línea de código requiere mantenimiento. Eliminar
aquello que ya no aporta valor simpli ca el sistema y reduce el riesgo
de errores futuros

Relació Testin

RE

Arquitectur

MNT-00 ¿Cómo identi car código muerto Clasi cación: 🟡 Heurístic

Objetiv Detectar componentes que permanecen en el sistema sin participar
en su funcionamiento

Regl V

.

fi g

a

fi a

n

o

4

n

n

a

fi .

.

.

?

.

fi

Todo componente que no pueda ser alcanzado desde los ujos activos del
sistema deberá revisarse para determinar si puede eliminarse

La ausencia de referencias no siempre implica que el código esté muerto;
deberá considerarse el uso mediante re exión, con guración, carga
dinámica u otros mecanismos de nidos por la arquitectura

Señales comune ⚠ Métodos nunca invocados

⚠ Clases sin referencias

⚠ Endpoints obsoletos

⚠ Recursos inaccesibles

Checklis - ¿Existe alguna referencia válida? - ¿Forma parte de una
funcionalidad activa? - ¿Hay evidencia de uso reciente? - ¿Puede
eliminarse de forma segura?

Indicadores de alert ⚠ Directorios completos sin modi caciones durante
años

⚠ Componentes sin cobertura de pruebas ni referencias

Automatizació Muy alta

El análisis estático puede detectar gran parte del código potencialmente
muerto .

.

t

fl n

.

.

.

s

fi .

a

fi

.

.

fl .

fi .

Justi cació El código muerto incrementa el tamaño del sistema y di culta
distinguir qué componentes siguen siendo relevantes

Relació Testin

CI/C

RE

MNT-00 ¿Cuándo debo duplicar código en lugar de reutilizarlo Clasi
cación: 🟡 Heurístic

Objetiv Evitar abstracciones prematuras que incrementen el acoplamiento
y di culten la evolución independiente de distintas funcionalidades

Regl La reutilización deberá introducirse cuando exista una necesidad
comprobada y estable

No deberá crearse una abstracción únicamente porque dos fragmentos de
código sean similares

En determinados escenarios, una duplicación temporal y consciente puede
ser preferible a una abstracción prematura V

D

fi g

a

fi n

o

.

5

n

.

?

a

.

fi fi .

.

Es recomendable reutilizar cuand ✅ La lógica representa un concepto
común y estable

✅ Las reglas evolucionarán conjuntamente

✅ La abstracción simpli ca el diseño

Puede aceptarse una duplicación temporal cuand 🟡 Los casos aún
evolucionan de forma independiente

🟡 No existe su ciente conocimiento para de nir una buena abstracción

🟡 La reutilización introduciría un acoplamiento arti cial

Evita ❌ Crear utilidades genéricas sin un propósito claro

❌ Compartir código únicamente para reducir líneas

❌ Forzar componentes comunes que di culten cambios futuros

Checklis - ¿La similitud representa realmente el mismo concepto? -
¿Ambos casos evolucionarán juntos? - ¿La abstracción reduce o aumenta la
complejidad? - ¿Estoy optimizando demasiado pronto?

Indicadores de alert ⚠ Clases Utils, Common, Shared con
responsabilidades heterogéneas r

t

fi fi a

.

fi .

fi

.

.

fi o

.

.

.

.

.

.

o

⚠ Cambios en una funcionalidad rompen otra debido a una abstracción
compartida

Automatizació Baja

Las herramientas detectan duplicación, pero no pueden decidir si una
abstracción es adecuada

Justi cació Eliminar toda duplicación no siempre mejora el diseño. Una
abstracción incorrecta puede generar más complejidad que una duplicación
controlada y temporal

Relació CL

FU

DE

Arquitectur

SEC --- Desarrollo Seguro (Secure Coding

SEC-00 ¿Debo asumir que toda entrada es con able Clasi cación: 🔴
Obligatori

Objetiv S

N

P

.

fi fi a

n

o

1

n

n

a

.

fi .

)

?

.

Garantizar que el sistema trate toda información proveniente del
exterior como potencialmente inválida, maliciosa o inesperada

Regl Toda entrada deberá considerarse no con able hasta que haya sido
validada de acuerdo con las reglas del sistema

Esta regla aplica independientemente del origen de los datos

La con anza no depende de quién envía la información, sino de que haya
sido veri cada

Se consideran entrada ✅ Solicitudes HTTP

✅ APIs

✅ Formularios

✅ Archivos

✅ Bases de datos externas

✅ Colas

✅ Servicios de terceros

✅ Variables de entorno

✅ Parámetros internos provenientes de otros sistemas

Nunca asumi ❌ Que el frontend ya validó

❌ Que un servicio interno siempre enviará datos correctos fi a

.

.

.

.

.

r

.

.

.

.

.

.

s

fi .

.

.

fi .

❌ Que la base de datos contiene únicamente información válida

Checklis Antes de utilizar un dato veri ca

-   ¿Proviene de una fuente externa?
-   ¿Fue validado?
-   ¿Puede contener información inesperada?
-   ¿Existe una política de validación para este tipo de dato?

Indicadores de alert ⚠ Datos utilizados directamente

⚠ Conversión automática sin validación

⚠ Con anza implícita en el cliente

Automatizació Media

Las herramientas pueden detectar algunos ujos inseguros, pero no todas
las validaciones requeridas

Justi cació La mayoría de los ataques explotan la con anza excesiva en
datos externos. Validar todas las entradas reduce signi cativamente la
super cie de ataque

Relació ER

CF G

R

.

fi fi .

n

t

n

fi n

fi a

:

.

.

.

fi fl fi

.

.

Arquitectura Backen

SEC-00 ¿Cómo debo validar información Clasi cación: 🔴 Obligatori

Objetiv Aceptar únicamente datos que cumplan las reglas de nidas por el
sistema

Regl La validación deberá basarse en listas de valores permitidos
(allowlists) siempre que sea posible

Rechazar únicamente ciertos valores conocidos (blocklists) no
proporciona protección su ciente frente a entradas inesperadas

La validación deberá realizarse tan cerca como sea posible del punto de
entrada, sin sustituir las validaciones propias del dominio

Es recomendable valida ✅ Tipo

✅ Longitud

✅ Formato

✅ Rango

✅ Conjunto de valores permitidos

✅ Reglas del dominio en la capa correspondiente fi a

.

.

o

.

.

2

d

.

a

.

.

r

.

fi ?

.

fi .

Evita ❌ Expresiones regulares excesivamente permisivas

❌ Validaciones parciales

❌ Con ar solo en JavaScript del navegador

Checklis - ¿Qué formato espero? - ¿Qué valores son válidos? - ¿Existe un
límite máximo? - ¿Estoy aceptando más de lo necesario?

Indicadores de alert ⚠ Campos aceptan cualquier contenido

⚠ Validaciones diferentes entre distintos puntos del sistema

Automatizació Alta

Puede integrarse con análisis estático y pruebas automatizadas

Justi cació Una validación basada en lo permitido es más robusta que una
basada únicamente en bloquear casos conocidos

Relació .

fi fi r

n

t

.

n

n

.

a

.

.

.

.

.

Testin

ER

SEC-00 ¿Cómo debo proteger información sensible Clasi cación: 🔴
Obligatori

Objetiv Garantizar el tratamiento adecuado de información cuya
exposición pueda afectar a personas, organizaciones o sistemas

Regl La información sensible deberá protegerse durante todo su ciclo de
vida: almacenamiento, procesamiento, transmisión y registro

El desarrollador deberá minimizar el acceso, exposición y permanencia de
estos datos en memoria, registros y respuestas

Información sensibl ✅ Credenciales

✅ Tokens

✅ Datos personales

✅ Información nanciera

✅ Secretos criptográ cos

✅ Información médica R

fi g

a

.

o

3

.

fi .

fi .

.

.

.

a

.

e

.

?

Evita ❌ Imprimir datos sensibles en logs

❌ Exponerlos en errores

❌ Enviarlos innecesariamente entre componentes

❌ Conservarlos más tiempo del necesario

Checklis - ¿Es realmente necesario acceder a este dato? - ¿Puede
anonimizarse? - ¿Debe cifrarse? - ¿Puede omitirse completamente?

Indicadores de alert ⚠ Objetos completos serializados en logs

⚠ Respuestas que contienen más información de la necesaria

Automatizació Alta

Existen herramientas para detectar datos sensibles en código y registros

Justi cació Reducir la exposición de información sensible disminuye el
impacto potencial de un incidente de seguridad .

fi r

.

t

n

n

.

a

.

.

.

.

.

.

Relació LO

CF

ER

SEC-00 ¿Cómo debo consultar la base de datos de forma segura Clasi
cación: 🔴 Obligatori

Objetiv Evitar vulnerabilidades derivadas de consultas construidas de
forma insegura

Regl Las consultas deberán utilizar mecanismos seguros de
parametrización o abstracción de nidos por la tecnología empleada

Nunca deberán construirse consultas concatenando directamente datos
provenientes de entradas externas

Es recomendabl ✅ Consultas parametrizadas

✅ ORM cuando resulte apropiado

✅ Procedimientos de nidos por la arquitectura G

R

G

fi a

.

n

o

4

fi e

.

?

a

.

.

.

.

fi

Evita ❌ Concatenar cadenas

❌ Construcción manual de SQL con datos externos

❌ Escapar manualmente como única medida de protección

Checklis - ¿La consulta está parametrizada? - ¿Existe riesgo de
inyección? - ¿La tecnología proporciona un mecanismo más seguro?

Indicadores de alert ⚠ Concatenación de parámetros

⚠ Construcción dinámica de SQL

Automatizació Muy alta

Las herramientas SAST detectan este tipo de vulnerabilidades con gran
precisión

Justi cació La parametrización reduce signi cativamente el riesgo de
inyección y mejora la consistencia de acceso a datos

Relació fi r

.

n

t

.

n

n

.

a

fi .

.

.

.

.

Arquitectura Backen

Testin

SEC-00 ¿Cómo debo diseñar pensando en el principio de mínimo privilegio
Clasi cación: 🔴 Obligatori

Objetiv Limitar el acceso a recursos únicamente a lo estrictamente
necesario para cumplir la responsabilidad del componente

Regl Todo componente deberá operar con el menor conjunto posible de
permisos, datos y capacidades

El acceso a recursos deberá concederse únicamente cuando sea necesario y
retirarse cuando deje de serlo

Aplica ✅ Usuarios

✅ Servicios

✅ APIs

✅ Procesos

✅ Bases de datos fi g

a

.

.

a

.

o

.

.

.

5

.

d

a

.

?

✅ Archivos

Evita ❌ Permisos administrativos por defecto

❌ Acceso global innecesario

❌ Compartir credenciales entre componentes

Checklis - ¿Qué permisos necesita realmente? - ¿Puede operar con menos
privilegios? - ¿Existe una separación adecuada de responsabilidades? -
¿Los permisos son revisables y revocables?

Indicadores de alert ⚠ Cuentas con privilegios excesivos

⚠ Componentes que acceden a recursos que nunca utilizan

Automatizació Media

Puede veri carse parcialmente mediante herramientas de análisis y
políticas de infraestructura

Justi cació Reducir los privilegios limita el impacto potencial de
errores, vulnerabilidades o accesos no autorizados .

fi r

fi .

.

t

n

n

.

a

.

.

.

.

.

Relació Arquitectur

IA

Complianc

PER --- Rendimiento (Performance

PER-00 ¿Cuándo debo preocuparme por el rendimiento Clasi cación: 🔴
Obligatori

Objetiv Tomar decisiones de rendimiento basadas en evidencia y en el
impacto real sobre el sistema

Regl El rendimiento deberá considerarse desde el diseño para evitar
decisiones claramente ine cientes, pero las optimizaciones especí cas
deberán realizarse únicamente cuando exista evidencia objetiva de un
problema

No deberá sacri carse la claridad, mantenibilidad o corrección del
software por optimizaciones no justi cadas

Es recomendabl ✅ Diseñar algoritmos razonables M

fi fi a

fi e

a

n

o

.

fi 1

e

?

a

.

.

fi )

.

✅ Evitar ine ciencias evidentes

✅ Medir antes de optimizar

Evita ❌ Optimizar por intuición

❌ Introducir complejidad sin necesidad

❌ Reescribir código únicamente porque "podría ser más rápido"

Checklis - ¿Existe un problema medido? - ¿La optimización aporta un bene
cio relevante? - ¿Incrementa signi cativamente la complejidad? - ¿Se
documentó la decisión cuando corresponde?

Indicadores de alert ⚠ Cambios motivados únicamente por percepción

⚠ Código mucho más complejo sin bene cios demostrables

Automatizació Baja

La decisión requiere métricas y contexto

Justi cació .

fi r

fi t

fi n

n

.

.

a

fi .

.

.

fi

.

.

.

La optimización prematura incrementa la complejidad del software y rara
vez mejora el desempeño donde realmente importa

Relació MN

RE

Arquitectur

PER-00 ¿Qué debo medir antes de optimizar Clasi cación: 🔴 Obligatori

Objetiv Basar las decisiones de optimización en información veri cable

Regl Antes de implementar una optimización deberá identi carse el
comportamiento que representa el cuello de botella mediante métricas,
per les de ejecución, monitoreo o evidencia equivalente

Es recomendable medi ✅ Tiempo de respuesta

✅ Uso de CPU

✅ Uso de memoria V

T

fi a

a

n

o

.

2

.

.

a

r

.

fi fi fi .

?

.

✅ Latencia

✅ Cantidad de consultas

✅ Operaciones de entrada y salida

Evita ❌ Optimizar componentes que no representan el problema principal

❌ Basarse únicamente en pruebas informales

Checklis - ¿Qué métrica demuestra el problema? - ¿Dónde ocurre el cuello
de botella? - ¿Cómo se medirá la mejora? - ¿Existe una línea base?

Indicadores de alert ⚠ "Creo que aquí está el problema.

⚠ No existen métricas antes ni después del cambio

Automatizació Alta

Las herramientas de monitoreo y pro ling proporcionan esta información

Justi cació .

fi r

.

t

n

n

.

a

.

``` text
"
```

fi

.

.

.

.

No puede mejorarse aquello que no se mide. Las optimizaciones sin
evidencia suelen atacar síntomas y no las causas reales

Relació Observabilida

LO

CI/C

PER-00 ¿Cómo debo tratar operaciones costosas Clasi cación: 🟡 Heurístic

Objetiv Reducir el impacto de operaciones que consumen una cantidad
signi cativa de recursos

Regl Las operaciones con alto costo computacional, de red,
almacenamiento o acceso a recursos externos deberán identi carse y
ejecutarse únicamente cuando sean necesarias

Siempre que sea posible, deberá evitarse repetir operaciones costosas
cuyo resultado ya sea conocido o pueda reutilizarse de forma segura

Ejemplos de operaciones costosa ✅ Consultas a bases de datos

✅ Llamadas a servicios externos G

D

fi a

n

o

d

3

fi a

.

.

.

.

s

fi .

?

.

✅ Lectura y escritura de archivos

✅ Procesamiento masivo de datos

✅ Operaciones criptográ cas intensivas

Evita ❌ Repetir la misma consulta innecesariamente

❌ Invocar servicios externos dentro de ciclos cuando puede evitarse

❌ Recalcular resultados sin necesidad

Checklis - ¿La operación realmente debe ejecutarse? - ¿Puede
reutilizarse el resultado? - ¿Existe una alternativa más e ciente? - ¿El
costo está justi cado?

Indicadores de alert ⚠ Múltiples consultas idénticas

⚠ Llamadas repetitivas a la misma API

⚠ Procesamiento redundante

Automatizació Media

Algunas herramientas detectan patrones de repetición, pero requieren
interpretación .

r

t

fi n

fi fi .

a

.

.

.

.

.

.

.

.

.

Justi cació Muchas degradaciones de rendimiento provienen de operaciones
costosas ejecutadas innecesariamente, no de algoritmos complejos

Relació Arquitectur

DE

PER-00 ¿Cuándo debo utilizar caché Clasi cación: 🟡 Heurístic

Objetiv Mejorar el rendimiento reutilizando información cuyo costo de
obtención sea signi cativamente mayor que su almacenamiento temporal

Regl El uso de caché deberá justi carse mediante evidencia de que reduce
un problema de rendimiento relevante y que el riesgo de servir
información desactualizada es aceptable para el caso de uso

Toda estrategia de caché deberá de nir claramente cómo se actualiza,
invalida y supervisa

Es recomendable considerar caché cuand ✅ Los datos cambian poco P

fi a

fi a

.

n

o

4

n

fi .

a

fi .

.

?

o

fi .

✅ La obtención de la información es costosa

✅ Existen muchas lecturas y pocas escrituras

Evita ❌ Usar caché como solución por defecto

❌ Almacenar información inde nidamente sin una política de expiración o
invalidación

❌ Ocultar problemas de diseño con caché

Checklis - ¿Cuál es el bene cio esperado? - ¿Qué estrategia de
invalidación se utilizará? - ¿Qué ocurre si la información queda
desactualizada? - ¿Cómo se monitoreará su efectividad?

Indicadores de alert ⚠ Cachés que nadie sabe cómo limpiar

⚠ Datos inconsistentes entre componentes

Automatizació Media

Las herramientas pueden medir tasas de aciertos (hit rate) y expiración,
pero el diseño sigue siendo una decisión de ingeniería

Justi cació .

fi r

t

fi n

n

a

fi .

.

.

.

.

.

.

.

La caché puede mejorar signi cativamente el rendimiento, pero también
introduce complejidad y riesgos de consistencia. Debe utilizarse de
manera consciente y controlada

Relació Arquitectur

CF

MN

PER-00 ¿Cómo debo equilibrar rendimiento y mantenibilidad Clasi cación:
🔴 Obligatori

Objetiv Tomar decisiones de optimización que mejoren el desempeño sin
comprometer innecesariamente la calidad del software

Regl Cuando existan varias soluciones funcionalmente equivalentes,
deberá preferirse aquella que ofrezca el mejor equilibrio entre
rendimiento, claridad, mantenibilidad y complejidad

Las optimizaciones que incrementen signi cativamente la di cultad de
comprensión deberán justi carse y documentarse cuando aporten un bene
cio relevante

Es recomendabl ✅ Favorecer soluciones simples G

T

fi fi a

a

n

o

5

.

e

a

fi ?

.

fi fi fi .

.

.

✅ Documentar optimizaciones complejas

✅ Revisar periódicamente si siguen siendo necesarias

Evita ❌ Sacri car legibilidad por mejoras marginales

❌ Mantener código altamente optimizado cuando el problema ya no existe

Checklis - ¿El bene cio compensa la complejidad añadida? - ¿Otro
desarrollador comprenderá esta implementación? - ¿La optimización sigue
siendo necesaria? - ¿Existe documentación su ciente?

Indicadores de alert ⚠ Código difícil de entender con comentarios como
"No modi car, está optimizado"

⚠ Optimizaciones heredadas cuya utilidad ya nadie puede demostrar

Automatizació Baja

El equilibrio entre rendimiento y mantenibilidad requiere criterio
profesional

Justi cació El objetivo del desarrollo no es producir el código más
rápido posible, sino el sistema más sostenible y e ciente para las
necesidades reales del negocio .

fi r

fi fi fi t

n

n

fi a

.

.

.

.

fi .

.

.

.

Relació MN

DO

RE

API --- Diseño de APIs y Contrato

API-00 ¿Qué es un contrato de software Clasi cación: 🔴 Obligatori

Objetiv Diseñar interfaces estables, comprensibles y predecibles entre
componentes o sistemas

Regl Toda interfaz pública deberá considerarse un contrato

Una vez publicada, otros componentes pueden depender de ella. Cualquier
modi cación deberá evaluarse considerando el impacto sobre los
consumidores

El contrato incluye no solo los datos intercambiados, sino también el
comportamiento esperado, las restricciones y los posibles errores

Un contrato puede se ✅ API HTTP

✅ Evento V

C

T

fi a

.

n

o

.

1

a

r

.

.

.

?

s

fi .

✅ Cola de mensajes

✅ Biblioteca pública

✅ Servicio interno

✅ Interfaz entre módulos

Evita ❌ Cambiar contratos sin evaluar el impacto

❌ Suponer que un consumidor se adaptará automáticamente

Checklis - ¿Quién consume este contrato? - ¿Qué dependencias generará? -
¿Qué ocurrirá si cambia? - ¿Existe documentación su ciente?

Indicadores de alert ⚠ Cambios frecuentes en interfaces públicas

⚠ Consumidores afectados inesperadamente

Automatizació Baja

La identi cación de contratos requiere conocimiento del contexto

Justi cació .

fi r

fi t

n

.

.

.

n

fi .

a

.

.

.

.

.

Los contratos representan compromisos entre componentes. Diseñarlos con
estabilidad reduce el costo de integración y evolución del sistema

Relació DO

RE

Arquitectur

API-00 ¿Cómo debo diseñar un contrato Clasi cación: 🔴 Obligatori

Objetiv Crear interfaces fáciles de comprender, utilizar y mantener

Regl Todo contrato deberá exponer únicamente la información necesaria
para cumplir su propósito

Deberá ser consistente con las convenciones de nidas por la arquitectura
y minimizar el conocimiento que el consumidor necesita para utilizarlo
correctamente

Es recomendabl ✅ Nombres claros

✅ Estructuras consistentes

✅ Respuestas predecibles V

C

fi a

a

n

o

2

.

e

.

.

a

.

fi .

?

.

.

✅ Comportamiento uniforme

Evita ❌ Campos ambiguos

❌ Respuestas distintas para casos equivalentes

❌ Convenciones diferentes entre APIs similares

Checklis - ¿Es consistente? - ¿Es fácil de entender? - ¿Expone solo lo
necesario? - ¿Mantiene un comportamiento uniforme?

Indicadores de alert ⚠ Interfaces difíciles de explicar

⚠ Consumidores con múltiples excepciones para utilizar la API

Automatizació Media

Las herramientas pueden validar esquemas, pero no la claridad del diseño

Justi cació La simplicidad y consistencia reducen el costo de
integración y disminuyen la probabilidad de errores en los consumidores
.

fi r

t

n

.

n

.

.

a

.

.

.

.

.

Relació NA

DO

RE

API-00 ¿Cuándo puedo modi car un contrato Clasi cación: 🔴 Obligatori

Objetiv Preservar la estabilidad de los consumidores mientras el sistema
evoluciona

Regl Todo cambio en un contrato deberá clasi carse como compatible o
incompatible antes de implementarse

Los cambios incompatibles deberán plani carse, comunicarse y gestionarse
mediante la estrategia de evolución de nida por la organización

Normalmente son compatible ✅ Agregar campos opcionales

✅ Incorporar nuevos endpoints o capacidades

✅ Ampliar valores permitidos cuando no rompan el comportamiento
existente V

M

C

fi a

n

o

.

3

fi a

.

fi fi fi s

.

.

.

.

?

Normalmente son incompatible ❌ Eliminar campos utilizados por
consumidores

❌ Cambiar el signi cado de un dato

❌ Modi car tipos de datos existentes

❌ Alterar el comportamiento esperado sin una estrategia de transición

Checklis - ¿Rompe consumidores existentes? - ¿Existe evidencia de
compatibilidad? - ¿La documentación fue actualizada? - ¿Se requiere una
estrategia de migración?

Indicadores de alert ⚠ Cambios publicados sin analizar el impacto

⚠ Integraciones que dejan de funcionar tras una actualización

Automatizació Media

Las herramientas pueden comparar esquemas, pero la compatibilidad
semántica requiere análisis

Justi cació La estabilidad de los contratos protege a los consumidores y
reduce el costo de evolución del ecosistema .

fi fi .

t

n

fi n

a

.

.

.

.

s

.

.

.

Relació MN

RE

DO

API-00 ¿Cómo debo comunicar los errores de un contrato Clasi cación: 🔴
Obligatori

Objetiv Proporcionar información su ciente para que el consumidor
comprenda el problema y actúe en consecuencia

Regl Los errores expuestos por un contrato deberán ser consistentes,
comprensibles y accionables

No deberán revelar información sensible ni detalles internos de
implementación

Siempre que sea posible, deberán permitir distinguir entre errores del
consumidor, del dominio y de la infraestructura

Es recomendable inclui ✅ Código del error

✅ Descripción clara V

C

T

fi a

n

o

.

4

?

.

.

.

fi a

r

.

.

✅ Contexto relevante

✅ Posibles acciones para resolverlo

Evita ❌ Stack traces

❌ Consultas SQL

❌ Rutas del servidor

❌ Excepciones internas sin traducir

Checklis - ¿El consumidor entiende el problema? - ¿Puede actuar con la
información recibida? - ¿Existe riesgo de exponer datos sensibles?

Indicadores de alert ⚠ Mensajes genéricos como "Error desconocido"

⚠ Excepciones técnicas visibles para el cliente

Automatizació Media

Las herramientas pueden validar formatos, pero no la utilidad del
mensaje

Justi cació .

fi r

t

.

n

.

.

.

n

a

.

.

.

.

.

Los errores forman parte del contrato. Un diseño consistente reduce el
tiempo de diagnóstico y mejora la experiencia de integración

Relació ER

SE

DO

API-00 ¿Cómo debe evolucionar un contrato Clasi cación: 🔴 Obligatori

Objetiv Permitir que los contratos evolucionen sin interrumpir
innecesariamente a los consumidores

Regl La evolución de un contrato deberá favorecer la compatibilidad
hacia atrás siempre que sea razonablemente posible

Cuando una incompatibilidad sea inevitable, deberá existir un proceso
controlado que contemple la coexistencia temporal, la comunicación del
cambio, el periodo de transición y el retiro de nitivo

Es recomendabl ✅ Mantener compatibilidad cuando sea posible

✅ Publicar periodos de deprecación fi C

R

C

fi a

.

n

o

5

.

e

a

.

.

.

?

.

✅ Proporcionar guías de migración

✅ Medir el uso antes de retirar versiones

Evita ❌ Eliminar versiones activas sin previo aviso

❌ Introducir cambios incompatibles de forma silenciosa

❌ Mantener inde nidamente versiones obsoletas

Checklis - ¿Existe un plan de transición? - ¿Los consumidores fueron
informados? - ¿La documentación re eja el cambio? - ¿Se de nió una fecha
de retiro cuando corresponde?

Indicadores de alert ⚠ Múltiples versiones sin estrategia de
mantenimiento

⚠ Consumidores que desconocen la existencia de cambios

Automatizació Media

Las herramientas pueden monitorear el uso de versiones, pero la
estrategia de evolución requiere gestión y coordinación

Justi cació .

fi fi r

t

n

fi fl .

n

a

.

.

.

.

.

.

.

La evolución controlada de contratos permite innovar sin comprometer la
estabilidad del ecosistema de aplicaciones y servicios

Relació MN

DO

RE

API-00 ¿Cómo debo declarar la deprecación de una funcionalidad Clasi
cación: 🔴 Obligatori

Objetiv Permitir la evolución controlada de un contrato noti cando a los
consumidores que una funcionalidad será retirada en el futuro, sin
interrumpir inmediatamente su operación

Regl La deprecación deberá utilizarse para comunicar que una
funcionalidad sigue disponible, pero no debe emplearse en nuevos
desarrollos y será retirada de acuerdo con la política de evolución del
sistema

Toda funcionalidad deprecada deberá indicar claramente su reemplazo, el
periodo de transición y las condiciones de retiro

Una funcionalidad deprecada deb ✅ Seguir funcionando durante el periodo
de nido V

C

T

fi a

.

n

o

6

.

a

?

.

fi .

fi e

.

✅ Estar documentada como deprecada

✅ Indicar la alternativa recomendada

✅ Comunicar la fecha o condición de retiro

Evita ❌ Eliminar una funcionalidad sin previo aviso

❌ Marcar como deprecado algo que nunca será retirado

❌ Mantener funcionalidades deprecadas inde nidamente sin una estrategia
de eliminación

Checklis - ¿Existe una alternativa recomendada? - ¿Los consumidores
fueron informados? - ¿Se de nió un periodo de transición? - ¿La
documentación fue actualizada?

Indicadores de alert ⚠ Funcionalidades marcadas como deprecadas durante
años

⚠ Consumidores que desconocen el cambio

⚠ Ausencia de un plan de retiro

Automatizació Media

Las herramientas pueden detectar el uso de elementos deprecados y
generar advertencias, pero la plani cación del retiro requiere
coordinación entre equipos fi .

fi r

t

n

a

.

.

.

.

.

fi .

.

.

.

.

Justi cació La deprecación permite evolucionar el sistema de forma
ordenada, reduciendo el impacto sobre los consumidores y proporcionando
tiempo su ciente para la migración

Relació API-00

DO

RE

MN

API-00 ¿Cómo debo retirar un contrato Clasi cación: 🔴 Obligatori

Objetiv Eliminar contratos obsoletos de forma controlada, minimizando el
impacto sobre los consumidores y preservando la estabilidad del
ecosistema

Regl Un contrato solo deberá retirarse cuando se haya veri cado que los
consumidores afectados han migrado o cuando exista una aprobación
explícita para asumir el impacto

El retiro deberá plani carse, comunicarse y ejecutarse de acuerdo con la
política de evolución de nida por la organización fi V

C

T

fi a

5

fi n

o

7

n

fi .

a

fi fi .

?

.

.

Antes del retir Debe veri carse

✅ La deprecación fue comunicada

✅ Existe una alternativa funcional

✅ Se evaluó el impacto

✅ La documentación re eja el cambio

✅ Se actualizaron las pruebas y monitoreo

Evita ❌ Eliminar contratos activos sin evidencia de migración

❌ Conservar versiones obsoletas por tiempo inde nido por falta de plani
cación

Checklis - ¿Quién sigue utilizando este contrato? - ¿Existe evidencia de
adopción del reemplazo? - ¿La fecha de retiro fue comunicada? - ¿El
ecosistema está preparado para el cambio?

Indicadores de alert ⚠ Versiones antiguas mantenidas inde nidamente

⚠ Retiros urgentes provocados por una mala plani cación

Automatizació r

fi t

:

o

n

.

fl a

.

.

fi .

.

.

fi fi .

.

fi .

Media

Las métricas de uso pueden apoyar la decisión, pero el retiro requiere
validación técnica y de negocio

Justi cació Un retiro plani cado reduce riesgos operativos y evita
afectar innecesariamente a consumidores que dependen del contrato

Relació API-00

API-00

MN

RE

CON --- Concurrenci

CON-00 ¿Cuándo debo asumir que existe concurrencia Clasi cación: 🔴
Obligatori

Objetiv Diseñar componentes que funcionen correctamente cuando múltiples
operaciones puedan ejecutarse simultáneamente V

T

fi .

6

5

fi .

n

o

fi 1

n

.

.

?

a

a

Regl Todo componente deberá asumir la posibilidad de ejecución
concurrente cuando exista más de un usuario, proceso, hilo, servicio o
tarea que pueda interactuar con los mismos recursos

La ausencia de concurrencia actual no garantiza que el sistema
permanezca así durante su evolución

Existe concurrencia cuand ✅ Dos usuarios realizan la misma operación

✅ Varias solicitudes llegan al mismo tiempo

✅ Existen procesos en segundo plano

✅ Hay múltiples instancias del sistema

✅ Se procesan eventos simultáneamente

Evita ❌ Asumir que una operación siempre será ejecutada por un único
usuario

❌ Basar la lógica únicamente en el orden de llegada

Checklis - ¿Otro proceso podría modi car este recurso? - ¿Existe acceso
simultáneo? - ¿Qué ocurre si dos operaciones llegan al mismo tiempo?

Indicadores de alert ⚠ Errores que aparecen solo bajo carga a

r

.

t

fi

a

.

.

.

.

o

.

.

.

.

.

⚠ Comportamientos inconsistentes difíciles de reproducir

Automatizació Baja

El análisis requiere comprensión del ujo del sistema

Justi cació La concurrencia no depende del lenguaje, sino del contexto
de ejecución. Considerarla desde el diseño reduce errores difíciles de
detectar y reproducir

Relació Arquitectur

Testin

PE

CON-00 ¿Cómo debo tratar el estado compartido Clasi cación: 🔴
Obligatori

Objetiv Reducir los riesgos derivados del acceso concurrente a datos o
recursos comunes

Regl R

.

fi g

a

fi a

n

o

2

n

n

a

fl .

.

.

.

?

El estado compartido deberá minimizarse siempre que sea posible

Cuando varios procesos necesiten acceder al mismo recurso, deberá de
nirse un mecanismo de coordinación apropiado para garantizar la
consistencia

Es recomendabl ✅ Preferir componentes sin estado cuando sea viable

✅ Mantener el estado encapsulado

✅ Reducir el tiempo durante el cual un recurso permanece compartido

Evita ❌ Variables globales modi cables

❌ Recursos compartidos sin coordinación

❌ Dependencias ocultas entre procesos

Checklis - ¿Este dato puede ser modi cado por varios procesos? - ¿Quién
es el responsable de mantener su consistencia? - ¿Puede eliminarse el
estado compartido?

Indicadores de alert ⚠ Resultados distintos para la misma operación

⚠ Inconsistencias difíciles de explicar

Automatizació r

t

n

e

fi fi a

.

.

.

.

.

.

.

.

.

fi .

Baja

Las herramientas detectan algunos patrones, pero no la arquitectura
completa

Justi cació La mayor parte de los problemas de concurrencia aparecen
alrededor del estado compartido. Reducirlo simpli ca el diseño y mejora
la con abilidad

Relació DE

MN

Arquitectur

CON-00 ¿Cómo debo diseñar operaciones idempotentes Clasi cación: 🟡
Heurístic

Objetiv Permitir que una operación pueda ejecutarse más de una vez sin
producir efectos secundarios no deseados

Regl Siempre que el contexto lo permita, las operaciones expuestas
públicamente deberán diseñarse para ser idempotentes P

T

.

fi a

fi .

a

n

o

fi 3

n

.

a

?

fi .

.

Cuando esto no sea posible, deberá existir un mecanismo que detecte o
controle ejecuciones repetidas

Es recomendabl ✅ Diseñar operaciones reintentables

✅ Identi car solicitudes duplicadas

✅ Registrar identi cadores de operación cuando corresponda

Evita ❌ Duplicar cobros

❌ Procesar el mismo evento varias veces

❌ Crear múltiples registros por reintentos

Checklis - ¿Qué ocurre si la operación se ejecuta dos veces? - ¿Produce
exactamente el mismo resultado? - ¿Existe protección frente a
duplicados?

Indicadores de alert ⚠ Eventos duplicados

⚠ Pagos repetidos

⚠ Inventarios inconsistentes

Automatizació r

.

fi t

.

fi .

.

n

e

.

a

.

.

.

.

.

Media

Las pruebas pueden veri car escenarios repetitivos, pero el diseño
requiere criterio

Justi cació Los sistemas distribuidos y las comunicaciones poco con
ables hacen inevitables los reintentos. Diseñar operaciones idempotentes
mejora la resiliencia y reduce errores de negocio

Relació ER

AP

Testin

CON-00 ¿Cómo debo evitar condiciones de carrera Clasi cación: 🔴
Obligatori

Objetiv Garantizar que el resultado de una operación no dependa del
orden impredecible en que varias ejecuciones concurrentes acceden al
mismo recurso

Regl Cuando múltiples operaciones puedan modi car el mismo estado,
deberá existir una estrategia explícita para preservar su consistencia

La elección del mecanismo dependerá de la arquitectura y de la
tecnología utilizada, pero la necesidad de coordinación deberá identi
carse desde el diseño R

I

fi g

.

a

fi n

o

4

n

fi a

.

fi fi .

fi .

.

.

?

Señales de riesg ⚠ Actualizaciones concurrentes

⚠ Lectura seguida de escritura

⚠ Incrementos compartidos

⚠ Procesamiento paralelo del mismo recurso

Evita ❌ Leer, modi car y guardar sin considerar accesos simultáneos

❌ Asumir que dos operaciones nunca coincidirán

Checklis - ¿Qué ocurre si dos operaciones modi can el mismo dato? -
¿Existe una estrategia de coordinación? - ¿El resultado será
consistente?

Indicadores de alert ⚠ Datos perdidos

⚠ Cambios sobrescritos

⚠ Resultados diferentes entre ejecuciones

Automatizació Baja .

r

t

fi .

n

.

o

.

.

a

.

fi

.

.

.

.

Las condiciones de carrera suelen requerir pruebas especí cas y análisis
de diseño

Justi cació Las condiciones de carrera producen errores intermitentes,
difíciles de reproducir y con alto impacto en la integridad del sistema

Relació Testin

Arquitectur

PE

CON-00 ¿Cómo debo coordinar procesos concurrentes Clasi cación: 🟡
Heurístic

Objetiv Seleccionar mecanismos de coordinación acordes con el nivel de
consistencia requerido por el sistema

Regl La coordinación entre procesos deberá responder al nivel de riesgo
y consistencia que exige el negocio

No todas las operaciones requieren sincronización estricta; algunas
pueden resolverse mediante mecanismos de compensación, reintentos o
consistencia eventual R

fi g

a

.

fi .

a

n

o

5

n

?

a

.

fi .

.

La estrategia elegida deberá estar documentada y alineada con la
arquitectura del sistema

Es recomendable considera ✅ Consistencia requerida

✅ Impacto del con icto

✅ Frecuencia de acceso concurrente

✅ Costo de la coordinación

Evita ❌ Aplicar sincronización máxima por defecto

❌ Ignorar con ictos porque "casi nunca ocurren"

❌ Diseñar sin una estrategia explícita

Checklis - ¿Qué nivel de consistencia necesita el negocio? - ¿Qué ocurre
si aparece un con icto? - ¿Cómo se resolverá? - ¿La estrategia está
documentada?

Indicadores de alert ⚠ Bloqueos excesivos que afectan el rendimiento

⚠ Inconsistencias repetitivas en producción

⚠ Estrategias diferentes para el mismo tipo de problema r

t

fl fl

.

.

.

fl a

.

.

r

.

.

.

.

.

.

Automatizació Baja

La elección depende del dominio, la arquitectura y los requisitos
funcionales

Justi cació No existe una única estrategia válida para todos los
escenarios de concurrencia. El objetivo es equilibrar consistencia,
disponibilidad, rendimiento y complejidad de acuerdo con las necesidades
del sistema

Relació PE

AP

MN

Arquitectur

AI --- Ingeniería Asistida por Inteligencia Arti cia

AI-00 ¿Quién es responsable del código generado por IA Clasi cación: 🔴
Obligatori

Objetiv R

I

T

.

fi fi fi a

n

o

1

?

l

n

n

.

a

.

Establecer claramente la responsabilidad sobre el software desarrollado
con asistencia de Inteligencia Arti cial

Regl Todo código incorporado al sistema será responsabilidad del
desarrollador que lo integre, independientemente de si fue escrito
manualmente, generado por IA o adaptado a partir de otra fuente

La utilización de herramientas de IA no modi ca las responsabilidades de
revisión, validación, documentación, pruebas y mantenimiento de nidas
por este Engineering Handbook

Es obligatori ✅ Comprender el funcionamiento del código

✅ Revisarlo antes de integrarlo

✅ Validarlo mediante pruebas

✅ Corregir cualquier incumplimiento de los estándares

Nunca justi ca ❌

``` text
"La IA lo escribió.
```

❌

``` text
"Así venía generado.
```

❌

``` text
"No sé exactamente cómo funciona.
```

.

a

fi fi

``` text
"
```

o

``` text
"
```

.

r

.

.

``` text
"
```

fi fi .

.

.

Checklis - ¿Entiendo completamente la solución? - ¿Podría mantener este
código dentro de seis meses? - ¿Asumo su responsabilidad técnica?

Indicadores de alert ⚠ Código que nadie del equipo comprende

⚠ Dependencia excesiva de la herramienta para explicar la implementación

Automatizació No

La responsabilidad profesional no puede delegarse

Justi cació La IA es una herramienta de asistencia. La responsabilidad
sobre el producto nal siempre recae en el equipo de ingeniería

Relació RE

TS

DO

AI-00 T

.

V

C

fi n

2

t

n

n

.

a

.

.

.

fi

¿Cuándo es apropiado utilizar IA durante el desarrollo Clasi cación: 🟡
Heurístic

Objetiv Utilizar la IA para aumentar la productividad sin sustituir el
criterio profesional

Regl La IA podrá emplearse para acelerar actividades de análisis,
generación, transformación, documentación o aprendizaje, siempre que los
resultados sean revisados y validados antes de incorporarse al sistema

El uso de IA deberá aportar valor al proceso y no sustituir decisiones
que requieren juicio de ingeniería

Es recomendable utilizar IA par ✅ Generar borradores

✅ Explorar alternativas

✅ Explicar conceptos

✅ Automatizar tareas repetitivas

✅ Crear documentación inicial

Evita ❌ Delegar decisiones arquitectónicas sin revisión fi a

r

.

o

?

.

.

.

.

a

.

.

.

a

.

❌ Aceptar cambios sin comprenderlos

❌ Utilizar IA como única fuente de información técnica

Checklis - ¿La IA está acelerando el trabajo o sustituyendo el
análisis? - ¿El resultado fue revisado? - ¿Existe evidencia su ciente
para aceptarlo?

Indicadores de alert ⚠ Dependencia total de la IA para resolver
problemas

⚠ Incorporación automática de sugerencias

Automatizació No

Depende del contexto y del juicio del desarrollador

Justi cació La IA incrementa la productividad cuando complementa el
conocimiento del ingeniero, no cuando reemplaza su capacidad de análisis

Relació RE

MN

DO .

V

C

T

fi n

t

n

fi n

a

.

.

.

.

.

.

AI-00 ¿Cómo debo revisar una propuesta generada por IA Clasi cación: 🔴
Obligatori

Objetiv Garantizar que toda propuesta generada por IA cumpla los
estándares técnicos de la organización antes de ser aceptada

Regl Toda propuesta generada por IA deberá evaluarse utilizando los
mismos criterios aplicados a cualquier contribución humana

La revisión deberá considerar arquitectura, seguridad, rendimiento,
mantenibilidad, pruebas, documentación y consistencia con el sistema
existente

Veri ca ✅ Correctitud funcional

✅ Arquitectura

✅ Seguridad

✅ Complejidad

✅ Cobertura de pruebas

✅ Cumplimiento de estándares fi fi a

o

3

r

.

?

.

.

.

.

.

a

.

.

.

Evita ❌ Revisar únicamente si "compila"

❌ Aprobar porque la solución parece razonable

❌ Omitir el Code Review por provenir de una IA

Checklis - ¿Cumple el Engineering Handbook? - ¿Introduce deuda
técnica? - ¿Se integra correctamente con el resto del sistema? - ¿Podría
defender esta solución en una revisión técnica?

Indicadores de alert ⚠ Código inconsistente con el proyecto

⚠ Soluciones innecesariamente complejas

⚠ Uso excesivo de patrones o abstracciones sin justi cación

Automatizació Media

Las herramientas pueden validar aspectos objetivos, pero la revisión nal
requiere criterio profesional

Justi cació La calidad del software depende del proceso de revisión, no
del origen del código .

fi r

.

t

n

n

a

.

.

.

.

.

fi

.

fi .

Relació RE

SE

PE

MN

AI-00 ¿Qué información puedo compartir con una IA Clasi cación: 🔴
Obligatori

Objetiv Proteger la información de la organización durante el uso de
herramientas de Inteligencia Arti cial

Regl Antes de compartir información con una herramienta de IA deberá
veri carse que dicha información pueda divulgarse conforme a las
políticas de seguridad, privacidad y con dencialidad de la organización

No deberán compartirse datos protegidos, credenciales, secretos,
información personal o cualquier contenido cuya divulgación no esté
autorizada

Nunca comparti ❌ Contraseñas C

R

V

fi fi T

fi ?

a

.

n

o

4

.

r

a

.

.

fi

❌ Tokens

❌ Claves privadas

❌ Información personal protegida

❌ Secretos comerciales

❌ Datos de clientes sin autorización

Es recomendabl ✅ Anonimizar ejemplos

✅ Reducir el contexto al mínimo necesario

✅ Utilizar datos cticios cuando sea posible

Checklis - ¿Esta información puede salir de la organización? - ¿Contiene
datos sensibles? - ¿Existe una alternativa anonimizada?

Indicadores de alert ⚠ Copiar bases de datos completas

⚠ Compartir archivos de con guración con secretos

⚠ Exponer información contractual o con dencial

Automatizació Media .

.

t

fi .

n

.

.

e

fi a

.

.

.

fi .

.

.

.

Las herramientas DLP pueden detectar algunos tipos de información
sensible

Justi cació La productividad nunca debe comprometer la con dencialidad
ni la protección de los activos de información de la organización

Relació SE

CF

Complianc

AI-00 ¿Cómo debe integrarse la IA al proceso de ingeniería Clasi cación:
🔴 Obligatori

Objetiv Incorporar herramientas de IA al ciclo de desarrollo sin alterar
las responsabilidades, controles y criterios de calidad de nidos por la
organización

Regl La utilización de IA deberá integrarse como un apoyo dentro del
proceso existente de ingeniería

Ninguna etapa obligatoria del ciclo de vida del software podrá omitirse
por el hecho de utilizar herramientas de IA C

G

fi a

fi e

n

o

5

n

.

?

fi a

.

.

fi .

.

Todo cambio generado con asistencia de IA deberá seguir el mismo ujo de
diseño, implementación, pruebas, revisión, documentación y aprobación
que cualquier otra contribución

El uso de IA no sustituy ❌ Arquitectura

❌ Code Review

❌ Testing

❌ Validación de seguridad

❌ Documentación

❌ Aprobaciones

Checklis - ¿Se siguieron todas las etapas del proceso? - ¿La IA aceleró
el trabajo sin eliminar controles? - ¿La calidad nal es equivalente a
una implementación manual?

Indicadores de alert ⚠ Cambios integrados directamente desde una
herramienta de IA

⚠ Ausencia de pruebas porque "la IA dijo que funcionaba"

⚠ Eliminación de revisiones para ahorrar tiempo

Automatizació Baja

La integración de la IA es una decisión de proceso organizacional .

.

fi t

.

.

.

.

n

.

a

e

.

.

.

.

fl .

Justi cació La IA debe fortalecer el proceso de ingeniería, no debilitar
los mecanismos que garantizan la calidad, seguridad y mantenibilidad del
software

Relació RE

TS

SE

MN

PARTE IV --- APÉNDICES Y MATERIAL DE REFERENCI

Apéndice A --- Glosario de Ingenierí Objetiv Establecer un vocabulario
común para evitar interpretaciones distintas de los mismos conceptos
dentro de la organización

Alcanc Este glosario de ne el signi cado o cial de los términos
utilizados en el Engineering Handbook

Cuando exista con icto entre una de nición externa y este documento,
prevalecerá la de nición aprobada por la organización

Arquitectur T

C

V

T

fi e

n

o

a

fi n

fl .

fi .

fi fi A

.

a

fi .

Organización estructural del software que de ne responsabilidades,
dependencias, restricciones y principios de diseño

AP

Contrato mediante el cual un componente expone funcionalidades a otros
componentes o sistemas

Cambio Compatibl

Modi cación que no requiere ajustes por parte de los consumidores
existentes

Cambio Incompatibl

Modi cación que obliga a adaptar consumidores existentes

Code Revie

Proceso de evaluación técnica destinado a veri car que un cambio cumple
los estándares de ingeniería establecidos

Complejida

Nivel de di cultad para comprender, modi car o mantener una solución

Contrat

Compromiso técnico que de ne el comportamiento esperado entre
componentes

Deuda Técnic

Decisión consciente o inconsciente que reduce la calidad del software a
cambio de un bene cio inmediato y que requerirá acciones futuras I

fi fi .

o

fi w

d

a

.

.

e

e

fi fi .

fi fi .

.

.

.

fi

Deprecació

Estado mediante el cual una funcionalidad continúa disponible, pero deja
de recomendarse para nuevos desarrollos y tiene prevista una estrategia
de retiro

Idempotenci

Propiedad por la cual ejecutar una misma operación varias veces produce
el mismo resultado observable que ejecutarla una sola vez

Mantenibilida

Capacidad del software para ser comprendido, corregido, adaptado y
evolucionado con un esfuerzo razonable

Refactorizació

Cambio interno del software que mejora su estructura sin modi car su
comportamiento observable

Responsabilida

Conjunto de decisiones o comportamientos que corresponden a un
componente especí co

Riesg

Probabilidad de que una decisión técnica afecte negativamente la
calidad, disponibilidad, seguridad o evolución del sistema

Sistem

Conjunto de componentes que colaboran para satisfacer una necesidad del
negocio

Trazabilida o

a

.

n

d

a

d

n

.

d

.

.

.

fi .

fi .

Capacidad para relacionar una decisión de ingeniería con los estándares,
evidencias y controles que la respaldan

Apéndice B --- Matriz de Trazabilida Aquí creo que está una de las
mejores ideas de todo el handbook

Cada regla debe indicar

-   Dónde se veri ca.
-   Si puede automatizarse.
-   Quién es responsable. Ejemplo

Automatizabl Regla Veri cación Responsable e NAM-00 Desarrollador + Code
Review Sí 1 Reviewer CLS-002 Code Review Parcial Arquitecto / Reviewer
DEP-003 Arquitectura No Arquitecto ERR-004 Code Review + SAST Sí
Desarrollador CFG-003 SAST + Secret Scan Sí DevOps SEC-002 Testing +
Review Parcial Desarrollador PER-002 Pro ling Parcial Equipo Revisión
API-005 No Arquitecto Arquitectónica AI-003 Code Review Parcial Reviewer

Apéndice C --- Niveles de Criticida Para evitar dudas durante las
revisiones, cada regla debe pertenecer a una categoría claramente de
nida

🔴 Obligatori Su incumplimiento impide aprobar el cambio fi fi fi .

:

fi .

a

:

.

.

d

d

Ejemplos

-   Seguridad.
-   Contratos.
-   Errores críticos.
-   Manejo de secretos.
-   Pruebas obligatorias.

🟡 Heurístic Representa una práctica recomendada cuya aplicación depende
del contexto

Puede justi carse una excepción

🔵 Recomendació Buenas prácticas que mejoran la calidad, pero cuyo
incumplimiento no representa un riesgo signi cativo

Apéndice D --- Checklist Maestro de Code Revie En lugar de que cada
reviewer invente su propio criterio, el handbook proporciona una lista
única

Arquitectur - ¿Respeta la arquitectura de nida? - ¿Las responsabilidades
están bien distribuidas? - ¿Se introducen dependencias innecesarias?

Calida - ¿El código es legible? - ¿Los nombres son claros? - ¿Existe
duplicación innecesaria? fi .

:

d

fi w

.

a

a

fi n

.

.

Segurida - ¿Hay validación de entradas? - ¿Existen secretos expuestos? -
¿Se protege la información sensible?

Rendimient - ¿Existen operaciones costosas evitables? - ¿Hay
optimización prematura? - ¿Se introducen consultas redundantes?

Testin - ¿Existen pruebas su cientes? - ¿Cubren los escenarios
críticos? - ¿Las pruebas son deterministas?

Documentació - ¿Cambió un contrato? - ¿Debe actualizarse la
documentación? - ¿La decisión arquitectónica requiere un ADR?

Apéndice E --- Automatizació Uno de los aspectos más innovadores del
handbook puede ser reconocer que no todas las reglas deben veri carse de
la misma manera

Tipo de regla Método principal Estilo Linter Seguridad SAST / Secret
Scanner Dependencias Análisis estático Rendimiento Pro ling Contratos
Contract Tests Arquitectura Revisión humana Diseño Revisión humana fi g

fi d

o

fi

n

.

n

Responsabilidade Revisión humana s Revisión humana apoyada por IA
herramientas

Este apéndice deja claro dónde invertir en automatización y dónde sigue
siendo indispensable el juicio profesional

Apéndice F --- Correspondencia con estándares externo El Engineering
Handbook no pretende reemplazar estándares reconocidos, sino
complementarlos y adaptarlos al contexto de la organización

Engineering Estándares relacionados Handbook SEC OWASP ASVS, OWASP Top
10, NIST SSDF TST ISO/IEC/IEEE 29119 PER ISO/IEC 25010 (E ciencia del
desempeño) MNT ISO/IEC 25010 (Mantenibilidad) API OpenAPI, AsyncAPI, RFC
relevantes REV NIST SSDF, prácticas de revisión por pares ISO/IEC/IEEE
26515, documentación de DOC software AI NIST AI RMF, ISO/IEC 42001
(cuando aplique) .

fi s

.
