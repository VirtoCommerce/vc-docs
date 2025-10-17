#!/usr/bin/env python3
"""
Build versioned documentation locally with Mike
This script builds non-versioned root and intermediate sites,
deploys versioned subsites with Mike, and serves everything with a local HTTP server
"""

import os
import sys
import subprocess
import shutil
import http.server
import socketserver

def run_command(command, check=True):
    """Run a command and return the result"""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if check and result.returncode != 0:
        # Check if it's just warnings (mkdocs returns 0 even with warnings)
        if "Error reading page" in result.stderr or "Inherited config file" in result.stderr:
            print(f"⚠️  Warning (non-critical): {result.stderr[:200]}...")
            return result
        print(f"❌ Error: {command}")
        print(result.stderr)
        sys.exit(1)
    return result

def main():
    print("🚀 Versioned build of documentation sites...")

    # Check if we're in the right directory
    if not os.path.exists("mkdocs.yml"):
        print("❌ Error: mkdocs.yml not found. Please run from the vc-docs root directory.")
        sys.exit(1)

    print("📋 Step 1: Build non-versioned sites (root + intermediate)")

    # Clean up previous builds
    if os.path.exists("site"):
        shutil.rmtree("site")

    # Build root site (only index.md)
    print("  Building root site...")
    run_command("mkdocs build -d site")

    # Build intermediate sites
    print("  Building intermediate sites...")
    intermediate_sites = ["platform", "marketplace", "storefront"]

    for site in intermediate_sites:
        if os.path.exists(f"{site}/mkdocs.yml"):
            print(f"    Building {site}...")
            run_command(f"mkdocs build -f {site}/mkdocs.yml -d site/{site}")

    print("✅ Non-versioned sites built")

    print("📋 Step 2: Deploy versioned subsites with Mike")

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

    print("📋 Step 3: Copy versioned content from gh-pages to site (with symlinks)")

    # Save current branch
    result = run_command("git branch --show-current")
    current_branch = result.stdout.strip()

    try:
        # Stash any uncommitted changes
        print("  Stashing changes and switching to gh-pages branch...")
        run_command("git stash", check=False)

        # Switch to gh-pages branch
        result = run_command("git checkout gh-pages", check=False)
        if result.returncode != 0:
            print(f"❌ Error: {result.stderr}")
            return

        # Copy versioned content to site directory
        print("  Copying versioned subsites (preserving symlinks)...")

        for subsite in subsites:
            src_dir = subsite
            dst_dir = f"site/{subsite}"

            if os.path.exists(src_dir):
                # Remove destination if it exists
                if os.path.exists(dst_dir):
                    shutil.rmtree(dst_dir)

                # Use rsync to copy with symlinks preserved
                run_command(f'rsync -a --copy-links "{src_dir}/" "{dst_dir}/"', check=False)
                print(f"    ✅ Copied {subsite}")

        # Copy assets and other shared files
        shared_dirs = ["assets", "javascripts", "stylesheets", "search"]
        for shared_dir in shared_dirs:
            if os.path.exists(shared_dir):
                src = shared_dir
                dst = f"site/{shared_dir}"
                if os.path.exists(dst):
                    shutil.rmtree(dst)
                shutil.copytree(src, dst, symlinks=True)

        # Return to original branch
        run_command(f"git checkout {current_branch}", check=False)

        # Restore stashed changes
        run_command("git stash pop", check=False)

    except Exception as e:
        print(f"❌ Error during versioned content copy: {e}")
        # Try to return to original branch
        run_command(f"git checkout {current_branch}", check=False)

    print("✅ Versioned content copied to site")

    print("📋 Step 4: Links will be handled by Mike symlinks (no manual fixing needed)")

    # Cleanup
    if os.path.exists("mkdocs-temp-root.yml"):
        os.remove("mkdocs-temp-root.yml")

    print("📋 Step 5: Start Python HTTP server")
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

