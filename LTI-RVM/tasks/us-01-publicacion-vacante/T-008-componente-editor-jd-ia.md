# T-008: Componente UI - Editor de Job Description con IA

## 1. Título Claro y Conciso

> Crear el componente React de editor de texto enriquecido con integración IA para generar, editar y regenerar job descriptions.

---

## 2. Descripción Detallada

### Propósito
Proveer una experiencia de edición asistida donde el Recruiter puede generar un JD con IA, editarlo manualmente, y regenerar nuevas versiones hasta obtener el resultado deseado.

### Detalles Específicos

**Funcionalidades:**
1. **Botón "Generar con IA"**
   - Toma datos del formulario de vacante
   - Muestra loading state durante generación
   - Renderiza JD generado en editor

2. **Editor de texto enriquecido**
   - Formato básico: negrita, cursiva, listas, headers
   - Preview del formato final
   - Character count con límite

3. **Controles adicionales**
   - "Regenerar": nueva versión con mismos inputs
   - "Ajustar tono": selector (profesional/casual/formal)
   - "Deshacer": volver a versión anterior

**Estados del componente:**
- `empty`: Sin contenido, muestra CTA de generar
- `loading`: Generación en progreso
- `generated`: JD generado, editable
- `edited`: Usuario modificó el JD generado
- `error`: Error en generación, muestra retry

### Contexto Técnico
- Editor: TipTap o Slate.js
- Estado: React Query para llamadas a AI service
- Debounce en edición para auto-save

---

## 3. Criterios de Aceptación

### Expectativas Claras
- [ ] Botón genera JD llamando a /api/v1/ai/generate-job-description
- [ ] Loading state visible durante generación (skeleton o spinner)
- [ ] Editor permite formato básico de texto
- [ ] Regenerar produce nuevo JD diferente
- [ ] Error handling con mensaje y opción de retry

### Pruebas de Validación
- [ ] Test de flujo completo generar → editar → regenerar
- [ ] Test de loading state
- [ ] Test de error handling
- [ ] Test de accesibilidad del editor

---

## 4. Prioridad

| Nivel | Urgencia | Justificación |
|-------|----------|---------------|
| Media | Normal | Feature diferenciador, depende de T-007 y T-003 |

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
| Módulo | vacantes, ia |
| Sprint | Sprint 1-2 |

---

## 8. Notas y Comentarios

### Consideraciones Técnicas
- Evaluar TipTap vs Slate.js por bundle size y features
- Implementar optimistic updates para mejor UX
- Considerar historial de versiones generadas

### Preguntas Abiertas
- [ ] ¿Cuántas regeneraciones permitir antes de rate limit?
- [ ] ¿Guardar historial de versiones generadas?

### Decisiones de Diseño
- Se usa TipTap por mejor documentación y extensibilidad
- El estado de edición se sincroniza con el form padre

### Riesgos Identificados

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Latencia percibida en generación | Alta | Medio | Skeleton loading, streaming si disponible |
| Bundle size del editor | Media | Bajo | Lazy loading del editor |

---

## 9. Enlaces y Referencias

| Tipo | Enlace/Referencia |
|------|-------------------|
| User Story origen | US-01: Publicación de vacante asistida por IA |
| Documentación técnica | TipTap Docs |
| Tickets relacionados | T-007 (prerequisito), T-003 (backend), T-010 (consume este) |

---

## 10. Historial de Cambios

| Fecha | Autor | Cambio | Versión |
|-------|-------|--------|---------|
| 2026-04-25 | Tech Lead | Creación inicial del ticket | v1.0 |
