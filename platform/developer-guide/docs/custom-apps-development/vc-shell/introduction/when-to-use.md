# When To Use VC-Shell

A VC-Shell custom app is one of three places to build merchant-facing functionality on Virto Commerce. Pick the right surface for your use case before writing code.

## Use VC-Shell when

- You need a **dedicated back-office app** for a single audience: a vendor portal, a fulfillment console, a merchandising tool, a partner dashboard.
- The UI does not fit cleanly inside the Platform manager. It needs different navigation, a different visual identity, or separate authentication for non-platform users.
- You are building **multiple admin apps** that should share a design system and integration glue with the Virto Commerce Platform.
- You need to ship the app as a **remote Module Federation bundle** for a host shell.

## Extend the Platform manager when

- The customization is one or two screens that fit inside the bundled manager's blade stack.
- The audience is the same as the manager's: administrators and merchandisers operating the entire Platform.
- You only need to add or replace existing manager flows, not build a separate product surface.

## Customize the Vendor portal when

- The default vendor flow covers the use case with adjustments to fields, columns, or branding.
- You do not need to expose new entities or build new workflows.
- Forking the Vendor portal source costs less than starting a fresh VC-Shell app from scratch.

## Trade-offs

| Trade-off | Implication |
| --- | --- |
| Bundle size. | The framework brings Vue, Tailwind, an icon library, a chart library, and several organisms. Small apps pay for capabilities they do not use. |
| Learning curve. | Blades, modules, and extension points are unfamiliar to teams new to the framework. Plan a week of onboarding for the first feature. |
| Framework version cadence. | Track upstream breaking changes on every major bump of `@vc-shell/framework`. The migration CLI handles most of it. |

![Readmore](../getting-started/installation.md){: width="25"} Install and run your first app.
