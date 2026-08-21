#!/usr/bin/env python3
"""
Versioned build script - combines non-versioned sites with versioned content
This is the proper way to build a complete site with versioning
"""

import os
import sys
import subprocess
import shutil
import tempfile
import http.server
import socketserver
import json

from build_optimize import deduplicate_assets, deduplicate_binaries, format_size

SITE_URL = "https://docs.virtocommerce.org"

VERSIONED_SUBSITES = [
    "platform/developer-guide",
    "platform/user-guide",
    "platform/deployment-on-cloud",
    "marketplace/developer-guide",
    "marketplace/user-guide",
    "storefront/developer-guide",
    "storefront/user-guide"
]

def get_latest_version(output_dir, subsite):
    """Get the actual version number that has 'latest' alias from versions.json"""
    versions_path = os.path.join(output_dir, subsite, "versions.json")
    if os.path.exists(versions_path):
        with open(versions_path) as f:
            versions = json.load(f)
        for v in versions:
            if "latest" in v.get("aliases", []):
                return v["version"]
        # If no 'latest' alias found, return first version
        if versions:
            return versions[0]["version"]
    return None


def generate_sitemap_index(output_dir):
    """Generate sitemap_index.xml referencing all subsite sitemaps for the latest version"""
    sitemap_entries = []

    # Add root sitemap
    root_sitemap = os.path.join(output_dir, "sitemap.xml")
    if os.path.exists(root_sitemap):
        sitemap_entries.append(f"{SITE_URL}/sitemap.xml")

    # Add subsite sitemaps for latest version
    for subsite in VERSIONED_SUBSITES:
        actual_version = get_latest_version(output_dir, subsite)
        if not actual_version:
            print(f"    ⚠️  No version found for {subsite}, skipping sitemap")
            continue

        sitemap_path = os.path.join(output_dir, subsite, actual_version, "sitemap.xml")
        if os.path.exists(sitemap_path):
            sitemap_entries.append(f"{SITE_URL}/{subsite}/{actual_version}/sitemap.xml")
            print(f"    Added sitemap for {subsite} (v{actual_version})")
        else:
            print(f"    ⚠️  Sitemap not found: {sitemap_path}")

    # Write sitemap index
    xml_entries = "\n".join(
        f"    <sitemap>\n        <loc>{url}</loc>\n    </sitemap>"
        for url in sitemap_entries
    )
    sitemap_index_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{xml_entries}
</sitemapindex>
"""
    sitemap_index_path = os.path.join(output_dir, "sitemap_index.xml")
    with open(sitemap_index_path, "w") as f:
        f.write(sitemap_index_xml)

    print(f"    ✅ Generated sitemap_index.xml with {len(sitemap_entries)} sitemaps")


def generate_robots_txt(output_dir):
    """Generate robots.txt with sitemap reference"""
    robots_content = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap_index.xml
"""
    robots_path = os.path.join(output_dir, "robots.txt")
    with open(robots_path, "w") as f:
        f.write(robots_content)
    print(f"    ✅ Generated robots.txt")


def copy_static_root_files(output_dir):
    """Copy static files from docs/ that must be at site root (e.g. Google verification)"""
    docs_dir = "docs"
    copied = 0
    for filename in os.listdir(docs_dir):
        filepath = os.path.join(docs_dir, filename)
        if os.path.isfile(filepath) and not filename.endswith(".md"):
            dest = os.path.join(output_dir, filename)
            if not os.path.exists(dest):
                shutil.copy2(filepath, dest)
                print(f"    Copied {filename} to {output_dir}/")
                copied += 1
    if copied:
        print(f"    ✅ Copied {copied} static root files")
    else:
        print(f"    No additional static files to copy")


def merge_search_indexes(output_dir):
    """Merge search indexes from all versioned subsites into a global index"""
    merged_docs = []
    config = {"lang": ["en"], "separator": "[\\s\\-]+", "pipeline": ["stopWordFilter"], "fields": {"title": {"boost": 1000.0}, "text": {"boost": 1.0}, "tags": {"boost": 1000000.0}}}

    for subsite in VERSIONED_SUBSITES:
        # Get actual version from versions.json (latest is an alias)
        actual_version = get_latest_version(output_dir, subsite)
        if not actual_version:
            print(f"    ⚠️  No versions.json found for {subsite}")
            continue

        index_path = os.path.join(output_dir, subsite, actual_version, "search", "search_index.json")
        if os.path.exists(index_path):
            with open(index_path) as f:
                data = json.load(f)

            # Add prefix using 'latest' alias for URL consistency
            prefix = f"{subsite}/latest/"
            for doc in data.get("docs", []):
                doc["location"] = prefix + doc["location"]
                merged_docs.append(doc)

            print(f"    Added {len(data.get('docs', []))} docs from {subsite} (v{actual_version})")
        else:
            print(f"    ⚠️  Index not found: {index_path}")

    # Write merged index
    merged_index = {"config": config, "docs": merged_docs}
    search_dir = os.path.join(output_dir, "search")
    os.makedirs(search_dir, exist_ok=True)

    with open(os.path.join(search_dir, "search_index.json"), "w") as f:
        json.dump(merged_index, f)

    print(f"    Total: {len(merged_docs)} docs in global search index")

def run_command(cmd, check=True):
    """Run shell command and return result"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"❌ Error: {result.stderr}")
        sys.exit(1)
    return result

def main():
    print("🚀 Versioned build of documentation sites...")

    # Check if we're in the right directory
    if not os.path.exists("mkdocs.yml"):
        print("❌ Please run this script from the vc-docs root directory")
        sys.exit(1)

    # Check if mike is installed
    result = run_command("mike --version", check=False)
    if result.returncode != 0:
        print("❌ Mike is not installed. Please install it:")
        print("pip install mike")
        sys.exit(1)

    print("📋 Step 1: Initialize local gh-pages folder")

    # Initialize local gh-pages folder if it doesn't exist
    if not os.path.exists("gh-pages"):
        print("  Creating local gh-pages folder and initializing git repository...")
        try:
            # Create gh-pages directory
            os.makedirs("gh-pages", exist_ok=True)

            # Initialize git repository in gh-pages folder
            run_command("cd gh-pages && git init", check=False)

            # Add remote origin (assuming it's the same as current repo)
            result = run_command("git remote get-url origin", check=False)
            if result.returncode == 0:
                origin_url = result.stdout.strip()
                run_command(f"cd gh-pages && git remote add origin {origin_url}", check=False)

            # Fetch and checkout gh-pages branch
            run_command("cd gh-pages && git fetch origin gh-pages", check=False)
            run_command("cd gh-pages && git checkout -b gh-pages origin/gh-pages", check=False)

            print("  ✅ Local gh-pages folder initialized with gh-pages branch")
        except Exception as e:
            print(f"  ⚠️  Warning: Could not initialize gh-pages folder: {e}")
            print("  Creating empty gh-pages folder...")
            os.makedirs("gh-pages", exist_ok=True)
    else:
        print("  ✅ Local gh-pages folder already exists")

        # Check if gh-pages folder has git repository and is on gh-pages branch
        try:
            result = run_command("cd gh-pages && git branch --show-current", check=False)
            if result.returncode == 0:
                current_branch = result.stdout.strip()
                if current_branch != "gh-pages":
                    print(f"  Switching gh-pages folder to gh-pages branch (currently on {current_branch})...")
                    run_command("cd gh-pages && git checkout gh-pages", check=False)
                    print("  ✅ Switched to gh-pages branch")
                else:
                    print("  ✅ Already on gh-pages branch")
            else:
                print("  ⚠️  gh-pages folder is not a git repository")
        except Exception as e:
            print(f"  ⚠️  Warning: Could not check gh-pages branch: {e}")

    print("📋 Step 2: Build non-versioned sites (root + intermediate)")

    # Create site directory
    os.makedirs("site", exist_ok=True)

    # Build root site using mkdocs.yml (WITHOUT monorepo plugin)
    # This builds only the main page + redirects, without rebuilding all subsites
    # Search index will be merged from versioned subsite indexes later
    print("  Building root site (without monorepo)...")
    run_command("mkdocs build -f mkdocs.yml -d site", check=False)

    # Build intermediate landing pages (platform, marketplace, storefront)
    # Using mkdocs.yml configs which override plugins to exclude redirects
    # This prevents generating hundreds of redirect HTML files
    print("  Building intermediate landing pages...")
    run_command("mkdocs build -f storefront/mkdocs.yml -d ../site/storefront", check=False)
    run_command("mkdocs build -f platform/mkdocs.yml -d ../site/platform", check=False)
    run_command("mkdocs build -f marketplace/mkdocs.yml -d ../site/marketplace", check=False)

    print("✅ Non-versioned sites built")

    print("📋 Step 3: Deploy versioned subsites with Mike")

    # Deploy all subsites with version 1.0
    subsites = [
        "marketplace/developer-guide",
        "marketplace/user-guide",
        "platform/developer-guide",
        "platform/user-guide",
        "platform/deployment-on-cloud",
        "storefront/developer-guide",
        "storefront/user-guide"
    ]
    version_file = "VERSION"
    if not os.path.exists(version_file):
        print(f"❌ {version_file} file not found in repo root. See VERSIONING.md.")
        sys.exit(1)
    with open(version_file) as f:
        version = f.read().strip()
    if not version:
        print(f"❌ {version_file} is empty. See VERSIONING.md.")
        sys.exit(1)
    print(f"Using version {version} from {version_file}")

    # Added by ruling (not requested by the original brief): check each mike
    # command's return code and collect failures instead of printing
    # "deployed" unconditionally. Without this, a failed mike deploy would
    # still be reported as a success, and the size report later in this
    # script would describe content that was never actually deployed.
    failed_subsites = []
    for subsite in subsites:
        config = f"{subsite}/mkdocs.yml"
        print(f"  Deploying {subsite} version {version}...")

        # Deploy with version 1.0 and set as latest.
        # --alias-type=copy: copy files into latest/ instead of redirect stubs, so
        # binary assets (images, PDFs) resolve under /<subsite>/latest/... too.
        # Pre-existing bug fix: only append "latest" as an alias when the
        # version being deployed is not itself "latest" (mirrors
        # versioned-build-cicd.py's `version != "latest"` guard). Without
        # this, mike rejects a version that lists its own name as an alias
        # with "duplicated version and alias" -- which is exactly what has
        # been silently breaking every local build since VERSION became the
        # literal string "latest".
        deploy_cmd = (
            f'mike deploy -F "{config}" --deploy-prefix "{subsite}" '
            f'--alias-type=copy --update-aliases "{version}"'
        )
        if version != "latest":
            deploy_cmd += " latest"
        result = run_command(deploy_cmd, check=False)
        if result.returncode != 0:
            print(f"  ❌ mike deploy failed for {subsite}")
            print(f"     command: {deploy_cmd}")
            print(f"     stderr: {result.stderr}")
            failed_subsites.append(subsite)
            continue

        # Set as default version
        set_default_cmd = f'mike set-default -F "{config}" --deploy-prefix "{subsite}" {version}'
        result = run_command(set_default_cmd, check=False)
        if result.returncode != 0:
            print(f"  ❌ mike set-default failed for {subsite}")
            print(f"     command: {set_default_cmd}")
            print(f"     stderr: {result.stderr}")
            failed_subsites.append(subsite)
            continue

        print(f"  ✅ {subsite} deployed")

    if failed_subsites:
        print(f"❌ Mike deploy failed for {len(failed_subsites)} subsite(s): {', '.join(failed_subsites)}")
        print("Aborting before the size report to avoid measuring content that never deployed.")
        sys.exit(1)

    print("✅ Versioned subsites deployed")

    print("📋 Step 4: Export versioned content from the local gh-pages ref")

    # mike deploy above wrote to THIS repository's local gh-pages ref, not to
    # the gh-pages/ folder (a separate, independent clone) and not to the
    # remote. This repository can be a shallow clone while gh-pages/ is a
    # full clone, and git refuses to fetch a shallow history into a complete
    # repository ("shallow roots are not allowed to be updated") -- so a
    # fetch-then-reset through gh-pages/ cannot work here no matter which ref
    # it names. Export the deployed tree directly from the local ref with
    # git archive instead, into a throwaway temp directory, and never touch
    # the gh-pages/ folder for this purpose.
    print("  Exporting versioned content from the local gh-pages ref...")

    ref_check = run_command("git rev-parse --verify --quiet gh-pages", check=False)
    if not ref_check.stdout.strip():
        print("  ❌ No local gh-pages ref found; nothing to export")
        sys.exit(1)

    gh_pages_export_dir = tempfile.mkdtemp(prefix="vc-docs-gh-pages-export-")
    archive_path = os.path.join(gh_pages_export_dir, "archive.tar")
    try:
        # Two separately-checked commands, not a shell pipeline. run_command
        # uses subprocess.run(shell=True), i.e. /bin/sh -c; a pipeline's exit
        # status is the LAST command's (tar), not git archive's, and
        # pipefail is never set. If git archive failed for a reason the
        # ref-existence check above does not catch (a corrupt object, disk
        # pressure, a permissions problem), tar would receive empty stdin,
        # exit 0, and this step would silently report success over an empty
        # directory -- exactly the silent-failure class this task exists to
        # remove. The temp archive file lives inside gh_pages_export_dir, so
        # the single rmtree in the finally block below cleans up both it and
        # the extracted content, on success or failure alike.
        result = run_command(f'git archive gh-pages -o "{archive_path}"', check=False)
        if result.returncode != 0:
            print(f"  ❌ Could not export the local gh-pages ref: {result.stderr}")
            sys.exit(1)

        result = run_command(f'tar -xf "{archive_path}" -C "{gh_pages_export_dir}"', check=False)
        if result.returncode != 0:
            print(f"  ❌ Could not extract the gh-pages export: {result.stderr}")
            sys.exit(1)

        print(f"  ✅ Exported local gh-pages content to {gh_pages_export_dir}")

        print("📋 Step 5: Copy versioned content from the export to site")

        print("  Copying versioned content from the export...")
        # Copy versioned subsites to site directory. Iterate the known list
        # of subsites (VERSIONED_SUBSITES) rather than every
        # {subsite}x{guide} combination -- not every subsite has every guide
        # (only platform has deployment-on-cloud), and a missing EXPECTED
        # subsite here must stop the script rather than merely warn: a
        # warning that lets the run continue is what turned the Finding 1
        # bug into a false success instead of a loud failure.
        for subsite in VERSIONED_SUBSITES:
            src = os.path.join(gh_pages_export_dir, subsite)
            if not os.path.exists(src):
                print(f"  ❌ {src} not found in the gh-pages export")
                sys.exit(1)
            dst = f"site/{subsite}"
            print(f"  Copying {src} to {dst}")
            if os.path.exists(dst):
                shutil.rmtree(dst)
            shutil.copytree(src, dst, ignore=shutil.ignore_patterns('.git'))
            print(f"  ✅ Copied {src} to {dst}")

        print("✅ Versioned content copied to site")
    finally:
        # Clean up the temp export (including the temp archive file) regardless
        # of success or failure above.
        shutil.rmtree(gh_pages_export_dir, ignore_errors=True)

    print("📋 Step 6: Extract sitemaps from copied content")

    # Extract sitemap.xml files from the copied content and copy to subsites
    versioned_subsites = [
        "marketplace/developer-guide",
        "marketplace/user-guide",
        "platform/developer-guide",
        "platform/user-guide",
        "platform/deployment-on-cloud",
        "storefront/developer-guide",
        "storefront/user-guide"
    ]

    for subsite in versioned_subsites:
        # Look for sitemap in the copied content (e.g., site/storefront/developer-guide/sitemap.xml)
        sitemap_path = f"site/{subsite}/sitemap.xml"
        target_sitemap_path = f"{subsite}/sitemap.xml"

        if os.path.exists(sitemap_path):
            print(f"  Extracting sitemap from {sitemap_path} to {target_sitemap_path}")
            # Ensure target directory exists
            os.makedirs(os.path.dirname(target_sitemap_path), exist_ok=True)
            # Copy sitemap
            shutil.copy2(sitemap_path, target_sitemap_path)
            print(f"  ✅ Sitemap copied to {target_sitemap_path}")
        else:
            print(f"  ⚠️  Sitemap not found at {sitemap_path}")

    print("✅ Sitemaps extracted from copied content")

    print("📋 Step 7: Merge search indexes from versioned subsites")

    # Merge search indexes from all versioned subsites into a global search index
    # This replaces the monorepo-generated index without rebuilding all subsites
    merge_search_indexes("site")

    print("✅ Search indexes merged")

    print("📋 Step 8: Generate SEO files (sitemap index, robots.txt, static root files)")
    generate_sitemap_index("site")
    generate_robots_txt("site")
    copy_static_root_files("site")
    print("✅ SEO files generated")

    # Cleanup
    if os.path.exists("mkdocs-temp-root.yml"):
        os.remove("mkdocs-temp-root.yml")

    print("📋 Step 9: Optimize build size (remove duplicates)")

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
    # sys.executable, not the literal "python3": run_command uses shell=True,
    # so a bare "python3" would resolve off the invoking shell's PATH rather
    # than the interpreter actually running this script.
    print(run_command(f'"{sys.executable}" measure_site_size.py site').stdout)

    print("📋 Step 11: Start Python HTTP server")
    print("")

    # Change to site directory and start server
    os.chdir("site")

    # Try different ports if the default is busy
    PORT = 8020
    Handler = http.server.SimpleHTTPRequestHandler

    for port in range(8020, 8100):
        try:
            with socketserver.TCPServer(("", port), Handler) as httpd:
                print(f"🌐 Server started on http://localhost:{port}")
                print("")
                print("You can now test:")
                print(f"  • Root site: http://localhost:{port}/")
                print(f"  • Platform: http://localhost:{port}/platform/")
                print(f"  • Platform Developer Guide: http://localhost:{port}/platform/developer-guide/")
                print(f"  • Versioned content: http://localhost:{port}/platform/developer-guide/1.0/")
                print(f"  • Latest version: http://localhost:{port}/platform/developer-guide/latest/")
                print("")
                print("Press Ctrl+C to stop the server")
                print("")

                httpd.serve_forever()
                break
        except OSError as e:
            if e.errno == 48:  # Address already in use
                print(f"⚠️  Port {port} is busy, trying {port + 1}...")
                continue
            else:
                raise
        except KeyboardInterrupt:
            print("\n\n✅ Server stopped")
            sys.exit(0)

if __name__ == "__main__":
    main()
