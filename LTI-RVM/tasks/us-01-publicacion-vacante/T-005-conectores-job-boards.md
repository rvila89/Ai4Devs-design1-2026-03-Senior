# T-005: Conectores Job Boards - LinkedIn e InfoJobs

## 1. Título Claro y Conciso

> Implementar los conectores de integración con LinkedIn Jobs API e InfoJobs API para publicar vacantes automáticamente en estas plataformas.

---

## 2. Descripción Detallada

### Propósito
Permitir la publicación automática de vacantes en los principales portales de empleo, eliminando la necesidad de que el Recruiter publique manualmente en cada plataforma.

### Detalles Específicos

**Conectores a implementar:**

1. **LinkedIn Jobs Posting API**
   - Autenticación OAuth 2.0
   - Endpoint: POST /v2/jobPostings
   - Mapeo de campos LTI → LinkedIn format
   - Manejo de límites de la API

2. **InfoJobs API**
   - Autenticación API Key
   - Endpoint: POST /api/v1/offers
   - Mapeo de campos LTI → InfoJobs format
   - Gestión de categorías y subcategorías

**Patrón de implementación:**
- Interface `JobBoardConnector` con métodos: publish, unpublish, getStatus
- Implementaciones específicas por canal
- Factory pattern para instanciar conectores

**Worker de publicación:**
- Consume de SQS queue
- Procesa publicaciones pendientes
- Actualiza estado en BD
- Emite evento de resultado

### Contexto Técnico
- Servicio: channel-service (workers)
- Colas: SQS para jobs de publicación
- Secrets: AWS Secrets Manager para API keys
- Circuit breaker: Para manejar fallos de APIs externas

---

## 3. Criterios de Aceptación

### Expectativas Claras
- [ ] Conector LinkedIn publica correctamente en sandbox/producción
- [ ] Conector InfoJobs publica correctamente
- [ ] Errores de API se manejan y registran apropiadamente
- [ ] Estado de publicación se actualiza via callback/polling
- [ ] Logs detallados para debugging

### Pruebas de Validación
- [ ] Test con mock de cada API externa
- [ ] Test de manejo de errores (rate limit, auth error, validation error)
- [ ] Test de circuit breaker
- [ ] Test end-to-end con sandbox de LinkedIn (si disponible)

---

## 4. Prioridad

| Nivel | Urgencia | Justificación |
|-------|----------|---------------|
| Media | Normal | Necesario para demo pero puede usar mocks inicialmente |

---

## 5. Estimación de Esfuerzo

| Métrica | Valor |
|---------|-------|
| Story Points | 8 |
| Horas Estimadas | 10-12 horas |
| Complejidad Técnica | Alta |
| Riesgo Técnico | Alto |
| Incertidumbre | Media |

---

## 6. Asignación

| Rol | Responsabilidad |
|-----|-----------------|
| Responsable | Backend Dev Senior |
| Equipo | Backend Team |
| Revisor Código | Tech Lead |
| Revisor QA | QA Engineer |

---

## 7. Etiquetas / Tags

| Categoría | Valor |
|-----------|-------|
| Tipo | feature |
| Capa | backend |
| Componente | channel-service |
| Módulo | vacantes, integraciones |
| Sprint | Sprint 2-3 |

---

## 8. Notas y Comentarios

### Consideraciones Técnicas
- Implementar retry con backoff exponencial
- Usar circuit breaker (ej: opossum) para evitar cascading failures
- Mapeo de campos debe ser configurable (no hardcoded)
- Considerar feature flags por conector

### Preguntas Abiertas
- [ ] ¿Tenemos acceso a sandbox de LinkedIn Jobs API?
- [ ] ¿Cuáles son los límites de rate de cada API?

### Decisiones de Diseño
- Se usa patrón Adapter para cada conector
- Los conectores son stateless, configuración via env vars
- Se priorizan logs estructurados para troubleshooting

### Riesgos Identificados

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| LinkedIn API requiere aprobación | Alta | Alto | Iniciar proceso de aprobación temprano |
| Rate limiting de APIs | Media | Medio | Cola con throttling |
| Cambios en APIs externas | Baja | Alto | Versionar adaptadores, tests de contrato |

---

## 9. Enlaces y Referencias

| Tipo | Enlace/Referencia |
|------|-------------------|
| User Story origen | US-01: Publicación de vacante asistida por IA |
| Documentación técnica | LinkedIn Jobs Posting API Docs, InfoJobs API Docs |
| Tickets relacionados | T-004 (prerequisito), T-006 (eventos) |

---

## 10. Historial de Cambios

| Fecha | Autor | Cambio | Versión |
|-------|-------|--------|---------|
| 2026-04-25 | Tech Lead | Creación inicial del ticket | v1.0 |
