<div align="center">

# 🎯 LTI - Applicant Tracking System

**El ATS del futuro impulsado por Inteligencia Artificial**

[![Status](https://img.shields.io/badge/status-en%20diseño-blue.svg)]()
[![License](https://img.shields.io/badge/license-MIT-green.svg)]()
[![AI4Devs](https://img.shields.io/badge/AI4Devs-2026-purple.svg)]()

[Documentación](#-documentación) •
[Arquitectura](#-arquitectura) •
[Contribuir](#-contribuir)

</div>

---

## 📋 Tabla de Contenidos

- [Descripción](#-descripción)
- [Características](#-características)
- [Arquitectura](#-arquitectura)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Documentación](#-documentación)
- [Stack Tecnológico](#-stack-tecnológico)
- [Contribuir](#-contribuir)
- [Licencia](#-licencia)
- [Autores](#-autores)

---

## 🚀 Descripción

**LTI** es un sistema ATS (Applicant Tracking System) de nueva generación diseñado para startups tecnológicas globales que buscan optimizar sus procesos de reclutamiento.

### ¿Por qué LTI?

| Problema | Solución LTI |
|----------|--------------|
| Fragmentación de herramientas | Plataforma unificada para todo el ciclo de reclutamiento |
| Procesos manuales repetitivos | Automatización inteligente con workflows no-code |
| Decisiones sin contexto | IA explicable para matching y recomendaciones |
| Falta de colaboración | Espacio centralizado para recruiters y hiring managers |
| Mala experiencia del candidato | Self-service scheduling y comunicación fluida |

---

## ✨ Características

### Core Features

- **🤖 IA Asistiva y Explicable**
  - Matching candidato-vacante con justificación transparente
  - Generación automática de job descriptions
  - Resúmenes inteligentes para hiring managers
  - Preguntas de entrevista contextualizadas

- **📊 Pipeline Visual**
  - Vista Kanban con drag & drop
  - Etapas configurables por proceso
  - Acciones rápidas sobre candidatos
  - Visualización clara del funnel

- **🔄 Automatización No-Code**
  - Motor visual de workflows (trigger → acción)
  - Secuencias de nurturing automatizadas
  - Gestión inteligente de BBDD

- **🤝 Colaboración en Tiempo Real**
  - Comentarios en hilo por candidato
  - Sistema de decisiones estructuradas
  - Notificaciones integradas

- **📅 Scheduling Inteligente**
  - Self-service para candidatos
  - Integración con Google/Outlook Calendar
  - Paneles de entrevista predefinidos

---

## 🏗 Arquitectura

El sistema sigue una **arquitectura de microservicios** desplegada en AWS:

```
┌─────────────────────────────────────────────────────────────┐
│                    CLIENTES                                  │
│  ┌──────────┐  ┌──────────────┐  ┌────────────────────┐     │
│  │ Web App  │  │ Mobile App   │  │ Portal Candidato   │     │
│  │ (React)  │  │(React Native)│  │    (Next.js)       │     │
│  └──────────┘  └──────────────┘  └────────────────────┘     │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  CloudFront (CDN) + WAF + API Gateway + Cognito (Auth)      │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│              MICROSERVICIOS (ECS Fargate)                   │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐       │
│  │ Vacantes │ │Candidatos│ │Evaluación│ │Scheduling│       │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘       │
│  ┌──────────────────┐  ┌──────────────────────────┐        │
│  │  Notificaciones  │  │  Servicio IA (Bedrock)   │        │
│  └──────────────────┘  └──────────────────────────┘        │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                    CAPA DE DATOS                             │
│  ┌────────────────┐  ┌───────────┐  ┌──────────────────┐   │
│  │ Aurora PostgreSQL│  │ ElastiCache│  │ S3 (Documentos)  │   │
│  └────────────────┘  └───────────┘  └──────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

> 📖 Ver [documentación de arquitectura completa](LTI-RVM/docs/architecture.md)

---

## 📁 Estructura del Proyecto

```
Ai4Devs-design1-2026-03-Senior/
├── 📄 ReadMe.md                    # Este archivo
├── 📁 context/                     # Investigación y contexto
│   ├── ats-research.md             # Análisis de mercado ATS
│   ├── ATSGeneralSpecs.md          # Especificaciones generales
│   └── lean-canvas-ats.drawio      # Lean Canvas editable
│
└── 📁 LTI-RVM/                     # Diseño del sistema (Roger Vila)
    ├── LTI-RVM.md                  # PRD - Product Requirements Document
    ├── prompts.md                  # Prompts utilizados con IA
    ├── UserStories-RVM.md          # Historias de usuario
    ├── lean-canvas.png             # Lean Canvas exportado
    │
    ├── 📁 docs/                    # Documentación técnica
    │   ├── architecture.md         # Arquitectura del sistema
    │   ├── c4-diagrams.md          # Diagramas C4
    │   ├── er-diagram.md           # Modelo de datos
    │   └── use-cases.md            # Casos de uso detallados
    │
    ├── 📁 backlog/                 # Product Backlog
    │   └── product-backlog.json    # Backlog estructurado
    │
    └── 📁 tasks/                   # Tareas técnicas por User Story
        └── us-01-publicacion-vacante/
            ├── T-001-migracion-bd-vacantes.md
            ├── T-002-api-crud-vacantes.md
            └── ...
```

---

## 📚 Documentación

| Documento | Descripción |
|-----------|-------------|
| [PRD - Product Requirements](LTI-RVM/LTI-RVM.md) | Requisitos del producto, funcionalidades y ventajas competitivas |
| [Arquitectura](LTI-RVM/docs/architecture.md) | Diseño técnico del sistema y decisiones de arquitectura |
| [Diagramas C4](LTI-RVM/docs/c4-diagrams.md) | Context, Container y Component diagrams |
| [Modelo de Datos](LTI-RVM/docs/er-diagram.md) | Diagrama ER y descripción de entidades |
| [Casos de Uso](LTI-RVM/docs/use-cases.md) | Casos de uso principales con diagramas |
| [User Stories](LTI-RVM/UserStories-RVM.md) | Historias de usuario priorizadas |
| [Product Backlog](LTI-RVM/backlog/product-backlog.json) | Backlog estructurado en JSON |

---

## 🛠 Stack Tecnológico

### Frontend
| Tecnología | Uso |
|------------|-----|
| React | Aplicación web principal |
| React Native | Aplicación móvil |
| Next.js | Portal del candidato (SSR) |

### Backend
| Tecnología | Uso |
|------------|-----|
| Node.js / Python | Microservicios |
| Amazon ECS Fargate | Orquestación de contenedores |
| Amazon API Gateway | Gestión de APIs |

### Datos
| Tecnología | Uso |
|------------|-----|
| Amazon Aurora PostgreSQL | Base de datos relacional |
| Amazon ElastiCache Redis | Caché y sesiones |
| Amazon S3 | Almacenamiento de documentos |
| Amazon OpenSearch | Búsqueda semántica |

### IA/ML
| Tecnología | Uso |
|------------|-----|
| Amazon Bedrock | LLM para generación de contenido |
| Amazon SageMaker | Modelos de scoring personalizados |

### Infraestructura
| Tecnología | Uso |
|------------|-----|
| AWS CDK | Infrastructure as Code |
| Amazon CloudWatch | Observabilidad |
| AWS X-Ray | Trazas distribuidas |

---

<div align="center">

[⬆ Volver arriba](#-lti---applicant-tracking-system)

</div>



