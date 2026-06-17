"""Append a content-hash query string to our extra_css links to defeat Cloudflare caching.

Our extra_css entries (main.css, version-selector.css, ai-overrides.css) have stable,
non-hashed URLs. Cloudflare caches them by URL, so editing a file does NOT change its
URL and the edge keeps serving the pre-edit copy until purged. We have no Cloudflare
access.

This hook appends a short content hash as a query string to each local extra_css link
(e.g. version-selector.css?h=4f2a1c8e). Cloudflare's cache key includes the query
string, so any edit changes the hash, hence the URL, hence the cache key, and the edge
fetches the current file. The filename on disk is left unchanged, which keeps the
versioned-build deduplication step working (it symlinks identical per-version asset
folders to the root assets/; renaming files per build would defeat that and balloon the
image past the runner's disk).

Registered per guide in mkdocs.yml under `hooks:`. External URLs and files not found on
disk are left untouched.
"""

import hashlib
import os


def on_files(files, config):
    rewritten = []
    for css in config.get("extra_css", []):
        if "://" in css or css.startswith("//") or "?" in css:
            rewritten.append(css)
            continue

        file = files.get_file_from_path(css)
        abs_src = getattr(file, "abs_src_path", None) if file else None
        if not abs_src or not os.path.isfile(abs_src):
            # Not one of our local files; leave as-is.
            rewritten.append(css)
            continue

        with open(abs_src, "rb") as handle:
            digest = hashlib.md5(handle.read()).hexdigest()[:8]

        rewritten.append(f"{css}?h={digest}")

    config["extra_css"] = rewritten
    return files
