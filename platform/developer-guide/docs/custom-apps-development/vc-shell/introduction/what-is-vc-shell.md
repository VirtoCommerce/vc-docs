# What Is VC-Shell

VC-Shell is the Vue 3 framework for building custom admin applications on top of the Virto Commerce Platform.

You install **@vc-shell/framework** as a Vue plugin, scaffold a project with the CLI, and start writing modules. The framework gives you a complete back-office shell: sidebar, top bar, dashboard, global search, settings, and a blade-paradigm navigation engine. On top of that, it ships an Atomic Design component library, typed API clients generated from the Platform's OpenAPI documents, and integration glue for OAuth, permissions, SignalR, i18n, dynamic properties, and uploaded assets.

You write features as Vue plugins. Each plugin registers itself with the runtime, declares its routes and permissions, and slots into well-defined extension points. The same module runs as a standalone application or as a Module Federation remote loaded into a host shell, so a team can ship a stand-alone admin and a federated bundle from one codebase.

VC-Shell is opinionated about the patterns it supports. It does not try to be a generic admin kit. It is tuned for Virto Commerce back-office workflows: blade stacks, parent-child messaging, deep linking, close guards, and Platform-aware data access.

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

- Not a general-purpose admin template. Use Quasar or Vuetify if you need a generic admin kit.
- Not a CMS. VC-Shell consumes Platform APIs; for content management, use the Platform's own content modules.
- Not a replacement for the bundled Platform manager. When customization fits inside the manager, extend the manager instead.
- Not framework-agnostic. Vue 3 + Composition API is hardcoded; for React or Angular admins, pick a different framework.

## How it compares

| | VC-Shell | Vue + general admin kit | Platform manager |
| --- | --- | --- | --- |
| Target. | Back-office apps for Virto Commerce. | Any admin UI. | Platform-wide configuration. |
| Navigation. | Blade stack, deep linking, messaging. | Routes + dialogs. | Blade stack (AngularJS, legacy). |
| Platform glue. | Built-in OAuth, SignalR, permissions, API clients. | Bring your own. | In-process. |
| Customization unit. | Vue plugins as modules with extension points. | Vue components + routes. | AngularJS module patches. |
| Distribution. | Standalone or remote MF module. | Standalone. | In-process module. |
| Stack. | Vue 3, TypeScript, Vite, Tailwind. | Varies. | AngularJS 1.x. |

![Readmore](architecture-overview.md){: width="25"} See how the pieces fit together in the architecture overview.
