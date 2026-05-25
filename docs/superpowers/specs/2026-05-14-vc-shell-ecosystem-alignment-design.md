# VC-Shell Documentation Ecosystem Alignment — Design

**Status:** Approved 2026-05-14.
**Scope:** Reframe 37 narrative pages of the VC-Shell section to match the project-wide documentation style.
**Inputs:** User feedback that current `introduction/` compares VC-Shell to non-VC frameworks (Quasar, Vuetify, Pinia), which is wrong for an ecommerce B2B solution; `create-your-app.md` does not mention the `vc-app` AI skill.
**Reference style:** `platform/developer-guide/docs/index.md`, `Fundamentals/Modularity/01-overview.md`, `Fundamentals/Caching/01-overview.md`.
**Relation to prior specs:** Builds on `2026-05-13-vc-shell-narrative-style-design.md`. That spec set the archetype skeletons; this spec adds the ecosystem-framing rule on top.

## 1. Goal

VC-Shell is a frontend layer of the Virto Commerce ecosystem. Readers arrive at these docs already in the VC stack. The documentation must reflect that.

Three deliverables:

1. **Introduction reframe**. Drop comparisons with non-VC products (Quasar, Vuetify, Pinia, Strapi, Sanity, React/Angular admins, "general Vue admin kit"). Position VC-Shell as a component of the VC ecosystem, not as a contender against external frameworks.
2. **`vc-app` AI skill**. Document the AI-assisted scaffolding path alongside the CLI scaffolder in `getting-started/create-your-app.md`.
3. **Project-style audit**. Sweep all 37 narrative pages for the same problems and for any additional drift from the project-wide tone (marketing-speak, ecosystem-framing inconsistencies, terminology).

## 2. The ecosystem-framing rule

A documentation page in this section may:

- Reference other Virto Commerce products (Platform, Storefront, Marketplace, Vendor Portal).
- Compare VC-Shell to the bundled Platform manager (when the comparison serves a decision the reader actually has).
- Mention third-party libraries when documenting an integration that VC-Shell uses internally (e.g., Tailwind, Vue Router, vee-validate, vue-i18n) — but only in technical context, never as "alternatives".

A documentation page in this section must NOT:

- Compare VC-Shell to non-VC frameworks (Quasar, Vuetify, Pinia as state alternatives, Strapi, Sanity, React/Angular admins).
- Use "Pick something else when…" / "Consider alternatives…" framing.
- Carry "What X is not" bullets that reference external products.
- Use marketing-speak ("blazing fast", "revolutionary", "powerful", "rich").

When the reader's decision is genuine, frame it within the VC ecosystem. Example replacement for the legacy "VC-Shell vs Quasar" comparison: a VC-internal decision matrix between **VC-Shell custom app** vs **extending the Platform manager** vs **customizing the Vendor portal**.

## 3. Streams

### Stream 1 — Introduction reframe (Phase F, 4 pages)

**Target files:**

- `introduction/index.md`
- `introduction/what-is-vc-shell.md`
- `introduction/architecture-overview.md`
- `introduction/when-to-use.md`

**Per-page directives:**

- `index.md`: rewrite the tagline and the 3 mental-model paragraphs in ecosystem-internal voice. Drop "Vue 3 ecosystem stance" prose that pitches VC-Shell against generic Vue tooling.
- `what-is-vc-shell.md`: delete the "How it compares" cross-platform table. Delete bullets in "What it is not" that reference Quasar, Vuetify, Strapi, Sanity, React, Angular. Either delete "What it is not" entirely or keep only VC-internal contrasts (such as "not a replacement for the Platform manager — complements it").
- `architecture-overview.md`: scan for any residual "Vue + general admin kit" comparison wording. Likely small; this page is mostly internal architecture.
- `when-to-use.md`: rewrite the page from scratch around the VC-internal decision. Three sections: "Use VC-Shell when…" (concrete VC use cases like vendor portal, custom merchandising console, partner-facing tool), "Use the Platform manager when…" (when customization fits inside bundled modules), "Use the Vendor portal when…" (when ready-made vendor flow is enough). Drop the trade-offs table comparing to external frameworks; if a trade-offs section remains, list internal trade-offs only (bundle size, learning curve, framework version cadence).

### Stream 2 — vc-app AI skill (Phase G, 1 page)

**Target file:** `getting-started/create-your-app.md`.

**Directive:** Add a new H2 section "Scaffold with the vc-app AI skill" positioned BEFORE "Generated layout" (so the reader sees both paths up front).

**Content:**

- Brief positioning paragraph: "The `vc-app` AI skill installs slash commands into your AI coding tool that scaffold projects, connect to a Platform, and generate full modules — an alternative to running the CLI by hand."
- Install commands per runtime (`Claude Code` / `Cursor` / `GitHub Copilot`, `OpenCode`, `Gemini CLI`, `Codex`). Each shown with the correct `--runtime` flag where applicable.
- Critical: use `npx @vc-shell/vc-app-skill install` (without `@alpha`).
- Slash-command reference: `/vc-app create`, `/vc-app connect`, `/vc-app generate`, `/vc-app add-module`, `/vc-app design`, `/vc-app migrate`. Verify against the actual command set in `cli/vc-app-skill/runtime/knowledge/`.
- One sentence about supported AI tools.
- Optional: `![Readmore]` link to the vc-app-skill README.

The existing "Run the scaffolder" CLI section stays — both paths are first-class.

### Stream 3 — Deep style audit (Phase H, 32 pages)

**Audit dimensions (apply to every page):**

| Dimension | What to look for |
| --- | --- |
| External comparisons. | Quasar, Vuetify, Pinia (as state alternative), Strapi, Sanity, "general Vue admin kit", "React/Angular admins". Remove the comparison; recast in ecosystem terms when the decision is internal. |
| "Alternatives" framing. | "Pick something else", "Consider X when", "if you need Y instead". Rewrite to ecosystem context or delete. |
| "What X is not" external. | Bullets pointing at non-VC products. Delete those bullets; keep VC-internal contrasts. |
| Marketing-speak. | "blazing fast", "revolutionary", "powerful", "rich set of features", "robust", "best in class". Replace with direct description. |
| Ecosystem language. | Use "the Platform", "Virto Commerce", "Frontend" (the user-facing storefront) consistently. Capitalize Platform only when referring to the Virto Commerce Platform; lowercase otherwise. |
| Style guide compliance (CLAUDE.md). | "Virto Commerce" (two words), `Frontend` alone (never "storefront" / "Frontend Application"), `ecommerce` lowercase mid-sentence / `eCommerce` in titles, `xAPI` / `xCatalog` / `xFile` / `xCart` / `xFrontend` orthography, file names in bold, sentence-ending periods including in tables and list items, no em dashes with spaces. |

**Batches:**

- **H1 — getting-started/** (4 pages remaining after Stream 2 touches `create-your-app.md`): `installation.md`, `project-structure.md`, `connecting-to-platform.md`, `first-blade.md`.
- **H2 — concepts/** (8 pages): `blade-navigation.md`, `modules.md`, `extensions.md`, `layout.md`, `permissions-model.md`, `localization.md`, `state-persistence.md`, `api-clients.md`.
- **H3 — guides/** (13 pages): `blades/index.md`, `data/index.md`, `forms/index.md`, `ui/index.md`, `modules-and-extensions/index.md`, `platform/index.md`, `platform/embedded-mode.md`, `platform/auth-pages.md`, `platform/custom-auth.md`, `cookbook/index.md`, `troubleshooting/index.md`, `deployment.md`, `routing.md`, `best-practices.md`.
- **H4 — reference/migration/** (1 page): `index.md`.

Each batch subagent:

1. Reads every page in its batch.
2. Applies audit dimensions.
3. Edits in place.
4. Commits per page (or per coherent batch) with descriptive messages.
5. Returns a per-page change summary.

## 4. Out of scope

- Pre-existing 2 mkdocs warnings on `docs/superpowers/specs+plans` (placeholder paths inside markdown examples).
- Auto-synced reference pages under `components/`, `composables/`, `plugins/`, `reference/api/`, `reference/modules/` (CI guard; out of edit scope).
- Restructure of folders or `.pages` reorganization.
- Diagrams beyond what already exists.

## 5. Acceptance criteria

For Streams 1 and 2:

- No mentions of Quasar, Vuetify, Pinia (as alternative), Strapi, Sanity, "general admin kit", "React/Angular admins" anywhere under `platform/developer-guide/docs/custom-apps-development/vc-shell/`.
- `introduction/when-to-use.md` decisions framed in VC ecosystem only.
- `getting-started/create-your-app.md` has a vc-app AI skill section with install command without `@alpha`.

For Stream 3:

- Every modified page passes the audit dimensions table.
- `mkdocs build` introduces no new warnings on touched pages.

For all:

- 37 pages remain consistent in voice with `platform/developer-guide/docs/index.md` and `Fundamentals/Modularity/01-overview.md`.
- Style spec (`2026-05-13-vc-shell-narrative-style-design.md`) rules still hold (no `When to read this`, no `??? collapsible`, no custom HTML footer, mental model in concepts H1, code blocks have `title=`).

## 6. Roadmap

| Phase | Pages | Subagent count |
| --- | --- | --- |
| F. Introduction reframe. | 4. | 1. |
| G. Add vc-app skill section. | 1. | 1. |
| H1. getting-started/ audit. | 4. | 1. |
| H2. concepts/ audit. | 8. | 1. |
| H3. guides/ audit. | 13. | 1. |
| H4. reference/migration/ audit. | 1. | 1. |

Total: 6 subagent dispatches.

## 7. Verification

After all phases:

1. `mkdocs build` returns no new warnings on vc-shell pages.
2. `grep -rniE "quasar|vuetify|pinia.*alternative|strapi|sanity|general.*admin.*kit|react.?or.?angular" platform/developer-guide/docs/custom-apps-development/vc-shell/` returns nothing relevant (some hits may be in code identifiers; review each).
3. `grep -rln "Pick something else\|Consider alternatives" platform/developer-guide/docs/custom-apps-development/vc-shell/` returns empty.
4. `grep -rln "When to read this" platform/developer-guide/docs/custom-apps-development/vc-shell/` returns empty.
5. `grep -rnE "^\?\?\?" platform/developer-guide/docs/custom-apps-development/vc-shell/{introduction,getting-started,concepts,guides,reference/migration}/` returns empty.
