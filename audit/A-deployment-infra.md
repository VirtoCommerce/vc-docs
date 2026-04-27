# Group A — Deployment & Infrastructure

## Claim 1: AWS-specific deployment (ECS/EKS/Elastic Beanstalk/Fargate) is not documented.
**Context7** (`/virtocommerce/vc-docs`, query: "How do I deploy VirtoCommerce to AWS using ECS, EKS, Fargate, or Elastic Beanstalk? Are there AWS-specific deployment guides?"):
No AWS-specific results. Closest hits: a generic `vc-build CloudDeploy` CLI for Virto Cloud, a statement that the platform can run on "Virto cloud, Azure cloud, or on-premises", and one multi-region note listing "Microsoft Azure, AWS, Google Cloud, or Alibaba Cloud" as possible cloud providers. No ECS / EKS / Fargate / Beanstalk mentions.

**WebSearch** (query: "VirtoCommerce AWS EKS ECS Fargate deployment guide"):
Only generic AWS docs/blog posts on EKS/ECS/Fargate patterns — no VirtoCommerce-specific AWS deployment guide found on the public web. Web search explicitly calls out "did not contain specific documentation or guides for VirtoCommerce deployments" on AWS services.

**Grep** (scope: DOCS):
- `grep -rli "AWS" DOCS`: 25 files (most are coincidental: "aware", "always", etc. false-positive from case-insensitive tokens; only \bAWS\b literal appears in 1 doc)
- `grep -rnI "\bAWS\b" DOCS` (Deployment/Platform guides only): 1 hit
- `grep -rnIi "EKS|ECS|Fargate|Beanstalk" DOCS`: **0 hits**
- Top hit: `PlatformUserGuide/platform/user-guide/docs/multiregional-ecommerce.md:41` — "…install it at a cloud provider such as Microsoft Azure, AWS, Google Cloud, or Alibaba Cloud."
- `DeploymentGuide` directory: **0 AWS mentions**

**Verdict**: 🔴
**Note**: AWS is name-dropped once in a multi-region scaling paragraph; no ECS/EKS/Fargate/Beanstalk anywhere. An AWS-first prospect gets effectively nothing.

---

## Claim 2: Google Cloud Platform (GKE, Cloud Run) deployment is not documented.
**Context7** (`/virtocommerce/vc-docs`, query: "How do I deploy VirtoCommerce to Google Cloud Platform (GCP) using GKE or Cloud Run? Is there a Google Cloud deployment guide?"):
No GCP deployment results. "Google Cloud" appears only in (a) Google SSO configuration steps ("Google Cloud Console") and (b) the same multi-region scaling paragraph listing it alongside AWS/Azure/Alibaba. No GKE/Cloud Run content.

**WebSearch** (query: "VirtoCommerce 'Google Cloud' OR GKE OR 'Cloud Run' deployment"):
Only generic Google Cloud deployment docs surfaced — no VirtoCommerce-specific GCP deployment guides found.

**Grep** (scope: DOCS):
- `grep -rli "Google Cloud|GCP|GKE|Cloud Run" DOCS`: 4 files
- `grep -rnIi "GKE|Cloud Run" DOCS`: **0 hits**
- Top hits:
  - `VirtoCommerce/industry/pharmaceutical.md:76` — "…private cloud (Microsoft Azure, Amazon Web Services, or Google Cloud), or hybrid."
  - `PlatformUserGuide/.../multiregional-ecommerce.md:41` — same multi-cloud name-drop line.
  - `PlatformDeveloperGuide/.../appsettingsjson.md:876-877` — "Google Cloud Console" for OAuth credentials (unrelated to hosting).

**Verdict**: 🔴
**Note**: GCP exists only as a name in a list. Zero GKE, zero Cloud Run, zero Google-specific deployment instructions.

---

## Claim 3: Kubernetes / Helm charts / manifests are not documented.
**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce provide Kubernetes manifests or Helm charts? How do I deploy the platform on a Kubernetes cluster?"):
The only Helm-adjacent content is the `vc-build CloudEnvSetParameter -HelmParameters platform.config.paramname=...` CLI for **Virto Cloud** (a managed PaaS, which internally runs on Kubernetes-in-Azure). No public Helm chart URL, no manifest examples, no self-hosted Kubernetes walkthrough.

**WebSearch**: not required (Context7 and grep produced sufficient signal).

**Grep** (scope: DOCS):
- `grep -rli "Kubernetes|k8s|Helm|kubectl" DOCS`: 6 files
- `grep -rnIi "Helm" DOCS`: 1 substantive hit (the CloudEnvSetParameter CLI), 1 false positive ("overwhelming")
- `grep -rnIi "kubectl|kubeconfig|deployment.yaml|manifest.yaml" DOCS`: **0 hits**
- Top hits:
  - `VirtoCommerce/open-source-net-ecommerce-platform.md:14` — marketing line: "Kubernetes container support"
  - `VirtoCommerce/index.md:91,127` + `marketplace.md:164` — "Extensible PaaS cloud-native infrastructure built on Kubernetes"
  - `PlatformDeveloperGuide/.../virto-cloud-overview.md:35` — "VC Cloud runs on Kubernetes in Azure"
  - `PlatformDeveloperGuide/.../virto-cloud.md:128` — `-HelmParameters` CLI flag

**Verdict**: 🟠
**Note**: Kubernetes is a marketing bullet and an internal implementation detail of Virto Cloud. Customers wanting to self-host on their own K8s cluster get no manifests, no Helm chart, no worked example.

---

## Claim 4: Docker multi-stage / compose for production is poorly documented.
**Context7** (`/virtocommerce/vc-docs`, query: "How do I run VirtoCommerce in production with Docker and docker-compose? Is there a production Dockerfile with multi-stage build or a production compose file?"):
Only a **development-oriented** compose workflow surfaces: `DockerCompose/ModulesDevelop/docker-compose.yml` for module development, plus a standalone Elastic App Search compose snippet. No production Dockerfile example, no multi-stage build example, no production-hardening compose (health checks, restart policies, resource limits, secrets, reverse proxy, TLS).

**WebSearch**: not required.

**Grep** (scope: DOCS):
- `grep -rli "Docker|docker-compose|Dockerfile" DOCS`: 14 files
- `grep -rnIi "multi-stage|multistage|docker-compose.prod" DOCS`: **0 hits**
- `grep -rnIi "docker-compose|docker compose" DOCS`: 14 hits, all development-flavored
- Top hits:
  - `PlatformDeveloperGuide/.../docker-modules-development.md:9-125` — whole page dedicated to ModulesDevelop compose for dev workflow
  - `PlatformDeveloperGuide/.../configuring-elastic-app-search.md:52,234` — compose for Elastic App Search
  - `PlatformDeveloperGuide/.../appsettingsjson.md:2467` — one-line example of env vars in compose
  - `StorefrontDeveloperGuide/.../migration-on-local-machine.md:5` — passing mention

**Verdict**: 🟡
**Note**: Docker Compose is documented, but only for local dev. No multi-stage Dockerfile guidance, no production compose with TLS/healthchecks/secrets, no ops-grade hardening.

---

## Claim 5: Infrastructure-as-Code (Terraform, Pulumi, Bicep, ARM, CloudFormation) is absent.
**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce provide Terraform modules, Pulumi, Bicep, ARM templates, or CloudFormation for infrastructure-as-code deployment?"):
Only **ARM** templates surface — `azureDeployWebAppForContainer.json`, `azuredeploy.json`, plus "Deploy to Azure" button and Azure Resource Manager CLI/PowerShell instructions. No Terraform/Pulumi/Bicep/CloudFormation mentions.

**WebSearch** (query: "VirtoCommerce Terraform module infrastructure as code"):
No VirtoCommerce-specific Terraform module found. Results are generic Terraform/IaC marketing pages.

**Grep** (scope: DOCS):
- `grep -rnIi "Terraform|Pulumi|Bicep|CloudFormation" DOCS`: **0 hits**
- `grep -rnIi "infrastructure.as.code|IaC" DOCS`: **0 hits**
- `grep -rnIi "ARM template|Resource Manager|azureDeploy" DOCS`: ~10 hits, all Azure ARM
- Top hits:
  - `PlatformDeveloperGuide/.../deploy-platform-on-azure.md:5,61-66` — ARM template "Deploy to Azure" button + PowerShell/CLI
  - `PlatformDeveloperGuide/.../deploy-storefront-on-azure.md:3,41-46` — same pattern for storefront
  - `StorefrontDeveloperGuide/.../migration-on-azure.md:9,15` — "modify the ARM template"

**Verdict**: 🟠
**Note**: ARM templates are present (Azure-only) but Terraform/Pulumi/Bicep/CloudFormation are entirely absent. IaC is a "maybe, if you like ARM" story — no modern cross-cloud IaC path.

---

## Claim 6: GitOps / ArgoCD / Flux is absent.
**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce support GitOps workflows with ArgoCD or Flux? How do I set up continuous deployment with GitOps?"):
`DeploymentGuide/.../enable-gitops.md` is a dedicated GitOps guide — enable toggle, GitHub template, secrets, workflow triggers, "Synced and Healthy" statuses (implicitly ArgoCD terminology). ArgoCD appears by name once in `virto-cloud-overview.md`. Flux is not mentioned.

**WebSearch**: not required.

**Grep** (scope: DOCS):
- `grep -rnIi "GitOps" DOCS` (DeploymentGuide only): 10 hits — whole `enable-gitops.md` page plus cross-refs
- `grep -rnIi "ArgoCD" DOCS`: 1 hit — `PlatformDeveloperGuide/.../virto-cloud-overview.md:51` "ArgoCD: For deployment and rollout management."
- `grep -rnIi "Flux" DOCS`: 0 hits for Flux-as-GitOps-tool
- Top hits:
  - `DeploymentGuide/.../enable-gitops.md:1-18` — step-by-step GitOps enable
  - `DeploymentGuide/.../qa-new-environment.md:67-71` — GitOps toggle in UI
  - `PlatformDeveloperGuide/.../virto-cloud-overview.md:51` — lists ArgoCD as a Virto Cloud component

**Verdict**: 🟡
**Note**: GitOps is documented but **only** inside the managed Virto Cloud experience. ArgoCD is named once; Flux is absent. No self-hosted GitOps recipe, no generic ArgoCD Application CR example.

---

## Claim 7: Zero-downtime deployment, blue/green, canary, rolling deploys are absent.
**Context7** (`/virtocommerce/vc-docs`, query: "How do I do zero-downtime deployments, blue/green, canary, or rolling deploys on VirtoCommerce? How do I roll back safely?"):
Zero-downtime deploys surface only as a one-line **Virto Cloud** feature ("Updates are released safely with zero-downtime rollouts"). No walkthrough. Feature flags are offered for "rollback control" as a substitute. Blue/green in Context7 is almost entirely about **search indexing**, not deployment.

**WebSearch**: not required.

**Grep** (scope: DOCS):
- `grep -rnIi "blue.green|blue/green" DOCS`: 12+ hits, all but one refer to **search indexing** (`blue-green-indexing.md`, `managing-search.md`)
- `grep -rnIi "canary" DOCS`: 1 hit — only in a B2BExperts McKinsey quote (`B2BExperts/.../The-big-product-and-platform-shift-five-actions.md:88`)
- `grep -rnIi "zero.downtime|zero-downtime" DOCS`: 2 hits — `virto-cloud-overview.md:16` + `indexing/overview.md:27` (the latter about index rebuild)
- `grep -rnIi "rolling deploy|rolling update|rolling release" DOCS`: **0 hits**
- Top hits:
  - `PlatformDeveloperGuide/.../virto-cloud-overview.md:16` — "Blue-green deployment: Updates are released safely with zero-downtime rollouts." (one line, no "how")
  - `PlatformUserGuide/.../search/managing-search.md:48-87` — real content, but about search indexes
  - `B2BExperts/.../The-big-product-and-platform-shift-five-actions.md:88` — "canary release techniques" quoted from McKinsey, not VC-specific

**Verdict**: 🟠
**Note**: VC clearly supports zero-downtime *internally* (Virto Cloud does it), but "blue-green" in docs almost always means search indexing. Canary, rolling, and rollback playbooks for app deploys are absent.

---

## Claim 8: Horizontal scaling / autoscaling / load balancing is poorly documented.
**Context7** (`/virtocommerce/vc-docs`, query: "How do I horizontally scale VirtoCommerce? Does it support autoscaling or load balancing across multiple instances?"):
A dedicated **Scalability** section exists: Redis backplane for cache + SignalR, architectural pillar "Horizontal scaling", multi-instance distributed lock via Redis. Example is Azure-only (`scaling-configuration-on-azure-cloud.md`).

**WebSearch**: not required.

**Grep** (scope: DOCS):
- `grep -rnIi "horizontal scal" DOCS`: 1 direct hit (`getting-to-know-platform.md:44`) + the scaling-configuration file
- `grep -rnIi "autoscal|auto-scal|auto scaling|HPA" DOCS`: **0 hits** — autoscaling/HPA entirely absent
- `grep -rnIi "load balanc" DOCS`: ~10 hits, mostly storefront architecture
- Top hits:
  - `PlatformDeveloperGuide/.../getting-to-know-platform.md:44` — "Supports horizontal scaling"
  - `PlatformDeveloperGuide/.../Scalability/scaling-configuration-on-azure-cloud.md` — full page on Redis backplane & ARR affinity (Azure-only)
  - `StorefrontDeveloperGuide/.../architecture.md:11,14,21-27` — LB as an architecture component (nginx / Azure LB)
  - `PlatformDeveloperGuide/.../Modularity/04-loading-modules-into-app-process.md:38,76` — multi-instance distributed lock

**Verdict**: 🟡
**Note**: Horizontal scaling is clearly supported and documented for Azure. But autoscaling (HPA, KEDA, App Service autoscale rules) is not covered, and the load-balancer story outside Azure / nginx is unspecified.

---

## Claim 9: Session affinity / sticky sessions requirements are poorly documented.
**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce require session affinity or sticky sessions? How do I configure sticky sessions at the load balancer?"):
Clearly documented **for Azure**: "When SignalR is running on a server farm, sticky sessions must be used… enable ARR Affinity." Includes scenario tables with ARR Affinity On/Off per tier.

**WebSearch**: not required.

**Grep** (scope: DOCS):
- `grep -rnIi "session affinity|sticky session|ARR Affinity" DOCS`: 5 hits — all in the one Azure scalability page
- No hits for "cookie-based affinity" or equivalent on AWS ALB / NLB / GCP / nginx `ip_hash`
- Top hits:
  - `PlatformDeveloperGuide/.../Scalability/scaling-configuration-on-azure-cloud.md:48-51` — requirement statement
  - same file lines 115, 153, 190 — scenario tables

**Verdict**: 🟡
**Note**: Sticky-session requirement is clearly called out — but **only** as Azure ARR Affinity. AWS ALB target-group stickiness, nginx `ip_hash`, Kubernetes `sessionAffinity: ClientIP`, and GCP backend-service affinity are not mentioned.

---

## Claim 10: CI/CD beyond GitHub Actions (Azure DevOps, GitLab CI, Jenkins) is absent.
**Context7** (`/virtocommerce/vc-docs`, query: "How do I set up CI/CD for VirtoCommerce with Azure DevOps, GitLab CI, Jenkins, or Bitbucket Pipelines?"):
GitHub Actions + Azure DevOps are called out as "ready-made CI/CD pipelines" for Virto Cloud. vc-build is advertised as "builder-server agnostic" — so CI/CD beyond GHA is positioned as "possible" but no Jenkins/Bitbucket/CircleCI/TeamCity walkthrough is provided. GitLab appears only as a **module source** (GitLab job artifacts, `-GitLabToken`), not as a CI/CD pipeline example.

**WebSearch**: not required.

**Grep** (scope: DOCS):
- `grep -rnIi "Azure DevOps|Azure Pipelines" DOCS`: ~6 hits (Virto Cloud + module source / artifact references)
- `grep -rnIi "GitLab" DOCS`: ~3 hits — all about consuming module artifacts via `-GitLabToken`, not a GitLab-CI pipeline
- `grep -rnIi "Jenkins|Bitbucket Pipelines|TeamCity|CircleCI" DOCS`: **0 hits**
- Top hits:
  - `PlatformDeveloperGuide/.../virto-cloud-overview.md:17,55` — "Ready-to-use pipelines for GitHub Actions or Azure DevOps"
  - `PlatformDeveloperGuide/.../install-and-update-platform-and-modules.md:110-113` — Azure pipeline artifacts / GitLab job artifacts as module sources
  - `PlatformDeveloperGuide/.../build-automation.md:3` — "builder-server agnostic"
  - `PlatformDeveloperGuide/.../Fundamentals/Testing/testing.md:314` — GH Actions workflows only

**Verdict**: 🟡
**Note**: Azure DevOps is first-class alongside GHA. Jenkins/GitLab-CI/Bitbucket/TeamCity get no worked example; the pitch is "vc-build works anywhere". That's thin if a customer standardizes on Jenkins or GitLab CI.

---
