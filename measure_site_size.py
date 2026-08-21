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
import json
import os
import subprocess

from build_optimize import file_digest, format_size, is_deduplicable

# First match wins; "Other" catches the rest.
CATEGORIES = [
    ("HTML", {".html", ".htm"}),
    ("Images", {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".ico"}),
    ("Fonts", {".woff", ".woff2", ".ttf", ".eot", ".otf"}),
    ("JS", {".js", ".map"}),
    ("CSS", {".css"}),
    ("JSON", {".json"}),
]


def categorize(filename):
    extension = os.path.splitext(filename)[1].lower()
    for name, extensions in CATEGORIES:
        if extension in extensions:
            return name
    return "Other"


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
        for linked_dir in linked_dirs:
            # A directory symlink is not free either: it occupies its own
            # target string, same as a file symlink. Charging zero here would
            # under-report total_bytes by the sum of every alias symlink.
            report["total_bytes"] += os.lstat(os.path.join(dirpath, linked_dir)).st_size
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
                key = file_digest(path)
                if key in seen:
                    report["duplicate_bytes"] += size
                else:
                    seen.add(key)

    return report


def measure_ref(ref, cwd=None):
    """Measure a git ref without checking it out.

    Blob OIDs are content hashes, so identical content shares an OID and
    duplicates are exact rather than sampled. cwd lets a test point this at
    a throwaway repository instead of the current one; the default behavior
    (run in the current directory) is unchanged.
    """
    output = subprocess.run(
        ["git", "ls-tree", "-r", "-l", ref],
        capture_output=True, text=True, check=True, cwd=cwd,
    ).stdout

    report = _blank()
    seen = set()

    for line in output.splitlines():
        meta, _, path = line.partition("\t")
        fields = meta.split()
        if len(fields) < 4 or fields[1] != "blob":
            continue
        mode = fields[0]
        oid = fields[2]
        if fields[3] == "-":
            continue
        size = int(fields[3])
        filename = os.path.basename(path)

        if mode == "120000":
            # A symlink is stored as a blob whose content is its target
            # path, so its reported size is the same quantity os.lstat's
            # st_size gives a real filesystem symlink. Git has no separate
            # representation for a symlink to a directory versus a file, so
            # this can only ever populate "symlinks", never "symlink_dirs".
            report["symlinks"] += 1
            report["total_bytes"] += size
            continue

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
