# Published documentation size reduction implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Take an ACR tag of the docs image from about 2 GB to about 0.6 GB by deduplicating identical media across published versions, and cut 424 MB from the `gh-pages` working tree by enabling the HTML minification that is installed but inert.

**Architecture:** Media deduplication runs at image assembly time and replaces byte-identical binaries with relative symlinks to one canonical copy, so no HTML is rewritten, no version is redeployed, and no release branch is touched. It is the dominant lever because registry layers are gzip-compressed: media compresses 1.1x and dominates the image, while HTML compresses 15.5x and dominates only the tree. Minification is enabled through options on the already-declared `minify` plugin and reaches `latest` immediately; the four frozen versions get it only when redeployed, which is a separate follow-up plan. Shared optimization code moves into **build_optimize.py**, which both build scripts import, because they had drifted: the CI script deduplicated theme assets and the local script did nothing at all.

**Tech Stack:** MkDocs 1.6.1, mkdocs-material 9.5.27, mkdocs-minify-plugin 0.8.0 with htmlmin2 0.1.13, mike 2.2.0, Python 3.9 or higher, GitHub Actions.

**Spec:** `.specs/2026-08-20-published-size-reduction-design.md`

## Global Constraints

- Planning documents live in **.specs**, never under **docs**. Everything under **docs** is published at the root of docs.virtocommerce.org.
- There is no unit test framework in this repository and none is introduced. Tests are plain `python3` scripts using `assert`, runnable with no new pip dependency. Verification is those scripts plus `./build.sh`.
- Commit messages and all code comments are in English. No AI attribution of any kind in commit messages.
- Never write to `gh-pages` by hand. mike owns that branch. Nothing in this plan modifies it. Reading it with `git ls-tree` or `git show` is fine and is how baselines are taken.
- Never run **versioned-build-cicd.py** for verification. It deploys with `mike --push`.
- **versioned-build.py** runs `git reset --hard origin/gh-pages` inside the **gh-pages** folder at its Step 4. That discards anything local in that folder. Task 4 fixes the consequence for reporting, but the reset stays; do not run the script if the local **gh-pages** folder holds anything you need.
- `deduplicate_binaries` must be called **after** `deduplicate_assets`. `os.walk` does not descend into symlinked directories, so running second skips the nested `assets/` trees the earlier pass already replaced.
- Deduplication must be deterministic: the canonical copy is the first path yielded by a sorted walk. Non-determinism would make the output tar differ between identical builds.
- One extension predicate. The optimizer and the size harness must classify deduplicable files identically, or the reported "remaining duplicates" figure describes a different file set from the one that was optimized.
- Any walk that inspects symlinks must inspect `dirnames` as well as `filenames`. `deduplicate_assets` creates symlinks to directories, which never appear in `filenames`.
- Do not enable `cache_safe`, `minify_js`, or `minify_css` on the `minify` plugin. See decisions 8 and 9 in the spec.
- Commit messages must not state a measured percentage that the task did not itself measure. Record the real number or omit it.
- `release/stableNN` branches carry their own frozen copies of the build scripts. Nothing in this plan changes a release branch. The follow-up redeploy plan must port **build_optimize.py** alongside **versioned-build-cicd.py**, or a frozen script fails at import.
- macOS is case-insensitive. A local `./build.sh` link warning after any case-only rename may be a phantom. Cross-check `git ls-tree` against `ls` before acting on one.
- New file names use underscores, not dashes. Every file this plan creates is imported by another file, and a dash makes a module unimportable. The existing dashed scripts keep their names.

---

## File Structure

| File | Status | Responsibility |
| --- | --- | --- |
| **build_optimize.py** | Create | Build output size optimization, shared by both build scripts. Owns the helpers moved out of **versioned-build-cicd.py**, the deduplicable-extension predicate, and `deduplicate_binaries`. Single owner of the symlink logic so the two scripts cannot drift again. |
| **measure_site_size.py** | Create | Reports size composition of a built tree or of a git ref, as text or JSON. Counts real bytes, symlinks in both files and directories, and duplicates over the same extension set the optimizer uses. The single source of before and after numbers. |
| **check_rendered_text.py** | Create | Compares the rendered text of two HTML files or two whole trees, with whitespace normalized. The gate that makes minification safe to merge. |
| **test_build_tools.py** | Create | Tests for all three modules above. One file, one command. |
| **versioned-build-cicd.py** | Modify: imports, lines 177-273, Step 8 | Import from **build_optimize.py**, lose the four moved helpers, call `deduplicate_binaries` in Step 8. |
| **versioned-build.py** | Modify: imports, Step 4, before Step 9 | Stop discarding the local mike output, gain the optimization pass it never had, print a size report. |
| **mkdocs.yml** and seven guide configs | Modify | Turn the inert `- minify` into `- minify: {minify_html: true}`. `INHERIT` does not merge the `plugins` array, so each config needs its own. |
| **.specs/baseline/** | Create | Machine-readable baselines: published-tree composition, clean-`main` build warnings. Committed, so a later task can diff against them instead of rerunning work. |

---

### Task 1: Shared optimization module

A pure refactor, no behavior change. It exists first because both the harness and the optimizer need the same extension predicate, and because **versioned-build.py** must be able to import the same code the CI script runs.

The four existing helpers move by line-range extraction rather than retyping, so the moved code is provably the code running in production today.

**Files:**
- Create: `build_optimize.py`
- Create: `test_build_tools.py`
- Modify: `versioned-build-cicd.py` imports and lines 177-273

**Interfaces:**
- Consumes: nothing.
- Produces, all from **build_optimize.py**: `format_size(size_bytes) -> str`, `file_digest(path) -> str`, `is_deduplicable(filename) -> bool`, `DEDUP_BINARY_EXTENSIONS: set`, plus `deduplicate_assets(site_dir) -> (int, int)`, `list_relative_files(folder) -> set`, and `get_folder_size(path) -> int` moved unchanged. Task 2 imports `format_size` and `is_deduplicable`; Task 3 adds `deduplicate_binaries` here; Task 4 imports the two deduplicators and `format_size`.

- [ ] **Step 1: Write the failing test**

Create `test_build_tools.py`:

```python
#!/usr/bin/env python3
"""Tests for the documentation build tooling.

No test framework is installed in this repository, so this file is a plain
script: run it with python3 and it prints one line per test, then exits
non-zero if any failed.

Modules are loaded by path because versioned-build-cicd.py has a dash in its
name and cannot be imported with an import statement.
"""

import importlib.util
import os
import shutil
import sys
import tempfile

ROOT = os.path.dirname(os.path.abspath(__file__))
TESTS = []


def test(func):
    """Register a test."""
    TESTS.append(func)
    return func


def load(filename, module_name):
    spec = importlib.util.spec_from_file_location(
        module_name, os.path.join(ROOT, filename)
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def make_tree(files):
    """Create a temp tree from a mapping of relative path to bytes."""
    tree = tempfile.mkdtemp(prefix="build-tools-")
    for relative, payload in files.items():
        path = os.path.join(tree, relative)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as handle:
            handle.write(payload)
    return tree


optimize = load("build_optimize.py", "build_optimize")


@test
def test_format_size_formats_megabytes():
    assert optimize.format_size(1536 * 1024) == "1.5 MB", optimize.format_size(1536 * 1024)


@test
def test_is_deduplicable_covers_media_and_rejects_html():
    assert optimize.is_deduplicable("shot.png")
    assert optimize.is_deduplicable("clip.GIF"), "extension match must be case-insensitive"
    assert optimize.is_deduplicable("manual.pdf")
    assert not optimize.is_deduplicable("index.html")
    assert not optimize.is_deduplicable("search_index.json")


@test
def test_file_digest_matches_for_identical_content():
    tree = make_tree({"a.png": b"y" * 500, "b.png": b"y" * 500, "c.png": b"z" * 500})
    try:
        a = optimize.file_digest(os.path.join(tree, "a.png"))
        b = optimize.file_digest(os.path.join(tree, "b.png"))
        c = optimize.file_digest(os.path.join(tree, "c.png"))
        assert a == b
        assert a != c
    finally:
        shutil.rmtree(tree)


def main():
    failures = 0
    for case in TESTS:
        try:
            case()
        except Exception as error:
            # Catch every exception, not just AssertionError. A test written
            # before its implementation exists fails with AttributeError, and
            # that must be reported as one failing test rather than crashing
            # the whole run and hiding the tests that do pass.
            failures += 1
            print(f"FAIL {case.__name__}: {type(error).__name__}: {error}")
        else:
            print(f"ok   {case.__name__}")
    if failures:
        print(f"\n{failures} of {len(TESTS)} test(s) failed")
        sys.exit(1)
    print(f"\n{len(TESTS)} test(s) passed")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run the test to verify it fails**

```bash
cd /Users/symbot/DEV/vc-docs
python3 test_build_tools.py
```

Expected: an immediate `FileNotFoundError` naming **build_optimize.py**, raised from the `load` call at import time. No `ok` lines appear, because the module is loaded before any test runs.

- [ ] **Step 3: Move the four helpers into the new module**

`list_relative_files`, `deduplicate_assets`, `get_folder_size`, and `format_size` occupy one contiguous block in **versioned-build-cicd.py**, from `def list_relative_files(` to the line before `def main(`.

```bash
python3 - <<'PY'
import pathlib

lines = pathlib.Path("versioned-build-cicd.py").read_text(encoding="utf-8").splitlines(keepends=True)
start = next(i for i, l in enumerate(lines) if l.startswith("def list_relative_files("))
end = next(i for i, l in enumerate(lines) if l.startswith("def main("))
block = "".join(lines[start:end]).rstrip("\n") + "\n"

for expected in ("def list_relative_files(", "def deduplicate_assets(", "def get_folder_size(", "def format_size("):
    assert expected in block, f"{expected} missing from the extracted block"
assert "def main(" not in block, "extraction overran into main()"

header = '''#!/usr/bin/env python3
"""Build output size optimization, shared by both documentation build scripts.

versioned-build-cicd.py and versioned-build.py had drifted: the CI script
deduplicated theme assets and the local script had no optimization pass at all,
so a local build could not report the size of what CI would publish. Both
import from here now, which makes this module the single owner of the symlink
logic and of the deduplicable-extension predicate.

The module name uses underscores because versioned-build-cicd.py cannot be
imported: a dash is not valid in a module name. That is why this code needs a
file of its own rather than being shared directly between the two scripts.
"""

import hashlib
import os
import shutil

# Binary file types worth deduplicating across versions. HTML and the search
# index are deliberately absent: they differ per version by design, and
# symlinking them would hide real content.
#
# The size harness imports this set so that "remaining duplicates" describes
# exactly the files the optimizer processes. Adding an extension here changes
# both at once, which is the point.
DEDUP_BINARY_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".ico",
    ".woff", ".woff2", ".ttf", ".eot", ".otf",
    ".pdf", ".zip", ".mp4", ".webm",
}

HASH_CHUNK = 1024 * 1024


def is_deduplicable(filename):
    """Return True if this file type participates in deduplication."""
    return os.path.splitext(filename)[1].lower() in DEDUP_BINARY_EXTENSIONS


def file_digest(path):
    """Return the SHA-256 hex digest of a file, read in chunks."""
    hasher = hashlib.sha256()
    with open(path, "rb") as handle:
        while True:
            chunk = handle.read(HASH_CHUNK)
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.hexdigest()


'''

pathlib.Path("build_optimize.py").write_text(header + block, encoding="utf-8")
print(f"moved {block.count('def ')} functions into build_optimize.py")
PY
```

Expected: `moved 4 functions into build_optimize.py`.

- [ ] **Step 4: Run the test to verify it passes**

```bash
python3 test_build_tools.py
```

Expected: three `ok` lines, then `3 test(s) passed`.

- [ ] **Step 5: Point the CI script at the module**

Three of the six names are used outside the module, so three are imported.

```bash
python3 - <<'PY'
import pathlib

path = pathlib.Path("versioned-build-cicd.py")
lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
start = next(i for i, l in enumerate(lines) if l.startswith("def list_relative_files("))
end = next(i for i, l in enumerate(lines) if l.startswith("def main("))
del lines[start:end]

source = "".join(lines)
old = "import re\nimport shlex\n"
new = "import re\nimport shlex\n\nfrom build_optimize import deduplicate_assets, format_size\n"
assert old in source, "import block does not match the expected shape"
assert "from build_optimize import" not in source, "already imports the shared module"
path.write_text(source.replace(old, new, 1), encoding="utf-8")
print("versioned-build-cicd.py now imports build_optimize")
PY
```

Expected: `versioned-build-cicd.py now imports build_optimize`.

- [ ] **Step 6: Verify the refactor moved code rather than changing it**

```bash
python3 -c "import py_compile; py_compile.compile('versioned-build-cicd.py', doraise=True); py_compile.compile('build_optimize.py', doraise=True); print('both compile')"
python3 - <<'PY'
import re
import subprocess

original = subprocess.run(["git", "show", "HEAD:versioned-build-cicd.py"],
                          capture_output=True, text=True, check=True).stdout
moved = open("build_optimize.py", encoding="utf-8").read()


def body(source, name):
    """Return one function's source, from its def line to the next top-level line."""
    match = re.search(rf"^def {name}\(.*?(?=^\S|\Z)", source, re.S | re.M)
    assert match, f"{name} not found"
    return match.group(0).rstrip("\n")


for name in ("list_relative_files", "deduplicate_assets", "get_folder_size", "format_size"):
    assert body(original, name) == body(moved, name), f"{name} changed during the move"
    print(f"ok {name} moved unchanged")
PY
grep -c 'def deduplicate_assets\|def format_size' versioned-build-cicd.py
```

Expected: `both compile`, four `ok ... moved unchanged` lines, and a final count of `0` proving the definitions no longer live in the CI script.

- [ ] **Step 7: Commit**

```bash
git add build_optimize.py versioned-build-cicd.py test_build_tools.py .specs/2026-08-20-published-size-reduction-design.md .specs/2026-08-20-published-size-reduction-plan.md
git commit -m "build: extract shared size optimization into build_optimize.py

versioned-build-cicd.py owned the deduplication helpers and versioned-build.py
had no optimization pass at all, so a local build could not report the size of
what CI publishes. The helpers move unchanged, verified against git HEAD, and
gain a deduplicable-extension predicate that the size harness will share."
```

---

### Task 2: Size measurement harness and committed baselines

Every later claim in this plan is a number. This task produces them, and persists the before state so the final report can be assembled without rerunning earlier work.

The harness reads a git ref directly, which is how a baseline is taken from the real published tree rather than from a working copy that may be months stale.

**Files:**
- Create: `measure_site_size.py`
- Create: `.specs/baseline/published-tree.json`
- Create: `.specs/baseline/build-warnings.txt`
- Modify: `test_build_tools.py`

**Interfaces:**
- Consumes: `format_size` and `is_deduplicable` from **build_optimize.py**.
- Produces: `measure_tree(root) -> dict` and `measure_ref(ref) -> dict`, both returning keys `categories` (name to `{"bytes": int, "files": int}`), `total_bytes`, `symlinks`, `symlink_dirs`, `duplicate_bytes`. CLI: `python3 measure_site_size.py <dir|--ref REF> [--json]`. Tasks 3, 4, 6, and 7 call the CLI.

- [ ] **Step 1: Write the failing tests**

Append to `test_build_tools.py`, before the `def main():` line:

```python
measure = load("measure_site_size.py", "measure_site_size")


@test
def test_measure_counts_bytes_by_category():
    tree = make_tree({
        os.path.join("guide", "index.html"): b"x" * 1000,
        os.path.join("guide", "shot.png"): b"y" * 500,
    })
    try:
        report = measure.measure_tree(tree)
        assert report["categories"]["HTML"]["bytes"] == 1000, report
        assert report["categories"]["HTML"]["files"] == 1, report
        assert report["categories"]["Images"]["bytes"] == 500, report
        assert report["total_bytes"] == 1500, report
    finally:
        shutil.rmtree(tree)


@test
def test_measure_counts_file_and_directory_symlinks():
    """deduplicate_assets creates directory symlinks, which never appear in filenames."""
    tree = make_tree({os.path.join("v1", "assets", "shot.png"): b"y" * 500})
    try:
        os.makedirs(os.path.join(tree, "v2"))
        os.symlink(os.path.join("..", "v1", "assets"), os.path.join(tree, "v2", "assets"))
        os.symlink(os.path.join("..", "v1", "assets", "shot.png"), os.path.join(tree, "v2", "shot.png"))

        report = measure.measure_tree(tree)

        assert report["symlinks"] == 1, report
        assert report["symlink_dirs"] == 1, report
        # The linked directory must not be walked into, or its bytes are double counted.
        assert report["categories"]["Images"]["bytes"] == 500, report
    finally:
        shutil.rmtree(tree)


@test
def test_measure_duplicate_metric_uses_the_optimizer_predicate():
    """Two identical .js files are not deduplicable, so they are not duplicates here."""
    tree = make_tree({
        os.path.join("v1", "shot.png"): b"y" * 500,
        os.path.join("v2", "shot.png"): b"y" * 500,
        os.path.join("v1", "app.js"): b"j" * 300,
        os.path.join("v2", "app.js"): b"j" * 300,
    })
    try:
        report = measure.measure_tree(tree)
        assert report["duplicate_bytes"] == 500, report
    finally:
        shutil.rmtree(tree)


@test
def test_measure_ref_reads_a_git_ref_without_checkout():
    report = measure.measure_ref("HEAD")
    assert report["total_bytes"] > 0, report
    assert report["categories"], report
```

- [ ] **Step 2: Run the tests to verify they fail**

```bash
python3 test_build_tools.py
```

Expected: an immediate `FileNotFoundError` naming **measure_site_size.py**, raised at import time.

- [ ] **Step 3: Write the implementation**

Create `measure_site_size.py`:

```python
#!/usr/bin/env python3
"""Report the size composition of a built documentation tree or of a git ref.

Produces the before and after numbers for any change that claims to shrink the
published documentation. Only real bytes are counted: a symlink contributes its
own link size, never its target's, which is what makes a deduplication saving
show up as a smaller number rather than an unchanged one.

Duplicates are counted over exactly the extensions build_optimize.py
deduplicates, so "remaining duplicate bytes" describes the same file set the
optimizer processed.

Usage:
    python3 measure_site_size.py site
    python3 measure_site_size.py --ref origin/gh-pages
    python3 measure_site_size.py --ref origin/gh-pages --json
"""

import argparse
import hashlib
import json
import os
import subprocess

from build_optimize import format_size, is_deduplicable

# First match wins; "Other" catches the rest.
CATEGORIES = [
    ("HTML", {".html", ".htm"}),
    ("Images", {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".ico"}),
    ("Fonts", {".woff", ".woff2", ".ttf", ".eot", ".otf"}),
    ("JS", {".js", ".map"}),
    ("CSS", {".css"}),
    ("JSON", {".json"}),
]

CHUNK = 1024 * 1024


def categorize(filename):
    extension = os.path.splitext(filename)[1].lower()
    for name, extensions in CATEGORIES:
        if extension in extensions:
            return name
    return "Other"


def _digest(path):
    hasher = hashlib.sha256()
    with open(path, "rb") as handle:
        while True:
            chunk = handle.read(CHUNK)
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.hexdigest()


def _blank():
    return {
        "categories": {},
        "total_bytes": 0,
        "symlinks": 0,
        "symlink_dirs": 0,
        "duplicate_bytes": 0,
    }


def _add(report, filename, size):
    name = categorize(filename)
    entry = report["categories"].setdefault(name, {"bytes": 0, "files": 0})
    entry["bytes"] += size
    entry["files"] += 1
    report["total_bytes"] += size


def measure_tree(root):
    """Walk a real directory tree and return its size composition."""
    report = _blank()
    seen = set()

    for dirpath, dirnames, filenames in os.walk(root):
        # Directory symlinks appear here, never in filenames. os.walk does not
        # descend into them, but they still have to be counted, and pruning
        # them keeps the traversal explicit rather than incidental.
        linked_dirs = [d for d in dirnames if os.path.islink(os.path.join(dirpath, d))]
        report["symlink_dirs"] += len(linked_dirs)
        dirnames[:] = sorted(d for d in dirnames if d not in linked_dirs)

        for filename in sorted(filenames):
            path = os.path.join(dirpath, filename)
            if os.path.islink(path):
                report["symlinks"] += 1
                # A symlink is not free: it occupies its target string.
                report["total_bytes"] += os.lstat(path).st_size
                continue
            try:
                size = os.path.getsize(path)
            except OSError:
                continue

            _add(report, filename, size)

            if is_deduplicable(filename):
                key = _digest(path)
                if key in seen:
                    report["duplicate_bytes"] += size
                else:
                    seen.add(key)

    return report


def measure_ref(ref):
    """Measure a git ref without checking it out.

    Blob OIDs are content hashes, so identical content shares an OID and
    duplicates are exact rather than sampled.
    """
    output = subprocess.run(
        ["git", "ls-tree", "-r", "-l", ref],
        capture_output=True, text=True, check=True,
    ).stdout

    report = _blank()
    seen = set()

    for line in output.splitlines():
        meta, _, path = line.partition("\t")
        fields = meta.split()
        if len(fields) < 4 or fields[1] != "blob":
            continue
        oid = fields[2]
        if fields[3] == "-":
            continue
        size = int(fields[3])
        filename = os.path.basename(path)

        _add(report, filename, size)

        if is_deduplicable(filename):
            if oid in seen:
                report["duplicate_bytes"] += size
            else:
                seen.add(oid)

    return report


def render(report, label):
    lines = [f"Tree: {label}", f"{'Category':<12}{'Size':>12}{'Files':>10}"]
    ordered = sorted(report["categories"].items(), key=lambda item: item[1]["bytes"], reverse=True)
    for name, entry in ordered:
        lines.append(f"{name:<12}{format_size(entry['bytes']):>12}{entry['files']:>10}")
    lines.append(f"{'TOTAL':<12}{format_size(report['total_bytes']):>12}")
    lines.append(f"Symlinks: {report['symlinks']} file(s), {report['symlink_dirs']} directory(ies)")
    lines.append(f"Duplicate bytes in deduplicable types: {format_size(report['duplicate_bytes'])}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Report site size composition")
    parser.add_argument("directory", nargs="?", help="Built site directory to measure")
    parser.add_argument("--ref", help="Measure a git ref instead of a directory")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of a table")
    args = parser.parse_args()

    if bool(args.directory) == bool(args.ref):
        parser.error("pass exactly one of a directory or --ref")

    if args.ref:
        report, label = measure_ref(args.ref), args.ref
    else:
        report, label = measure_tree(args.directory), args.directory

    if args.json:
        print(json.dumps({"label": label, **report}, indent=2, sort_keys=True))
    else:
        print(render(report, label))


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run the tests to verify they pass**

```bash
python3 test_build_tools.py
```

Expected: seven `ok` lines, then `7 test(s) passed`.

- [ ] **Step 5: Cross-check the harness against an independent measurement**

```bash
python3 measure_site_size.py --ref origin/gh-pages
git ls-tree -r -l origin/gh-pages | awk '$4 != "-" {s += $4} END {printf "independent total: %.0f MB\n", s/1048576}'
```

Expected: the harness `TOTAL` and the `awk` total agree to the megabyte. They read the same data by different code paths; a mismatch means the harness is wrong, not the tree.

- [ ] **Step 6: Commit the published-tree baseline**

```bash
mkdir -p .specs/baseline
python3 measure_site_size.py --ref origin/gh-pages --json > .specs/baseline/published-tree.json
python3 - <<'PY'
import json

data = json.load(open(".specs/baseline/published-tree.json"))
mb = lambda b: b / 1048576
print(f"total {mb(data['total_bytes']):.0f} MB")
for name in ("HTML", "Images"):
    print(f"{name}: {mb(data['categories'][name]['bytes']):.0f} MB")
print(f"duplicates: {mb(data['duplicate_bytes']):.0f} MB")
assert data["total_bytes"] > 4_000_000_000, "published tree smaller than expected; is the ref stale?"
PY
```

Expected: a total near 5086 MB, HTML near 3039 MB, Images near 1690 MB, duplicates near 1577 MB. Exact figures will drift with each deploy; the assertion only guards against measuring a stale or empty ref.

- [ ] **Step 7: Commit the clean-main build warning baseline**

Task 6 must prove minification introduces no new warnings, which requires knowing what `main` produces now. Capture it before anything changes.

```bash
git stash list | head -1
rm -rf site
./build.sh 2>&1 | grep -E 'WARNING|ERROR' | sed -E 's/[0-9]{4}-[0-9]{2}-[0-9]{2}[T ][0-9:.]+Z?//g' | sort | uniq -c | sort -rn > .specs/baseline/build-warnings.txt
wc -l .specs/baseline/build-warnings.txt
head -10 .specs/baseline/build-warnings.txt
rm -rf site
```

Expected: a file listing normalized warning lines with counts. An empty file is a valid baseline and means `main` builds clean; record it either way.

- [ ] **Step 8: Commit**

```bash
git add measure_site_size.py test_build_tools.py .specs/baseline/
git commit -m "build: add size measurement harness and committed baselines

The harness reads a directory or a git ref, so a baseline comes from the real
published tree rather than a working copy that may be months stale. It counts
directory symlinks as well as file symlinks, charges a symlink its own size,
and counts duplicates over exactly the extension set build_optimize.py
deduplicates.

Baselines for the published tree and for clean-main build warnings are
committed so later tasks diff against them instead of rerunning the work."
```

---

### Task 3: Deduplicate identical binaries across versions

The headline change. Media is 1690 MB of the published tree, of which 1334 MB is byte-identical across versions, and because media compresses only 1.1x while HTML compresses 15.5x, those duplicates are roughly 1213 MB of every 2 GB registry tag. Removing them needs no redeploy and touches no release branch.

**Files:**
- Modify: `build_optimize.py`
- Modify: `versioned-build-cicd.py` Step 8
- Modify: `test_build_tools.py`

**Interfaces:**
- Consumes: `file_digest`, `is_deduplicable`, `format_size` from **build_optimize.py**.
- Produces: `deduplicate_binaries(site_dir) -> (replaced_count: int, freed_bytes: int)`, matching the shape `deduplicate_assets` returns so Step 8 can sum them. Task 4 imports it.

- [ ] **Step 1: Write the failing tests**

Append to `test_build_tools.py`, before `def main():`:

```python
@test
def test_dedup_replaces_identical_image_with_working_symlink():
    tree = make_tree({
        os.path.join("stable14", "media", "shot.png"): b"y" * 500,
        os.path.join("stable15", "media", "shot.png"): b"y" * 500,
    })
    try:
        replaced, freed = optimize.deduplicate_binaries(tree)

        assert replaced == 1, replaced
        assert freed == 500, freed
        duplicate = os.path.join(tree, "stable15", "media", "shot.png")
        assert os.path.islink(duplicate)
        assert not os.path.isabs(os.readlink(duplicate)), "symlink target must be relative"
        with open(duplicate, "rb") as handle:
            assert handle.read() == b"y" * 500, "symlink does not resolve to the content"
        assert not os.path.islink(os.path.join(tree, "stable14", "media", "shot.png"))
    finally:
        shutil.rmtree(tree)


@test
def test_dedup_keeps_different_content_and_ignores_html():
    tree = make_tree({
        os.path.join("stable14", "media", "shot.png"): b"y" * 500,
        os.path.join("stable15", "media", "shot.png"): b"z" * 500,
        os.path.join("stable14", "index.html"): b"<p>same</p>",
        os.path.join("stable15", "index.html"): b"<p>same</p>",
    })
    try:
        replaced, freed = optimize.deduplicate_binaries(tree)

        assert replaced == 0, replaced
        assert freed == 0, freed
        assert not os.path.islink(os.path.join(tree, "stable15", "index.html")), "HTML must not be touched"
    finally:
        shutil.rmtree(tree)


@test
def test_dedup_canonical_copy_is_lexicographically_first():
    """Determinism: identical input must always keep the same file."""
    files = {
        os.path.join("b-version", "media", "shot.png"): b"y" * 500,
        os.path.join("a-version", "media", "shot.png"): b"y" * 500,
    }
    for _ in range(2):
        tree = make_tree(files)
        try:
            optimize.deduplicate_binaries(tree)
            assert not os.path.islink(os.path.join(tree, "a-version", "media", "shot.png"))
            assert os.path.islink(os.path.join(tree, "b-version", "media", "shot.png"))
        finally:
            shutil.rmtree(tree)


@test
def test_dedup_is_idempotent():
    tree = make_tree({
        os.path.join("v1", "media", "shot.png"): b"y" * 500,
        os.path.join("v2", "media", "shot.png"): b"y" * 500,
    })
    try:
        optimize.deduplicate_binaries(tree)
        replaced, freed = optimize.deduplicate_binaries(tree)

        assert replaced == 0, replaced
        assert freed == 0, freed
    finally:
        shutil.rmtree(tree)


@test
def test_dedup_does_not_follow_directory_symlinks():
    """deduplicate_assets runs first and leaves directory symlinks behind."""
    tree = make_tree({os.path.join("root", "assets", "logo.svg"): b"<svg/>" * 50})
    try:
        os.makedirs(os.path.join(tree, "v1"))
        os.symlink(os.path.join("..", "root", "assets"), os.path.join(tree, "v1", "assets"))

        replaced, freed = optimize.deduplicate_binaries(tree)

        assert replaced == 0, "a linked directory must not be traversed"
        assert freed == 0, freed
        assert os.path.islink(os.path.join(tree, "v1", "assets"))
    finally:
        shutil.rmtree(tree)
```

- [ ] **Step 2: Run the tests to verify they fail**

```bash
python3 test_build_tools.py
```

Expected: seven `ok` lines followed by five `FAIL` lines reporting `AttributeError: module 'build_optimize' has no attribute 'deduplicate_binaries'`, then `5 of 12 test(s) failed`. Unlike the earlier tasks the module exists, so the suite runs and reports per-test failures.

- [ ] **Step 3: Write the implementation**

Append to `build_optimize.py`:

```python
def deduplicate_binaries(site_dir):
    """
    Replace byte-identical binary files with relative symlinks to one copy.

    Every published version carries its own copy of the screenshots it
    references. Across the five published versions that is roughly 1690MB of
    media holding roughly 355MB of unique content, because most screenshots do
    not change between releases.

    Media matters out of proportion to its share of the tree. Registry layers
    are gzip-compressed, and media compresses about 1.1x while HTML compresses
    about 15.5x, so these duplicates are roughly 1213MB of every 2GB image tag
    even though HTML is the larger part of the tree.

    Only files whose content hashes are equal are linked, so a version whose
    screenshot did change keeps its own file. No HTML is rewritten: each page
    keeps referencing its own path, and the path still resolves. That is what
    makes this safe for historical fidelity, unlike a shared unversioned media
    folder, where an old version would start showing a new screenshot.

    The canonical copy is the first path yielded by a sorted walk. The choice must be deterministic: an identical input tree has to
    produce an identical output tree, or the resulting image layer differs
    between builds for no reason.

    IMPORTANT: call this after deduplicate_assets. os.walk does not descend
    into symlinked directories, so running second means the nested assets/
    trees that pass already replaced are skipped instead of being rehashed
    once per version.
    """
    canonical = {}
    replaced_count = 0
    freed_bytes = 0

    for dirpath, dirnames, filenames in os.walk(site_dir):
        # Sorted traversal is what makes the canonical choice reproducible.
        # Linked directories are dropped explicitly: os.walk would not descend
        # into them anyway, and being explicit keeps that guarantee visible.
        dirnames[:] = sorted(
            d for d in dirnames if not os.path.islink(os.path.join(dirpath, d))
        )

        for filename in sorted(filenames):
            if not is_deduplicable(filename):
                continue

            path = os.path.join(dirpath, filename)
            if os.path.islink(path):
                continue

            try:
                digest = file_digest(path)
                size = os.path.getsize(path)
            except OSError as error:
                print(f"    ⚠️  Skipped {os.path.relpath(path, site_dir)}: {error}")
                continue

            keep = canonical.get(digest)
            if keep is None:
                canonical[digest] = path
                continue

            target = os.path.relpath(keep, dirpath)
            os.remove(path)
            os.symlink(target, path)
            replaced_count += 1
            freed_bytes += size

    return replaced_count, freed_bytes
```

- [ ] **Step 4: Run the tests to verify they pass**

```bash
python3 test_build_tools.py
```

Expected: twelve `ok` lines, then `12 test(s) passed`.

- [ ] **Step 5: Wire the call into Step 8 of the CI build**

```bash
python3 - <<'PY'
import pathlib

path = pathlib.Path("versioned-build-cicd.py")
source = path.read_text(encoding="utf-8")

source = source.replace(
    "from build_optimize import deduplicate_assets, format_size\n",
    "from build_optimize import deduplicate_assets, deduplicate_binaries, format_size\n",
    1,
)

old = "    total_freed = assets_freed\n"
new = '''    # Runs after the assets pass on purpose: os.walk does not descend into the
    # symlinked assets/ folders it just created, so those are skipped here.
    print("  Deduplicating identical binaries across versions...")
    binaries_replaced, binaries_freed = deduplicate_binaries(args.output_dir)
    print(f"  ✅ Replaced {binaries_replaced} duplicate binaries with symlinks ({format_size(binaries_freed)} freed)")

    total_freed = assets_freed + binaries_freed
'''
assert source.count(old) == 1, "expected exactly one total_freed assignment"
assert "deduplicate_binaries," in source, "import was not extended"
path.write_text(source.replace(old, new, 1), encoding="utf-8")
print("Step 8 wired")
PY
python3 -c "import py_compile; py_compile.compile('versioned-build-cicd.py', doraise=True); print('compiles')"
grep -n 'deduplicate_assets(args.output_dir)\|deduplicate_binaries(args.output_dir)\|total_freed =' versioned-build-cicd.py
```

Expected: `Step 8 wired`, `compiles`, and the assets call on a lower line number than the binaries call.

- [ ] **Step 6: Prove the saving on real published content**

Run against a copy of two real snapshots. Never against `gh-pages` itself.

```bash
rm -rf /tmp/dedup-trial && mkdir -p /tmp/dedup-trial
git archive origin/gh-pages platform/developer-guide/stable14 platform/developer-guide/stable15 | tar -x -C /tmp/dedup-trial
python3 measure_site_size.py /tmp/dedup-trial --json > /tmp/dedup-before.json
python3 - <<'PY'
import build_optimize

replaced, freed = build_optimize.deduplicate_binaries("/tmp/dedup-trial")
print(f"replaced {replaced} files, freed {build_optimize.format_size(freed)}")
PY
python3 measure_site_size.py /tmp/dedup-trial --json > /tmp/dedup-after.json
python3 - <<'PY'
import json

before = json.load(open("/tmp/dedup-before.json"))
after = json.load(open("/tmp/dedup-after.json"))
mb = lambda b: b / 1048576
print(f"total {mb(before['total_bytes']):.0f} MB -> {mb(after['total_bytes']):.0f} MB")
print(f"symlinks {before['symlinks']} -> {after['symlinks']}")
print(f"remaining duplicates {mb(before['duplicate_bytes']):.0f} MB -> {mb(after['duplicate_bytes']):.0f} MB")
assert after["total_bytes"] < before["total_bytes"], "no bytes were freed"
assert after["duplicate_bytes"] == 0, "duplicates remain in deduplicable types"
assert after["symlinks"] > before["symlinks"], "no symlinks were created"
PY
```

Expected: a smaller total, remaining duplicates exactly zero, and a non-zero symlink count. Remaining duplicates must be zero rather than merely small: the harness and the optimizer share one extension predicate, so anything left over is a defect in one of them.

- [ ] **Step 7: Verify no symlink escapes the tree, files and directories alike**

```bash
python3 - <<'PY'
import os

root = os.path.realpath("/tmp/dedup-trial")
bad = []
files = dirs = 0
for dirpath, dirnames, filenames in os.walk(root):
    for name in list(dirnames) + filenames:
        path = os.path.join(dirpath, name)
        if not os.path.islink(path):
            continue
        if os.path.isdir(path):
            dirs += 1
        else:
            files += 1
        resolved = os.path.realpath(path)
        if not resolved.startswith(root + os.sep):
            bad.append((path, os.readlink(path), "escapes the tree"))
        elif not os.path.exists(resolved):
            bad.append((path, os.readlink(path), "broken target"))
assert not bad, bad
print(f"{files} file symlink(s) and {dirs} directory symlink(s), all resolve inside the tree")
PY
```

Expected: a non-zero file count and `all resolve inside the tree`.

- [ ] **Step 8: Commit**

```bash
rm -rf /tmp/dedup-trial /tmp/dedup-before.json /tmp/dedup-after.json
git add build_optimize.py versioned-build-cicd.py test_build_tools.py
git commit -m "build: deduplicate identical binaries across published versions

Each published version carried its own copy of every screenshot it references.
Media is 1690MB of the published tree holding 355MB of unique content.

Media matters out of proportion to its share of the tree because registry
layers are gzip-compressed: media compresses 1.1x while HTML compresses 15.5x,
so these duplicates are roughly 1213MB of every 2GB image tag.

Identical files become relative symlinks to one canonical copy, so no HTML is
rewritten and every version keeps referencing its own path. The canonical copy
is the first path yielded by a sorted walk, which keeps the output
reproducible for identical input. Runs after deduplicate_assets, whose
directory symlinks are skipped rather than traversed."
```

---

### Task 4: Local build script reports what a deploy would publish

**versioned-build.py** has nine steps and none of them optimizes anything, so the tree it produces is larger than the tree CI publishes. It also discards the version it just built: Step 4 runs `git reset --hard origin/gh-pages` inside the **gh-pages** folder, while the local `mike deploy` wrote to the root repository's own `gh-pages` ref. The report would therefore describe what is on the remote, not what was just built.

**Files:**
- Modify: `versioned-build.py` imports, Step 4, and the block before Step 9

**Interfaces:**
- Consumes: `deduplicate_assets`, `deduplicate_binaries`, `format_size` from **build_optimize.py**; the `measure_site_size.py` CLI; the script's own `run_command(cmd, check=True)`.
- Produces: nothing other tasks call.

- [ ] **Step 1: Confirm the premise**

```bash
cd /Users/symbot/DEV/vc-docs
grep -c 'deduplicate' versioned-build.py
grep -n 'Step 9\|reset --hard' versioned-build.py
```

Expected: a count of `0`; `Step 9: Start Python HTTP server` as the only Step 9; and a `git reset --hard origin/gh-pages` line inside Step 4. Any difference means the script changed upstream; reread it before editing.

- [ ] **Step 2: Add the imports**

```bash
python3 - <<'PY'
import pathlib

path = pathlib.Path("versioned-build.py")
source = path.read_text(encoding="utf-8")
old = "import socketserver\nimport json\n"
new = ("import socketserver\nimport json\n\n"
       "from build_optimize import deduplicate_assets, deduplicate_binaries, format_size\n")
assert old in source, "import block does not match the expected shape"
assert "from build_optimize import" not in source, "already imports the shared module"
path.write_text(source.replace(old, new, 1), encoding="utf-8")
print("imports added")
PY
```

Expected: `imports added`.

- [ ] **Step 3: Stop discarding the locally built version**

The local `mike deploy` updates the root repository's `gh-pages` ref. Fetching from `origin` and hard-resetting to it throws that away. Pull from the local ref instead, and fall back to `origin` only when the local ref does not exist, so a first run still works.

```bash
python3 - <<'PY'
import pathlib

path = pathlib.Path("versioned-build.py")
source = path.read_text(encoding="utf-8")

old = '''        run_command("cd gh-pages && git fetch origin gh-pages", check=False)
        run_command("cd gh-pages && git reset --hard origin/gh-pages", check=False)
'''
new = '''        # mike deploy above wrote to THIS repository's gh-pages ref, not to the
        # remote. Fetching from origin and resetting to it would discard the
        # version that was just built and report the remote instead. Pull the
        # local ref first, and fall back to origin only if it does not exist.
        local_ref = run_command("git rev-parse --verify --quiet gh-pages", check=False)
        if local_ref.stdout.strip():
            result = run_command("cd gh-pages && git fetch .. gh-pages", check=False)
            if result.returncode != 0:
                print(f"  ❌ Could not fetch the local gh-pages ref: {result.stderr}")
                sys.exit(1)
        else:
            print("  ⚠️  No local gh-pages ref yet, falling back to origin")
            result = run_command("cd gh-pages && git fetch origin gh-pages", check=False)
            if result.returncode != 0:
                print(f"  ❌ Could not fetch origin/gh-pages: {result.stderr}")
                sys.exit(1)
        result = run_command("cd gh-pages && git reset --hard FETCH_HEAD", check=False)
        if result.returncode != 0:
            print(f"  ❌ Could not reset the gh-pages folder: {result.stderr}")
            sys.exit(1)
'''
assert source.count(old) == 1, "Step 4 refresh block does not match the expected shape"
path.write_text(source.replace(old, new, 1), encoding="utf-8")
print("Step 4 now reports the locally built version")
PY
```

Expected: `Step 4 now reports the locally built version`.

- [ ] **Step 4: Insert the optimization and reporting steps**

The two passes run in the same order as CI. The report shells out to the harness rather than reimplementing its output, so the two can never disagree. `run_command` captures output, hence the explicit print.

```bash
python3 - <<'PY'
import pathlib

path = pathlib.Path("versioned-build.py")
source = path.read_text(encoding="utf-8")

old = '    print("📋 Step 9: Start Python HTTP server")\n'
new = '''    print("📋 Step 9: Optimize build size (remove duplicates)")

    # The same two passes CI runs, in the same order, so the size reported below
    # is the size of what a deploy would publish. The assets pass must run first:
    # os.walk does not descend into the symlinked assets/ folders it creates.
    print("  Deduplicating assets folders...")
    assets_replaced, assets_freed = deduplicate_assets("site")
    print(f"  ✅ Replaced {assets_replaced} assets folders with symlinks ({format_size(assets_freed)} freed)")

    print("  Deduplicating identical binaries across versions...")
    binaries_replaced, binaries_freed = deduplicate_binaries("site")
    print(f"  ✅ Replaced {binaries_replaced} duplicate binaries with symlinks ({format_size(binaries_freed)} freed)")

    print(f"✅ Build optimized! Total space saved: {format_size(assets_freed + binaries_freed)}")

    print("📋 Step 10: Report build size")

    # Shelling out to the harness keeps one implementation of the report.
    print(run_command("python3 measure_site_size.py site").stdout)

    print("📋 Step 11: Start Python HTTP server")
'''

assert source.count(old) == 1, "expected exactly one Step 9 server banner"
path.write_text(source.replace(old, new, 1), encoding="utf-8")
print("optimization and reporting steps inserted")
PY
python3 -c "import py_compile; py_compile.compile('versioned-build.py', doraise=True); print('compiles')"
grep -n '📋 Step' versioned-build.py
```

Expected: `optimization and reporting steps inserted`, `compiles`, then eleven step banners numbered 1 through 11 with no gaps, ending at `Step 11: Start Python HTTP server`.

- [ ] **Step 5: Verify the new code path on a real tree**

The full script performs mike deploys and takes minutes. Check the inserted code path first, on a throwaway copy.

```bash
rm -rf /tmp/local-trial && mkdir -p /tmp/local-trial
git archive origin/gh-pages platform/developer-guide | tar -x -C /tmp/local-trial
python3 - <<'PY'
from build_optimize import deduplicate_assets, deduplicate_binaries, format_size

assets_replaced, assets_freed = deduplicate_assets("/tmp/local-trial")
binaries_replaced, binaries_freed = deduplicate_binaries("/tmp/local-trial")
print(f"assets: {assets_replaced} folders, {format_size(assets_freed)}")
print(f"binaries: {binaries_replaced} files, {format_size(binaries_freed)}")
PY
python3 measure_site_size.py /tmp/local-trial
rm -rf /tmp/local-trial
```

Expected: a non-zero binaries count and `Duplicate bytes in deduplicable types: 0.0 B`. The assets count may be zero because this partial tree has no root `assets/` to link to; that is expected here and is covered by Step 6.

- [ ] **Step 6: Run the local build end to end**

This is the deliverable: one command that reports the size of what would be published.

Before running, note that Step 4 hard-resets the **gh-pages** folder. That is pre-existing behavior this task narrows but does not remove.

```bash
rm -rf site
python3 versioned-build.py
```

Expected: Steps 1 through 8 as before, a Step 9 reporting freed space for both passes, a Step 10 size table, then the server on `http://localhost:8020`. Open `/platform/developer-guide/` and confirm the page is styled, which proves the symlinked `assets/` resolve through a server. Open a page with a screenshot and confirm the image loads, which proves the media symlinks resolve. Stop with Ctrl+C.

- [ ] **Step 7: Commit**

```bash
rm -rf site
git add versioned-build.py
git commit -m "build: optimize and report size in the local build script

versioned-build.py had no optimization pass, so the tree it produced was larger
than the tree CI publishes. It also discarded the version it had just built:
mike deploy writes to this repository's gh-pages ref, while Step 4 fetched from
origin and hard-reset to it, so any report described the remote instead.

Step 4 now pulls the local ref and fails loudly instead of continuing with
stale content. The build then runs the same two passes as CI, from
build_optimize.py, and prints the breakdown from measure_site_size.py."
```

---

### Task 5: Rendered-text equivalence gate

Minification is safe only if the visible text survives it on every page, not on a sampled few. The risk is not lost markup: it is whitespace collapse joining two words across an inline tag boundary, which this repository is unusually exposed to because the style guide puts bold UI labels inside sentences.

A browser inserts no whitespace for `</strong>`, so the checker must not either. Getting that distinction wrong in either direction makes the checker useless: treating all tags as separators hides the very defect being hunted, and treating none as separators reports a failure every time a newline between two paragraphs disappears.

**Files:**
- Create: `check_rendered_text.py`
- Modify: `test_build_tools.py`

**Interfaces:**
- Consumes: nothing from other tasks.
- Produces: `rendered_text(path) -> str` and the CLI `python3 check_rendered_text.py <before> <after>`, accepting two files or two directories, exiting 0 on equality and 1 on any difference. Task 6 uses the directory form as a merge gate.

- [ ] **Step 1: Write the failing tests**

Append to `test_build_tools.py`, before `def main():`:

```python
checker = load("check_rendered_text.py", "check_rendered_text")


def _text(html):
    tree = make_tree({"page.html": html.encode("utf-8")})
    try:
        return checker.rendered_text(os.path.join(tree, "page.html"))
    finally:
        shutil.rmtree(tree)


@test
def test_rendered_text_ignores_whitespace_between_block_tags():
    assert _text("<p>First.</p>\n\n    <p>Second.</p>") == _text("<p>First.</p><p>Second.</p>")


@test
def test_rendered_text_detects_words_joined_across_inline_tag():
    before = _text("<p>Click <strong>Save</strong> in the toolbar.</p>")
    after = _text("<p>Click <strong>Save</strong>in the toolbar.</p>")
    assert before != after, "joined words across </strong> must be detected"


@test
def test_rendered_text_detects_joining_across_less_common_inline_tags():
    """The inline set must be the real phrasing-content set, not a partial one."""
    for tag in ("label", "button", "output", "abbr", "code", "select"):
        before = _text(f"<p><{tag}>Name</{tag}> required</p>")
        after = _text(f"<p><{tag}>Name</{tag}>required</p>")
        assert before != after, f"joining across </{tag}> was not detected"


@test
def test_rendered_text_survives_a_gt_inside_an_attribute():
    """A naive [^>]* tag regex truncates here and leaks attribute text."""
    text = _text('<p><abbr title="a > b">EAV</abbr> store</p>')
    assert text == "EAV store", text


@test
def test_rendered_text_drops_script_and_style_content():
    text = _text("<style>p{color:red}</style><p>Hello</p><script>var x=1;</script>")
    assert text == "Hello", text
```

- [ ] **Step 2: Run the tests to verify they fail**

```bash
python3 test_build_tools.py
```

Expected: an immediate `FileNotFoundError` naming **check_rendered_text.py**.

- [ ] **Step 3: Write the implementation**

Create `check_rendered_text.py`:

```python
#!/usr/bin/env python3
"""Compare the rendered text of two HTML files, or two whole trees.

The gate for HTML minification. Minification may change every byte of markup;
it may not change one character of what a reader sees.

Inline tags are removed with no replacement, because a browser inserts no
whitespace for </strong> or </a>. Every other tag becomes a space, because a
browser does separate block boundaries. Both halves of that rule matter:
replacing all tags with a space hides words joined across an inline boundary,
which is the defect being hunted, and removing all tags reports a failure every
time a newline between two paragraphs disappears.

Parsing uses html.parser from the standard library rather than a tag regex.
A regex of the form <[^>]*> truncates on a > inside a quoted attribute and
leaks the remainder of the attribute into the text it claims to have stripped.

Usage:
    python3 check_rendered_text.py before.html after.html
    python3 check_rendered_text.py before_tree/ after_tree/
"""

import argparse
import os
import re
import sys
from html.parser import HTMLParser

# Phrasing content per the HTML specification, minus <br>, which represents a
# line break and therefore does separate words. Anything not listed here is
# treated as a block boundary.
INLINE_TAGS = frozenset({
    "a", "abbr", "b", "bdi", "bdo", "button", "cite", "code", "data", "dfn",
    "em", "i", "img", "input", "kbd", "label", "mark", "meter", "output",
    "picture", "progress", "q", "rp", "rt", "ruby", "s", "samp", "select",
    "slot", "small", "span", "strong", "sub", "sup", "svg", "textarea",
    "time", "u", "var", "wbr",
})

SKIP_CONTENT = frozenset({"script", "style", "template"})
WHITESPACE = re.compile(r"\s+")


class TextExtractor(HTMLParser):
    """Collect visible text, modelling inline and block tags differently."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self._skip_depth = 0

    def _boundary(self, tag):
        if tag not in INLINE_TAGS:
            self.parts.append(" ")

    def handle_starttag(self, tag, attrs):
        if tag in SKIP_CONTENT:
            self._skip_depth += 1
        self._boundary(tag)

    def handle_startendtag(self, tag, attrs):
        self._boundary(tag)

    def handle_endtag(self, tag):
        if tag in SKIP_CONTENT and self._skip_depth:
            self._skip_depth -= 1
        self._boundary(tag)

    def handle_data(self, data):
        if not self._skip_depth:
            self.parts.append(data)

    def text(self):
        return WHITESPACE.sub(" ", "".join(self.parts)).strip()


def rendered_text(path):
    """Return the visible text of an HTML file, with whitespace normalized."""
    with open(path, encoding="utf-8", errors="replace") as handle:
        parser = TextExtractor()
        parser.feed(handle.read())
        parser.close()
        return parser.text()


def _first_difference(before, after):
    for index in range(min(len(before), len(after))):
        if before[index] != after[index]:
            start = max(0, index - 60)
            return (f"  first difference at char {index}\n"
                    f"  before: ...{before[start:index + 60]}...\n"
                    f"  after:  ...{after[start:index + 60]}...")
    return f"  one side is a prefix of the other, diverging at char {min(len(before), len(after))}"


def _html_paths(root):
    found = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if not os.path.islink(os.path.join(dirpath, d)))
        for filename in sorted(filenames):
            if filename.endswith((".html", ".htm")):
                path = os.path.join(dirpath, filename)
                found[os.path.relpath(path, root)] = path
    return found


def compare_trees(before_root, after_root):
    """Compare every HTML page in two trees. Returns a list of problems."""
    before = _html_paths(before_root)
    after = _html_paths(after_root)
    problems = []

    for relative in sorted(set(before) - set(after)):
        problems.append(f"missing in after: {relative}")
    for relative in sorted(set(after) - set(before)):
        problems.append(f"unexpected in after: {relative}")

    for relative in sorted(set(before) & set(after)):
        b = rendered_text(before[relative])
        a = rendered_text(after[relative])
        if b != a:
            problems.append(f"text changed: {relative}\n{_first_difference(b, a)}")

    return problems, len(set(before) & set(after))


def main():
    parser = argparse.ArgumentParser(description="Compare rendered text of HTML files or trees")
    parser.add_argument("before")
    parser.add_argument("after")
    args = parser.parse_args()

    if os.path.isdir(args.before) != os.path.isdir(args.after):
        parser.error("pass either two files or two directories, not one of each")

    if os.path.isdir(args.before):
        problems, compared = compare_trees(args.before, args.after)
        if problems:
            print(f"DIFFERENT: {len(problems)} problem(s) across {compared} compared page(s)")
            for problem in problems[:20]:
                print(f"- {problem}")
            if len(problems) > 20:
                print(f"... and {len(problems) - 20} more")
            sys.exit(1)
        print(f"OK: rendered text identical across {compared} page(s)")
        return

    before = rendered_text(args.before)
    after = rendered_text(args.after)
    if before == after:
        print(f"OK: rendered text identical ({len(before)} chars)")
        return
    print("DIFFERENT: rendered text changed")
    print(f"  before: {len(before)} chars")
    print(f"  after:  {len(after)} chars")
    print(_first_difference(before, after))
    sys.exit(1)


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run the tests to verify they pass**

```bash
python3 test_build_tools.py
```

Expected: seventeen `ok` lines, then `17 test(s) passed`.

- [ ] **Step 5: Commit**

```bash
git add check_rendered_text.py test_build_tools.py
git commit -m "build: add rendered-text equivalence gate for HTML minification

Compares two files or two whole trees, so minification is gated on every page
rather than a sample. Parses with html.parser instead of a tag regex, which
truncates on a > inside a quoted attribute. Inline tags are removed with no
replacement and every other tag becomes a space, matching how a browser
separates words, so words joined across </strong> are detected while collapsed
whitespace between paragraphs is not reported."
```

---

### Task 6: Enable HTML minification

The `minify` plugin is declared in eight configs and does nothing in all eight, because its default is `minify_html: false`. Enabling it cuts 57% of HTML bytes in the version being deployed.

This reaches `latest` only. mike deploys one version per run, so the four frozen versions keep their un-minified HTML until they are redeployed, which is the follow-up plan named at the end of this document. In the registry the immediate effect is small, about 27 MB of a 2 GB tag, because HTML compresses 15.5x. In the working tree it is 424 MB of 5086 MB, which is what CI checks out on every run.

**Files:**
- Modify: `mkdocs.yml:90-91`
- Modify: the seven guide `mkdocs.yml` files

**Interfaces:**
- Consumes: `check_rendered_text.py` and `measure_site_size.py` from Tasks 5 and 2.
- Produces: nothing other tasks call. Task 7 re-measures the whole build.

- [ ] **Step 1: Pick a sample page that exists, and capture the before tree**

Two pages are checked in detail and the whole tree is checked for text equality, so the sample only needs to contain a code block. Resolve it once into a variable rather than hard-coding a path in each command.

```bash
cd /Users/symbot/DEV/vc-docs
rm -rf site /tmp/minify-before
mkdocs build -f platform/developer-guide/mkdocs.yml -d ../../site/platform/developer-guide
GUIDE=site/platform/developer-guide
SAMPLE=$(grep -rl '<pre' "$GUIDE" --include='index.html' | grep -v "^$GUIDE/index.html$" | head -1)
echo "SAMPLE=$SAMPLE"
test -n "$SAMPLE" || { echo "no page with a code block found"; exit 1; }
echo "$SAMPLE" > /tmp/minify-sample-path
cp -R "$GUIDE" /tmp/minify-before
python3 measure_site_size.py "$GUIDE" --json > /tmp/minify-before.json
```

Expected: `SAMPLE=` naming a real page, and a saved before tree. The sample is discovered, not assumed, so a page rename cannot break this task.

- [ ] **Step 2: Confirm the plugin is currently inert**

```bash
grep -n 'minify' mkdocs.yml platform/developer-guide/mkdocs.yml
grep -c '<!-- Main navigation item' site/platform/developer-guide/index.html
```

Expected: `- minify` with no options in both configs, a commented `minify_html: true` under the root one, and a non-zero count of Jinja comments in the built page. A count of zero means minification is already active and this task is done.

- [ ] **Step 3: Enable minification in the root config**

The sub-key is indented by ten spaces to match the neighboring `redirects` entry.

```bash
python3 - <<'PY'
import pathlib

path = pathlib.Path("mkdocs.yml")
source = path.read_text(encoding="utf-8")
old = "    - minify\n    #       minify_html: true\n"
new = "    - minify:\n          minify_html: true\n"
assert old in source, "root mkdocs.yml does not contain the expected inert minify block"
path.write_text(source.replace(old, new, 1), encoding="utf-8")
print("root config updated")
PY
```

Expected: `root config updated`.

- [ ] **Step 4: Enable minification in the seven guide configs**

The sub-key is indented by eight spaces to match the neighboring `search` entry in those files.

```bash
python3 - <<'PY'
import pathlib

guides = [
    "platform/user-guide/mkdocs.yml",
    "platform/developer-guide/mkdocs.yml",
    "platform/deployment-on-cloud/mkdocs.yml",
    "storefront/user-guide/mkdocs.yml",
    "storefront/developer-guide/mkdocs.yml",
    "marketplace/user-guide/mkdocs.yml",
    "marketplace/developer-guide/mkdocs.yml",
]
old = "    - minify\n"
new = "    - minify:\n        minify_html: true\n"
for guide in guides:
    path = pathlib.Path(guide)
    source = path.read_text(encoding="utf-8")
    assert source.count(old) == 1, f"{guide}: expected exactly one bare minify line"
    path.write_text(source.replace(old, new, 1), encoding="utf-8")
    print(f"updated {guide}")
PY
```

Expected: seven `updated` lines.

- [ ] **Step 5: Verify every config still parses and carries the option**

A YAML indentation mistake here fails the whole deploy, so check before building.

```bash
python3 - <<'PY'
import re
import yaml

configs = [
    "mkdocs.yml",
    "platform/user-guide/mkdocs.yml",
    "platform/developer-guide/mkdocs.yml",
    "platform/deployment-on-cloud/mkdocs.yml",
    "storefront/user-guide/mkdocs.yml",
    "storefront/developer-guide/mkdocs.yml",
    "marketplace/user-guide/mkdocs.yml",
    "marketplace/developer-guide/mkdocs.yml",
]

# The emoji extension config uses !!python/name: tags, which safe_load rejects.
# Blank them out textually rather than registering a permissive loader: this
# check only needs the plugins array, and safe_load must stay safe_load.
PYTHON_TAG = re.compile(r"!!python/name:\S+")

for config in configs:
    with open(config, encoding="utf-8") as handle:
        data = yaml.safe_load(PYTHON_TAG.sub("null", handle.read()))
    entries = [p for p in (data.get("plugins") or []) if isinstance(p, dict) and "minify" in p]
    assert entries, f"{config}: no minify mapping found"
    assert entries[0]["minify"]["minify_html"] is True, f"{config}: minify_html not True"
    print(f"ok {config}")
PY
```

Expected: eight `ok` lines. A `KeyError` or `TypeError` means the indentation is wrong; fix it before continuing.

- [ ] **Step 6: Rebuild the sample guide**

```bash
rm -rf site/platform/developer-guide
mkdocs build -f platform/developer-guide/mkdocs.yml -d ../../site/platform/developer-guide
```

Expected: the build succeeds with no new warnings compared with Step 1.

- [ ] **Step 7: Gate on rendered-text equality across the whole guide**

This is the step that decides whether minification ships. Every page is compared, not a sample.

```bash
python3 check_rendered_text.py /tmp/minify-before site/platform/developer-guide
```

Expected: `OK: rendered text identical across N page(s)` with N in the hundreds. Any `DIFFERENT` output means minification is altering visible text; revert Steps 3 and 4 and report the printed excerpt. Do not proceed.

- [ ] **Step 8: Verify code blocks are byte-identical**

`htmlmin` preserves `pre`, but this repository puts file names in code-block titles and relies on exact indentation in YAML and JSON samples, so confirm rather than trust.

```bash
python3 - <<'PY'
import pathlib
import re

PRE = re.compile(r"<pre\b.*?</pre>", re.S)
sample = pathlib.Path("/tmp/minify-sample-path").read_text().strip()
before_path = sample.replace("site/platform/developer-guide", "/tmp/minify-before", 1)

before = PRE.findall(pathlib.Path(before_path).read_text(encoding="utf-8"))
after = PRE.findall(pathlib.Path(sample).read_text(encoding="utf-8"))

assert before, f"no pre block found in {before_path}"
assert len(before) == len(after), f"pre block count changed: {len(before)} -> {len(after)}"
for index, (b, a) in enumerate(zip(before, after)):
    assert b == a, f"pre block {index} was modified"
print(f"{len(before)} pre block(s) byte-identical in {sample}")
PY
```

Expected: a non-zero count and `byte-identical`.

- [ ] **Step 9: Measure the saving and record the real number**

```bash
python3 measure_site_size.py site/platform/developer-guide --json > /tmp/minify-after.json
python3 - <<'PY'
import json

before = json.load(open("/tmp/minify-before.json"))
after = json.load(open("/tmp/minify-after.json"))
b = before["categories"]["HTML"]["bytes"]
a = after["categories"]["HTML"]["bytes"]
percent = 100 * (b - a) / b
print(f"HTML {b/1048576:.0f} MB -> {a/1048576:.0f} MB, saving {percent:.1f}%")
open("/tmp/minify-percent", "w").write(f"{percent:.1f}")
assert percent > 40, "saving far below the measured 57%; is the plugin applying?"
PY
```

Expected: a saving between roughly 50% and 60%. Below 40% means the plugin is not applying; recheck Step 5.

- [ ] **Step 10: Commit, using the measured number**

```bash
PERCENT=$(cat /tmp/minify-percent)
git add mkdocs.yml platform/user-guide/mkdocs.yml platform/developer-guide/mkdocs.yml platform/deployment-on-cloud/mkdocs.yml storefront/user-guide/mkdocs.yml storefront/developer-guide/mkdocs.yml marketplace/user-guide/mkdocs.yml marketplace/developer-guide/mkdocs.yml
git commit -m "build: enable HTML minification in root and guide configs

The minify plugin was declared in all eight configs without options, and its
default is minify_html: false, so it had no effect. Measured saving on the
platform developer guide is ${PERCENT}% of HTML bytes. Rendered text was
verified identical across every page of that guide, and pre blocks byte for
byte on a sample page.

This reaches the version being deployed. The four frozen versions keep their
un-minified HTML until they are redeployed, which is tracked separately.

cache_safe stays off: it renames extra_css and extra_javascript files, which
has previously broken deduplication and filled the deploy disk. minify_js and
minify_css stay off: negligible yield against a real risk to
version-redirect.js and scroll-menu.js."
rm -f /tmp/minify-percent /tmp/minify-before.json /tmp/minify-after.json /tmp/minify-sample-path
rm -rf /tmp/minify-before
```

---

### Task 7: Whole-build verification and result report

Earlier tasks verified one guide, one pair of snapshots, or one script. This task runs the full build, compares against the committed baselines, checks that symlinks survive a real container image, and records the result.

**Files:**
- Create: `.specs/2026-08-20-size-reduction-result.md`

**Interfaces:**
- Consumes: `measure_site_size.py`, `check_rendered_text.py`, the baselines in `.specs/baseline/`, and everything Tasks 1 to 6 changed.
- Produces: nothing other tasks call. This is the last task.

- [ ] **Step 1: Run the full local build**

```bash
cd /Users/symbot/DEV/vc-docs
rm -rf site
./build.sh 2>&1 | tee /tmp/full-build.log
echo "exit: ${PIPESTATUS[0]}"
```

Expected: exit 0. `build.sh` uses `set -euo pipefail`, so any guide failing stops it.

- [ ] **Step 2: Diff warnings against the committed baseline**

```bash
grep -E 'WARNING|ERROR' /tmp/full-build.log | sed -E 's/[0-9]{4}-[0-9]{2}-[0-9]{2}[T ][0-9:.]+Z?//g' | sort | uniq -c | sort -rn > /tmp/after-warnings.txt
diff .specs/baseline/build-warnings.txt /tmp/after-warnings.txt && echo "warnings unchanged" || echo "REVIEW THE DIFF ABOVE"
```

Expected: `warnings unchanged`. If lines appear, judge each one. A new warning naming a file whose path differs only in letter case is likely a macOS case-insensitivity phantom; confirm with `git ls-tree -r HEAD --name-only | grep -i <name>` against `ls` before treating it as real.

- [ ] **Step 3: Measure the built tree**

```bash
python3 measure_site_size.py site --json > /tmp/after-build.json
python3 measure_site_size.py site
```

Expected: a report with HTML well below its former per-page average. `./build.sh` produces the non-versioned build, so this measures the minification effect, not the versioned assembly.

- [ ] **Step 4: Verify symlinks survive a real container image**

The saving depends entirely on `COPY` preserving symlinks and nginx following them. The production image is built by an external action pinned to `@master`, so this checks the mechanism locally rather than assuming it.

Skip this step and record it as a gap if Docker is unavailable, but do not silently omit it.

```bash
command -v docker >/dev/null || { echo "GAP: docker unavailable, symlink survival unverified"; exit 0; }
rm -rf /tmp/image-trial && mkdir -p /tmp/image-trial/site
git archive origin/gh-pages platform/developer-guide | tar -x -C /tmp/image-trial/site
python3 - <<'PY'
from build_optimize import deduplicate_assets, deduplicate_binaries, format_size

deduplicate_assets("/tmp/image-trial/site")
replaced, freed = deduplicate_binaries("/tmp/image-trial/site")
print(f"prepared tree: {replaced} symlinks, {format_size(freed)} freed")
PY
cat > /tmp/image-trial/Dockerfile <<'EOF'
FROM nginx:alpine
COPY site /usr/share/nginx/html
EOF
docker build -t docs-symlink-trial /tmp/image-trial
echo "--- symlinks inside the image ---"
docker run --rm docs-symlink-trial find /usr/share/nginx/html -type l | head -5
docker run --rm docs-symlink-trial sh -c 'find /usr/share/nginx/html -type l | wc -l'
echo "--- a linked file served over HTTP ---"
docker run -d --name docs-symlink-trial-run -p 8899:80 docs-symlink-trial >/dev/null
LINK=$(docker run --rm docs-symlink-trial sh -c 'find /usr/share/nginx/html -type l -name "*.png" | head -1')
REL=${LINK#/usr/share/nginx/html/}
curl -s -o /dev/null -w "GET /$REL -> %{http_code} %{size_download} bytes\n" "http://localhost:8899/$REL"
docker rm -f docs-symlink-trial-run >/dev/null
docker rmi -f docs-symlink-trial >/dev/null
rm -rf /tmp/image-trial
```

Expected: a non-zero symlink count inside the image, proving `COPY` did not dereference them, and `200` with a non-zero byte count for the linked PNG, proving nginx follows them. A symlink count of zero means Docker dereferenced the links and the entire saving is lost in the image; that is a blocker for the whole approach and must be reported, not worked around.

- [ ] **Step 5: Look at the built site**

Automated checks do not catch a layout that renders but looks wrong.

```bash
python3 -m http.server 8123 --directory site
```

Open `http://localhost:8123/platform/developer-guide/`. Confirm the sidebar navigation expands, an abbreviation tooltip appears on hover, a table renders, and a code block keeps its indentation. Stop with Ctrl+C.

Expected: no visible difference from before the change.

- [ ] **Step 6: Run the full test suite**

```bash
python3 test_build_tools.py
```

Expected: `17 test(s) passed`.

- [ ] **Step 7: Write the result report**

Create `.specs/2026-08-20-size-reduction-result.md`. Every bracketed value must be replaced with a measured number taken from a command above or from `.specs/baseline/`. A remaining bracket means this task is unfinished.

```markdown
# Published size reduction: result

Date: [date the build was run]. Branch: [branch name].

## Measured effect

| Measure | Before | After | Source |
| --- | --- | --- | --- |
| HTML in the sample guide | [before] | [after] | Task 6 Step 9 |
| Binaries in a two-snapshot trial | [before] | [after] | Task 3 Step 6 |
| Symlinks created in that trial | 0 | [count] | Task 3 Step 6 |
| Remaining duplicates in that trial | [before] | 0 B | Task 3 Step 6 |
| Published tree, for reference | [from .specs/baseline/published-tree.json] | not redeployed | Task 2 Step 6 |

## Verification performed

- Rendered text identical across [count] pages of the platform developer guide.
- All `pre` blocks byte-identical on the sample page.
- `./build.sh` exit 0; warning set [unchanged / changed as follows: ...] against `.specs/baseline/build-warnings.txt`.
- All file and directory symlinks resolve inside the output tree.
- Symlinks inside a real nginx image: [count] present, linked PNG served with HTTP [code]. [Or: GAP, docker unavailable.]
- Visual check of navigation, tooltips, tables, and code blocks.

## Not achieved here

Minification reached only the version deployed from this branch. The four frozen
versions keep their un-minified HTML, about [figure] MB, until they are
redeployed. See the follow-up plan named in the plan document.

Docker layer stratification, ACR retention, `navigation.prune`, and GIF
conversion remain open. See the Out of scope section of
`.specs/2026-08-20-published-size-reduction-design.md`.

## Port required

**versioned-build-cicd.py** changed and now imports **build_optimize.py**.
Release branches carry frozen copies of the build script, so a port must carry
both files or the frozen script fails at import.
```

- [ ] **Step 8: Commit**

```bash
rm -rf site
git add .specs/2026-08-20-size-reduction-result.md
git commit -m "docs: record measured result of the published size reduction"
```

- [ ] **Step 9: Confirm nothing landed under docs/**

Everything in **docs** is published publicly. Four internal specs once sat there for three months.

```bash
git diff --name-only main...HEAD | grep '^docs/' && echo "STOP: working files under docs/" || echo "clean: nothing added under docs/"
```

Expected: `clean: nothing added under docs/`.

---

## Follow-up plan: redeploy the frozen versions

Not a task here. It needs its own plan because it has a hard external precondition and a different risk profile.

**Precondition.** ACR retention must exist first. A push to `release/**` builds and pushes a roughly 2 GB image that is never promoted to prod, so four redeploys add about 8 GB of undeployable images before returning anything. See decision 7 in the spec.

**What it buys.** 1308 MB off the `gh-pages` working tree, which every CI run checks out, and about 85 MB of registry bytes. The registry figure is small because HTML compresses 15.5x; the checkout figure is the real motivation.

**Why it is safe, already verified.** The toolchain is pinned identically on every branch, `requirements-docs.txt` blob `70bc2716` on `main`, `stable14`, and `stable15`, and blob `b31a3e7f` on `stable11` and `stable12` pinning the same mkdocs-material 9.5.27, mkdocs 1.6.1, and mike 2.2.0. No release branch has unpublished content: every branch tip is at or behind its last deploy. `VERSIONING.md:12` makes redeploy the sanctioned way to update a released version.

**Scope, which differs per branch.**

- `release/stable14` and `release/stable15`: `mkdocs.yml` edit only. Their **versioned-build-cicd.py** is byte-identical to `main`.
- `release/stable11` and `release/stable12`: also need **versioned-build-cicd.py** and **build_optimize.py** ported. Their build script is 12 KB and 20 KB against 22 KB on `main`.

**Extra verification those two need.** Both pin `mkdocs-awesome-pages-plugin==2.10.1` alongside `awesome-nav`, so two navigation plugins are active. Compare the set of generated page paths before and after the rebuild for those versions specifically, because a changed path breaks the inbound links that versioning exists to protect.

**Sequencing.** `concurrency` in the deploy workflow is keyed on the ref while every branch writes the same `gh-pages`, so the four deploys must run one at a time.

**Cost that does not reverse.** mike commits a full version tree rather than a patch. Twenty-eight commits later the history holds both the un-minified and the minified copy of every version, permanently.

---

## Self-Review

Checked against `.specs/2026-08-20-published-size-reduction-design.md`.

**Spec coverage.** Decision 1 is Task 3, which is deliberately ordered before minification. Decisions 2, 3, and 4 are Task 3 Step 3, each asserted by a test, and Task 4 Step 4 repeats the ordering rule in the local script with the same comment. Decision 5 is Task 6. Decision 6 is stated in Task 6's preamble, in its commit message, and in the result report's "Not achieved here" section, so the limit travels with the change. Decision 7 is the follow-up plan's precondition. Decisions 8 and 9 are Task 6 Step 10. Decision 10 is Task 1. Decision 11 needs no task: stable11 and stable12 are simply not excluded anywhere. Decision 12 is Task 2, including the git-ref mode that makes a baseline possible without a checkout.

The five spec risks each map to a step: minification altering every byte is Task 6 Step 7; whitespace collapse is Tasks 5 and 6 Step 7; symlink survival in the image is Task 7 Step 4; invisible directory symlinks are Task 2 Step 1, Task 3 Step 1, and Task 3 Step 7; history growth and serialization belong to the follow-up plan and are recorded there.

**Placeholders.** The only bracketed values are in the Task 7 Step 7 report template, where they are the deliverable's own blanks, and the step states that a remaining bracket means the task is unfinished. Task 6 Step 1 discovers its sample page rather than naming one, because the previously named `Getting-Started/index.html` does not exist in this repository.

**Type consistency.** `deduplicate_binaries(site_dir)` and `deduplicate_assets(site_dir)` both return `(int, int)`, in the spec, the docstrings, all five tests, and all four call sites across the two build scripts. `measure_tree(root)` and `measure_ref(ref)` return the same five keys, built by one `_blank()` helper so they cannot drift. `is_deduplicable(filename)` is defined once in **build_optimize.py** and used by both the optimizer and the harness, which is what makes "remaining duplicates: 0" a meaningful assertion. `format_size(size_bytes)` is defined once, in **build_optimize.py**, and imported by both build scripts and the harness. `rendered_text(path)` returns `str`; `compare_trees` returns `(list, int)`.

**Gaps found and closed during this revision.**

1. The headline forecast was wrong. It assumed minification would shrink the whole 3039 MB HTML corpus, but mike deploys one version per run, so it reaches only `latest`. The goal, the ordering, and the expected-result table are rewritten around the compressed-registry measurement, which puts media deduplication first.
2. Absolute figures were taken from a January working copy holding three versions. The real tree holds five versions and 5086 MB. Task 2 now reads `origin/gh-pages` directly so a baseline cannot go stale again.
3. The sample page named in the minification task did not exist. It is now discovered by search.
4. The rendered-text checker used a tag regex that truncates on a `>` inside a quoted attribute, and an inline-tag set missing `label`, `button`, `output`, and others. It now uses `html.parser` and the full phrasing-content set, with tests for both defects.
5. The gate compared two pages. It now compares every page in a tree, including detecting pages that appear or disappear.
6. The duplicate metric and the optimizer used different extension sets, so "remaining duplicates near zero" was unfalsifiable. They now share `is_deduplicable`, and the assertion is exact zero.
7. Both walks ignored directory symlinks, which is the only kind `deduplicate_assets` creates. Both now count and prune them, with tests.
8. Symlinks were charged zero bytes. They are now charged `lstat` size.
9. No baseline of build warnings existed, so "warnings unchanged" was not checkable. Task 2 Step 7 commits one.
10. `versioned-build.py` discarded the version it had just built and then reported the remote. Task 4 Step 3 fixes it and makes the fetch fail loudly instead of silently.
11. The stated failing-test output for a missing module was impossible, since the module loads at import time. Expectations now distinguish import-time failure from per-test failure, and a `@test` decorator replaces the hand-maintained list that made the two easy to confuse. The runner also catches every exception rather than only `AssertionError`: a test written before its implementation fails with `AttributeError`, which would otherwise crash the run and hide the tests that pass, making the stated Task 3 Step 2 output impossible for a second reason.
12. A commit message hard-coded 57%. It now interpolates the measured value.

---

## Post-execution corrections

Three defects in this plan's own reference code were found by review during execution and corrected in the delivered code. They are recorded here so that anyone re-executing the plan does not reintroduce them from the text above. The authoritative record of each is the SDD ledger.

1. **Task 2, the size harness.** Directory symlinks were counted but never charged their `lstat` bytes, and `measure_ref` ignored the git file mode so a symlink blob (`120000`) was silently treated as a regular file, making its `symlinks` key structurally unreachable. Both are fixed with covering tests. A private `_digest` that duplicated `build_optimize.file_digest` was also removed.
2. **Task 3, `deduplicate_binaries`.** The replacement was a non-atomic `os.remove` followed by `os.symlink`; an interrupt between them lost the file with no rerun recovery. It is now a symlink at a temporary name followed by `os.replace`.
3. **Task 3, the determinism test.** As written it repeated one identical run rather than comparing two orders, and it killed the unsorted-walk mutant only because APFS returns readdir entries in creation order. It now monkeypatches `os.walk` to force reverse order, which is independent of the filesystem, and both the dirnames and the filenames sort were confirmed load-bearing by killing each mutant in isolation. Varying file creation order, which this plan originally suggested, does not work: APFS returned alphabetical order regardless.

The ordering rule stated throughout this document was also imprecise. The canonical copy is the first path yielded by a sorted walk, which is a sorted pre-order traversal and is not the same as the lexicographically first path in the tree: with `v1/shot.png` and `v1x.png` holding identical bytes the walk keeps `v1x.png`, because `/` is 0x2F and `x` is 0x78. Determinism, the property that matters, is unaffected.
