#!/usr/bin/env python3
"""
CI/CD versioned build script for GitHub Actions
Based on versioned-build.py but optimized for CI/CD environment
"""

import os
import sys
import subprocess
import shutil
import argparse
import json

def run_command(cmd, check=True, cwd=None):
    """Run shell command and return result"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    if check and result.returncode != 0:
        print(f"❌ Error: {result.stderr}")
        sys.exit(1)
    return result

def main():
    parser = argparse.ArgumentParser(description='CI/CD versioned documentation build')
    parser.add_argument('--version', help='Global version for all subsites')
    parser.add_argument('--marketplace-developer-guide-version', help='Version for marketplace/developer-guide')
    parser.add_argument('--marketplace-user-guide-version', help='Version for marketplace/user-guide')
    parser.add_argument('--platform-developer-guide-version', help='Version for platform/developer-guide')
    parser.add_argument('--platform-user-guide-version', help='Version for platform/user-guide')
    parser.add_argument('--platform-deployment-on-cloud-version', help='Version for platform/deployment-on-cloud')
    parser.add_argument('--storefront-developer-guide-version', help='Version for storefront/developer-guide')
    parser.add_argument('--storefront-user-guide-version', help='Version for storefront/user-guide')
    parser.add_argument('--set-as-latest', action='store_true', help='Set as latest version')
    parser.add_argument('--set-as-default', action='store_true', help='Set as default version')
    parser.add_argument('--output-dir', default='site', help='Output directory for built site')
    parser.add_argument('--no-docker', action='store_true', help='Skip Docker build')

    args = parser.parse_args()

    print("🚀 CI/CD Versioned build of documentation sites...")

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

    print("📋 Step 1: Configure Git for CI/CD")

    # Configure git for CI/CD
    run_command('git config user.name "github-actions[bot]"')
    run_command('git config user.email "github-actions[bot]@users.noreply.github.com"')

    print("✅ Git configured for CI/CD")

    print("📋 Step 2: Build non-versioned sites (root + intermediate)")

    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)

    # Build root site (without subsites)
    run_command("mkdocs build -d " + args.output_dir, check=False)

    # Build intermediate sites (platform, marketplace, storefront)
    print("  Building intermediate sites...")
    run_command(f"mkdocs build -f storefront/mkdocs.yml -d ../{args.output_dir}/storefront", check=False)
    run_command(f"mkdocs build -f platform/mkdocs.yml -d ../{args.output_dir}/platform", check=False)
    run_command(f"mkdocs build -f marketplace/mkdocs.yml -d ../{args.output_dir}/marketplace", check=False)

    print("✅ Non-versioned sites built")

    print("📋 Step 3: Deploy versioned subsites with Mike")

    # Define subsites and their versions
    subsites = {
        "marketplace/developer-guide": args.marketplace_developer_guide_version or args.version,
        "marketplace/user-guide": args.marketplace_user_guide_version or args.version,
        "platform/developer-guide": args.platform_developer_guide_version or args.version,
        "platform/user-guide": args.platform_user_guide_version or args.version,
        "platform/deployment-on-cloud": args.platform_deployment_on_cloud_version or args.version,
        "storefront/developer-guide": args.storefront_developer_guide_version or args.version,
        "storefront/user-guide": args.storefront_user_guide_version or args.version
    }

    # Deploy each subsite
    for subsite, version in subsites.items():
        if not version:
            print(f"  ⚠️  Skipping {subsite} (no version specified)")
            continue

        config = f"{subsite}/mkdocs.yml"
        print(f"  Deploying {subsite} version {version}...")

        # Build mike command
        # Use --force to overwrite existing version content
        mike_cmd = [
            "mike", "deploy", "-F", config, "--deploy-prefix", subsite,
            "--update-aliases", "--force", version
        ]

        # Add latest alias if requested
        if args.set_as_latest:
            mike_cmd.append("latest")

        # Add push flag for CI/CD
        mike_cmd.append("--push")

        # Execute mike deploy
        result = run_command(" ".join(mike_cmd), check=False)
        if result.returncode != 0:
            print(f"❌ Mike deploy failed for {subsite}: {result.stderr}")
            print("This might cause deployment issues!")

        # Set as default if requested
        if args.set_as_default:
            print(f"  Setting {subsite} as default...")
            run_command(f'mike set-default -F "{config}" --deploy-prefix "{subsite}" {version} --push', check=False)

        print(f"  ✅ {subsite} deployed")

    print("✅ Versioned subsites deployed")

    print("📋 Step 4: Export versioned content from gh-pages")

    # Save current branch
    result = run_command("git branch --show-current")
    current_branch = result.stdout.strip()

    try:
        # Stash changes and checkout gh-pages
        print("  Stashing changes and switching to gh-pages branch...")
        run_command("git stash push -m 'temp changes for CI/CD build'", check=False)
        run_command("git checkout gh-pages")

        print("  Copying versioned content...")
        # Copy versioned subsites to output directory
        for subsite in ["marketplace", "platform", "storefront"]:
            for guide in ["developer-guide", "user-guide", "deployment-on-cloud"]:
                src = f"{subsite}/{guide}"
                if os.path.exists(src):
                    dst = f"{args.output_dir}/{subsite}/{guide}"
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
        sys.exit(1)

    print("✅ Versioned content exported")

    print("📋 Step 5: Extract sitemaps from versioned content")

    # Extract sitemap.xml files from versioned content
    versioned_subsites = [
        "marketplace/developer-guide",
        "marketplace/user-guide",
        "platform/developer-guide",
        "platform/user-guide",
        "platform/deployment-on-cloud",
        "storefront/developer-guide",
        "storefront/user-guide"
    ]

    for subsite in versioned_subsites:
        # Look for sitemap in the copied content
        sitemap_path = f"{args.output_dir}/{subsite}/sitemap.xml"
        target_sitemap_path = f"{subsite}/sitemap.xml"

        if os.path.exists(sitemap_path):
            print(f"  Extracting sitemap from {sitemap_path} to {target_sitemap_path}")
            # Ensure target directory exists
            os.makedirs(os.path.dirname(target_sitemap_path), exist_ok=True)
            # Copy sitemap
            shutil.copy2(sitemap_path, target_sitemap_path)
            print(f"  ✅ Sitemap copied to {target_sitemap_path}")
        else:
            print(f"  ⚠️  Sitemap not found at {sitemap_path}")

    print("✅ Sitemaps extracted from versioned content")

    # Cleanup
    if os.path.exists("mkdocs-temp-root.yml"):
        os.remove("mkdocs-temp-root.yml")

    print("✅ CI/CD versioned build completed!")

    # Verify that files were actually created
    print("🔍 Verifying build output...")
    site_dir = args.output_dir
    required_dirs = ["marketplace", "platform", "storefront"]

    missing_dirs = []
    for dir_name in required_dirs:
        if not os.path.exists(os.path.join(site_dir, dir_name)):
            missing_dirs.append(dir_name)

    if missing_dirs:
        print(f"❌ WARNING: Missing directories in build output: {missing_dirs}")
        print("This will likely cause deployment failures!")
    else:
        print("✅ All required directories found in build output")

    # Output build information for GitHub Actions
    build_info = {
        "output_dir": args.output_dir,
        "subsites_deployed": [subsite for subsite, version in subsites.items() if version],
        "versions": {subsite: version for subsite, version in subsites.items() if version},
        "missing_dirs": missing_dirs
    }

    print(f"📊 Build Summary:")
    print(f"  Output directory: {args.output_dir}")
    print(f"  Subsites deployed: {len([s for s in build_info['subsites_deployed']])}")
    for subsite, version in build_info['versions'].items():
        print(f"    {subsite}: {version}")

    if missing_dirs:
        print(f"  ⚠️  Missing directories: {missing_dirs}")

    # Write build info to file for GitHub Actions
    with open("build-info.json", "w") as f:
        json.dump(build_info, f, indent=2)

    print("✅ Build info written to build-info.json")

if __name__ == "__main__":
    main()
