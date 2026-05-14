# Embedded Mode

Launch a VC-Shell app inside the AngularJS-based Virto Commerce Platform back office.

A VC-Shell app runs in two layouts. Standalone is the default: the app is its own SPA, served from its own URL, with its own header, sidebar, and user dropdown. Embedded is opt-in: the Platform iframes the same app from a back-office menu entry, and the shell hides its top-level chrome so the AngularJS host frame owns the navigation. The choice is declared once in **module.manifest**; the same Vue bundle serves both modes.

## When to use

- A module complements rather than replaces the bundled Platform manager, and merchants reach it from the existing back-office menu.
- A product-specific surface, for example, Push Messages or Loyalty, is shipped as a VC-Shell app but needs to live next to AngularJS screens.
- A progressive AngularJS-to-Vue migration where some screens stay AngularJS and a new screen ships as a VC-Shell app.
- A merchant tool is gated by Platform permissions and should never be opened outside an authenticated back-office session.

## Enable embedded mode

Declare the app and set `<supportEmbeddedMode>` to `true` inside the `<app>` element:

```xml title="module.manifest" hl_lines="7"
<apps>
  <app id="push-messages">
    <title>Push Messages</title>
    <description>Push Messages</description>
    <iconUrl>/apps/push-messages/img/icons/safari-pinned-tab.svg</iconUrl>
    <permission>PushMessages:access</permission>
    <supportEmbeddedMode>true</supportEmbeddedMode>
  </app>
</apps>
```

Rebuild the module and deploy it to the Platform. Once installed, the app shows up as a menu entry in the back office and opens inside the AngularJS shell instead of in a new tab.

## What changes for the app

Nothing changes in the Vue code. The same VC-Shell bundle runs whether it is served standalone or iframed by the Platform. The framework detects the embedding context from the route, reading `EmbeddedMode=true` from the query string, and provides the resulting flag through the `EmbeddedModeKey` injection key. The shell uses that flag to hide the top header, the menu sidebar, the user dropdown, and the standalone AI agent panel, so the app blends into the host chrome without overlapping it.

If a blade or composable needs to vary its behavior in embedded mode, inject the same key:

```ts title="components/some-widget.vue"
import { inject } from "vue";
import { EmbeddedModeKey } from "@vc-shell/framework";

const isEmbedded = inject(EmbeddedModeKey, false);
```

Locale follows the host: when `isEmbedded` is `true`, `useShellBootstrap` calls `usePlatformLocaleSync` and the shell mirrors the Platform's `NG_TRANSLATE_LANG_KEY`. The in-shell language selector is hidden in embedded mode, so the host stays the single source of truth for the user's language.

## Deployment checklist

- App built and bundled into the module's static assets under **/apps/&lt;id&gt;/**.
- `<supportEmbeddedMode>true</supportEmbeddedMode>` added to the `<app>` element in **module.manifest**.
- A `<permission>` declared on the app so the menu entry respects back-office access control.
- Module deployed to a Platform instance whose VC-Shell dependency supports embedded mode. The feature landed in VC-Shell 1.1.61.

![Readmore](../../introduction/architecture-overview.md){: width="25"} How the shell composes apps.
