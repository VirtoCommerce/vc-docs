# Project Structure

This page maps the folders a scaffolded VC-Shell app gives you, so you know where to drop new code.

## Top level

```text
my-app/
├─ public/                       Static assets (logo, favicon, background).
├─ src/                          All application source.
├─ .env                          Committed defaults.
├─ .env.local                    Local secrets and overrides (gitignored).
├─ index.html                    Vite entry HTML.
├─ package.json                  Scripts and dependencies.
├─ tailwind.config.ts            Tailwind preset extending the framework's.
├─ vite.config.mts               Vite config from @vc-shell/config-generator.
├─ tsconfig.json                 TypeScript with preserveSymlinks ready.
└─ yarn.lock                     Locked dependency graph.
```

The `@vc-shell/*` packages are consumed from npm. You do not edit them; you compose against the public API.

## src/

```text
src/
├─ main.ts                       Installs the framework plugin and modules.
├─ bootstrap.ts                  Side effects (menu items, dashboard widgets).
├─ env.d.ts                      Vite env typings.
├─ api_client/                   Generated TypeScript API clients (yarn generate:api-client).
├─ components/                   App-scoped Vue components reused across modules.
├─ composables/                  App-scoped composables. Re-exported via composables/index.ts.
├─ config/                       App extras (push-hub config).
├─ locales/                      App-wide translations.
├─ modules/                      Domain modules. One subdir per module.
├─ pages/                        App-level pages (App.vue, Dashboard.vue).
├─ router/                       Vue Router setup.
├─ styles/                       Tailwind entry (index.scss) + custom SCSS.
└─ types/                        Ambient TypeScript declarations.
```

## Inside a module

```text
src/modules/orders/
├─ index.ts                      defineAppModule({ blades, locales }).
├─ pages/                        Blade components.
│  ├─ list.vue                   Workspace blade with VcDataTable.
│  ├─ details.vue                Child blade with the form.
│  └─ index.ts                   Re-exports the blade components.
├─ composables/                  Module-scoped composables.
├─ components/                   Module-scoped Vue components.
├─ locales/                      Translation bundles for this module.
└─ sample-data/                  Present only when scaffolded with --mocks.
```

```ts title="src/modules/orders/index.ts"
import * as blades from "./pages";
import * as locales from "./locales";
import { defineAppModule } from "@vc-shell/framework";

export default defineAppModule({ blades, locales });

export * from "./pages";
export * from "./composables";
```

![Readmore](../concepts/modules.md){: width="25"} Modules in depth.

## Where things go

| You want to add | Put it in |
| --- | --- |
| A new blade in an existing module. | `src/modules/<module>/pages/<MyBlade>.vue`, re-export from `pages/index.ts`. |
| A new module. | `npx @vc-shell/create-vc-app add-module <module>`. |
| A shared composable used by multiple modules. | `src/composables/`, exported through `composables/index.ts`. |
| A shared Vue component used by multiple modules. | `src/components/`. |
| A module-private composable or component. | `src/modules/<module>/composables/` or `.../components/`. |
| A new API client for a Platform module. | Generated into `src/api_client/` by `yarn generate:api-client`. |
| A module-scoped translation key. | `src/modules/<module>/locales/<lang>.json`. |
| An app-wide translation key. | `src/locales/<lang>.json`. |
| A new menu item. | `menuItem` config of `defineBlade`, or `addMenuItem(...)` in `bootstrap.ts`. |
| A new dashboard widget. | A Vue component, registered via `registerDashboardWidget(...)` in `bootstrap.ts`. |
| A router-level page (outside the blade stack). | `src/pages/<Page>.vue` + a route in `src/router/`. |

## Conventions

- **Module isolation.** Modules do not import from other modules. Cross-module wiring goes through extension points, the menu service, or shared composables in `src/composables/`.
- **Locale namespacing.** Prefix module keys with the module name in uppercase (`SAMPLE_APP.PAGES.LIST.TITLE`).
- **Blade names are global.** `defineBlade({ name: "OrderDetails" })` is the lookup key in `BladeRegistry`. Use a `<Module><Subject>` shape (`OrdersList`, `OrderDetails`).
- **Generated code stays generated.** Do not hand-edit `src/api_client/`. Re-run `yarn generate:api-client` after a schema change.
- **Framework code is imported, not patched.** Customize through extension points, menu services, and overrides.

![Readmore](first-blade.md){: width="25"} Build your first blade.
