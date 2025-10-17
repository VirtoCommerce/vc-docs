#!/usr/bin/env python3
"""
Simple build script - build all sites separately and copy to common directory
No Mike, no versioning complexity - just like it worked before
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
    print("🚀 Simple build of all documentation sites...")

    # Check if we're in the right directory
    if not os.path.exists("mkdocs.yml"):
        print("❌ Please run this script from the vc-docs root directory")
        sys.exit(1)

    print("📋 Step 1: Build all sites separately")

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

    # Build all subsites
    print("  Building subsites...")
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

    # Cleanup
    if os.path.exists("mkdocs-temp-root.yml"):
        os.remove("mkdocs-temp-root.yml")

    print("📋 Step 2: Start Python HTTP server")
    print("")
    print("🌐 Starting server on http://localhost:8010")
    print("")
    print("You can now test:")
    print("  • Root site: http://localhost:8010/")
    print("  • Platform: http://localhost:8010/platform/")
    print("  • Platform Developer Guide: http://localhost:8010/platform/developer-guide/")
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
