#!/usr/bin/env python3
"""
Quick test script - serve current gh-pages content with Docker
Use this when you already have versioned content deployed
"""

import os
import sys
import subprocess
import shutil

def run_command(cmd, check=True):
    """Run shell command and return result"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"❌ Error: {result.stderr}")
        sys.exit(1)
    return result

def main():
    print("🚀 Quick test of versioned documentation...")

    # Check if we're in the right directory
    if not os.path.exists("mkdocs.yml"):
        print("❌ Please run this script from the vc-docs root directory")
        sys.exit(1)

    # Check if Docker is running
    result = run_command("docker info", check=False)
    if result.returncode != 0:
        print("❌ Docker is not running. Please start Docker first.")
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

    # Build intermediate sites directly into their target directories
    print("  Building intermediate sites...")
    os.makedirs("site/storefront", exist_ok=True)
    os.makedirs("site/platform", exist_ok=True)
    os.makedirs("site/marketplace", exist_ok=True)

    run_command("mkdocs build -f storefront/mkdocs.yml -d site/storefront", check=False)
    run_command("mkdocs build -f platform/mkdocs.yml -d site/platform", check=False)
    run_command("mkdocs build -f marketplace/mkdocs.yml -d site/marketplace", check=False)

    print("✅ Sites built")

    print("📋 Step 2: Export and merge versioned content from gh-pages")

    # Save current branch
    result = run_command("git branch --show-current")
    current_branch = result.stdout.strip()

    try:
        # Checkout gh-pages and copy versioned content over existing files
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

    except Exception as e:
        print(f"❌ Error during export: {e}")
        # Try to return to original branch
        run_command(f"git checkout {current_branch}", check=False)
        sys.exit(1)

    print("✅ Versioned content merged")

    # Cleanup temporary file
    if os.path.exists("mkdocs-temp-root.yml"):
        os.remove("mkdocs-temp-root.yml")

    print("📋 Step 3: Prepare Docker context")

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

    print("📋 Step 4: Build and start server")

    # Build Docker image
    print("  Building Docker image...")
    run_command("docker build -t vc-docs-quick:local .")

    print("✅ Docker image built")
    print("")
    print("🌐 Starting server on http://localhost:8080")
    print("")
    print("You can now test:")
    print("  • Root site: http://localhost:8080/")
    print("  • Platform: http://localhost:8080/platform/")
    print("  • Platform Developer Guide: http://localhost:8080/platform/developer-guide/")
    print("  • Versioned content: http://localhost:8080/platform/developer-guide/1.0/")
    print("")
    print("Press Ctrl+C to stop the server")
    print("")

    # Start Docker container
    try:
        subprocess.run(
            "docker run --rm -p 8080:80 vc-docs-quick:local",
            shell=True,
            check=True
        )
    except KeyboardInterrupt:
        print("\n\n✅ Server stopped")
        sys.exit(0)

if __name__ == "__main__":
    main()

