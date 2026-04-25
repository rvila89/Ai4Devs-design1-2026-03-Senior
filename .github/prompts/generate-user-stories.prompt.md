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
