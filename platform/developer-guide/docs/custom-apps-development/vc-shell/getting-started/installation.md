# Installation

Scaffold a VC-Shell app, install dependencies, point it at a Virto Commerce Platform, and launch the dev server.

## Prerequisites

Before installing VC-Shell, make sure you have:

- **Node.js** 22 or higher (`node --version`).
- **Corepack** enabled: `corepack enable`.
- **Yarn 4** (pinned by the scaffolder once Corepack is on).
- A reachable Virto Commerce Platform instance, if you plan to connect to real data right away.

## Scaffold

Run the interactive scaffolder to generate a new VC-Shell project. The wizard prompts for app type, primary module name, and optional flags such as a Dashboard page and sample mocks.

```bash
npx @vc-shell/create-vc-app my-app
```

For CI or repeatable setups, skip the prompts and pass flags directly:

```bash
# Standalone app with Dashboard + sample data
npx @vc-shell/create-vc-app my-app \
  --type standalone --module-name "Products" --dashboard --mocks

# Dynamic module for an MF host
npx @vc-shell/create-vc-app my-module \
  --type dynamic-module --module-name "Reviews"
```

Full flag reference: [create-vc-app README](https://github.com/VirtoCommerce/vc-shell/blob/main/cli/create-vc-app/README.md).

## Install dependencies

The scaffolder does not install for you. Enter the new project and pull packages with Yarn 4:

```bash
cd my-app
yarn install
```

## Configure the Platform URL

The scaffolder writes two env files: **.env** (committed defaults) and **.env.local** (your machine-local overrides, gitignored). Edit **.env.local** so the app talks to your Platform:

```bash title=".env.local"
APP_PLATFORM_URL=https://your-platform.example.com
```

Without `APP_PLATFORM_URL` the app still runs but cannot reach a backend. With `--mocks`, the sample module ships with in-memory data, so the UI renders even when no Platform is wired up.

## Run

Start the Vite dev server with hot module replacement:

```bash
yarn serve
```

The server opens at `http://localhost:8080`. Sign in with your Platform credentials to see live data, or browse the mock module if you scaffolded with `--mocks`.

## Troubleshooting

!!! warning "`Couldn't find package manager 'yarn'`"
    Run `corepack enable`, then re-run `yarn install`.

!!! warning "`Port 8080 is already in use`"
    `yarn serve --port 8081`.

!!! warning "Blank screen, 401 errors in the network tab"
    `APP_PLATFORM_URL` is wrong or the Platform's OAuth client is not configured for this app. See [Connecting to the Platform](connecting-to-platform.md).

!!! warning "`Vue has already been registered`"
    Two Vue copies are loaded. Usually `portal:` linking without `preserveSymlinks`. See the [vc-shell README](https://github.com/VirtoCommerce/vc-shell/blob/main/README.md#local-development-via-portal-protocol).
