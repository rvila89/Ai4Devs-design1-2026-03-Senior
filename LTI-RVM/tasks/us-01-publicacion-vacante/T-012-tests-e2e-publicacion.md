# T-012: Tests E2E - Flujo completo de publicación de vacante

## 1. Título Claro y Conciso

> Implementar suite de tests end-to-end que validen el flujo completo de creación y publicación de vacantes con IA.

---

## 2. Descripción Detallada

### Propósito
Garantizar la calidad y estabilidad del flujo de publicación de vacantes mediante tests automatizados que simulen el comportamiento real del usuario.

### Detalles Específicos

**Escenarios de test:**

1. **Happy Path - Publicación exitosa**
   - Login como Recruiter
   - Crear nueva vacante con datos válidos
   - Generar JD con IA
   - Seleccionar canales integrados
   - Publicar y verificar confirmación

2. **Edición de JD generado**
   - Generar JD con IA
   - Editar manualmente
   - Verificar que cambios persisten

3. **Regeneración de JD**
   - Generar JD
   - Click en regenerar
   - Verificar nuevo contenido

4. **Canal no integrado**
   - Verificar que canal no integrado está deshabilitado
   - Verificar tooltip explicativo

5. **Error handling**
   - Simular error de API de IA
   - Verificar mensaje de error y retry

### Contexto Técnico
- Framework: Playwright
- Entorno: Staging con servicios reales o mocks
- CI: Ejecutar en cada PR

---

## 3. Criterios de Aceptación

### Expectativas Claras
- [ ] Todos los escenarios críticos cubiertos
- [ ] Tests ejecutan en < 5 minutos
- [ ] Tests son estables (no flaky)
- [ ] Reports generados con screenshots en fallo

### Pruebas de Validación
- [ ] Tests pasan en CI consistentemente
- [ ] Coverage de los 3 escenarios de la US
- [ ] Tests pueden ejecutarse en local

---

## 4. Prioridad

| Nivel | Urgencia | Justificación |
|-------|----------|---------------|
| Baja | Diferible | Puede hacerse post-integración, pero necesario antes de release |

---

## 5. Estimación de Esfuerzo

| Métrica | Valor |
|---------|-------|
| Story Points | 3 |
| Horas Estimadas | 5-6 horas |
| Complejidad Técnica | Media |
| Riesgo Técnico | Bajo |
| Incertidumbre | Baja |

---

## 6. Asignación

| Rol | Responsabilidad |
|-----|-----------------|
| Responsable | QA Engineer |
| Equipo | QA Team |
| Revisor Código | QA Lead |
| Revisor QA | Dev que implementó features |

---

## 7. Etiquetas / Tags

| Categoría | Valor |
|-----------|-------|
| Tipo | task |
| Capa | qa |
| Componente | e2e-tests |
| Módulo | vacantes |
| Sprint | Sprint 3 |

---

## 8. Notas y Comentarios

### Consideraciones Técnicas
- Usar Page Object Model para mantenibilidad
- Implementar data fixtures para tests repetibles
- Considerar visual regression tests para UI crítica

### Preguntas Abiertas
- [ ] ¿Usar mocks de APIs externas o servicios reales en staging?

### Decisiones de Diseño
- Se priorizan tests de happy path y errores críticos
- Tests son independientes (pueden ejecutarse en cualquier orden)

### Riesgos Identificados

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Flakiness por timing | Media | Medio | Usar waitFor apropiados, retry en CI |

---

## 9. Enlaces y Referencias

| Tipo | Enlace/Referencia |
|------|-------------------|
| User Story origen | US-01: Publicación de vacante asistida por IA |
| Documentación técnica | Playwright Docs |
| Tickets relacionados | T-011 (prerequisito) |

---

## 10. Historial de Cambios

| Fecha | Autor | Cambio | Versión |
|-------|-------|--------|---------|
| 2026-04-25 | Tech Lead | Creación inicial del ticket | v1.0 |
