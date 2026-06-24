# Deploy Virto Commerce on AWS

!!! warning 
    Virto Commerce officially ships an Azure deployment template ([**azuredeploy.json**](https://github.com/VirtoCommerce/vc-platform/blob/master/azuredeploy.json)) for self-hosted Azure and the **Virto Cloud** managed-hosting product (which has its own internal Terraform and Helm assets tied to Virto Cloud's infrastructure). **AWS self-hosted topologies are partner-implemented reference patterns**, not Virto-supported turnkey deployments. The Virto Commerce GitHub organization does not publish CloudFormation templates, CDK constructs, Terraform modules, or Helm charts for self-hosted AWS, and the Virto Cloud assets are not made available for self-hosted AWS use. Use this guide as a starting point for your own infrastructure-as-code, and verify each component against the latest Virto Commerce release before going to production.

This guide describes deployment patterns on Amazon Web Services across the following container topologies: 

* Elastic Beanstalk
* ECS on EC2
* ECS on Fargate
* EKS


## Required components

Virto Commerce's [**docker-compose.override.yml**](https://github.com/VirtoCommerce/vc-platform/blob/master/docker-compose.override.yml) declares the minimum dependency set.

| Component | Purpose | Required |
| --- | --- | --- |
| Database | Stores catalog, orders, customers, security, and module state. | Yes. Microsoft SQL Server or PostgreSQL. |
| Search backend | Indexed product, content, and order search. | Yes. Lucene (in-process; single-instance only), Elasticsearch 7/8/9, or Azure AI Search. On AWS, Amazon OpenSearch in Elasticsearch 7 compatibility mode is the natural choice. |
| Blob storage | Stores product images, CMS assets, exports, and uploaded files. | Yes. FileSystem (local volume) or Azure Blob Storage. There is no first-party Amazon S3 provider. <br> ![Readmore](media/readmore.png){: width="25"} [Storage strategy](#storage-strategy) |
| Cache (Redis) | Distributed cache for multi-instance deployments. | Optional for single-instance. Required for multi-instance to keep cache coherent. |

## AWS service mapping

Translating the Virto-supported Azure topology to AWS:

| Concern | Azure (Virto-supported) | AWS (reference equivalent) |
| --- | --- | --- |
| Container host | App Service for Linux | Elastic Beanstalk, ECS (EC2 or Fargate), or EKS |
| Database | Azure SQL Database | Amazon RDS for SQL Server, or RDS / Aurora for PostgreSQL |
| Cache | Azure Cache for Redis | Amazon ElastiCache for Redis |
| Search | Azure AI Search / self-hosted Elasticsearch | Amazon OpenSearch (Elasticsearch 7 compatibility mode) |
| Blob storage | Azure Blob Storage (first-party module) | No first-party module.<br> ![Readmore](media/readmore.png){: width="25"} [Storage strategy](#storage-strategy). |
| Container registry | Azure Container Registry / GitHub Container Registry | Amazon ECR, or pull directly from GitHub Container Registry |
| Load balancer | App Service-integrated | Application Load Balancer |
| Secrets | App Service configuration | AWS Secrets Manager or Systems Manager Parameter Store |
| Persistent volume | Azure Files / App Service file system | Amazon EFS |

## Storage strategy

Virto Commerce does not publish an Amazon S3 blob storage provider. Two patterns work today:

* [FileSystem provider on Amazon EFS](#filesystem-provider-on-amazon-efs) for prototypes and small deployments.
* [Custom S3-backed IBlobStorageProvider](#custom-s3-backed-iblobstorageprovider) for production with significant asset volume.

### FileSystem provider on Amazon EFS

Mount an EFS volume into the container at the Platform's `Assets:FileSystem:RootPath` and `Content:FileSystem:RootPath` paths. The FileSystem provider reads and writes through the EFS mount.

| Pros | Cons|
| ---| ---|
| Uses a first-party Virto provider.<br>Works across ECS, Fargate, EKS, and Beanstalk.| EFS is slower than S3 for large-blob workloads and costs more per GB.|

### Custom S3-backed IBlobStorageProvider

Implement `VirtoCommerce.AssetsModule.Core.Assets.IBlobStorageProvider` against the AWS SDK and package it as a Virto Commerce module. The [Azure Blob Storage module](https://github.com/VirtoCommerce/vc-module-azureblob-assets) is the reference implementation to mirror.


| Pros | Cons|
| ---| ---|
|Native S3 performance, lifecycle policies, S3-class economics.| A custom module to build and maintain.<br> Not part of the Virto-supported module catalog.|


## Module installation

The `platform` image ships without commerce modules; they are installed into the module discovery path (`/app/modules`) on first boot.

The Platform auto-installs the module bundles listed in the `ExternalModules:AutoInstallModuleBundles` setting, which the stock **appsettings.json** defaults to `["commerce"]`. On first startup the Platform downloads those modules into the discovery path, installs them, and then becomes ready. Two implications for self-hosting:

* The modules volume must be **writable** on first boot, and the container needs outbound internet access to pull the module packages from the Virto Commerce feed.
* The install runs once and persists to the volume, so the volume must survive restarts (which EFS does).

!!! warning
    Do not let multiple instances perform the first install concurrently against the same modules volume; they can race and corrupt the modules directory. For the initial deploy, run a single instance, or pre-seed the volume, then scale out after the install finishes.

To use immutable, pre-baked modules instead, build your own image `FROM virtocommerce/platform:latest` with modules copied into the discovery path, set `ExternalModules:AutoInstallModuleBundles` to an empty array, and mount the modules volume read-only.

## Elastic Beanstalk

Use this topology for single-environment deployments, prototypes, and internal pilots. It is the simplest path from a Docker image to a running URL.

The architecture combines:

* Elastic Beanstalk Docker platform that pulls the Virto image.
* RDS for SQL Server (single-AZ for cost) or Aurora PostgreSQL.
* ElastiCache Redis (optional, single-node).
* OpenSearch single-node.
* EFS file system mounted into the Beanstalk EC2 instance.

A minimal **Dockerrun.aws.json** (Beanstalk single-container format) looks like:

```json title="Dockerrun.aws.json"
{
  "AWSEBDockerrunVersion": "1",
  "Image": {
    "Name": "virtocommerce/platform:latest",
    "Update": "true"
  },
  "Ports": [{ "ContainerPort": 80 }],
  "Volumes": [
    { "HostDirectory": "/var/efs/vc-modules", "ContainerDirectory": "/app/modules" },
    { "HostDirectory": "/var/efs/vc-cms",     "ContainerDirectory": "/app/wwwroot/cms-content" }
  ]
}
```

Connection strings, search settings, and asset paths are configured through the Beanstalk environment-properties UI or CLI. 

![Readmore](media/readmore.png){: width="25"} [Configuration reference](#configuration-reference)

**Limitations**: Single-container, single-instance by default. Scaling to multiple instances requires Redis for cache coherence and a non-Lucene search backend, plus an external load balancer.

## ECS on EC2 or Fargate

Use this topology for production deployments where you want explicit task-definition control without operating Kubernetes. ECS on Fargate removes EC2 management. ECS on EC2 gives more instance-level control, including custom AMIs, GPU support, and persistent local storage.

The architecture combines:

* An ECS task definition that wraps the Virto image.
* An Application Load Balancer fronting the ECS service.
* RDS for SQL Server or PostgreSQL.
* ElastiCache Redis cluster.
* OpenSearch domain.
* EFS volume attached to the task definition for `/app/modules` and `/app/wwwroot/cms-content`.

A minimal task-definition fragment:

```json title="virto-task-definition.json"
{
  "family": "virto-platform",
  "requiresCompatibilities": ["FARGATE"],
  "networkMode": "awsvpc",
  "cpu": "1024",
  "memory": "2048",
  "containerDefinitions": [
    {
      "name": "vc-platform",
      "image": "virtocommerce/platform:latest",
      "portMappings": [{ "containerPort": 80 }],
      "mountPoints": [
        { "sourceVolume": "vc-modules", "containerPath": "/app/modules" },
        { "sourceVolume": "vc-cms",     "containerPath": "/app/wwwroot/cms-content" }
      ],
      "secrets": [
        { "name": "ConnectionStrings__VirtoCommerce", "valueFrom": "arn:aws:secretsmanager:...:vc-db-connection" }
      ],
      "environment": [
        { "name": "Search__Provider",              "value": "ElasticSearch" },
        { "name": "Search__ElasticSearch__Server", "value": "https://your-opensearch-endpoint" }
      ]
    }
  ],
  "volumes": [
    { "name": "vc-modules", "efsVolumeConfiguration": { "fileSystemId": "fs-xxxx", "rootDirectory": "/vc-modules" } },
    { "name": "vc-cms",     "efsVolumeConfiguration": { "fileSystemId": "fs-xxxx", "rootDirectory": "/vc-cms" } }
  ]
}
```

Switch `requiresCompatibilities` to `["EC2"]` and adjust the service's launch type for the EC2 variant. Everything else is unchanged.

With more than one task running, configure Redis for distributed caching by adding `ConnectionStrings__RedisConnectionString` from Secrets Manager. Lucene cannot be used as the search backend in this topology; use OpenSearch.

## EKS

Use this topology when you have an existing Kubernetes investment, multi-tenant or multi-environment workloads, or a GitOps pipeline such as Argo CD or Flux. EKS is the most portable option and the one with the highest operational complexity.

The architecture combines:

* A Kubernetes Deployment running the Virto image.
* A ClusterIP Service plus Ingress, typically backed by the AWS Load Balancer Controller.
* RDS, ElastiCache, and OpenSearch outside the cluster, accessed via VPC endpoints.
* Persistent modules and content via the EFS CSI driver and PersistentVolumeClaims.

A minimal Deployment manifest:

```yaml title="vc-platform-deployment.yaml"
apiVersion: apps/v1
kind: Deployment
metadata:
  name: vc-platform
spec:
  replicas: 2
  selector:
    matchLabels:
      app: vc-platform
  template:
    metadata:
      labels:
        app: vc-platform
    spec:
      containers:
        - name: vc-platform
          image: virtocommerce/platform:latest
          ports:
            - containerPort: 80
          envFrom:
            - secretRef:
                name: vc-platform-secrets
          env:
            - name: Search__Provider
              value: ElasticSearch
            - name: Search__ElasticSearch__Server
              value: https://your-opensearch-endpoint
          volumeMounts:
            - { name: vc-modules, mountPath: /app/modules }
            - { name: vc-cms,     mountPath: /app/wwwroot/cms-content }
      volumes:
        - name: vc-modules
          persistentVolumeClaim: { claimName: vc-modules-pvc }
        - name: vc-cms
          persistentVolumeClaim: { claimName: vc-cms-pvc }
```

Fargate profiles in EKS can run the Virto pod, but EFS-backed PVCs work differently than on EC2 nodes. Validate the volume strategy against your EKS and Fargate versions before committing.

Virto Commerce does not publish a public Helm chart for self-hosted deployments. Virto Cloud (the managed-hosting product) maintains an internal Helm chart and Terraform stack, but those artifacts are tied to Virto Cloud's specific infrastructure and are not made available for self-hosted AWS use. Wrap the manifest above in your own chart, or use Kustomize.

## Configuration reference

The Virto Commerce Platform reads configuration through standard ASP.NET Core conventions. Environment variables override the **appsettings.json** values using the `__` (double underscore) separator for nested keys.

The minimum set of environment variables for an AWS deployment:

| Variable | Purpose | Source |
| --- | --- | --- |
| `ConnectionStrings__VirtoCommerce` | Main database connection string. | AWS Secrets Manager |
| `ConnectionStrings__RedisConnectionString` | Redis connection (multi-instance only). | AWS Secrets Manager |
| `Search__Provider` | Set to `ElasticSearch` for OpenSearch. | Environment variable |
| `Search__ElasticSearch__Server` | OpenSearch endpoint URL. | Environment variable |
| `Search__ElasticSearch__User` | OpenSearch user (if fine-grained auth enabled). | AWS Secrets Manager |
| `Search__ElasticSearch__Key` | OpenSearch password or API key. | AWS Secrets Manager |
| `Search__Scope` | Index prefix. Defaults to `default`. | Environment variable |
| `Assets__Provider` | Set to `FileSystem` for EFS-backed storage. | Environment variable |
| `Assets__FileSystem__RootPath` | Mount path of the EFS assets volume. | Environment variable |
| `Assets__FileSystem__PublicUrl` | Public URL prefix for asset delivery (typically your CDN). | Environment variable |
| `Content__Provider` | Set to `FileSystem`. | Environment variable |
| `Content__FileSystem__RootPath` | Mount path of the EFS CMS volume. | Environment variable |
| `Content__FileSystem__PublicUrl` | Public URL prefix for CMS content. | Environment variable |
| `VirtoCommerce__DiscoveryPath` | Module discovery path; typically `/app/modules`. | Environment variable |
| `ExternalModules__AutoInstallModuleBundles__0` | First module bundle to auto-install on first boot. Defaults to `commerce`. | Environment variable |

![Readmore](media/readmore.png){: width="25"} [appsettings.json reference](../../Configuration-Reference/appsettingsjson.md)

## Next steps

1. Choose your topology based on team familiarity and operational maturity. Beanstalk for prototypes, ECS for production without Kubernetes, EKS for Kubernetes-native.
1. Decide on the storage pattern: EFS for simplicity, custom S3 module for performance.
1. Provision the dependencies (RDS, ElastiCache, OpenSearch, EFS) in the same VPC as your container hosts.
1. Wire secrets through AWS Secrets Manager and reference them from your task definition or pod spec.
1. Deploy the Virto image, point it at the dependencies via environment variables, and verify by accessing the Admin UI.
1. Reach out to your Virto Commerce account team to validate the topology against the latest Platform release.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../overview">← Tutorials and how-tos</a>
    <a href="../deploy-platform-on-gcp">Deploy on Google Cloud →</a>
</div>