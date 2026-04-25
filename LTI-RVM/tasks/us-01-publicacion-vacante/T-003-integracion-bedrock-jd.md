# T-003: Integración Amazon Bedrock - Generación de Job Description con IA

## 1. Título Claro y Conciso

> Implementar el servicio de integración con Amazon Bedrock para generar job descriptions optimizados a partir de los datos básicos de la vacante.

---

## 2. Descripción Detallada

### Propósito
Permitir que el sistema genere automáticamente descripciones de trabajo profesionales y atractivas usando modelos de lenguaje de Amazon Bedrock, reduciendo el tiempo de creación de vacantes y mejorando la calidad del contenido.

### Detalles Específicos

**Endpoint requerido:**
| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | /api/v1/ai/generate-job-description | Genera JD basado en inputs |

**Input esperado:**
```json
{
  "title": "Senior Software Engineer",
  "department": "Engineering",
  "location": "Madrid, España",
  "requirements": ["5+ años experiencia", "Node.js", "AWS"],
  "responsibilities": ["Diseño de arquitectura", "Mentoring"],
  "salary_range": { "min": 50000, "max": 70000, "currency": "EUR" },
  "tone": "professional" | "casual" | "formal"
}
```

**Output esperado:**
```json
{
  "job_description": "...(texto generado)...",
  "summary": "...(resumen corto)...",
  "keywords": ["node.js", "aws", "senior"],
  "estimated_reach": 15000,
  "generation_id": "uuid",
  "model_version": "claude-3-sonnet"
}
```

### Contexto Técnico
- Servicio: ai-service (microservicio independiente)
- Modelo: Amazon Bedrock con Claude 3 Sonnet o Titan
- Prompt engineering: Templates versionados y configurables
- Timeout: 30 segundos máximo
- Retry policy: 3 intentos con backoff exponencial

---

## 3. Criterios de Aceptación

### Expectativas Claras
- [ ] Endpoint genera JD coherente y profesional en español e inglés
- [ ] Tiempo de respuesta < 15 segundos en percentil 95
- [ ] Manejo de errores de Bedrock con fallback graceful
- [ ] Logs de cada generación para auditoría y mejora de prompts
- [ ] Rate limiting implementado (máx 10 requests/minuto por usuario)

### Pruebas de Validación
- [ ] Test con diferentes combinaciones de input
- [ ] Test de timeout y manejo de errores
- [ ] Test de rate limiting
- [ ] Validación de calidad de output (revisión manual de samples)

---

## 4. Prioridad

| Nivel | Urgencia | Justificación |
|-------|----------|---------------|
| Alta | Crítica | Feature diferenciador de la US. Sin IA no hay valor agregado principal. |

---

## 5. Estimación de Esfuerzo

| Métrica | Valor |
|---------|-------|
| Story Points | 5 |
| Horas Estimadas | 6-8 horas |
| Complejidad Técnica | Media-Alta |
| Riesgo Técnico | Medio |
| Incertidumbre | Media |

---

## 6. Asignación

| Rol | Responsabilidad |
|-----|-----------------|
| Responsable | Backend Dev (especialista IA) |
| Equipo | Backend Team |
| Revisor Código | Tech Lead |
| Revisor QA | QA Engineer |

---

## 7. Etiquetas / Tags

| Categoría | Valor |
|-----------|-------|
| Tipo | feature |
| Capa | backend |
| Componente | ai-service |
| Módulo | vacantes, ia |
| Sprint | Sprint 1 |

---

## 8. Notas y Comentarios

### Consideraciones Técnicas
- Almacenar prompts en archivos de configuración para iteración rápida
- Implementar feature flag para cambiar entre modelos de Bedrock
- Considerar caché de respuestas similares (mismo título + dept)

### Preguntas Abiertas
- [ ] ¿Cuál modelo de Bedrock usar: Claude 3 Sonnet vs Titan Text?
- [ ] ¿Se requiere soporte para múltiples idiomas desde el inicio?

### Decisiones de Diseño
- Se genera un ID único por generación para trazabilidad
- El prompt incluye instrucciones de longitud y estructura deseada
- Se retorna keywords extraídos para SEO y matching futuro

### Riesgos Identificados

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Latencia alta de Bedrock | Media | Medio | UX con loading state, timeout configurable |
| Calidad variable de outputs | Media | Medio | Iteración de prompts, opción de regenerar |
| Costos de API altos | Baja | Medio | Rate limiting, monitoreo de uso |

---

## 9. Enlaces y Referencias

| Tipo | Enlace/Referencia |
|------|-------------------|
| User Story origen | US-01: Publicación de vacante asistida por IA |
| Documentación técnica | AWS Bedrock Developer Guide |
| Especificación API | Por definir (OpenAPI 3.0) |
| Tickets relacionados | T-008 (frontend), T-011 (integración) |

---

## 10. Historial de Cambios

| Fecha | Autor | Cambio | Versión |
|-------|-------|--------|---------|
| 2026-04-25 | Tech Lead | Creación inicial del ticket | v1.0 |
