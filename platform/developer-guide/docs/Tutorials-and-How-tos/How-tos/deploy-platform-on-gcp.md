# Deploy Virto Commerce on Google Cloud

!!! warning 
    Virto Commerce officially ships an Azure deployment template ([**azuredeploy.json**](https://github.com/VirtoCommerce/vc-platform/blob/master/azuredeploy.json)) for self-hosted Azure and the **Virto Cloud** managed-hosting product (which has its own internal Terraform and Helm assets tied to Virto Cloud's infrastructure). **Google Cloud self-hosted topologies are partner-implemented reference patterns**, not Virto-supported turnkey deployments. The Virto Commerce GitHub organization does not publish Deployment Manager templates, Config Connector resources, Terraform modules, or Helm charts for self-hosted GCP, and the Virto Cloud assets are not made available for self-hosted GCP use. Use this guide as a starting point for your own infrastructure-as-code, and verify each component against the latest Virto Commerce release before going to production.

This guide describes deployment patterns for Virto Commerce Platform on Google Cloud across two container topologies: Google Kubernetes Engine (GKE) and Cloud Run.

## Required components

Virto Commerce's [**docker-compose.override.yml**](https://github.com/VirtoCommerce/vc-platform/blob/master/docker-compose.override.yml) declares the minimum dependency set.

| Component | Purpose | Required |
| --- | --- | --- |
| Database | Stores catalog, orders, customers, security, and module state. | Yes. Microsoft SQL Server or PostgreSQL. |
| Search backend | Indexed product, content, and order search. | Yes. Lucene (in-process; single-instance only), Elasticsearch 7/8/9, or Azure AI Search. On GCP, the natural choices are Elastic Cloud on GCP Marketplace, or self-managed Elasticsearch on GKE. |
| Blob storage | Stores product images, CMS assets, exports, and uploaded files. | Yes. FileSystem (local volume) or Azure Blob Storage. There is no first-party Google Cloud Storage provider; see [Storage strategy](#storage-strategy). |
| Cache (Redis) | Distributed cache for multi-instance deployments. | Optional for single-instance. Required for multi-instance to keep cache coherent. |

## GCP service mapping

Translating the Virto-supported Azure topology to Google Cloud:

| Concern | Azure (Virto-supported) | Google Cloud (reference equivalent) |
| --- | --- | --- |
| Container host | App Service for Linux | GKE or Cloud Run |
| Database | Azure SQL Database | Cloud SQL for SQL Server, Cloud SQL for PostgreSQL, or AlloyDB for PostgreSQL |
| Cache | Azure Cache for Redis | Memorystore for Redis |
| Search | Azure AI Search / self-hosted Elasticsearch | Elastic Cloud on GCP, or self-managed Elasticsearch on GKE |
| Blob storage | Azure Blob Storage (first-party module) | No first-party module. See workarounds in [Storage strategy](#storage-strategy). |
| Container registry | Azure Container Registry / GitHub Container Registry | Artifact Registry, or pull directly from GitHub Container Registry |
| Load balancer | App Service-integrated | Cloud Load Balancing (HTTP(S) Load Balancer) |
| Secrets | App Service configuration | Secret Manager |
| Persistent volume | Azure Files / App Service file system | Filestore, or Persistent Disk (block-level) |

**Note on managed search**: Unlike AWS (OpenSearch) or Azure (AI Search), GCP does not offer a first-party managed Elasticsearch-compatible service. Elastic Cloud on GCP is a partner offering available through Google Cloud Marketplace; self-managed Elasticsearch on GKE is the alternative if you prefer in-cluster operation.

## Storage strategy

Virto Commerce does not publish a Google Cloud Storage blob provider. The following patterns work today:

* [FileSystem provider on Filestore](#filesystem-provider-on-filestore) for prototypes and small deployments.
* [FileSystem provider on Cloud Storage via gcsfuse](#filesystem-provider-on-cloud-storage-via-gcsfuse).
* [Custom GCS-backed IBlobStorageProvider](#custom-gcs-backed-iblobstorageprovider) for production with significant asset volume.


### FileSystem provider on Filestore

Mount a Filestore NFS volume into the container at the Platform's `Assets:FileSystem:RootPath` and `Content:FileSystem:RootPath` paths. The FileSystem provider reads and writes through the Filestore mount.

| Pros| Cons |
| --- | ---|
| Uses a first-party Virto provider.<br> Works on GKE and on Cloud Run (with Serverless VPC Access plus the Filestore NFS mount feature)| Filestore is provisioned in fixed-size tiers and costs more per GB than Cloud Storage.<br>Filestore has region- and zone-locality constraints.|

### FileSystem provider on Cloud Storage via gcsfuse

Mount a Cloud Storage bucket as a filesystem using Cloud Storage FUSE (gcsfuse). The FileSystem provider then reads and writes through the FUSE mount, while data lives in GCS.

| Pros| Cons |
| --- | ---|
| Combines GCS economics with the first-party FileSystem provider. <br> Cloud Storage FUSE is now supported natively on GKE and Cloud Run. | gcsfuse has known POSIX-semantics caveats. Rename and append are emulated, sequential write latency is higher than block storage, and consistency guarantees are weaker than a real file system. <br> Verify against your workload before production.|

### Custom GCS-backed IBlobStorageProvider

Implement `VirtoCommerce.AssetsModule.Core.Assets.IBlobStorageProvider` against the Google Cloud Storage client library and package it as a Virto Commerce module. The [Azure Blob Storage module](https://github.com/VirtoCommerce/vc-module-azureblob-assets) is the reference implementation to mirror.

| Pros| Cons |
| --- | ---|
| Native GCS performance, lifecycle policies, GCS-class economics, no FUSE caveats.
| A custom module to build and maintain. <br> Not part of the Virto-supported module catalog. |

## GKE

Use this topology when you have an existing Kubernetes investment, multi-tenant or multi-environment workloads, or a GitOps pipeline such as Argo CD or Flux. GKE is the most flexible and most operationally portable option.

The architecture combines:

* A Kubernetes Deployment running the Virto image.
* A ClusterIP Service plus Ingress, backed by the GKE Ingress controller or HTTP(S) Load Balancer.
* Cloud SQL, Memorystore, and Elastic Cloud (or in-cluster Elasticsearch) outside the workload, accessed via VPC peering or Private Service Connect.
* Persistent modules and content via the Filestore CSI driver mounted as PersistentVolumeClaims, or via the Cloud Storage FUSE CSI driver.

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
          image: ghcr.io/virtocommerce/vc-platform/platform:latest
          ports:
            - containerPort: 80
          envFrom:
            - secretRef:
                name: vc-platform-secrets
          env:
            - name: Search__Provider
              value: ElasticSearch
            - name: Search__ElasticSearch__Server
              value: https://your-elastic-endpoint
          volumeMounts:
            - { name: vc-modules, mountPath: /app/modules }
            - { name: vc-cms,     mountPath: /app/wwwroot/cms-content }
      volumes:
        - name: vc-modules
          persistentVolumeClaim: { claimName: vc-modules-pvc }
        - name: vc-cms
          persistentVolumeClaim: { claimName: vc-cms-pvc }
```

Wire `vc-platform-secrets` from Secret Manager via the Secret Manager CSI driver or external-secrets-operator. PersistentVolumeClaims are backed by the Filestore CSI driver (Pattern A) or the GCS FUSE CSI driver (Pattern B).

Virto Commerce does not publish a public Helm chart for self-hosted deployments. Virto Cloud (the managed-hosting product) maintains an internal Helm chart and Terraform stack, but those artifacts are tied to Virto Cloud's specific infrastructure and are not made available for self-hosted GCP use. Wrap the manifest above in your own chart, or use Kustomize.

## Cloud Run

Use this topology for stateless API or storefront tiers, ephemeral environments, or workloads where you want the lowest operational overhead. Cloud Run scales the Virto container automatically and removes infrastructure management.

The architecture combines:

* A Cloud Run service running the Virto image.
* Cloud SQL connected through the Cloud SQL Auth Proxy sidecar, or via private IP and Serverless VPC Access.
* Memorystore via Serverless VPC Access.
* Elastic Cloud or in-cluster Elasticsearch via Serverless VPC Access.
* Persistent modules and CMS content via Filestore (Serverless VPC Access) or Cloud Storage FUSE volume mounts (Cloud Run's built-in support).

!!! warning 
    Cloud Run has architectural constraints that affect Virto deployments. Validate each against your use case before committing.

    * **Stateless instances.** Cloud Run scales to zero and recycles instances. Module changes made at runtime through the Admin UI must be persisted to a mounted volume (Filestore or GCS FUSE); otherwise they vanish on the next cold start.
    * **Request timeout.** Cloud Run requests have a default timeout of 5 minutes, configurable up to 60 minutes. Large catalog imports, bulk operations, and indexing jobs can exceed this. Long-running work should run on a separate worker host (GKE Deployment, GCE VM) and not be triggered from Cloud Run request handlers.
    * **Cold starts.** Virto's module discovery and DI container build add seconds to cold start. Configure minimum-instances ≥ 1 in production to avoid user-visible cold starts.
    * **No Hangfire dashboard from scale-to-zero.** Hangfire background jobs run inside the same process. If Cloud Run scales to zero, scheduled jobs do not fire. Either run the Hangfire-bearing tier on GKE or GCE, or keep a Cloud Run min-instances ≥ 1 instance warm.

A minimal Cloud Run service definition (deployable via `gcloud run services replace`):

```yaml title="vc-platform-service.yaml"
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: vc-platform
spec:
  template:
    metadata:
      annotations:
        run.googleapis.com/cloudsql-instances: project:region:instance
        run.googleapis.com/vpc-access-connector: vc-connector
        autoscaling.knative.dev/minScale: "1"
    spec:
      containerConcurrency: 50
      timeoutSeconds: 900
      containers:
        - image: ghcr.io/virtocommerce/vc-platform/platform:latest
          ports:
            - containerPort: 80
          env:
            - name: Search__Provider
              value: ElasticSearch
            - name: Search__ElasticSearch__Server
              value: https://your-elastic-endpoint
            - name: ConnectionStrings__VirtoCommerce
              valueFrom:
                secretKeyRef:
                  name: vc-db-connection
                  key: value
```

Use Cloud Run for the **storefront API tier** (xCatalog, xCart) where requests are short and stateless. Run the **Admin Platform** on GKE or GCE where module installation, Hangfire jobs, and long-running operations can persist properly. Both tiers point at the same Cloud SQL, Memorystore, and search backend.

## Configuration reference

The Virto Commerce Platform reads configuration through standard ASP.NET Core conventions. Environment variables override the **appsettings.json** values using the `__` (double underscore) separator for nested keys.

The minimum set of environment variables for a Google Cloud deployment:

| Variable | Purpose | Source |
| --- | --- | --- |
| `ConnectionStrings__VirtoCommerce` | Main database connection string. | Secret Manager |
| `ConnectionStrings__RedisConnectionString` | Redis connection (multi-instance only). | Secret Manager |
| `Search__Provider` | Set to `ElasticSearch` for Elastic Cloud or self-managed Elasticsearch. | Environment variable |
| `Search__ElasticSearch__Server` | Elasticsearch endpoint URL. | Environment variable |
| `Search__ElasticSearch__User` | Elasticsearch user. | Secret Manager |
| `Search__ElasticSearch__Key` | Elasticsearch password or API key. | Secret Manager |
| `Search__Scope` | Index prefix. Defaults to `default`. | Environment variable |
| `Assets__Provider` | Set to `FileSystem` for Filestore-backed or gcsfuse-backed storage. | Environment variable |
| `Assets__FileSystem__RootPath` | Mount path of the assets volume. | Environment variable |
| `Assets__FileSystem__PublicUrl` | Public URL prefix for asset delivery (typically Cloud CDN). | Environment variable |
| `Content__Provider` | Set to `FileSystem`. | Environment variable |
| `Content__FileSystem__RootPath` | Mount path of the CMS volume. | Environment variable |
| `Content__FileSystem__PublicUrl` | Public URL prefix for CMS content. | Environment variable |
| `VirtoCommerce__DiscoveryPath` | Module discovery path; typically `/app/modules`. | Environment variable |

![Readmore](media/readmore.png){: width="25"} [appsettings.json reference](../../Configuration-Reference/appsettingsjson.md)

## Next steps

1. Choose your topology based on team familiarity and operational maturity. GKE for full control and long-running workloads, Cloud Run for stateless storefront/API tiers with low operational overhead.
1. Decide on the storage pattern: Filestore for simplicity, gcsfuse for GCS economics with FileSystem semantics, or a custom GCS module for native performance.
1. Provision the dependencies (Cloud SQL, Memorystore, Elasticsearch, Filestore) and wire them to the workload via Serverless VPC Access or VPC peering.
1. Wire secrets through Secret Manager and reference them from your Deployment, Cloud Run service, or sidecar.
1. Deploy the Virto image, point it at the dependencies via environment variables, and verify by accessing the Admin UI.
1. Reach out to your Virto Commerce account team to validate the topology against the latest Platform release.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../deploy-platform-on-aws">← Deploy on AWS</a>
    <a href="../connect-azure-function-to-events">Connect Azure Functions to Virto Events →</a>
</div>