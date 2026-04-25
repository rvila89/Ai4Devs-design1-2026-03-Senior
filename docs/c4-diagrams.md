# Diagramas C4 – Sistema ATS LTI

---

## Resumen de niveles C4 representados

Se han generado tres niveles del modelo C4 para el sistema ATS LTI. El **Nivel 1 (Context)** sitúa el sistema en su entorno, mostrando los tres tipos de usuarios que interactúan con él (Recruiter, Hiring Manager y Candidato) y los sistemas externos con los que se integra (calendarios, bolsas de empleo, HRIS y proveedores de comunicación). Este nivel permite a cualquier stakeholder entender el alcance y las fronteras del sistema sin entrar en detalles técnicos.

El **Nivel 2 (Container)** desglosa el interior del sistema ATS LTI en sus contenedores principales: las aplicaciones cliente (Web App, Mobile App, Portal del Candidato), la capa de API (API Gateway + ALB), los seis microservicios funcionales desplegados en ECS Fargate, las bases de datos (Aurora PostgreSQL, ElastiCache Redis, S3, OpenSearch) y la capa de mensajería asíncrona (SQS/SNS/EventBridge). Este diagrama es la referencia principal para el equipo de desarrollo y operaciones.

El **Nivel 3 (Component)** profundiza en el **Servicio de Evaluación**, el contenedor de mayor complejidad al integrar los tres flujos de UC-02 (scoring IA, scorecards estructurados y decisiones trazadas). Se muestran sus componentes internos: los controladores REST, los gestores de dominio, los repositorios de datos y los adaptadores hacia el Servicio de IA y el bus de eventos. Las decisiones de diseño más relevantes son la separación entre lógica de aplicación y acceso a datos mediante el patrón Repository, y el uso de eventos de dominio para notificar cambios de etapa al resto del sistema.

---

## Nivel 1 – System Context

```plantuml
@startuml "C4_Context_ATS_LTI"
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Context.puml

LAYOUT_TOP_DOWN()
LAYOUT_WITH_LEGEND()

title System Context – ATS LTI

Person(recruiter, "Recruiter", "Gestiona vacantes, candidatos y el pipeline de selección")
Person(hiring_manager, "Hiring Manager", "Evalúa candidatos y toma decisiones de contratación")
Person_Ext(candidato, "Candidato", "Postula a vacantes y agenda entrevistas de forma autónoma")

System(ats_lti, "ATS LTI", "Plataforma centralizada de gestión del proceso de reclutamiento con automatización e IA")

System_Ext(google_cal, "Google Calendar", "Gestión de disponibilidad y creación de eventos de entrevista")
System_Ext(outlook_cal, "Microsoft Outlook Calendar", "Gestión de disponibilidad y creación de eventos de entrevista")
System_Ext(job_boards, "Job Boards\n(LinkedIn, InfoJobs)", "Publicación multicanal de vacantes")
System_Ext(hris, "HRIS\n(BambooHR, Workday)", "Sincronización de datos de empleados y posiciones")
System_Ext(email_sms, "Proveedor Email/SMS\n(Amazon SES/SNS)", "Envío de notificaciones y recordatorios")

Rel(recruiter, ats_lti, "Crea vacantes, gestiona pipeline y evalúa candidatos", "HTTPS")
Rel(hiring_manager, ats_lti, "Completa scorecards y registra decisiones", "HTTPS")
Rel(candidato, ats_lti, "Postula a vacantes y selecciona slot de entrevista", "HTTPS")

Rel(ats_lti, google_cal, "Consulta disponibilidad y crea eventos", "HTTPS / Google Calendar API")
Rel(ats_lti, outlook_cal, "Consulta disponibilidad y crea eventos", "HTTPS / Microsoft Graph API")
Rel(ats_lti, job_boards, "Publica vacantes en múltiples canales", "HTTPS / REST API")
Rel(ats_lti, hris, "Sincroniza posiciones y datos de empleados", "HTTPS / REST API")
Rel(ats_lti, email_sms, "Envía notificaciones, recordatorios y comunicaciones", "HTTPS / SMTP")

@enduml
```

---

## Nivel 2 – Container

```plantuml
@startuml "C4_Container_ATS_LTI"
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

LAYOUT_TOP_DOWN()
LAYOUT_WITH_LEGEND()

title Container Diagram – ATS LTI

Person(recruiter, "Recruiter", "Gestiona vacantes y pipeline")
Person(hiring_manager, "Hiring Manager", "Evalúa y decide sobre candidatos")
Person_Ext(candidato, "Candidato", "Postula y agenda entrevistas")

System_Ext(google_cal, "Google Calendar API")
System_Ext(outlook_cal, "Microsoft Graph API")
System_Ext(job_boards, "Job Boards")
System_Ext(hris, "HRIS")
System_Ext(email_sms, "Amazon SES / SNS")

System_Boundary(ats_lti, "ATS LTI – AWS Cloud") {

    Container(web_app, "Web App", "React, TypeScript", "Interfaz principal para Recruiters y Hiring Managers")
    Container(mobile_app, "Mobile App", "React Native", "Acceso móvil para Recruiters y Hiring Managers")
    Container(candidate_portal, "Portal del Candidato", "Next.js, TypeScript", "Portal self-service para candidatos: postulación y scheduling")

    Container(cdn_waf, "CloudFront + WAF", "Amazon CloudFront, AWS WAF", "CDN global y firewall de aplicación web")
    Container(cognito, "Auth Service", "Amazon Cognito", "Autenticación y autorización con tokens JWT")
    Container(api_gw, "API Gateway", "Amazon API Gateway", "Enrutamiento REST y WebSocket hacia microservicios")
    Container(alb, "Load Balancer", "AWS Application Load Balancer", "Distribución de tráfico hacia microservicios con health checks")

    Container(svc_vacantes, "Servicio Vacantes", "Node.js, Express, ECS Fargate", "UC-01: Gestión de vacantes, JD con IA y publicación multicanal")
    Container(svc_candidatos, "Servicio Candidatos", "Node.js, Express, ECS Fargate", "Gestión de la base de talento y sourcing")
    Container(svc_evaluacion, "Servicio Evaluación", "Node.js, Express, ECS Fargate", "UC-02: Matching IA, scorecards y decisiones estructuradas")
    Container(svc_scheduling, "Servicio Scheduling", "Node.js, Express, ECS Fargate", "UC-03: Gestión de paneles, slots y entrevistas self-service")
    Container(svc_notificaciones, "Servicio Notificaciones", "Node.js, ECS Fargate", "Envío de recordatorios y comunicaciones automatizadas")
    Container(svc_ia, "Servicio IA", "Python, FastAPI, ECS Fargate", "Generación de JD, matching candidato-vacante y resúmenes")

    Container(message_bus, "Bus de Mensajería", "Amazon SQS, SNS, EventBridge", "Comunicación asíncrona entre microservicios")

    ContainerDb(aurora_db, "Base de Datos Relacional", "Amazon Aurora PostgreSQL Multi-AZ", "Datos transaccionales: vacantes, candidatos, aplicaciones, entrevistas")
    ContainerDb(redis_cache, "Caché / Sesión", "Amazon ElastiCache Redis", "Caché de rankings, sesiones de usuario y slots disponibles")
    ContainerDb(s3_storage, "Almacenamiento de Objetos", "Amazon S3", "CVs, documentos adjuntos y assets estáticos")
    ContainerDb(opensearch, "Motor de Búsqueda", "Amazon OpenSearch", "Búsqueda semántica de candidatos por skills y experiencia")
    Container(bedrock, "LLM Service", "Amazon Bedrock", "Generación de job descriptions, resúmenes y preguntas de entrevista")
    Container(sagemaker, "Scoring Model", "Amazon SageMaker", "Modelo propio de scoring y matching candidato-vacante")
}

Rel(recruiter, cdn_waf, "Usa", "HTTPS")
Rel(hiring_manager, cdn_waf, "Usa", "HTTPS")
Rel(candidato, cdn_waf, "Usa", "HTTPS")

Rel(cdn_waf, web_app, "Sirve", "HTTPS")
Rel(cdn_waf, mobile_app, "Sirve", "HTTPS")
Rel(cdn_waf, candidate_portal, "Sirve", "HTTPS")
Rel(cdn_waf, api_gw, "Enruta peticiones API", "HTTPS")

Rel(web_app, api_gw, "Llama a", "HTTPS / REST, WebSocket")
Rel(mobile_app, api_gw, "Llama a", "HTTPS / REST")
Rel(candidate_portal, api_gw, "Llama a", "HTTPS / REST")

Rel(api_gw, cognito, "Valida tokens JWT", "HTTPS")
Rel(api_gw, alb, "Enruta hacia microservicios", "HTTP")

Rel(alb, svc_vacantes, "Enruta", "HTTP")
Rel(alb, svc_candidatos, "Enruta", "HTTP")
Rel(alb, svc_evaluacion, "Enruta", "HTTP")
Rel(alb, svc_scheduling, "Enruta", "HTTP")

Rel(svc_vacantes, aurora_db, "Lee y escribe", "SQL / port 5432")
Rel(svc_vacantes, s3_storage, "Almacena documentos", "AWS SDK")
Rel(svc_vacantes, svc_ia, "Solicita generación de JD", "HTTP / REST")
Rel(svc_vacantes, message_bus, "Publica eventos de vacante", "AWS SDK")
Rel(svc_vacantes, job_boards, "Publica vacantes", "HTTPS / REST API")

Rel(svc_candidatos, aurora_db, "Lee y escribe", "SQL / port 5432")
Rel(svc_candidatos, opensearch, "Indexa y busca candidatos", "HTTPS / REST")
Rel(svc_candidatos, s3_storage, "Almacena CVs", "AWS SDK")
Rel(svc_candidatos, hris, "Sincroniza datos", "HTTPS / REST API")

Rel(svc_evaluacion, aurora_db, "Lee y escribe", "SQL / port 5432")
Rel(svc_evaluacion, redis_cache, "Cachea rankings", "Redis protocol")
Rel(svc_evaluacion, svc_ia, "Solicita scoring y matching", "HTTP / REST")
Rel(svc_evaluacion, message_bus, "Publica decisiones y cambios de etapa", "AWS SDK")

Rel(svc_scheduling, aurora_db, "Lee y escribe", "SQL / port 5432")
Rel(svc_scheduling, redis_cache, "Cachea slots disponibles", "Redis protocol")
Rel(svc_scheduling, google_cal, "Consulta disponibilidad y crea eventos", "HTTPS / Google API")
Rel(svc_scheduling, outlook_cal, "Consulta disponibilidad y crea eventos", "HTTPS / Graph API")
Rel(svc_scheduling, message_bus, "Publica eventos de entrevista", "AWS SDK")

Rel(svc_notificaciones, aurora_db, "Lee estado de recordatorios", "SQL / port 5432")
Rel(svc_notificaciones, email_sms, "Envía emails y SMS", "HTTPS / SMTP")
Rel(message_bus, svc_notificaciones, "Entrega eventos de notificación", "AWS SDK")

Rel(svc_ia, bedrock, "Genera contenido con LLM", "HTTPS / AWS SDK")
Rel(svc_ia, sagemaker, "Invoca modelo de scoring", "HTTPS / AWS SDK")

@enduml
```

---

## Nivel 3 – Component (Servicio de Evaluación)

```plantuml
@startuml "C4_Component_EvaluacionService"
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Component.puml

LAYOUT_TOP_DOWN()
LAYOUT_WITH_LEGEND()

title Component Diagram – Servicio de Evaluación (UC-02)

Container_Ext(alb, "Application Load Balancer", "AWS ALB", "Enruta peticiones HTTP al servicio")
Container_Ext(svc_ia, "Servicio IA", "Python, FastAPI", "Proporciona scoring y matching explicable")
ContainerDb_Ext(aurora_db, "Aurora PostgreSQL", "Base de datos relacional", "Almacena aplicaciones, scorecards y decisiones")
ContainerDb_Ext(redis_cache, "ElastiCache Redis", "Caché", "Rankings en memoria y caché de scorecards")
Container_Ext(message_bus, "Bus de Mensajería", "SQS / SNS / EventBridge", "Recibe y publica eventos de dominio")

Container_Boundary(svc_evaluacion, "Servicio de Evaluación – Node.js / ECS Fargate") {

    Component(pipeline_controller, "Pipeline Controller", "Express REST Controller", "Expone endpoints para gestionar la etapa de los candidatos en el pipeline")
    Component(scorecard_controller, "Scorecard Controller", "Express REST Controller", "Expone endpoints para crear y completar scorecards por vacante")
    Component(matching_controller, "Matching Controller", "Express REST Controller", "Expone endpoints para obtener el ranking IA y su explicación")
    Component(decision_controller, "Decision Controller", "Express REST Controller", "Expone endpoints para registrar decisiones estructuradas")

    Component(pipeline_service, "Pipeline Service", "Domain Service", "Lógica de negocio para cambios de etapa, validaciones y reglas del funnel")
    Component(scorecard_service, "Scorecard Service", "Domain Service", "Lógica de asignación de scorecards y cálculo de puntuación total")
    Component(matching_service, "Matching Service", "Domain Service", "Orquesta la llamada al Servicio IA y persiste el resultado explicable")
    Component(decision_service, "Decision Service", "Domain Service", "Valida y persiste decisiones, publica evento de dominio")

    Component(aplicacion_repo, "Aplicacion Repository", "Repository Pattern", "Acceso a datos de APLICACION en Aurora")
    Component(scorecard_repo, "Scorecard Repository", "Repository Pattern", "Acceso a datos de SCORECARD y EVALUACION_CANDIDATO en Aurora")
    Component(matching_repo, "Matching Repository", "Repository Pattern", "Acceso a datos de MATCHING_IA en Aurora y caché Redis")
    Component(decision_repo, "Decision Repository", "Repository Pattern", "Acceso a datos de DECISION en Aurora")

    Component(ia_adapter, "IA Adapter", "HTTP Client", "Adaptador para llamar al Servicio IA (scoring y matching)")
    Component(event_publisher, "Event Publisher", "AWS SDK SQS/SNS", "Publica eventos de dominio al bus de mensajería")
}

Rel(alb, pipeline_controller, "Enruta peticiones REST", "HTTP")
Rel(alb, scorecard_controller, "Enruta peticiones REST", "HTTP")
Rel(alb, matching_controller, "Enruta peticiones REST", "HTTP")
Rel(alb, decision_controller, "Enruta peticiones REST", "HTTP")

Rel(pipeline_controller, pipeline_service, "Delega lógica de negocio")
Rel(scorecard_controller, scorecard_service, "Delega lógica de negocio")
Rel(matching_controller, matching_service, "Delega lógica de negocio")
Rel(decision_controller, decision_service, "Delega lógica de negocio")

Rel(pipeline_service, aplicacion_repo, "Lee y actualiza etapa de aplicación")
Rel(pipeline_service, event_publisher, "Publica CandidatoAvanzado / CandidatoDescartado")

Rel(scorecard_service, scorecard_repo, "Lee scorecard y persiste evaluación")
Rel(scorecard_service, aplicacion_repo, "Verifica estado de la aplicación")

Rel(matching_service, ia_adapter, "Solicita score y explicación")
Rel(matching_service, matching_repo, "Persiste y recupera resultado de matching")

Rel(decision_service, decision_repo, "Persiste decisión estructurada")
Rel(decision_service, aplicacion_repo, "Actualiza etapa final")
Rel(decision_service, event_publisher, "Publica DecisionRegistrada")

Rel(aplicacion_repo, aurora_db, "SQL: APLICACION", "SQL / port 5432")
Rel(scorecard_repo, aurora_db, "SQL: SCORECARD, EVALUACION_CANDIDATO", "SQL / port 5432")
Rel(matching_repo, aurora_db, "SQL: MATCHING_IA", "SQL / port 5432")
Rel(matching_repo, redis_cache, "Caché de rankings por vacante", "Redis protocol")
Rel(decision_repo, aurora_db, "SQL: DECISION", "SQL / port 5432")

Rel(ia_adapter, svc_ia, "POST /score, POST /match", "HTTP / REST")
Rel(event_publisher, message_bus, "Publica eventos de dominio", "AWS SDK")

@enduml
```

---

*Documento generado el 21 de abril de 2026 para el sistema ATS LTI.*
