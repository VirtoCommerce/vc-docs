#!/usr/bin/env python3
"""
Mike Serve Versioned Documentation
Uses mike serve to serve versioned documentation with proper aliases and redirects
"""

import os
import sys
import subprocess
import tempfile
import shutil
from pathlib import Path

def run_command(command, check=True):
    """Run a command and return the result"""
    print(f"  Running: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"❌ Command failed: {command}")
        print(f"Error: {result.stderr}")
        sys.exit(1)
    return result

def main():
    print("🚀 Starting Mike Serve for versioned documentation...")
    print("")

    # Check if we're in the right directory
    if not os.path.exists("mkdocs.yml"):
        print("❌ Error: mkdocs.yml not found. Please run from the vc-docs root directory.")
        sys.exit(1)

    # Check if mike is installed
    result = run_command("mike --version", check=False)
    if result.returncode != 0:
        print("❌ Error: Mike is not installed. Please install it with: pip install mike")
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

    print("📋 Step 3: Create aliases for unversioned paths")

    # Create aliases for unversioned paths to redirect to latest versions
    for subsite in subsites:
        config = f"{subsite}/mkdocs.yml"
        print(f"  Creating aliases for {subsite}...")

        # Create alias for developer-guide path (if it exists)
        if "developer-guide" in subsite:
            run_command(
                f'mike alias -F "{config}" --deploy-prefix "{subsite}" latest developer-guide',
                check=False
            )

        # Create alias for user-guide path (if it exists)
        if "user-guide" in subsite:
            run_command(
                f'mike alias -F "{config}" --deploy-prefix "{subsite}" latest user-guide',
                check=False
            )

        # Create alias for deployment-on-cloud path (if it exists)
        if "deployment-on-cloud" in subsite:
            run_command(
                f'mike alias -F "{config}" --deploy-prefix "{subsite}" latest deployment-on-cloud',
                check=False
            )

    print("✅ Aliases for unversioned paths created")

    print("📋 Step 4: Copy non-versioned content to gh-pages")

    # Save current branch
    result = run_command("git branch --show-current")
    current_branch = result.stdout.strip()

    try:
        # Stash any uncommitted changes
        run_command("git stash", check=False)

        # Switch to gh-pages branch
        run_command("git checkout gh-pages", check=False)

        # Copy non-versioned content to gh-pages
        print("  Copying non-versioned content...")

        # Copy root site files
        if os.path.exists("site/index.html"):
            shutil.copy2("site/index.html", "index.html")

        # Copy intermediate site files
        for site in intermediate_sites:
            if os.path.exists(f"site/{site}"):
                if os.path.exists(site):
                    shutil.rmtree(site)
                shutil.copytree(f"site/{site}", site)

        # Commit changes
        run_command("git add .", check=False)
        run_command("git commit -m 'Add non-versioned content for local testing'", check=False)

        print("✅ Non-versioned content copied to gh-pages")

    except Exception as e:
        print(f"❌ Error during content copy: {e}")
        # Try to return to original branch
        run_command(f"git checkout {current_branch}", check=False)

    print("📋 Step 5: Start Mike serve")
    print("")

    # Start mike serve
    print("🌐 Starting Mike serve...")
    print("")
    print("You can now test:")
    print("  • Root site: http://localhost:8000/")
    print("  • Platform: http://localhost:8000/platform/")
    print("  • Platform Developer Guide (redirects to latest): http://localhost:8000/platform/developer-guide/")
    print("  • Versioned content: http://localhost:8000/platform/developer-guide/1.0/")
    print("  • Latest version: http://localhost:8000/platform/developer-guide/latest/")
    print("")
    print("Press Ctrl+C to stop the server")
    print("")

    try:
        # Use mike serve to serve the documentation
        run_command("mike serve --dev-addr 0.0.0.0:8000")
    except KeyboardInterrupt:
        print("\n\n✅ Server stopped")
        # Return to original branch
        run_command(f"git checkout {current_branch}", check=False)
        run_command("git stash pop", check=False)
        sys.exit(0)

if __name__ == "__main__":
    main()
