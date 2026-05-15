# VC-Shell Ecosystem Alignment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reframe the VC-Shell narrative documentation under the ecosystem-only positioning rule (no comparisons with non-VC frameworks), document the `vc-app` AI skill in `getting-started/create-your-app.md`, and audit all 37 narrative pages for compliance with the project-wide style.

**Architecture:** Three streams. Stream 1 rewrites the four `introduction/` pages with ecosystem-internal voice. Stream 2 adds an `vc-app` AI skill section to `getting-started/create-your-app.md`. Stream 3 sweeps the remaining 32 narrative pages in four archetype-batch subagents that find and fix style drift in place. One subagent dispatch per task; commits per page or per coherent batch.

**Tech Stack:** mkdocs, mkdocs-material, awesome-pages, pymdownx.superfences, pymdownx.details (already configured).

**Reference spec:** `/Users/symbot/DEV/vc-docs/docs/superpowers/specs/2026-05-14-vc-shell-ecosystem-alignment-design.md`.

**Style anchor sources (read for tone calibration):**

- `/Users/symbot/DEV/vc-docs/platform/developer-guide/docs/index.md` — Platform docs index, ecosystem framing.
- `/Users/symbot/DEV/vc-docs/platform/developer-guide/docs/Fundamentals/Modularity/01-overview.md` — narrative concept page exemplar.
- `/Users/symbot/DEV/vc-docs/platform/developer-guide/docs/Fundamentals/Caching/01-overview.md` — second narrative exemplar.
- `/Users/symbot/DEV/vc-docs/CLAUDE.md` — project-wide style guide (Virto Commerce orthography, sentence-ending periods, file names in bold, no italics, no em dashes with spaces).

**vc-app skill source of truth (in `/Users/symbot/DEV/vc-shell-main-dev/vc-shell/cli/vc-app-skill/`):**

- `package.json` — version (`2.0.3` at the time of writing).
- `README.md` — install commands per runtime, full slash-command reference.
- `commands/vc-app.md` — canonical slash-command entry.
- `runtime/knowledge/` — knowledge base (patterns, agents, examples).

---

## Files

All 37 pages are under `platform/developer-guide/docs/custom-apps-development/vc-shell/`.

**Stream 1 — introduction/ (Phase F, 4 pages):**

- `introduction/index.md`
- `introduction/what-is-vc-shell.md`
- `introduction/architecture-overview.md`
- `introduction/when-to-use.md`

**Stream 2 — getting-started/create-your-app.md (Phase G, 1 page):**

- `getting-started/create-your-app.md`

**Stream 3 — audit batches (Phase H, 32 pages):**

- **H1 — getting-started/** (4 pages): `installation.md`, `project-structure.md`, `connecting-to-platform.md`, `first-blade.md`.
- **H2 — concepts/** (8 pages): `blade-navigation.md`, `modules.md`, `extensions.md`, `layout.md`, `permissions-model.md`, `localization.md`, `state-persistence.md`, `api-clients.md`.
- **H3 — guides/** (13 pages): `blades/index.md`, `data/index.md`, `forms/index.md`, `ui/index.md`, `modules-and-extensions/index.md`, `platform/index.md`, `platform/embedded-mode.md`, `platform/auth-pages.md`, `platform/custom-auth.md`, `cookbook/index.md`, `troubleshooting/index.md`, `deployment.md`, `routing.md`, `best-practices.md`.
- **H4 — reference/migration/** (1 page): `index.md`.

---

## Appendix A: The ecosystem-framing rule

A documentation page in this section MAY:

- Reference other Virto Commerce products (Platform, Storefront, Marketplace, Vendor Portal).
- Compare VC-Shell to the bundled Platform manager when the comparison serves an actual reader decision.
- Mention third-party libraries that VC-Shell uses internally (Tailwind, Vue Router, vee-validate, vue-i18n) — only in technical context, never as "alternatives".

A documentation page in this section MUST NOT:

- Compare VC-Shell to non-VC frameworks (Quasar, Vuetify, Pinia as a state alternative, Strapi, Sanity, React/Angular admins).
- Use "Pick something else when…" or "Consider alternatives…" framing.
- Carry "What X is not" bullets that point at external products.
- Use marketing-speak ("blazing fast", "revolutionary", "powerful", "rich set of features", "robust", "best in class").

---

## Appendix B: Audit dimensions (apply to every page)

| Dimension | What to look for | Action |
| --- | --- | --- |
| External comparisons. | Quasar, Vuetify, Pinia (as alt), Strapi, Sanity, "general Vue admin kit", "React/Angular admins". | Remove the comparison; recast in VC-internal terms when a decision exists. |
| "Alternatives" framing. | "Pick something else", "Consider X when", "if you need Y instead". | Rewrite to ecosystem context or delete. |
| "What X is not" external. | Bullets pointing at non-VC products. | Delete those bullets; keep VC-internal contrasts only. |
| Marketing-speak. | "blazing fast", "revolutionary", "powerful", "rich set of features", "robust", "best in class". | Replace with direct description. |
| Ecosystem language. | Ensure "the Platform" / "Virto Commerce" / "Frontend" usage is consistent. Capitalize Platform when referring to VC Platform. | Edit in place. |
| Style guide compliance. | "Virto Commerce" (two words), `Frontend` alone, `ecommerce` / `eCommerce`, `xAPI` / `xCatalog` / `xFile` / `xCart` / `xFrontend`, file names bolded, sentence-ending periods including in tables and lists, no em dashes with spaces. | Edit in place. |
| Style spec invariants. | No `## When to read this` sections, no `??? collapsible` blocks, no custom HTML prev/next footers, every concepts H2 opens with prose. | Edit in place. |

---

## Task 0: Baseline check

**Files:**
- None (read-only).

- [ ] **Step 1: Capture pre-existing mkdocs warnings on vc-shell pages**

```bash
cd /Users/symbot/DEV/vc-docs
mkdocs build 2>&1 | grep -E "WARNING.*custom-apps-development/vc-shell" > /tmp/vc-shell-baseline.txt
wc -l /tmp/vc-shell-baseline.txt
```

Expected: count of pre-existing warnings (likely 0 for vc-shell scope).

- [ ] **Step 2: Confirm vc-shell source repo + vc-app-skill present**

```bash
test -d /Users/symbot/DEV/vc-shell-main-dev/vc-shell/cli/vc-app-skill && echo OK
test -f /Users/symbot/DEV/vc-shell-main-dev/vc-shell/cli/vc-app-skill/README.md && echo OK
```

Expected: `OK\nOK`.

- [ ] **Step 3: Confirm spec is in place**

```bash
test -f /Users/symbot/DEV/vc-docs/docs/superpowers/specs/2026-05-14-vc-shell-ecosystem-alignment-design.md && echo OK
```

Expected: `OK`.

No commit.

---

## Phase F: Introduction reframe (1 task)

### Task 1: Reframe `introduction/` to ecosystem-internal voice

**Files (modify):**

- `platform/developer-guide/docs/custom-apps-development/vc-shell/introduction/index.md`
- `platform/developer-guide/docs/custom-apps-development/vc-shell/introduction/what-is-vc-shell.md`
- `platform/developer-guide/docs/custom-apps-development/vc-shell/introduction/architecture-overview.md`
- `platform/developer-guide/docs/custom-apps-development/vc-shell/introduction/when-to-use.md`

**Per-page directives:**

#### `introduction/index.md`

- Confirm tagline opens by placing VC-Shell inside the Virto Commerce ecosystem. Replacement tagline:
  > VC-Shell is the Vue 3 frontend layer of the Virto Commerce ecosystem — the framework you build custom back-office apps on top of the Virto Commerce Platform.
- Drop the third mental-model paragraph that pitches VC-Shell against generic Vue tooling ("You stay in the Vue 3 ecosystem the whole way through…"). Replace with one paragraph about how the apps slot into the broader VC product family (Platform, Vendor portal, Storefront).
- Keep the install one-liner, the Storybook iframe, and the inline `![Readmore]` cross-links.
- Verify length stays in 200–600 words (introduction archetype).

#### `introduction/what-is-vc-shell.md`

- Delete the "## How it compares" H2 section AND its cross-platform comparison table entirely.
- Rewrite the "## What it is not" section to keep only VC-internal contrasts. Acceptable bullets:
  - "Not a replacement for the Virto Commerce Platform manager — it complements the manager when a customization does not fit inside it."
  - "Not a CMS — VC-Shell consumes Platform APIs; for content, use the Platform's own catalog and content modules."
  - "Not a deployment platform — it is the frontend; deployment is your CI/CD and static hosting story."
- Remove these bullets if currently present:
  - "Not a general-purpose admin template. Use Quasar or Vuetify if you need a generic admin kit."
  - "Not framework-agnostic. Vue 3 + Composition API is hardcoded; for React or Angular admins, pick a different framework."
- Reframe the lead paragraphs to position VC-Shell as the **canonical** frontend layer for VC, not as one option among many.
- Verify length stays in 400–600 words.

#### `introduction/architecture-overview.md`

- Read the page. Look for any wording in the layer table or prose that compares VC-Shell to "general Vue admin kits" or "Vue + Tailwind starters". If found, remove and rephrase as ecosystem-internal description.
- The mermaid diagram, layer table, blade architecture table, module model section, MF section, public API, source-of-truth table all stay. They are already ecosystem-internal.
- Likely a small change. Length stays in 600–900 words.

#### `introduction/when-to-use.md`

- Rewrite from scratch. New structure:

  ```markdown
  # When To Use VC-Shell

  A VC-Shell custom app is one of three places to build merchant-facing functionality on Virto Commerce. Pick the right surface for your use case before writing code.

  ## Use VC-Shell when

  - You need a **dedicated back-office app** for a single audience: a vendor portal, a fulfillment console, a merchandising tool, a partner dashboard.
  - The UI does not fit cleanly inside the Platform manager — different navigation, different visual identity, separate authentication for non-platform users.
  - You are building **multiple admin apps** that should share a design system and integration glue with the Virto Commerce Platform.
  - You need to ship the app as a **remote Module Federation bundle** for a host shell.

  ## Extend the Platform manager when

  - The customization is one or two screens that fit inside the bundled manager's blade stack.
  - The audience is the same as the manager's (administrators, merchandisers operating the entire Platform).
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
  ```

- Length: ~280–420 words.

**Style invariants:**

- `!!! note` / `!!! tip` / `!!! warning` / `!!! info` only. NEVER `??? collapsible`.
- No `## Next` link list at end (mkdocs-material renders prev/next automatically).
- No custom HTML prev/next footer.
- CLAUDE.md applies on top.

**Per-page audit checklist (ALL four):**

1. No mention of Quasar, Vuetify, Pinia, Strapi, Sanity, "general Vue admin kit", "React/Angular admins".
2. No "Pick something else" / "Consider alternatives" framing.
3. Decisions framed in VC ecosystem only.
4. CLAUDE.md orthography (Virto Commerce, Platform, Frontend) applied.
5. Length within archetype range.
6. Inline `![Readmore]` cross-links preserved or repositioned.

**Steps:**

- [ ] **Step 1: Read `index.md`, apply directives.**

- [ ] **Step 2: Read `what-is-vc-shell.md`, delete the comparison table and external-product bullets, rewrite intro.**

- [ ] **Step 3: Read `architecture-overview.md`, scan for residual external comparisons, fix in place.**

- [ ] **Step 4: Read `when-to-use.md`, replace contents wholesale with the new VC-internal three-bucket structure shown above.**

- [ ] **Step 5: Run grep verification.**

```bash
grep -rniE "quasar|vuetify|strapi|sanity|general.*admin.*kit|pick something else|consider alternatives" \
  platform/developer-guide/docs/custom-apps-development/vc-shell/introduction/
```

Expected: empty.

- [ ] **Step 6: Run mkdocs build, confirm no new warnings on these pages.**

```bash
mkdocs build 2>&1 | grep -E "WARNING.*introduction" | grep -v -F -f /tmp/vc-shell-baseline.txt
```

Expected: empty.

- [ ] **Step 7: Commit per page.**

```bash
git add platform/developer-guide/docs/custom-apps-development/vc-shell/introduction/index.md
git commit -m "docs(vc-shell): reframe introduction/index for VC ecosystem"

git add platform/developer-guide/docs/custom-apps-development/vc-shell/introduction/what-is-vc-shell.md
git commit -m "docs(vc-shell): drop external comparisons in what-is-vc-shell"

git add platform/developer-guide/docs/custom-apps-development/vc-shell/introduction/architecture-overview.md
git commit -m "docs(vc-shell): polish architecture-overview ecosystem framing"

git add platform/developer-guide/docs/custom-apps-development/vc-shell/introduction/when-to-use.md
git commit -m "docs(vc-shell): rewrite when-to-use as VC-internal decision"
```

Each commit MUST include `Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>` via HEREDOC.

**Report:** Status, word counts per page, grep verification result, commit SHAs, concerns.

---

## Phase G: Add vc-app skill section (1 task)

### Task 2: Add vc-app AI skill section to `getting-started/create-your-app.md`

**Files (modify):**

- `platform/developer-guide/docs/custom-apps-development/vc-shell/getting-started/create-your-app.md`

**Source materials:**

- `/Users/symbot/DEV/vc-shell-main-dev/vc-shell/cli/vc-app-skill/README.md` — full slash-command reference.
- `/Users/symbot/DEV/vc-shell-main-dev/vc-shell/cli/vc-app-skill/package.json` — version.
- `/Users/symbot/DEV/vc-shell-main-dev/vc-shell/cli/vc-app-skill/commands/vc-app.md` — canonical entry.
- `/Users/symbot/DEV/vc-shell-main-dev/vc-shell/cli/vc-app-skill/runtime/knowledge/` — knowledge base (verify slash command coverage).
- `/Users/symbot/DEV/vc-shell-main-dev/vc-shell/README.md` — also lists install commands.

**Confirmed slash-command set (from `cli/vc-app-skill/README.md`):**

- `/vc-app create`
- `/vc-app connect`
- `/vc-app add-module <name>`
- `/vc-app generate`
- `/vc-app design`
- `/vc-app promote <name>`
- `/vc-app migrate`

**Critical:** Use install command `npx @vc-shell/vc-app-skill install` (NO `@alpha`, NO `@latest` — the README has `@alpha` but the published package is now `@2.0.3` on the default tag).

**Per-runtime install commands:**

```bash
# Claude Code / Cursor / GitHub Copilot (default)
npx @vc-shell/vc-app-skill install

# OpenCode
npx @vc-shell/vc-app-skill install --runtime opencode

# Gemini CLI
npx @vc-shell/vc-app-skill install --runtime gemini

# Codex
npx @vc-shell/vc-app-skill install --runtime codex
```

**Section to insert (place BEFORE the `## Generated layout` H2 so the reader sees both paths up front):**

```markdown
## Scaffold with the vc-app AI skill

The `vc-app` AI skill installs slash commands into your AI coding tool that scaffold projects, connect to a Virto Commerce Platform, and generate full UI modules from plain-English intent. This is an alternative to running the CLI by hand — pick the path that fits your workflow.

### Install

Pick the line that matches your AI tool. Restart the AI tool session after install to register the `/vc-app` commands.

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

### Slash commands

| Command | What it does |
| --- | --- |
| `/vc-app create`. | Scaffold a new VC-Shell project interactively. |
| `/vc-app connect`. | Wire `.env` / `.env.local` and generate typed API clients from a Platform instance. |
| `/vc-app add-module <name>`. | Add a list + details module to an existing app. |
| `/vc-app generate`. | Intent-driven module generation with mock or live data. |
| `/vc-app design`. | Generate a multi-module app from a free-text product description. |
| `/vc-app promote <name>`. | Promote a prototype module from mock data to real API clients. |
| `/vc-app migrate`. | Migrate the app to the latest `@vc-shell/framework` version (runs the CLI migrator and AI-assisted manual refactors). |

The skill follows VC-Shell conventions automatically: Vue 3 with `<script setup lang="ts">`, Tailwind with the `tw-` prefix, BEM class names, and the framework's blade and module patterns.

![Readmore](https://github.com/VirtoCommerce/vc-shell/blob/main/cli/vc-app-skill/README.md){: width="25"} Full vc-app skill README on GitHub.
```

**Position:** insert this section IMMEDIATELY AFTER `## Run the scaffolder` (the existing CLI section) and BEFORE `## Generated layout`. The result is a page where the CLI path and the AI path are both first-class, side by side.

**Style invariants:**

- `!!! note` / `!!! tip` / `!!! warning` / `!!! info` only.
- Code blocks use `bash` for shell snippets.
- All slash commands verified against `cli/vc-app-skill/README.md`.
- CLAUDE.md applies.
- Length: keep page under 1000 words after the addition.

**Steps:**

- [ ] **Step 1: Read the current `create-your-app.md` to find the insertion point (between `## Run the scaffolder` and `## Generated layout`).**

- [ ] **Step 2: Verify the slash-command list against `cli/vc-app-skill/README.md`. If commands have changed, adjust.**

- [ ] **Step 3: Insert the new `## Scaffold with the vc-app AI skill` H2 section.**

- [ ] **Step 4: Verify length: `wc -w platform/developer-guide/docs/custom-apps-development/vc-shell/getting-started/create-your-app.md`. Should be under 1000 words.**

- [ ] **Step 5: Run mkdocs build, confirm no new warnings.**

```bash
mkdocs build 2>&1 | grep -E "WARNING.*create-your-app" | grep -v -F -f /tmp/vc-shell-baseline.txt
```

Expected: empty.

- [ ] **Step 6: Commit.**

```bash
git add platform/developer-guide/docs/custom-apps-development/vc-shell/getting-started/create-your-app.md
git commit -m "docs(vc-shell): document vc-app AI skill in create-your-app"
```

(Use HEREDOC + `Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>`.)

**Report:** Status, word count after addition, slash-command verification result, commit SHA, concerns.

---

## Phase H: Project-style audit batches (4 tasks)

Each H-task follows the same pattern: read the pages in the batch, apply Appendix B audit dimensions, edit in place, commit per page or per coherent batch, return a per-page change summary.

### Task 3: H1 — getting-started/ audit

**Files (review and possibly modify):**

- `platform/developer-guide/docs/custom-apps-development/vc-shell/getting-started/installation.md`
- `platform/developer-guide/docs/custom-apps-development/vc-shell/getting-started/project-structure.md`
- `platform/developer-guide/docs/custom-apps-development/vc-shell/getting-started/connecting-to-platform.md`
- `platform/developer-guide/docs/custom-apps-development/vc-shell/getting-started/first-blade.md`

(The fifth page, `create-your-app.md`, was touched by Task 2 and is excluded from this audit.)

**Per-page directives:**

- For each file, read the full content.
- Apply Appendix B dimensions. Edit in place.
- Pay particular attention to:
  - "Choose between this and an alternative" framing — getting-started pages are imperative tutorials and rarely have decisions, so external comparisons should be absent already.
  - Marketing-speak in any introduction sentences.
  - CLAUDE.md orthography (especially `Frontend` alone, `Virto Commerce` two-words, `Platform` capitalized).

**Steps:**

- [ ] **Step 1: Read all four pages.**

- [ ] **Step 2: For each page with edits needed, apply changes.**

- [ ] **Step 3: Run grep verification across the batch.**

```bash
grep -rniE "quasar|vuetify|strapi|sanity|general.*admin.*kit|pick something else|consider alternatives|blazing|revolutionary|powerful|rich set of|robust" \
  platform/developer-guide/docs/custom-apps-development/vc-shell/getting-started/
```

Expected: only legitimate hits (e.g., `powerful` in a verified API description). Review each.

- [ ] **Step 4: Run mkdocs build, confirm no new warnings.**

```bash
mkdocs build 2>&1 | grep -E "WARNING.*getting-started" | grep -v -F -f /tmp/vc-shell-baseline.txt
```

Expected: empty.

- [ ] **Step 5: Commit per page (only pages with actual changes; skip clean ones).**

```bash
# Example commit shape — repeat per modified file
git add platform/developer-guide/docs/custom-apps-development/vc-shell/getting-started/<file>.md
git commit -m "docs(vc-shell): align <file> with project style"
```

(HEREDOC + Co-Authored-By.)

**Report:** Status, list of pages modified vs untouched, per-page change summary, grep results, commit SHAs.

### Task 4: H2 — concepts/ audit

**Files (review and possibly modify):**

- `platform/developer-guide/docs/custom-apps-development/vc-shell/concepts/blade-navigation.md`
- `platform/developer-guide/docs/custom-apps-development/vc-shell/concepts/modules.md`
- `platform/developer-guide/docs/custom-apps-development/vc-shell/concepts/extensions.md`
- `platform/developer-guide/docs/custom-apps-development/vc-shell/concepts/layout.md`
- `platform/developer-guide/docs/custom-apps-development/vc-shell/concepts/permissions-model.md`
- `platform/developer-guide/docs/custom-apps-development/vc-shell/concepts/localization.md`
- `platform/developer-guide/docs/custom-apps-development/vc-shell/concepts/state-persistence.md`
- `platform/developer-guide/docs/custom-apps-development/vc-shell/concepts/api-clients.md`

**Per-page directives:**

- For each file, read the full content.
- Apply Appendix B dimensions.
- Pay particular attention to:
  - `localization.md` may mention vue-i18n in a comparative way — keep technical mentions, drop "alternatives" language.
  - `api-clients.md` may mention non-Platform APIs — keep technical mentions, ensure no marketing-speak.
  - Concept pages should still open with mental-model paragraphs (do not regress that structure).

**Steps:**

- [ ] **Step 1: Read all eight pages.**

- [ ] **Step 2: For each page with edits needed, apply changes in place.**

- [ ] **Step 3: Run grep verification across the batch.**

```bash
grep -rniE "quasar|vuetify|pinia.*alternative|strapi|sanity|general.*admin.*kit|pick something else|consider alternatives|blazing|revolutionary|powerful|rich set of|robust" \
  platform/developer-guide/docs/custom-apps-development/vc-shell/concepts/
```

Expected: only legitimate hits. Review each.

- [ ] **Step 4: Verify mental model is still present in each concepts H1.**

For each page, confirm the first ~3 paragraphs after the H1 heading are mental-model prose, NOT a code fence.

- [ ] **Step 5: Run mkdocs build, confirm no new warnings.**

```bash
mkdocs build 2>&1 | grep -E "WARNING.*concepts/" | grep -v -F -f /tmp/vc-shell-baseline.txt
```

Expected: empty.

- [ ] **Step 6: Commit per page (only pages with actual changes).**

```bash
git add platform/developer-guide/docs/custom-apps-development/vc-shell/concepts/<file>.md
git commit -m "docs(vc-shell): align concepts/<file> with project style"
```

(HEREDOC + Co-Authored-By.)

**Report:** Status, list of pages modified vs untouched, per-page change summary, grep results, commit SHAs.

### Task 5: H3 — guides/ audit (largest batch)

**Files (review and possibly modify):**

- `platform/developer-guide/docs/custom-apps-development/vc-shell/guides/blades/index.md`
- `platform/developer-guide/docs/custom-apps-development/vc-shell/guides/data/index.md`
- `platform/developer-guide/docs/custom-apps-development/vc-shell/guides/forms/index.md`
- `platform/developer-guide/docs/custom-apps-development/vc-shell/guides/ui/index.md`
- `platform/developer-guide/docs/custom-apps-development/vc-shell/guides/modules-and-extensions/index.md`
- `platform/developer-guide/docs/custom-apps-development/vc-shell/guides/platform/index.md`
- `platform/developer-guide/docs/custom-apps-development/vc-shell/guides/platform/embedded-mode.md`
- `platform/developer-guide/docs/custom-apps-development/vc-shell/guides/platform/auth-pages.md`
- `platform/developer-guide/docs/custom-apps-development/vc-shell/guides/platform/custom-auth.md`
- `platform/developer-guide/docs/custom-apps-development/vc-shell/guides/cookbook/index.md`
- `platform/developer-guide/docs/custom-apps-development/vc-shell/guides/troubleshooting/index.md`
- `platform/developer-guide/docs/custom-apps-development/vc-shell/guides/deployment.md`
- `platform/developer-guide/docs/custom-apps-development/vc-shell/guides/routing.md`
- `platform/developer-guide/docs/custom-apps-development/vc-shell/guides/best-practices.md`

**Per-page directives:**

- For each file, read the full content.
- Apply Appendix B dimensions.
- Pay particular attention to:
  - `ui/index.md` may mention general design systems — keep VC-Shell-internal context only.
  - `best-practices.md` may have anti-patterns that reference external products — review.
  - `custom-auth.md` already documents the v2-honest story (no IAuthProvider) but may have residual "alternative auth providers" framing — keep VC-internal positioning.
  - `auth-pages.md` may compare to "build your own login" — frame inside VC.
  - `forms/index.md` may mention vee-validate — keep technical, drop "alternatives".
  - `data/index.md` may compare VcDataTable to other table libraries — keep VC-internal.
- Recipe pages should keep their recipe structure; only audit for tone, not structure.

**Steps:**

- [ ] **Step 1: Read all 14 pages.**

- [ ] **Step 2: For each page with edits needed, apply changes in place.**

- [ ] **Step 3: Run grep verification across the batch.**

```bash
grep -rniE "quasar|vuetify|pinia.*alternative|strapi|sanity|general.*admin.*kit|pick something else|consider alternatives|blazing|revolutionary|powerful|rich set of|robust|best in class" \
  platform/developer-guide/docs/custom-apps-development/vc-shell/guides/
```

Expected: only legitimate hits.

- [ ] **Step 4: Run mkdocs build, confirm no new warnings.**

```bash
mkdocs build 2>&1 | grep -E "WARNING.*guides/" | grep -v -F -f /tmp/vc-shell-baseline.txt
```

Expected: empty.

- [ ] **Step 5: Commit per page (only pages with actual changes).**

```bash
git add platform/developer-guide/docs/custom-apps-development/vc-shell/guides/<path>.md
git commit -m "docs(vc-shell): align guides/<path> with project style"
```

(HEREDOC + Co-Authored-By.)

**Report:** Status, list of pages modified vs untouched, per-page change summary (especially for `ui/index.md`, `best-practices.md`, `custom-auth.md`, `auth-pages.md`, `forms/index.md`, `data/index.md`), grep results, commit SHAs.

### Task 6: H4 — reference/migration/ audit

**Files (review and possibly modify):**

- `platform/developer-guide/docs/custom-apps-development/vc-shell/reference/migration/index.md`

**Per-page directives:**

- Read the full content.
- Apply Appendix B dimensions.
- Pay particular attention to:
  - Migration pages often quote tooling from external sources; verify each external mention is technical-context only, not "alternatives".
  - CLAUDE.md compliance for any version numbers, file references, etc.

**Steps:**

- [ ] **Step 1: Read the page.**

- [ ] **Step 2: Apply edits if needed.**

- [ ] **Step 3: Run grep verification.**

```bash
grep -niE "quasar|vuetify|pinia.*alternative|strapi|sanity|general.*admin.*kit|pick something else|consider alternatives|blazing|revolutionary|powerful|rich set of|robust" \
  platform/developer-guide/docs/custom-apps-development/vc-shell/reference/migration/index.md
```

Expected: only legitimate hits.

- [ ] **Step 4: Run mkdocs build, confirm no new warnings.**

```bash
mkdocs build 2>&1 | grep -E "WARNING.*reference/migration" | grep -v -F -f /tmp/vc-shell-baseline.txt
```

Expected: empty.

- [ ] **Step 5: Commit (only if changes were made).**

```bash
git add platform/developer-guide/docs/custom-apps-development/vc-shell/reference/migration/index.md
git commit -m "docs(vc-shell): align reference/migration with project style"
```

(HEREDOC + Co-Authored-By.)

**Report:** Status (DONE or SKIP), changes applied, grep results, commit SHA.

---

## Task 7: Final verification

**Files:**
- None (read-only verification).

- [ ] **Step 1: Full mkdocs build, confirm no new warnings on any vc-shell page.**

```bash
mkdocs build 2>&1 | grep -E "WARNING.*custom-apps-development/vc-shell" > /tmp/vc-shell-final.txt
diff /tmp/vc-shell-baseline.txt /tmp/vc-shell-final.txt
```

Expected: no diff.

- [ ] **Step 2: Confirm no external-product comparisons remain.**

```bash
grep -rniE "quasar|vuetify|pinia.*alternative|strapi|sanity|general.*admin.*kit|pick something else|consider alternatives" \
  platform/developer-guide/docs/custom-apps-development/vc-shell/ | grep -v "/components/" | grep -v "/composables/" | grep -v "/plugins/" | grep -v "/reference/api/" | grep -v "/reference/modules/"
```

Expected: empty (or only legitimate technical mentions like vee-validate as integration partner).

- [ ] **Step 3: Confirm vc-app skill is documented.**

```bash
grep -ln "vc-app-skill" platform/developer-guide/docs/custom-apps-development/vc-shell/getting-started/create-your-app.md
```

Expected: file path returned.

- [ ] **Step 4: Confirm no marketing-speak.**

```bash
grep -rniE "blazing|revolutionary|best in class" \
  platform/developer-guide/docs/custom-apps-development/vc-shell/ | grep -v "/components/" | grep -v "/composables/" | grep -v "/plugins/" | grep -v "/reference/api/" | grep -v "/reference/modules/"
```

Expected: empty.

- [ ] **Step 5: Confirm style spec invariants still hold.**

```bash
# No collapsibles
grep -rnE "^\?\?\?" platform/developer-guide/docs/custom-apps-development/vc-shell/{introduction,getting-started,concepts,guides,reference/migration}/

# No "When to read this"
grep -rln "When to read this" platform/developer-guide/docs/custom-apps-development/vc-shell/

# No custom HTML prev/next footer
grep -rnE 'display: flex.*justify-content: space-between' platform/developer-guide/docs/custom-apps-development/vc-shell/
```

Expected: all three return empty.

- [ ] **Step 6: Confirm CLAUDE.md orthography spot-check.**

```bash
# Should NOT find "Virto-Commerce" hyphenated
grep -rln "Virto-Commerce" platform/developer-guide/docs/custom-apps-development/vc-shell/

# Should NOT find "storefront" used as a synonym for Frontend (case-insensitive, but exclude legitimate uses about the storefront product itself)
grep -rln "storefront" platform/developer-guide/docs/custom-apps-development/vc-shell/{introduction,getting-started,concepts}/
```

Expected: first returns empty. Second may have legitimate hits — review each.

No commit at this step.

---

## Self-review notes

Spec coverage:

- Spec section 2 (ecosystem-framing rule) → enforced in Appendix A and Appendix B and applied in every H-task.
- Spec section 3 Stream 1 → Task 1 (Phase F).
- Spec section 3 Stream 2 → Task 2 (Phase G).
- Spec section 3 Stream 3 H1-H4 → Tasks 3-6 (Phase H).
- Spec section 5 acceptance criteria → Task 7 final verification.
- Spec section 7 verification commands → executed verbatim in Task 7.

No placeholders: every task lists exact file paths, replacement content (where prescribed), exact verification commands, and exact commit messages.

Type consistency: not applicable to documentation work; all string identifiers (slash command names, file paths, tagline text) match the spec verbatim.
