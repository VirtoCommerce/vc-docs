# Deployment

A VC-Shell app ships **with** a Virto Commerce Platform module, not next to it. The frontend bundle lives inside the module's `App/` folder; the .NET module's publish step copies the built assets into the Platform's `Modules/{moduleId}/App/dist/` directory, and the Platform sources them from there. There is no separate frontend host to maintain — wherever the Platform runs, the app runs.

This guide covers the **host app** delivery — the SPA users navigate to. Adding plugin extensions that attach to that host at runtime is a separate topic: see [Module Federation](module-federation/index.md).

## Prerequisites

Before deploying, make sure you have:

- A production-ready build pipeline that runs Node.js 22 or higher and Yarn 4.
- A `.csproj` for the .NET module that includes the App folder in its publish output.
- A Virto Commerce Platform instance the module deploys into.

## Production build

The scaffold ships a `build` script inside the `App/` folder that runs Vite in production mode and emits the application bundle plus TypeScript declaration files:

```bash
cd src/MyModule.Web/App
yarn build
```

Internally, this expands to `yarn build:app && yarn build:types`. The first step runs `cross-env APP_ENV=production vite build` and writes hashed, minified assets to **dist/**. The second step runs `vue-tsc --declaration --emitDeclarationOnly --outDir dist/types** and emits **.d.ts** files for downstream consumers.

To smoke-test the production bundle locally before shipping, run:

```bash
yarn preview
```

This starts a static server that mirrors how the Platform serves the assets and helps catch base-path or asset issues that only surface in production builds.

## Environments and configuration

Vite loads environment variables from **.env** files at build time. The scaffold ships **.env** with the public defaults and **.env.local** with a placeholder for the Platform URL, which stays out of version control:

```bash title=".env"
APP_BASE_PATH=/apps/my-app/
APP_I18N_LOCALE=en
APP_I18N_FALLBACK_LOCALE=en
```

```bash title=".env.local"
APP_PLATFORM_URL=https://your-platform-host
```

For per-mode overrides, add **.env.production**, **.env.staging**, or **.env.&lt;mode&gt;** alongside them.

Variables must be prefixed with `APP_` to be exposed to the client bundle. The framework configures Vite with `envPrefix: "APP_"`, so anything else is dropped at build time. `APP_BASE_PATH` matches the URL path the Platform serves the app from (typically `/apps/{appId}/`); `APP_PLATFORM_URL` is the Platform origin the bundle issues API calls against.

Because the values are baked into the bundle at build time, do not store secrets in **.env** files. Anything in the client bundle is visible to every user. Use the Platform's OAuth flow for credentialed access; pass runtime URLs through the build pipeline.

## Packaging the App folder into the .NET module

The module's `.csproj` copies `App/dist/**` into the publish output so the Platform finds the bundle alongside the assembly. The Import module's project file is a working reference:

```xml title="src/MyModule.Web/MyModule.Web.csproj"
<ItemGroup>
  <ImportApp Include="App\dist\**" />
</ItemGroup>

<Target Name="CopyCustomContentOnPublish" AfterTargets="Publish">
  <Copy SourceFiles="@(ImportApp)" DestinationFiles="$(PublishDir)\..\%(Identity)" />
</Target>

<ItemGroup>
  <Compile Remove="App\**" />
  <Content Remove="App\**" />
  <EmbeddedResource Remove="App\**" />
  <None Remove="App\**" />
</ItemGroup>
```

The two halves matter:

- The `CopyCustomContentOnPublish` target runs after `dotnet publish` and lifts the built assets next to the module assembly.
- The `Remove` items keep the `App/` source out of the .NET build — only the compiled `dist/**` ships.

When the Platform loads the module, it sources the bundle from `Modules/{moduleId}/App/dist/` and serves it under `APP_BASE_PATH`.

## Registering the app in the manifest

A single `<apps>` entry tells the Platform's app-hub to surface the app in the application grid. The same declaration is what the Platform's manifest endpoint uses to know which `appId` exists — without an `<app>` element, the host endpoint returns 404 and no plugins ever attach:

```xml title="module.manifest"
<apps>
  <app id="my-app">
    <title>My App</title>
    <iconUrl>/apps/my-app/img/icons/favicon-32x32.png</iconUrl>
    <contentPath>App/dist</contentPath>
    <permission>my-app:access</permission>
    <supportEmbeddedMode>true</supportEmbeddedMode>
  </app>
</apps>
```

- `contentPath` points at `App/dist` relative to the module root.
- `permission` gates the app behind a Platform permission. Users without it never see the app in the hub.
- `supportEmbeddedMode` (optional) opts the app in to running inside the AngularJS back office iframe — see the [embedded mode](#embedded-mode) section.

See [Register an App in the Module Manifest](../../how-to-register-new-app.md) for the full set of manifest options.

## Embedded mode

The same Vue bundle runs in two layouts. **Standalone** is the default — the app serves its own SPA at `APP_BASE_PATH`, with its own header, sidebar, and user dropdown. **Embedded** is opt-in: the Platform iframes the same app from a back-office menu entry, and the shell hides its outer chrome so the AngularJS host frame owns the navigation.

Add `<supportEmbeddedMode>true</supportEmbeddedMode>` inside the `<app>` element to opt in. There is no separate build, deploy target, or bundle — the framework detects the embedding context at runtime (via `EmbeddedMode=true` in the query string) and hides the standalone chrome. One artifact, two surfaces.

For details on what changes inside the app (which composables expose the embedding flag, how to vary behavior) see the [embedded-mode concept](../concepts/embedded-mode.md) and the [embedded-mode guide](platform/embedded-mode.md).

## CI/CD

A typical pipeline builds the frontend, then publishes the .NET module that wraps it. The scaffold ships `lint` and `type-check` as the verification commands:

```yaml title=".github/workflows/deploy.yml"
- run: cd src/MyModule.Web/App && yarn install --immutable
- run: cd src/MyModule.Web/App && yarn lint
- run: cd src/MyModule.Web/App && yarn type-check
- run: cd src/MyModule.Web/App && yarn build
- run: dotnet publish src/MyModule.Web/MyModule.Web.csproj -c Release
- run: <upload .nupkg or copy publish output to the Platform>
```

The frontend build must run **before** `dotnet publish`, because the publish target copies `App/dist/**` — an empty directory means an empty bundle in the published module.

## Common deployment mistakes

!!! warning "Wrong APP_BASE_PATH"
    `APP_BASE_PATH` must match the URL path the Platform serves the app from — usually `/apps/{appId}/`. A mismatch breaks asset URLs and HTML5 history routing. Verify the value in **.env.production** before running `yarn build`, and confirm the bundled **index.html** uses the expected paths.

!!! warning "Forgot to run yarn build before dotnet publish"
    The `.csproj` copies `App/dist/**`. If you publish the .NET module without rebuilding the frontend first, the Platform deploys a stale or empty bundle. Wire the order explicitly in CI.

!!! warning "Missing permission"
    The `<app>` element gates visibility behind `permission`. A new permission must exist in the Platform (registered via the module's `Module.cs` `ModuleConstants.Security.Permissions`) before users can be granted it. Without that, the app stays invisible no matter what the bundle does.

!!! warning "Forgot to set APP_ENV"
    `yarn build` sets `APP_ENV=production` through the scaffold script, but custom CI scripts may bypass it. Without production mode, Vite skips production-only optimizations and the bundle ships unoptimized.

!!! warning "Embedded mode flag missing"
    `<supportEmbeddedMode>true</supportEmbeddedMode>` is the only switch that lets the AngularJS back office iframe the app cleanly. Without it the app still loads in the iframe, but its full chrome (header, sidebar, user dropdown) renders on top of the host shell.

- [Register an App in the Module Manifest.](../../how-to-register-new-app.md)
- [Module Federation — adding plugin remotes to a host.](module-federation/index.md)
- [Embedded mode concept.](../concepts/embedded-mode.md)
- [Embedded mode guide.](platform/embedded-mode.md)
