# Getting to Know Virto Commerce Platform

The **Virto Commerce Platform** is the foundational core of the entire Virto ecosystem serving as:

* A **back office** and **master data management** system.
* An **admin UI** host.
* An **integration hub**, exposing comprehensive **REST** and **GraphQL APIs**.
* A **headless**, modular foundation not bound to any specific frontend.

You can integrate it into an existing architecture as a central system, or use it as a standalone module for specialized functionality (such as pricing, promotions, or catalog services).


## Architectural pillars

* [Modularity](Fundamentals/Modularity/01-overview.md):

    * All business logic is delivered as independent modules.
    * The base installation is minimal — only install what you need.
    * Modules can be replaced or extended without affecting the core Platform.
    * The Platform can be used as a full e-commerce core or embedded as a subsystem in larger solutions. For example, it can be used solely as a pricing engine or as a marketing promotion service.

* Headless architecture:

    * Business logic is exposed entirely via APIs.
    * [REST](https://virtostart-demo-admin.govirto.com/docs/index.html) is commonly used for integrations and admin tools.
    * [GraphQL](GraphQL-Storefront-API-Reference-xAPI/index.md) is optimized for frontend applications — reducing overfetching, improving performance, and enabling tailored data retrieval.

* [Extensibility](Extensibility/overview.md):

    * The Platform includes only essential, general-purpose functionality (e.g., catalog, orders, pricing) to prevent complexity and maintainability issues.
    * Extension points allow deep behavior customization without modifying the Platform’s core:

        * Extending or customizing data models.
        * Changing how orders are processed.
        * Modifying search indexing.
        * Integrating with external payment providers.
        * Overriding calculation workflows or event handlers.

    * Partners can not only extend the Platform but also override default modules entirely.

* [Scalability](Fundamentals/Scalability/scalability-options.md):

    * Running multiple instances simultaneously.
    * Supports **horizontal scaling**.
    * Caching, transactions, and data consistency are all handled seamlessly.
    * Stable operation across distributed environments.


## Core components

The Platform is built around three main architectural elements:

1. **Host application**: The entry point and runtime environment.
1. **Modular engine**: Responsible for loading, initializing, and managing modules dynamically.
1. **Backoffice UI (admin interface)**: A user interface layer for interacting with Platform features exposed by modules.

You can run the Platform without any business modules to get a lightweight shell ready to load whatever functionality you need.

## Cross-cutting services (out of the box)

These services are shared across all modules:

* [Caching](Fundamentals/Caching/01-overview.md) (including [Redis](Fundamentals/Caching/03-setting-up-Redis.md) for distributed sync).
* [Database integration and persistence](Fundamentals/Persistence/DB-Agnostic/overview.md).
* Web service infrastructure.
* [Authentication](Fundamentals/Security/authentication/overview.md) and [authorization](Fundamentals/Security/authorization/overview.md).
* Background jobs (via [Hangfire](Fundamentals/Scalability/scaling-configuration-on-azure-cloud.md#configure-hangfire-server-to-process-background-jobs-in-another-process)).
* [Centralized logging](Fundamentals/Logging/overview.md) and auditing.
* Configuration management.
* [Localization and internationalization](Platform-Manager/localization.md).
* Host application for administrative UI.

All business-specific capabilities (like catalog, pricing, marketing, or order management) are delivered as installable modules. 


## Modules

[Modules](../../user-guide/index) are the primary unit of functional delivery into the Platform. Each module can include:

* A data layer, which defines or extends the domain model and database schema.
* A business logic layer, encapsulating domain services and rules.
* A service layer, exposing APIs (REST or GraphQL) for integration.
* (Optionally) a UI extension, integrating with the administrative interface.

Each module is discovered and initialized at runtime. It can register its own services, extend APIs, and inject views into the admin UI, without altering the Platform code. Modules can be installed, upgraded, or replaced without impacting the core Platform or other features.

### Dependencies

While loosely coupled by design, some modules may depend on others. These dependencies are declared to ensure proper loading order during initialization.

These dependencies can be defined on different levels:

* **At the project level**: For example, add a NuGet package reference to another module.
* **In the module manifest**: Declare other modules the current one depends on and how they should be loaded.
* **During startup**: the Platform analyzes these declarations and ensures that all modules are initialized in the correct sequence. This is essential when developing or maintaining complex solutions, especially 
those involving many interconnected components.

## Versioning and update strategy

Virto Commerce uses a **modular versioning** strategy. The ecosystem includes over 80 modules, but essential ones are grouped into **bundles**:

* [Stable bundles](Updating-Virto-Commerce-Based-Project/stable-releases.md):

    * Released \~every 3 months.
    * Fully tested and recommended for production.
    * Migration guides provided if breaking changes occur.

* [Edge releases](Updating-Virto-Commerce-Based-Project/edge-releases.md):

    * Released more frequently.
    * Include the latest features and fixes.
    * Less testing depth than stable releases.

Choose **Stable** for reliability or **Edge** for faster iteration and access to cutting-edge features.

<br>
<br>
********

<div style="display: flex; justify-content: flex-end;">
    <a href="../">Platform documentation overview →</a>
</div>