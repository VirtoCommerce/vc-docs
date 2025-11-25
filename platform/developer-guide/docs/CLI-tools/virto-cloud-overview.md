# Overview

**VC Cloud** is an internal **Platform-as-a-Service (PaaS)** solution purpose-built to host and manage projects based on the **Virto Commerce Platform**. It automates the setup, deployment, scaling, and maintenance of infrastructure, helping teams streamline operations and reduce manual overhead.

Designed with scalability, reliability, and developer efficiency in mind, VC Cloud brings together years of deployment experience into a unified, production-ready solution.

VC Cloud takes full responsibility for infrastructure management:

- Automatically provisions resources such as databases, Redis, blob storage, and search indexes.
- Follows best practices in performance, fault tolerance, and security.
- Provides preconfigured logging, monitoring, and alerting for all environments.

## Key benefits

- **Fast provisioning**: Infrastructure is ready in minutes with no manual setup.
- **Blue-green deployment**: Updates are released safely with zero-downtime rollouts.
- **Built-in CI/CD**: Ready-to-use pipelines for GitHub Actions or Azure DevOps.
- **Reduced DevOps overhead**: Developers can focus on features instead of infrastructure.
- **Improved reliability and security**: Standardized environments minimize errors.
- **Centralized maintenance**: Updates and patches are applied consistently.
- **Custom CLI Tools**: Simplify build, deployment, and package management tasks.

VC Cloud enables development teams to operate more efficiently by offloading infrastructure responsibilities. Your team no longer needs to manage:

* Deployment processes.
* Scaling and provisioning.
* Monitoring and alerting.
* Backup routines.

VC Cloud handles the full lifecycle of your solution so you can focus on delivering business value.


## VC Cloud architecture

VC Cloud runs on **Kubernetes in Azure** and includes:

* Application pods.
* Databases.
* Redis cache.
* Blob storage.
* Search indexes.

It supports deployment in both our Azure subscription or your own, depending on your preferences.

![Architecture](media/cloud-architecture.png){: style="display: block; margin: 0 auto;" }

## Tooling

We provide three key tools to manage your environments:

* **ArgoCD**: For deployment and rollout management.
* **Grafana**: For monitoring and metrics visualization.
* **VC CLI**: For automating builds and environment management.

In addition, we offer **ready-made CI/CD pipelines** using GitHub Actions or Azure DevOps to support full automation from build to deployment.


## How it works

Each VC Cloud environment is defined by:

* A **VC Packages file**: Specifies module versions and dependencies.
* A **YAML configuration file**: Defines environment-specific variables and settings.

These files enable reproducible, automated deployments across all stages — from development to production.

For example, a GitHub workflow can automatically build and deploy a new version by referencing these files. The [VC-Build CLI tool](overview.md) helps with packaging, testing, and publishing projects and NuGet packages.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../more-targets">← Managing Platform and modules</a>
    <a href="../virto-cloud">Using Virto Cloud →</a>
</div>