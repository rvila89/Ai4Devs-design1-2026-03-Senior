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

---------

# Documento de Definición – Sistema ATS (LTI)

## Índice
1. Descripción breve del software LTI  
2. Valor añadido y ventajas competitivas  
3. Funciones principales del sistema  

---

## 1. Descripción breve del software LTI

LTI es un sistema ATS (Applicant Tracking System) diseñado para startups tecnológicas globales que buscan optimizar sus procesos de reclutamiento. Su enfoque principal es simplificar la operación diaria de recruiters y hiring managers, mejorar la experiencia del candidato y aumentar la calidad de contratación mediante automatización inteligente, colaboración centralizada e inteligencia artificial explicable.

El sistema actúa como una plataforma unificada donde se gestionan vacantes, candidatos, entrevistas, decisiones y métricas, eliminando la fragmentación de herramientas y procesos paralelos.

---

## 2. Valor añadido y ventajas competitivas

LTI se diferencia de los ATS tradicionales en los siguientes aspectos clave:

### Simplicidad operativa real
- Interfaces intuitivas diseñadas para usuarios no técnicos.
- Reducción significativa de la curva de aprendizaje.
- Flujos optimizados con pocas acciones para tareas críticas.

### Colaboración centralizada
- Reclutadores y hiring managers trabajan en un único sistema.
- Eliminación de comunicación dispersa (email, Slack, hojas de cálculo).
- Trazabilidad completa de decisiones y feedback.

### Automatización útil y controlada
- Motor no-code enfocado en tareas repetitivas (no decisiones críticas).
- Transparencia total (logs, override manual).
- Mejora del time-to-hire sin perder control humano.

### IA asistiva y explicable
- Matching inteligente con justificación (no caja negra).
- Generación de contenido (JD, resúmenes, preguntas).
- Priorización de candidatos basada en contexto real, no solo keywords.

### Datos accionables
- Dashboards operativos claros (no solo exportación de datos).
- Métricas orientadas a negocio (no solo HR).
- Identificación rápida de cuellos de botella.

### Experiencia de candidato mejorada
- Procesos simples, claros y mobile-friendly.
- Scheduling self-service.
- Comunicación más rápida y consistente.

### Integración y extensibilidad
- Integraciones con herramientas clave (calendar, HRIS, evaluaciones técnicas).
- API y webhooks para ecosistema tecnológico.
- Eliminación de silos de información.

---

## 3. Funciones principales del sistema

### 3.1 Gestión de candidatos y sourcing
- Importación de candidatos desde múltiples fuentes.
- Base de talento centralizada con tagging estructurado.
- Búsqueda semántica por skills y experiencia.
- Recomendaciones automáticas desde la base existente.

---

### 3.2 Gestión de vacantes
- Creación de vacantes con plantillas especializadas.
- Publicación multicanal desde un solo punto.
- Página de carreras personalizable.
- Librería de job descriptions optimizadas.

---

### 3.3 Pipeline de reclutamiento
- Vista Kanban por vacante con drag & drop.
- Etapas configurables del proceso.
- Acciones rápidas sobre candidatos (mover, comentar, evaluar).
- Visualización clara del estado del funnel.

---

### 3.4 Screening y evaluación
- Scorecards estructurados por rol.
- Preguntas knockout configurables.
- Ranking automático de candidatos.
- Evaluación consistente entre entrevistadores.

---

### 3.5 Entrevistas y scheduling
- Integración con calendarios (Google/Outlook).
- Self-scheduling para candidatos.
- Paneles de entrevista predefinidos.
- Recordatorios automáticos.

---

### 3.6 Colaboración y comunicación
- Comentarios en hilo por candidato.
- Sistema de decisiones estructuradas.
- Inbox unificado de comunicación.
- Notificaciones integradas con herramientas externas.

---

### 3.7 Automatización y workflows
- Motor visual no-code (trigger → acción).
- Automatización de tareas repetitivas.
- Secuencias de nurturing.
- Gestión de base de datos (limpieza, consentimiento).

---

### 3.8 Inteligencia artificial
- Generación de job descriptions.
- Matching candidato–vacante con explicación.
- Resúmenes automáticos para hiring managers.
- Generación de preguntas de entrevista.
- Recomendaciones sobre el pipeline.

---

### 3.9 Analytics y reporting
- Dashboard de funnel de reclutamiento.
- Métricas de time-to-hire y conversiones.
- Análisis de fuentes de talento.
- Seguimiento de SLA de feedback.

---

### 3.10 Integraciones y plataforma
- Integraciones con herramientas externas clave.
- API abierta.
- Webhooks para eventos.
- Sincronización con sistemas de HR.

# Lean Canvas Diagram
/context/lean-canvas-ats.drawio

# Use Cases
/docs/use-cases.md

# Entidad Relacion Diagram
/docs/er-diagram.md

# High Level Architecture Diagram
/docs/architecture.md

# C4 Diagrams
/docs/c4-diagrams.md

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