# Generate an App From a Prompt

Use `/vc-app design` as the primary start path for a new VC-Shell application. The command turns a free-text product description into a structured app plan, scaffolds the project if needed, and generates modules, blades, composables, locales, and mock data.

## Create a new app

From an empty workspace or an existing parent directory, ask your AI tool:

```text
/vc-app design "Build a supplier operations app with products, offers, fulfillment centers, and team management"
```

The skill will:

1. Parse entities, fields, actions, and relationships from the prompt.
2. Present a structured generation plan for confirmation.
3. Scaffold a VC-Shell project if no project exists.
4. Generate modules with list and details blades.
5. Use mock data when no API client is available.
6. Run type checking after generation.

## Add or enhance a module

Use `/vc-app generate` inside an existing app:

```text
/vc-app generate
```

If the target module does not exist, the skill creates it. If it exists, the skill switches to enhancement mode and can add columns, fields, toolbar actions, blade links, and logic.

## Output style

Generated code follows VC-Shell conventions:

- Vue 3 with `<script setup lang="ts">`.
- `defineBlade(...)` for blade metadata.
- `defineAppModule({ blades, locales })` for module registration.
- UI components from `@vc-shell/framework/ui`.
- Composables from `@vc-shell/framework`.
- Tailwind utilities with the `tw-` prefix.

- [Connect to Platform APIs.](connect-to-platform.md)
