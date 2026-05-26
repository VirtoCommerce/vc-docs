# Awesome-Pages Navigation Migration — Design

**Date:** 2026-05-26
**Scope:** `platform/developer-guide` (first guide; other guides to follow in separate cycles)
**Status:** Approved for planning

## Motivation

Today, navigation for every MkDocs sub-site lives in a hand-curated `nav:` block inside its `mkdocs.yml`. The largest, `platform/developer-guide/mkdocs.yml`, holds 932 lines, with 830 of them dedicated to `nav:`. The root site `mkdocs.yml` has 623 lines, `platform/user-guide` has 455.

The `awesome-pages` plugin is already declared in the root `mkdocs.yml` and inherited via `INHERIT:` by every sub-site, but its only active use is in `platform/developer-guide/docs/custom-apps-development/`, where 28 `.pages` files manage the VC-Shell sub-tree.

Migrating the rest of the guide to the same model gives:

- **Locality.** New page in `Fundamentals/Caching/` is one `.md` plus one line in `Fundamentals/Caching/.pages`. The shared 932-line `mkdocs.yml` is never touched by content authors.
- **Fewer merge conflicts.** Parallel PRs that add or rearrange pages collide on distinct `.pages` files, not the same monolithic YAML.
- **Rename safety.** If a page moves between folders, `awesome-pages` re-derives navigation from filesystem structure; a manual `nav:` would silently drop the page from the menu.
- **Structural visibility.** The directory tree under `docs/` becomes the menu tree.
- **Smaller review surface.** Adding a page produces a diff next to that page, not inside the master navigation YAML.

This migration is an **organizational change, not a reduction of YAML lines.** Explicit `nav:` entries inside `.pages` will remain wherever menu titles diverge from page H1s.

## Non-Goals

- Renaming files or folders to make navigation titles match filenames.
- Editing H1s of existing pages.
- Touching `custom-apps-development/` (already migrated).
- Migrating any guide other than `platform/developer-guide` in this cycle.
- URL changes of any kind.

## Approach

**Section-by-section migration within `platform/developer-guide`.** Each top-level section of the current `nav:` is migrated in its own commit/PR. Intermediate states are valid: sections not yet migrated continue to render from the residual `nav:` block, sections already migrated render from their `.pages` files. `awesome-pages` and an explicit `nav:` for sibling branches coexist without conflict.

Rejected alternatives:

- **Big-bang per guide** — single PR replacing the whole `nav:`. Too large to review, hard to isolate regressions.
- **Generator script** — reads `nav:` and produces `.pages` automatically. Adds tooling for a one-time job, still requires manual verification, overkill.

## `.pages` File Format

```yaml
title: Display Title For This Folder
nav:
  - Overview: index.md
  - Quick Start: quick-start.md
  - AI Assistance: ai-quick-start.md
  - Installation Guide
  - skills-required-for-VC-developers.md
```

Conventions:

- One `.pages` per folder at every level of the migrated tree. Without `.pages`, a folder renders in alphabetical order of its files; this almost never matches the editorial order in the current `nav:`.
- `nav:` inside `.pages` is an **ordered list** that reproduces the current order from `mkdocs.yml`.
- Use explicit `- "Display Name": file.md` only when the page's H1 differs from the desired menu label. Otherwise use the bare filename (`file.md`) or folder name.
- Use `title:` at the top of `.pages` when the folder needs a display label different from its directory name in the parent menu.
- Sub-folders are referenced by their folder name; their own `.pages` file controls their internal order.

## Top-Level Order Anchor

The top-level section order in `platform/developer-guide` is editorial (About → Overview → Getting Started → Architecture → Security and Compliance → CLI Tools → Fundamentals → Configuration Reference → Platform Manager → GraphQL API Reference (xAPI) → … → Custom Apps Development), not alphabetical or filename-prefix-derived. To preserve it without keeping a `nav:` in `mkdocs.yml`, a single `platform/developer-guide/docs/.pages` file pins the top-level order. This file is created on the first migration step and updated incrementally as further sections move.

## Per-Section Migration Procedure

Each top-level section follows the same six-step procedure. Example: `CLI Tools`.

### Step 1 — Baseline snapshot

```bash
mkdocs build -f platform/developer-guide/mkdocs.yml -d /tmp/before
mkdocs serve -f platform/developer-guide/mkdocs.yml --dev-addr 127.0.0.1:8005
```

Capture the **rendered menu** with Playwright before any change:

- Navigate to a representative page in the section (`/CLI-tools/overview/`).
- Snapshot the sidebar DOM (`mcp__playwright__browser_snapshot`).
- Save a screenshot of the expanded section (`mcp__playwright__browser_take_screenshot`).

### Step 2 — Create `.pages` files

Place a `.pages` in the section root and every sub-folder that needs custom titles or ordering:

```yaml title="docs/CLI-tools/.pages"
title: CLI Tools
nav:
  - Overview: overview.md
  - Getting Started: getting-started.md
  - Build Automation: build-automation.md
  - Package Management: package-management.md
  - Grab Migrator Utility Quickstart: grab-migrator.md
  - Cold Start Optimization and Data Migration: cold-start-and-data-migration.md
  - Installing and Updating Platform and Modules: install-and-update-platform-and-modules.md
  - Managing Platform and Modules with CLI: more-targets.md
  - Virto Cloud:
      - Overview: virto-cloud-overview.md
      - Using Virto Cloud: virto-cloud.md
```

Note the inline nested list for `Virto Cloud`: its two pages live in the `CLI-tools/` folder directly (not in a sub-folder), so they cannot be moved into a sibling `.pages` without renaming files. `awesome-pages` supports nested inline groups inside `nav:` exactly for this case. Where a sub-section corresponds to a real sub-folder, prefer a separate `.pages` in that sub-folder instead — see Step 2 conventions.

### Step 3 — Remove section from `mkdocs.yml`

Delete the `- CLI Tools:` branch from `nav:` in `platform/developer-guide/mkdocs.yml`. Add the corresponding entry to `docs/.pages` to preserve top-level ordering.

Steps 2 and 3 happen in the same commit. Atomic.

### Step 4 — Post-change snapshot

```bash
mkdocs build -f platform/developer-guide/mkdocs.yml -d /tmp/after
diff -r /tmp/before /tmp/after \
  | grep -v "git-revision-date\|search_index.json\|sitemap"
```

Acceptance for the diff:

- No HTML files added or removed (URL surface unchanged).
- Per-page differences confined to sidebar/breadcrumb regions of HTML; main content untouched.

### Step 5 — Playwright validation (required on every section)

Restart `mkdocs serve` and run the following Playwright sequence:

1. Navigate to the same representative page from Step 1.
2. Snapshot the sidebar DOM. Diff against the Step 1 snapshot: menu items, order, labels, nesting must be identical.
3. Take a screenshot. Compare to Step 1 screenshot.
4. For each page in the section, click through the menu and verify:
   - Active-state highlighting works.
   - `scroll-menu.js` brings the deep nav item into view (this is load-bearing per `project_material_sidebar_no_native_auto_scroll`).
   - No console errors (`mcp__playwright__browser_console_messages`).
5. Test a deep page in the section: open it via direct URL, confirm the sidebar auto-scrolls and the page itself renders unchanged.

If any check fails, do **not** commit. Investigate, fix the `.pages` file, repeat from Step 4.

### Step 6 — Commit

One commit per section. Commit message names the section and references this spec.

## Migration Order

1. **About Virto Commerce Platform + Overview** — creates the top-level `docs/.pages` scaffold and pins the editorial order. Smallest possible first step.
2. **Getting Started** — three nesting levels; first real test of folder hierarchy.
3. **Architecture** — small, low risk.
4. **Security and Compliance** — single page.
5. **CLI Tools** — example used throughout this spec.
6. **Configuration Reference** — single page.
7. **Platform Manager**.
8. **Fundamentals** — largest section (~200 lines of `nav:`, up to 5 levels). Done after the procedure is proven on smaller sections.
9. **GraphQL API Reference (xAPI)** — large, long folder name (`GraphQL-Storefront-API-Reference-xAPI`); careful title check.
10. Remaining top-level sections in original `nav:` order.
11. **Custom Apps Development** — not touched; already migrated.

After all sections are migrated, `platform/developer-guide/mkdocs.yml`'s `nav:` block is either deleted entirely or reduced to a single flat list of top-level folder references — decided in the final step when the full `docs/.pages` is visible.

## Risks and Mitigations

| Risk | Mitigation |
| --- | --- |
| Page disappears from menu after migration. | Step 4 `diff -r` and Step 5 Playwright menu snapshot catch this before commit. |
| Menu label differs from current. | Explicit `"Display": file.md` in `.pages`. Step 5 Playwright DOM diff catches drift. |
| URLs break. | Files and folders are not renamed in this migration. |
| `mike` versioning breaks old links under `/2.0/`. | Not affected. `/latest/` rebuilds with new structure; `/2.0/` is frozen build artifact. |
| `awesome-pages` and residual `nav:` conflict. | Each commit removes the section from `nav:` and adds the `.pages` atomically. Intermediate states keep one source of truth per branch. |
| `scroll-menu.js` (load-bearing for deep-nav-item visibility) breaks on new menu DOM. | Step 5 Playwright sequence explicitly verifies auto-scroll for deep pages. |
| `custom-apps-development` conflicts with new top-level `docs/.pages`. | `docs/.pages` references `custom-apps-development` only as a folder entry. Its internal `.pages` chain stays authoritative for its sub-tree. |
| Search index breaks (hook `search_index_fixer.py` runs against new menu). | Build run in Step 4 emits the index; Playwright Step 5 verifies search works on a known query. |
| Editor accidentally relies on alphabetic ordering after section migration. | `nav:` inside `.pages` is always explicit. Bare folder/file references (which would alphabetize) are used only when alphabetic order coincides with the desired order, never as a default. |

## Definition of Done (per section)

A section is migrated when:

- The section's branch is gone from `mkdocs.yml`'s `nav:`.
- A `.pages` file exists in the section root and every sub-folder that needs custom titles or ordering.
- `mkdocs build` succeeds with no warnings related to navigation or missing pages.
- `diff -r` of site-output before/after shows only sidebar/breadcrumb changes; no HTML files added or removed.
- Playwright sidebar DOM snapshot is identical to baseline: same labels, same order, same nesting.
- Playwright screenshot matches baseline (manual visual review acceptable).
- `scroll-menu.js` auto-scroll verified for at least one deep page in the section.
- No new console errors on any page in the section.

## Definition of Done (whole guide)

The guide is migrated when:

- All top-level sections in original `nav:` (except `custom-apps-development`, already done) have their own `.pages` chains.
- `mkdocs.yml`'s `nav:` is empty or reduced to a flat top-level list.
- Full-site Playwright pass: navigate all top-level sections, sidebar matches baseline DOM snapshots, no console errors.
- A short note added to the guide's contributor docs explaining the `.pages` convention so future page authors know not to edit `mkdocs.yml` for navigation.

## Out-of-Scope Follow-Ups

After this guide is done, the same procedure can be applied to:

- `platform/user-guide` (455 lines)
- `storefront/developer-guide` (103 lines)
- `marketplace/developer-guide` (77 lines)
- `storefront/user-guide`, `marketplace/user-guide`, `platform/deployment-on-cloud` — all small.
- Root `mkdocs.yml` (623 lines) — different surface (cross-guide top-level navigation); may need its own design pass.

These are separate cycles and not part of this spec.
