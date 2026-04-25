# T-004: API REST - Endpoints de canales de publicación

## 1. Título Claro y Conciso

> Implementar endpoints para gestionar canales de publicación y el registro de publicaciones de vacantes por canal.

---

## 2. Descripción Detallada

### Propósito
Proveer la API que permita listar canales disponibles, consultar estado de integración, y registrar/consultar las publicaciones de vacantes en cada canal.

### Detalles Específicos

**Endpoints requeridos:**

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | /api/v1/channels | Listar canales disponibles |
| GET | /api/v1/channels/:id | Detalle de canal |
| POST | /api/v1/vacancies/:id/publish | Publicar vacante en canales seleccionados |
| GET | /api/v1/vacancies/:id/publications | Estado de publicaciones por canal |
| DELETE | /api/v1/vacancies/:id/publications/:channelId | Despublicar de un canal |

**Estados de publicación:**
- `pending` → `published` → `expired` | `failed`

**Respuesta de publicación:**
```json
{
  "vacancy_id": "uuid",
  "publications": [
    {
      "channel_id": "linkedin",
      "status": "published",
      "external_url": "https://linkedin.com/jobs/123",
      "estimated_reach": 5000,
      "published_at": "2026-04-25T10:00:00Z"
    }
  ],
  "total_estimated_reach": 15000
}
```

### Contexto Técnico
- Servicio: channel-service (microservicio)
- La publicación real en canales externos es asíncrona
- Se usa SQS para encolar las publicaciones
- Webhook de callback para actualizar estado

---

## 3. Criterios de Aceptación

### Expectativas Claras
- [ ] Listado de canales incluye estado de integración (activo/inactivo)
- [ ] Publicación encola correctamente en SQS
- [ ] Estado de publicaciones refleja estado real por canal
- [ ] Canales no integrados retornan aviso apropiado

### Pruebas de Validación
- [ ] Test de listado de canales con filtros
- [ ] Test de publicación en múltiples canales
- [ ] Test de manejo de canal no integrado
- [ ] Test de despublicación

---

## 4. Prioridad

| Nivel | Urgencia | Justificación |
|-------|----------|---------------|
| Alta | Crítica | Necesario para el flujo de publicación multicanal |

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
| Componente | channel-service |
| Módulo | vacantes, canales |
| Sprint | Sprint 1-2 |

---

## 8. Notas y Comentarios

### Consideraciones Técnicas
- El endpoint de publish solo encola, no espera respuesta del canal
- Usar patrón de eventos para actualizar estado cuando canal confirma
- Considerar idempotencia para evitar publicaciones duplicadas

### Preguntas Abiertas
- [ ] ¿Cuántos reintentos para publicaciones fallidas?

### Decisiones de Diseño
- La publicación es asíncrona para no bloquear al usuario
- Se almacena URL externa cuando el canal la proporciona

### Riesgos Identificados

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Canal externo no disponible | Media | Medio | Cola de reintentos, notificación al usuario |

---

## 9. Enlaces y Referencias

| Tipo | Enlace/Referencia |
|------|-------------------|
| User Story origen | US-01: Publicación de vacante asistida por IA |
| Documentación técnica | LTI-RVM/docs/architecture.md |
| Tickets relacionados | T-001 (prerequisito), T-005 (conectores), T-006 (eventos) |

---

## 10. Historial de Cambios

| Fecha | Autor | Cambio | Versión |
|-------|-------|--------|---------|
| 2026-04-25 | Tech Lead | Creación inicial del ticket | v1.0 |
