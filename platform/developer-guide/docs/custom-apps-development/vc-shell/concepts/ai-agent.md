# AI Agent

VC-Shell can embed an AI assistant directly inside the app: a panel that slides in from the right and sees the same context the user sees. The framework owns the panel chrome and the two-way bridge to the assistant. Your modules decide which blade context the assistant receives and which prompts it offers as shortcuts.

The AI Agent is optional. If you do not configure an agent URL, the framework silently skips installing the panel and the app runs as a plain VC-Shell app. There is no penalty for leaving it off.

## What the assistant sees

The agent runs in a sandbox separate from the host. The framework relays context across that boundary: the current user, the active blade, the parameters that opened it, the rows currently selected in a list. The assistant cannot reach into your app's memory or DOM; it only knows what the host forwards.

## What you wire from your modules

The framework provides the panel, the channel, and the default set of context messages (open, close, blade-context-changed, navigate, download). Modules contribute the substance:

| You add | Where it goes |
| --- | --- |
| What "context" means for a blade. | A call to `useAiAgentContext` that binds the blade's data ref. |
| Which prompts the panel offers as shortcuts. | The `suggestions` array passed to `useAiAgentContext`. |

Most blades need nothing module-specific beyond the data ref. The defaults — user, blade name, parameters, and a list of selected ids — cover the assistant's typical needs. Reach for custom suggestions only when the blade has well-defined tasks the assistant should drive on, for example, "translate description" or "generate summary".

## When to use it

The AI Agent shines for catalog-heavy or content-heavy modules where the user's task is "draft a thing, then refine it": writing product descriptions, generating marketing copy, drafting pricing rules, building a quote. It is less useful for transactional flows where the user is following a strict business rule and there is little to interpret.

Treat it as an optional surface, not a redesign of the user's workflow. The blade and the assistant should be usable independently. If a blade requires the assistant to function, you have built two products in a trench coat.

## Configuration

Enable the agent by setting an agent URL at build or runtime:

```bash title=".env"
APP_AI_AGENT_URL=https://agent.example.com/chat
```

With that single environment variable, the panel appears, the channel opens, and the framework starts forwarding default context. Everything beyond that is module-level wiring.

- [Integrate the AI Agent — step-by-step.](../guides/ai-agent-integration.md)
- [AI Agent plugin reference.](../plugins/ai-agent.md)
- [Embedded mode.](embedded-mode.md)
