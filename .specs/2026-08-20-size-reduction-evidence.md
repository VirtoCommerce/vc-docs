# Published size reduction: evidence

These are verbatim captures, copied without reformatting from console output
recorded in agent reports under
`.superpowers/sdd/2026-08-20-published-size-reduction-plan/`, a
git-ignored, working-only directory that will not exist in the merged
repository. They are preserved here so the figures cited in
`.specs/2026-08-20-size-reduction-result.md` remain checkable after that
directory is gone. Section 7 preserves the full text of a script cited as
evidence, for the same reason.

## 1. Media deduplication on the assembled tree — Step 9 output

From a local `versioned-build.py` run against the fully assembled
seven-guide, five-version tree, launched with `PYTHONUNBUFFERED=1` to
capture Step 9/10 verbatim rather than reconstructing them from a partial
log. Commit `ee022c1c11` (2026-08-21). Recorded in `task-4-report.md`,
lines 1976 and 1978-1979.

```
  ✅ Replaced 9 assets folders with symlinks (99.0 MB freed)
  ✅ Replaced 13545 duplicate binaries with symlinks (1.5 GB freed)
✅ Build optimized! Total space saved: 1.6 GB
```

## 2. Media deduplication on the assembled tree — Step 10 size report

Same run as section 1, immediately following output. Recorded in
`task-4-report.md`, lines 1980-1992.

```
📋 Step 10: Report build size
Tree: site
Category            Size     Files
HTML              3.0 GB      8109
Images          354.8 MB      2396
JS               65.9 MB      1348
JSON             27.1 MB        57
Other             9.8 MB       167
Fonts             6.9 MB        71
CSS               6.9 MB       858
TOTAL             3.4 GB
Symlinks: 13545 file(s), 9 directory(ies)
Duplicate bytes in deduplicable types: 0.0 B
```

## 3. Rendered-text equivalence gate — final, shipped minify config

From the fifth and final pass of Task 6, run against the platform developer
guide with the shipped `htmlmin_opts` (`remove_comments: true` only).
Commit `66ce7a3286` (2026-08-21). Recorded in `task-6-report.md`, lines
574-575.

```
$ .venv-docs/bin/python check_rendered_text.py /tmp/minify-before site/platform/developer-guide
OK: rendered text identical across 981 page(s)
```

## 4. HTML byte measurement — final, shipped minify config

Same pass as section 3, `measure_site_size.py` before/after comparison.
Recorded in `task-6-report.md`, line 598.

```
HTML 666398606 bytes (635.5 MB) -> 279744113 bytes (266.8 MB), saving 58.0%
```

## 5. Container symlink survival check

From the Task 7 Docker trial. The tree under test was a `git archive` export
of `platform/developer-guide` only (one guide, five published versions:
`stable10`, `stable11`, `stable12`, `stable14`, `stable15`, `latest`), not
the assembled seven-guide tree — its purpose was to prove that `COPY`
preserves symlinks and that nginx follows them, not to measure the saving.
Recorded on 2026-08-24 in `task-7-report.md`, lines 182 (symlink count
inside the built image, via `find -type l | wc -l`) and 200 (the `curl`
check of a symlinked PNG served by the running container).

```
2910
```

```
GET /platform/developer-guide/stable15/Back-End-Architecture/media/atomic-architecture.png -> 200 124066 bytes
```

## 6. Durable code-indentation check — output

From the Task 7 additional step, run against `platform/developer-guide/latest/`
exported from `origin/gh-pages` (the published, un-minified tree), compared
against the same pages run through `htmlmin` with the options the shipped
`mkdocs-minify-plugin` configuration produces. Recorded on 2026-08-24 in
`task-7-report.md`, lines 320-326.

```
pages checked: 587
total <pre> blocks: 2857
pages with a difference: 0
pages that could not be minified (excluded from the count above): 1
  UNMINIFIABLE: Fundamentals/SEO/add-seo-to-module/index.html (OpenTagNotFoundError)
```

## 7. `check-code-indentation.py`, full text

The script that produced section 6, quoted in full because it is cited as
evidence for that result. Copied verbatim from
`.superpowers/sdd/2026-08-20-published-size-reduction-plan/check-code-indentation.py`
as it stands on branch `feat/published-size-reduction`; the file is
git-ignored and was never committed.

```python
"""
Durable code-indentation check (Task 7 additional step).

Purpose: check_rendered_text.py normalizes whitespace before comparing, so it
cannot detect a changed indentation inside a <pre> code sample. This script
closes that gap by comparing <pre> block text byte-for-byte, with whitespace
preserved exactly, between the published (un-minified) "latest" tree and the
same pages run through htmlmin with exactly the options the shipped
mkdocs-minify-plugin configuration produces.

Usage:
    .venv-docs/bin/python check-code-indentation.py <latest_dir>

<latest_dir> is expected to be a local export of
platform/developer-guide/latest/ from origin/gh-pages (see Task 7 report for
how it was produced: `git archive origin/gh-pages | tar -x -C <tmp>`).

Options mirror mkdocs_minify_plugin/plugin.py:134-143 (the plugin's hardcoded
output_opts dict), with remove_comments overridden to True, which is the one
key every shipped mkdocs.yml in this repo sets via htmlmin_opts. No other key
is overridden, matching the shipped configuration exactly.

Known limitation: <pre> block extraction below is regex-based
(PRE_BLOCK_RE), the same class of shortcut check_rendered_text.py's own
tag-matching once used before it was rewritten on html.parser. A `>`
inside a quoted attribute on the <pre> tag itself (for example
`<pre id="x" data-foo="a>b">`) would end the match early and mis-extract
the block silently. Material's generated markup does not produce that
shape, so this has not been observed in practice, but a reader relying on
this script for a differently-templated tree should not trust it beyond
this method without first rewriting extraction on html.parser, which would
remove the caveat entirely.
"""
import html
import re
import sys
from pathlib import Path

import htmlmin

# Exactly mkdocs_minify_plugin/plugin.py:134-143's output_opts dict, with
# remove_comments overridden to True to match every shipped mkdocs.yml's
# htmlmin_opts: {remove_comments: true}. No other key is touched.
OUTPUT_OPTS = {
    "remove_comments": True,
    "remove_empty_space": False,
    "remove_all_empty_space": False,
    "reduce_empty_attributes": True,
    "reduce_boolean_attributes": False,
    "remove_optional_attribute_quotes": True,
    "convert_charrefs": True,
    "keep_pre": False,
    "pre_tags": ("pre", "textarea"),
    "pre_attr": "pre",
}

PRE_BLOCK_RE = re.compile(r"<pre\b[^>]*>(.*?)</pre>", re.DOTALL | re.IGNORECASE)
TAG_RE = re.compile(r"<[^>]+>")


def extract_pre_texts(page_html: str) -> list[str]:
    """Return the displayed text of every <pre> block, tags stripped, entities
    unescaped, whitespace preserved exactly (no strip, no collapse)."""
    texts = []
    for match in PRE_BLOCK_RE.finditer(page_html):
        inner = match.group(1)
        stripped = TAG_RE.sub("", inner)
        texts.append(html.unescape(stripped))
    return texts


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: check-code-indentation.py <latest_dir>", file=sys.stderr)
        return 2

    latest_dir = Path(sys.argv[1])
    pages = sorted(
        p for p in latest_dir.rglob("*.html") if "<pre" in p.read_text(encoding="utf-8", errors="strict").lower()
    )

    pages_checked = 0
    total_blocks = 0
    differing_pages = []
    unminifiable_pages = []

    for page in pages:
        original = page.read_text(encoding="utf-8")

        try:
            minified = htmlmin.minify(original, **OUTPUT_OPTS)
        except Exception as exc:  # noqa: BLE001 - report and skip, do not mask
            # The published "latest" tree can carry a pre-existing content
            # defect that predates a later fix in the working tree (see the
            # SEO how-to page fixed in 8c41a95773: unbalanced <meta>/<head>
            # markup crashes htmlmin's parser). That page has no minified
            # counterpart to compare against, so it is reported separately
            # rather than silently skipped or allowed to abort the run.
            unminifiable_pages.append((str(page.relative_to(latest_dir)), type(exc).__name__))
            continue

        original_blocks = extract_pre_texts(original)
        minified_blocks = extract_pre_texts(minified)

        pages_checked += 1
        total_blocks += len(original_blocks)

        if original_blocks != minified_blocks:
            differing_pages.append(
                (str(page.relative_to(latest_dir)), len(original_blocks), len(minified_blocks))
            )

    print(f"pages checked: {pages_checked}")
    print(f"total <pre> blocks: {total_blocks}")
    print(f"pages with a difference: {len(differing_pages)}")
    for rel_path, n_before, n_after in differing_pages:
        print(f"  DIFFERS: {rel_path} (before {n_before} block(s), after {n_after} block(s))")

    print(f"pages that could not be minified (excluded from the count above): {len(unminifiable_pages)}")
    for rel_path, exc_name in unminifiable_pages:
        print(f"  UNMINIFIABLE: {rel_path} ({exc_name})")

    return 0 if not differing_pages else 1


if __name__ == "__main__":
    raise SystemExit(main())
```
