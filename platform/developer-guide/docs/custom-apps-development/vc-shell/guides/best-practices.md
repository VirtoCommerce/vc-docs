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
| **Low coupling**. | Modules do not import from each other. Cross-module wiring runs through extension points or the menu service. |
| **Colocation**. | Files that change together live together. Resist organizing strictly by technical layer (`all-types/`, `all-composables/`) at the app level. |
| **Convention over configuration**. | Follow the scaffolder's layout. Diverging adds onboarding cost; reverting later costs more. |
| **Verify, don't assume**. | Before reusing or refactoring, read the source. APIs evolve. |

## Code organization

The full layout reference lives in [Project structure](../getting-started/project-structure.md). The principles below apply on top.

### App-level rules

A few rules keep the app shell lean and prevent it from absorbing module-specific logic.

- **Reach for `src/composables/` only when the composable is used by 2+ modules**, or holds genuinely app-wide state (current tenant, feature flags, global search). A composable used by one module belongs in that module.
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
| Permission | `<domain>:<entity>:<verb>` | `seller:orders:view`, `catalog:product:edit` |
| Extension point id | `<owning-module>:<slot>` | `seller:commissions`, `order:line-items` |

## Styling strategy

VC-Shell ships a CSS-variable theme system layered with Tailwind utilities. Stay inside that system.

- **CSS custom properties first**. Override framework variables (`--primary-500`, `--font-family`) in **src/styles/custom.scss**, not by overwriting framework SCSS files.
- **Tailwind utilities for layout**. Use `tw-` prefixed utilities for spacing, flex, and grid. Reach for SCSS only when a computed property or a complex selector is required.
- **Don't fork Vc-components**. Wrap them. A `MyCard` that wraps `VcCard` with app-specific defaults is cheaper than a forked `VcCard` to maintain.

![Readmore](ui/index.md){: width="25"} Theming and the UI layer.

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
    Module A importing from **src/modules/B/** is a smell. Move the shared piece to **src/composables/** or expose an extension point in B that A consumes.

!!! warning "Hand-rolled fetch in modules"
    All Platform calls go through `useApiClient`. A bare `fetch("/api/...")` skips the framework's auth interceptor and breaks token refresh.

!!! warning "Blade names without a module prefix"
    `BladeRegistry` is a flat global namespace. Two modules registering `Details` collide; the second overwrites the first.

!!! warning "Modifying generated code under src/api_client/"
    Rerunning `yarn generate:api-client` discards every hand-edit. Wrap or extend in your own composable instead.

![Readmore](../concepts/modules.md){: width="25"} Module mechanics.

![Readmore](modules-and-extensions/index.md){: width="25"} Distributing modules.
