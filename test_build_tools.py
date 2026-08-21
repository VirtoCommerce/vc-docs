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
