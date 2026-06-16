"""Content-hash our own extra_css filenames so Cloudflare cannot serve a stale copy.

Our extra_css entries (main.css, fonts.css, version-selector.css, ai-overrides.css)
have stable, non-hashed URLs. Cloudflare caches them by URL, so editing a file does
NOT change its URL and the edge keeps serving the pre-edit copy until the cache is
purged. We have no Cloudflare access, so instead we rename each local extra_css file
to include a short content hash at build time (e.g. version-selector.4f2a1c8e.css) and
rewrite the <link> reference to match. Any future edit changes the hash, hence the URL,
hence the cache key, so the edge always fetches the current file.

Material already does this for its own bundled assets (main.<hash>.min.css); this hook
extends the same cache-busting to our hand-written stylesheets.

Registered per guide in mkdocs.yml under `hooks:`. External URLs (http(s)://, //) and
files not found on disk are left untouched.
"""

import hashlib
import os


def on_files(files, config):
    rewritten = []
    for css in config.get("extra_css", []):
        if "://" in css or css.startswith("//"):
            rewritten.append(css)
            continue

        file = files.get_file_from_path(css)
        abs_src = getattr(file, "abs_src_path", None) if file else None
        if not abs_src or not os.path.isfile(abs_src):
            # Not one of our local files (or already missing); leave as-is.
            rewritten.append(css)
            continue

        with open(abs_src, "rb") as handle:
            digest = hashlib.md5(handle.read()).hexdigest()[:8]

        base, ext = os.path.splitext(css)
        hashed = f"{base}.{digest}{ext}"

        # Repoint the build output to the hashed name. dest_uri/url/abs_dest_path are
        # cached_property values on mkdocs 1.6 File objects; assigning shadows them.
        file.dest_uri = hashed
        file.url = hashed
        file.abs_dest_path = os.path.normpath(os.path.join(file.dest_dir, hashed))

        rewritten.append(hashed)

    config["extra_css"] = rewritten
    return files
