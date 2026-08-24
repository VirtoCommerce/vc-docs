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
import subprocess
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


@test
def test_measure_charges_directory_symlinks_their_own_size():
    """A directory symlink must contribute its own lstat size, never zero.

    Fix round 1, finding 1: measure_tree counted the directory symlink in
    symlink_dirs but added nothing to total_bytes for it.
    """
    tree = make_tree({os.path.join("v1", "assets", "shot.png"): b"y" * 500})
    try:
        link = os.path.join(tree, "v2", "assets")
        os.makedirs(os.path.dirname(link))
        os.symlink(os.path.join("..", "v1", "assets"), link)
        link_size = os.lstat(link).st_size

        report = measure.measure_tree(tree)

        assert report["symlink_dirs"] == 1, report
        assert report["total_bytes"] == 500 + link_size, report
    finally:
        shutil.rmtree(tree)


@test
def test_measure_ref_counts_a_symlink_blob_instead_of_a_regular_file():
    """git stores a symlink as a blob with mode 120000; measure_ref must not
    silently treat it as a regular file.

    Fix round 1, finding 2: measure_ref never looked at the mode field, so a
    symlink blob was added to a size category and never counted as a symlink.
    Builds a throwaway repository so a real symlink blob exists to measure.
    """
    repo = tempfile.mkdtemp(prefix="build-tools-repo-")
    try:
        def run(*args):
            subprocess.run(
                ["git", *args], cwd=repo, check=True, capture_output=True, text=True
            )

        run("init", "-q")
        run("config", "user.email", "test@example.com")
        run("config", "user.name", "Test")
        with open(os.path.join(repo, "shot.png"), "wb") as handle:
            handle.write(b"y" * 500)
        os.symlink("shot.png", os.path.join(repo, "alias.png"))
        run("add", "-A")
        run("commit", "-q", "-m", "init")

        report = measure.measure_ref("HEAD", cwd=repo)

        assert report["symlinks"] == 1, report
        assert report["categories"]["Images"]["files"] == 1, report
    finally:
        shutil.rmtree(repo)


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
def test_dedup_replacement_is_atomic_and_leaves_no_temp_files():
    """The swap creates a temp symlink and moves it into place with
    os.replace, so a successful run must leave a working symlink behind, no
    ".dedup-tmp" artifact, and a stable, idempotent result on a rerun."""
    tree = make_tree({
        os.path.join("v1", "media", "shot.png"): b"y" * 500,
        os.path.join("v2", "media", "shot.png"): b"y" * 500,
    })
    try:
        replaced, freed = optimize.deduplicate_binaries(tree)
        assert replaced == 1, replaced
        assert freed == 500, freed

        duplicate = os.path.join(tree, "v2", "media", "shot.png")
        assert os.path.islink(duplicate)
        with open(duplicate, "rb") as handle:
            assert handle.read() == b"y" * 500, "symlink does not resolve to the content"

        leftovers = [
            name for name in os.listdir(os.path.dirname(duplicate))
            if name.endswith(".dedup-tmp")
        ]
        assert not leftovers, leftovers

        # The tree is already fully deduplicated, so a rerun must be a no-op
        # and must not disturb the working symlink.
        replaced_again, freed_again = optimize.deduplicate_binaries(tree)
        assert replaced_again == 0, replaced_again
        assert freed_again == 0, freed_again
        assert os.path.islink(duplicate)
        with open(duplicate, "rb") as handle:
            assert handle.read() == b"y" * 500
    finally:
        shutil.rmtree(tree)


@test
def test_dedup_rerun_recovers_from_a_leftover_temp_file():
    """A leftover ".dedup-tmp" from an earlier interrupted run (a crash
    between creating the temp symlink and the atomic rename) must not break
    the next run: it is not deduplicable itself, so it is never touched by the
    walk directly, and it is cleared only when the real file it shadows is
    processed again."""
    tree = make_tree({
        os.path.join("v1", "media", "shot.png"): b"y" * 500,
        os.path.join("v2", "media", "shot.png"): b"y" * 500,
    })
    try:
        stale = os.path.join(tree, "v2", "media", "shot.png.dedup-tmp")
        os.symlink("bogus-leftover-target", stale)

        replaced, freed = optimize.deduplicate_binaries(tree)

        assert replaced == 1, replaced
        assert freed == 500, freed
        duplicate = os.path.join(tree, "v2", "media", "shot.png")
        assert os.path.islink(duplicate)
        with open(duplicate, "rb") as handle:
            assert handle.read() == b"y" * 500
        assert not os.path.lexists(stale), "stale temp file must be cleared, not left behind"
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
def test_dedup_canonical_choice_survives_reversed_walk_order():
    """Determinism: the file that sorts first must survive no matter what
    order the filesystem hands dirnames and filenames back in.

    Building the tree in two different creation orders and hoping that
    surfaces a missing `sorted(...)` call through the filesystem's own
    readdir order is not reliable: measured directly on this machine
    (macOS/APFS), a two-file directory came back in alphabetical order from
    os.scandir regardless of which file was created first, so a missing sort
    on the filenames pass would have gone unnoticed. CI runs on a different
    filesystem (ubuntu-latest) where the risk runs the other way. This
    monkeypatches os.walk instead, forcing dirnames and filenames into
    reverse-alphabetical order on every call, independent of what any real
    filesystem happens to do, so a missing `sorted(...)` on either the
    dirnames or the filenames pass is guaranteed to flip the outcome.
    """
    real_walk = os.walk

    def reversed_walk(top, *args, **kwargs):
        for dirpath, dirnames, filenames in real_walk(top, *args, **kwargs):
            dirnames[:] = list(reversed(sorted(dirnames)))
            yield dirpath, dirnames, list(reversed(sorted(filenames)))

    tree = make_tree({
        os.path.join("a-version", "media", "shot.png"): b"y" * 500,
        os.path.join("b-version", "media", "shot.png"): b"y" * 500,
        os.path.join("c-version", "media", "m.png"): b"z" * 500,
        os.path.join("c-version", "media", "n.png"): b"z" * 500,
    })
    os.walk = reversed_walk
    try:
        optimize.deduplicate_binaries(tree)
        # Exercises the dirnames sort: "a-version" must still precede
        # "b-version" even though the fake walk visits directories in
        # reverse-alphabetical order.
        assert not os.path.islink(os.path.join(tree, "a-version", "media", "shot.png"))
        assert os.path.islink(os.path.join(tree, "b-version", "media", "shot.png"))
        # Exercises the filenames sort: "m.png" must still precede "n.png"
        # within the same directory.
        assert not os.path.islink(os.path.join(tree, "c-version", "media", "m.png"))
        assert os.path.islink(os.path.join(tree, "c-version", "media", "n.png"))
    finally:
        os.walk = real_walk
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
