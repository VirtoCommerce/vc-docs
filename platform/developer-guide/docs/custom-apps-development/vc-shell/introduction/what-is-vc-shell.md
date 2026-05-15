# What Is VC-Shell

VC-Shell is the canonical Vue 3 frontend layer for building custom back-office apps on the Virto Commerce Platform. It is the same framework the Virto Commerce Vendor portal is built on, packaged for any team that needs a dedicated admin surface beyond what the bundled Platform manager covers.

You install **@vc-shell/framework** as a Vue plugin, scaffold a project with the CLI, and start writing modules. The framework gives you a complete back-office shell: sidebar, top bar, dashboard, global search, settings, and a blade-paradigm navigation engine. On top of that, it ships an Atomic Design component library, typed API clients generated from the Platform's OpenAPI documents, and integration glue for OAuth, permissions, SignalR, i18n, dynamic properties, and uploaded assets.

You write features as Vue plugins. Each plugin registers itself with the runtime, declares its routes and permissions, and slots into well-defined extension points. The same module runs as a standalone application or as a Module Federation remote loaded into a host shell, so a team can ship a stand-alone admin and a federated bundle from one codebase.

VC-Shell is opinionated about the patterns it supports. It is tuned specifically for Virto Commerce back-office workflows: blade stacks, parent-child messaging, deep linking, close guards, and Platform-aware data access. That is what makes it the default starting point for a Virto Commerce admin app.

## What you get

| Capability | Provided by |
| --- | --- |
| App shell: sidebar, top bar, dashboard, settings, global search. | `framework/shell`. |
| Blade-paradigm navigation: stack, parent-child messaging, URL sync, close guards. | `framework/core/blade-navigation`, `useBlade()`. |
| Atomic Design components: atoms, molecules, organisms (`VcBlade`, `VcDataTable`, `VcForm`, ...). | `framework/ui`. |
| Module runtime with semver compatibility and extension points. | `framework/core/plugins/modularity`, `framework/core/plugins/extension-points`. |
| OAuth, role-based permissions, i18n, notifications, SignalR, dynamic properties, uploaded assets. | `framework/core/plugins/*`. |
| Typed API clients from the Platform's OpenAPI documents. | `@vc-shell/api-client-generator`. |
| Standalone or Module Federation deployment. | `@vc-shell/mf-host`, `@vc-shell/mf-module`. |

## What it is not

- Not a replacement for the Virto Commerce Platform manager. It complements the manager when a customization does not fit inside it.
- Not a CMS. VC-Shell consumes Platform APIs; for content, use the Platform's own catalog and content modules.
- Not a deployment platform. It is the Frontend; deployment is your CI/CD and static hosting story.

![Readmore](architecture-overview.md){: width="25"} See how the pieces fit together in the architecture overview.
