# T-009: Componente UI - Selector de canales de publicación

## 1. Título Claro y Conciso

> Crear el componente React para seleccionar los canales donde publicar la vacante, mostrando estado de integración y alcance estimado.

---

## 2. Descripción Detallada

### Propósito
Permitir al Recruiter visualizar y seleccionar los canales de publicación disponibles, con información clara sobre cuáles están integrados y el alcance potencial de cada uno.

### Detalles Específicos

**Funcionalidades:**
1. **Lista de canales**
   - Checkbox para cada canal
   - Icono/logo del canal
   - Badge de estado (integrado/no integrado)
   - Alcance estimado por canal

2. **Información visual**
   - Canales integrados: seleccionables
   - Canales no integrados: deshabilitados con tooltip explicativo
   - Total de alcance estimado (suma de seleccionados)

3. **Comportamiento**
   - "Seleccionar todos (integrados)"
   - Persistencia de preferencias del usuario

**Datos a mostrar por canal:**
```typescript
interface Channel {
  id: string;
  name: string;
  logo_url: string;
  is_integrated: boolean;
  estimated_reach: number;
  integration_status: 'active' | 'pending' | 'unavailable';
}
```

### Contexto Técnico
- Datos vienen de GET /api/v1/channels
- Estado local con React state o form context
- Diseño responsivo (cards en mobile, tabla en desktop)

---

## 3. Criterios de Aceptación

### Expectativas Claras
- [ ] Lista de canales renderiza correctamente desde API
- [ ] Canales no integrados muestran aviso y están deshabilitados
- [ ] Selección múltiple funciona correctamente
- [ ] Total de alcance se actualiza dinámicamente
- [ ] Loading y error states implementados

### Pruebas de Validación
- [ ] Test de renderizado con mock de canales
- [ ] Test de selección/deselección
- [ ] Test de canal no integrado (no seleccionable)
- [ ] Test de accesibilidad

---

## 4. Prioridad

| Nivel | Urgencia | Justificación |
|-------|----------|---------------|
| Media | Normal | Componente necesario para flujo completo, puede desarrollarse en paralelo |

---

## 5. Estimación de Esfuerzo

| Métrica | Valor |
|---------|-------|
| Story Points | 2 |
| Horas Estimadas | 3-4 horas |
| Complejidad Técnica | Baja |
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
| Módulo | vacantes, canales |
| Sprint | Sprint 1 |

---

## 8. Notas y Comentarios

### Consideraciones Técnicas
- Cachear lista de canales (cambia poco)
- Logos de canales en CDN con fallback

### Preguntas Abiertas
- [ ] ¿Guardar preferencias de canales por usuario o por vacante?

### Decisiones de Diseño
- Se muestran todos los canales (integrados y no) para transparencia
- El alcance estimado es informativo, no garantizado

### Riesgos Identificados

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Ninguno significativo | - | - | - |

---

## 9. Enlaces y Referencias

| Tipo | Enlace/Referencia |
|------|-------------------|
| User Story origen | US-01: Publicación de vacante asistida por IA |
| Diseño/Mockup | Por definir (Figma) |
| Tickets relacionados | T-004 (backend), T-010 (consume este) |

---

## 10. Historial de Cambios

| Fecha | Autor | Cambio | Versión |
|-------|-------|--------|---------|
| 2026-04-25 | Tech Lead | Creación inicial del ticket | v1.0 |
