# Modules and Extensions

Recipes for packaging VC-Shell features: declaring framework compatibility, exposing an extension point so other modules can plug into your UI, and shipping external extensions through Module Federation. Local application modules stay under `src/modules/`; Module Federation is for modules that are built and deployed outside the app.

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
import { defineAppModule, registerDashboardWidget } from "@vc-shell/framework";
import { markRaw } from "vue";
import * as pages from "./pages";
import * as locales from "./locales";
import ReviewCreatedTemplate from "./notifications/ReviewCreatedDomainEvent.vue";
import ReviewsDashboardCard from "./components/ReviewsDashboardCard.vue";

registerDashboardWidget({
  id: "reviews-widget",
  name: "Reviews",
  component: markRaw(ReviewsDashboardCard),
  size: { width: 6, height: 6 },
});

export default defineAppModule({
  blades: pages,
  locales,
  notifications: {
    ReviewCreatedDomainEvent: {
      template: ReviewCreatedTemplate,
      toast: { mode: "auto" },
    },
  },
});

export * from "./pages";
export * from "./composables";
```

A real module's **index.ts** does four things in this order: register dashboard widgets at module load, return `defineAppModule({...})` as the default export with blades, locales, and notification handlers, then re-export pages and composables so other modules can import them as a public contract. The barrel re-exports are essential — without them, consumer modules have no clean import path and end up reaching into private folders.

The host installs the package with `app.use(reviewsModule)` after `npm install @acme/vc-shell-reviews`. Peer dependencies prevent duplicate copies of Vue and the framework, which would otherwise break provide/inject DI across module boundaries.

- [Module shape and lifecycle.](../../concepts/modules.md)

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
import { ExtensionPoint } from "@vc-shell/framework/extensions";
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

- [Extension points and metadata filters.](../../concepts/extensions.md)

## Recipe: ship a Module Federation plugin remote

A plugin remote ships as a Vue subpackage inside a .NET module and attaches to a host app at runtime. The plugin's vite config writes its bundle to `<moduleRoot>/plugins/<appId>/remoteEntry.js`; the .NET module's `.csproj` ships the `plugins/` folder inside the module zip; the Platform's `AppManifestService` discovers the file and surfaces it through `GET /api/apps/{appId}/manifest`. The host loads it on next boot.

The minimum a plugin author writes:

```ts title="src/modules/vite.config.with-api.mts"
import { fileURLToPath } from "node:url";
import path from "node:path";
import { getDynamicModuleConfiguration } from "@vc-shell/mf-module";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const moduleRoot = path.resolve(__dirname, "../../..");

export default getDynamicModuleConfiguration({
  entry: "./src/modules/index.ts",
  appId: "vendor-portal",                // host app this plugin attaches to
  moduleRoot,                            // .NET module root
  remoteName: "VirtoCommerce.MyModule",  // matches PluginEntry.remote.name
});
```

```ts title="src/modules/index.ts"
import type { App } from "vue";
import type { Router } from "vue-router";
import routes from "./routes";

export default {
  install(app: App, { router }: { router: Router }) {
    routes.forEach((route) => router.addRoute(route));
  },
};
```

Add a build step that produces the bundle:

```json title="package.json"
{
  "scripts": {
    "build:modules-bundle": "vite build --config ./src/modules/vite.config.with-api.mts"
  }
}
```

The full author + host walkthrough (manifest endpoint shape, federation name alignment, shared-deps catalogue, troubleshooting) lives in the [Module Federation guide](../module-federation/index.md).

- [Module Federation guide.](../module-federation/index.md)
- [Module Federation concept.](../../concepts/module-federation.md)
- [Modularity plugin reference, including the full loading sequence.](../../plugins/modularity.md)

## Recipe: a module that exposes only composables

Not every module ships blades. A module can be purely a domain layer that wraps an API client and re-exports composables for other modules to consume. There is no `defineAppModule` call — the module is a plain barrel file, installed through normal imports, with no entry in `main.ts`.

Use this shape for cross-cutting capabilities that several feature modules need but that have no UI of their own: a workflow engine wrapper, a tax calculator, a recommendations client, anything that is logic plus types and zero pages.

```ts title="src/modules/workflow/composables/useWorkflow.ts"
import { ref, type Ref } from "vue";
import { useApiClient, useAsync } from "@vc-shell/framework";
import { WorkflowClient, type WorkflowState } from "../../../api_client/workflow";

export interface IUseWorkflow {
  state: Ref<WorkflowState | undefined>;
  loading: Ref<boolean>;
  loadState: (entityId: string) => Promise<void>;
  transition: (entityId: string, command: string) => Promise<void>;
}

export function useWorkflow(): IUseWorkflow {
  const { getApiClient } = useApiClient(WorkflowClient);
  const state = ref<WorkflowState>();

  const { action: loadState, loading } = useAsync<string>(async (id) => {
    const client = await getApiClient();
    state.value = await client.getState({ entityId: id });
  });

  const { action: transition } = useAsync<{ entityId: string; command: string }>(
    async ({ entityId, command }) => {
      const client = await getApiClient();
      await client.execute({ entityId, command });
      await loadState(entityId);
    },
  );

  return { state, loading, loadState, transition: (id, cmd) => transition({ entityId: id, command: cmd }) };
}
```

```ts title="src/modules/workflow/index.ts"
export { useWorkflow, type IUseWorkflow } from "./composables/useWorkflow";
export type { WorkflowState } from "../../api_client/workflow";
```

Feature modules consume it like any other composable:

```ts title="src/modules/orders/composables/useOrderState.ts"
import { useWorkflow } from "../../workflow";

export function useOrderState(orderId: string) {
  const wf = useWorkflow();
  wf.loadState(orderId);
  return wf;
}
```

Nothing changes in **main.ts**: there is no `app.use(workflow)` call because there is no Vue plugin to install. The module's only job is to publish a stable composable surface that other modules import against. Treat the module's **index.ts** as the public contract and keep API client imports inside the module, so consumers do not reach into `api_client/` directly.

## Variations

| Variation | Approach |
| --- | --- |
| App-local module (one repo). | `src/modules/<name>/` inside the host app, bundled at build time, no separate package. |
| npm-distributed module. | Standalone package, install via npm, host calls `app.use(module)` after import. |
| Module Federation remote. | Dynamic module project, served as `remoteEntry.js`, loaded at runtime by `registerRemoteModules`. |
| Private monorepo module. | Workspace package linked through pnpm or yarn workspaces, consumed as if published. |
| Composables-only module. | No `defineAppModule`, no `app.use(...)`. Just a barrel file exporting composables and types from `src/modules/<name>/index.ts`. |

- [Extension points plugin reference.](../../plugins/extension-points.md)
