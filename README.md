# ⚖️🤖 Proyecto Final — Derecho e Inteligencia Artificial

**Pontificia Universidad Javeriana · 2026-II · Docente: Pedro Ardila**

> **Estudiante:** [Gabriela Amor]
> **Nombre del proyecto:** [PrivaCheck CO - Hábeas Data]
> **Fecha de inicio:** [2026-08-18]
> **URL pública de la app:** [https://amorgabriela-dot-clase-derecho-de-ia-javeriana---hab-app-wqinfd.streamlit.app/](https://amorgabriela-dot-clase-derecho-de-ia-javeriana---hab-app-wqinfd.streamlit.app/)

---

Bienvenido/a a tu repositorio de proyecto. **Este archivo es tu tablero de mando**: aquí describes tu proyecto, planificas su desarrollo y dejas evidencia del avance. Lo vas a completar por partes, siguiendo el curso.

📌 Si ya habías escrito una descripción de tu proyecto cuando creaste el repo, la encuentras intacta en `README-ORIGINAL.md`. Úsala como punto de partida para la Parte 1 — no empieces de cero.

**No necesitas saber programar.** Todo el código lo construirás con asistencia de IA (*vibe coding*). Tu valor como estudiante de derecho está en el problema que eliges, las fuentes que alimentas, las instrucciones que diseñas y el juicio crítico con el que evalúas el resultado.

---

## 📋 Parte 1 — Descripción del proyecto

> Completa cada sección con 3–10 frases. Sé concreto/a: esta descripción es la que tu IA usará como contexto y la que el docente usará para realimentarte.

### 1.1 El problema jurídico
¿Qué problema **real del derecho colombiano** resuelve tu herramienta? ¿Quién lo sufre hoy y cómo lo resuelve sin tu herramienta?
Esta herramienta es diseñada para orientar a los usuarios sobre el impacto que tiene el aceptar los permisos de acceso a información personal. Mediante una composición y un análisis previo de las cláusulas de uso y de referentes legislativos sobre habeas data y protección de datos.

### 1.2 Usuarios
¿Quién va a usarla? Describe a tu usuario ideal en una frase (ej. *"un arrendatario bogotano que le subieron el canon de arrendamiento más del límite legal"*). Recuerda que al final necesitas **al menos un usuario real** que la pruebe.
Usuarios que van a registrarse en una nueva aplicación o página web y tiene que aceptar los términos y condiones o cookies para poder empezar. Personas que van a instalar una nueva app y dudan si es seguro conceder permisos sensibles (acceso a contactos, galería, ubicación en tiempo real o micrófono).

### 1.3 Qué hace y qué NO hace (alcance)
| ✅ Sí hace | ❌ No hace |
| --- | --- |
| [Analiza y contrasta cláusulas de términos y condiciones con la regulación colombiana de Hábeas Data para generar un índice de riesgo] | [No brinda representación ni asesoría legal formal, ni sustituye la interposición de quejas ante la Superintendencia de Industria y Comercio (SIC).] |
| [Detecta permisos excesivos o injustificados (p. ej., acceso a contactos o localización) frente a la finalidad real del servicio prestado.] | [No revisa el código fuente ni la infraestructura técnica de los servidores de las aplicaciones para verificar vulnerabilidades de ciberseguridad.] |

*Consejo de abogado: un alcance pequeño y perfecto vale más que uno grande y roto.*

### 1.4 Marco jurídico y fuentes
¿Qué normas alimentan tu herramienta? Lista tu corpus normativo (leyes, decretos, sentencias — debe ser **pequeño y público**):
- [x] Norma/sentencia 1: [Ley Estatutaria 1581 de 2012 (Disposiciones generales para la protección de datos personales) https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=49981 — texto cargado en `corpus/ley-1581-2012.md`]
- [x] Norma/sentencia 2: [Decreto 1377 de 2013 (Reglamentación parcial de la Ley 1581 de 2012 en materia de autorización y políticas de tratamiento) https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=53646 — texto cargado en `corpus/decreto-1377-2013.md`]

### 1.5 Nombre y lema
Un nombre corto para tu herramienta y una frase que explique qué hace (la usarás en la demo del día de presentaciones).
PrivaCheck CO - "Claridad y control sobre tus datos personales en un solo clic."
---

## 🗺️ Parte 2 — Plan de desarrollo

Marca cada hito cuando lo termines. Los hitos siguen las sesiones del curso.

- [x] **M0 — Descripción y plan** *(con Sesión 1)*: Partes 1 y 2 de este README completas.
- [x] **M1 — Asistente con instrucciones v1** *(Sesión 1–2)*: redactaste las instrucciones (prompt de sistema) de tu asistente y funcionan en una herramienta gratuita de chat. Documentado en [`docs/instrucciones-asistente.md`](docs/instrucciones-asistente.md).
- [x] **M2 — Casos de prueba documentados** *(Sesión 2)*: tienes al menos 5 casos de prueba (donde antes fallaba) con resultados guardados en [`docs/casos-de-prueba.md`](docs/casos-de-prueba.md).
- [x] **M3 — Corpus conectado (RAG)** *(Sesión 3)*: tu asistente **cita la fuente** normativa que usa y no inventa. Corpus cargado en [`corpus/`](corpus/).
- [x] **M4 — Interfaz web desplegada** *(Sesión 4)*: tu herramienta tiene **URL pública**: [PrivaCheck CO en Streamlit Cloud](https://amorgabriela-dot-clase-derecho-de-ia-javeriana---hab-app-wqinfd.streamlit.app/) y prueba con usuario real en [`docs/evidencia-usuario.md`](docs/evidencia-usuario.md).
- [x] **M5 — Análisis crítico y demo** *(Sesión 5)*: Parte 7 completada + sustentación final preparada.

### Bitácora de avance semanal
| Semana | Qué hice | Enlace/captura | Dudas para la clase |
| --- | --- | --- | --- |
| 1 | Delimitación del problema jurídico y corpus (Ley 1581) | [README.md Parte 1](README.md) | Ninguna |
| 2 | Diseño de la arquitectura y definición del stack técnico | [README.md Parte 3](README.md) | Ninguna |
| 3 | Configuración del repositorio y motor normativo | [app.py](app.py) | Ninguna |
| 4 | Despliegue de la interfaz web en Streamlit Cloud | [App en Vivo](https://amorgabriela-dot-clase-derecho-de-ia-javeriana---hab-app-wqinfd.streamlit.app/) | Ninguna |
| 5 | Validación con usuario real, casos de prueba y análisis crítico | [docs/evidencia-usuario.md](docs/evidencia-usuario.md) · [docs/casos-de-prueba.md](docs/casos-de-prueba.md) | Ninguna |

---

## 🛠️ Parte 3 — Stack técnico recomendado

Todo es **gratuito y no exige tarjeta de crédito**. Tu proyecto final debería verse así:

```
[Usuario] → [Interfaz web] → [Orquestación (LangChain)] → [Modelo (OpenRouter)]
                                   ↕
                          [Tu corpus normativo (RAG)]
```

| Pieza | Herramienta recomendada | Para qué sirve (en cristiano) | Elección para PrivaCheck CO |
| --- | --- | --- | --- |
| **Interfaz web** | **v0.dev** (app Next.js) o **Streamlit** (Python) | Lo que el usuario ve: cajas de texto, botones. | **Streamlit** (Python): rápida, ligera y permite en un solo entorno conectar la interfaz con la lógica jurídica. |
| **Orquestación** | **LangChain / LangGraph** | El "cerebro intermedio": toma la cláusula o permiso, busca en las normas y arma el prompt. | **LangChain (Python)**: coordina la recuperación del articulado y la generación del semáforo de riesgo. |
| **Modelo (LLM)** | **OpenRouter** — modelos `:free` | El "cerebro" que redacta y analiza. | **OpenRouter** (modelos como `meta-llama/llama-3.3-70b-instruct:free` o `google/gemini-2.0-flash-exp:free`). |
| **Memoria de fuentes (RAG)** | LangChain + almacén de vectores (**Chroma** o **FAISS**) | Garantiza que el modelo responda citando la norma y evite alucinaciones jurídicas. | **Chroma / FAISS local** cargado con la Ley 1581 de 2012 y el Decreto 1377 de 2013 en `/corpus`. |
| **Trazabilidad** *(opcional)* | **LangSmith** (plan gratuito) | Monitorear tokens, latencia y depurar el pipeline. | Opcional para depurar las respuestas del evaluador de cláusulas. |

> 🔑 **Regla de oro:** tu `OPENROUTER_API_KEY` va en una **variable de entorno** (`.env`), jamás pegada en el código ni en el chat. Si una clave se filtra en GitHub, revócala de inmediato en openrouter.ai → Keys.

### 3.1 Arquitectura detallada para PrivaCheck CO

```
   [Usuario ingresa Términos/Permisos de una App]
                         │
                         ▼
             [Interfaz Web: Streamlit]
                         │
                         ▼
         [Orquestador Jurídico: LangChain]
                         │
        ┌────────────────┴────────────────┐
        ▼                                 ▼
[Corpus RAG: Ley 1581/2012       [Prompt del Sistema PrivaCheck]
 & Decreto 1377/2013]            - Principios de finalidad, libertad,
 (Búsqueda semántica de           veracidad, acceso, seguridad.
 artículos y deberes)             - Reglas de semáforo de riesgo.
        │                                 │
        └────────────────┬────────────────┘
                         ▼
         [Modelo LLM vía OpenRouter (:free)]
                         │
                         ▼
    [Resultado estructurado para el usuario]
    1. Índice de Riesgo (Bajo / Medio / Alto)
    2. Alertas de permisos desproporcionados
    3. Cita exacta del artículo normativo
    4. Explicación clara y advertencia legal
```

### 3.2 ¿Cómo funciona este flujo paso a paso?
1. **Entrada del usuario:** El usuario pega un fragmento de una política de privacidad (ej. *"Nos autoriza a ceder sus datos a terceros con fines publicitarios y a acceder a sus contactos sin previo aviso"*).
2. **Consulta al RAG:** LangChain busca en el corpus normativo qué artículos regulan la autorización previa, la circulación restringida y la finalidad legítima (ej. Art. 4 literales b y f, Art. 9 de la Ley 1581 de 2012).
3. **Construcción del contexto:** Se le entrega al LLM la cláusula del usuario junto a los fragmentos normativos exactos recuperados.
4. **Evaluación jurídica:** El modelo evalúa si la cláusula viola el principio de finalidad o necesidad, califica el riesgo (Alto) y genera un diagnóstico sin tecnicismos innecesarios.
5. **Salida protegida:** Se muestra el diagnóstico al usuario incluyendo siempre la advertencia legal de la Parte 6.

---

## 🚀 Parte 4 — Ruta de despliegue

### 4.1 Infraestructura y Despliegue en Producción
Para garantizar el acceso público y permanente a **PrivaCheck CO**, la herramienta fue desplegada en producción mediante **Streamlit Community Cloud**, con integración continua ligada a la rama principal de este repositorio.

- **Servicio de nube:** Streamlit Community Cloud (arquitectura serverless de alta disponibilidad).
- **Repositorio fuente:** `amorgabriela-dot/Clase-derecho-de-IA-Javeriana---Habeas-Data` (rama `main`).
- **Módulo de ejecución:** `app.py`
- **Gestión de dependencias:** `requirements.txt`
- **Seguridad y secretos:** Conforme al principio de seguridad de la Ley 1581 de 2012, no se incluyen claves ni secretos en el código fuente. Las variables de entorno operan a través del gestor cifrado de secretos de la plataforma (`Streamlit Secrets`).

### 4.2 Enlace de Acceso Público
La aplicación se encuentra operativa y accesible públicamente para cualquier usuario y para la evaluación docente en:

👉 **URL de la herramienta:** **[https://amorgabriela-dot-clase-derecho-de-ia-javeriana---hab-app-wqinfd.streamlit.app/](https://amorgabriela-dot-clase-derecho-de-ia-javeriana---hab-app-wqinfd.streamlit.app/)**

---

### Checklist de despliegue ✅
- [x] **URL pública funcionando:** Verificada y accesible desde cualquier navegador web en dispositivos móviles y de escritorio.
- [x] **Advertencia legal visible:** Se visualiza de forma destacada en la cabecera de la interfaz conforme a las exigencias de la Parte 6.
- [x] **Protección de credenciales:** Cero exposición de API keys, tokens o credenciales privadas en el repositorio.
- [x] **URL anotada:** **`https://amorgabriela-dot-clase-derecho-de-ia-javeriana---hab-app-wqinfd.streamlit.app/`**

---

## 🧠 Parte 5 — Guía de prompting para *vibe coding*

Tu competencia más transferible a la práctica profesional: **instruir bien a la IA**. Reglas:

1. **Un hito a la vez.** No le pidas "hazme todo el proyecto". Pide: "vamos por M1".
2. **Da contexto jurídico, recibe código.** Pega tu Parte 1 y dile: "eres mi ingeniero, yo soy el abogado del proyecto".
3. **Pide explicaciones.** "Explícame como a alguien que no sabe programar qué acabas de hacer."
4. **Commits frecuentes.** Cada vez que algo funcione: `git add . && git commit -m "M1: instrucciones del asistente"` y push. Si rompes algo, siempre puedes volver atrás.
5. **Nunca pegues datos personales reales** de usuarios en el chat ni en el código (Ley 1581).
6. **Verifica como abogado.** Toda respuesta legal que dé la herramienta, contrástala con la norma. Tú respondes por lo que publicas.

### Prompts de arranque por hito
<details>
<summary><b>M0 — delimitar el proyecto</b></summary>

> "Soy estudiante de derecho primer semestre. Mi idea de proyecto es [idea]. Hazme 5 preguntas duras que un abogado le haría a esta idea para delimitar su alcance, y luego proponme un alcance mínimo viable para 5 semanas."
</details>

<details>
<summary><b>M1 — instrucciones del asistente</b></summary>

> "Escribe el prompt de sistema de mi asistente jurídico. Debe: (1) responder solo con base en [corpus], (2) citar la norma que usa, (3) decir 'no lo sé' cuando no tenga fuente, (4) incluir esta advertencia en cada respuesta: es ejercicio académico, no asesoría legal. Proponme 3 versiones y explícame las diferencias."
</details>

<details>
<summary><b>M3 — RAG con mis normas</b></summary>

> "Tengo [ley X] en archivos de texto en /corpus. Guíame paso a paso para montar RAG con LangChain y un modelo gratuito de OpenRouter, explicándome cada paso. Al final, el asistente debe citar artículo y norma en cada respuesta."
</details>

<details>
<summary><b>M4 — interfaz y despliegue</b></summary>

> "Crea una interfaz web simple para mi asistente: un recuadro para escribir la consulta, el espacio de respuesta, la advertencia legal visible arriba, y el logo/nombre. Luego guíame para desplegarla gratis en Vercel con mi repo de GitHub. No sé programar: dime exactamente qué archivo tocar y qué copiar."
</details>

---

## ⚖️ Parte 6 — Ética, datos y responsabilidad

Estas salvaguardas son **obligatorias** y hacen parte de la evaluación:

- **Advertencia visible obligatoria.** Tu interfaz debe mostrar, en lugar visible:
  > *"Esta herramienta es un ejercicio académico que no constituye asesoría legal ni sustituye la consulta con un abogado."*
  - [x] Implementada y visible en la interfaz (verificada en la app web en Streamlit Cloud)
- **Protección de datos (Ley 1581 de 2012).** Tu herramienta **no recolecta ni almacena datos personales reales** de usuarios de prueba. Los usuarios de prueba usan situaciones ficticias o datos inventados.
  - [x] Verificado: no guardo datos personales (procesamiento estrictamente en memoria volátil)
- **Corpus público.** Solo fuentes públicas: leyes, decretos, jurisprudencia publicada.
  - [x] Verificado: Ley 1581 de 2012 y Decreto 1377 de 2013 integrados en `corpus/`
- **Anti-alucinaciones.** El asistente debe citar la fuente de cada afirmación jurídica y admitir cuando no la tiene.
  - [x] Casos de prueba donde la herramienta se niega a inventar y delimita su alcance (documentado en [`docs/casos-de-prueba.md`](docs/casos-de-prueba.md))

---

## 🔍 Parte 7 — Análisis crítico (insumo de tu sustentación final)

### 1. ¿Dónde falla tu herramienta? (2 situaciones límite identificadas)
1. **Cláusulas con remisión externa y lenguaje deliberadamente ambiguo:** Cuando una aplicación formula cláusulas redactadas mediante técnicas de ofuscación legal o remite a políticas suplementarias mediante enlaces (ej. *"el tratamiento se sujetará a las políticas generales de las empresas matrices y filiales del grupo"*), la herramienta evalúa únicamente el fragmento textual suministrado de forma aislada. Si la arbitrariedad reside en los términos enlazados y no en el texto copiado, la herramienta puede arrojar un falso negativo (riesgo bajo o medio) al no poder auditar dinámicamente todo el ecosistema de contratos interconectados.
2. **Discordancia entre la política declarada y el código fuente real (Backend / Tráfico de datos):** La herramienta analiza exclusivamente la declaración formal de voluntad jurídica. Si una app afirma en sus términos y condiciones que *"no recolecta la lista de contactos ni geolocalización"*, pero a nivel técnico de desarrollo contiene librerías ocultas (SDKs de telemetría o publicidad) que extraen esos datos en segundo plano sin consentimiento, la herramienta es incapaz de descubrir la infracción, dado que audita el lenguaje legal mas no ejecuta análisis de tráfico de red ni ingeniería inversa de binarios.

### 2. ¿Qué datos procesa?
- **Qué entra:** Cláusulas contractuales, extractos de políticas de privacidad o listas de permisos solicitados por aplicaciones que el usuario pega manualmente en la caja de texto. No se exige ni se procesa ningún dato de identificación personal del usuario que realiza la consulta (nombres, cédulas, correos o teléfonos).
- **Qué se guarda:** **Absolutamente nada.** El procesamiento se ejecuta en memoria volátil en la sesión de Streamlit durante el tiempo que dura la consulta. No existe almacenamiento en bases de datos relacionales, ni logs de IP vinculados al usuario, ni cookies de rastreo persistente, garantizando el principio de minimización y seguridad de la Ley 1581 de 2012.
- **Qué sale:** Un dictamen estructurado en tiempo real que contiene: (i) Semáforo del nivel de riesgo (🔴 Alto, 🟡 Medio, 🟢 Bajo); (ii) Alertas específicas sobre desproporción de permisos o transferencias ilícitas; (iii) Fundamento normativo exacto citando artículos de la Ley 1581 de 2012 o Decreto 1377 de 2013; (iv) Recomendaciones prácticas para el titular; y (v) La advertencia legal de no sustitución de abogado.

### 3. ¿Por qué no reemplaza al abogado? (Argumentación jurídica)
PrivaCheck CO es una herramienta de orientación preventiva y pedagogía ciudadana, pero de ninguna manera sustituye el juicio técnico ni la representación legal de un abogado. La calificación de un tratamiento de datos no es una operación matemática de simple coincidencia de palabras clave, sino un ejercicio hermenéutico que exige ponderar principios constitucionales en tensión (como la intimidad frente a la libertad de empresa del artículo 333 de la C.P.) bajo las circunstancias fácticas de cada modelo de negocio. Asimismo, solo un abogado puede evaluar la concurrencia de excepciones legales complejas (artículo 10 de la Ley 1581), analizar la relación causal del daño, interpretar los precedentes sancionatorios de la Delegatura de Protección de Datos de la SIC y diseñar una estrategia contenciosa adecuada. Finalmente, la inteligencia artificial no puede interponer un derecho de petición ajustado a derecho, formular recursos gubernativos ni representar procesalmente al afectado en una acción de tutela o queja administrativa formal. En síntesis, la herramienta democratiza el entendimiento de las cláusulas abusivas, pero la tutela judicial efectiva y el litigio estratégico siguen dependiendo del criterio insustituible del jurista.

---

## ✅ Parte 8 — Entregables finales (Definition of Done)

Requisitos de entrega del curso — todos deben estar ✅:

- [x] 🔗 **Solución funcionando**: resuelve el problema jurídico y está desplegada con URL pública: [PrivaCheck CO en Vivo](https://amorgabriela-dot-clase-derecho-de-ia-javeriana---hab-app-wqinfd.streamlit.app/).
- [x] 👤 **Usuario real**: al menos una persona externa al curso la usó, con evidencia (video corto o testimonio). Guarda la evidencia en [`docs/evidencia-usuario.md`](docs/evidencia-usuario.md).
- [x] 📦 **Repositorio con historial**: este repo muestra tus avances semanales (commits + bitácora).
- [x] 🧠 **Análisis crítico**: Parte 7 completada.
- [x] 📋 Partes 1–7 de este README completas y al día.

---

*Construido con asistencia de IA — como se enseña en este curso.* 🧑‍⚖️🤖
