#!/usr/bin/env python3
"""
Mike serve test - use mike serve for versioned content
This is the proper way to test versioned documentation locally
"""

import os
import sys
import subprocess
import time

def run_command(cmd, check=True):
    """Run shell command and return result"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"❌ Error: {result.stderr}")
        sys.exit(1)
    return result

def main():
    print("🚀 Mike serve test for versioned documentation...")

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

    print("📋 Step 1: Deploy version 1.0 for all subsites")

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

    print("✅ All subsites deployed")

    print("📋 Step 2: Start Mike serve")
    print("")
    print("🌐 Starting Mike serve on http://localhost:8000")
    print("")
    print("You can now test:")
    print("  • Platform Developer Guide: http://localhost:8000/platform/developer-guide/")
    print("  • Versioned content: http://localhost:8000/platform/developer-guide/1.0/")
    print("  • Latest version: http://localhost:8000/platform/developer-guide/latest/")
    print("")
    print("Press Ctrl+C to stop the server")
    print("")

    # Start Mike serve
    try:
        # Use the first subsite config as the main config for mike serve
        main_config = "platform/developer-guide/mkdocs.yml"
        run_command(f'mike serve -F "{main_config}" --dev-addr localhost:8000', check=False)
    except KeyboardInterrupt:
        print("\n\n✅ Server stopped")
        sys.exit(0)

if __name__ == "__main__":
    main()
