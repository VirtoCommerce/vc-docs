# create-vc-app

The scaffolding CLI for VC-Shell applications and modules. It generates a runnable project from templates: standalone apps that bundle their own modules and dynamic modules that host apps load through Module Federation.

The CLI is published as **@vc-shell/create-vc-app** and is normally invoked through `npx` so each run uses the latest published version.

## Synopsis

```bash
npx @vc-shell/create-vc-app [project-name] [options]
npx @vc-shell/create-vc-app add-module <module-name>
```

Without flags, the CLI runs interactively and prompts for every required value. Pass the flags below to skip prompts.

## Project types

| Type | Output | Use case |
| --- | --- | --- |
| `standalone`. | Full Vue 3 app with router, bootstrap, sample module, and Vite config. | An application that ships and runs on its own. |
| `dynamic-module`. | Module Federation remote that emits `remoteEntry.js`. | A module loaded at runtime by a host VC-Shell app. |

## Options

| Option | Purpose | Default |
| --- | --- | --- |
| `--type <type>`. | Project type. `standalone` or `dynamic-module`. | Prompted. |
| `--name`, `--app-name`. | Application title surfaced in the UI. | Directory name. |
| `--package-name`. | npm package name written to **package.json**. Validated against npm naming rules. | Application name, sanitized. |
| `--module-name`. | Initial module name for the generated `src/modules/` folder. For `standalone`, generating an initial module is opt-in: omit the flag and the project ships with no module. For `dynamic-module`, the module is always generated. | None (standalone), prompted (dynamic-module). |
| `--base-path`. | Base path used by Vite and the router. | `/apps/<name>/`. |
| `--tenant-routes`. | Generate routes with a UUID-shaped `:tenantId` prefix. | `false`. |
| `--ai-agent`. | Include AI Agent plugin configuration scaffold. | `false`. |
| `--dashboard`. | Include the Dashboard page and a sample widget registration. | `false`. |
| `--mocks`. | Include a sample module with mock data for local exploration. | `false`. |
| `--overwrite`. | Overwrite existing files without prompting. | `false`. |
| `--help`, `-h`. | Show CLI help. | — |
| `--version`, `-v`. | Show CLI version. | — |

## Non-interactive examples

```bash title="Standalone app with dashboard and sample data"
npx @vc-shell/create-vc-app my-app \
  --type standalone \
  --module-name "Products" \
  --dashboard \
  --mocks
```

```bash title="Dynamic Module Federation remote"
npx @vc-shell/create-vc-app my-module \
  --type dynamic-module \
  --module-name "Reviews"
```

## After scaffold

```bash
cd <project-name>
yarn install
yarn serve
```

The generated `package.json` includes scripts for `serve`, `build`, `build:app`, `build:types`, `lint`, `type-check`, and `generate-api-client`. The last one is wired to **@vc-shell/api-client-generator**, see [API Client Generator](api-client-generator.md).

## Add a module

From an existing app's root:

```bash
npx @vc-shell/create-vc-app add-module <module-name>
```

The subcommand:

1. Creates `src/modules/<module-name>/` with `pages/list.vue`, `pages/details.vue`, `composables/`, `locales/`, and `index.ts`.
2. Imports the module in `src/main.ts` and calls `app.use(<module>)`.
3. Registers a default menu entry in `src/bootstrap.ts`.

If the CLI cannot parse `src/main.ts` or `src/bootstrap.ts` (custom formatting, unsupported syntax), it prints manual integration instructions instead of writing.

## Related

- [Manual CLI start.](../../getting-started/manual-cli-start.md)
- [Generate an app from a prompt.](../../getting-started/generate-app-from-prompt.md)
- [API Client Generator.](api-client-generator.md)
