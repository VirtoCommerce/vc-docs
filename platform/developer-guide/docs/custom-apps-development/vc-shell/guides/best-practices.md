# Best Practices

Architectural principles for building scalable, maintainable VC-Shell applications.

## Prerequisites

Before applying these practices, make sure you have:

- An app scaffolded and a module under your belt.
- Familiarity with the project layout (see [Project structure](../getting-started/project-structure.md)).

## Principles

VC-Shell apps follow a few overarching principles. Treat them as defaults, not absolutes. When a principle bites, make a deliberate decision and document why.

| Principle | What it means |
| --- | --- |
| **High cohesion**. | Related code lives together. A blade, its composable, its types, and its locale strings sit in the same module folder. |
| **Low coupling**. | Modules keep internals private. Cross-module UI wiring runs through extension points or the menu service; shared composables are imported only when they are intentionally exposed as a module contract. |
| **Colocation**. | Files that change together live together. Resist organizing strictly by technical layer (`all-types/`, `all-composables/`) at the app level. |
| **Convention over configuration**. | Follow the scaffolder's layout. Diverging adds onboarding cost; reverting later costs more. |
| **Verify, don't assume**. | Before reusing or refactoring, read the source. APIs evolve. |

## AI-generated work

Use `/vc-app design` and `/vc-app generate` to get to a working module quickly, then treat the result as production code you own. The generated scaffold gives you the framework shape; your job is to verify contracts, replace mocks, and make the business behavior explicit.

- **Keep the generated boundaries**. Preserve module-local pages, composables, locales, and API wiring unless there is a concrete reason to move them.
- **Promote prototypes deliberately**. Use `/vc-app promote <module>` when a mock-backed module is ready for a Platform API. Do not mix mock arrays and real API calls in the same composable after promotion.
- **Review generated permissions and routes**. AI can infer intent, but final route names, menu labels, and permission codes are product decisions.
- **Type-check before manual cleanup**. Run the app and type-check the generated module before broad refactoring; otherwise it is hard to tell whether a failure came from generation or cleanup.
- **Document deviations inside the module**. If a module intentionally breaks the scaffold convention, leave a short README or code comment near the decision.

## Code organization

The full layout reference lives in [Project structure](../getting-started/project-structure.md). The principles below apply on top.

### App-level rules

A few rules keep the app shell lean and prevent it from absorbing module-specific logic.

- **Reach for `src/composables/` only when the composable is used by 2+ modules**, or holds genuinely app-wide state (current tenant, feature flags, shopping cart). A composable used by one module belongs in that module.
- **`src/services/` is optional**. Create it only when you have a non-Vue class that wraps an external SDK or third-party service. Plain functions belong in `src/utils/`.
- **`src/components/` is rare**. App-wide UI usually comes from `@vc-shell/framework`. Hand-rolled shared components signal that the framework is missing something. Flag it as an extension point candidate before forking.

### Module-level rules

Modules are the unit of feature ownership. They should be self-contained and replaceable.

- **Every blade has a composable**. The blade is the template plus chrome glue; the composable holds state, API calls, and business logic. The split keeps blades testable and replaceable.
- **Module locales prefix their keys with the module name**. `ORDERS.PAGES.LIST.TITLE`, never `PAGES.LIST.TITLE`.
- **Blade names are global identifiers**. Prefix with the module: `OrdersList`, `OrderDetails`, not `List` or `Details`. Module name plus entity plus role.

## Naming

Consistent names make the codebase searchable and the module boundaries obvious.

| Kind | Pattern | Example |
| --- | --- | --- |
| Blade name | `<Module><Entity><Role>` | `OrdersList`, `OrderDetails`, `OrderShipmentDetails` |
| Composable | `use<Subject>` | `useOrdersList`, `useOrderDetails` |
| Locale key | `MODULE.SECTION.SUBSECTION.KEY` | `ORDERS.PAGES.LIST.TABLE.HEADER.STATUS` |
| Permission | `<domain>:<entity>:<verb>` | `orders:order:view`, `catalog:product:edit` |
| Extension point id | `<owning-module>:<slot>` | `account:pricing-adjustments`, `order:line-items` |

## Styling strategy

VC-Shell ships a CSS-variable theme system layered with Tailwind utilities. Stay inside that system.

- **CSS custom properties first**. Override framework variables (`--primary-500`, `--font-family`) in **src/styles/custom.scss**, not by overwriting framework SCSS files.
- **Tailwind utilities for layout**. Use `tw-` prefixed utilities for spacing, flex, and grid. Reach for SCSS only when a computed property or a complex selector is required.
- **Don't fork Vc-components**. Wrap them. A `MyCard` that wraps `VcCard` with app-specific defaults is cheaper than a forked `VcCard` to maintain.

- [Theming and the UI layer.](ui/index.md)

## TypeScript

Strict typing pays compounding interest in a multi-module app.

- **Strict mode is on by default**. Keep it on. Type errors at build time are cheaper than runtime errors.
- **Type generated API client responses**. They come typed from `@vc-shell/api-client-generator`. Use the generated `Customer`, `CustomerOrder`, and other classes directly; do not redeclare them.
- **Module-local types** in **src/modules/&lt;module&gt;/types/**. App-wide types in **src/types/**. Do not declare ambient types unless you genuinely augment third-party libraries.

## Composables and state

The framework's pattern is composables-as-state. Reach for a heavier store only when you can name the feature it unlocks.

- **Local state in components** (`ref`, `reactive`) until two components need it.
- **Composable state for module-scoped concerns**. `useOrdersList` holds the list of loaded orders, the current page, and the sort.
- **App-wide state in `src/composables/` shared composables**. Use VueUse's `createSharedComposable` pattern, applied by the framework's own `useUser`.
- **Pinia is not used by default**. Add Pinia only if you have a justified need for cross-module store features such as devtools, time travel, or hydration.

## Performance

Module federation handles most of the heavy lifting; a few habits keep the rest in check.

- **Lazy-load remote modules**. The MF host loads modules in parallel at startup; you do not write the lazy loader.
- **Lazy-load module routes when bundle size matters**. Vue Router's `() => import(...)` pattern works as expected.
- **Skip persistent state on data tables you do not need to remember**. The `state-key` prop adds localStorage writes; omit it when the table is transient.

## Testing

Test the layer that holds the logic, not the layer that paints it.

- **Test composables, not blades**. Composables hold the logic; blades are mostly template glue.
- **Hit a real test database when integration testing the API client**. Mock-only tests miss schema mismatches.
- **Smoke-test the dev server before merging**. Run `yarn build` plus `yarn preview` to cover production assets.

## Common anti-patterns

A few patterns reliably bite later. Catch them in review.

!!! warning "Cross-module imports"
    Module A reaching into **src/modules/B/composables/internalThing** is a smell. Move app-wide utilities to **src/composables/**, expose UI composition through an extension point, or export a stable composable from module B's **index.ts** and treat it as a public frontend contract.

!!! warning "Hand-rolled fetch in modules"
    All Platform calls go through `useApiClient`. The framework's fetch wrapper still applies its timeout, offline check, and 401-redirect to any same-origin `/api/*` request — including a bare `fetch("/api/...")` — so the operational guards survive. What you lose with a bare fetch is the generated client's typed request and response signatures and the unified `useAsync` error handling that blade banners rely on.

!!! warning "Blade names without a module prefix"
    `BladeRegistry` is a flat global namespace. Registering two blades under the same name throws at module install time. Prefix every name with the module domain (`OrdersList`, not `List`).

!!! warning "Modifying generated code under src/api_client/"
    Rerunning `yarn generate-api-client` discards every hand-edit. Wrap or extend in your own composable instead.

- [Module mechanics.](../concepts/modules.md)

- [Distributing modules.](modules-and-extensions/index.md)
