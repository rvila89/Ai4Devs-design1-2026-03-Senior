# diagrams (mingrammer) — Detailed Reference

**Official docs:** https://diagrams.mingrammer.com  
**GitHub:** https://github.com/mingrammer/diagrams  
**Node browser:** https://diagrams.mingrammer.com/docs/nodes/aws

---

## Table of Contents
1. [Installation](#1-installation)
2. [Core Concepts](#2-core-concepts)
3. [Diagram Options](#3-diagram-options)
4. [Clusters](#4-clusters)
5. [Edges](#5-edges)
6. [Node Provider Reference](#6-node-provider-reference)
7. [C4 Nodes via diagrams](#7-c4-nodes-via-diagrams)
8. [Custom Nodes](#8-custom-nodes)
9. [Full Examples](#9-full-examples)

---

## 1. Installation

```bash
# Install Graphviz first (rendering engine)
# macOS
brew install graphviz

# Ubuntu/Debian
sudo apt-get install -y graphviz

# Windows (Chocolatey)
choco install graphviz

# Then install the Python library
pip install diagrams --break-system-packages
```

Python ≥ 3.7 required.

---

## 2. Core Concepts

Everything lives inside a `with Diagram(...)` context manager. Nodes represent
infrastructure components, connected with `>>` (directional) or `-` (undirected) arrows.

```python
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB

with Diagram("My App", show=False):
    ELB("lb") >> EC2("web")
```

**ALWAYS use `show=False`** in server/agent environments — otherwise it tries to
open the PNG with a desktop viewer and will hang or error.

---

## 3. Diagram Options

```python
with Diagram(
    name="Title",               # Also used for output filename (spaces → underscores)
    filename="my_diagram",      # Override output filename (no extension)
    outformat="png",            # "png" | "jpg" | "svg" | "pdf" | "dot"
    show=False,                 # Never auto-open in agent context
    direction="TB",             # "TB" (top-bottom) | "LR" (left-right)
    curvestyle="ortho",         # "ortho" | "curved"
    graph_attr={                # Graphviz graph-level attributes
        "fontsize": "20",
        "bgcolor": "white",
        "pad": "0.5",
        "splines": "spline",    # Edge style: "spline" | "ortho" | "polyline"
        "nodesep": "0.8",       # Horizontal spacing between nodes
        "ranksep": "1.0",       # Vertical spacing between ranks
    },
    node_attr={                 # Graphviz node-level attributes
        "fontsize": "12",
    },
    edge_attr={                 # Graphviz edge-level attributes
        "minlen": "2",
    },
):
    ...
```

---

## 4. Clusters

Group related nodes visually with `Cluster`:

```python
from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS

with Diagram("Clustered", show=False):
    with Cluster("Public Subnet"):
        web = EC2("web")
    with Cluster("Private Subnet"):
        db = RDS("db")
    web >> db
```

Clusters can be nested:
```python
with Cluster("VPC"):
    with Cluster("AZ-1"):
        ec2_a = EC2("app-a")
    with Cluster("AZ-2"):
        ec2_b = EC2("app-b")
```

---

## 5. Edges

```python
from diagrams import Edge

# Simple flow
A >> B

# Reverse flow
A << B

# Undirected / bidirectional
A - B

# Labelled edge
A >> Edge(label="HTTPS") >> B

# Styled edge
A >> Edge(label="async", color="firebrick", style="dashed") >> B

# Fan out (list)
lb >> [web1, web2, web3]

# Fan in
[web1, web2] >> db
```

Edge styles: `"solid"` (default), `"dashed"`, `"dotted"`, `"bold"`

---

## 6. Node Provider Reference

### AWS
```python
from diagrams.aws.compute    import EC2, Lambda, ECS, EKS, Fargate, Batch
from diagrams.aws.database   import RDS, Aurora, Dynamodb, ElastiCache, Redshift
from diagrams.aws.network    import ELB, ALB, NLB, Route53, VPC, CloudFront, APIGateway
from diagrams.aws.storage    import S3, EBS, EFS, Glacier
from diagrams.aws.security   import IAM, Cognito, Shield, WAF, KMS
from diagrams.aws.integration import SQS, SNS, Eventbridge, StepFunctions
from diagrams.aws.management import Cloudwatch, Cloudformation, SystemsManager
from diagrams.aws.analytics  import Kinesis, Glue, Athena, EMR
from diagrams.aws.ml         import Sagemaker, Rekognition
```

### Azure
```python
from diagrams.azure.compute  import FunctionApps, VM, AKS, ContainerInstances
from diagrams.azure.database import SQLDatabases, CosmosDb, BlobStorage
from diagrams.azure.network  import ApplicationGateway, LoadBalancers, CDNProfiles
from diagrams.azure.storage  import BlobStorage, DataLakeStorage
from diagrams.azure.security import KeyVaults
from diagrams.azure.analytics import EventHubs, StreamAnalyticsJobs
```

### GCP
```python
from diagrams.gcp.compute    import GCE, GKE, Functions, Run
from diagrams.gcp.database   import SQL, Firestore, Bigtable, Spanner
from diagrams.gcp.network    import LoadBalancing, CDN, DNS, VPC
from diagrams.gcp.storage    import GCS
from diagrams.gcp.analytics  import Bigquery, Dataflow, Pubsub
from diagrams.gcp.security   import IAP, KMS
```

### Kubernetes
```python
from diagrams.k8s.compute    import Deployment, Pod, StatefulSet, DaemonSet, Job
from diagrams.k8s.network    import Service, Ingress, NetworkPolicy
from diagrams.k8s.storage    import PersistentVolume, PersistentVolumeClaim, StorageClass
from diagrams.k8s.rbac       import ClusterRole, Role, ServiceAccount
from diagrams.k8s.infra      import Node, Namespace
```

### On-Premises / Generic
```python
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL, MySQL, MongoDB, Redis
from diagrams.onprem.network import Nginx, HAProxy, Traefik, Envoy
from diagrams.onprem.queue   import Kafka, RabbitMQ, Celery
from diagrams.onprem.monitoring import Grafana, Prometheus, Datadog
from diagrams.onprem.ci      import Jenkins, GitlabCI, GithubActions
from diagrams.onprem.vcs     import Git, Github, Gitlab
from diagrams.generic.compute import Rack
from diagrams.generic.network import Firewall, Router, Switch
from diagrams.generic.storage import Storage
```

---

## 7. C4 Nodes via diagrams

The `diagrams` library includes C4 nodes for creating C4-style diagrams programmatically:

```python
from diagrams import Diagram
from diagrams.c4 import (
    Person, Container, Database, System,
    SystemBoundary, Relationship
)

graph_attr = {"splines": "spline"}

with Diagram("Container Diagram", direction="TB", graph_attr=graph_attr, show=False):
    customer = Person(
        name="Customer",
        description="A user of the system"
    )
    with SystemBoundary("My Application"):
        web = Container(
            name="Web App",
            technology="React",
            description="Frontend SPA"
        )
        api = Container(
            name="API",
            technology="Node.js",
            description="REST API"
        )
        db = Database(
            name="Database",
            technology="PostgreSQL",
            description="Stores all data"
        )
    ext = System(
        name="Payment Gateway",
        description="Stripe",
        external=True
    )
    customer >> Relationship("Uses") >> web
    web >> Relationship("Calls") >> api
    api >> Relationship("Reads/Writes") >> db
    api >> Relationship("Processes payments") >> ext
```

Note: For full C4 model compliance with all level types (Context/Container/Component/Deployment),
use C4-PlantUML instead (see `references/c4-plantuml.md`).

---

## 8. Custom Nodes

Use your own icons:

```python
from diagrams import Diagram
from diagrams.custom import Custom

with Diagram("Custom Icons", show=False):
    my_service = Custom("My Service", "./assets/my_icon.png")
```

The icon should be a PNG file, ideally 256×256px.

---

## 9. Full Examples

### Multi-tier AWS Web Application

```python
from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EC2, Lambda
from diagrams.aws.database import RDS, ElastiCache
from diagrams.aws.network import ELB, Route53, CloudFront, APIGateway
from diagrams.aws.storage import S3
from diagrams.aws.security import WAF, Cognito

with Diagram("Multi-tier AWS Application", show=False, direction="TB",
             filename="aws_web_app",
             graph_attr={"pad": "0.5", "nodesep": "0.8"}):

    dns = Route53("DNS")
    cdn = CloudFront("CDN")
    waf = WAF("WAF")
    auth = Cognito("Auth")

    with Cluster("Public Tier"):
        lb = ELB("Load Balancer")

    with Cluster("Application Tier"):
        apps = [EC2("app-1"), EC2("app-2"), EC2("app-3")]

    with Cluster("Data Tier"):
        db_primary = RDS("Primary DB")
        db_replica = RDS("Read Replica")
        cache = ElastiCache("Cache")

    static = S3("Static Assets")
    api_gw = APIGateway("API Gateway")
    fn = Lambda("Functions")

    dns >> cdn >> waf >> lb >> apps
    apps >> db_primary >> db_replica
    apps >> cache
    cdn >> static
    apps >> Edge(label="async") >> api_gw >> fn
    auth >> apps
```

### Kubernetes Microservices

```python
from diagrams import Diagram, Cluster, Edge
from diagrams.k8s.compute import Deployment, Pod
from diagrams.k8s.network import Service, Ingress
from diagrams.k8s.storage import PersistentVolumeClaim
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.monitoring import Prometheus, Grafana

with Diagram("Kubernetes Microservices", show=False, direction="LR",
             filename="k8s_services"):

    ingress = Ingress("Ingress")

    with Cluster("namespace: frontend"):
        fe_svc = Service("frontend-svc")
        fe_dep = Deployment("frontend")
        ingress >> fe_svc >> fe_dep

    with Cluster("namespace: backend"):
        api_svc = Service("api-svc")
        api_dep = Deployment("api")
        fe_dep >> api_svc >> api_dep

    with Cluster("namespace: data"):
        db_svc = Service("db-svc")
        db_dep = Deployment("postgres")
        pvc = PersistentVolumeClaim("db-pvc")
        api_dep >> db_svc >> db_dep >> pvc

    with Cluster("namespace: monitoring"):
        prom = Prometheus("prometheus")
        graf = Grafana("grafana")
        prom >> graf
```
