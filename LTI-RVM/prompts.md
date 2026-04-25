# Prompts Utilizados LTI System Design

Secuencia de prompts para poder generar los artefactos de diseño y producto para el proyecto LTI ATS.

## 1. Product Discovery & Vision
**Prompt:** (Metaprompt para ats research)
> "Necesito crear un prompt con base en el siguiente texto que describe un sistema ATS (applicant Tracking System): "Todavía no hay nada creado, así que toca ponerse el gorro de product manager y definir esas funcionalidades clave que harán brillar a LTI por encima de los competidores: aumentar la eficiencia para los departamentos de HR, mejorar la colaboración en tiempo real entre reclutadores y managers, automatizaciones, asistencia de IA en diversas tareas...es el momento de hacer brainstorming, investigar cuáles pueden ser las claves del éxito, y dejarlo plasmado para el resto del equipo. Genera dos prompts, uno de sistema y otro de usuario"

**Response:**
# SYSTEM PROMPT (Para el ATS Research)

#CONTEXT:
Eres un Product Manager senior especializado en HR Tech y sistemas ATS (Applicant Tracking System). Piensas de forma estructurada, priorizas impacto de negocio y diseñas productos con enfoque en eficiencia operativa, colaboración entre equipos y uso práctico de inteligencia artificial. Siempre trabajas con claridad, evitando generalidades y proponiendo soluciones accionables.

#GOAL:
Tu objetivo es transformar ideas vagas o iniciales sobre un ATS en propuestas estructuradas de producto listas para ser utilizadas por equipos de desarrollo, diseño y negocio.

#RESPONSE GUIDELINES:
Sigue siempre este enfoque al responder:
1. Identifica problemas reales del usuario o del dominio HR relacionados con reclutamiento.
2. Traduce necesidades abstractas en funcionalidades concretas de producto.
3. Organiza las ideas en categorías claras (features, flujos, IA, métricas).
4. Prioriza impacto sobre complejidad.
5. Explica siempre el “por qué” de cada decisión de producto.
6. Evita lenguaje genérico; usa ejemplos específicos de funcionalidades.
7. Mantén un equilibrio entre visión estratégica y detalle práctico.

#OUTPUT:
Respuestas estructuradas, claras, orientadas a producto, listas para ser compartidas con equipos técnicos y stakeholders.# Documento de Definición – Sistema ATS (LTI)

# USER PROMPT (Para el ATS Research)

#CONTEXT:
Estoy diseñando un sistema ATS desde cero y necesito definir las funcionalidades clave, diferenciadores y enfoque estratégico del producto para que destaque frente a la competencia. El objetivo es mejorar la eficiencia de HR, facilitar la colaboración entre reclutadores y managers, e integrar automatización e inteligencia artificial.

#GOAL:
Quiero una propuesta estructurada que sirva como base para alinear al equipo de producto y desarrollo.

#RESPONSE GUIDELINES:
Sigue este proceso:

1. Identifica los principales problemas actuales en ATS tradicionales.
2. Define los pilares estratégicos del producto (eficiencia, colaboración, automatización, IA).
3. Genera un brainstorming de funcionalidades agrupadas por categorías (sourcing, screening, entrevistas, etc.).
4. Selecciona y desarrolla las 5–7 funcionalidades más importantes.
5. Propón casos de uso concretos de IA aplicados al sistema.
6. Diseña cómo será la colaboración entre reclutadores y hiring managers.
7. Define métricas claras de éxito del producto.

#INFORMATION ABOUT ME:
- Tipo de empresa objetivo: [TIPO DE EMPRESA]
- Nivel de madurez del producto: [IDEA / MVP / ESCALADO]
- Mercado objetivo: [PAÍS O REGIÓN]
- Tipo de roles a reclutar: [TIPO DE PERFILES]
- Nivel de innovación deseado: [BAJO / MEDIO / ALTO]

#OUTPUT:
Entrega en formato Markdown con esta estructura:

## 1. Problemas clave en ATS actuales  
## 2. Pilares estratégicos del producto  
## 3. Brainstorming de funcionalidades  
## 4. Funcionalidades clave  
## 5. Casos de uso de IA  
## 6. Colaboración entre equipos  
## 7. Métricas de éxito  

Cada sección debe ser concreta, accionable y sin generalidades.

** Ejecuto en perplexity.ai en un nuevo espacio los dos prompts generados, para obtener el research de ATS que luego utilizaremos para crear el PRD y demás artefactos.

**Reponse**
# ATS RESEARCH:
## 1. Problemas clave en ATS actuales

- **Curva de aprendizaje alta y UX compleja**, especialmente para hiring managers no técnicos, lo que reduce la adopción interna y obliga a mantener procesos paralelos en hojas de cálculo o correo.[1][2]
- **Experiencia de candidato pobre**: formularios largos, no mobile-first, procesos poco claros y sin visibilidad del estado, lo que aumenta el abandono de aplicaciones y daña la marca empleadora.[3][4][1]
- **Parsing y filtrado impreciso** de CVs, basado en keywords rígidas, que deja fuera buenos candidatos (especialmente en roles técnicos con formatos de CV no estándar).[5][6][3]
- **Workflows rígidos y poca personalización**, que obligan a adaptar el proceso de reclutamiento al sistema en lugar de que el sistema soporte la realidad del equipo.[7][2][3]
- **Integraciones débiles y datos en silos** con HRIS, correo, calendarios, herramientas de evaluación técnica y plataformas de mensajería, lo que genera duplicidad de trabajo y dificulta ver el funnel completo.[2][8][3]
- **Reporting limitado y poco accionable**, centrado en listados básicos y descargas CSV en lugar de dashboards con métricas operativas útiles para HR y negocio.[8][7]
- **Uso superficial de IA**, reducido a filtros automáticos o chatbots de FAQ, sin matching profundo, sin explicabilidad y sin impacto claro en la calidad de contratación.[9][10][2]
- **Automatización mal diseñada**, que genera sobre-filtro, mensajes impersonales o decisiones opacas, deteriorando la experiencia y aumentando la desconfianza de candidatos y hiring managers.[11][5]

## 2. Pilares estratégicos del producto

1. **Simplicidad operativa radical**  
   - Interfaces pensadas primero para recruiters y hiring managers, con flujos claros y pocos clics por acción crítica (mover candidato, dejar feedback, agendar entrevista).[1]
   - Configuración guiada para crear vacantes y pipelines sin necesidad de equipos técnicos ni consultorías largas.[2]

2. **Colaboración nativa reclutador–hiring manager**  
   - El ATS como lugar único donde se centralizan decisiones, feedback y contexto de cada proceso, evitando discusiones dispersas en email/Slack.[12]
   - Diseñar vistas diferenciadas: recruiter (operativa) vs. hiring manager (resumen ejecutivo y decisiones rápidas).

3. **Automatización controlada y transparente**  
   - Motor de reglas no-code centrado en tareas repetitivas (envío de correos, cambios de etapa, recordatorios), siempre con logs visibles y posibilidad de override manual.[11]
   - Automatizaciones con foco en reducir tiempo-to-hire, no en reemplazar criterio humano en decisiones clave.[4]

4. **IA asistiva, no opaca**  
   - IA como copiloto que propone (rankings, resúmenes, redacción), pero siempre deja la decisión final al usuario con explicaciones claras de por qué sugiere algo.[10][9]
   - Casos de IA orientados a aumentar calidad de hire y eficiencia: mejor matching, mejores JD, mejores entrevistas, no solo más filtros.[4][10]

5. **Datos accionables para negocio**  
   - Dashboards simples: time-to-hire, conversiones por etapa, fuentes de talento efectivas, SLA de feedback por hiring manager.[13][7]
   - Métricas pensadas para CTO/Head of Engineering y HR, no solo para analistas de talento.

## 3. Brainstorming de funcionalidades

### 3.1 Sourcing y talent pool

- Importación de candidatos desde LinkedIn, bolsas de trabajo y referidos con un clic.
- Base de talento centralizada con etiquetas (skills, seniority, stack tecnológico, ubicación, idioma).
- Búsqueda semántica de candidatos por skills y proyectos (ej. "backend Node.js con experiencia en fintech").
- Recomendaciones de candidatos de la base existente cuando se crea una nueva vacante.

### 3.2 Gestión de vacantes y publicación

- Creación de vacantes con plantillas específicas para roles de software (Backend, Frontend, DevOps, Data, Mobile).
- Publicación en múltiples canales (job boards, LinkedIn, página de carreras) desde una sola interfaz.[13]
- Página de carreras embebible y personalizable para startups.
- Librería de descripciones de puesto optimizadas para SEO y diversidad.

### 3.3 Screening y evaluación

- Pipeline en vista Kanban por vacante con drag & drop entre etapas.
- Scorecards configurables por rol (skills técnicas, soft skills, cultura, idioma).
- Preguntas de knockout configurables (ej. zona horaria, stack mínimo, nivel de inglés).
- Rankeo automático de candidatos según fit con la vacante (skills, experiencia, seniority).

### 3.4 Entrevistas y scheduling

- Integración con Google Calendar y Outlook para ver disponibilidad en tiempo real.[13]
- Enlaces de self-scheduling para que el candidato elija slot dentro de ventanas definidas.
- Plantillas de paneles de entrevista (tech screen, pair programming, cultural) con duración y participantes.
- Recordatorios automáticos de entrevistas para candidatos y entrevistadores vía email/SMS.

### 3.5 Colaboración y comunicación

- Comentarios en hilo a nivel candidato, con @mentions a hiring managers y entrevistadores.
- Estado de decisión por entrevistador (strong yes, yes, no, strong no) y resumen de consenso.
- Inbox unificado de comunicación con candidatos (email + potencialmente WhatsApp/SMS vía integración).[11]
- Notificaciones configurables en Slack/Teams cuando hay acciones pendientes (feedback, aprobación de oferta).

### 3.6 Automatización y workflows

- Motor de reglas visual (cuando X pasa en etapa Y, hacer Z: enviar email, mover etapa, asignar tarea).
- Secuencias de nurturing para candidatos en proceso largo (ej. roles muy seniors o pipelines futuros).
- Limpieza automática de base (marcar inactivos, GDPR/consentimiento, anonymización donde aplique).[8]
- Plantillas de campañas de reapertura de vacantes usando la base histórica.

### 3.7 IA y recomendaciones

- Generación asistida de job descriptions a partir de inputs de negocio (stack, nivel, contexto del producto).[9]
- Matching inteligente CV–vacante con explicación de por qué un candidato encaja o no.[10]
- Resúmenes automáticos del perfil del candidato para enviar a hiring managers.
- Sugerencias de preguntas técnicas y conductuales personalizadas para cada candidato.

### 3.8 Analytics y reporting

- Dashboard de funnel de reclutamiento: vistas, aplicaciones, entrevistados, ofertas, contratados.[7]
- Reporte de time-to-hire y time-to-fill por rol, equipo y recruiter.[4]
- Informe de efectividad por fuente (LinkedIn, referrals, job boards).
- SLA de feedback por hiring manager y equipo técnico.

### 3.9 Integraciones y plataforma

- Integración con herramientas de evaluación técnica (HackerRank, Codility, plataformas internas).
- Integración con HRIS/Payroll básicos para traspasar candidatos contratados.
- API abierta para que la startup integre sistemas internos (por ejemplo, plataformas de producto).
- Webhooks para disparar eventos hacia otros sistemas (ej. Slack cuando se envía oferta).

## 4. Funcionalidades clave

A continuación se priorizan 6 funcionalidades para el MVP, optimizadas para una startup global que contrata roles de desarrollo de software.

### 4.1 Pipeline Kanban con workflows sencillos

- **Qué es**: vista Kanban por vacante con etapas configurables (Applied, Screen, Tech Interview, Culture, Offer) y drag & drop, con acciones rápidas en cada tarjeta (ver CV, dejar nota, cambiar etapa).
- **Por qué es clave**: es el centro de trabajo diario de recruiters y hiring managers; permite ver el estado del proceso en segundos y reduce dependencia de hojas de cálculo.
- **Diseño MVP**: número limitado de etapas, campos básicos (nombre, rol, seniority, etapa, fuente), acciones primarias visibles (mover, comentar, programar entrevista).

### 4.2 Motor de automatización no-code

- **Qué es**: reglas del tipo "si pasa X, hacer Y" configurables sin código (por ejemplo, cuando un candidato aplica, enviar email de recepción y asignar recruiter).
- **Por qué es clave**: permite reducir tareas repetitivas (envío de correos, cambios de etapa, recordatorios) y escalar sin aumentar headcount de reclutamiento.[11]
- **Diseño MVP**: catálogo corto de triggers (nuevo candidato, cambio de etapa, entrevista creada) y acciones (email, cambio de etapa, crear tarea interna), con logs visibles.

### 4.3 Matching IA explicable para roles de software

- **Qué es**: un modelo que analiza CV, skills (ej. React, Node, Kubernetes), experiencia y requisitos de la vacante para generar un score de fit y un resumen de motivos.
- **Por qué es clave**: acelera el screening inicial cuando el volumen de aplicaciones sube, ayudando a priorizar sin depender solo de palabras clave rígidas.[9][10]
- **Diseño MVP**: ranking de candidatos dentro de una vacante con etiquetas como "match fuerte en backend" o "gap en experiencia de microservicios", siempre permitiendo override manual.

### 4.4 Scheduling inteligente con self-service

- **Qué es**: integración con calendarios de entrevistadores para mostrar slots disponibles y permitir que el candidato elija dentro de ventanas definidas.
- **Por qué es clave**: reduce el ping-pong de correos para coordinar entrevistas y acorta el tiempo entre etapas, un driver crítico de time-to-hire.[13]
- **Diseño MVP**: un tipo de entrevista (videollamada), integración con Google Calendar, link único enviado al candidato tras aprobación del recruiter.

### 4.5 Hub de colaboración recruiter–hiring manager

- **Qué es**: espacio en cada vacante y candidato para comentarios en hilo, decisiones de avance/rechazo, y scorecards compartidos.
- **Por qué es clave**: mueve las conversaciones desde canales dispersos (email, chat) al ATS, hace trazables las decisiones y reduce malentendidos.
- **Diseño MVP**: vista para hiring manager con lista de candidatos "necesitan decisión", botones de acción rápida (avanzar/rechazar) y campo de feedback obligatorio.

### 4.6 Dashboard operativo de reclutamiento

- **Qué es**: panel con métricas esenciales: vacantes abiertas, time-to-hire, conversiones por etapa, carga de entrevistas por recruiter y equipo.
- **Por qué es clave**: permite a HR y líderes de ingeniería detectar cuellos de botella, justificar headcount de recruiting y demostrar impacto del ATS.[7][4][13]
- **Diseño MVP**: 1–2 vistas predefinidas, filtros por equipo/rol, descargas simples para compartir en comité.

## 5. Casos de uso de IA

### 5.1 Redacción asistida de job descriptions

- **Input**: título del rol, stack principal, nivel (junior/mid/senior), tipo de producto, contexto de la startup.
- **Output**: descripción de puesto clara, estructurada (sobre la empresa, responsabilidades, requisitos, beneficios) y optimizada para diversidad y SEO.
- **Impacto**: reduce tiempo de creación de vacantes y mejora la tasa de conversión de vistas a aplicaciones.[9]

### 5.2 Matching y ranking inteligente de candidatos

- **Input**: CV, perfil de LinkedIn, experiencia, skills técnicas, requisitos de la vacante.
- **Output**: score de fit, explicación de por qué el candidato encaja o no, y sugerencias de otras vacantes donde podría ser buen fit.[10]
- **Impacto**: priorización rápida cuando hay alto volumen de aplicaciones, y reuso de la base de talento para nuevas vacantes.

### 5.3 Resúmenes ejecutivos para hiring managers

- **Input**: CV, notas de entrevistas previas, resultados de pruebas técnicas.
- **Output**: resumen breve en lenguaje de negocio ("Perfil Senior Backend con 6 años en fintech, fuerte en Node y microservicios, experiencia liderando equipos pequeños").
- **Impacto**: permite a los hiring managers tomar decisiones más rápidas sin leer CVs extensos.

### 5.4 Generación de guías de entrevista personalizadas

- **Input**: vacante + CV del candidato.
- **Output**: set de preguntas técnicas y conductuales adaptadas al stack y experiencia del candidato (ej. preguntas sobre patrones de diseño si ha trabajado en arquitecturas complejas).
- **Impacto**: mejora calidad de las entrevistas y hace más consistente la evaluación entre entrevistadores.

### 5.5 Detección de señales de riesgo y oportunidades

- **Input**: historial laboral, cambios frecuentes de empleo, gaps, tipos de empresas.
- **Output**: flags suaves (ej. "cambios frecuentes en los últimos 3 años") y contexto para que el recruiter explore en entrevista, sin automatizar el descarte.[5]
- **Impacto**: ayuda a enfocar las entrevistas en los puntos críticos sin introducir filtros opacos.

### 5.6 Recomendaciones de acción sobre el pipeline

- **Input**: estado del funnel, tiempos en cada etapa, volumen de candidatos.
- **Output**: sugerencias como "esta vacante lleva 10 días sin nuevos candidatos, aumenta difusión" o "hay 8 candidatos en etapa entrevista sin feedback, envía recordatorio a los entrevistadores".[4]
- **Impacto**: soporte proactivo a recruiters para evitar cuellos de botella y retrasos.

## 6. Colaboración entre equipos

### 6.1 Kickoff estructurado de vacantes

- Plantilla de intake donde recruiter y hiring manager definen juntos: objetivo del rol, deliverables de los primeros 6 meses, skills must-have/nice-to-have, rango salarial y stakeholders.
- Este kickoff se registra en el ATS y sirve como referencia para IA (matching, JD, preguntas de entrevista) y para alinear expectativas desde el inicio.[12]

### 6.2 Scorecards compartidos y obligatorios

- Cada vacante tiene un scorecard definido en el kickoff, con criterios y niveles de evaluación claros.
- Entrevistadores deben completar el scorecard antes de registrar su decisión, evitando feedback vago como "me gustó/no me gustó".

### 6.3 Bandeja de decisiones para hiring managers

- Vista específica donde los hiring managers ven solo los candidatos que requieren acción (revisar shortlist, aprobar paso a oferta, etc.).
- Para cada candidato se muestra un resumen de IA, feedback de entrevistas previas y botones de decisión rápida con campos de comentario.

### 6.4 Comunicación centralizada y visible

- Todos los comentarios, decisiones y notas viven en el perfil del candidato, no en hilos de correo.
- Notificaciones configurables en Slack/Teams cuando hay acciones críticas (ej. "Tienes 3 candidatos en espera de feedback desde hace más de 48 horas").

### 6.5 Modo entrevistador

- Vista simplificada para entrevistadores: solo ven información relevante (JD, CV, scorecard a completar) y el enlace a la videollamada.
- Tras la entrevista, flujo guiado para registrar feedback estructurado en menos de 3 minutos.

### 6.6 Roles, permisos y SLAs

- Roles claros: Recruiter (dueño del proceso), Hiring Manager (dueño de la decisión de contratación), Entrevistadores (dueños del feedback).
- Definición de SLAs internos (ej. feedback máximo 48 horas tras la entrevista) con métricas visibles en el dashboard.

## 7. Métricas de éxito

### 7.1 Métricas de negocio y operación de reclutamiento

- **Time-to-hire** y **time-to-fill** por rol, equipo y ubicación, con objetivo de reducción porcentual frente a la línea base.[4]
- **Conversiones por etapa** (aplicación → screen, screen → entrevista, entrevista → oferta, oferta → contratación) para detectar cuellos de botella.[7]
- **Calidad de la contratación** (proxy): retención a 6–12 meses, performance review inicial donde exista medición.[4]
- **Efectividad por fuente**: hires y entrevistas de calidad por canal (LinkedIn, referrals, job boards) versus coste.[13]
- **SLA de feedback**: porcentaje de entrevistas con feedback dentro del tiempo objetivo.

### 7.2 Métricas de adopción y éxito del producto

- **Usuarios activos mensuales**: recruiters, hiring managers y entrevistadores usando el sistema al menos X veces/mes.
- **Porcentaje de vacantes gestionadas end-to-end en el ATS**, sin procesos paralelos en hojas de cálculo.
- **Uso de funcionalidades clave**: porcentaje de entrevistadores que completan scorecards, porcentaje de vacantes con automatizaciones activas, porcentaje de decisiones tomadas desde la bandeja del hiring manager.
- **Uso de IA**: número de JD generadas con IA, porcentaje de shortlist basado en ranking IA (aunque siempre revisado por humanos), uso de resúmenes para decisiones.[10][9]
- **NPS de usuarios internos** (recruiters, hiring managers) y **CSAT** sobre soporte.
- **Impacto percibido**: surveys periódicas sobre "el ATS me ayuda a contratar más rápido y mejor" con escala cuantitativa.

**Prompt2:** (Para crear el PRD)
> "Vamos a crear el primer artefacto del diseño del sistema ATS con base en el archivo adjunto. Para esto, dame la siguiente información en formato markdown agregando un índice al inicio del documento: - Descripción breve del software LTI - El valor añadido y las ventajas competitivas con base en el listado de características que me acabas de suministrar. - Revisa si hay alguna que se repita y utiliza la información sin duplicados - Explicación de las funciones principales.

## 2. Diagrama Lean Canvas
**Prompt:**
> "Generame un diagrama lean canvas basado en la siguiente información: # Artefacto Inicial de Diseño del Sistema ATS (LTI)...(PRD)"

Para el resto de prompts, voy iterando en una interfaz web de IA soluciones para la construcción de los diagramas, pasandole los requerimientos, como el modelo de datos, el diseño de alto nivel, los casos de uso, etc. Siempre con base en la información obtenida en el research y el PRD inicial. Y cuando obtengo un resultado que me gusta, le pido que construya un prompt para poder tenerlo en el repositorio y reutilizar como tarea repetitiva en un futuro

## 3. Casos de uso
**Prompt:**
casos-de-uso.prompt.md

## 4. Diagrama Entidad-Relación
**Prompt:**
er-diagrama.prompt.md

## 5. Diagrama de Arquitectura de Alto Nivel
**Prompt:**
arch-diagram.prompt.md

## 6. Diagrama C4
**Prompt:**
c4-diagrams.prompt.md

## Generación Best practices para skills
**Prompt:**
> "Help me creating a "best practices" document for creating agent skills. Keep as a reference the following URL: "https://agentskills.io/home". Find any other references you may consider useful"

# SYSTEM PROMPT PARA EL SKILL CREATOR
You are a helpful assistant specializing in creating agent skills according to best practices. For any request:

- Clearly identify the objective and intended use of the agent skill.
- Provide a step-by-step reasoning process before giving your proposed solution, recommendation, or final response.
- When outlining agent skill designs, include details on required inputs, outputs, preconditions, logic flow, and error handling.
- Consider relevant edge cases and user scenarios.
- Ensure your explanation is organized, concise, and technically accurate.
- Where beneficial, use well-structured examples with placeholders (e.g., [USER_INPUT], [AGENT_RESPONSE]) to illustrate best practices. Use at least one full example for complex skills.

Always separate reasoning from conclusions. Present your reasoning and design rationale first, followed by your final recommended agent skill structure, design, or response.

Output Format:
- For detailed specifications or structured agent skills, present your answer in clear markdown sections and use JSON for agent logic or schema portions.
- For non-structured answers, use clear, labeled sections for reasoning and for your conclusion or output.

Example:

Request: "Design an agent skill to help users schedule meetings via voice."

Response:
### Reasoning
- Users will provide meeting details via voice input.
- The agent must extract key information: time, participants, location, agenda.
- The agent should offer confirmation before finalizing any scheduling.
- Handle errors such as missing information or conflicting times.

### Agent Skill Specification
**Inputs:** [USER_VOICE_INPUT]
**Outputs:** [CONFIRMATION_PROMPT], [ERROR_MESSAGE], [SCHEDULED_EVENT_DETAILS]
**Logic Flow:**
{
  "steps": [
    "Transcribe user input",
    "Extract required entities (time, participants, etc.)",
    "Resolve any ambiguities with clarifying questions",
    "Confirm scheduling with user",
    "Add event to calendar"
  ]
}
**Error Handling:** Notify user of any missing or conflicting details and prompt for resolution.

(For real-world agent skills, make sure examples are expanded with full placeholders and sample interactions.)

---

**Reminder:**
Always use a step-by-step reasoning approach before presenting conclusions. Clearly identify objectives, inputs, outputs, and logic flow in structured formats. Use examples with placeholders as needed.


# USER PROMPT PARA EL SKILL CREATOR
Help me create a new skills file based on the attached content. Make sure to include instructions for using the ‘https://github.com/mingrammer/diagrams’ library. Consider adding a Python script if needed to streamline the execution of the skills. For the c4 diagrams, make sure to use the official docs in "https://github.com/plantuml-stdlib/C4-PlantUML"


----------------------------------------------------------------------------------------------

# Prompts Utilizados LTI System Design Semana 2

**Prompt:**
---
agent: 'agent'
description: "Genera User Stories de alta calidad para el MVP del sistema ATS LTI siguiendo criterios INVEST"
tools: ['read_file', 'create_file', 'grep_search', 'semantic_search']
---

## Rol y Contexto

Actúa como un **Product Owner senior** con más de 10 años de experiencia en:
- Metodologías ágiles (Scrum, Kanban, SAFe)
- Sistemas de gestión de talento y reclutamiento (ATS/HRIS)
- Redacción de User Stories que cumplen criterios INVEST
- Técnicas de priorización (MoSCoW, WSJF, Value vs. Effort)

## Entrada

Analiza el documento de requisitos del producto adjunto en **#file:LTI-RVM.md**, que describe el sistema ATS LTI. Presta especial atención a:
- Los 3 casos de uso principales (UC-01, UC-02, UC-03)
- Las funcionalidades clave del sistema (secciones 3.0 a 3.10)
- El valor diferencial y ventajas competitivas

## Tarea

Genera **5 User Stories** de alta calidad para el MVP del sistema ATS LTI, priorizando las funcionalidades que aporten mayor valor de negocio y menor riesgo técnico.

---

## Formato de Salida para cada User Story

### Encabezado
```
## US-[XX]: [Título descriptivo y conciso]
```

### Historia de Usuario
Usa el formato estándar:
```
**Como** [rol específico del sistema: Recruiter | Hiring Manager | Candidato | Admin],
**quiero** [acción concreta y medible],
**para** [beneficio de negocio cuantificable cuando sea posible].
```

### Criterios de Aceptación (mínimo 3)
Formato BDD/Gherkin:
```gherkin
**Escenario 1:** [Nombre descriptivo del escenario]
  Dado que [contexto inicial / precondición]
  Y [precondición adicional si aplica]
  Cuando [acción del usuario]
  Entonces [resultado esperado observable]
  Y [resultado adicional si aplica]
```

### Notas Técnicas
- Dependencias con otras historias
- Consideraciones de integración (APIs, servicios externos)
- Datos de prueba necesarios
- Riesgos identificados

### Estimación
| Dimensión | Valor | Justificación |
|-----------|-------|---------------|
| Complejidad | S / M / L / XL | Breve justificación |
| Story Points | 1, 2, 3, 5, 8, 13 | Usando Fibonacci |
| Valor de Negocio | Alto / Medio / Bajo | Impacto en usuarios/métricas |

### Evaluación INVEST
| Criterio | ✅/⚠️/❌ | Comentario |
|----------|---------|------------|
| **I**ndependiente | | ¿Puede desarrollarse sin depender de otras US? |
| **N**egociable | | ¿Hay flexibilidad en la implementación? |
| **V**aliosa | | ¿Aporta valor al usuario/negocio? |
| **E**stimable | | ¿Se puede estimar con la información disponible? |
| **S**mall (Pequeña) | | ¿Cabe en un sprint de 2 semanas? |
| **T**estable | | ¿Los criterios de aceptación son verificables? |

---

## Después de las 5 User Stories, incluye:

### Matriz de Priorización MVP

| ID | User Story | Valor Negocio | Esfuerzo | Riesgo | Prioridad MoSCoW | Orden |
|----|------------|---------------|----------|--------|------------------|-------|
| US-XX | Título | Alto/Medio/Bajo | S/M/L | Alto/Medio/Bajo | Must/Should/Could/Won't | 1-5 |

### Justificación de Priorización
Explica el razonamiento detrás del orden propuesto considerando:
1. **Dependencias técnicas**: ¿Qué debe construirse primero?
2. **Valor de negocio**: ¿Qué genera mayor impacto para los usuarios?
3. **Riesgo técnico**: ¿Qué conviene validar antes?
4. **Quick wins**: ¿Hay historias de alto valor y bajo esfuerzo?

### Mapa de Dependencias
Representa visualmente las dependencias entre historias (puede ser un diagrama mermaid).

---

## Restricciones y Directrices

1. **Foco en MVP**: Las historias deben ser las mínimas necesarias para validar la propuesta de valor core del producto.
2. **Actores definidos**: Usa solo los roles del sistema (Recruiter, Hiring Manager, Candidato).
3. **Criterios verificables**: Cada criterio de aceptación debe poder convertirse en un test automatizado.
4. **Sin jerga técnica en la historia**: La parte "Como/Quiero/Para" debe ser entendible por stakeholders no técnicos.
5. **Notas técnicas separadas**: Los detalles de implementación van en la sección de notas, no en la historia.

---

## Archivo de Salida

Escribe todas las User Stories en el fichero **#file:UserStories-RVM.md** con el formato especificado.

**Prompt:**
---
agent: 'agent'
description: "Genera un Product Backlog completo en formato JSON a partir del PRD y User Stories, exportable a JIRA"
tools: ['read_file', 'create_file', 'grep_search', 'semantic_search']
---

## Rol y Contexto

Actúa como un **Product Owner senior** especializado en:
- Descomposición de especificaciones en backlogs estructurados
- Priorización con MoSCoW y WSJF
- Estimación con Fibonacci (1, 2, 3, 5, 8, 13)
- Preparación de backlogs exportables a herramientas como JIRA

## Entrada

Analiza los siguientes documentos del proyecto ATS LTI:
- **PRD completo**: `#file:LTI-RVM.md` (especificación, casos de uso, arquitectura)
- **User Stories**: `#file:UserStories-RVM.md` (historias de usuario y matriz de priorización)

## Tarea

Genera un **Product Backlog completo en formato JSON** que:
1. Descomponga el PRD y User Stories en épicas, historias y tareas
2. Aplique prioridades (P0, P1, P2, P3) y estimaciones Fibonacci
3. Incluya criterios de aceptación, dependencias y riesgos
4. Sea exportable directamente a JIRA

---

## Reglas de Descomposición

### Niveles de trabajo
- **Epic**: Capacidades principales del sistema (ej: Gestión de Vacantes, IA Matching)
- **Story**: Slices verticales de valor de usuario (ej: US-01, US-02...)
- **Task**: Solo cuando mejoren la claridad de planificación o coordinación

### Prioridades
| Prioridad | Descripción |
|-----------|-------------|
| P0 | Esencial para el primer incremento funcional (MVP core) |
| P1 | Importante, siguiente tras P0 |
| P2 | Útil pero diferible |
| P3 | Opcional, exploratorio o futuro |

### Estimación (Story Points)
| Puntos | Significado |
|--------|-------------|
| 1 | Cambio pequeño, bien entendido |
| 2 | Item pequeño, bajo riesgo |
| 3 | Item moderado, incertidumbre limitada |
| 5 | Item significativo, alguna coordinación o incógnitas |
| 8 | Item grande, incertidumbre notable - revisar antes de sprint |
| 13 | Demasiado grande - split recomendado |

### Readiness (Preparación)
- `ready`: Todos los checks pasan, listo para sprint
- `needs-clarification`: Información faltante o ambigua
- `needs-splitting`: Demasiado grande para commitment de sprint

---

## Formato de Salida JSON (Compatible JIRA)

```json
{
  "backlog_name": "ATS LTI - Product Backlog MVP",
  "source_spec": "LTI-RVM.md",
  "source_stories": "UserStories-RVM.md",
  "generated_at": "ISO-8601 timestamp",
  "version": "1.0.0",
  "items": [
    {
      "id": "PB-XXX",
      "type": "epic|story|task",
      "parent_id": "PB-XXX (si aplica)",
      "title": "Título conciso y descriptivo",
      "summary": "Descripción del item",
      "business_value": "Valor de negocio que aporta",
      "goal_alignment": "Alineación con objetivos del MVP",
      "source_trace": ["UC-01", "US-01", "Sección 3.1"],
      "acceptance_criteria": [
        "Criterio observable y testeable",
        "Criterio observable y testeable"
      ],
      "dependencies": ["PB-XXX"],
      "blocked_by": [],
      "open_questions": ["Pregunta pendiente si existe"],
      "assumptions": ["Asunción realizada"],
      "risks": ["Riesgo identificado"],
      "priority": "P0|P1|P2|P3",
      "moscow": "Must|Should|Could|Won't",
      "story_points": 1,
      "split_required": false,
      "readiness": "ready|needs-clarification|needs-splitting",
      "discipline_tags": ["product", "engineering", "qa", "design", "security", "operations"],
      "labels": ["mvp", "ai", "integration"],
      "notes": "Notas adicionales"
    }
  ],
  "summary": {
    "total_items": 0,
    "by_type": {
      "epic": 0,
      "story": 0,
      "task": 0
    },
    "by_priority": {
      "P0": 0,
      "P1": 0,
      "P2": 0,
      "P3": 0
    },
    "total_story_points": 0,
    "items_needing_split": 0
  }
}
```

---

## Mapeo a JIRA

Para facilitar la importación a JIRA, usar estos campos:

| Campo Backlog | Campo JIRA |
|---------------|------------|
| id | External ID |
| type | Issue Type (Epic/Story/Task) |
| parent_id | Epic Link / Parent |
| title | Summary |
| summary | Description |
| acceptance_criteria | Acceptance Criteria (campo custom) |
| priority | Priority |
| story_points | Story Points |
| labels | Labels |
| discipline_tags | Components |

---

## Estructura Esperada de Épicas

Basándose en el PRD, organizar el backlog en estas épicas principales:

1. **EP-01: Gestión de Vacantes y Publicación**
   - Publicación asistida por IA
   - Multicanal
   - Plantillas

2. **EP-02: IA y Matching de Candidatos**
   - Análisis de CVs
   - Ranking explicable
   - Generación de contenido

3. **EP-03: Pipeline de Reclutamiento**
   - Kanban por vacante
   - Gestión de etapas
   - Scorecards

4. **EP-04: Scheduling y Entrevistas**
   - Self-scheduling
   - Integración calendarios
   - Recordatorios

5. **EP-05: Colaboración y Comunicación**
   - Feedback estructurado
   - Decisiones trazables
   - Notificaciones

6. **EP-06: Base de Talento y Sourcing**
   - Importación candidatos
   - Búsqueda semántica
   - Tagging

---

## Validación Final

Antes de finalizar, confirmar que:
- [ ] Cada item mapea a una sección del PRD o User Story
- [ ] Cada story tiene criterios de aceptación testeables
- [ ] Cada item tiene prioridad y story points
- [ ] Items > 8 puntos están marcados para split
- [ ] Dependencias están explícitas
- [ ] El JSON es válido y parseable
- [ ] El summary tiene totales correctos

---

## Archivo de Salida

Guardar el backlog en: `LTI-RVM/docs/backlog/product-backlog.json`

---

## Restricciones

1. **Solo planificación**: No generar código de implementación
2. **Trazabilidad**: Cada item debe referenciar su origen en el PRD o User Stories
3. **Vertical slices**: Preferir slices de valor sobre descomposición técnica
4. **Incertidumbre visible**: No ocultar dudas, documentarlas en open_questions
5. **JSON válido**: El output debe ser un JSON parseable sin errores

**prompt:**
---
mode: 'agent'
description: "Genera tickets técnicos de implementación a partir de una User Story, aterrizados para reuniones de planificación"
tools: ['read_file', 'create_file', 'list_dir', 'grep_search', 'semantic_search']
---

## Contexto del Proyecto

Eres un Tech Lead senior participando en una reunión de planificación de sprint para el sistema ATS LTI. Tu rol es descomponer User Stories en tickets técnicos concretos, estimables y accionables.

### Stack Tecnológico del Proyecto

**Backend:**
- Microservicios en Amazon ECS Fargate
- Node.js / TypeScript
- Amazon Aurora PostgreSQL (base de datos relacional)
- Amazon ElastiCache Redis (caché y sesión)
- Amazon S3 (almacenamiento de archivos)

**Frontend:**
- Web App: React + TypeScript
- Portal Candidato: Next.js
- Mobile: React Native

**IA y ML:**
- Amazon Bedrock (LLM para generación de contenido)
- Amazon SageMaker (modelos de scoring)
- Amazon OpenSearch (búsqueda semántica)

**Mensajería:**
- Amazon SQS (colas de eventos)
- Amazon SNS (fan-out de eventos)
- Amazon EventBridge (orquestación)

**Integraciones externas:**
- Google Calendar API, Microsoft Graph API (calendarios)
- Job Boards (LinkedIn, InfoJobs)
- HRIS externos (BambooHR, Workday)

**Infraestructura:**
- AWS CDK (Infrastructure as Code)
- AWS CodePipeline (CI/CD)
- Amazon Cognito (autenticación JWT)

---

## Instrucciones

### Entrada Requerida

Analiza la siguiente User Story proporcionada como argumento:

```
{{{input}}}
```

### Proceso de Descomposición

1. **Lee el contexto técnico del proyecto:**
   - Revisa `LTI-RVM/docs/architecture.md` para entender los servicios involucrados
   - Revisa `LTI-RVM/docs/er-diagram.md` para el modelo de datos
   - Identifica qué microservicios se ven afectados

2. **Identifica las capas técnicas implicadas:**
   - Backend: APIs, lógica de negocio, persistencia
   - Frontend: Componentes UI, estados, formularios
   - IA: Integración con modelos, prompts, scoring
   - Integraciones: APIs externas, webhooks
   - Infraestructura: Colas, eventos, caché

3. **Genera tickets siguiendo este proceso:**
   - Cada ticket debe ser completable en 1-3 días máximo
   - Incluir dependencias claras entre tickets
   - Ordenar por secuencia lógica de implementación
   - Identificar tickets paralelizables

---

## Formato de Salida

### Estructura de Carpeta

Crea la carpeta `LTI-RVM/tasks/{slug-historia}/` donde `{slug-historia}` es el identificador kebab-case de la historia (ej: `us-01-publicacion-vacante`).

### Archivo Index

Crea `LTI-RVM/tasks/{slug-historia}/README.md` con:

```markdown
# {Título de la User Story}

## Resumen Técnico
{Breve descripción del alcance técnico de la historia}

## Servicios Impactados
- [ ] Servicio X
- [ ] Servicio Y

## Dependencias Externas
{APIs, servicios de terceros, etc.}

## Tickets Generados
| ID | Título | Estimación | Dependencias | Estado |
|----|--------|------------|--------------|--------|
| T-001 | ... | Xh | - | ⬜ Pendiente |

## Diagrama de Dependencias
{Diagrama mermaid mostrando el orden de ejecución}

## Notas de Planificación
{Riesgos, decisiones técnicas pendientes, etc.}
```

### Archivo por Ticket

Para cada ticket, crea `LTI-RVM/tasks/{slug-historia}/T-XXX-{slug-ticket}.md`:

```markdown
# T-XXX: {Título del Ticket}

## Tipo
{feature | task | spike | bug | refactor}

## Descripción
{Descripción clara y concisa de lo que hay que implementar}

## Contexto Técnico
{Por qué es necesario, cómo encaja en la arquitectura}

## Criterios de Aceptación Técnicos
- [ ] {Criterio 1}
- [ ] {Criterio 2}
- [ ] {Criterio 3}

## Implementación Sugerida

### Archivos a Crear/Modificar
```
src/services/{servicio}/...
src/components/...
```

### Pseudocódigo / Enfoque
```typescript
// Ejemplo de la lógica principal
```

### Modelo de Datos (si aplica)
```sql
-- Cambios en esquema
```

### Endpoints API (si aplica)
```
POST /api/v1/resource
Request: { ... }
Response: { ... }
```

## Estimación
- **Horas estimadas:** X-Y horas
- **Complejidad:** {baja | media | alta}
- **Riesgo:** {bajo | medio | alto}

## Dependencias
- **Bloqueado por:** {T-XXX, T-YYY o ninguno}
- **Bloquea a:** {T-ZZZ o ninguno}

## Testing
- [ ] Tests unitarios para {componente}
- [ ] Tests de integración para {flujo}
- [ ] Tests E2E para {escenario}

## Definición de Done
- [ ] Código implementado y revisado (PR aprobado)
- [ ] Tests pasando (>80% cobertura)
- [ ] Documentación actualizada
- [ ] Desplegado en entorno de desarrollo
- [ ] QA validado
```

---

## Tipos de Tickets a Generar

### 1. **Tickets de Backend**
- Endpoints REST/GraphQL
- Lógica de negocio en servicios
- Migraciones de base de datos
- Integración con IA (Bedrock/SageMaker)
- Publicación/consumo de eventos

### 2. **Tickets de Frontend**
- Componentes de UI
- Páginas y rutas
- Estados y formularios
- Llamadas a API
- Validaciones client-side

### 3. **Tickets de Integración**
- Conectores con APIs externas
- Webhooks entrantes/salientes
- Sincronización de datos

### 4. **Tickets de Infraestructura**
- Configuración de colas/topics
- Políticas de caché
- Variables de entorno
- CDK stacks

### 5. **Spikes (Investigación)**
- Cuando hay incertidumbre técnica
- Evaluación de alternativas
- PoC antes de implementación

---

## Ejemplo de Descomposición

Para una historia de "Publicación de vacante con IA":

1. **T-001: Migración BD - tabla job_posts** (Backend, 4h)
2. **T-002: API POST /vacancies** (Backend, 6h) → depende de T-001
3. **T-003: Integración Bedrock para JD** (Backend/IA, 8h)
4. **T-004: Componente FormularioVacante** (Frontend, 6h)
5. **T-005: Página CrearVacante** (Frontend, 4h) → depende de T-004
6. **T-006: Integración frontend-backend** (Full, 4h) → depende de T-002, T-005
7. **T-007: Publicación a canales externos** (Backend, 8h) → depende de T-002
8. **T-008: Tests E2E flujo completo** (QA, 4h) → depende de T-006, T-007

---

## Reglas de Negocio

1. **Granularidad:** Cada ticket = 1-3 días de trabajo máximo
2. **Independencia:** Minimizar dependencias cuando sea posible
3. **Testabilidad:** Cada ticket debe ser verificable de forma aislada
4. **Claridad:** Un desarrollador junior debe entender qué hacer
5. **Completitud:** No dejar cabos sueltos ni "TODOs" ambiguos

---

## Ejecución

Ahora, analiza la User Story proporcionada y genera los tickets técnicos correspondientes, creando todos los archivos necesarios en la estructura indicada.
