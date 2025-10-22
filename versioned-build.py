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

    # Build root site (without subsites)
    # print("  Building root site...")
    # with open("mkdocs-temp-root.yml", "w") as f:
    #     f.write("INHERIT: mkdocs.yml\n")
    #     f.write("nav:\n")
    #     f.write("    - Home: index.md\n")

    run_command("mkdocs build -d site", check=False)

    # Build intermediate sites (platform, marketplace, storefront)
    print("  Building intermediate sites...")
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

    print("📋 Step 4: Copy versioned content from local gh-pages folder to site")

    print("  Copying versioned content from local gh-pages folder...")
    # Copy versioned subsites to site directory
    # This overwrites the non-versioned subsites with versioned ones
    for subsite in ["marketplace", "platform", "storefront"]:
        for guide in ["developer-guide", "user-guide", "deployment-on-cloud"]:
            # Look for versioned content in gh-pages/{subsite}/{guide}/{version}/
            src = f"gh-pages/{subsite}/{guide}/{version}"
            if os.path.exists(src):
                dst = f"site/{subsite}/{guide}"
                print(f"  Copying {src} to {dst}")
                if os.path.exists(dst):
                    shutil.rmtree(dst)
                shutil.copytree(src, dst, ignore=shutil.ignore_patterns('.git'))
            else:
                print(f"  ⚠️  {src} not found in local gh-pages folder")

    print("✅ Versioned content copied to site")

    print("📋 Step 5: Extract sitemaps from versioned subdirectories")

    # Extract sitemap.xml files from versioned subdirectories and copy to subsites
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
        # Look for sitemap in versioned directory (e.g., site/storefront/developer-guide/1.0/sitemap.xml)
        versioned_sitemap_path = f"site/{subsite}/{version}/sitemap.xml"
        target_sitemap_path = f"{subsite}/sitemap.xml"

        if os.path.exists(versioned_sitemap_path):
            print(f"  Extracting sitemap from {versioned_sitemap_path} to {target_sitemap_path}")
            # Ensure target directory exists
            os.makedirs(os.path.dirname(target_sitemap_path), exist_ok=True)
            # Copy sitemap
            shutil.copy2(versioned_sitemap_path, target_sitemap_path)
            print(f"  ✅ Sitemap copied to {target_sitemap_path}")
        else:
            print(f"  ⚠️  Sitemap not found at {versioned_sitemap_path}")

    print("✅ Sitemaps extracted from versioned subdirectories")

    print("📋 Step 6: Clean up versioned subdirectories from site")

    # Remove versioned subdirectories from site/ (keep only the main subsite directories)
    for subsite in versioned_subsites:
        versioned_dir = f"site/{subsite}/{version}"
        if os.path.exists(versioned_dir):
            print(f"  Removing versioned directory: {versioned_dir}")
            shutil.rmtree(versioned_dir)
            print(f"  ✅ Removed {versioned_dir}")
        else:
            print(f"  ⚠️  Versioned directory not found: {versioned_dir}")

    print("✅ Versioned subdirectories cleaned up")

    # Cleanup
    if os.path.exists("mkdocs-temp-root.yml"):
        os.remove("mkdocs-temp-root.yml")

    print("📋 Step 7: Start Python HTTP server")
    print("")

    # Change to site directory and start server
    os.chdir("site")

    # Try different ports if the default is busy
    PORT = 8020
    Handler = http.server.SimpleHTTPRequestHandler

    for port in range(8020, 8030):
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
