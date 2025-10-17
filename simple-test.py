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

    print("📋 Step 3: Start Python HTTP server")
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

