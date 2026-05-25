# Manual CLI Start

Use the manual CLI path when you need a deterministic scaffold without AI-assisted app or module generation.

## Scaffold

```bash
npx @vc-shell/create-vc-app my-app --type standalone
cd my-app
yarn install
yarn serve
```

Optional flags:

| Flag | Purpose |
| --- | --- |
| `--dashboard` | Include a dashboard page and widget wiring. |
| `--mocks` | Include sample mock modules for local exploration. |
| `--tenant-routes` | Include tenant-aware route prefixes. |
| `--ai-agent` | Include AI agent configuration scaffold. |

## Add a module manually

```bash
npx @vc-shell/create-vc-app add-module orders
```

The command creates a module folder with list and details blades and wires it into the app entry points.

Use `/vc-app generate` when you want the AI skill to build or enhance modules from intent instead of starting from an empty skeleton. Continue with [Manual Platform API Setup](manual-platform-api-setup.md) when you want to connect the scaffold to Platform and generate API clients without the AI skill.

- [Project structure.](project-structure.md)
