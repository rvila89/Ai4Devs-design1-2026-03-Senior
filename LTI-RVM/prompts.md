# Prompts Utilizados LTI System Design

Secuencia de prompts para poder generar los artefactos de diseño y producto para el proyecto LTI ATS.

## 1. Product Discovery & Vision
**Prompt:** (Metaprompt para ats research)
> "Necesito crear un prompt con base en el siguiente texto que describe un sistema ATS (applicant Tracking System): "Todavía no hay nada creado, así que toca ponerse el gorro de product manager y definir esas funcionalidades clave que harán brillar a LTI por encima de los competidores: aumentar la eficiencia para los departamentos de HR, mejorar la colaboración en tiempo real entre reclutadores y managers, automatizaciones, asistencia de IA en diversas tareas...es el momento de hacer brainstorming, investigar cuáles pueden ser las claves del éxito, y dejarlo plasmado para el resto del equipo. Genera dos prompts, uno de sistema y otro de usuario"

** Ejecuto en perplexity.ai en un nuevo espacio los dos prompts generados, para obtener el research de ATS que luego utilizaremos para crear el PRD y demás artefactos.

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




