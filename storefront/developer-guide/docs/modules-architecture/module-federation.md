# Module Federation

Module Federation lets a backend module ship its own Frontend UI as a separate build, loaded by the Frontend at runtime instead of being compiled into its bundle. The Sales Rep Hub is the first module shipped this way, replacing the module that used to live directly in **client-app/modules/sales-rep**.

Choose a plugin over an in-repo module when the feature ships on a backend module's own release cadence, not the Frontend's.

## Plugin loading

The Frontend gets its plugin list at startup, from the `store.plugins(appId: "vc-frontend")` query or a build-time override for local development.

Before any plugin code is fetched, the Frontend checks each plugin's required permission and its `when` condition. It then applies the placeholders, menu entries, and reserved slots the plugin declared.

For each remaining plugin, the Frontend:

1. Fetches its **mf-manifest.json**.
1. Skips the plugin if its required facade version does not match the host's.
1. Loads the plugin's code.
1. Calls its `init()` function.

The plugin ends up loaded, failed, or skipped.

!!! note
    **Loaded** does not mean **working**. A plugin with no `init()` function still counts as loaded, with a warning.

## Declaration and implementation

A plugin describes itself to the Frontend in two layers:

* **plugin.config.ts**: read before the plugin's code is fetched. It declares routes, menu entries, and reserved slots.
* **src/index.ts**, through its `init()` function: read once the plugin's code has loaded. It registers the real routes, components, and logic.

A declared route shows a loader inside its parent page while the plugin is still loading, instead of a 404. Declared menu entries and slots render immediately, before the plugin code arrives.

## Enable Module Federation

Module Federation is controlled by `module_federation_enabled` in **client-app/config/settings_data.json**, a build-time theme setting rather than a Store-level toggle. Only a literal `true` turns it on.

It ships on by default from theme version 2.60. It requires Platform 3.1078.0 and higher, with the **VirtoCommerce.XFrontend** module 3.1005.0 and higher.

!!! note
    The Sales Rep Hub has no fallback. Disable Module Federation or remove the plugin, and the Hub disappears entirely.

## Build plugin

A plugin is a separate Vite and Vue project that exposes a `./plugin` entry point with an `init()` function, built with the `federation()` plugin from `@vc-frontend/core/federation`. It consumes the Frontend's router, Apollo client, and UI kit only through the `@vc-frontend/core` facade package. It never imports the Frontend's own source directly.

Scaffold a new plugin with:

```bash
yarn create:plugin <name> <dir>
```

Or scaffold one directly inside a backend module:

```bash
yarn create:plugin <name> --module <YourModule.Web>
```

A backend module ships its built plugin by publishing it to **{moduleRoot}/plugins/vc-frontend/**, the same folder the Platform already serves module assets from. Check a module and its package before shipping with:

```bash
yarn check:plugin-module <YourModule.Web>
```

## Security

A plugin runs with the Frontend's full rights: the same origin, the same session, the same Apollo client. A plugin's required permission only decides whether a signed-in user's browser fetches it. It is not a security boundary, so the backend must still authorize every query the plugin makes.


![Readmore](../media/readmore.png){: width="25"} [Module Federation guide and scenarios](https://github.com/VirtoCommerce/vc-frontend/blob/dev/client-app/core/federation/README.md)

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../modules-architecture">← Modules architecture</a>
    <a href="../../spa-architecture-for-seo-and-404-handling">SPA architecture for SEO and 404 handling →</a>
</div>
