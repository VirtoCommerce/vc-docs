#!/usr/bin/env python3
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


def list_relative_files(folder):
    """Return the set of file paths under folder, relative to folder."""
    files = set()
    for dirpath, _, filenames in os.walk(folder):
        for filename in filenames:
            files.add(os.path.relpath(os.path.join(dirpath, filename), folder))
    return files


def deduplicate_assets(site_dir):
    """
    Replace duplicate MkDocs theme assets folders with symlinks to the root assets.

    MkDocs Material theme copies ~11MB of assets (CSS, JS, fonts, icons) into each
    subsite build. With 10+ subsites, this adds ~100MB+ of duplicate content, so
    nested assets/ folders are replaced with symlinks to the root assets/.

    IMPORTANT: only deduplicate a nested assets/ folder when every file in it also
    exists in the root assets/. Material uses content-hashed asset filenames
    (e.g. main.<hash>.min.css); a mike version built with a different Material
    release carries a DIFFERENT hash. Blindly symlinking such a folder to the root
    assets/ (built with the current Material) would hide that version's stylesheets,
    so its pages reference a hash that no longer exists and load unstyled. Folders
    whose files are not a subset of the root assets/ are kept as real files.
    """
    root_assets = os.path.join(site_dir, "assets")

    if not os.path.exists(root_assets):
        print("    ⚠️  Root assets folder not found, skipping deduplication")
        return 0, 0

    # Files available in the root assets/ (relative paths). A nested folder can
    # only be safely symlinked here if all of its files are present in this set.
    root_files = list_relative_files(root_assets)

    replaced_count = 0
    freed_bytes = 0
    kept_count = 0

    for root, dirs, _ in os.walk(site_dir, topdown=True):
        if "assets" in dirs and root != site_dir:
            assets_path = os.path.join(root, "assets")

            # Skip if already a symlink
            if os.path.islink(assets_path):
                continue

            rel_assets = os.path.relpath(assets_path, site_dir)

            # Keep version-specific assets that the root assets/ does not contain
            # (e.g. an older Material build's content-hashed stylesheets).
            nested_files = list_relative_files(assets_path)
            if not nested_files.issubset(root_files):
                kept_count += 1
                print(f"    Kept {rel_assets}/ (version-specific assets differ from root)")
                continue

            # Calculate size before removal
            folder_size = get_folder_size(assets_path)
            freed_bytes += folder_size

            # Calculate relative path from current directory to root assets
            rel_path = os.path.relpath(root_assets, root)

            # Remove the duplicate folder and create symlink
            shutil.rmtree(assets_path)
            os.symlink(rel_path, assets_path)

            replaced_count += 1
            # Print relative path from site_dir for cleaner output
            print(f"    Symlinked {rel_assets}/ -> {rel_path}")

    if kept_count:
        print(f"    Kept {kept_count} version-specific assets folder(s) intact")

    return replaced_count, freed_bytes


def get_folder_size(path):
    """Calculate total size of a folder in bytes."""
    total = 0
    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            # Skip symbolic links
            if not os.path.islink(filepath):
                total += os.path.getsize(filepath)
    return total


def format_size(size_bytes):
    """Format bytes as human-readable size."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} TB"


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

    The canonical copy is the lexicographically first path, taken from a sorted
    walk. The choice must be deterministic: an identical input tree has to
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
