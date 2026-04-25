# T-001: Migración BD - Tablas vacantes y canales

## 1. Título Claro y Conciso

> Crear las tablas de base de datos necesarias para almacenar vacantes, canales de publicación y el registro de publicaciones en Amazon Aurora PostgreSQL.

---

## 2. Descripción Detallada

### Propósito
Establecer el modelo de datos relacional que soportará toda la funcionalidad de gestión de vacantes y publicación multicanal. Esta migración es prerequisito para todos los endpoints de backend.

### Detalles Específicos
Se requieren las siguientes tablas:
- `vacancies`: Datos maestros de vacantes
- `publication_channels`: Catálogo de canales de publicación disponibles
- `vacancy_publications`: Registro de publicaciones por vacante/canal
- `job_descriptions`: Historial de JDs generados (versiones)

Campos clave para `vacancies`:
- id, title, department, location, salary_range_min/max
- status (draft, published, closed, archived)
- created_by, created_at, updated_at
- ai_generated_jd, manual_jd_override

### Contexto Técnico
- Base de datos: Amazon Aurora PostgreSQL
- ORM: Prisma con migraciones versionadas
- El esquema debe soportar soft-delete y auditoría
- Índices necesarios para búsquedas frecuentes (status, department, created_at)

---

## 3. Criterios de Aceptación

### Expectativas Claras
- [ ] Migración ejecutable sin errores en entorno de desarrollo
- [ ] Todas las tablas creadas con constraints de integridad referencial
- [ ] Índices creados para campos de búsqueda frecuente
- [ ] Seed data con canales de publicación predefinidos (LinkedIn, InfoJobs, Web Corporativa)

### Pruebas de Validación
- [ ] Migración up/down ejecuta correctamente
- [ ] Foreign keys funcionan según lo esperado
- [ ] Consultas de prueba retornan datos del seed
- [ ] No hay warnings de Prisma al generar cliente

---

## 4. Prioridad

| Nivel | Urgencia | Justificación |
|-------|----------|---------------|
| Alta | Crítica | Es bloqueante para T-002 y T-004. Sin la BD no hay desarrollo de APIs posible. |

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
| Responsable | Backend Dev |
| Equipo | Backend Team |
| Revisor Código | Tech Lead |
| Revisor QA | Backend Dev Senior |

---

## 7. Etiquetas / Tags

| Categoría | Valor |
|-----------|-------|
| Tipo | task |
| Capa | backend |
| Componente | vacancy-service |
| Módulo | vacantes |
| Sprint | Sprint 1 |

---

## 8. Notas y Comentarios

### Consideraciones Técnicas
- Usar UUID v4 para IDs en lugar de auto-increment por seguridad
- Implementar campos de auditoría (created_at, updated_at, deleted_at)
- El campo `salary_range` debe soportar diferentes monedas (considerar campo currency)

### Preguntas Abiertas
- [ ] ¿Se requiere soporte multi-idioma para títulos de vacantes desde el inicio?

### Decisiones de Diseño
- Se usa soft-delete (deleted_at) en lugar de delete físico para mantener histórico
- Los JDs se versionan en tabla separada para auditoría

### Riesgos Identificados

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Cambios de esquema tardíos | Baja | Medio | Revisión de diseño antes de implementar |

---

## 9. Enlaces y Referencias

| Tipo | Enlace/Referencia |
|------|-------------------|
| User Story origen | US-01: Publicación de vacante asistida por IA |
| Documentación técnica | LTI-RVM/docs/er-diagram.md |
| Especificación API | N/A |
| Tickets relacionados | T-002 (depende de este), T-004 (depende de este) |

---

## 10. Historial de Cambios

| Fecha | Autor | Cambio | Versión |
|-------|-------|--------|---------|
| 2026-04-25 | Tech Lead | Creación inicial del ticket | v1.0 |
