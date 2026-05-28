# VC-Shell Narrative Documentation Style — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Audit and rewrite the 12 already-written VC-Shell narrative pages under the style locked in the design spec, then author the 14 remaining placeholder pages by the same rules. End state: 26 pages, mkdocs build clean, each page passes the audit checklist.

**Architecture:** Two-phase. Phase 1 rewrites the 12 existing pages against the audit checklist, fixing the four known systemic issues (`When to read this`, `??? collapsible`, custom HTML prev/next footer, code-first concepts). Phase 2 writes the 14 placeholder pages from scratch using the archetype skeletons. Each page is one commit so reviewers can isolate problems.

**Tech Stack:** mkdocs, mkdocs-material (mermaid, admonitions, code titles, hl_lines, attr_list, md_in_html, pymdownx.superfences via existing `mkdocs.yml`).

**Reference spec:** `docs/superpowers/specs/2026-05-13-vc-shell-narrative-style-design.md`.

**Source repo for verification:** `/Users/symbot/DEV/vc-shell-main-dev/vc-shell/`.

---

## Files

All 26 pages already exist. Phase 1 modifies 12 written pages. Phase 2 replaces 14 placeholders (`Content coming soon — see vc-shell repo until this section is filled out.`).

Target root: `platform/developer-guide/docs/custom-apps-development/vc-shell/`.

**Phase 1 (audit + rewrite):**

- `introduction/index.md`
- `introduction/what-is-vc-shell.md`
- `introduction/architecture-overview.md`
- `introduction/when-to-use.md`
- `getting-started/installation.md`
- `getting-started/create-your-app.md`
- `getting-started/project-structure.md`
- `getting-started/connecting-to-platform.md`
- `getting-started/first-blade.md`
- `concepts/blade-navigation.md`
- `concepts/modules.md`
- `concepts/api-clients.md`

**Phase 2 (write from placeholder):**

- `concepts/extensions.md`
- `concepts/layout.md`
- `concepts/permissions-model.md`
- `concepts/localization.md`
- `concepts/state-persistence.md`
- `guides/blades/index.md`
- `guides/data/index.md`
- `guides/forms/index.md`
- `guides/ui/index.md`
- `guides/modules-and-extensions/index.md`
- `guides/platform/index.md`
- `guides/cookbook/index.md`
- `guides/troubleshooting/index.md`
- `reference/migration/index.md`

---

## Appendix A: Archetype skeletons

Reproduced verbatim from spec section 2 so tasks can be executed without flipping documents.

### A.1 introduction archetype

```text
# <Title>

<1-line tagline.>

<2-3 paragraphs of mental model.>

<Diagram (mermaid for structural; PNG for screenshots).>

## <Sub-concept 1>

<Prose. May include a comparison table for positioning pages.>

## <Sub-concept 2>

<Prose, optionally a single code or CLI block.>

![Readmore](relative/path.md){: width="25"} Inline cross-link.
```

No code blocks except a single CLI command on `index.md`. Length 200–600 words.

### A.2 getting-started archetype

```text
# <Title>

<1-line goal sentence.>

## Prerequisites

Before <verb-ing>, make sure you have:

- <item>.
- <item>.

## <Imperative step name>

<1-2 sentences of context.>

```bash title="..."
command
```

## <Next step>

<context + code>

## Verify

<bullet list of expected outcomes>

## Troubleshooting

!!! warning "Symptom"
    Cause and fix.
```

Imperative voice in section headings. Troubleshooting items are `!!! warning` admonitions, not a table. Length 300–900 words.

### A.3 concepts archetype

```text
# <Title>

<1-line statement of what this concept is.>

<2-3 paragraphs of mental model.>

```mermaid
<structural diagram>
```

## <Sub-concept 1>

<Prose paragraph explaining the why.>

<Code or table.>

## <Sub-concept 2>

<Prose-led.>

```vue title="src/modules/orders/pages/OrdersList.vue"
<real code adapted from vendor-portal>
```

!!! tip
    Inline tip.

![Readmore](../composables/.../X.md){: width="25"} Full API reference.

## Common patterns

<Table or 2-3 H3 subsections with prose-led code.>

## Common mistakes

!!! warning "Mistake description"
    Why it happens. How to fix.
```

Mental model mandatory in the first 2-3 paragraphs. Every H2 opens with prose, then code. Length 600–1200 words.

### A.4 guides archetype

```text
# <Title>

<1-line goal.>

## Prerequisites

<List.>

## <Recipe 1>

<1-paragraph context.>

```vue title="..."
real code
```

<Short prose elaborating.>

## <Recipe 2>

...

## Variations

<Table: variation -> change to make.>

![Readmore] cross-links.
```

3–6 recipes per page. Length 500–1200 words.

### A.5 reference/migration archetype

```text
# Migration

<Intro paragraph.>

## v1 → v2

### Breaking changes

<Bullet list.>

### Codemods

```bash
npx @vc-shell/migrate v1-to-v2
```

### Manual changes

<Table: feature -> what to do.>

## v2 → v3

...
```

One H2 per major version. Length 400+ words per major bump.

---

## Appendix B: Style invariants

- `!!! note`, `!!! tip`, `!!! warning`, `!!! info` only. Never `??? note` (collapsible).
- Code blocks use `title="<file path>" linenums="1" hl_lines="X Y"` where appropriate.
- Diagrams: mermaid for structural, PNG (in `media/`) for screenshots.
- Cross-links inline via `![Readmore](path){: width="25"} <Title>`. No custom HTML prev/next footer.
- No `Next steps` section at page end (mkdocs renders prev/next automatically).
- Second-person, present tense, active voice. Imperative in headings.
- Verify every Vc-class against vc-shell source before naming it in code.
- First mention of a framework concept is bolded.

CLAUDE.md continues to apply: "Virto Commerce" (two words), "Platform" capitalized when referring to VC Platform, "Frontend" alone, sentences end with periods including in tables and list items.

---

## Appendix C: Audit checklist

Each rewritten or new page passes all 13 items:

1. Tone anchor matches archetype.
2. Opens with 1-line statement; concepts add 2-3 paragraphs of mental model.
3. Diagram present when structural.
4. Concepts: every H2 opens with prose, not code.
5. Code blocks have `title=`.
6. No `When to read this` section.
7. No `??? collapsible` blocks.
8. Inline `![Readmore]` links present where reader needs deeper material.
9. No custom HTML prev/next footer.
10. All Vc-types verified against vc-shell source.
11. Framework internals absent on application-developer pages.
12. Length within archetype range.
13. Code adapted from `apps/vendor-portal/` where applicable.

---

## Task 0: Baseline check

**Files:**
- None (read-only).

- [ ] **Step 1: Run mkdocs build and capture warnings**

```bash
mkdocs build 2>&1 | grep -E "WARNING.*custom-apps-development/vc-shell" > /tmp/vc-shell-baseline-warnings.txt
wc -l /tmp/vc-shell-baseline-warnings.txt
```

Expected: a line count > 0 of pre-existing warnings unrelated to this plan (these will be ignored when verifying later tasks; only new ones matter).

- [ ] **Step 2: Confirm vc-shell source repo is available**

```bash
test -d /Users/symbot/DEV/vc-shell-main-dev/vc-shell/framework && echo "OK"
```

Expected: `OK`.

- [ ] **Step 3: Confirm spec file is in place**

```bash
test -f /Users/symbot/DEV/vc-docs/docs/superpowers/specs/2026-05-13-vc-shell-narrative-style-design.md && echo "OK"
```

Expected: `OK`.

No commit at this step.

---

## Phase 1: Audit and rewrite 12 existing pages

Each Phase 1 task follows the same shape:

1. Read current page.
2. Apply targeted fixes listed in the task (the systemic issues are known from spec section 6).
3. Apply Appendix C checklist.
4. Run `mkdocs build`, confirm no new warnings on the modified file.
5. Commit with the message shown.

### Task 1: introduction/index.md

**File:** `platform/developer-guide/docs/custom-apps-development/vc-shell/introduction/index.md`.

**Archetype:** introduction (Appendix A.1).

**Targeted fixes:**

- Confirm page opens with 1-line tagline and 2-3 mental-model paragraphs (positioning).
- Drop `## Next` section if present.
- Add inline `![Readmore]` cross-links where they help: after the tagline (→ `what-is-vc-shell.md`), after "What you build with it" (→ `architecture-overview.md`), after Storybook embed (→ `../getting-started/installation.md`).
- Keep the single CLI install block.
- Keep the Storybook iframe inside `<div class="vc-storybook-embed">`.

- [ ] **Step 1: Read the current file**

```bash
cat platform/developer-guide/docs/custom-apps-development/vc-shell/introduction/index.md
```

- [ ] **Step 2: Edit per targeted fixes**

Apply the changes. Resulting H2 list: `What you build with it`, `Live components`. No `Next` section.

- [ ] **Step 3: Run mkdocs build, confirm no new warnings on this file**

```bash
mkdocs build 2>&1 | grep "introduction/index" | grep -v -F -f /tmp/vc-shell-baseline-warnings.txt
```

Expected: empty output.

- [ ] **Step 4: Commit**

```bash
git add platform/developer-guide/docs/custom-apps-development/vc-shell/introduction/index.md
git commit -m "docs(vc-shell): align introduction/index with narrative style spec"
```

### Task 2: introduction/what-is-vc-shell.md

**File:** `platform/developer-guide/docs/custom-apps-development/vc-shell/introduction/what-is-vc-shell.md`.

**Archetype:** introduction.

**Targeted fixes:**

- Drop the closing "How to decide" paragraph; the comparison table makes the decision.
- Keep the "What you get" table.
- Keep the "How it compares" cross-platform table.
- Trim "What it is not" to 3 bullets, each paired with a concrete alternative (CMS → "use Strapi/Sanity"; admin template → "use Quasar"; Platform manager → "extend the bundled manager"). Drop bullets without an alternative.
- Replace any inline `**Important:**` / `**Tip:**` with `!!! note` / `!!! tip` admonitions if any are present.
- Drop trailing `## Next` section if present.

- [ ] **Step 1: Read the current file**

```bash
cat platform/developer-guide/docs/custom-apps-development/vc-shell/introduction/what-is-vc-shell.md
```

- [ ] **Step 2: Edit per targeted fixes**

- [ ] **Step 3: Verify length is 400–600 words**

```bash
wc -w platform/developer-guide/docs/custom-apps-development/vc-shell/introduction/what-is-vc-shell.md
```

Expected: between 400 and 600 words.

- [ ] **Step 4: Run mkdocs build, confirm no new warnings**

- [ ] **Step 5: Commit**

```bash
git commit -am "docs(vc-shell): tighten what-is-vc-shell to spec"
```

### Task 3: introduction/architecture-overview.md

**File:** `.../introduction/architecture-overview.md`.

**Archetype:** introduction.

**Targeted fixes:**

- Replace the `??? note "Framework bootstrap sequence"` collapsible with a regular `## Framework bootstrap` H2 containing the numbered list, OR move the content to a single paragraph "Bootstrap is sequential: theme registration, fetch interceptors, i18n, services, blade registry, plugins, error handlers, router guards. Authoritative source: framework/index.ts." Pick the second form to keep page length down.
- Drop the `## Next` section at the end.
- Add inline `![Readmore]` cross-links: after the layer table (→ `../concepts/blade-navigation.md`), after the module-model section (→ `../concepts/modules.md`), after the MF section (→ `../concepts/api-clients.md` is wrong — link to the MF source instead, since there is no concepts page for MF).
- Keep the mermaid layered diagram, keep the source-of-truth table.

- [ ] **Step 1: Read the current file**

- [ ] **Step 2: Edit per targeted fixes**

- [ ] **Step 3: Verify the `???` (collapsible) syntax is gone**

```bash
grep "^???" platform/developer-guide/docs/custom-apps-development/vc-shell/introduction/architecture-overview.md
```

Expected: empty output.

- [ ] **Step 4: Run mkdocs build, confirm no new warnings**

- [ ] **Step 5: Commit**

```bash
git commit -am "docs(vc-shell): inline architecture bootstrap and remove collapsible"
```

### Task 4: introduction/when-to-use.md

**File:** `.../introduction/when-to-use.md`.

**Archetype:** introduction.

**Targeted fixes:**

- Keep the page largely as-is; it already follows the archetype.
- Drop trailing `## Next` section.
- Verify the trade-off table cells end with periods (CLAUDE.md rule).

- [ ] **Step 1: Read and verify**

- [ ] **Step 2: Drop `## Next` if present**

- [ ] **Step 3: Run mkdocs build**

- [ ] **Step 4: Commit**

```bash
git commit -am "docs(vc-shell): when-to-use polish to spec"
```

### Task 5: getting-started/installation.md

**File:** `.../getting-started/installation.md`.

**Archetype:** getting-started (Appendix A.2).

**Targeted fixes:**

- Drop trailing `## Next` section.
- Ensure section headings are imperative: `Prerequisites`, `Scaffold`, `Install dependencies`, `Configure the Platform URL`, `Run`, `Troubleshooting`.
- Troubleshooting items already use `!!! warning` admonitions — keep.
- No `Verify` section needed; the dev server URL is the verification.

- [ ] **Step 1: Read, apply edits**

- [ ] **Step 2: Run mkdocs build**

- [ ] **Step 3: Commit**

```bash
git commit -am "docs(vc-shell): installation polish to spec"
```

### Task 6: getting-started/create-your-app.md

**File:** `.../getting-started/create-your-app.md`.

**Archetype:** getting-started.

**Targeted fixes:**

- Drop trailing `## Next` section.
- Verify imperative section headings.

- [ ] **Step 1: Read, apply edits**

- [ ] **Step 2: Commit**

```bash
git commit -am "docs(vc-shell): create-your-app polish to spec"
```

### Task 7: getting-started/project-structure.md

**File:** `.../getting-started/project-structure.md`.

**Archetype:** getting-started (but content-wise it is reference-like — tables and trees).

**Targeted fixes:**

- Drop trailing `## Next` section.
- Verify all section headings (`Top level`, `src/`, `Inside a module`, `Where things go`, `Conventions`) are descriptive.

- [ ] **Step 1: Apply edits**

- [ ] **Step 2: Commit**

```bash
git commit -am "docs(vc-shell): project-structure polish to spec"
```

### Task 8: getting-started/connecting-to-platform.md

**File:** `.../getting-started/connecting-to-platform.md`.

**Archetype:** getting-started.

**Targeted fixes:**

- Replace the `??? note "How authentication works"` collapsible with a regular `## How authentication works` H2 containing the 4-step numbered list. The reader benefits from seeing it inline.
- Drop trailing `## Next` section.

- [ ] **Step 1: Apply edits**

- [ ] **Step 2: Verify `???` is gone**

```bash
grep "^???" platform/developer-guide/docs/custom-apps-development/vc-shell/getting-started/connecting-to-platform.md
```

Expected: empty.

- [ ] **Step 3: Commit**

```bash
git commit -am "docs(vc-shell): connecting-to-platform — inline auth section, drop collapsible"
```

### Task 9: getting-started/first-blade.md

**File:** `.../getting-started/first-blade.md`.

**Archetype:** getting-started.

**Targeted fixes:**

- Drop trailing `## Next` section.
- Verify the tutorial flows: module layout → blade → locale → module entry → install → run → troubleshooting → what to try next.
- "What to try next" is allowed in tutorials (not the same as a generic "Next steps" link list).

- [ ] **Step 1: Apply edits**

- [ ] **Step 2: Commit**

```bash
git commit -am "docs(vc-shell): first-blade polish to spec"
```

### Task 10: concepts/blade-navigation.md

**File:** `.../concepts/blade-navigation.md`.

**Archetype:** concepts (Appendix A.3) — this is the load-bearing one for the spec.

**Targeted fixes:**

- The current page opens code-first. Insert mental-model paragraphs immediately after the title:

  > A blade is a vertical panel pushed onto a stack. Opening a new blade slides it in from the right; closing it slides it back out.
  >
  > The pattern (popularized by the Azure Portal) preserves context across drill-downs: opening a details panel does not unmount the list, so the user can compare list and details side by side instead of losing search state on every click. Each blade has at most one active child, so the navigation history is linear but branchable; a URL captures the whole stack, so the browser back button restores the workspace and all open child blades. The framework owns the header, toolbar slot, banners, and close button — blade authors only write the body.
  >
  > Three primitives back the system: `useBladeStack` is the state machine; `useBladeMessaging` is the parent-child method dispatcher; `useBlade()` is the everyday composable that wraps both and works inside and outside blade context.

- Keep the existing mermaid stack diagram.
- Keep the operations table, `useBlade()` section, passing-data section, messaging section, close-guards section, common-patterns section, URL sync section, common-mistakes admonitions.
- Drop trailing `## Next` section.
- Add inline `![Readmore]` cross-links where reference deep-dives exist (`../composables/blade-navigation/useBlade.md`, `../composables/blade-navigation/blade-nav-composables.md`).

- [ ] **Step 1: Insert mental-model paragraphs at the top, immediately after the title**

- [ ] **Step 2: Verify every H2 opens with prose**

Read through each H2 section. The first non-whitespace line after each `## ` heading must be a paragraph of prose, not a code fence.

- [ ] **Step 3: Drop trailing `## Next` section**

- [ ] **Step 4: Add inline `![Readmore]` after `useBlade()` section**

```markdown
![Readmore](../composables/blade-navigation/useBlade.md){: width="25"} Full `useBlade` reference.
```

- [ ] **Step 5: Verify length 600–1200 words**

```bash
wc -w platform/developer-guide/docs/custom-apps-development/vc-shell/concepts/blade-navigation.md
```

- [ ] **Step 6: Run mkdocs build, confirm no new warnings**

- [ ] **Step 7: Commit**

```bash
git commit -am "docs(vc-shell): restore mental model in concepts/blade-navigation"
```

### Task 11: concepts/modules.md

**File:** `.../concepts/modules.md`.

**Archetype:** concepts.

**Targeted fixes:**

- The current page opens with code. Insert mental-model paragraphs:

  > A module is the unit of feature packaging in VC-Shell: a self-contained Vue plugin that bundles blades, routes, menu items, notification handlers, and translations for one bounded subdomain.
  >
  > Modules exist to make features composable. A standalone app bundles its modules at build time. A host app loads remote modules at runtime via Module Federation, with semver compatibility filtering. Either way, the host calls `app.use(myModule)` and the module's install function registers blades in the `BladeRegistry`, creates routes, attaches menu items, registers notification types, and merges locale bundles. Two modules never import from each other directly — cross-module wiring runs through extension points or the menu service.

- Keep the existing API table, lifecycle section, blade static properties table, notifications section, locales section, recipes, when-to-split section, MF section, common-mistakes admonitions.
- Drop trailing `## Next` section.
- Add inline `![Readmore]` to `../plugins/modularity.md` next to the lifecycle/notifications sections.

- [ ] **Step 1: Insert mental-model paragraphs at the top**

- [ ] **Step 2: Verify every H2 opens with prose**

- [ ] **Step 3: Drop trailing `## Next`**

- [ ] **Step 4: Run mkdocs build**

- [ ] **Step 5: Commit**

```bash
git commit -am "docs(vc-shell): restore mental model in concepts/modules"
```

### Task 12: concepts/api-clients.md

**File:** `.../concepts/api-clients.md`.

**Archetype:** concepts.

**Targeted fixes:**

- The current page is code-only after the last revision. Restore mental model:

  > VC-Shell apps talk to a Virto Commerce Platform through typed clients generated from the Platform's OpenAPI documents. The generator (`@vc-shell/api-client-generator`) emits one TypeScript class per Platform module under `src/api_client/`; each class carries the type definitions for every request, response, and search query.
  >
  > Application code never instantiates these classes directly. The `useApiClient(ClientCtor)` composable returns an async factory that resolves to a configured, authenticated client — base URL filled in from `APP_PLATFORM_URL`, OAuth token attached, token refresh handled automatically. The factory is paired with `useAsync` to provide loading and error refs that flow into `<VcBlade :loading>`, `<VcButton :loading>`, and error banners.
  >
  > The standard composable shape across vendor-portal modules is: import the client class, call `useApiClient(ClientCtor)`, wrap each operation in `useAsync`, expose `items`, `loading`, and the action functions. Pagination plugs in via `useDataTablePagination`; sort strings come from `useTableSort`.

- Keep the quick-start code example, the `getApiClient` async warning, the CRUD pattern, the multiple-clients alias section, the search/pagination section, the generate-clients section.
- Drop the trailing `## Next` section.
- Add inline `![Readmore]` to `../composables/data/useApiClient.md` after the quick-start code.

- [ ] **Step 1: Insert the three mental-model paragraphs at the top**

- [ ] **Step 2: Verify every H2 opens with prose**

- [ ] **Step 3: Drop trailing `## Next`**

- [ ] **Step 4: Verify the page does not mention `IAuthApiBase`, fetch interceptors, or token-refresh mechanics**

```bash
grep -E "IAuthApiBase|fetch interceptor|token refresh|vc_auth_data" platform/developer-guide/docs/custom-apps-development/vc-shell/concepts/api-clients.md
```

Expected: empty output.

- [ ] **Step 5: Run mkdocs build**

- [ ] **Step 6: Commit**

```bash
git commit -am "docs(vc-shell): restore mental model in concepts/api-clients"
```

---

## Phase 2: Write the 14 placeholder pages

Each Phase 2 task follows this shape:

1. Read source materials in `/Users/symbot/DEV/vc-shell-main-dev/vc-shell/` (paths listed per task).
2. Confirm reference docs exist in vc-docs at the linked paths (so `![Readmore]` cross-links resolve).
3. Replace the "Content coming soon" placeholder with content built from the archetype skeleton in Appendix A.
4. Apply audit checklist (Appendix C).
5. Run `mkdocs build`, confirm no new warnings.
6. Commit.

### Task 13: concepts/extensions.md

**File:** `.../concepts/extensions.md`.

**Archetype:** concepts.

**Source materials to read first:**

- `vc-shell:framework/core/plugins/extension-points/extension-points.docs.md`.
- `vc-shell:framework/core/plugins/extension-points/defineExtensionPoint.ts`.
- `vc-shell:framework/core/plugins/extension-points/useExtensionPoint.ts`.
- `vc-shell:framework/core/plugins/extension-points/store.ts`.

**Existing reference page in vc-docs (for `![Readmore]`):**

- `../plugins/extension-points.md`.

**Mental model to communicate (first 2-3 paragraphs):**

- Extension points are the framework's answer to "how does module A let module B inject UI into A without A knowing B exists at build time."
- The host blade declares a named slot with `defineExtensionPoint("id")`; consumer modules register components against the slot with `useExtensionPoint("id").register({ id, component, priority })`. Registration is order-independent — modules may register before the host declares the slot. The host receives a reactive, priority-sorted list.
- Distinguish from `<slot>` (compile-time, same-file) and from `provide/inject` (component-tree-scoped). Extension points are app-scoped and runtime-registered.

**H2 outline:**

- `## Host: declaring an extension point` — `defineExtensionPoint`, `<ExtensionPoint name="..." />` rendering.
- `## Consumer: registering a component` — `useExtensionPoint("id").register({ id, component, priority })`.
- `## Add, replace, remove` — module-side modifiers (`add`, `replace`, `remove`).
- `## Priority and ordering` — how the priority-sorted list works.
- `## Real example: customizing seller-details with marketplace-commissions` — adapt the recipe from the modularity docs (`framework/core/plugins/modularity/modularity.docs.md` "Module Extending Another Module" recipe).
- `## Common mistakes` — `!!! warning` admonitions: forgetting `priority`, name collisions, registering on a non-existent slot (it silently waits), referencing the host's reactive data without `inject`.

**Steps:**

- [ ] **Step 1: Read source materials**

```bash
cat /Users/symbot/DEV/vc-shell-main-dev/vc-shell/framework/core/plugins/extension-points/extension-points.docs.md
cat /Users/symbot/DEV/vc-shell-main-dev/vc-shell/framework/core/plugins/extension-points/defineExtensionPoint.ts
cat /Users/symbot/DEV/vc-shell-main-dev/vc-shell/framework/core/plugins/extension-points/useExtensionPoint.ts
```

- [ ] **Step 2: Confirm reference page exists**

```bash
test -f platform/developer-guide/docs/custom-apps-development/vc-shell/plugins/extension-points.md && echo OK
```

- [ ] **Step 3: Write the page using the concepts skeleton (Appendix A.3) and the outline above**

- [ ] **Step 4: Verify length 600–1200 words and mental model is in place**

- [ ] **Step 5: Run mkdocs build**

- [ ] **Step 6: Commit**

```bash
git commit -am "docs(vc-shell): write concepts/extensions"
```

### Task 14: concepts/layout.md

**File:** `.../concepts/layout.md`.

**Archetype:** concepts.

**Source materials:**

- `vc-shell:framework/shell/` (top-level structure).
- `vc-shell:framework/ui/components/organisms/vc-app/` (app shell component).
- `vc-shell:framework/ui/components/organisms/vc-app/vc-app.vue`.
- `vc-shell:framework/ui/components/organisms/vc-app/composables/useShellLifecycle.ts`.
- `vc-shell:framework/assets/styles/theme/` for theming.

**Reference page in vc-docs:**

- `../components/layout/vc-app.md` (auto-synced).

**Mental model:**

- VC-Shell ships a complete app shell — top bar, sidebar, blade area, dashboard, settings, search — composed by `VcApp`. Apps customize the chrome by registering items through services (`addMenuItem`, `registerDashboardWidget`) and by theming via CSS custom properties — not by editing `VcApp` itself.
- Responsiveness is built in: mobile and desktop variants are provided as separate component paths within the shell. The `useShellLifecycle` composable coordinates app readiness (`isReady` prop on `VcApp`).
- Theming flows through SCSS custom properties under `framework/assets/styles/theme/`. Apps override the variables in their own SCSS layer.

**H2 outline:**

- `## The app chrome` — what `VcApp` renders, slot map.
- `## Customizing the menu` — `addMenuItem` from `bootstrap.ts`, `defineBlade({ menuItem })`.
- `## Theme and branding` — CSS custom properties, `tailwind.config.ts` extension, where to override.
- `## Mobile vs desktop` — `useResponsive`, where layout switches happen.
- `## Common mistakes` — replacing `VcApp` (do not), forgetting `markRaw` on widget components, theme overrides scoped too narrowly.

**Steps:**

- [ ] **Step 1: Read source materials**

- [ ] **Step 2: Confirm reference page exists**

- [ ] **Step 3: Write the page**

- [ ] **Step 4: Run mkdocs build**

- [ ] **Step 5: Commit**

```bash
git commit -am "docs(vc-shell): write concepts/layout"
```

### Task 15: concepts/permissions-model.md

**File:** `.../concepts/permissions-model.md`.

**Archetype:** concepts.

**Source materials:**

- `vc-shell:framework/core/plugins/permissions/permissions.docs.md`.
- `vc-shell:framework/core/plugins/permissions/` (source files).
- vc-platform user-guide section on role-based access for context (look up via vc-docs `platform/user-guide` if relevant).

**Reference page in vc-docs:**

- `../plugins/permissions.md`.

**Mental model:**

- Permissions are string identifiers (`seller:orders:view`, `catalog:product:edit`) granted by Platform roles. VC-Shell consumes them through `$hasAccess` (global property) and `usePermissions()` (composable).
- Blade-level gating is declarative: `defineBlade({ permissions: ["seller:orders:view"] })` makes the route blocked and the menu item hidden when the user lacks the permission.
- Component-level gating is done with `usePermissions()` or `$hasAccess` in templates. Both check against the user's permission set loaded from the Platform.
- Server-side enforcement is the source of truth — UI gating is for UX only. The Platform's API rejects unauthorized calls regardless of UI state.

**H2 outline:**

- `## Permission strings` — naming convention, source (Platform OAuth scopes / roles).
- `## Blade-level gating` — `defineBlade({ permissions })`, automatic route + menu visibility.
- `## Component-level gating` — `usePermissions()`, `$hasAccess`, v-if patterns.
- `## Working with multiple permissions` — AND/OR composition.
- `## Server-side is the source of truth` — `!!! warning` admonition that UI gates are advisory.
- `## Common mistakes` — relying on UI gating for security, mismatched permission string vs Platform role, forgetting permissions on the `menuItem` override.

**Steps:**

- [ ] **Step 1: Read `permissions.docs.md`**

- [ ] **Step 2: Confirm reference page exists**

- [ ] **Step 3: Write the page**

- [ ] **Step 4: Run mkdocs build**

- [ ] **Step 5: Commit**

```bash
git commit -am "docs(vc-shell): write concepts/permissions-model"
```

### Task 16: concepts/localization.md

**File:** `.../concepts/localization.md`.

**Archetype:** concepts.

**Source materials:**

- `vc-shell:framework/core/plugins/i18n/i18n.docs.md`.
- `vc-shell:framework/core/plugins/i18n/` source files.
- Sample locale bundles in `vc-shell:cli/create-vc-app/src/templates/sample-module/locales/en.json`.

**Reference page in vc-docs:**

- `../plugins/i18n.md`.

**Mental model:**

- VC-Shell uses `vue-i18n`. The framework's `vue-i18n` instance is created during plugin install; modules merge their locale bundles into the global instance via `defineAppModule({ locales: { en, de } })`.
- Locale keys are namespaced under the module's name (`ORDERS.PAGES.LIST.TITLE`) to prevent cross-module collisions. The framework merges shallow per language code.
- Runtime locale switching goes through `useLanguages()` (`setLocale`, `currentLocale`). The locale is persisted in `localStorage`; on next load, `useLanguages` resolves the user's preference, then falls back to `APP_I18N_LOCALE` from env.

**H2 outline:**

- `## Setting up locale bundles` — file layout, JSON shape.
- `## Namespacing` — why and how, with one warning admonition about collisions.
- `## Using translations` — `$t` in templates, `useI18n({ useScope: "global" })` in scripts, `defineBlade({ menuItem: { title: "KEY" } })`.
- `## Switching the language at runtime` — `useLanguages()`.
- `## Pluralization and number/date formats` — vue-i18n features that work.
- `## Common mistakes` — missing namespace, hard-coded strings in `defineBlade`, forgetting to export the language from `locales/index.ts`.

**Steps:**

- [ ] **Step 1: Read i18n.docs.md**

- [ ] **Step 2: Write the page**

- [ ] **Step 3: Run mkdocs build**

- [ ] **Step 4: Commit**

```bash
git commit -am "docs(vc-shell): write concepts/localization"
```

### Task 17: concepts/state-persistence.md

**File:** `.../concepts/state-persistence.md`.

**Archetype:** concepts.

**Source materials:**

- `vc-shell:framework/ui/components/organisms/vc-data-table/composables/useDataTableState.ts`.
- `vc-shell:framework/ui/components/organisms/vc-data-table/` README or `*.docs.md` if present.

**Reference page in vc-docs:**

- `../components/data-display/vc-data-table.md`.

**Mental model:**

- VC-Shell persists data-table state — column widths, column order, hidden columns, sort, filters — to browser storage so that the user's table layout survives reloads.
- Keying: the `state-key` prop on `VcDataTable` becomes the storage namespace. Storage key format: `VC_DATATABLE_${stateKey.toUpperCase()}`.
- Backend choice: `localStorage` by default; `sessionStorage` opt-in.
- Persistence is opt-out: leave `state-key` unset and the table renders stateless.

**H2 outline:**

- `## What gets persisted` — bullet list.
- `## Storage backends` — local vs session, when to pick each.
- `## Keying convention` — `state-key`, the resulting storage key, namespace strategy.
- `## Disabling persistence` — omit `state-key`.
- `## Schema migration` — what happens when columns change (storage holds stale ids), how to bump the `state-key` to invalidate.
- `## Common mistakes` — duplicate `state-key` across blades, leaking sensitive filters into localStorage, forgetting to update `state-key` on schema change.

**Steps:**

- [ ] **Step 1: Read `useDataTableState.ts`**

- [ ] **Step 2: Write the page**

- [ ] **Step 3: Run mkdocs build**

- [ ] **Step 4: Commit**

```bash
git commit -am "docs(vc-shell): write concepts/state-persistence"
```

### Task 18: guides/blades/index.md

**File:** `.../guides/blades/index.md`.

**Archetype:** guides (Appendix A.4).

**Source materials:**

- `vc-shell:apps/vendor-portal/src/modules/orders/pages/` for list and details blade examples.
- `vc-shell:cli/create-vc-app/src/templates/sample-module/pages/list.vue` and `details.vue`.
- `vc-shell:framework/ui/components/organisms/vc-blade/` for `VcBlade` props.

**H2 outline (5 recipes):**

- `## Recipe: list blade with VcDataTable` — workspace blade, `useApiClient` + `useAsync`, `useDataTablePagination`. Adapt `useOrdersListNew.ts`.
- `## Recipe: details blade with form` — child blade, `param`, save/cancel toolbar, `callParent("reload")`. Adapt `useOrderDetailsNew.ts`.
- `## Recipe: wizard blade` — multi-step using `openBlade` per step, returning data via `callParent`.
- `## Recipe: confirmation blade` — modal-like, `usePopup().showConfirmation`. When to use vs full blade.
- `## Recipe: custom toolbar, banner, skeleton` — `defineBlade({ toolbarItems })`, `useBlade().addBanner()`, `<VcBlade :loading>`.

`## Variations` table at the end: variation → which prop or method to change.

**Steps:**

- [ ] **Step 1: Read vendor-portal blade examples**

- [ ] **Step 2: Write the page using the guides skeleton**

- [ ] **Step 3: Run mkdocs build**

- [ ] **Step 4: Commit**

```bash
git commit -am "docs(vc-shell): write guides/blades"
```

### Task 19: guides/data/index.md

**File:** `.../guides/data/index.md`.

**Archetype:** guides.

**Source materials:**

- `vc-shell:framework/ui/components/organisms/vc-data-table/`.
- `vc-shell:framework/core/composables/useDataTablePagination/`.
- `vc-shell:framework/core/composables/useTableSort/`.
- `vc-shell:apps/vendor-portal/src/modules/orders/composables/useOrdersListNew.ts`.

**H2 outline (5 recipes):**

- `## Recipe: server-side paginated list` — `useDataTablePagination` + search query with `skip`/`take`.
- `## Recipe: client-side filtering` — when the dataset is small enough.
- `## Recipe: sorting integration` — `useTableSort`, sort expression format.
- `## Recipe: row selection and bulk actions` — `selection-mode`, `selectedItems` ref, bulk-action toolbar.
- `## Recipe: custom cell renderer` — `<template #cell-...>` slots, when to fall back to a custom column.
- `## Recipe: state persistence on a data table` — `state-key`, link to `../../concepts/state-persistence.md`.

**Steps:**

- [ ] **Step 1: Read source materials**

- [ ] **Step 2: Write the page**

- [ ] **Step 3: Run mkdocs build**

- [ ] **Step 4: Commit**

```bash
git commit -am "docs(vc-shell): write guides/data"
```

### Task 20: guides/forms/index.md

**File:** `.../guides/forms/index.md`.

**Archetype:** guides.

**Source materials:**

- `vc-shell:framework/ui/components/organisms/vc-form/`.
- `vc-shell:framework/core/composables/useBladeForm/` if it exists, otherwise search vendor-portal for form composables.
- `vc-shell:framework/ui/components/organisms/vc-dynamic-property/` for dynamic properties.

**H2 outline (4-5 recipes):**

- `## Recipe: VcForm with VcField rows` — basic setup.
- `## Recipe: validation` — schema-based (vee-validate), per-field, error rendering.
- `## Recipe: dynamic properties` — `VcDynamicProperty`, Platform dynamic property pattern.
- `## Recipe: file upload` — `VcFileUpload` + asset client.
- `## Recipe: useBladeForm` — wrapping form state and dirty tracking for the blade close guard.

**Steps:**

- [ ] **Step 1: Read source materials**

- [ ] **Step 2: Write the page**

- [ ] **Step 3: Run mkdocs build**

- [ ] **Step 4: Commit**

```bash
git commit -am "docs(vc-shell): write guides/forms"
```

### Task 21: guides/ui/index.md

**File:** `.../guides/ui/index.md`.

**Archetype:** guides.

**Source materials:**

- `vc-shell:framework/ui/` for component layers.
- `vc-shell:framework/assets/styles/theme/` for theming.
- `vc-shell:.storybook/` for Storybook setup if relevant.

**H2 outline (4 recipes):**

- `## Recipe: theming with CSS custom properties` — variable map, where to override.
- `## Recipe: extending Tailwind` — `tailwind.config.ts` extension, when to use raw Tailwind vs Vc components.
- `## Recipe: compose, don't fork` — wrapping a Vc component vs forking the source.
- `## Recipe: Storybook for visual exploration` — running it, finding the story for a component.

**Steps:**

- [ ] **Step 1: Read theme styles**

- [ ] **Step 2: Write the page**

- [ ] **Step 3: Commit**

```bash
git commit -am "docs(vc-shell): write guides/ui"
```

### Task 22: guides/modules-and-extensions/index.md

**File:** `.../guides/modules-and-extensions/index.md`.

**Archetype:** guides.

**Source materials:**

- `vc-shell:framework/core/plugins/modularity/modularity.docs.md`.
- `vc-shell:framework/core/plugins/extension-points/extension-points.docs.md`.
- `vc-shell:packages/mf-module/`, `vc-shell:packages/mf-host/`, `vc-shell:packages/mf-config/`.

**H2 outline (4 recipes):**

- `## Recipe: package a module for npm distribution` — package.json shape, exports, peer deps.
- `## Recipe: declare framework compatibility` — `compatibleWith` in module manifest, semver ranges.
- `## Recipe: expose an extension point in your module` — host side.
- `## Recipe: ship a remote Module Federation bundle` — Vite config, `remoteEntry.js`, registry endpoint.

**Steps:**

- [ ] **Step 1: Read MF package configs and modularity docs**

- [ ] **Step 2: Write the page**

- [ ] **Step 3: Commit**

```bash
git commit -am "docs(vc-shell): write guides/modules-and-extensions"
```

### Task 23: guides/platform/index.md

**File:** `.../guides/platform/index.md`.

**Archetype:** guides.

**Source materials:**

- `vc-shell:framework/core/plugins/signalR/`.
- `vc-shell:framework/core/plugins/notifications/` or wherever the notification plugin lives.
- `vc-shell:framework/core/composables/useAssets/` and `useAssetsManager/`.
- vc-platform docs for backend context.

**H2 outline (4-5 recipes):**

- `## Recipe: SignalR for real-time updates` — `useSignalR`, subscribing to a topic, integration with notifications.
- `## Recipe: background jobs / Hangfire` — polling pattern, push via SignalR.
- `## Recipe: notifications subsystem` — `defineAppModule({ notifications })`, custom templates, toast modes.
- `## Recipe: asset and file upload` — `VcFileUpload`, asset clients, asset-manager blade integration.
- `## Recipe: dynamic properties for entities` — wiring Platform's dynamic properties to `VcDynamicProperty`.

**Steps:**

- [ ] **Step 1: Read SignalR and notifications source**

- [ ] **Step 2: Write the page**

- [ ] **Step 3: Commit**

```bash
git commit -am "docs(vc-shell): write guides/platform"
```

### Task 24: guides/cookbook/index.md

**File:** `.../guides/cookbook/index.md`.

**Archetype:** guides.

**Source materials:**

- `vc-shell:apps/vendor-portal/src/modules/` for real patterns across orders, offers, products.
- `vc-shell:cli/vc-app-skill/runtime/knowledge/` for accumulated AI-skill patterns.

**Format:** A loose collection of small recipes — "How do I X?" with 5-20 lines of code each. Aim for 6-10 recipes.

**H2 outline (each is an H2 recipe):**

- `## Show a confirmation before closing a blade` — `onBeforeClose` + `usePopup`.
- `## Pass selected rows from list to details` — `param` for ids, `options` for richer data.
- `## Refresh a list after a modification in a child blade` — `exposeToChildren({ reload })` + `callParent("reload")`.
- `## Hide a menu item based on permissions` — `menuItem.permissions` override.
- `## Open a blade from a dashboard widget` — `useBlade().openBlade()` outside blade context.
- `## Add a toolbar button conditionally` — `useToolbar()` + watch on a ref.
- `## Set a dynamic blade title` — `useBlade().setError` and title setter via `defineExpose({ title })`.

**Steps:**

- [ ] **Step 1: Read vendor-portal patterns**

- [ ] **Step 2: Write the page with 6-10 recipes**

- [ ] **Step 3: Commit**

```bash
git commit -am "docs(vc-shell): write guides/cookbook"
```

### Task 25: guides/troubleshooting/index.md

**File:** `.../guides/troubleshooting/index.md`.

**Archetype:** guides (recipe-form, but contents are problem -> diagnosis).

**Source materials:**

- The "Troubleshooting" admonitions already written in `installation.md`, `connecting-to-platform.md`, `first-blade.md`.
- `vc-shell:README.md` (`portal:` troubleshooting section).
- Recurring issues in vc-shell issue tracker if accessible.

**H2 outline (8-12 symptoms):**

- `## Blade does not open / closes immediately` — usually a thrown error in setup; check console for `useBlade()` outside blade context errors.
- `## useBlade() returns undefined methods` — calling blade-specific methods outside a blade.
- `## Storybook iframe does not load` — CSP, third-party cookies, dev server not running.
- `## Hot reload does not pick up framework changes` — `portal:` linking caveat, rebuild `@vc-shell/framework`.
- `## Build errors: peer version mismatch` — `yarn why vue`, framework / app version skew.
- `## Build errors: circular deps` — `yarn check:circular`, layer rule violations.
- `## Auth: 401 on refresh` — OAuth client scopes, refresh-token expiry.
- `## CORS preflight rejected` — dev origin not whitelisted, Vite proxy fallback.
- `## VcDataTable state lost across reloads` — `state-key` mismatch, storage cleared.
- `## Locale key shows as raw string` — bundle not merged, `APP_I18N_LOCALE` mismatch.

Each is a small section: 1-paragraph symptom + 1-2 paragraph diagnosis + a code snippet or command if applicable.

**Steps:**

- [ ] **Step 1: Aggregate symptoms from existing pages**

- [ ] **Step 2: Write the page**

- [ ] **Step 3: Commit**

```bash
git commit -am "docs(vc-shell): write guides/troubleshooting"
```

### Task 26: reference/migration/index.md

**File:** `.../reference/migration/index.md`.

**Archetype:** reference/migration (Appendix A.5).

**Source materials:**

- `vc-shell:MIGRATION_GUIDE.md` (root).
- `vc-shell:CHANGELOG.md` (root) — for breaking change inventory.
- `vc-shell:WHATS_NEW.md` (root) — v2 feature highlights.
- `vc-shell:migration/` directory if present.
- `vc-shell:cli/migrate/` for codemod CLI.

**H2 outline:**

- `## v1 → v2` — Breaking changes, codemods, manual changes (table). Lift summary from `MIGRATION_GUIDE.md`; do not duplicate the full guide — link to it.
- `## v2 → v3` — same shape. Use placeholder section noting "in progress" if v3 is not yet stabilized.
- `## Latest version highlights` — link to `WHATS_NEW.md` and `CHANGELOG.md` upstream.
- `## Migration tooling` — `vc-shell migrate` CLI usage.

**Steps:**

- [ ] **Step 1: Read `MIGRATION_GUIDE.md`, `WHATS_NEW.md`, `CHANGELOG.md`**

```bash
cat /Users/symbot/DEV/vc-shell-main-dev/vc-shell/MIGRATION_GUIDE.md
cat /Users/symbot/DEV/vc-shell-main-dev/vc-shell/WHATS_NEW.md
head -100 /Users/symbot/DEV/vc-shell-main-dev/vc-shell/CHANGELOG.md
```

- [ ] **Step 2: Write the page using the migration skeleton**

- [ ] **Step 3: Run mkdocs build**

- [ ] **Step 4: Commit**

```bash
git commit -am "docs(vc-shell): write reference/migration"
```

---

## Task 27: Final verification

**Files:**
- None (read-only verification).

- [ ] **Step 1: Full mkdocs build, diff against baseline**

```bash
mkdocs build 2>&1 | grep -E "WARNING.*custom-apps-development/vc-shell" > /tmp/vc-shell-final-warnings.txt
diff /tmp/vc-shell-baseline-warnings.txt /tmp/vc-shell-final-warnings.txt
```

Expected: no new warnings introduced by the rewritten or newly written pages. Pre-existing baseline warnings are acceptable.

- [ ] **Step 2: Confirm every page is no longer a placeholder**

```bash
grep -rln "Content coming soon" platform/developer-guide/docs/custom-apps-development/vc-shell/
```

Expected: empty output.

- [ ] **Step 3: Confirm no `??? collapsible` blocks remain in narrative pages**

```bash
grep -rnE "^\?\?\?" platform/developer-guide/docs/custom-apps-development/vc-shell/{introduction,getting-started,concepts,guides,reference/migration}/
```

Expected: empty output.

- [ ] **Step 4: Confirm no `When to read this` sections remain**

```bash
grep -rln "When to read this" platform/developer-guide/docs/custom-apps-development/vc-shell/
```

Expected: empty output.

- [ ] **Step 5: Confirm no custom HTML prev/next footers**

```bash
grep -rnE 'display: flex.*justify-content: space-between' platform/developer-guide/docs/custom-apps-development/vc-shell/
```

Expected: empty output.

- [ ] **Step 6: Run the local mkdocs serve and visually smoke-test 3 representative pages**

```bash
mkdocs serve
```

Open `http://localhost:8000/.../concepts/blade-navigation/`, `.../getting-started/first-blade/`, `.../guides/cookbook/`. Verify mermaid renders, admonitions render, prev/next link bar appears at the bottom.

- [ ] **Step 7: Open a PR**

```bash
gh pr create --title "docs(vc-shell): align narrative pages to style spec" --body "$(cat <<'EOF'
## Summary
- Audit and rewrite 12 already-written narrative pages under the style locked in the design spec.
- Author the 14 remaining placeholder pages by the same archetype rules.
- 26 pages total; mkdocs build clean.

## Test plan
- [ ] mkdocs build introduces no new warnings on the 26 pages
- [ ] Visual smoke test: blade-navigation, first-blade, cookbook render correctly
- [ ] Spec compliance: no `When to read this`, no `??? collapsible`, no custom HTML footer; all concepts open with mental model; all Vc-types verified against vc-shell source

Spec: docs/superpowers/specs/2026-05-13-vc-shell-narrative-style-design.md
EOF
)"
```

---

## Self-review notes

Spec coverage:

- Spec section 2.1 (introduction) → Tasks 1-4.
- Spec section 2.2 (getting-started) → Tasks 5-9.
- Spec section 2.3 (concepts) → Tasks 10-12, 13-17.
- Spec section 2.4 (guides) → Tasks 18-25.
- Spec section 2.5 (migration) → Task 26.
- Spec section 3 (cross-cutting rules) → Appendix B referenced by every task.
- Spec section 4 (anti-patterns) → enforced in Task 27 verification (`??? collapsible`, `When to read this`, custom HTML footer).
- Spec section 5 (audit checklist) → Appendix C referenced by every task.
- Spec section 6 (roadmap) → Phase 1 and Phase 2 sections.

No placeholders: every task lists specific files, source materials, content notes, and verification commands.

Type consistency: archetype skeletons are reproduced verbatim once in Appendix A and referenced by stable section number from each task; no drift between Phase 1 and Phase 2.
