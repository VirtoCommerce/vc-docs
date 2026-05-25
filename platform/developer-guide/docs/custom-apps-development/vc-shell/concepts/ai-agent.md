# AI Agent

VC-Shell can embed an AI assistant directly inside the app: a panel that slides in from the right, sees the same context the user sees, and can suggest changes that the user previews and applies. The framework owns the panel chrome and the two-way bridge to the assistant. Your modules decide which actions the assistant can drive and which blade context it receives.

The AI Agent is optional. If you do not configure an agent URL, the framework silently skips installing the panel and the app runs as a plain VC-Shell app. There is no penalty for leaving it off.

## What the assistant sees

The agent runs in a sandbox separate from the host. The framework relays context across that boundary: the current user, the active blade, the parameters that opened it, the rows currently selected in a list. The assistant cannot reach into your app's memory or DOM; it only knows what the host forwards.

The host stays in control of every change. The assistant proposes; the host carries out. When the assistant requests a "preview changes" view, the host renders a comparison. When the user clicks Apply, the host writes the change through the blade's normal save path. When the user clicks Cancel, nothing happens.

## What you wire from your modules

The framework provides the panel, the channel, and the default set of context messages (open, close, blade-context-changed, navigate, preview, apply, download). Modules contribute the substance:

| You add | Where it goes |
| --- | --- |
| Which blade fields show in the preview panel. | A schema or formatter exposed by the module that owns the blade. |
| How an "apply" message becomes a save. | The blade's existing save handler, called with the proposed values. |
| What "context" means for a blade. | Optional hooks that map the blade's state to the message payload. |

Most blades need nothing module-specific. The defaults: user, blade name, parameters, and a list of selected ids cover the assistant's typical needs. Reach for custom context only when the blade has structured state the assistant should act on, for example, a draft pricing table.

## When to use it

The AI Agent shines for catalog-heavy or content-heavy modules where the user's task is "draft a thing, then refine it": writing product descriptions, generating marketing copy, drafting pricing rules, building a quote. It is less useful for transactional flows where the user is following a strict business rule and there is little to interpret.

Treat it as an optional surface, not a redesign of the user's workflow. The blade and the assistant should be usable independently. If a blade requires the assistant to function, you have built two products in a trench coat.

## Configuration

Enable the agent by setting an agent URL at build or runtime:

```bash title=".env"
APP_AI_AGENT_URL=https://agent.example.com/chat
```

With that single environment variable, the panel appears, the channel opens, and the framework starts forwarding default context. Everything beyond that is module-level wiring.

- [AI Agent plugin reference.](../plugins/ai-agent.md)
- [Embedded mode.](embedded-mode.md)
