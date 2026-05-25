# VC-Shell Narrative Documentation Style — Design

**Status:** Approved 2026-05-13.
**Scope:** Style rules for 26 narrative pages under `platform/developer-guide/docs/custom-apps-development/vc-shell/`.
**Anchor models:** [Nuxt 3 docs](https://nuxt.com/docs) for tone; vc-docs `Fundamentals/Modularity/` and `Fundamentals/Caching/` for repo convention.
**Out of scope:** Auto-synced reference (`components/`, `composables/`, `plugins/`, `reference/api/`, `reference/modules/`) — guarded by CI.
**Relation to CLAUDE.md:** This design is additive. The project-level style guide in `CLAUDE.md` (Virto Commerce / Platform / Frontend orthography, file-name bolding, no italics, code-block titling, sentence-ending periods) continues to apply on top of these archetype rules.

## 1. Goal

Unify narrative content across the VC-Shell section under the established vc-docs Fundamentals convention. Eliminate ad-hoc structures introduced in prior iterations (`When to read this` sections, `??? collapsible` details, code-first concept pages, custom HTML prev/next footers). Provide a checklist that can verify any page against the rules.

The reader profile is a Vue 3 developer meeting VC-Shell for the first time. They know Vue and TypeScript; they do not know blade paradigm, modularity, or extension points. They want to ship a custom app, not learn framework internals.

## 2. Page archetypes

The plan locks 26 pages across 5 folders. Each folder maps to one archetype with its own skeleton and rules.

### 2.1 introduction/ (4 pages)

Pitch and orientation. Reader walks away knowing what VC-Shell is, who it is for, how it relates to neighboring tools.

Skeleton:

```text
# <Title>

<1-line tagline.>

<2-3 paragraphs of mental model: what this is in one sentence,
what problem it solves, the target audience, where it sits in the
architecture.>

<Diagram (mermaid for structural; PNG for screenshots).>

## <Sub-concept 1>

<Prose. May include a comparison table for positioning pages.>

## <Sub-concept 2>

<Prose, optionally a single code or CLI block.>

![Readmore](relative/path.md){: width="25"} Inline cross-link.
```

Rules:

- No code blocks except a single CLI command on `index.md` (the install one-liner).
- Comparison tables (VC-Shell vs general admin kits vs Platform manager) are encouraged on positioning pages.
- Length: 200–600 words.

### 2.2 getting-started/ (5 pages)

Sequential tutorial flow. Reader goes from empty disk to first authenticated API call.

Skeleton:

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

Rules:

- Section headings in imperative voice: `Install dependencies`, `Configure the URL`, `Run`.
- Every CLI block carries `title=` describing the context where the command runs.
- Troubleshooting items are `!!! warning` admonitions, not a table.
- Length: 300–900 words.

### 2.3 concepts/ (8 pages)

The main archetype. Establishes the mental model, then walks through the everyday API, common patterns, common mistakes.

Skeleton:

```text
# <Title>

<1-line statement of what this concept is.>

<2-3 paragraphs setting up the mental model: why this concept exists,
what problem it solves, how it relates to neighboring concepts in
VC-Shell. Nuxt-style: opinionated, narrative.>

```mermaid
<diagram if the concept is structural — stack, layers, flow>
```

## <Sub-concept 1>

<Paragraph of prose explaining the why.>

<Code or table.>

<Optional second paragraph elaborating.>

## <Sub-concept 2>

<Prose-led.>

```vue title="src/modules/orders/pages/OrdersList.vue"
<real-looking code adapted from vendor-portal>
```

!!! tip
    Inline tip about the concept.

![Readmore](../composables/.../X.md){: width="25"} Full API reference.

## Common patterns

<Table of pattern -> how, or 2-3 H3 subsections with prose-led code.>

## Common mistakes

!!! warning "Mistake description"
    Why it happens. How to fix.
```

Rules:

- Mental model is mandatory in the first 2-3 paragraphs. Code-first is forbidden in this archetype.
- Every H2 opens with prose, then code. Not the reverse.
- Cross-link to the auto-synced reference (`composables/.../X.md`) via inline `![Readmore]` adjacent to the relevant sub-concept — not in a "Next steps" footer.
- Code examples should come from real `apps/vendor-portal/` composables when possible. Use real Vc-class names (`VcmpSellerOrdersClient`, not `OrderClient`).
- Length: 600–1200 words.

### 2.4 guides/ (8 pages)

Recipe-oriented. Reader looks for "to do X, do Y" with minimum theory.

Skeleton:

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

Rules:

- 3–6 recipes per page, each as a top-level H2.
- Code lifted from vendor-portal where applicable.
- Length: 500–1200 words.

### 2.5 reference/migration/ (1 page)

Version-by-version upgrade reference.

Skeleton:

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

Rules:

- One H2 section per major version bump.
- Before/after code in fenced blocks with language hint.
- Length: 400+ words per major bump.

## 3. Cross-cutting rules

### Admonitions

| Type | Use for |
| --- | --- |
| `!!! note`. | Neutral context. |
| `!!! tip`. | Actionable hint. |
| `!!! warning`. | Pitfall, common mistake, troubleshooting symptom. |
| `!!! info`. | Supplementary information. |

Do not use `??? note` (collapsible details). No prior usage in vc-docs.

### Code blocks

````md
```vue title="src/modules/orders/pages/OrdersList.vue" linenums="1" hl_lines="3 7"
```
````

- `title=` required for file-content blocks.
- `linenums="1"` for blocks longer than 5 lines.
- `hl_lines` when specific lines are central to the explanation.
- Language hint always present (`vue`, `ts`, `bash`, `json`).

### Diagrams

- **Mermaid** for structural diagrams (flow, layer, stack). Version-controllable, theme-aware.
- **PNG** in `media/` for UI screenshots or complex hand-drawn diagrams.
- Center with `{: style="display: block; margin: 0 auto;" }`.

### Cross-links

- **Inline `![Readmore](path){: width="25"} Title`** where the reader needs a deeper dive.
- **No custom HTML footer** for prev/next. mkdocs-material renders prev/next from `.pages` automatically.
- No "Next steps" or "Next" section at the end of pages.

### Naming

- Verify every Vc-class, composable, plugin, and type against vc-shell source before drafting.
- First mention of a framework concept is bolded (`**defineAppModule**`); subsequent mentions are regular weight.

### Voice

- Second-person, present tense, active voice: "You install the framework by ..."
- Headings in imperative voice: "Install dependencies", not "Installing dependencies".
- No marketing-speak ("revolutionary", "blazing fast").

## 4. Anti-patterns

| Anti-pattern | Why |
| --- | --- |
| `## When to read this` section. | Not in vc-docs convention. The intro paragraph already does this job. |
| `??? note` collapsible details. | No prior usage in vc-docs. |
| Code-first concept page. | Concepts must establish mental model first, otherwise they duplicate the auto-synced reference. |
| "Trade-offs to weigh" without concrete alternatives. | Vague. Use only when paired with specific options. |
| "What X is not" lists for their own sake. | Only when paired with concrete alternatives. |
| Custom HTML `<div>` prev/next footer. | mkdocs-material renders prev/next automatically. |
| Invented identifier names (e.g., `OrderClient` instead of `VcmpSellerOrdersClient`). | All Vc-names verified against source. |
| Framework internals on app-dev pages (`IAuthApiBase`, fetch interceptors, token refresh mechanics). | Application developers never touch these. |
| "Next steps" with 3-4 links at the end. | Replaced by mkdocs auto prev/next plus inline `![Readmore]`. |
| Generic JS patterns (`Promise.all`, try/catch). | Not VC-Shell-specific. |

## 5. Audit checklist

Apply to each page:

1. Tone anchor matches archetype? (intro: pitch / getting-started: imperative / concepts: mental model + code / guides: recipe.)
2. Opens with 1-line statement, plus 2-3 paragraphs of mental model for concepts?
3. Diagram present when the topic is structural?
4. For concepts: every H2 opens with prose, not code?
5. Code blocks have `title=`?
6. No `When to read this` section?
7. No `??? collapsible` blocks?
8. Inline `![Readmore]` links present where the reader needs deeper material?
9. No custom HTML footer prev/next?
10. All Vc-types verified against vc-shell source?
11. Framework internals absent on app-dev pages?
12. Length within the archetype's target range?
13. Code adapted from `apps/vendor-portal/` where applicable?

## 6. Roadmap

### Phase 1 — Audit and rewrite the 12 already-written pages

| # | Page | Archetype | Known issues to fix |
| --- | --- | --- | --- |
| 1 | introduction/index.md. | intro. | OK. May benefit from inline `![Readmore]`. |
| 2 | introduction/what-is-vc-shell.md. | intro. | "How to decide" closer, "What it is not" — review for value. |
| 3 | introduction/architecture-overview.md. | intro. | `??? note` (forbidden), "Next" footer (forbidden). |
| 4 | introduction/when-to-use.md. | intro. | "Trade-offs to weigh" — keep, decision-driven. |
| 5 | getting-started/installation.md. | getting-started. | "Next" footer (forbidden). |
| 6 | getting-started/create-your-app.md. | getting-started. | "Next" footer (forbidden). |
| 7 | getting-started/project-structure.md. | getting-started. | "Next" footer (forbidden). |
| 8 | getting-started/connecting-to-platform.md. | getting-started. | `??? note` (forbidden) → `!!! note`. "Next" footer (forbidden). |
| 9 | getting-started/first-blade.md. | getting-started. | "Next" footer (forbidden). |
| 10 | concepts/blade-navigation.md. | concepts. | Code-first opening — add mental-model paragraphs. |
| 11 | concepts/modules.md. | concepts. | Code-first opening — add mental-model paragraphs. |
| 17 | concepts/api-clients.md. | concepts. | Code-only — add mental model, restore why blade composition uses these primitives. |

Commit per page or per coherent batch.

### Phase 2 — Write the 14 remaining pages

| # | Page | Archetype |
| --- | --- | --- |
| 12 | concepts/extensions.md. | concepts. |
| 13 | concepts/layout.md. | concepts. |
| 14 | concepts/permissions-model.md. | concepts. |
| 15 | concepts/localization.md. | concepts. |
| 16 | concepts/state-persistence.md. | concepts. |
| 18 | guides/blades/index.md. | guides. |
| 19 | guides/data/index.md. | guides. |
| 20 | guides/forms/index.md. | guides. |
| 21 | guides/ui/index.md. | guides. |
| 22 | guides/modules-and-extensions/index.md. | guides. |
| 23 | guides/platform/index.md. | guides. |
| 24 | guides/cookbook/index.md. | guides. |
| 25 | guides/troubleshooting/index.md. | guides. |
| 26 | reference/migration/index.md. | reference/migration. |

Apply the archetype skeletons. Commit per page.

## 7. Out of scope

- Translation to non-English languages.
- Screenshots and screencasts beyond what `media/` already holds.
- Tutorial courses spanning multiple pages.
- Re-styling the mkdocs theme.
- Adding new mkdocs plugins.
- Modifying the `*.docs.md` → vc-docs sync pipeline.
- Hidden source-frontmatter blocks (deferred; revisit when maintainability becomes an issue).
