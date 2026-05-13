# When To Use VC-Shell

## Use VC-Shell

- Back-office app for Virto Commerce: vendor portal, fulfillment console, pricing or merchandising tool, tenant-facing dashboard.
- You want Vue 3, TypeScript, and a working blade-paradigm engine on day one.
- You need to compose modules with extension points, bundled at build time or loaded at runtime via Module Federation.
- You need Platform integration: OAuth, role-based permissions, SignalR, dynamic properties, uploaded assets.
- You plan to ship more than one admin app and want to share a design system.

## Pick something else

- The customization fits inside the bundled Platform manager.
- Your stack is not Vue 3, or your design system is non-negotiable.
- The UI is not back-office in shape — a public storefront, a marketing page.
- No Virto Commerce Platform integration is needed.

## Trade-offs

| Trade-off | Implication |
| --- | --- |
| Bundle size. | Vue, Tailwind, icon and chart libraries, several organisms. Small apps pay for features they do not use. |
| Learning curve. | Blades, modules, and extension points are unfamiliar to teams new to the framework. |
| Vue and Platform lock-in. | Moving away later means rewriting. |
| Release cadence. | Track upstream breaking changes on every major bump. |

![Readmore](../getting-started/installation.md){: width="25"} Install and run your first app.
