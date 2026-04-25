# T-007: Componente UI - Formulario de vacante

## 1. Título Claro y Conciso

> Crear el componente React reutilizable de formulario para capturar los datos básicos de una vacante (título, departamento, ubicación, requisitos, etc.).

---

## 2. Descripción Detallada

### Propósito
Proveer un formulario estructurado y validado que capture toda la información necesaria para crear una vacante, sirviendo como input para la generación de JD con IA.

### Detalles Específicos

**Campos del formulario:**

| Campo | Tipo | Validación | Requerido |
|-------|------|------------|-----------|
| title | text | min 5, max 100 chars | Sí |
| department | select | de catálogo | Sí |
| location | text/autocomplete | - | Sí |
| employment_type | select | full-time/part-time/contract | Sí |
| experience_level | select | junior/mid/senior/lead | Sí |
| salary_min | number | >= 0 | No |
| salary_max | number | >= salary_min | No |
| currency | select | EUR/USD/GBP | Si hay salario |
| requirements | textarea/tags | - | Sí |
| responsibilities | textarea | - | No |
| benefits | textarea/tags | - | No |

**Comportamiento:**
- Validación en tiempo real con feedback visual
- Guardado automático en localStorage (draft)
- Responsive design
- Accesibilidad WCAG 2.1 AA

### Contexto Técnico
- Framework: React 18 + TypeScript
- Form library: React Hook Form
- Validación: Zod (compartido con backend)
- UI: Design System existente (si aplica)

---

## 3. Criterios de Aceptación

### Expectativas Claras
- [ ] Todos los campos renderizados correctamente
- [ ] Validaciones funcionan en blur y submit
- [ ] Mensajes de error claros y accesibles
- [ ] Draft se guarda automáticamente
- [ ] Formulario es responsive

### Pruebas de Validación
- [ ] Test de renderizado de todos los campos
- [ ] Test de validaciones (campo vacío, formato inválido)
- [ ] Test de submit exitoso con datos válidos
- [ ] Test de accesibilidad (jest-axe)

---

## 4. Prioridad

| Nivel | Urgencia | Justificación |
|-------|----------|---------------|
| Media | Normal | Componente base para la página, puede desarrollarse en paralelo al backend |

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
| Responsable | Frontend Dev |
| Equipo | Frontend Team |
| Revisor Código | Frontend Lead |
| Revisor QA | QA Engineer |

---

## 7. Etiquetas / Tags

| Categoría | Valor |
|-----------|-------|
| Tipo | feature |
| Capa | frontend |
| Componente | web-app |
| Módulo | vacantes |
| Sprint | Sprint 1 |

---

## 8. Notas y Comentarios

### Consideraciones Técnicas
- Usar React Hook Form para performance con muchos campos
- Schemas Zod importados del paquete compartido con backend
- Componente debe ser composable para uso en crear/editar

### Preguntas Abiertas
- [ ] ¿Existe design system definido para inputs?

### Decisiones de Diseño
- Se usa controlled components para validación en tiempo real
- El componente expone callbacks onSubmit y onChange

### Riesgos Identificados

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Cambios en campos requeridos | Media | Bajo | Diseño flexible con config |

---

## 9. Enlaces y Referencias

| Tipo | Enlace/Referencia |
|------|-------------------|
| User Story origen | US-01: Publicación de vacante asistida por IA |
| Diseño/Mockup | Por definir (Figma) |
| Tickets relacionados | T-008 (depende de este), T-010 (depende de este) |

---

## 10. Historial de Cambios

| Fecha | Autor | Cambio | Versión |
|-------|-------|--------|---------|
| 2026-04-25 | Tech Lead | Creación inicial del ticket | v1.0 |
