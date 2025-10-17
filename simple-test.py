#!/usr/bin/env python3
"""
Simple test - serve gh-pages content with Python HTTP server
No Docker required
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
    print("🚀 Simple test of versioned documentation...")

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

    print("📋 Step 1: Build non-versioned root and intermediate sites")

    # Create site directory
    os.makedirs("site", exist_ok=True)

    # Create temporary mkdocs.yml for root without subsites
    print("  Creating temporary root config...")
    with open("mkdocs-temp-root.yml", "w") as f:
        f.write("INHERIT: mkdocs.yml\n")
        f.write("nav:\n")
        f.write("    - Home: index.md\n")

    # Build root site without subsites
    print("  Building root site...")
    run_command("mkdocs build -f mkdocs-temp-root.yml -d site", check=False)

    # Build intermediate sites with their real content and templates
    print("  Building intermediate sites...")
    os.makedirs("site/storefront", exist_ok=True)
    os.makedirs("site/platform", exist_ok=True)
    os.makedirs("site/marketplace", exist_ok=True)

    # Create temporary configs for intermediate sites with only Home: index.md
    # This prevents them from including all subsites
    for subsite in ["storefront", "platform", "marketplace"]:
        print(f"  Creating temporary config for {subsite}...")

        # Read original mkdocs.yml
        with open(f"{subsite}/mkdocs.yml", "r") as f:
            content = f.read()

        # Create temporary config with only Home: index.md
        temp_content = f"""INHERIT: ../mkdocs.yml
theme:
    custom_dir: ../overrides

docs_dir: docs

# Project information
extra_site_name: Documentation
site_name: {subsite}
site_description: {subsite.title()} documentation center
site_author: Virto Commerce
site_url: https://docs.virtocommerce.org/{subsite}

# Repository
repo_name: VirtoCommerce/vc-{subsite}
repo_url: https://github.com/VirtoCommerce/vc-{subsite}
edit_uri: edit/dev/docs/

nav:
    - Home: index.md
"""

        # Write temporary config
        with open(f"mkdocs-temp-{subsite}.yml", "w") as f:
            f.write(temp_content)

    # Build each intermediate site with temporary configs
    run_command("mkdocs build -f mkdocs-temp-storefront.yml -d site/storefront", check=False)
    run_command("mkdocs build -f mkdocs-temp-platform.yml -d site/platform", check=False)
    run_command("mkdocs build -f mkdocs-temp-marketplace.yml -d site/marketplace", check=False)

    print("✅ Sites built")

    print("📋 Step 2: Deploy versioned subsites with Mike")

    # Deploy all subsites with version 1.0 using Mike
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

    print("✅ Versioned content deployed with Mike")

    print("📋 Step 3: Copy versioned content from gh-pages to site")

    # Save current branch
    result = run_command("git branch --show-current")
    current_branch = result.stdout.strip()

    try:
        # Checkout gh-pages and copy versioned content
        print("  Switching to gh-pages branch...")
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

        # Return to original branch
        print(f"  Returning to {current_branch} branch...")
        run_command(f"git checkout {current_branch}")

    except Exception as e:
        print(f"❌ Error during export: {e}")
        # Try to return to original branch
        run_command(f"git checkout {current_branch}", check=False)
        sys.exit(1)

    print("✅ Versioned content copied to site")

    # Cleanup temporary files
    for temp_file in ["mkdocs-temp-root.yml", "mkdocs-temp-storefront.yml", "mkdocs-temp-platform.yml", "mkdocs-temp-marketplace.yml"]:
        if os.path.exists(temp_file):
            os.remove(temp_file)

    print("📋 Step 4: Start Python HTTP server")
    print("")
    print("🌐 Starting server on http://localhost:8001")
    print("")
    print("You can now test:")
    print("  • Root site: http://localhost:8001/")
    print("  • Platform: http://localhost:8001/platform/")
    print("  • Platform Developer Guide: http://localhost:8001/platform/developer-guide/")
    print("  • Versioned content: http://localhost:8001/platform/developer-guide/1.0/")
    print("")
    print("Press Ctrl+C to stop the server")
    print("")

    # Change to site directory and start server
    os.chdir("site")

    PORT = 8001
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n✅ Server stopped")
            sys.exit(0)

if __name__ == "__main__":
    main()

