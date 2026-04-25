# T-010: Página - Crear/Editar Vacante

## 1. Título Claro y Conciso

> Implementar la página completa de creación y edición de vacantes integrando los componentes de formulario, editor JD con IA, y selector de canales.

---

## 2. Descripción Detallada

### Propósito
Proveer la vista completa donde el Recruiter puede crear una nueva vacante o editar una existente, siguiendo un flujo guiado desde los datos básicos hasta la publicación.

### Detalles Específicos

**Layout de la página:**

```
┌─────────────────────────────────────────────────┐
│  Header: Crear Nueva Vacante / Editar [título]  │
├─────────────────────────────────────────────────┤
│  Progress Steps: 1. Datos │ 2. Descripción │ 3. Publicar │
├─────────────────────────────────────────────────┤
│                                                 │
│  [Contenido del paso actual]                   │
│                                                 │
├─────────────────────────────────────────────────┤
│  Footer: [Anterior] [Guardar borrador] [Siguiente/Publicar] │
└─────────────────────────────────────────────────┘
```

**Pasos del wizard:**
1. **Datos básicos**: FormularioVacante (T-007)
2. **Job Description**: EditorJD con IA (T-008)
3. **Publicar**: SelectorCanales (T-009) + Confirmación

**Rutas:**
- `/vacancies/new` - Crear nueva
- `/vacancies/:id/edit` - Editar existente

### Contexto Técnico
- Router: React Router v6
- Estado: React Query para datos, Zustand para wizard state
- URL params para mantener estado en navegación

---

## 3. Criterios de Aceptación

### Expectativas Claras
- [ ] Wizard de 3 pasos funcional
- [ ] Navegación entre pasos con validación
- [ ] Modo crear y editar funcionan correctamente
- [ ] Guardar borrador disponible en cualquier paso
- [ ] Publicar solo habilitado cuando todo está completo

### Pruebas de Validación
- [ ] Test de navegación completa del wizard
- [ ] Test de validación entre pasos
- [ ] Test de modo edición con datos precargados
- [ ] Test de publicación exitosa

---

## 4. Prioridad

| Nivel | Urgencia | Justificación |
|-------|----------|---------------|
| Media | Normal | Integra componentes previos, necesario para demo end-to-end |

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
| Sprint | Sprint 2 |

---

## 8. Notas y Comentarios

### Consideraciones Técnicas
- Usar Suspense boundaries para carga de componentes
- Implementar autosave cada 30 segundos
- Mantener estado en URL para permitir refresh

### Preguntas Abiertas
- [ ] ¿Permitir saltar pasos o solo secuencial?

### Decisiones de Diseño
- Wizard secuencial con posibilidad de volver atrás
- Estado del wizard persiste en sessionStorage

### Riesgos Identificados

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Pérdida de datos por navegación | Media | Medio | Autosave + confirmación de salida |

---

## 9. Enlaces y Referencias

| Tipo | Enlace/Referencia |
|------|-------------------|
| User Story origen | US-01: Publicación de vacante asistida por IA |
| Diseño/Mockup | Por definir (Figma) |
| Tickets relacionados | T-007, T-008, T-009 (prerequisitos), T-011 (integración) |

---

## 10. Historial de Cambios

| Fecha | Autor | Cambio | Versión |
|-------|-------|--------|---------|
| 2026-04-25 | Tech Lead | Creación inicial del ticket | v1.0 |
