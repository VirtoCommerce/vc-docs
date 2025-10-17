#!/usr/bin/env python3
"""
Simple Mike Test - Copy versioned content from gh-pages and serve locally
"""

import os
import sys
import subprocess
import shutil
import http.server
import socketserver

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
    print("🚀 Simple Mike Test - Copy versioned content and serve locally")
    print("")
    
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
    
    print("📋 Step 2: Copy versioned content from gh-pages")
    
    # Save current branch
    result = run_command("git branch --show-current")
    current_branch = result.stdout.strip()
    
    try:
        # Stash any uncommitted changes
        run_command("git stash", check=False)
        
        # Switch to gh-pages branch
        run_command("git checkout gh-pages", check=False)
        
        print("  Copying versioned subsites...")
        # Copy versioned subsites to site directory
        for subsite in ["marketplace", "platform", "storefront"]:
            for guide in ["developer-guide", "user-guide", "deployment-on-cloud"]:
                src = f"{subsite}/{guide}"
                if os.path.exists(src):
                    dst = f"site/{subsite}/{guide}"
                    print(f"    Copying {src} to {dst}")
                    if os.path.exists(dst):
                        shutil.rmtree(dst)
                    shutil.copytree(src, dst, ignore=shutil.ignore_patterns('.git'))
                else:
                    print(f"    ⚠️  {src} not found in gh-pages")
        
        # Return to original branch and restore changes
        print(f"  Returning to {current_branch} branch...")
        run_command(f"git checkout {current_branch}")
        run_command("git stash pop", check=False)
        
    except Exception as e:
        print(f"❌ Error during versioned content copy: {e}")
        # Try to return to original branch
        run_command(f"git checkout {current_branch}", check=False)
    
    print("✅ Versioned content copied to site")
    
    print("📋 Step 3: Start HTTP server")
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
                print(f"  • Platform Developer Guide (should redirect): http://localhost:{port}/platform/developer-guide/")
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
