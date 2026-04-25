# T-011: Integración Frontend-Backend - Flujo completo de publicación

## 1. Título Claro y Conciso

> Conectar la página de creación de vacantes con todas las APIs de backend, implementando el flujo end-to-end desde creación hasta publicación.

---

## 2. Descripción Detallada

### Propósito
Asegurar que todos los componentes frontend se comunican correctamente con los servicios backend, manejando estados de carga, errores, y confirmaciones a lo largo del flujo completo.

### Detalles Específicos

**Integraciones requeridas:**

| Acción Frontend | Endpoint Backend | Handling |
|-----------------|------------------|----------|
| Guardar borrador | POST/PUT /vacancies | Optimistic update |
| Generar JD | POST /ai/generate-job-description | Loading state + retry |
| Cargar canales | GET /channels | Cache 5 min |
| Publicar | POST /vacancies/:id/publish | Confirmación + polling estado |
| Ver estado | GET /vacancies/:id/publications | Polling cada 10s |

**Manejo de estados:**
- Loading states en cada llamada
- Error boundaries con retry
- Toast notifications para feedback
- Redirect tras publicación exitosa

### Contexto Técnico
- HTTP Client: Axios con interceptors
- Cache: React Query con stale-while-revalidate
- Auth: Token JWT en headers (via Cognito)

---

## 3. Criterios de Aceptación

### Expectativas Claras
- [ ] Flujo completo funciona sin errores en happy path
- [ ] Errores de red muestran mensaje y opción de retry
- [ ] Token expirado redirige a login
- [ ] Publicación muestra confirmación con alcance

### Pruebas de Validación
- [ ] Test E2E del flujo completo con backend real/mock
- [ ] Test de error handling (network error, 500, 401)
- [ ] Test de polling de estado de publicación

---

## 4. Prioridad

| Nivel | Urgencia | Justificación |
|-------|----------|---------------|
| Media | Normal | Necesario para demo funcional, depende de todos los tickets previos |

---

## 5. Estimación de Esfuerzo

| Métrica | Valor |
|---------|-------|
| Story Points | 3 |
| Horas Estimadas | 5-6 horas |
| Complejidad Técnica | Media |
| Riesgo Técnico | Medio |
| Incertidumbre | Media |

---

## 6. Asignación

| Rol | Responsabilidad |
|-----|-----------------|
| Responsable | Full Stack Dev |
| Equipo | Full Stack Team |
| Revisor Código | Tech Lead |
| Revisor QA | QA Engineer |

---

## 7. Etiquetas / Tags

| Categoría | Valor |
|-----------|-------|
| Tipo | task |
| Capa | fullstack |
| Componente | web-app, vacancy-service, ai-service, channel-service |
| Módulo | vacantes |
| Sprint | Sprint 2-3 |

---

## 8. Notas y Comentarios

### Consideraciones Técnicas
- Configurar CORS correctamente entre servicios
- Implementar retry con backoff para llamadas críticas
- Usar MSW para mocks durante desarrollo frontend

### Preguntas Abiertas
- [ ] ¿Timeout para publicación antes de mostrar "pendiente"?

### Decisiones de Diseño
- Se usa polling para estado de publicación (no websockets por simplicidad)
- Errores 4xx muestran mensaje específico, 5xx mensaje genérico

### Riesgos Identificados

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Discrepancia en contratos API | Media | Medio | OpenAPI spec compartido, tests de contrato |

---

## 9. Enlaces y Referencias

| Tipo | Enlace/Referencia |
|------|-------------------|
| User Story origen | US-01: Publicación de vacante asistida por IA |
| Especificación API | OpenAPI specs de cada servicio |
| Tickets relacionados | T-002, T-003, T-004, T-010 (prerequisitos) |

---

## 10. Historial de Cambios

| Fecha | Autor | Cambio | Versión |
|-------|-------|--------|---------|
| 2026-04-25 | Tech Lead | Creación inicial del ticket | v1.0 |
