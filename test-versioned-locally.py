#!/usr/bin/env python3
"""
Test versioned documentation locally
This script emulates the CI process locally
"""

import os
import sys
import subprocess
import shutil
import tempfile

def run_command(cmd, check=True, capture=True):
    """Run shell command and return result"""
    if capture:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if check and result.returncode != 0:
            print(f"❌ Error: {result.stderr}")
            sys.exit(1)
        return result
    else:
        result = subprocess.run(cmd, shell=True, check=check)
        return result

def cleanup():
    """Cleanup temporary files"""
    print("📋 Cleaning up...")

    if os.path.exists("mkdocs-temp-root.yml"):
        os.remove("mkdocs-temp-root.yml")

    print("✅ Cleanup completed")

def main():
    print("🚀 Testing versioned documentation locally...")
    print("")

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

    # Check if Docker is running
    result = run_command("docker info", check=False)
    if result.returncode != 0:
        print("❌ Docker is not running. Please start Docker first.")
        sys.exit(1)

    try:
        print("📋 Step 1: Deploy versioned subsites with Mike")
        print("This will deploy version 1.0 for all subsites...")

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

        for subsite in subsites:
            print(f"  Deploying {subsite}...")
            config = f"{subsite}/mkdocs.yml"

            # Deploy with version 1.0 and set as latest
            run_command(
                f'mike deploy -F "{config}" --deploy-prefix "{subsite}" --update-aliases 1.0 latest',
                capture=False
            )

            # Set as default version
            run_command(
                f'mike set-default -F "{config}" --deploy-prefix "{subsite}" 1.0',
                capture=False
            )

            print(f"  ✅ {subsite} deployed")

        print("📋 Step 2: Build non-versioned root and intermediate sites")

        # Create site directory
        os.makedirs("site", exist_ok=True)

        # Create temporary mkdocs.yml for root without subsites
        with open("mkdocs-temp-root.yml", "w") as f:
            f.write("INHERIT: mkdocs.yml\n")
            f.write("nav:\n")
            f.write("    - Home: index.md\n")

        # Build root site without subsites
        print("  Building root site...")
        run_command("mkdocs build -f mkdocs-temp-root.yml -d site", capture=False)

        # Create intermediate site directories and index pages
        print("  Creating intermediate site directories...")
        os.makedirs("site/storefront", exist_ok=True)
        os.makedirs("site/platform", exist_ok=True)
        os.makedirs("site/marketplace", exist_ok=True)

        # Create simple index.html for intermediate sites
        # These will be landing pages that redirect to versioned subsites
        for subsite in ["storefront", "platform", "marketplace"]:
            index_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{subsite.title()} Documentation</title>
    <meta http-equiv="refresh" content="0; url=./developer-guide/">
</head>
<body>
    <p>Redirecting to <a href="./developer-guide/">developer-guide</a>...</p>
</body>
</html>"""
            with open(f"site/{subsite}/index.html", "w") as f:
                f.write(index_content)

        print("✅ Sites built")

        print("📋 Step 3: Export and merge versioned content from gh-pages")

        # Save current branch
        result = run_command("git branch --show-current")
        current_branch = result.stdout.strip()

        # Checkout gh-pages and copy versioned content
        print("  Switching to gh-pages branch...")
        run_command("git checkout gh-pages")

        print("  Copying versioned content (overwriting intermediate sites)...")
        # Copy versioned subsites, overwriting intermediate site content
        # This preserves versioned content while keeping intermediate index pages
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

        print("✅ Versioned content exported and merged")

        print("📋 Step 4: Prepare Docker context")

        # Copy site directory for Docker
        if os.path.exists("vc-docs/site"):
            shutil.rmtree("vc-docs/site")
        shutil.copytree("site", "vc-docs/site")

        # Copy Docker files
        docker_src = "../vc-github-actions/update-virtocommerce-docs-versioned/docker"
        if os.path.exists(docker_src):
            for item in os.listdir(docker_src):
                src = os.path.join(docker_src, item)
                dst = item
                if os.path.isfile(src):
                    shutil.copy2(src, dst)
        else:
            print(f"⚠️  Warning: Docker files not found at {docker_src}")

        print("✅ Docker context prepared")

        print("📋 Step 5: Build Docker image")
        run_command("docker build -t vc-docs-versioned:local .", capture=False)

        print("✅ Docker image built")

        print("📋 Step 6: Start local server")
        print("")
        print("🌐 Starting local server on http://localhost:8080")
        print("")
        print("You can now test:")
        print("  • Root site: http://localhost:8080/")
        print("  • Platform: http://localhost:8080/platform/")
        print("  • Platform Developer Guide: http://localhost:8080/platform/developer-guide/")
        print("  • Versioned content: http://localhost:8080/platform/developer-guide/1.0/")
        print("")
        print("Press Ctrl+C to stop the server")
        print("")

        # Start the container
        try:
            subprocess.run(
                "docker run --rm -p 8080:80 vc-docs-versioned:local",
                shell=True,
                check=True
            )
        except KeyboardInterrupt:
            print("\n\n✅ Server stopped")

    finally:
        cleanup()

if __name__ == "__main__":
    main()

