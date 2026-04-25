# T-002: API REST - CRUD de vacantes

## 1. Título Claro y Conciso

> Implementar los endpoints REST para crear, leer, actualizar y eliminar vacantes en el vacancy-service, incluyendo validaciones y manejo de estados.

---

## 2. Descripción Detallada

### Propósito
Proveer la API backend que permita a los Recruiters gestionar el ciclo de vida completo de las vacantes, desde su creación en borrador hasta su cierre o archivo.

### Detalles Específicos

**Endpoints requeridos:**

| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | /api/v1/vacancies | Crear nueva vacante |
| GET | /api/v1/vacancies | Listar vacantes con filtros y paginación |
| GET | /api/v1/vacancies/:id | Obtener detalle de vacante |
| PUT | /api/v1/vacancies/:id | Actualizar vacante |
| PATCH | /api/v1/vacancies/:id/status | Cambiar estado de vacante |
| DELETE | /api/v1/vacancies/:id | Soft-delete de vacante |

**Estados de vacante:**
- `draft` → `published` → `closed` → `archived`
- Transiciones válidas deben ser validadas

**Filtros para listado:**
- status, department, location, created_by, date_range

### Contexto Técnico
- Framework: Express.js con TypeScript
- Validación: Zod schemas
- Autenticación: JWT via Amazon Cognito
- Autorización: Middleware de roles (solo Recruiters y Admins)

---

## 3. Criterios de Aceptación

### Expectativas Claras
- [ ] Todos los endpoints implementados y documentados en OpenAPI
- [ ] Validación de entrada con mensajes de error descriptivos
- [ ] Paginación implementada (limit, offset, total_count)
- [ ] Filtros funcionando correctamente
- [ ] Manejo de errores consistente (formato estándar)

### Pruebas de Validación
- [ ] Tests unitarios para cada endpoint (>80% coverage)
- [ ] Tests de integración con base de datos de prueba
- [ ] Validación de autorización (usuario sin permisos recibe 403)
- [ ] Respuestas cumplen contrato OpenAPI

---

## 4. Prioridad

| Nivel | Urgencia | Justificación |
|-------|----------|---------------|
| Alta | Crítica | API core del módulo, bloquea desarrollo frontend y flujo completo |

---

## 5. Estimación de Esfuerzo

| Métrica | Valor |
|---------|-------|
| Story Points | 5 |
| Horas Estimadas | 6-8 horas |
| Complejidad Técnica | Media |
| Riesgo Técnico | Bajo |
| Incertidumbre | Baja |

---

## 6. Asignación

| Rol | Responsabilidad |
|-----|-----------------|
| Responsable | Backend Dev |
| Equipo | Backend Team |
| Revisor Código | Backend Dev Senior |
| Revisor QA | QA Engineer |

---

## 7. Etiquetas / Tags

| Categoría | Valor |
|-----------|-------|
| Tipo | feature |
| Capa | backend |
| Componente | vacancy-service |
| Módulo | vacantes |
| Sprint | Sprint 1-2 |

---

## 8. Notas y Comentarios

### Consideraciones Técnicas
- Usar transacciones para operaciones que afecten múltiples tablas
- Implementar rate limiting por usuario
- Logs estructurados para auditoría de acciones

### Preguntas Abiertas
- [ ] ¿El listado debe incluir vacantes archivadas por defecto o excluirlas?

### Decisiones de Diseño
- Se usa PUT para actualización completa, PATCH solo para cambio de estado
- La eliminación es soft-delete, no se expone endpoint de delete permanente

### Riesgos Identificados

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Cambios en validaciones durante desarrollo | Media | Bajo | Schemas Zod centralizados y versionados |

---

## 9. Enlaces y Referencias

| Tipo | Enlace/Referencia |
|------|-------------------|
| User Story origen | US-01: Publicación de vacante asistida por IA |
| Documentación técnica | LTI-RVM/docs/architecture.md |
| Especificación API | Por definir (OpenAPI 3.0) |
| Tickets relacionados | T-001 (prerequisito), T-006 (eventos), T-011 (integración) |

---

## 10. Historial de Cambios

| Fecha | Autor | Cambio | Versión |
|-------|-------|--------|---------|
| 2026-04-25 | Tech Lead | Creación inicial del ticket | v1.0 |
