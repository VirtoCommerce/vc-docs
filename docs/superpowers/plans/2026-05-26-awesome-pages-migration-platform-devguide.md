# Awesome-Pages Navigation Migration: platform/developer-guide Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Migrate `platform/developer-guide` navigation from a 932-line manual `nav:` in `mkdocs.yml` to per-folder `.pages` files managed by the `awesome-pages` MkDocs plugin, section by section, with no regression in URLs, menu titles, ordering, or behavior of `scroll-menu.js`.

**Architecture:** Each top-level section of the current `nav:` is migrated atomically: a single commit removes its branch from `mkdocs.yml` and adds the corresponding `.pages` files under `platform/developer-guide/docs/`. Intermediate states are valid — `awesome-pages` processes any folder not covered by the residual `nav:`. Every step is verified by side-by-side site builds plus a Playwright DOM/screenshot diff of the rendered sidebar.

**Tech Stack:** MkDocs, `awesome-pages` plugin (already declared in this guide's `mkdocs.yml`), `mike` versioning, Playwright MCP for browser-based validation, `mkdocs serve` for local preview.

**Reference:** Design spec at `docs/superpowers/specs/2026-05-26-awesome-pages-migration-design.md`.

---

## Prerequisites for Every Task

Read this once before starting. Every section-migration task uses the same procedure; the per-task block below shows the section-specific files and YAML content.

### Local environment

- Working directory: `/Users/symbot/DEV/vc-docs/`.
- Branch: `fix/sidebar-auto-scroll` (or a fresh branch off it — verify with `git status` before starting Task 0).
- Python venv with MkDocs and plugins already installed. If `mkdocs --version` fails, run `pip install mkdocs mkdocs-awesome-pages-plugin mike` from the project root.

### How `awesome-pages` reads `.pages`

- One `.pages` per folder, YAML format.
- Top-level keys we use: `title:` (folder's display label in parent menu) and `nav:` (ordered list of children).
- `nav:` entry forms:
  - `- file.md` — page uses its own H1 as the menu label.
  - `- "Display Label": file.md` — explicit label override (use when H1 differs from current `mkdocs.yml` label).
  - `- folder-name` — sub-folder; its own `.pages` controls its internals.
  - `- "Display Label": folder-name` — sub-folder with explicit label.
  - Inline nested group (no real sub-folder):
    ```yaml
    - Virto Cloud:
        - Overview: virto-cloud-overview.md
        - Using Virto Cloud: virto-cloud.md
    ```
    Use this when the source `nav:` groups loose files in the same folder into a logical sub-section. Do NOT introduce new sub-folders.
- If a folder has both an explicit `nav:` in a parent `.pages` and its own `.pages`, the parent wins for ordering/labels and the child controls its internals. To avoid confusion, prefer: parent `.pages` references the sub-folder by name; child `.pages` has the `title:` and full `nav:`.

### Standard six-step section procedure

Every section task follows this template. Concrete commands are filled in per task.

1. **Baseline build (before any change):**

   ```bash
   rm -rf /tmp/before
   mkdocs build -f platform/developer-guide/mkdocs.yml -d /tmp/before --strict
   ```

   Expected: build succeeds. No `WARNING - A reference to '...' is included in the 'nav'` messages. If there are pre-existing warnings, capture the count.

2. **Baseline Playwright snapshot (before any change):**

   Start a dev server:

   ```bash
   mkdocs serve -f platform/developer-guide/mkdocs.yml --dev-addr 127.0.0.1:8005 &
   sleep 5
   ```

   Then via Playwright MCP tools:
   - `mcp__playwright__browser_navigate` to `http://127.0.0.1:8005/<SECTION-REPRESENTATIVE-PAGE>/`.
   - `mcp__playwright__browser_snapshot` — save accessibility tree of the sidebar (look for `<nav class="md-nav md-nav--primary">`).
   - `mcp__playwright__browser_take_screenshot` with `fullPage: false`, filename: `/tmp/before-<section-slug>.png`.
   - `mcp__playwright__browser_evaluate` with this function to capture the sidebar DOM as text:
     ```javascript
     () => {
       const nav = document.querySelector('.md-sidebar--primary .md-nav__list');
       return nav ? nav.innerText : 'NOT FOUND';
     }
     ```
     Save the returned string to `/tmp/before-<section-slug>-sidebar.txt` via Write.
   - Kill the server: `pkill -f "mkdocs serve" || true`.

3. **Create `.pages` files for the section.**

   For each `.pages` file listed in the per-task block, use Write tool. Each file is shown in full YAML. Folder structure follows the existing `docs/` tree — no new folders are created in this migration.

4. **Remove section from `mkdocs.yml`.**

   Edit `platform/developer-guide/mkdocs.yml`: delete the section's `- Section Name:` branch from the `nav:` block. The per-task block names the exact line range.

   Also, update `platform/developer-guide/docs/.pages` to insert/keep the section in the top-level order. If `docs/.pages` does not yet exist, Task 1 creates it.

5. **Post-change build + diff:**

   ```bash
   rm -rf /tmp/after
   mkdocs build -f platform/developer-guide/mkdocs.yml -d /tmp/after --strict
   diff -r /tmp/before /tmp/after \
     | grep -v "git-revision-date" \
     | grep -v "search_index.json" \
     | grep -v "sitemap" \
     | tee /tmp/diff-<section-slug>.txt
   ```

   Acceptance:
   - Build succeeds.
   - No HTML files added or removed (`diff` output mentions only "differ" lines, never "Only in /tmp/before" or "Only in /tmp/after" for `.html` files).
   - Per-page differences are confined to sidebar/breadcrumb HTML.

   If the diff shows HTML files missing/added, **stop** — the `.pages` file is wrong. Most common cause: an `.md` file in the folder is not listed and `nav:` does not contain `...` to glob remaining files.

6. **Post-change Playwright re-verification:**

   ```bash
   mkdocs serve -f platform/developer-guide/mkdocs.yml --dev-addr 127.0.0.1:8005 &
   sleep 5
   ```

   - `mcp__playwright__browser_navigate` to the same representative page from step 2.
   - `mcp__playwright__browser_evaluate` with the same JS function from step 2. Save to `/tmp/after-<section-slug>-sidebar.txt`.
   - Run `diff /tmp/before-<section-slug>-sidebar.txt /tmp/after-<section-slug>-sidebar.txt`. Expected: **empty output** (zero differences in sidebar text).
   - `mcp__playwright__browser_take_screenshot` to `/tmp/after-<section-slug>.png`. Compare visually to `/tmp/before-<section-slug>.png`.
   - `mcp__playwright__browser_console_messages` — confirm no new errors.
   - Click into one deep page in the section. Confirm `scroll-menu.js` brings the active sidebar item into view (active item is `<li class="md-nav__item md-nav__item--active">` and should be visible in the viewport — verify with `mcp__playwright__browser_evaluate`:
     ```javascript
     () => {
       const active = document.querySelector('.md-sidebar--primary .md-nav__item--active');
       if (!active) return 'NO ACTIVE ITEM';
       const rect = active.getBoundingClientRect();
       const inView = rect.top >= 0 && rect.bottom <= window.innerHeight;
       return inView ? 'IN VIEWPORT' : `OUT OF VIEW: top=${rect.top}, bottom=${rect.bottom}`;
     }
     ```
     Expected: `"IN VIEWPORT"`.
   - Kill the server: `pkill -f "mkdocs serve" || true`.

   If any check fails, do **not** commit. Edit the `.pages` file or `mkdocs.yml` to fix, then repeat from step 5.

7. **Commit.**

   ```bash
   git add platform/developer-guide/docs/.pages \
           platform/developer-guide/docs/<SECTION-FOLDER>/.pages \
           platform/developer-guide/mkdocs.yml
   git commit -m "$(cat <<'EOF'
docs(nav): migrate <Section Name> to awesome-pages .pages

See docs/superpowers/specs/2026-05-26-awesome-pages-migration-design.md.
Removed <Section Name> branch from platform/developer-guide/mkdocs.yml
nav:, added equivalent .pages files under docs/<SECTION-FOLDER>/.
Playwright sidebar DOM diff is empty; no HTML files added or removed.

EOF
)"
   ```

   Add `git add` lines for additional sub-folder `.pages` files when the section has sub-folders.

### Common pitfalls

- **Sub-folder vs inline group.** If the source `nav:` groups files in the SAME folder (e.g., `Virto Cloud:` containing `CLI-tools/virto-cloud-overview.md` and `CLI-tools/virto-cloud.md` — both in `CLI-tools/`, no `Virto-Cloud/` sub-folder), use an **inline nested group** inside the parent `.pages`. Do NOT create new sub-folders — that renames URLs.
- **File not yet listed.** If a `.pages` `nav:` lists 5 files and the folder has 7 `.md` files, the extra 2 will not render. Either list all files explicitly, or append `- ...` at the end of `nav:` to glob the rest in filename order.
- **Index pages.** `index.md` inside a folder becomes the section landing page (URL `/folder/`). It must still be listed inside `.pages` `nav:` if it should appear as a menu item — otherwise it is rendered only as the implicit folder link.
- **Order alignment with top-level.** After removing a section from `mkdocs.yml` `nav:`, the top-level `docs/.pages` is the only place that controls top-level order. Forgetting to update it makes the migrated section appear at the wrong position.

---

## Task 0: Setup and Pre-Migration Verification

**Files:**
- Verify: `platform/developer-guide/mkdocs.yml`

- [ ] **Step 1: Verify clean git state**

  ```bash
  cd /Users/symbot/DEV/vc-docs
  git status
  ```

  Expected: branch `fix/sidebar-auto-scroll` (or current working branch), no unrelated uncommitted changes. If untracked junk exists, decide whether to stash before migration.

- [ ] **Step 2: Verify `awesome-pages` is registered in this guide's plugins**

  ```bash
  grep -n "awesome-pages" platform/developer-guide/mkdocs.yml
  ```

  Expected: line 23 contains `    - awesome-pages`. If missing, add it to the `plugins:` block before any other migration step.

- [ ] **Step 3: Verify full-site build succeeds before migration**

  ```bash
  rm -rf /tmp/baseline-full
  mkdocs build -f platform/developer-guide/mkdocs.yml -d /tmp/baseline-full --strict
  ```

  Expected: completes with exit 0. Capture any pre-existing warnings; these are not regressions if they reappear after migration.

- [ ] **Step 4: Verify Playwright MCP is available**

  Confirm tool calls work by navigating to about:blank:
  - `mcp__playwright__browser_navigate` with `url: about:blank` should succeed.

  If Playwright MCP is not available, stop here and resolve before continuing — the spec requires it for validation on every section.

- [ ] **Step 5: Verify the example pre-migrated folder still works**

  ```bash
  ls platform/developer-guide/docs/custom-apps-development/.pages
  ls platform/developer-guide/docs/custom-apps-development/vc-shell/.pages
  ```

  Expected: both files exist. This is the reference shape we are copying.

- [ ] **Step 6: Commit a "migration baseline" marker (optional but recommended)**

  No file change, but tag the commit before any migration starts:

  ```bash
  git tag awesome-pages-migration-baseline
  ```

  Lets you compare site output back to this exact state at any point.

---

## Task 1: Top-Level Scaffold + About + Overview

**Files:**
- Create: `platform/developer-guide/docs/.pages`
- Modify: `platform/developer-guide/mkdocs.yml` (lines 104–105: remove `About Virto Commerce Platform` and `Overview` entries)

This task establishes the top-level order anchor (`docs/.pages`) and migrates the two single-page top-level entries. Representative page for Playwright snapshot: `http://127.0.0.1:8005/` (root, which is `index.md`).

- [ ] **Step 1: Baseline build**

  ```bash
  rm -rf /tmp/before
  mkdocs build -f platform/developer-guide/mkdocs.yml -d /tmp/before --strict
  ```

- [ ] **Step 2: Baseline Playwright snapshot (representative: root page)**

  ```bash
  mkdocs serve -f platform/developer-guide/mkdocs.yml --dev-addr 127.0.0.1:8005 &
  sleep 5
  ```

  Navigate to `http://127.0.0.1:8005/`, snapshot, evaluate sidebar text → save to `/tmp/before-toplevel-sidebar.txt`, screenshot to `/tmp/before-toplevel.png`. Then kill server.

- [ ] **Step 3: Create `platform/developer-guide/docs/.pages`**

  ```yaml
  nav:
    - About Virto Commerce Platform: getting-to-know-platform.md
    - Overview: index.md
    - Getting Started
    - Architecture
    - Security and Compliance
    - CLI Tools: CLI-tools
    - Fundamentals
    - Configuration Reference
    - Platform Manager
    - GraphQL API Reference (xAPI): GraphQL-Storefront-API-Reference-xAPI
    - Extensibility
    - Operations
    - Tutorials and How-tos: Tutorials-and-How-tos
    - Releases, Bundles, PBCs. Installation and Updates: Updating-Virto-Commerce-Based-Project
    - Custom Apps Development: custom-apps-development
  ```

  Notes:
  - Folder names with `Title Case Hyphenated` form (`Getting-Started`, `Architecture`, etc.) are matched directly — `- Getting Started` works because `awesome-pages` treats the unquoted scalar as the folder name when a folder of that name (case-insensitive, hyphens equivalent to spaces) exists. **Verify each one** with `ls platform/developer-guide/docs/` before relying on this. If a folder name has unusual casing or unrelated characters, use the explicit `- "Display": folder-name` form (already used above for `CLI Tools: CLI-tools`, `GraphQL API Reference (xAPI): GraphQL-Storefront-API-Reference-xAPI`, `Tutorials and How-tos: Tutorials-and-How-tos`, and `Releases, ...: Updating-Virto-Commerce-Based-Project`).
  - Sub-folder ordering and internal navigation will be added in Tasks 2–13 (one per section). Until then, awesome-pages renders unmigrated folders alphabetically — that's OK at top level because `docs/.pages` pins the top-level order; the inside of each folder still comes from `mkdocs.yml` `nav:`.

- [ ] **Step 4: Update `platform/developer-guide/mkdocs.yml`**

  Delete lines 104–105 (the two top-level single-page entries):

  ```yaml
  # REMOVE these two lines from nav::
  - About Virto Commerce Platform: getting-to-know-platform.md
  - Overview: index.md
  ```

  Use the Edit tool with `old_string`:
  ```
      - About Virto Commerce Platform: getting-to-know-platform.md
      - Overview: index.md
      - Getting Started:
  ```
  and `new_string`:
  ```
      - Getting Started:
  ```

- [ ] **Step 5: Post-change build + diff**

  ```bash
  rm -rf /tmp/after
  mkdocs build -f platform/developer-guide/mkdocs.yml -d /tmp/after --strict
  diff -r /tmp/before /tmp/after \
    | grep -v "git-revision-date" \
    | grep -v "search_index.json" \
    | grep -v "sitemap" \
    | tee /tmp/diff-toplevel.txt
  ```

  Expected: differences only inside `.html` files (sidebar markup). **No** "Only in" lines for HTML files. The fact that this commit also pre-references folders we have not yet migrated is fine — those folders keep their own ordering from the residual `mkdocs.yml` `nav:` block.

- [ ] **Step 6: Post-change Playwright re-verification**

  Same as Step 2, save to `/tmp/after-toplevel-sidebar.txt` and `/tmp/after-toplevel.png`. Diff:

  ```bash
  diff /tmp/before-toplevel-sidebar.txt /tmp/after-toplevel-sidebar.txt
  ```

  Expected: empty output (sidebar text identical). Active-item-in-viewport check from Prerequisites step 6 should return `"IN VIEWPORT"`.

- [ ] **Step 7: Commit**

  ```bash
  git add platform/developer-guide/docs/.pages platform/developer-guide/mkdocs.yml
  git commit -m "$(cat <<'EOF'
  docs(nav): scaffold top-level .pages and migrate About + Overview

  Created platform/developer-guide/docs/.pages with top-level order
  anchor. Removed About Virto Commerce Platform and Overview entries
  from platform/developer-guide/mkdocs.yml nav:. Playwright sidebar
  DOM diff is empty.

  See docs/superpowers/specs/2026-05-26-awesome-pages-migration-design.md.
  EOF
  )"
  ```

---

## Task 2: Migrate "Getting Started"

**Files:**
- Create: `platform/developer-guide/docs/Getting-Started/.pages`
- Create: `platform/developer-guide/docs/Getting-Started/Installation-Guide/.pages`
- Create: `platform/developer-guide/docs/Getting-Started/Installation-Guide/Post-Installation-Steps/.pages`
- Modify: `platform/developer-guide/mkdocs.yml` (lines 106–120: remove `Getting Started` branch)

Source nav lines being migrated (current `mkdocs.yml`):

```yaml
- Getting Started:
      - Quick Start: Getting-Started/quick-start.md
      - AI Assistance: Getting-Started/ai-quick-start.md
      - System Requirements: Getting-Started/system-requirements.md
      - Installation Guide:
            - Windows: Getting-Started/Installation-Guide/windows.md
            - Linux: Getting-Started/Installation-Guide/linux.md
            - MacOS: Getting-Started/Installation-Guide/macOS.md
            - Local install with start-local: Getting-Started/Installation-Guide/start-local.md
            - Post Installation Steps:
                  - Setting Up Self Signed SSL Certificate: Getting-Started/Post-Installation-Steps/01-setting-up-self-signed-ssl-cert.md
                  - Configuring Email Notifications: Getting-Started/Post-Installation-Steps/02-configuring-email-notifications.md
                  - Configuring Asset Blob Storage: Getting-Started/Post-Installation-Steps/03-configuring-asset-blob-storage.md
                  - Importing Sample Data: Getting-Started/Post-Installation-Steps/04-importing-sample-data.md
      - Skills Required for VC Developers: skills-required-for-VC-developers.md
```

Representative page for Playwright: `http://127.0.0.1:8005/Getting-Started/quick-start/`.

**Note:** `Post Installation Steps` is grouped under `Installation Guide:` in the source nav, but its files live in `Getting-Started/Post-Installation-Steps/` — a sibling of `Getting-Started/Installation-Guide/`, not a child. We cannot place a sub-folder `.pages` inside `Installation-Guide/Post-Installation-Steps/` because that folder does not exist there. Two options:
- **(A)** Use an **inline nested group** inside `Getting-Started/Installation-Guide/.pages` that references the sibling folder's files directly. Verify with `ls platform/developer-guide/docs/Getting-Started/Post-Installation-Steps/` — these files are at that sibling path.
- **(B)** Place `Post Installation Steps` as its own top-level child of `Getting Started` in `Getting-Started/.pages` (matching the filesystem), and accept that the menu shape changes.

Option B changes menu nesting (currently Post Installation Steps is under Installation Guide), so it is a visible regression. Option A preserves the current menu shape by referencing files across folders inline. Use Option A.

- [ ] **Step 1: Baseline build** (same as Task 1 Step 1)

- [ ] **Step 2: Baseline Playwright snapshot**

  Navigate to `http://127.0.0.1:8005/Getting-Started/quick-start/`. Save sidebar text to `/tmp/before-getting-started-sidebar.txt` and screenshot to `/tmp/before-getting-started.png`.

- [ ] **Step 3a: Create `platform/developer-guide/docs/Getting-Started/.pages`**

  ```yaml
  title: Getting Started
  nav:
    - Quick Start: quick-start.md
    - AI Assistance: ai-quick-start.md
    - System Requirements: system-requirements.md
    - Installation Guide
    - Skills Required for VC Developers: skills-required-for-VC-developers.md
  ```

- [ ] **Step 3b: Create `platform/developer-guide/docs/Getting-Started/Installation-Guide/.pages`**

  ```yaml
  title: Installation Guide
  nav:
    - Windows: windows.md
    - Linux: linux.md
    - MacOS: macOS.md
    - Local install with start-local: start-local.md
    - Post Installation Steps:
        - Setting Up Self Signed SSL Certificate: ../Post-Installation-Steps/01-setting-up-self-signed-ssl-cert.md
        - Configuring Email Notifications: ../Post-Installation-Steps/02-configuring-email-notifications.md
        - Configuring Asset Blob Storage: ../Post-Installation-Steps/03-configuring-asset-blob-storage.md
        - Importing Sample Data: ../Post-Installation-Steps/04-importing-sample-data.md
  ```

  The `..` parent-relative paths reference files in the sibling `Post-Installation-Steps/` folder. **Verify this works** by checking the post-build site output; `awesome-pages` accepts file paths relative to the folder containing the `.pages` file.

  If `..` paths are rejected by `awesome-pages` (older versions did not support them), fall back: in `Getting-Started/.pages`, append the Post Installation Steps inline group as a sibling of `Installation Guide` and document this menu-shape change in the commit message. Test which works in step 5.

- [ ] **Step 4: Update `platform/developer-guide/mkdocs.yml`**

  Use Edit with `old_string`:
  ```
      - Getting Started:
            - Quick Start: Getting-Started/quick-start.md
            - AI Assistance: Getting-Started/ai-quick-start.md
            - System Requirements: Getting-Started/system-requirements.md
            - Installation Guide:
                  - Windows: Getting-Started/Installation-Guide/windows.md
                  - Linux: Getting-Started/Installation-Guide/linux.md
                  - MacOS: Getting-Started/Installation-Guide/macOS.md
                  - Local install with start-local: Getting-Started/Installation-Guide/start-local.md
                  - Post Installation Steps:
                        - Setting Up Self Signed SSL Certificate: Getting-Started/Post-Installation-Steps/01-setting-up-self-signed-ssl-cert.md
                        - Configuring Email Notifications: Getting-Started/Post-Installation-Steps/02-configuring-email-notifications.md
                        - Configuring Asset Blob Storage: Getting-Started/Post-Installation-Steps/03-configuring-asset-blob-storage.md
                        - Importing Sample Data: Getting-Started/Post-Installation-Steps/04-importing-sample-data.md
            - Skills Required for VC Developers: skills-required-for-VC-developers.md
      - Architecture:
  ```
  and `new_string`:
  ```
      - Architecture:
  ```

- [ ] **Step 5: Post-change build + diff**

  ```bash
  rm -rf /tmp/after
  mkdocs build -f platform/developer-guide/mkdocs.yml -d /tmp/after --strict
  diff -r /tmp/before /tmp/after | grep -v "git-revision-date\|search_index.json\|sitemap" | tee /tmp/diff-getting-started.txt
  ```

  Expected: no "Only in" lines for HTML files. If `Post-Installation-Steps/*.html` show up as "Only in /tmp/before" (i.e., dropped), the `..` path approach failed — fall back to Option B as described in Step 3b.

- [ ] **Step 6: Post-change Playwright re-verification**

  Same procedure as Task 1 Step 6, target page `http://127.0.0.1:8005/Getting-Started/quick-start/`. Diff `/tmp/before-getting-started-sidebar.txt` vs `/tmp/after-getting-started-sidebar.txt` should be empty.

  Also click into `http://127.0.0.1:8005/Getting-Started/Post-Installation-Steps/01-setting-up-self-signed-ssl-cert/` — verify the active item shows as nested under Installation Guide → Post Installation Steps, and that `scroll-menu.js` keeps it in viewport.

- [ ] **Step 7: Commit**

  ```bash
  git add platform/developer-guide/docs/Getting-Started/.pages \
          platform/developer-guide/docs/Getting-Started/Installation-Guide/.pages \
          platform/developer-guide/mkdocs.yml
  git commit -m "$(cat <<'EOF'
  docs(nav): migrate Getting Started to awesome-pages .pages

  Inline nested group for Post Installation Steps preserves the
  current menu shape despite the filesystem split between
  Installation-Guide/ and Post-Installation-Steps/ sibling folders.

  See docs/superpowers/specs/2026-05-26-awesome-pages-migration-design.md.
  EOF
  )"
  ```

---

## Task 3: Migrate "Architecture"

**Files:**
- Create: `platform/developer-guide/docs/Back-End-Architecture/.pages`
- Modify: `platform/developer-guide/mkdocs.yml` (lines 121–125: remove `Architecture` branch)

Source nav being migrated (verify the exact lines with `grep -n "Architecture:" platform/developer-guide/mkdocs.yml` before editing):

```yaml
- Architecture:
      - Virto Atomic Architecture: Back-End-Architecture/atomic-architecture.md
      - Back End Architecture:
            - Tech Stack: Back-End-Architecture/01-tech-stack.md
            - Conceptual Overview: Back-End-Architecture/02-conceptual-overview.md
```

**Pitfall:** the top-level section is named "Architecture" but the underlying folder is `Back-End-Architecture/`. The first child `Virto Atomic Architecture` lives in the same folder as the `Back End Architecture:` inline group. Use inline nesting.

Representative page: `http://127.0.0.1:8005/Back-End-Architecture/atomic-architecture/`.

- [ ] **Step 1: Baseline build** (as Task 1)

- [ ] **Step 2: Baseline Playwright snapshot** → `/tmp/before-architecture-*`

- [ ] **Step 3: Create `platform/developer-guide/docs/Back-End-Architecture/.pages`**

  ```yaml
  title: Architecture
  nav:
    - Virto Atomic Architecture: atomic-architecture.md
    - Back End Architecture:
        - Tech Stack: 01-tech-stack.md
        - Conceptual Overview: 02-conceptual-overview.md
  ```

  Note: `title: Architecture` overrides the folder's natural label `Back-End-Architecture` so the top-level menu shows "Architecture" exactly as before.

  Also update `platform/developer-guide/docs/.pages` if line `- Architecture` does not yet resolve to this folder. With `title: Architecture` in the child `.pages`, the parent's `- Architecture` works only if `awesome-pages` resolves by `title:`. **Safer:** use explicit form in parent — edit `docs/.pages` line `- Architecture` to `- Architecture: Back-End-Architecture`.

- [ ] **Step 4: Update `platform/developer-guide/mkdocs.yml`**

  Edit `old_string`:
  ```
      - Architecture:
            - Virto Atomic Architecture: Back-End-Architecture/atomic-architecture.md
            - Back End Architecture:
                  - Tech Stack: Back-End-Architecture/01-tech-stack.md
                  - Conceptual Overview: Back-End-Architecture/02-conceptual-overview.md
      - Security and Compliance:
  ```
  `new_string`:
  ```
      - Security and Compliance:
  ```

  Also Edit `docs/.pages` to replace `- Architecture` with `- Architecture: Back-End-Architecture`.

- [ ] **Step 5: Post-change build + diff** → `/tmp/diff-architecture.txt`

- [ ] **Step 6: Playwright re-verification** at `/Back-End-Architecture/atomic-architecture/`. Diff sidebar text → empty.

- [ ] **Step 7: Commit**

  ```bash
  git add platform/developer-guide/docs/.pages \
          platform/developer-guide/docs/Back-End-Architecture/.pages \
          platform/developer-guide/mkdocs.yml
  git commit -m "docs(nav): migrate Architecture to awesome-pages .pages"
  ```

---

## Task 4: Migrate "Security and Compliance"

**Files:**
- Create: `platform/developer-guide/docs/Security-and-Compliance/.pages`
- Modify: `platform/developer-guide/mkdocs.yml` (lines 126–127)

Source nav:

```yaml
- Security and Compliance:
      - SOC 2 Type II Compliance: Security-and-Compliance/soc2-type-ii.md
```

Single child, but we still create a `.pages` so future additions don't depend on filename alphabetization.

Representative page: `http://127.0.0.1:8005/Security-and-Compliance/soc2-type-ii/`.

- [ ] **Step 1: Baseline build**
- [ ] **Step 2: Baseline Playwright snapshot** → `/tmp/before-security-*`
- [ ] **Step 3: Create `platform/developer-guide/docs/Security-and-Compliance/.pages`**

  ```yaml
  title: Security and Compliance
  nav:
    - SOC 2 Type II Compliance: soc2-type-ii.md
  ```

  Update `docs/.pages`: replace `- Security and Compliance` with `- Security and Compliance: Security-and-Compliance`.

- [ ] **Step 4: Remove the `Security and Compliance` branch from `mkdocs.yml`**

  `old_string`:
  ```
      - Security and Compliance:
            - SOC 2 Type II Compliance: Security-and-Compliance/soc2-type-ii.md
      - CLI Tools:
  ```
  `new_string`:
  ```
      - CLI Tools:
  ```

- [ ] **Step 5: Build + diff** → `/tmp/diff-security.txt`
- [ ] **Step 6: Playwright re-verification**
- [ ] **Step 7: Commit**

  ```bash
  git add platform/developer-guide/docs/.pages \
          platform/developer-guide/docs/Security-and-Compliance/.pages \
          platform/developer-guide/mkdocs.yml
  git commit -m "docs(nav): migrate Security and Compliance to awesome-pages .pages"
  ```

---

## Task 5: Migrate "CLI Tools"

**Files:**
- Create: `platform/developer-guide/docs/CLI-tools/.pages`
- Modify: `platform/developer-guide/mkdocs.yml` (lines 128–139)

Source nav:

```yaml
- CLI Tools:
      - Overview: CLI-tools/overview.md
      - Getting Started: CLI-tools/getting-started.md
      - Build Automation: CLI-tools/build-automation.md
      - Package Management: CLI-tools/package-management.md
      - Grab Migrator Utility Quickstart: CLI-tools/grab-migrator.md
      - Cold Start Optimization and Data Migration: CLI-tools/cold-start-and-data-migration.md
      - Installing and Updating Platform and Modules: CLI-tools/install-and-update-platform-and-modules.md
      - Managing Platform and Modules with CLI: CLI-tools/more-targets.md
      - Virto Cloud:
            - Overview: CLI-tools/virto-cloud-overview.md
            - Using Virto Cloud: CLI-tools/virto-cloud.md
```

`Virto Cloud` is an inline group (its two files live in `CLI-tools/` directly, no `Virto-Cloud/` sub-folder). Confirm: `ls platform/developer-guide/docs/CLI-tools/Virto-Cloud/` should fail.

Representative page: `http://127.0.0.1:8005/CLI-tools/overview/`.

- [ ] **Step 1: Baseline build**
- [ ] **Step 2: Baseline Playwright snapshot** → `/tmp/before-cli-tools-*`
- [ ] **Step 3: Create `platform/developer-guide/docs/CLI-tools/.pages`**

  ```yaml
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

  `docs/.pages` already has `- CLI Tools: CLI-tools` from Task 1 — no further change there.

- [ ] **Step 4: Edit `mkdocs.yml`**, remove the entire `- CLI Tools:` branch (lines 128–139).

  `old_string` is the full block above (12 lines). `new_string` is empty (just the indentation context that follows).

  Use the actual surrounding context for the Edit's `old_string` (3 lines before, 3 after) to make it unique.

- [ ] **Step 5: Build + diff** → `/tmp/diff-cli-tools.txt`
- [ ] **Step 6: Playwright re-verification**. Also navigate to `http://127.0.0.1:8005/CLI-tools/virto-cloud/` to confirm the inline `Virto Cloud` group renders nested.
- [ ] **Step 7: Commit**

  ```bash
  git add platform/developer-guide/docs/CLI-tools/.pages \
          platform/developer-guide/mkdocs.yml
  git commit -m "docs(nav): migrate CLI Tools to awesome-pages .pages"
  ```

---

## Task 6: Migrate "Configuration Reference"

**Files:**
- Create: `platform/developer-guide/docs/Configuration-Reference/.pages`
- Modify: `platform/developer-guide/mkdocs.yml` (lines 263–264)

Source:
```yaml
- Configuration Reference:
      - Appsettings.json: Configuration-Reference/appsettingsjson.md
```

Representative page: `http://127.0.0.1:8005/Configuration-Reference/appsettingsjson/`.

- [ ] **Step 1: Baseline build**
- [ ] **Step 2: Baseline Playwright snapshot** → `/tmp/before-config-*`
- [ ] **Step 3: Create `platform/developer-guide/docs/Configuration-Reference/.pages`**

  ```yaml
  title: Configuration Reference
  nav:
    - Appsettings.json: appsettingsjson.md
  ```

  Update `docs/.pages`: replace `- Configuration Reference` with `- Configuration Reference: Configuration-Reference`.

- [ ] **Step 4: Edit `mkdocs.yml`** to remove the `- Configuration Reference:` block.

  `old_string`:
  ```
      - Configuration Reference:
            - Appsettings.json: Configuration-Reference/appsettingsjson.md
      - Platform Manager:
  ```
  `new_string`:
  ```
      - Platform Manager:
  ```

- [ ] **Step 5: Build + diff**
- [ ] **Step 6: Playwright re-verification**
- [ ] **Step 7: Commit**

  ```bash
  git add platform/developer-guide/docs/.pages \
          platform/developer-guide/docs/Configuration-Reference/.pages \
          platform/developer-guide/mkdocs.yml
  git commit -m "docs(nav): migrate Configuration Reference to awesome-pages .pages"
  ```

---

## Task 7: Migrate "Platform Manager"

**Files:**
- Create: `platform/developer-guide/docs/Platform-Manager/.pages`
- Create: `platform/developer-guide/docs/Platform-Manager/Extensibility-Points/.pages`
- Modify: `platform/developer-guide/mkdocs.yml` (lines 265–275)

Source:
```yaml
- Platform Manager:
      - Style Guide: Platform-Manager/style-guide.md
      - UI Scroll Directive: Platform-Manager/ui-scroll-directive.md
      - Localization: Platform-Manager/localization.md
      - Extensibility Points:
            - Extending Main Menu: Platform-Manager/Extensibility-Points/extending-main-menu.md
            - Blades and Navigation: Platform-Manager/Extensibility-Points/blades-and-navigation.md
            - Metaform: Platform-Manager/Extensibility-Points/metaform.md
            - Widgets: Platform-Manager/Extensibility-Points/widgets.md
            - Extending Grid Columns: Platform-Manager/Extensibility-Points/extending-grid-columns.md
            - Blade Toolbar: Platform-Manager/Extensibility-Points/blade-toolbar.md
```

`Extensibility Points/` is a real sub-folder. Use a separate `.pages` for it.

Representative page: `http://127.0.0.1:8005/Platform-Manager/style-guide/`.

- [ ] **Step 1: Baseline build**
- [ ] **Step 2: Baseline Playwright snapshot** → `/tmp/before-platform-manager-*`
- [ ] **Step 3a: Create `platform/developer-guide/docs/Platform-Manager/.pages`**

  ```yaml
  title: Platform Manager
  nav:
    - Style Guide: style-guide.md
    - UI Scroll Directive: ui-scroll-directive.md
    - Localization: localization.md
    - Extensibility Points: Extensibility-Points
  ```

  Update `docs/.pages`: replace `- Platform Manager` with `- Platform Manager: Platform-Manager`.

- [ ] **Step 3b: Create `platform/developer-guide/docs/Platform-Manager/Extensibility-Points/.pages`**

  ```yaml
  title: Extensibility Points
  nav:
    - Extending Main Menu: extending-main-menu.md
    - Blades and Navigation: blades-and-navigation.md
    - Metaform: metaform.md
    - Widgets: widgets.md
    - Extending Grid Columns: extending-grid-columns.md
    - Blade Toolbar: blade-toolbar.md
  ```

- [ ] **Step 4: Edit `mkdocs.yml`**, remove the entire `- Platform Manager:` branch.

  `old_string` covers lines 265–275 inclusive, plus 1 line before and 1 after for uniqueness.

- [ ] **Step 5: Build + diff** → `/tmp/diff-platform-manager.txt`
- [ ] **Step 6: Playwright re-verification**. Click into one Extensibility Points page (e.g. `/Platform-Manager/Extensibility-Points/widgets/`) and verify auto-scroll.
- [ ] **Step 7: Commit**

  ```bash
  git add platform/developer-guide/docs/.pages \
          platform/developer-guide/docs/Platform-Manager/.pages \
          platform/developer-guide/docs/Platform-Manager/Extensibility-Points/.pages \
          platform/developer-guide/mkdocs.yml
  git commit -m "docs(nav): migrate Platform Manager to awesome-pages .pages"
  ```

---

## Task 8: Migrate "Fundamentals"

**Files:**
- Create: `platform/developer-guide/docs/Fundamentals/.pages` (top-level for the section)
- Create: one `.pages` per direct sub-folder of `Fundamentals/`
- Create: deeper `.pages` for nested sub-folders that exist on disk (e.g. `Fundamentals/Persistence/DB-Agnostic/`, `Fundamentals/Indexed-Search/indexing/`, `Fundamentals/Security/authentication/`)
- Modify: `platform/developer-guide/mkdocs.yml` (lines 140–262: remove `Fundamentals` branch — verify range with `grep -n` before editing)

This is the largest non-GraphQL section. The source nav spans ~120 lines.

**Strategy:** generate the `.pages` files mechanically from the existing nav block. Treat each sub-group as either:
- A sub-folder that exists on disk → its own `.pages` with `nav:`.
- An inline group of loose files in the parent folder → inline group in the parent `.pages` (`- Group Name:` with nested list).

Use this checklist of Fundamentals sub-sections (verify with `ls platform/developer-guide/docs/Fundamentals/` before starting):

| Source group | Disk folder | Treatment |
| --- | --- | --- |
| Caching | `Fundamentals/Caching/` | Sub-folder `.pages` |
| Data Import | `Fundamentals/Data-Import/` | Sub-folder `.pages` |
| Indexed Search | `Fundamentals/Indexed-Search/` | Sub-folder `.pages` with nested `indexing/`, `search/`, `integration/` |
| Intent Search | `Fundamentals/Intent-Search/` | Sub-folder `.pages` |
| Persistence | `Fundamentals/Persistence/` | Sub-folder `.pages` with nested `DB-Agnostic/` and inline `Concurrency-handling` |
| Modularity | `Fundamentals/Modularity/` | Sub-folder `.pages` |
| Scalability | `Fundamentals/Scalability/` | Sub-folder `.pages` |
| Event Driven Development | `Fundamentals/Event-Driven-Development/` | Sub-folder `.pages` with inline `Event Providers` group |
| Testing | `Fundamentals/Testing/` | Single file — list in `Fundamentals/.pages` directly as `- Testing: Testing/testing.md` |
| Payments | `Fundamentals/Payments/` | Sub-folder `.pages` |
| Shipments | `Fundamentals/Shipments/` | Sub-folder `.pages` |
| Taxes | `Fundamentals/Taxes/` | Sub-folder `.pages` |
| SEO | `Fundamentals/SEO/` | Sub-folder `.pages` |
| Dynamic Properties | `Fundamentals/Dynamic-Properties/` | Sub-folder `.pages` |
| Notifications | `Fundamentals/Notifications/` | Sub-folder `.pages` |
| Security | `Fundamentals/Security/` | Sub-folder `.pages` with nested `authentication/`, `authorization/`, `extensions/` |
| Logging | `Fundamentals/Logging/` | Sub-folder `.pages` |

Representative page for Playwright: `http://127.0.0.1:8005/Fundamentals/Caching/01-overview/`.

- [ ] **Step 1: Baseline build**

- [ ] **Step 2: Baseline Playwright snapshot** → `/tmp/before-fundamentals-*`

  Important: also snapshot a deep nested page like `/Fundamentals/Security/authentication/oidc/` to verify deep nav after.

- [ ] **Step 3a: Create `Fundamentals/.pages`**

  ```yaml
  title: Fundamentals
  nav:
    - Caching
    - Data Import: Data-Import
    - Indexed Search: Indexed-Search
    - Intent Search: Intent-Search
    - Persistence
    - Modularity
    - Scalability
    - Event Driven Development: Event-Driven-Development
    - Testing: Testing/testing.md
    - Payments
    - Shipments
    - Taxes
    - SEO
    - Dynamic Properties: Dynamic-Properties
    - Notifications
    - Security
    - Logging
  ```

  Update `docs/.pages`: `- Fundamentals` stays as is.

- [ ] **Step 3b: Create `Fundamentals/Caching/.pages`**

  ```yaml
  title: Caching
  nav:
    - Overview: 01-overview.md
    - Cache Configuration: 02-cache-configuration.md
    - Setting Up Redis Backplane for Scaling Out: 03-setting-up-Redis.md
  ```

- [ ] **Step 3c: Create `Fundamentals/Data-Import/.pages`**

  ```yaml
  title: Data Import
  nav:
    - Main Concept: 01-main-concept.md
    - Building Custom Importer: 02-building-custom-importer.md
    - Import App: import-app.md
  ```

- [ ] **Step 3d: Create `Fundamentals/Indexed-Search/.pages`**

  ```yaml
  title: Indexed Search
  nav:
    - Overview: overview.md
    - Search Query Syntax: search-query-syntax-reference.md
    - Indexing: indexing
    - Search: search
    - Integration: integration
    - Configuration: configuration.md
  ```

  Plus:

  `Fundamentals/Indexed-Search/indexing/.pages`:
  ```yaml
  title: Indexing
  nav:
    - Overview: overview.md
    - Indexing in Platform Manager: indexing-in-platform-manager.md
    - Blue-Green Indexing: blue-green-indexing.md
  ```

  `Fundamentals/Indexed-Search/search/.pages`:
  ```yaml
  title: Search
  nav:
    - Overview: overview.md
    - Faceted Search Overview and Configuration: faceted-search.md
  ```

  `Fundamentals/Indexed-Search/integration/.pages`:
  ```yaml
  title: Integration
  nav:
    - Elasticsearch 9:
        - Overview: elastic-search-9.md
        - Semantic Search: semantic-search-es9.md
    - Elasticsearch 8:
        - Overview: elastic-search-8.md
        - Semantic Search: semantic-search.md
    - Elastic App Search:
        - Overview: elastic-app-search-overview.md
        - Configuration: configuring-elastic-app-search.md
        - Using Analytics: using-analytics.md
        - Tuning Search Relevance: search_relevance_tuning.md
    - Elasticsearch: configuring-elasticsearch.md
    - OpenSearch: opensearch.md
    - Azure Cognitive Search: configuring-azure-cognitive-search.md
    - Algolia: algolia.md
    - Lucene: lucene.md
  ```

- [ ] **Step 3e: Create `Fundamentals/Intent-Search/.pages`**

  ```yaml
  title: Intent Search
  nav:
    - Overview: overview.md
    - Installation and Configuration: installation-and-configuration.md
    - Examples: examples.md
  ```

- [ ] **Step 3f: Create `Fundamentals/Persistence/.pages` and `Fundamentals/Persistence/DB-Agnostic/.pages`**

  `Fundamentals/Persistence/.pages`:
  ```yaml
  title: Persistence
  nav:
    - DB Agnostic Architecture: DB-Agnostic
    - Concurrency Handling: Concurrency-handling/concurrency-handling.md
  ```

  `Fundamentals/Persistence/DB-Agnostic/.pages`:
  ```yaml
  title: DB Agnostic Architecture
  nav:
    - Overview: overview.md
    - Configuring VC with DB Providers: configuring-vc-with-db-providers.md
    - Creating Custom Module with DB Agnostic Approach: creating-custom-module.md
    - Transforming Custom Module to Support DB Agnostic Approach: transforming-custom-module.md
  ```

- [ ] **Step 3g: Create `Fundamentals/Modularity/.pages`**

  ```yaml
  title: Modularity
  nav:
    - Overview: 01-overview.md
    - Folder Structure: 02-folder-structure.md
    - Versioning and Dependencies: 03-versioning-and-dependencies.md
    - Optional Dependency between Modules: optional-dependency.md
    - Loading Modules into App Process: 04-loading-modules-into-app-process.md
    - IPlatformStartup: IPlatformStartup.md
    - Module.manifest File: 06-module-manifest-file.md
    - Best Practices: 05-best-practices.md
    - Configuration: configuration.md
    - Azure App Configuration: azure-app-configuration.md
  ```

- [ ] **Step 3h: Create `Fundamentals/Scalability/.pages`**

  ```yaml
  title: Scalability
  nav:
    - Scalability Options: scalability-options.md
    - Scaling Configuration on Azure Cloud: scaling-configuration-on-azure-cloud.md
  ```

- [ ] **Step 3i: Create `Fundamentals/Event-Driven-Development/.pages`**

  ```yaml
  title: Event Driven Development
  nav:
    - Using Domain Events: using-domain-events.md
    - Event Providers:
        - Webhooks: webhooks.md
        - Event Bus:
            - Overview: event-bus.md
            - Configuration: event-bus-configuration.md
  ```

- [ ] **Step 3j: Create remaining sub-folder `.pages` files**

  Apply the same mechanical translation for: `Fundamentals/Payments/`, `Fundamentals/Shipments/`, `Fundamentals/Taxes/`, `Fundamentals/SEO/`, `Fundamentals/Dynamic-Properties/`, `Fundamentals/Notifications/`. The source nav lines are 210–233 of the original `mkdocs.yml` (verify with `grep -n`).

  Each follows the pattern: `title: <Section Name>`, then `nav:` listing each file with its display label and filename (relative to that folder).

- [ ] **Step 3k: Create `Fundamentals/Security/.pages` and nested folder `.pages`**

  `Fundamentals/Security/.pages`:
  ```yaml
  title: Security
  nav:
    - Overview: overview.md
    - Authentication: authentication
    - Authorization: authorization
    - Encryption and Signing Credentials: encryption-and-signing-credentials.md
    - Extensions: extensions
    - Security in Depth: security-in-depth.md
    - Password Management: passwords-management.md
    - Configuration: configuration.md
  ```

  `Fundamentals/Security/authentication/.pages`:
  ```yaml
  title: Authentication
  nav:
    - Overview: overview.md
    - Username and Password:
        - Issuing and Using Access Token: issuing-and-using-access-token.md
        - Access Token and Cookie Mixed Authentication: access-token-and-cookie-mixed-auth.md
        - API Key Authentication: api-key-authentication.md
    - OpenId Connect: oidc.md
    - Virto as Identity Provider: virto-as-identity-provider.md
  ```

  `Fundamentals/Security/authorization/.pages`:
  ```yaml
  title: Authorization
  nav:
    - Overview: overview.md
    - Global Permissions: global-permissions.md
    - Scope Based Permissions: scope-based-permissions.md
  ```

  `Fundamentals/Security/extensions/.pages`:
  ```yaml
  title: Extensions
  nav:
    - Extending Authorization Policies: extending-authorization-policies.md
    - Extending ASP.NET Identity UserManager and RoleManager: extending-usermanager-and-rolemanager.md
    - Adding Azure AD as SSO Provider: adding-azure-as-sso-provider.md
    - Adding Google as SSO Provider: adding-google-as-sso-provider.md
  ```

- [ ] **Step 3l: Create `Fundamentals/Logging/.pages`**

  ```yaml
  title: Logging
  nav:
    - Overview: overview.md
    - Updating to Serilog Integrated Version: how-to-update.md
    - AppInsights: application-insights.md
    - Extending Logging: extended-logging.md
    - Seq Log Module: seq-module.md
  ```

- [ ] **Step 4: Remove the `Fundamentals:` branch from `mkdocs.yml`**

  Use `grep -n "^    - Fundamentals:" platform/developer-guide/mkdocs.yml` and `grep -n "^    - Configuration Reference:" platform/developer-guide/mkdocs.yml` to find the exact start and end. Edit out the entire range.

- [ ] **Step 5: Build + diff** → `/tmp/diff-fundamentals.txt`

  Critical: this is the biggest single migration. Read the diff line by line. Any `Only in /tmp/before` or `Only in /tmp/after` for `.html` files means a page disappeared or got duplicated. Most likely cause: a sub-folder `.pages` is missing or a file is not listed.

- [ ] **Step 6: Playwright re-verification**

  Test at minimum:
  - `/Fundamentals/Caching/01-overview/`
  - `/Fundamentals/Indexed-Search/integration/elastic-search-9/` (deep nested)
  - `/Fundamentals/Security/authentication/oidc/` (deep nested)
  - `/Fundamentals/Event-Driven-Development/event-bus/` (inline nested group)

  Confirm sidebar text identical, screenshots match, no console errors, active item in viewport on each.

- [ ] **Step 7: Commit**

  ```bash
  git add platform/developer-guide/docs/Fundamentals \
          platform/developer-guide/mkdocs.yml
  git commit -m "docs(nav): migrate Fundamentals to awesome-pages .pages"
  ```

---

## Task 9: Migrate "GraphQL API Reference (xAPI)"

**Files:**
- Create: `platform/developer-guide/docs/GraphQL-Storefront-API-Reference-xAPI/.pages`
- Create: many sub-folder `.pages` files (one per sub-folder that has its own `nav:` group in the source)
- Modify: `platform/developer-guide/mkdocs.yml` (lines 276–843)

This is the largest single section (~570 lines of nav). Sub-modules (xCart, xCatalog, xCMS, xOrder, xFile, xFrontend, Loyalty, xMarketing, News, Customer Review, Back-in-Stock, AI Document Processing) each map to a real sub-folder.

**Strategy:** same mechanical translation as Fundamentals. The repeating shape inside each xAPI sub-module is:

```
- xCart:
      - Overview: GraphQL-.../Cart/overview.md
      - Queries: [list of files]
      - Objects: [list of files]
      - Mutations: [list of files]
      - Examples: [optional]
```

Each xAPI sub-module → its own `.pages`, e.g. `GraphQL-Storefront-API-Reference-xAPI/Cart/.pages`. Whether `Queries`/`Objects`/`Mutations` are inline groups or real sub-folders depends on filesystem layout. Check each:

```bash
ls platform/developer-guide/docs/GraphQL-Storefront-API-Reference-xAPI/Cart/
ls platform/developer-guide/docs/GraphQL-Storefront-API-Reference-xAPI/Cart/queries/
```

If `queries/`, `objects/`, `mutations/` exist as real folders → each gets its own `.pages` with the file list. If files live directly in `Cart/` → use inline groups in `Cart/.pages`. Most xAPI sub-modules use real sub-folders (check `Cart/queries/`, `Catalog/objects/`, etc.).

Representative pages for Playwright:
- `/GraphQL-Storefront-API-Reference-xAPI/` (section root)
- `/GraphQL-Storefront-API-Reference-xAPI/Cart/queries/cart/` (deep, inline-or-folder)
- `/GraphQL-Storefront-API-Reference-xAPI/Catalog/examples/full-text-search/` (deep)

- [ ] **Step 1: Baseline build**
- [ ] **Step 2: Baseline Playwright snapshot** → `/tmp/before-graphql-*`. Snapshot all three representative pages.

- [ ] **Step 3: Create section root `GraphQL-Storefront-API-Reference-xAPI/.pages`**

  ```yaml
  title: GraphQL API Reference (xAPI)
  nav:
    - Overview: index.md
    - Setting Up Environment For Working With xAPI: getting-started.md
    - Extending xAPI Module: x-api-extensions.md
    - Updating xAPI Modules: update-xapi-modules.md
    - Multiregional Development: multiregional-development.md
    - Best Practices: best-practices.md
    - Troubleshooting: troubleshooting.md
    - Tools to Explore GraphQL:
        - GraphiQL: graphiql.md
        - Postman: postman.md
        - Curl: curl.md
    - AI Document Processing: PurchaseRequest
    - Back-in-Stock: Back-in-stock
    - xCart: Cart
    - xCatalog: Catalog
    - xCMS: Content
    - Customer Review: Reviews
    - xFile: File
    - xFrontend: xFrontend
    - Loyalty: Loyalty
    - xMarketing: Marketing
    - News: News
    - xOrder: Order
  ```

  Verify order matches the source `mkdocs.yml` nav lines 287–599+. **The order in this `.pages` must match the source exactly** — `awesome-pages` orders strictly by the `nav:` list.

  Also update `docs/.pages`: `- GraphQL API Reference (xAPI): GraphQL-Storefront-API-Reference-xAPI` (already in place from Task 1).

- [ ] **Step 3a–3l: Create one `.pages` per xAPI sub-folder**

  For each sub-module, create `.pages` files in:
  - `PurchaseRequest/.pages` plus `PurchaseRequest/Queries/.pages`, `PurchaseRequest/Objects/.pages`, `PurchaseRequest/Mutations/.pages`
  - `Back-in-stock/.pages` plus nested `Queries/`, `Objects/`, `Mutations/`
  - `Cart/.pages` plus nested `queries/`, `objects/`, `mutations/`
  - `Catalog/.pages` plus nested `queries/`, `objects/`, `examples/` — `Catalog/objects/` itself has sub-folders (`ProductConnection/`, `ProductAssociation/`, `category/`, `Price/`, `Property/`, `CommonVendor/`, `VideoConnection/`, `Facets/`) which each need a `.pages` based on their nav grouping in source
  - `Content/.pages` plus nested `Queries/`, `Objects/`
  - `Reviews/.pages` plus nested `Queries/`, `Objects/`, `Mutations/`
  - `File/.pages` plus nested `Queries/`, `Objects/`, `Mutations/`
  - `xFrontend/.pages` plus nested `objects/` (if exists)
  - `Loyalty/.pages` plus nested `queries/`, `objects/`
  - `Marketing/.pages` plus nested `queries/`, `objects/`, `mutations/`
  - `News/.pages` plus nested `queries/`, `objects/`
  - `Order/.pages` plus nested `queries/`, `objects/`

  Each `.pages` follows the same form:
  ```yaml
  title: <Display Title>
  nav:
    - <file order from source nav>
  ```

  Use the source `mkdocs.yml` (lines 276–843) as the authoritative ordering. For each sub-section heading in the source (e.g. `- Queries:` under `xCart:`), find the matching sub-folder on disk; the file list under that heading becomes the `nav:` of the sub-folder's `.pages`.

  **Time-saving approach:** open the source nav range in a YAML-aware editor, copy each block, paste into the corresponding `.pages`, and strip the folder prefix from every path. Each file path like `GraphQL-Storefront-API-Reference-xAPI/Cart/queries/cart.md` becomes `cart.md` inside `Cart/queries/.pages`.

  **Verification per sub-section:** after creating a sub-folder's `.pages`, run:
  ```bash
  ls platform/developer-guide/docs/GraphQL-Storefront-API-Reference-xAPI/Cart/queries/ | wc -l
  grep -c "^  - " platform/developer-guide/docs/GraphQL-Storefront-API-Reference-xAPI/Cart/queries/.pages
  ```
  Counts should match (modulo any `.pages` file itself, which `ls` will include).

- [ ] **Step 4: Edit `mkdocs.yml`**, remove the entire `- GraphQL API Reference (xAPI):` branch (lines 276–843 inclusive — verify).

- [ ] **Step 5: Build + diff** → `/tmp/diff-graphql.txt`

  Expect this diff to be huge (every xAPI HTML's sidebar changes). Filter `diff -r` output to flag only `Only in` lines:
  ```bash
  diff -r /tmp/before /tmp/after | grep "^Only in" | tee /tmp/missing-graphql.txt
  ```
  Expected: empty (no missing/extra HTML files). Anything else means a file was missed in a `.pages`.

- [ ] **Step 6: Playwright re-verification**

  Visit:
  - `/GraphQL-Storefront-API-Reference-xAPI/` (root)
  - `/GraphQL-Storefront-API-Reference-xAPI/Cart/queries/cart/` (one query)
  - `/GraphQL-Storefront-API-Reference-xAPI/Cart/mutations/add-item/` (one mutation)
  - `/GraphQL-Storefront-API-Reference-xAPI/Catalog/examples/full-text-search/` (examples sub-folder)
  - `/GraphQL-Storefront-API-Reference-xAPI/PurchaseRequest/Mutations/createPurchaseRequest/` (different casing — `Mutations/` with capital M)

  Sidebar text diff must be empty on each. Active-item-in-viewport check must return `"IN VIEWPORT"` on each.

- [ ] **Step 7: Commit**

  ```bash
  git add platform/developer-guide/docs/GraphQL-Storefront-API-Reference-xAPI \
          platform/developer-guide/mkdocs.yml
  git commit -m "docs(nav): migrate GraphQL API Reference (xAPI) to awesome-pages .pages"
  ```

---

## Task 10: Migrate "Extensibility"

**Files:**
- Create: `platform/developer-guide/docs/Extensibility/.pages`
- Create: `platform/developer-guide/docs/Extensibility/cms-integrations/.pages`
- Create: `platform/developer-guide/docs/Extensibility/cms-integrations/PageBuilder/.pages`
- Modify: `platform/developer-guide/mkdocs.yml` (lines 844–880)

Source nav being migrated:

```yaml
- Extensibility:
      - Overview: Extensibility/overview.md
      - Key Extensibility Points: Extensibility/key-extensibility-points.md
      - Extending Dynamic Expression Tree: Extensibility/extending-dynamic-expression-tree.md
      - Extending Product Completeness Evaluator: Extensibility/product-completeness-evaluator.md
      - Extending Application User: Extensibility/extending-application-user.md
      - Open Telemetry: Extensibility/opentelemetry.md
      - CMSs:
            - Overview: Extensibility/cms-integrations/cms-overview.md
            - Builder.io Setup: Extensibility/cms-integrations/builder-io-setup.md
            - Page Builder: [13 sub-items + Controls inline group of 15]
            - Sanity Setup: Extensibility/cms-integrations/sanity-setup.md
            - Contentful Setup: Extensibility/cms-integrations/contentful-setup.md
```

`CMSs` corresponds to disk folder `Extensibility/cms-integrations/` — title override needed. `Page Builder` corresponds to `cms-integrations/PageBuilder/`. `Controls` is an inline group inside `PageBuilder/.pages` (all 15 control files live directly in `PageBuilder/`).

Representative pages: `/Extensibility/overview/`, `/Extensibility/cms-integrations/PageBuilder/calendar/` (deep, inline group).

- [ ] **Step 1: Baseline build**
- [ ] **Step 2: Baseline Playwright snapshot** → `/tmp/before-extensibility-*`

- [ ] **Step 3a: Create `platform/developer-guide/docs/Extensibility/.pages`**

  ```yaml
  title: Extensibility
  nav:
    - Overview: overview.md
    - Key Extensibility Points: key-extensibility-points.md
    - Extending Dynamic Expression Tree: extending-dynamic-expression-tree.md
    - Extending Product Completeness Evaluator: product-completeness-evaluator.md
    - Extending Application User: extending-application-user.md
    - Open Telemetry: opentelemetry.md
    - CMSs: cms-integrations
  ```

  Update `docs/.pages`: replace `- Extensibility` with `- Extensibility: Extensibility` (keep `Extensibility` label since the folder name matches).

- [ ] **Step 3b: Create `platform/developer-guide/docs/Extensibility/cms-integrations/.pages`**

  ```yaml
  title: CMSs
  nav:
    - Overview: cms-overview.md
    - Builder.io Setup: builder-io-setup.md
    - Page Builder: PageBuilder
    - Sanity Setup: sanity-setup.md
    - Contentful Setup: contentful-setup.md
  ```

- [ ] **Step 3c: Create `platform/developer-guide/docs/Extensibility/cms-integrations/PageBuilder/.pages`**

  ```yaml
  title: Page Builder
  nav:
    - Overview: overview.md
    - Setup: page-builder-setup.md
    - Creating New Block: create-new-block.md
    - Server Descriptors: server-descriptors.md
    - Settings: settings.md
    - Schemas: schemas.md
    - Component Context: component-context.md
    - Asset File: asset.md
    - Controls:
        - Calendar: calendar.md
        - Checkbox: checkbox.md
        - Collection: collection.md
        - Color: color.md
        - Files: files.md
        - Header: header.md
        - Images: images.md
        - Markdown: markdown.md
        - Number: number.md
        - Object: object.md
        - Paragraph: paragraph.md
        - Search: search.md
        - Select: select.md
        - String: string.md
        - Text: text.md
  ```

- [ ] **Step 4: Edit `mkdocs.yml`**, remove the entire `- Extensibility:` branch.

  Use `grep -n "^    - Extensibility:" platform/developer-guide/mkdocs.yml` to find the exact start and `grep -n "^    - Operations:" platform/developer-guide/mkdocs.yml` to find the end (the line just after the Extensibility branch). Edit removes the inclusive range.

- [ ] **Step 5: Build + diff** → `/tmp/diff-extensibility.txt`. Expected: no "Only in" for HTML files.

- [ ] **Step 6: Playwright re-verification**

  At `/Extensibility/overview/` and `/Extensibility/cms-integrations/PageBuilder/calendar/`. Sidebar diff empty. Active-item-in-viewport check passes.

- [ ] **Step 7: Commit**

  ```bash
  git add platform/developer-guide/docs/.pages \
          platform/developer-guide/docs/Extensibility/.pages \
          platform/developer-guide/docs/Extensibility/cms-integrations/.pages \
          platform/developer-guide/docs/Extensibility/cms-integrations/PageBuilder/.pages \
          platform/developer-guide/mkdocs.yml
  git commit -m "docs(nav): migrate Extensibility to awesome-pages .pages"
  ```

---

## Task 11: Migrate "Operations"

**Files:**
- Create: `platform/developer-guide/docs/Operations/.pages`
- Modify: `platform/developer-guide/mkdocs.yml` (lines 881–882)

Source nav:

```yaml
- Operations:
      - Maintenance Tasks for SQL: Operations/maintenance-tasks-for-sql.md
```

Single child, but we still create a `.pages`. Representative page: `http://127.0.0.1:8005/Operations/maintenance-tasks-for-sql/`.

- [ ] **Step 1: Baseline build**
- [ ] **Step 2: Baseline Playwright snapshot** → `/tmp/before-operations-*`

- [ ] **Step 3: Create `platform/developer-guide/docs/Operations/.pages`**

  ```yaml
  title: Operations
  nav:
    - Maintenance Tasks for SQL: maintenance-tasks-for-sql.md
  ```

  Update `docs/.pages`: replace `- Operations` with `- Operations: Operations` (folder name matches label; the explicit form makes the relation unambiguous).

- [ ] **Step 4: Edit `mkdocs.yml`**

  `old_string`:
  ```
      - Operations:
            - Maintenance Tasks for SQL: Operations/maintenance-tasks-for-sql.md
      - Tutorials and How-tos:
  ```
  `new_string`:
  ```
      - Tutorials and How-tos:
  ```

- [ ] **Step 5: Build + diff** → `/tmp/diff-operations.txt`
- [ ] **Step 6: Playwright re-verification**
- [ ] **Step 7: Commit**

  ```bash
  git add platform/developer-guide/docs/.pages \
          platform/developer-guide/docs/Operations/.pages \
          platform/developer-guide/mkdocs.yml
  git commit -m "docs(nav): migrate Operations to awesome-pages .pages"
  ```

---

## Task 12: Migrate "Tutorials and How-tos"

**Files:**
- Create: `platform/developer-guide/docs/Tutorials-and-How-tos/.pages`
- Create: `platform/developer-guide/docs/Tutorials-and-How-tos/Tutorials/.pages`
- Create: `platform/developer-guide/docs/Tutorials-and-How-tos/How-tos/.pages`
- Modify: `platform/developer-guide/mkdocs.yml` (lines 883–923)

Source nav (abbreviated; full content at lines 883–923 of `mkdocs.yml`):

```yaml
- Tutorials and How-tos:
      - Overview: Tutorials-and-How-tos/overview.md
      - Tutorials:
            - Creating Custom Module from Template:
                  - Creating Custom Module from Template: Tutorials-and-How-tos/Tutorials/creating-custom-module.md
                  - Custom Modules Templates for Dotnet New: Tutorials-and-How-tos/Tutorials/module-templates-for-dotnet-new.md
            - Creating New Module from Scratch: Tutorials-and-How-tos/Tutorials/create-new-module-from-scratch.md
            - Deploying Module from Source Code: Tutorials-and-How-tos/Tutorials/deploy-module-from-source-code.md
            - Modules Development via Docker: Tutorials-and-How-tos/How-tos/docker-modules-development.md   # cross-folder
            - Extending Database Model: Tutorials-and-How-tos/Tutorials/extending-database-model.md
            - Building and Customizing Platform Manager UI: Tutorials-and-How-tos/Tutorials/build-platform-manager-ui.md
            - Extending Domain Models: Tutorials-and-How-tos/Tutorials/extending-domain-models.md
      - How-tos: [28 files in Tutorials-and-How-tos/How-tos/]
```

**Cross-folder pitfall:** `Modules Development via Docker` is grouped under `Tutorials:` in the source but its file lives in `How-tos/docker-modules-development.md`. Use a `..` relative path in `Tutorials-and-How-tos/Tutorials/.pages` to reference it, the same pattern as Task 2 (Post Installation Steps). If `..` paths don't work, fall back to listing it under How-tos and accept a documented menu shape change.

`Creating Custom Module from Template` is an inline group of two files inside `Tutorials/`.

Representative pages: `/Tutorials-and-How-tos/overview/`, `/Tutorials-and-How-tos/Tutorials/creating-custom-module/`, `/Tutorials-and-How-tos/How-tos/upgrading-to-dot-net-10/`.

- [ ] **Step 1: Baseline build**
- [ ] **Step 2: Baseline Playwright snapshot** → `/tmp/before-tutorials-*`

- [ ] **Step 3a: Create `platform/developer-guide/docs/Tutorials-and-How-tos/.pages`**

  ```yaml
  title: Tutorials and How-tos
  nav:
    - Overview: overview.md
    - Tutorials
    - How-tos
  ```

- [ ] **Step 3b: Create `platform/developer-guide/docs/Tutorials-and-How-tos/Tutorials/.pages`**

  ```yaml
  title: Tutorials
  nav:
    - Creating Custom Module from Template:
        - Creating Custom Module from Template: creating-custom-module.md
        - Custom Modules Templates for Dotnet New: module-templates-for-dotnet-new.md
    - Creating New Module from Scratch: create-new-module-from-scratch.md
    - Deploying Module from Source Code: deploy-module-from-source-code.md
    - Modules Development via Docker: ../How-tos/docker-modules-development.md
    - Extending Database Model: extending-database-model.md
    - Building and Customizing Platform Manager UI: build-platform-manager-ui.md
    - Extending Domain Models: extending-domain-models.md
  ```

- [ ] **Step 3c: Create `platform/developer-guide/docs/Tutorials-and-How-tos/How-tos/.pages`**

  ```yaml
  title: How-tos
  nav:
    - Upgrading to Virto Commerce on .NET10: upgrading-to-dot-net-10.md
    - Connecting Virto Commerce to AI agents via onX Adapter: connect-to-ai-agents-via-onx.md
    - Adding Case-Insensitive Search Support for PostgreSQL: adding-case-sensitive-search-support-for-postgre.md
    - Setting up Context7: using-context7.md
    - Using llms.txt: using-llms-txt.md
    - Swagger/API Integration in Virto Commerce: swagger-api.md
    - Generating C# Client from VC Swagger with NSwag: generating-c-sharp-client.md
    - Type Inheritance Support in Swagger API: type-inheritance-support-in-swagger.md
    - Adding Azure App Configuration: azure-app-configuration.md
    - Setting Up Prerender.io with Azure Application Gateway: setting-up-prerender-io-with-azure-app-gateway.md
    - Debugging VC Code without Source Code: debugging.md
    - Configuring Multiple Stores: configuring-multiple-stores.md
    - Configuring Multiple Stores on Virto Cloud: configuring-multiple-stores-on-virto-cloud.md
    - Product Snapshot Module Architecture and Extensibility: product-snapshot.md
    - Extending Cart Query With Custom Parameter: extending-cart-query-with-custom-parameter.md
    - Customizing Cart Validation Policies: customizing-cart-validation-policies.md
    - Overriding Rounding Policy: overriding-rounding-policy.md
    - Using Feature Flags with VC Platform and Frontend: feature-flags.md
    - Using responseGroup in Virto Commerce REST APIs: using-responseGroups-in-rest-api.md
    - Partial Updates for Entities Using PATCH-Endpoint: update-using-patch.md
    - Generating PDFs: generating-pdfs.md
    - Health Checks: health-checks.md
    - JSON Web Token Authorization Mechanism: authorization-using-jwt.md
    - Sharing Bearer Tokens Across Multiple Instances: sharing-bearer-tokens.md
    - User Email Verification: user-email-verification.md
    - Enabling Embedded Mode for VC-Shell Instances: enable-embedded-mode-for-vc-shell.md
    - Migration to New xAPI Modules: migration-to-new-xapi-modules.md
    - Configuring Environments for Comparison: configuring-environments.md
  ```

  Note: `docker-modules-development.md` is also in `How-tos/`, but it is referenced from `Tutorials/.pages` via `../How-tos/docker-modules-development.md` so the menu shows it under Tutorials. To avoid duplicating it under How-tos, **do not list it** in `How-tos/.pages` if the `..` cross-reference works. If the cross-reference fails (verify in Step 5 diff), list it here at the position it currently occupies in the source nav.

- [ ] **Step 4: Edit `mkdocs.yml`**, remove the entire `- Tutorials and How-tos:` branch (lines 883–923).

  Use `grep -n "^    - Tutorials and How-tos:" platform/developer-guide/mkdocs.yml` and `grep -n "^    - Releases" platform/developer-guide/mkdocs.yml` to bracket.

- [ ] **Step 5: Build + diff** → `/tmp/diff-tutorials.txt`. Critical check: is `docker-modules-development.html` still in `/tmp/after/Tutorials-and-How-tos/How-tos/`? If not, the cross-folder reference failed — apply the fallback noted in Step 3b/3c.

- [ ] **Step 6: Playwright re-verification** at three representative pages

- [ ] **Step 7: Commit**

  ```bash
  git add platform/developer-guide/docs/Tutorials-and-How-tos \
          platform/developer-guide/mkdocs.yml
  git commit -m "docs(nav): migrate Tutorials and How-tos to awesome-pages .pages"
  ```

---

## Task 13: Migrate "Releases, Bundles, PBCs. Installation and Updates"

**Files:**
- Create: `platform/developer-guide/docs/Updating-Virto-Commerce-Based-Project/.pages`
- Modify: `platform/developer-guide/mkdocs.yml` (lines 924–931)

Source:

```yaml
- Releases, Bundles, PBCs. Installation and Updates:
      - Release Strategy Overview: Updating-Virto-Commerce-Based-Project/release-strategy-overview.md
      - Stable Releases: Updating-Virto-Commerce-Based-Project/stable-releases.md
      - Edge Releases: Updating-Virto-Commerce-Based-Project/edge-releases.md
      - Installing Specific Version: Updating-Virto-Commerce-Based-Project/installing-specific-version.md
      - Packaged Business Capabilities (PBCs) and PBCs Max: Updating-Virto-Commerce-Based-Project/pbcs.md
      - Outdated Strategy: Updating-Virto-Commerce-Based-Project/outdated-strategy.md
      - Useful Tips: Updating-Virto-Commerce-Based-Project/tips.md
```

Representative page: `http://127.0.0.1:8005/Updating-Virto-Commerce-Based-Project/release-strategy-overview/`.

- [ ] **Step 1: Baseline build**
- [ ] **Step 2: Baseline Playwright snapshot** → `/tmp/before-releases-*`
- [ ] **Step 3: Create `Updating-Virto-Commerce-Based-Project/.pages`**

  ```yaml
  title: Releases, Bundles, PBCs. Installation and Updates
  nav:
    - Release Strategy Overview: release-strategy-overview.md
    - Stable Releases: stable-releases.md
    - Edge Releases: edge-releases.md
    - Installing Specific Version: installing-specific-version.md
    - Packaged Business Capabilities (PBCs) and PBCs Max: pbcs.md
    - Outdated Strategy: outdated-strategy.md
    - Useful Tips: tips.md
  ```

  `docs/.pages` already has `- Releases, Bundles, PBCs. Installation and Updates: Updating-Virto-Commerce-Based-Project`.

- [ ] **Step 4: Edit `mkdocs.yml`**, remove the `- Releases, Bundles, PBCs...:` branch.

  `old_string`:
  ```
      - Releases, Bundles, PBCs. Installation and Updates:
            - Release Strategy Overview: Updating-Virto-Commerce-Based-Project/release-strategy-overview.md
            - Stable Releases: Updating-Virto-Commerce-Based-Project/stable-releases.md
            - Edge Releases: Updating-Virto-Commerce-Based-Project/edge-releases.md
            - Installing Specific Version: Updating-Virto-Commerce-Based-Project/installing-specific-version.md
            - Packaged Business Capabilities (PBCs) and PBCs Max: Updating-Virto-Commerce-Based-Project/pbcs.md
            - Outdated Strategy: Updating-Virto-Commerce-Based-Project/outdated-strategy.md
            - Useful Tips: Updating-Virto-Commerce-Based-Project/tips.md
      - ... | regex=^custom-apps-development/.+\.md$
  ```
  `new_string`:
  ```
      - ... | regex=^custom-apps-development/.+\.md$
  ```

- [ ] **Step 5: Build + diff**
- [ ] **Step 6: Playwright re-verification**
- [ ] **Step 7: Commit**

  ```bash
  git add platform/developer-guide/docs/Updating-Virto-Commerce-Based-Project/.pages \
          platform/developer-guide/mkdocs.yml
  git commit -m "docs(nav): migrate Releases, Bundles, PBCs to awesome-pages .pages"
  ```

---

## Task 14: Final Cleanup — Remove or Minimize Residual `nav:` Block

**Files:**
- Modify: `platform/developer-guide/mkdocs.yml`

After Tasks 1–13, the `nav:` block in `platform/developer-guide/mkdocs.yml` should contain only:

```yaml
nav:
    - ... | regex=^custom-apps-development/.+\.md$
```

The `custom-apps-development` glob was the pre-existing `awesome-pages` integration. With the rest migrated, this entry is redundant — `docs/.pages` already references the folder as `- Custom Apps Development: custom-apps-development`, and the folder's own `.pages` chain takes over.

- [ ] **Step 1: Baseline build**
- [ ] **Step 2: Baseline Playwright snapshot** → `/tmp/before-final-*`. Snapshot the root page plus one `custom-apps-development` deep page like `/custom-apps-development/vc-shell/getting-started/...`.

- [ ] **Step 3: Remove the entire `nav:` block from `mkdocs.yml`**

  Use Edit with `old_string`:
  ```
  # Page tree
  nav:
      - ... | regex=^custom-apps-development/.+\.md$
  ```
  and `new_string`:
  ```
  # Page tree
  ```

  (Or just delete `nav:` and the regex line, leaving the comment.)

- [ ] **Step 4: Build + diff**

  ```bash
  rm -rf /tmp/after
  mkdocs build -f platform/developer-guide/mkdocs.yml -d /tmp/after --strict
  diff -r /tmp/before /tmp/after | grep -v "git-revision-date\|search_index.json\|sitemap" | tee /tmp/diff-final.txt
  ```

  Expected: empty (no differences whatsoever — every page already comes from `.pages`).

- [ ] **Step 5: Playwright re-verification**

  Visit at minimum:
  - `/` (root, `index.md`)
  - `/getting-to-know-platform/` (former About)
  - `/Fundamentals/` and one deep Fundamentals page
  - `/GraphQL-Storefront-API-Reference-xAPI/` and one deep query page
  - `/custom-apps-development/vc-shell/` (pre-migrated section — verify still works)

  Sidebar diff vs Step 2 baseline must be empty.

- [ ] **Step 6: Run full-site link check**

  ```bash
  mkdocs build -f platform/developer-guide/mkdocs.yml -d /tmp/final --strict 2>&1 | tee /tmp/build-final.log
  grep -i "warning\|error" /tmp/build-final.log | grep -v "^INFO"
  ```

  Expected: no new warnings beyond those captured in Task 0's baseline.

- [ ] **Step 7: Commit**

  ```bash
  git add platform/developer-guide/mkdocs.yml
  git commit -m "$(cat <<'EOF'
  docs(nav): remove residual nav: from platform/developer-guide/mkdocs.yml

  All sections now driven by awesome-pages .pages files under
  platform/developer-guide/docs/. Navigation is fully filesystem-derived.

  Closes the migration started in
  docs/superpowers/specs/2026-05-26-awesome-pages-migration-design.md.
  EOF
  )"
  ```

---

## Task 15: Documentation Note for Future Contributors

**Files:**
- Create or modify: `platform/developer-guide/docs/CONTRIBUTING.md` (or wherever this guide's contributor notes live — check existing files first; if none, skip this task)

If a contributor doc exists for this guide, add a short note explaining the new convention.

- [ ] **Step 1: Check for existing contributor doc**

  ```bash
  ls platform/developer-guide/docs/CONTRIBUTING.md \
     platform/developer-guide/docs/Tutorials-and-How-tos/Tutorials/contribute*.md 2>/dev/null
  find platform/developer-guide/docs -iname "contribut*"
  ```

  If found, edit it. If nothing relevant, skip this task — the spec lives at `docs/superpowers/specs/2026-05-26-awesome-pages-migration-design.md` and is the source of truth.

- [ ] **Step 2: Add a section explaining `.pages`**

  Add this prose to the existing contributor doc:

  > ## Adding pages to the navigation
  >
  > Navigation for this guide is built from `.pages` files (one per folder under `docs/`), managed by the `awesome-pages` MkDocs plugin. **Do not edit `nav:` in `mkdocs.yml`** — there is no `nav:` block to edit. To add or move a page:
  >
  > 1. Create or move the `.md` file in the appropriate folder.
  > 2. Open the folder's `.pages` file. If it has a `nav:` block, add the new page to the list in the position you want it to appear. If you want to add a sub-section that has its own folder, reference the folder by name.
  > 3. If the page's H1 differs from the desired menu label, use the explicit form: `- "Display Name": file.md`.
  > 4. Build locally with `mkdocs serve -f platform/developer-guide/mkdocs.yml` to verify.

- [ ] **Step 3: Commit**

  ```bash
  git add <contributor-doc-path>
  git commit -m "docs: document .pages navigation convention for contributors"
  ```

---

## Self-Review Checklist (Plan Author)

After all tasks are executed, the following must be true:

- [ ] `platform/developer-guide/mkdocs.yml` has no `nav:` block (or only an empty / vestigial one).
- [ ] Every folder under `platform/developer-guide/docs/` that previously appeared in the `nav:` block has a `.pages` file.
- [ ] `mkdocs build --strict` succeeds with no warnings beyond the Task 0 baseline.
- [ ] No HTML files added or removed compared to the pre-migration baseline.
- [ ] Playwright sidebar DOM diff is empty for each migrated section's representative page.
- [ ] Active-item-in-viewport check passes for at least one deep page per section (`scroll-menu.js` still load-bearing).
- [ ] `custom-apps-development/` continues to work unchanged.
- [ ] All commits reference `docs/superpowers/specs/2026-05-26-awesome-pages-migration-design.md`.
