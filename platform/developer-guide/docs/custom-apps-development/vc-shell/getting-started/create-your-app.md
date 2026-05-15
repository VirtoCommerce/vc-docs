# Create Your App

Generate a VC-Shell project, understand what the scaffolder produces, and add modules to it as your app grows.

## Prerequisites

Before creating your app, make sure you have:

- **Node.js** 22 or higher.
- **Corepack** enabled, so the scaffolder can pin Yarn 4.
- A decision on project type: a Standalone App, or a Dynamic Module for a host shell.

## Run the scaffolder

Invoke the CLI in an empty parent directory. The wizard asks for project type, names, and optional features, then writes the project tree.

```bash
npx @vc-shell/create-vc-app my-app
```

Prompts (in order):

1. **Project type:** Standalone App or Dynamic Module.
2. **App name** (display name).
3. **Package name** (npm package id).
4. **Initial module name** (default: app name in title case).
5. **Optional features:** Dashboard with widgets, mock data, AI agent, tenant routes.

Skip the prompts by passing the equivalent flags. Full reference: [create-vc-app README](https://github.com/VirtoCommerce/vc-shell/blob/main/cli/create-vc-app/README.md#options).

## Scaffold with the vc-app AI skill

The `vc-app` AI skill installs slash commands into your AI coding tool that scaffold projects, connect to a Virto Commerce Platform, and generate full UI modules from plain-English intent. This is an alternative to running the CLI by hand. Pick the path that fits your workflow.

### Install

Pick the line that matches your AI tool. Restart the AI tool session after install to register the `/vc-app` commands.

```bash
# Claude Code / Cursor / GitHub Copilot
npx @vc-shell/vc-app-skill install

# OpenCode
npx @vc-shell/vc-app-skill install --runtime opencode

# Gemini CLI
npx @vc-shell/vc-app-skill install --runtime gemini

# Codex
npx @vc-shell/vc-app-skill install --runtime codex
```

### Slash commands

| Command | What it does |
| --- | --- |
| `/vc-app create` | Scaffold a new VC-Shell project interactively. |
| `/vc-app connect` | Wire **.env** and **.env.local** and generate typed API clients from a Platform instance. |
| `/vc-app add-module <name>` | Add a list and details module to an existing app. |
| `/vc-app generate` | Intent-driven module generation with mock or live data. |
| `/vc-app design` | Generate a multi-module app from a free-text product description. |
| `/vc-app promote <name>` | Promote a prototype module from mock data to real API clients. |
| `/vc-app migrate` | Migrate the app to the latest `@vc-shell/framework` version, running the CLI migrator and AI-assisted manual refactors. |

The skill follows VC-Shell conventions automatically: Vue 3 with `<script setup lang="ts">`, Tailwind with the `tw-` prefix, BEM class names, and the framework's blade and module patterns.

![Readmore](https://github.com/VirtoCommerce/vc-shell/blob/main/cli/vc-app-skill/README.md){: width="25"} Full vc-app skill README on GitHub.

## Generated layout

The scaffolder produces a Vite-driven Vue app, fully wired to the framework, ready for `yarn install` and `yarn serve`.

```text
my-app/
├─ .env                          Default env (locale, base path).
├─ .env.local                    Local overrides, including APP_PLATFORM_URL.
├─ index.html                    Vite entry HTML.
├─ package.json                  Scripts and dependencies.
├─ tailwind.config.ts            Tailwind preset, extends the framework's.
├─ vite.config.mts               Vite config from @vc-shell/config-generator.
├─ tsconfig.json                 preserveSymlinks ready.
├─ public/                       Static assets (logo, background, icons).
└─ src/
   ├─ main.ts                    Entry. Installs the framework plugin and modules.
   ├─ bootstrap.ts               Side effects (menu items, dashboard widgets).
   ├─ env.d.ts                   Vite env typings.
   ├─ api_client/                Generated API clients live here.
   ├─ composables/               App-scoped composables.
   ├─ locales/                   App-wide translations.
   ├─ pages/                     App-level pages: App.vue, Dashboard.vue.
   ├─ router/                    Vue Router configuration.
   ├─ styles/                    Tailwind entry + custom SCSS.
   └─ modules/                   Your domain modules.
```

With `--mocks`, you also get `src/modules/sample/`, a complete reference module with list and details blades backed by in-memory data.

![Readmore](project-structure.md){: width="25"} Project structure in detail.

## Entry point

Every VC-Shell app starts in `src/main.ts`. The file loads the current user, instantiates Vue, installs the framework plugin, registers modules, and mounts the app.

```ts title="src/main.ts"
import VirtoShellFramework, { useUser, useLanguages, notification } from "@vc-shell/framework";
import { createApp } from "vue";
import { RouterView } from "vue-router";
import { router } from "./router";
import * as locales from "./locales";
import Sample from "./modules/sample";
import { bootstrap } from "./bootstrap";
import "@vc-shell/framework/dist/index.css";

async function startApp() {
  const { loadUser } = useUser();
  try { await loadUser(); } catch (e) { console.log(e); }

  const app = createApp(RouterView);
  app.use(VirtoShellFramework, { router });
  app.use(Sample);
  app.use(router);

  bootstrap(app);
  Object.entries(locales).forEach(([k, m]) =>
    app.config.globalProperties.$mergeLocaleMessage(k, m));

  await router.isReady();
  app.mount("#app");
}

startApp();
```

The companion **bootstrap.ts** file is where menu items and dashboard widgets are registered. The scaffolder pre-fills it when you pick `--dashboard`.

## Add another module later

Run the same CLI from the project root with the `add-module` subcommand to extend an existing app.

```bash
npx @vc-shell/create-vc-app add-module orders
```

The command creates `src/modules/orders/` with list and details blades, patches **src/main.ts** to import and `app.use(...)` the new module, and patches **src/bootstrap.ts** to register its menu item. If either file cannot be parsed, the CLI prints manual instructions instead.

![Readmore](first-blade.md){: width="25"} Build your first blade.

## Troubleshooting

!!! warning "`npx` cannot find `@vc-shell/create-vc-app`"
    Clear the npx cache (`npx clear-npx-cache`) or upgrade npm. The scaffolder is published under the `@vc-shell` scope and requires npm 7 or higher.

!!! warning "`add-module` reports it could not patch `main.ts`"
    The CLI uses AST patching. If you have edited the entry file beyond recognition, add the import and `app.use(...)` line yourself, then register the menu item in **bootstrap.ts**.
