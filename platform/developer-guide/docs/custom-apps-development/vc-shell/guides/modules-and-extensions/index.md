# Modules and Extensions

Recipes for packaging a VC-Shell feature as a redistributable unit: declaring framework compatibility, exposing an extension point so other modules can plug into your UI, and shipping the bundle through Module Federation. Each recipe maps to the same `defineAppModule` contract the host uses to install local code.

## Prerequisites

Before packaging a module, make sure you have:

- A working VC-Shell module built with `defineAppModule`. See [Modules](../../concepts/modules.md).
- A grasp of the host loader and the extension points runtime. See [Modularity plugin](../../plugins/modularity.md) and [Extension Points plugin](../../plugins/extension-points.md).
- The `@vc-shell/create-vc-app` CLI available through `npx`.

## Recipe: package a module for npm distribution

A distributable module is a plain npm package whose entry point exports the Vue plugin returned by `defineAppModule`. The framework, Vue, and Vue Router live as peer dependencies so the host owns the runtime singletons. List blade components, locales, notification configs in the module's own files, do not duplicate `@vc-shell/framework` source.

```json title="package.json"
{
  "name": "@acme/vc-shell-reviews",
  "version": "1.2.0",
  "type": "module",
  "main": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "files": ["dist"],
  "peerDependencies": {
    "@vc-shell/framework": "^2.0.0",
    "vue": "^3.4.0",
    "vue-router": "^4.0.0 || ^5.0.0"
  }
}
```

```typescript title="src/index.ts"
import { defineAppModule } from "@vc-shell/framework";
import * as blades from "./pages";
import en from "./locales/en.json";

export default defineAppModule({
  blades,
  locales: { en },
});
```

The host installs the package with `app.use(reviewsModule)` after `npm install @acme/vc-shell-reviews`. Peer dependencies prevent duplicate copies of Vue and the framework, which would otherwise break provide/inject DI across module boundaries.

![Readmore](../../concepts/modules.md){: width="25"} Module shape and lifecycle.

## Recipe: declare framework compatibility

Remote modules advertise the framework versions they tolerate through a `compatibleWith.dependencies` block on their registry entry. The host reads this at startup, runs a semver check against the running `@vc-shell/framework` version, and skips entries that do not satisfy the range. Modules without a `compatibleWith` block load unconditionally.

```json title="Registry response from POST /api/frontend-modules"
{
  "modules": [
    {
      "id": "reviews",
      "entry": "https://cdn.example.com/reviews/remoteEntry.js",
      "version": "1.2.0",
      "compatibleWith": {
        "dependencies": {
          "@vc-shell/framework": ">=2.0.0 <3.0.0"
        }
      }
    }
  ]
}
```

NuGet-style ranges (`[2.0.0,3.0.0)`) are accepted; the host converts them to semver internally before calling `semver.satisfies`. Failed checks log a console warning naming the module, the required range, and the running framework version, then the host moves on.

## Recipe: expose an extension point in your module

To let other modules inject UI into your blade, mount an `<ExtensionPoint name="...">` slot where you want their components to land. Plugin modules register components against the same name through `useExtensionPoint(...).add({ id, component })`. Names are plain strings; pick one that scopes the location, for example `reviews:details-actions`.

```vue title="pages/review-details.vue"
<template>
  <VcBlade :title="$t('REVIEWS.DETAILS.TITLE')">
    <VcForm><!-- main fields --></VcForm>

    <ExtensionPoint
      v-if="review?.id"
      name="reviews:details-actions"
      separator
      gap="1rem"
    />
  </VcBlade>
</template>

<script setup lang="ts">
import { ExtensionPoint } from "@vc-shell/framework";
</script>
```

A consumer module registers a button into that slot at install time:

```typescript title="consumer module index.ts"
import { defineAppModule, useExtensionPoint } from "@vc-shell/framework";
import ModerateButton from "./components/ModerateButton.vue";

const { add } = useExtensionPoint("reviews:details-actions");
add({ id: "moderation:review-action", component: ModerateButton, priority: 10 });

export default defineAppModule({ locales: { en: {} } });
```

Order does not matter. The reactive store accepts `add` calls before the host declares the point and resolves them when the host blade mounts. Use globally unique `id` values; a second `add` with the same `id` replaces the entry.

![Readmore](../../concepts/extensions.md){: width="25"} Extension points and metadata filters.

## Recipe: ship a remote Module Federation bundle

Generate a dynamic-module project with the scaffolder, build it into a `remoteEntry.js`, and serve it from any static host. The host application discovers the bundle by calling `POST /api/frontend-modules` at startup; the Platform returns a registry that lists each module's entry URL, version, and compatibility block.

```bash title="Scaffold a dynamic module"
npx @vc-shell/create-vc-app reviews --type dynamic-module --module-name "Reviews"
```

The generated **vite.config.mts** delegates to `@vc-shell/mf-module`, which wires the Module Federation plugin with the canonical `REMOTE_SHARED` deps list (Vue, Vue Router, vue-i18n, vee-validate, lodash-es, `@vueuse/core`, and every `@vc-shell/framework` subpath). All shared deps are marked `import: false` so the remote does not bundle fallback chunks; the host provides the singletons at runtime.

```typescript title="vite.config.mts"
import { getDynamicModuleConfiguration } from "@vc-shell/mf-module";

export default getDynamicModuleConfiguration({
  compatibility: { framework: "^2.0.0" },
});
```

```typescript title="src/modules/index.ts"
import { defineAppModule } from "@vc-shell/framework";
import * as blades from "./pages";
import * as locales from "./locales";

export default defineAppModule({ blades, locales });
```

Run `npm run build`. The output is written to **dist/mf/remoteEntry.js** with a base URL of `/apps/<package-name>/`. Upload the **dist/mf** folder to a CDN or static origin, then register an entry on the Platform so the registry endpoint returns it for the target app. On the next reload, `registerRemoteModules` fetches the registry, filters by compatibility, initializes the Module Federation runtime, and calls `app.use(plugin)` on every resolved module's default export. The blades, locales, and notification configs land in the same registries as locally-installed modules.

![Readmore](../../plugins/modularity.md){: width="25"} Modularity plugin reference, including the full loading sequence.

![Readmore](../../introduction/architecture-overview.md){: width="25"} Where mf-host and mf-module sit in the runtime.

## Variations

| Variation | Approach |
| --- | --- |
| App-local module (one repo). | `src/modules/<name>/` inside the host app, bundled at build time, no separate package. |
| npm-distributed module. | Standalone package, install via npm, host calls `app.use(module)` after import. |
| Module Federation remote. | Dynamic module project, served as `remoteEntry.js`, loaded at runtime by `registerRemoteModules`. |
| Private monorepo module. | Workspace package linked through pnpm or yarn workspaces, consumed as if published. |

![Readmore](../../plugins/extension-points.md){: width="25"} Extension points plugin reference.
