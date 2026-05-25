# Architecture

A VC-Shell app is a Vue 3 application made of two halves: the **shell** the framework gives you, and the **modules** you write. The shell renders the chrome (sidebar, top bar, blade stack, login, dashboard) and handles cross-cutting concerns (auth, i18n, permissions, notifications). Modules contribute the domain: blades, composables, locale bundles, dashboard widgets, extension contributions.

Your code never redraws the chrome and rarely touches the cross-cutting plumbing. You write modules, install them, and the framework composes the running application around them.

## Platform boundary

VC-Shell owns the back-office user experience. The Virto Commerce Platform owns business data, persistence, jobs, roles, permissions, OAuth, REST APIs, and SignalR events.

Application code talks to the Platform through generated TypeScript clients via `useApiClient(ClientCtor)`. Authentication flows through the browser session cookie that the Platform sets at sign-in; you do not attach tokens or build auth headers yourself.

Do not treat client-side permissions as a security boundary. Blade and menu permissions keep the UI predictable, while the Platform must enforce the same permissions and tenant or account scope on the server.

## Runtime composition

A scaffolded app starts by installing the framework plugin with a Vue Router instance. The framework brings up the shell, the language service, the permission cache, the notification pipeline, the blade navigation system, and the API client factory in one step. Application modules are then installed with `app.use(module)`. Each module contributes blade components, locale messages, notification type mappings, dashboard widgets, and extension-point registrations. The shell composes these contributions at runtime.

You can mix bundled modules (in `src/modules/`, installed at build time) with remote modules loaded at runtime through Module Federation. Both kinds use the same `defineAppModule` shape and the same extension points; the only difference is when they reach the host. See [Module Federation](module-federation.md) for the runtime-loaded case.

## Blade model

The user-visible primitive is the blade: a vertical panel pushed onto a stack. A blade declares routing, menu, and permissions through `defineBlade`. Modules ship blades, register them through `defineAppModule({ blades })`, and the framework wires routing, menu, permission gating, and URL synchronization around them.

For the full mental model see [Blade navigation](blade-navigation.md).

## Related

- [Modules.](modules.md)
- [Blade navigation.](blade-navigation.md)
- [Module Federation.](module-federation.md)
