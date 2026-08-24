# Published size reduction: result

Date: 2026-08-24. Branch: feat/published-size-reduction.

## Measured effect

| Measure | Before | After | Source |
| --- | --- | --- | --- |
| HTML in the sample guide | 635.5 MB (666,398,606 B) | 266.8 MB (279,744,113 B) | Task 6 Step 9 |
| Binaries in a two-snapshot trial | 1162 MB | 1110 MB | Task 3 Step 6 |
| Symlinks created in that trial | 0 | 808 | Task 3 Step 6 |
| Remaining duplicates in that trial | 51 MB | 0 B | Task 3 Step 6 |
| Published tree, for reference | 5086 MB | not redeployed | Task 2 Step 6 |

## Verification performed

- Rendered text identical across 981 pages of the platform developer guide (Task 6 Step 7).
- All `pre` blocks byte-identical on the sample page: 21 pre blocks in `CLI-tools/build-automation/index.html`, whitespace-exact identical (Task 6 Step 8).
- Durable code-indentation check (this task's additional step, see below): 587 pages checked, 2857 `<pre>` blocks total, 0 differed.
- `./build.sh` exit 0; warning set unchanged against `.specs/baseline/build-warnings.txt` (9 normalized lines, `diff` empty).
- All file and directory symlinks resolve inside the output tree (covered by the test suite's dedup tests and, independently, by the linked PNG serving 200 inside the container trial below).
- Symlinks inside a real nginx image: 2910 present, linked PNG served with HTTP 200 (124,066 bytes).
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
- **The gate has a known blind spot.** `check_rendered_text.py` normalizes
  `&nbsp;` to an ordinary space, because Python's Unicode `\s` includes it. A
  minification pass that swapped a non-breaking space for a breaking one
  would not be caught. Low likelihood in Material output, but the gate must
  not be trusted beyond what it checks.
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
