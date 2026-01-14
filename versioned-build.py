#!/usr/bin/env python3
"""
Versioned build script - combines non-versioned sites with versioned content
This is the proper way to build a complete site with versioning
"""

import os
import sys
import subprocess
import shutil
import http.server
import socketserver
import json

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

def merge_search_indexes(output_dir):
    """Merge search indexes from all versioned subsites into a global index"""
    subsites = [
        "platform/developer-guide",
        "platform/user-guide",
        "platform/deployment-on-cloud",
        "marketplace/developer-guide",
        "marketplace/user-guide",
        "storefront/developer-guide",
        "storefront/user-guide"
    ]

    merged_docs = []
    config = {"lang": ["en"], "separator": "[\\s\\-]+", "pipeline": ["stopWordFilter"]}

    for subsite in subsites:
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
    version = "1.0"

    for subsite in subsites:
        config = f"{subsite}/mkdocs.yml"
        print(f"  Deploying {subsite} version {version}...")

        # Deploy with version 1.0 and set as latest
        run_command(
            f'mike deploy -F "{config}" --deploy-prefix "{subsite}" --update-aliases "{version}" latest',
            check=False
        )

        # Set as default version
        run_command(
            f'mike set-default -F "{config}" --deploy-prefix "{subsite}" {version}',
            check=False
        )

        print(f"  ✅ {subsite} deployed")

    print("✅ Versioned subsites deployed")

    print("📋 Step 4: Update local gh-pages folder with latest deployed content")

    # Update local gh-pages folder to get the latest deployed content
    print("  Updating local gh-pages folder with latest deployed content...")
    try:
        run_command("cd gh-pages && git fetch origin gh-pages", check=False)
        run_command("cd gh-pages && git reset --hard origin/gh-pages", check=False)
        print("  ✅ Local gh-pages folder updated with latest content")
    except Exception as e:
        print(f"  ⚠️  Warning: Could not update gh-pages folder: {e}")

    print("📋 Step 5: Copy versioned content from local gh-pages folder to site")

    print("  Copying versioned content from local gh-pages folder...")
    # Copy versioned subsites to site directory
    # This overwrites the non-versioned subsites with versioned ones
    for subsite in ["marketplace", "platform", "storefront"]:
        for guide in ["developer-guide", "user-guide", "deployment-on-cloud"]:
            # Look for versioned content in gh-pages/{subsite}/{guide}/
            src = f"gh-pages/{subsite}/{guide}"
            if os.path.exists(src):
                dst = f"site/{subsite}/{guide}"
                print(f"  Copying {src} to {dst}")
                if os.path.exists(dst):
                    shutil.rmtree(dst)
                shutil.copytree(src, dst, ignore=shutil.ignore_patterns('.git'))
                print(f"  ✅ Copied {src} to {dst}")
            else:
                print(f"  ⚠️  {src} not found in local gh-pages folder")
                # Try to find what's actually there
                guide_path = f"gh-pages/{subsite}/{guide}"
                if os.path.exists(guide_path):
                    print(f"  📁 Found {guide_path}, contents:")
                    try:
                        contents = os.listdir(guide_path)
                        for item in contents:
                            item_path = os.path.join(guide_path, item)
                            if os.path.isdir(item_path):
                                print(f"    📁 {item}/")
                            else:
                                print(f"    📄 {item}")
                    except Exception as e:
                        print(f"    ❌ Error listing contents: {e}")
                else:
                    print(f"  ❌ {guide_path} not found")

    print("✅ Versioned content copied to site")

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

    # Cleanup
    if os.path.exists("mkdocs-temp-root.yml"):
        os.remove("mkdocs-temp-root.yml")

    print("📋 Step 8: Start Python HTTP server")
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
