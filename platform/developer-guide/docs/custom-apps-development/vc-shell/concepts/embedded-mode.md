# Embedded Mode

A VC-Shell app runs in one of two layouts. By default it is standalone: served from its own URL, owning its top header, its menu sidebar, its user menu. Embedded mode is opt-in: the same Vue bundle is iframed by the AngularJS-based Virto Commerce Platform back office, and the shell hides its outer chrome so the host frame owns the navigation. One bundle, two layouts.

This split exists because the Platform back office is itself an app, with its own menu and its own session. A VC-Shell app that lives inside it should feel like part of the same product, not a second product inside a window. Hiding the shell's own header is the simplest version of "feel like part of the host".

## What the app sees

The framework detects the embedding context from the route. When the Platform opens the app, it appends `EmbeddedMode=true` to the URL. The framework picks that up early in boot and exposes the result through an injection key.

```ts title="components/some-widget.vue"
import { inject } from "vue";
import { EmbeddedModeKey } from "@vc-shell/framework";

const isEmbedded = inject(EmbeddedModeKey, false);
```

Most blades never read the flag. Default rendering is the same in both modes; what changes is what the shell hides around them. Blades touch the flag only when they want to suppress UI that duplicates host functionality, for example, hiding a "sign out" button when the host already owns sign-out.

## What the shell hides automatically

When embedded mode is detected, the shell:

- Hides its top header bar.
- Hides the menu sidebar.
- Hides the user dropdown.
- Hides the standalone AI Agent panel.
- Synchronizes the active locale with the host's `NG_TRANSLATE_LANG_KEY` and hides the in-shell language selector.

The list is deliberately small. The blade stack, the dashboard, popups, toasts, the notification dropdown, and every business-domain surface stay exactly where they are. The user keeps the muscle memory they built in standalone mode.

## A single source of truth per concern

Embedded mode rests on the rule that any given concern has one owner. Locale: the host owns it; the shell mirrors. Sign-in: the host owns it; the shell trusts the iframed session. Navigation to the app: the host owns it; the shell stops drawing its own menu. The app never tries to read or write the host's state directly. Where the host needs to influence the app, it does so through the URL.

This is what lets the same bundle ship both modes safely. A blade does not know whether the user reached it from the standalone URL or from a Platform menu click. It does not need to know.

## When to enable it

Embedded mode fits when a module complements the back office rather than replacing it: a Push Messages app, a Loyalty surface, a progressive migration of one screen from AngularJS to Vue. It does not fit when the app's value is to be its own product: a standalone storefront-adjacent tool that lives at its own domain.

The decision is declared once per app in **module.manifest** through `<supportEmbeddedMode>`. The same Vue code ships either way.

- [Embedded mode setup.](../guides/platform/embedded-mode.md)
- [Architecture.](architecture.md)
- [Localization.](localization.md)
