# Module Federation

Module Federation is how a VC-Shell host app loads **plugin extensions** it does not know about at build time. The host builds its own bundle as usual, ships, runs, and then asks the Platform "which plugins apply to this app right now?" The Platform returns a manifest of plugin remotes; the host fetches each, evaluates it as a Vue plugin, and installs it into the live app. The user sees new menu items, blades, dashboard widgets, and extension contributions appear without a host rebuild.

This is the framework's answer to the "plug-in shaped Platform module" need: a single host shell that absorbs frontend contributions from any .NET module that opts in, without the host having to know about them in advance.

## Host vs plugin remote

Two different roles share the same federation mechanism. Keep them distinct in your head:

- **Host app** — the standalone Vue SPA users navigate to. Vendor portal is a host. So is Commerce Manager (the Platform's built-in `appId="platform"`). A host owns its own .NET module wrapper that declares `<app id="...">` in **module.manifest**, builds with its own deployment pipeline, and calls `registerRemoteModules` at boot.
- **Plugin remote** — an extension that lives inside **another** .NET module and attaches to a host at runtime. A plugin builds a Module Federation remote (`remoteEntry.js`), ships inside its .NET module zip, and is discovered by the Platform via the dependency graph. From the user's perspective, the plugin's UI just appears inside the host.

The same .NET module can ship a host (`App/dist/`) **and** plugins (`plugins/<appId>/`). They are independent build outputs that serve independent roles.

## When you need it

You do not need Module Federation for everything. It introduces a network step on app boot and shifts some integration testing from build time to runtime. Use it when:

- A module is shipped by a team or partner that does not own the host's release cycle.
- The same host must enable different plugin sets per tenant.
- A plugin's lifecycle is independent enough that "rebuild the host to ship the plugin" is the wrong shape.

For modules your team writes alongside the host, keep them in `src/modules/` and rely on the standard plugin install instead. They build with the host, ship with the host, and never need the federation pipeline.

## The host's view

The host does not maintain a list of plugin remotes. At startup, it calls one Platform endpoint that returns a manifest of plugins to load:

```http
GET /api/apps/{appId}/manifest
```

The Platform's Backoffice Modularity Framework walks the .NET-module dependency graph, finds every `plugins/<appId>/remoteEntry.js` shipped by an installed module, applies permission filtering for the current user, and returns the resulting list — already topologically sorted. The host fetches each `remoteEntry.js`, loads its default export, and runs `app.use(plugin, { router })` exactly as if the plugin had been bundled with the host. From the host's perspective, the new blades, menu entries, and extension contributions just appear; there is no per-remote code to write.

Plugin remotes share Vue, the framework, and a handful of core libraries with the host as singletons, so a route registered by a plugin ends up in the same router the host uses, a translation merges into the same i18n instance, an extension-point contribution lands in the same registry. The build step of a federation module ensures these singletons are not duplicated; the host has nothing to configure.

## Writing a plugin remote

A plugin is a Vue subpackage inside a .NET module that builds a federation remote. The subpackage default-exports a Vue plugin (the same shape `app.use()` consumes); the federation config in the build step declares the `appId` it attaches to, the `moduleRoot` where the output lands, and a `remoteName` that matches the Platform's view of the .NET module:

```ts
import { getDynamicModuleConfiguration } from "@vc-shell/mf-module";

export default getDynamicModuleConfiguration({
  entry: "./src/modules/index.ts",
  appId: "vendor-portal",                // host this plugin attaches to
  moduleRoot,                            // absolute path to the .NET module root
  remoteName: "VirtoCommerce.MyModule",  // matches the Platform's manifest
});
```

The build output lands at `<moduleRoot>/plugins/<appId>/remoteEntry.js`. The .NET module's `.csproj` ships the `plugins/` folder inside the module zip; the Platform's `AppManifestService` finds the file by convention, computes a cache-busting hash, and surfaces it through the manifest endpoint. The host loads it on next boot, and the plugin is live.

The full author + host walkthrough — vite config options, entry-point shapes, federation-name alignment, build scripts, troubleshooting — lives in the [Module Federation guide](../guides/module-federation/index.md).

## Coexistence with bundled modules

A single host can mix bundled and plugin modules freely. Bundled modules install during `main.ts`; plugins install on top during boot. Both sides use the same extension points, the same notification store, the same permissions catalog. A bundled module exposing an extension slot will be filled by a plugin's contribution as long as the slot name matches. There is no separate "remote API".

## Compatibility

Plugin compatibility is settled on the Platform side, not in the browser. The Platform validates each plugin's `<dependency>` declarations in **module.manifest** at .NET module install time and refuses incompatible installs. By the time a plugin appears in the manifest endpoint, the dependency graph has already approved it — there is no client-side semver filter. Upgrading the host's framework does not silently drop older plugins; if a plugin becomes incompatible, the Platform admin sees an install-time error first.

- [Module Federation guide.](../guides/module-federation/index.md)
- [Modularity plugin reference.](../plugins/modularity.md)
- [Architecture overview.](architecture.md)
- [Extensions.](extensions.md)
