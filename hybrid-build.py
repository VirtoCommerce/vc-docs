#!/usr/bin/env python3
"""
Hybrid build script - build all sites separately + copy versioned content
This combines the simplicity of separate builds with versioning support
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
    print("🚀 Hybrid build of documentation sites...")

    # Check if we're in the right directory
    if not os.path.exists("mkdocs.yml"):
        print("❌ Please run this script from the vc-docs root directory")
        sys.exit(1)

    print("📋 Step 1: Build all sites separately (like before)")

    # Create site directory
    os.makedirs("site", exist_ok=True)

    # Build root site (without subsites)
    print("  Building root site...")
    with open("mkdocs-temp-root.yml", "w") as f:
        f.write("INHERIT: mkdocs.yml\n")
        f.write("nav:\n")
        f.write("    - Home: index.md\n")

    run_command("mkdocs build -f mkdocs-temp-root.yml -d site", check=False)

    # Build intermediate sites (platform, marketplace, storefront)
    print("  Building intermediate sites...")
    run_command("mkdocs build -f platform/mkdocs.yml -d site/platform", check=False)
    run_command("mkdocs build -f marketplace/mkdocs.yml -d site/marketplace", check=False)
    run_command("mkdocs build -f storefront/mkdocs.yml -d site/storefront", check=False)

    # Build all subsites (non-versioned)
    print("  Building subsites (non-versioned)...")
    subsites = [
        "platform/developer-guide",
        "platform/user-guide",
        "platform/deployment-on-cloud",
        "marketplace/developer-guide",
        "marketplace/user-guide",
        "storefront/developer-guide",
        "storefront/user-guide"
    ]

    for subsite in subsites:
        print(f"    Building {subsite}...")
        run_command(f"mkdocs build -f {subsite}/mkdocs.yml -d site/{subsite}", check=False)

    print("✅ All sites built")

    print("📋 Step 2: Deploy versioned content with Mike")

    # Check if mike is installed
    result = run_command("mike --version", check=False)
    if result.returncode != 0:
        print("⚠️  Mike not installed - skipping versioned deployment")
        print("   Install with: pip install mike")
    else:
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

        print("📋 Step 3: Copy versioned content from gh-pages")

        # Save current branch
        result = run_command("git branch --show-current")
        current_branch = result.stdout.strip()

        try:
            # Stash changes and checkout gh-pages
            print("  Stashing changes and switching to gh-pages branch...")
            run_command("git stash push -m 'temp changes for testing'", check=False)
            run_command("git checkout gh-pages")

            print("  Copying versioned content...")
            # Copy versioned subsites to site directory
            for subsite in ["marketplace", "platform", "storefront"]:
                for guide in ["developer-guide", "user-guide", "deployment-on-cloud"]:
                    src = f"{subsite}/{guide}"
                    if os.path.exists(src):
                        dst = f"site/{subsite}/{guide}"
                        print(f"  Copying {src} to {dst}")
                        if os.path.exists(dst):
                            shutil.rmtree(dst)
                        shutil.copytree(src, dst, ignore=shutil.ignore_patterns('.git'))
                    else:
                        print(f"  ⚠️  {src} not found in gh-pages")

            # Return to original branch and restore changes
            print(f"  Returning to {current_branch} branch...")
            run_command(f"git checkout {current_branch}")
            run_command("git stash pop", check=False)

        except Exception as e:
            print(f"❌ Error during versioned content copy: {e}")
            # Try to return to original branch
            run_command(f"git checkout {current_branch}", check=False)

        print("✅ Versioned content copied")

    # Cleanup
    if os.path.exists("mkdocs-temp-root.yml"):
        os.remove("mkdocs-temp-root.yml")

    print("📋 Step 4: Start Python HTTP server")
    print("")
    print("🌐 Starting server on http://localhost:8010")
    print("")
    print("You can now test:")
    print("  • Root site: http://localhost:8010/")
    print("  • Platform: http://localhost:8010/platform/")
    print("  • Platform Developer Guide: http://localhost:8010/platform/developer-guide/")
    if result.returncode == 0:
        print("  • Versioned content: http://localhost:8010/platform/developer-guide/1.0/")
        print("  • Latest version: http://localhost:8010/platform/developer-guide/latest/")
    print("")
    print("Press Ctrl+C to stop the server")
    print("")

    # Change to site directory and start server
    os.chdir("site")

    PORT = 8010
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n✅ Server stopped")
            sys.exit(0)

if __name__ == "__main__":
    main()
