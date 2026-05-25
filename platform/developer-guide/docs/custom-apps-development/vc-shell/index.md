# VC-Shell

VC-Shell is the Vue 3 application framework for building custom back-office applications on the Virto Commerce Platform. It provides the authenticated shell, blade navigation, UI components, composables, module runtime, localization, permissions, notifications, and Platform API integration that custom applications use.

The recommended starting point is the `vc-app` AI skill. It can scaffold a shell app, connect it to a Virto Commerce Platform instance, generate working prototype modules from a prompt, and promote mock-backed prototypes to generated API clients when the backend contract is ready.

The skill is available for AI coding tools that can load file-based skills or slash commands: Claude Code, Cursor, GitHub Copilot, OpenCode, Gemini CLI, and Codex. Runtime-specific install commands are documented in [Install the vc-app Skill](getting-started/install-vc-app-skill.md).

```bash
npx @vc-shell/vc-app-skill install
```

After installing the skill in your AI coding tool, start with:

```text
/vc-app design "Build an app for managing orders, inventory, and customer service workflows"
```

Use the manual CLI path only when you need a deterministic scaffold without AI-assisted generation:

```bash
npx @vc-shell/create-vc-app my-app --type standalone
cd my-app
yarn install
yarn serve
```

## Documentation map

| Section | Use it for |
| --- | --- |
| [Getting Started](getting-started/getting-started.md) | Installing the AI skill, generating an app from a prompt, connecting Platform APIs, and promoting prototypes. |
| [Concepts](concepts/architecture.md) | Framework contracts: app structure, blades, modules, Platform integration, permissions, localization, and Module Federation. |
| [Guides](guides/blades/index.md) | Task-based implementation patterns for production apps. |
| [Components](components/layout/vc-app.md) | UI component reference. |
| [Composables](composables/blade-navigation/useBlade.md) | Composable API reference. |
| [Plugins](plugins/modularity.md) | Framework plugin reference. |
| [Reference](reference/api/index.md) | CLI, API utilities, built-in modules, and migration reference. |
