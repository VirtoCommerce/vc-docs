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

    print("📋 Step 1: Build non-versioned sites (root + intermediate)")

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

    print("📋 Step 3: Copy versioned content from gh-pages to site")

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
        # This overwrites the non-versioned subsites with versioned ones
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

    print("✅ Versioned content copied to site")

    print("📋 Step 4: Fix sitemap.xml URLs for versioning")

    # Fix sitemap.xml to include proper versioning
    sitemap_path = "site/sitemap.xml"
    if os.path.exists(sitemap_path):
        print("  Fixing sitemap.xml URLs...")
        result = run_command(f"python3 fix-sitemap.py {sitemap_path} {version} --use-latest", check=False)
        if result.returncode == 0:
            print("  ✅ Sitemap URLs fixed")
        else:
            print(f"  ⚠️  Warning: Could not fix sitemap: {result.stderr}")
    else:
        print("  ⚠️  Warning: sitemap.xml not found")

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
