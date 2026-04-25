# Tickets de Trabajo Técnicos

Esta carpeta contiene los tickets técnicos generados a partir de las User Stories del proyecto LTI.

## Estructura

```
tasks/
├── README.md                           # Este archivo
├── us-01-publicacion-vacante/         # Tickets de la US-01
│   ├── README.md                       # Resumen y dependencias
│   ├── T-001-migracion-tabla-vacantes.md
│   ├── T-002-api-crear-vacante.md
│   └── ...
├── us-02-matching-candidatos/         # Tickets de la US-02
│   └── ...
└── ...
```

## Cómo Generar Tickets

### Usando el Prompt de VS Code

1. Abre el archivo `prompts/generate-technical-tickets.prompt.md`
2. Ejecuta el prompt con Copilot Chat (Ctrl+Shift+I o Cmd+Shift+I)
3. Proporciona la User Story como argumento:

```
Genera tickets para:

## US-01: Publicación de vacante asistida por IA

**Como** Recruiter,
**quiero** crear y publicar vacantes optimizadas...
```

### Formato de Tickets

Cada ticket incluye:
- **Descripción técnica** clara y accionable
- **Criterios de aceptación** verificables
- **Implementación sugerida** (archivos, pseudocódigo, APIs)
- **Estimación** en horas y complejidad
- **Dependencias** con otros tickets
- **Testing** requerido

## Convenciones

- **Nomenclatura:** `T-XXX-descripcion-kebab-case.md`
- **Estimaciones:** 1-3 días máximo por ticket
- **Estados:** ⬜ Pendiente | 🔄 En Progreso | ✅ Completado | ⏸️ Bloqueado
