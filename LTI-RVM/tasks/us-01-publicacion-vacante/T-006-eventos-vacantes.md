# T-006: Eventos - Publicación de eventos de vacantes

## 1. Título Claro y Conciso

> Implementar la publicación de eventos de dominio para vacantes (creada, actualizada, publicada, cerrada) usando Amazon SNS/EventBridge.

---

## 2. Descripción Detallada

### Propósito
Establecer el sistema de eventos que permita la comunicación desacoplada entre servicios cuando ocurren cambios en vacantes, habilitando reacciones como notificaciones, indexación para búsqueda, y analytics.

### Detalles Específicos

**Eventos a implementar:**

| Evento | Trigger | Consumers |
|--------|---------|-----------|
| `vacancy.created` | POST /vacancies | notification-service, analytics |
| `vacancy.updated` | PUT /vacancies/:id | search-service (reindex) |
| `vacancy.published` | Publicación exitosa | notification-service |
| `vacancy.publication.completed` | Todos los canales procesados | notification-service |
| `vacancy.closed` | Cambio estado a closed | search-service |

**Estructura de evento:**
```json
{
  "event_type": "vacancy.published",
  "event_id": "uuid",
  "timestamp": "2026-04-25T10:00:00Z",
  "source": "vacancy-service",
  "data": {
    "vacancy_id": "uuid",
    "title": "...",
    "channels_published": ["linkedin", "infojobs"],
    "total_reach": 15000
  },
  "metadata": {
    "correlation_id": "uuid",
    "user_id": "uuid"
  }
}
```

### Contexto Técnico
- Bus: Amazon EventBridge para routing
- Fan-out: Amazon SNS para múltiples consumers
- Schema registry para validación de eventos
- Dead letter queue para eventos fallidos

---

## 3. Criterios de Aceptación

### Expectativas Claras
- [ ] Eventos se publican correctamente en EventBridge
- [ ] Estructura de eventos validada contra schema
- [ ] Correlation ID propagado para trazabilidad
- [ ] DLQ configurada para eventos fallidos

### Pruebas de Validación
- [ ] Test de publicación de cada tipo de evento
- [ ] Test de validación de schema
- [ ] Test de consumer recibe evento correctamente
- [ ] Test de DLQ para eventos malformados

---

## 4. Prioridad

| Nivel | Urgencia | Justificación |
|-------|----------|---------------|
| Media | Normal | Necesario para notificaciones y analytics, puede desarrollarse en paralelo |

---

## 5. Estimación de Esfuerzo

| Métrica | Valor |
|---------|-------|
| Story Points | 2 |
| Horas Estimadas | 3-4 horas |
| Complejidad Técnica | Media |
| Riesgo Técnico | Bajo |
| Incertidumbre | Baja |

---

## 6. Asignación

| Rol | Responsabilidad |
|-----|-----------------|
| Responsable | Backend Dev |
| Equipo | Backend Team |
| Revisor Código | Tech Lead |
| Revisor QA | Backend Dev |

---

## 7. Etiquetas / Tags

| Categoría | Valor |
|-----------|-------|
| Tipo | task |
| Capa | backend |
| Componente | vacancy-service, eventos |
| Módulo | vacantes, mensajeria |
| Sprint | Sprint 2 |

---

## 8. Notas y Comentarios

### Consideraciones Técnicas
- Usar transactional outbox pattern para consistencia
- Eventos deben ser idempotentes
- Incluir version del schema en metadata

### Preguntas Abiertas
- [ ] ¿Se requiere ordenamiento garantizado de eventos?

### Decisiones de Diseño
- Se usa EventBridge para routing basado en reglas
- SNS fan-out para múltiples consumers del mismo evento

### Riesgos Identificados

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Pérdida de eventos | Baja | Alto | Outbox pattern, DLQ, monitoreo |

---

## 9. Enlaces y Referencias

| Tipo | Enlace/Referencia |
|------|-------------------|
| User Story origen | US-01: Publicación de vacante asistida por IA |
| Documentación técnica | AWS EventBridge Developer Guide |
| Tickets relacionados | T-002 (prerequisito) |

---

## 10. Historial de Cambios

| Fecha | Autor | Cambio | Versión |
|-------|-------|--------|---------|
| 2026-04-25 | Tech Lead | Creación inicial del ticket | v1.0 |
