# Install the vc-app Skill

The `vc-app` skill adds VC-Shell-aware commands to your AI coding tool. It can scaffold apps, connect Platform APIs, generate modules, promote mock prototypes, and run framework migrations.

## Prerequisites

- Node.js 22 or higher.
- Corepack enabled: `corepack enable`.
- An AI coding tool supported by the skill.

## Install

Use the command for your runtime:

```bash
# Claude Code / Cursor / GitHub Copilot
npx @vc-shell/vc-app-skill install

# OpenCode
npx @vc-shell/vc-app-skill install --runtime opencode

# Gemini CLI
npx @vc-shell/vc-app-skill install --runtime gemini

# Codex
npx @vc-shell/vc-app-skill install --runtime codex
```

Restart the AI tool session after installation. The skill is active when `/vc-app` commands are available.

## Commands

| Command | Purpose |
| --- | --- |
| `/vc-app create` | Scaffold a new VC-Shell project. |
| `/vc-app connect` | Configure Platform URL and generate typed API clients. |
| `/vc-app add-module <name>` | Add an empty module skeleton. |
| `/vc-app generate` | Generate or enhance a UI module from intent. |
| `/vc-app design` | Generate a multi-module application from a prompt. |
| `/vc-app promote <name>` | Replace mock data in a prototype module with generated API clients. |
| `/vc-app migrate` | Migrate an existing app to the latest framework conventions. |

## Update

Run the install command again to update the skill:

```bash
npx @vc-shell/vc-app-skill install
```

- [Generate an app from a prompt.](generate-app-from-prompt.md)
