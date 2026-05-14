# Troubleshooting

When something goes wrong, find the symptom you see and follow the diagnosis.

## Blade does not open or closes immediately

A blade that disappears the moment you click its menu entry, or never appears at all, almost always points to a thrown error during setup. The component never finishes mounting, so the framework unmounts it and the stack reverts to the previous blade.

Open the browser console first. The four common causes are: `useBlade()` invoked outside a blade context (for example, in a dashboard widget), a missing `defineBlade` macro on the component, a route guard that is rejecting the navigation silently, or a parent that closed itself in `onMounted` because of a thrown error. The console message names the failing function in every case.

![Readmore](../../concepts/blade-navigation.md){: width="25"} Blade lifecycle in depth.

## `useBlade()` methods throw "requires blade context"

`closeSelf`, `callParent`, `onBeforeClose`, and `setError` only work when called from a component that is mounted inside the blade stack. The framework reads the descriptor from Vue's dependency injection tree, and there is no descriptor outside a blade.

Calling these from a dashboard widget, a toolbar handler that lives outside the blade, a global pinia action, or a plain composable throws a descriptive runtime error. Only `openBlade` works everywhere; for everything else, move the call into the blade's `<script setup>`.

```typescript
// BAD -- thrown from a dashboard widget
const { closeSelf } = useBlade();
closeSelf(); // Error: closeSelf() requires blade context

// GOOD -- only openBlade works outside a blade
const { openBlade } = useBlade();
openBlade({ name: "OrderDetails", param: orderId });
```

## Storybook iframe does not load

The vc-shell Storybook embeds previews in iframes. A blank panel usually means the dev server is not running, third-party cookies are blocked for `localhost`, or a content security policy from a browser extension is rejecting the inline scripts.

Hard refresh first (Cmd-Shift-R / Ctrl-Shift-R). If the panel stays blank, open the iframe URL directly in a new tab and read the console. If you see mixed-content warnings, you are pointing the host page at `https://` while the iframe loads from `http://`; align the protocols.

## Hot reload does not pick up framework changes

When the app uses `portal:` to consume a local clone of `@vc-shell/framework`, Yarn symlinks the package directory directly. The symlink resolves to **dist/**, not to source, and Vite watches **dist/**.

Rebuild the framework, then restart the app dev server.

```bash
# In the vc-shell clone
yarn build:framework

# In the app
yarn serve
```

There is no watch mode for the framework build yet. If the app still does not pick up the change, clear stale artifacts with `yarn clean` in the vc-shell clone and rebuild.

## Build errors: peer version mismatch

`Vue has already been registered`, lost reactivity across blade boundaries, or a `vue-router` type clash on build all point to two copies of Vue or vue-router being loaded at runtime. The portal-linked framework brings its own **node_modules/**, and if the app pins a different version, both copies end up in the bundle.

Run `yarn why vue` in both repos. The reported versions must match. Bump the app's **package.json** to align with the framework's peer range, then `yarn install` and rebuild.

```bash
# Inside the app
yarn why vue
# Inside the vc-shell clone
yarn why vue
```

`preserveSymlinks: true` must also be set in both **vite.config.ts** and **tsconfig.json**; the scaffolder enables it, so an absent flag means a manually edited config.

## Build errors: circular deps and layer violations

When the framework's strict-checks pre-commit hook fires on a contribution, two scripts catch the most common architectural slips.

```bash
yarn check:circular   # madge over framework/
yarn check:layers     # enforces layer dependency direction
```

`check:circular` lists every cycle madge finds; `check:layers` reports any import that crosses a layer boundary in the wrong direction. Both must pass before the build is considered green.

## Auth: 401 on refresh

A 401 immediately after a token refresh means the refresh token itself was rejected. The two causes: the refresh token expired (default lifetime is 30 days, the user has been idle longer), or the OAuth client on the Platform was reconfigured and the previously issued tokens no longer match its scopes.

Sign out and sign in again. If the new sign-in still hits 401 on the first protected call, open the OAuth client config on the Platform and confirm the scopes cover the API endpoints the app calls.

![Readmore](../../getting-started/connecting-to-platform.md){: width="25"} Auth wiring in depth.

## CORS preflight rejected

The browser issues an `OPTIONS` preflight before any cross-origin request with custom headers. If the Platform does not respond with the matching `Access-Control-Allow-Origin` and `Access-Control-Allow-Headers`, the actual request never fires.

There are two fixes. The simpler one is to add `http://localhost:8080` (or whatever your dev server origin is) to the Platform's allowed origins list. The other is to configure a Vite dev proxy that forwards `/api` to the Platform; with that in place, the browser sees a same-origin request and CORS does not apply.

```ts title="vite.config.ts"
export default defineConfig({
  server: {
    proxy: {
      "/api": {
        target: "https://your-platform.example.com",
        changeOrigin: true,
      },
    },
  },
});
```

![Readmore](../../concepts/api-clients.md){: width="25"} API client patterns.

## VcDataTable state lost across reloads

`VcDataTable` persists column widths, sort, and pagination under the `state-key` you give it. If users complain that their table layout reset overnight, check whether someone bumped the key.

Bumping `state-key` is the intentional escape hatch after a schema change. Old, incompatible state is discarded, and users start from the new defaults. If the reset was accidental, restore the previous key. If the user cleared local storage from devtools, there is nothing to recover; the next interaction starts a fresh state under the same key.

## Locale key shows as raw string

When the UI renders `RESERVATIONS.LIST.TITLE` instead of "Reservations", the bundle never reached the global `vue-i18n` instance.

Check three things. First, confirm `locales` is passed to `defineAppModule({ blades, locales })` in the module entry. Second, confirm the locale file's top-level key (for example, `en`) matches `APP_I18N_LOCALE` in **.env**. Third, confirm every key in the bundle is namespaced under your module name; an unnamespaced `MENU.TITLE` collides with the first module that won the merge race.

```ts title="src/modules/reservations/index.ts"
import { defineAppModule } from "@vc-shell/framework";
import * as blades from "./pages";
import * as locales from "./locales";

export default defineAppModule({ blades, locales });
```

## Menu item missing

A blade with no sidebar entry is registered correctly but the menu service skipped it. The menu service requires both a `url` (so the entry has somewhere to navigate) and a `menuItem` (the title, icon, and priority).

```typescript
defineBlade({
  name: "ReservationsList",
  url: "/reservations",         // required for the menu entry
  isWorkspace: true,
  menuItem: {                   // also required
    title: "RESERVATIONS.MENU.TITLE",
    icon: "lucide-calendar-check",
    priority: 30,
  },
});
```

If you also see another module's blade silently replace yours, you collided on the global `BladeRegistry`. Blade names are global; prefix every name with the module domain (`ReservationsList`, not `List`).

![Readmore](../../getting-started/first-blade.md){: width="25"} Walk through a working module.

## Where else to look

A few source-side pages cover the same ground in more detail and stay closer to the framework's evolution:

- The framework's `useBlade` "Common Mistakes" section, for the full list of blade-context pitfalls (wrong `onBeforeClose` return value, deprecated `provideBladeData`, missing `.value` on identity refs).
- The modularity plugin "Common Mistakes" section, for module registration footguns (`defineOptions` missing on a blade, unwrapped `markRaw` on dashboard widget components, duplicate blade names, locale key collisions).
- The vc-shell README's `portal:` troubleshooting section, for the full list of local-linking issues (lost reactivity, stale **.tsbuildinfo**, lockfile conflicts).

If your symptom is not listed here or in the source-side pages, the [Connecting to the Platform](../../getting-started/connecting-to-platform.md) and [Installation](../../getting-started/installation.md) pages also carry inline `!!! warning` blocks for the most common setup failures.
