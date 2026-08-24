# Published size reduction: result

Date: 2026-08-24. Branch: feat/published-size-reduction.

## Measured effect

**Two different scales appear below and must not be confused.** Task 3's row
is a small, two-version trial that proved the mechanism. Task 4's row is a
live capture on the actual, fully assembled seven-guide, five-version tree —
the real result, and about thirty times larger than the trial. Media
deduplication needs no redeploy of any version; it lands automatically the
next time the tree is assembled for an image build (design document,
decision 1). Minification, by contrast, reaches only the version being
deployed from this branch, so it does not yet reach the four frozen
versions; see "Not achieved here" below.

| Measure | Before | After | Source |
| --- | --- | --- | --- |
| HTML in the sample guide (minification; reaches only the deployed version) | 635.5 MB (666,398,606 B) | 266.8 MB (279,744,113 B) | Evidence file, §4 |
| Binaries in a two-snapshot trial (small-scale proof, not the real result) | 1162 MB | 1110 MB | Task 3 Step 6 |
| Symlinks created in that trial | 0 | 808 | Task 3 Step 6 |
| Remaining duplicates in that trial | 51 MB | 0 B | Task 3 Step 6 |
| **Media deduplication on the assembled tree (the real result; no redeploy needed)** | — | assets pass: 9 folders, 99.0 MB freed. Binaries pass: 13,545 files, 1.5 GB freed. Total freed: 1.6 GB. Resulting tree: 3.4 GB. | Evidence file, §§1-2 |
| Symlinks created on the assembled tree | 0 | 13,545 files + 9 directories | Evidence file, §2 |
| Remaining duplicates on the assembled tree | — | 0.0 B | Evidence file, §2 |
| Published tree, for reference | 5086 MB | not redeployed | Task 2 Step 6 |

No separate "before" total for the assembled tree itself is cited above:
the 3.4 GB figure is the first real measurement of the fully assembled tree
taken anywhere in this work, captured after both dedup passes already ran,
so no pre-dedup total of that exact tree was ever measured to cite. The
freed-byte figures (99.0 MB, 1.5 GB, 1.6 GB total) are the real, captured
before/after effect of the two passes; a "before" total is left out rather
than derived by adding freed bytes back onto the after-total, since that
number was never itself measured.

## Verification performed

- Rendered text identical across 981 pages of the platform developer guide (evidence file, §3).
- All `pre` blocks byte-identical on the sample page after unquoting the one benign attribute-quoting difference: 21 pre blocks in `CLI-tools/build-automation/index.html`, whitespace-exact identical. A single-page spot check made during minify-config verification, superseded in scope (though not contradicted) by the durable, corpus-wide check below.
- Durable code-indentation check (this task's additional step): 587 pages checked, 2857 `<pre>` blocks total, 0 differed (evidence file, §6; script quoted in full at §7). See "Additional notes" below for the one excluded page.
- `./build.sh` exit 0; warning set unchanged against `.specs/baseline/build-warnings.txt` (9 normalized lines, `diff` empty).
- All file and directory symlinks resolve inside the output tree (covered by the test suite's dedup tests and, independently, by the linked PNG serving 200 inside the container trial below).
- Symlinks inside a real nginx image: 2910 present, linked PNG served with HTTP 200 (124,066 bytes) (evidence file, §5). This trial ran on a `platform/developer-guide`-only tree (five versions), not the assembled seven-guide tree behind the 13,545 figure above; it existed to prove the `COPY`/nginx mechanism, not to measure the saving, so its count is not comparable to that larger one.
- Visual check of navigation, tooltips, tables, and code blocks: substituted with curl checks against a local `http.server` (see below); this is a substitution for a visual check, not a completed one — layout was not judged.

## Not achieved here

Minification reached only the version deployed from this branch. The four frozen
versions keep their un-minified HTML, about 2293 MB, until they are
redeployed. See the follow-up plan named in the plan document.

Docker layer stratification, ACR retention, `navigation.prune`, and GIF
conversion remain open. See the Out of scope section of
`.specs/2026-08-20-published-size-reduction-design.md`.

## Port required

**versioned-build-cicd.py** changed and now imports **build_optimize.py**.
Release branches carry frozen copies of the build script, so a port must carry
both files or the frozen script fails at import.

## Additional notes

- **One page's broken sentence survives in the frozen versions**, and also
  currently survives in the published (un-minified) `latest` tree until the
  next deploy. The content fix (commit `8c41a95773`) corrected `<meta>` and
  `<head>` being swallowed on the SEO how-to page
  (`platform/developer-guide/docs/Fundamentals/SEO/add-seo-to-module.md`),
  but every already-published copy (the four frozen versions, and `latest`
  until redeployed) still serves the pre-fix markup. This is expected and
  consistent with how mike deploys, not an oversight. It also surfaced
  directly during this task's additional step: `htmlmin.minify` raises
  `OpenTagNotFoundError` on the pre-fix copy of that exact page
  (`Fundamentals/SEO/add-seo-to-module/index.html`) inside the exported
  `origin/gh-pages` `latest` tree, which is why that one page was excluded
  from the code-indentation check's counted sample rather than silently
  passed.
- **The gate has a known blind spot, wider than any single normalization
  quirk.** `check_rendered_text.py` compares decoded text only; it discards
  every HTML attribute before comparing, so it has zero coverage of
  attribute changes. One instance of that gap is `&nbsp;` normalizing to an
  ordinary space (Python's Unicode `\s` includes it), so a minification pass
  that swapped a non-breaking space for a breaking one would not be caught.
  More concretely, this branch turned two `mkdocs-minify-plugin` defaults
  from inert to active — `remove_optional_attribute_quotes` and
  `reduce_empty_attributes` — and both sit entirely outside what the gate
  checks. Rather than speculate about that exposure, it was measured
  directly: 40 random `latest` pages across all seven guides, run through
  the shipped `htmlmin` options, produced zero crashes and exactly one
  attribute change, present on 38 of the 40 — `data-clipboard-text=""`
  becoming a bare `data-clipboard-text` via `reduce_empty_attributes`,
  which is semantically identical in the DOM. No change touched `title`,
  `alt`, `aria-label`, or `href`. The rendered-text gate itself (unlike that
  40-page attribute spot check) ran on only one guide — 981 pages of the
  roughly 1,450 in the currently deployed version, all in the platform
  developer guide; the other six guides carry no equivalent gate run and
  rest on `./build.sh` completing with no new warnings. The gate must not
  be trusted beyond what it checks.
- **`remove_empty_space` is permanently rejected.** It deletes the whitespace
  text node between adjacent inline elements instead of collapsing it,
  concatenating adjacent link titles (for example, two prev/next footer link
  titles ran together with no space) on 603 of 981 pages of the platform
  developer guide, for no material additional byte saving over
  `remove_comments` alone. It must never be reintroduced.
- **The container symlink check ran successfully**, Docker was available
  after the daemon started. 2910 symlinks were present inside the built
  image and a symlinked PNG served over HTTP with a 200 and a non-zero body,
  proving both that `COPY` preserves symlinks and that nginx follows them.
  No GAP to record for this run.
