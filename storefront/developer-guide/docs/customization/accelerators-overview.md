# Development Accelerators

Development accelerators are tools and scripts that automate routine tasks, enforce consistency, and speed up the workflow. When extending Frontend for your custom e-commerce project, you will likely want to create your own development accelerators:

| Aspect                      | Command(s) / Tools                          | Location                           | Description |
| --------------------------- | ------------------------------------------- | ---------------------------------- | ------ |
| Code generation             | `yarn generate:graphql-types`               | /scripts/graphql-codegen/generator.ts    | Generates TypeScript types from GraphQL schemas and queries for safe API usage. |
| Linting and formatting      | `yarn lint-staged`<br> `yarn lint` <br> `yarn lint:fix` <br> `yarn prettier` <br> `yarn prettier:fix` | eslint.config.js <br> .prettierrc.json <br> .prettierignore | Ensures consistent code style with automated linting/formatting before commits. |
| Commit message convention   | `commitlint`                     | .commitlintrc.json                 | Enforces standard commit message format for readable history and changelogs.|
| [Internationalization (i18n)](texts-customization.md) | `yarn check-locales`<br> `yarn fix-locales` | /scripts/ | Detects and fixes missing translation keys across locale files. |
| Type checking               | `yarn validate:types` (`vue-tsc`)           | Project root                       | Validates TypeScript across the codebase to ensure type safety.  |
| Dependency validation       | `yarn validate:dependencies` (`dependency-cruiser`)  | .dependency-cruiser.cjs   | Enforces dependency rules and prevents architectural violations. |
| UI development ([Storybook](../storybook.md))  | `yarn storybook:dev` <br> `yarn storybook:build`     | .storybook/               | Develop and test UI components in isolation with Storybook.      |
| Bundle analysis             | `yarn generate:bundle-map`               | /artifacts/bundle-map.html         | Generates a visual map of JS bundles to identify heavy dependencies.|
| Dependency graph            | `yarn generate:dependency-graph`            | /artifacts/dependency-graph.html   | Produces a graph of module dependencies to analyze architecture. |
| Local SSL certificates      | `yarn generate:certificates`                | /scripts/generate-certificates.ts  | Creates SSL certificates for secure local development (HTTPS).  |

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../customization-overview">← Customization</a>
    <a href="../accelerators-guidelines">Guidelines for using accelerators →</a>
</div>