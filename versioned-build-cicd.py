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


def cleanup_duplicate_folders(site_dir):
    """
    Remove duplicate flat folders created by monorepo plugin.

    The monorepo plugin creates folders like 'platform-developer-guide' at the root level
    when using !include directives. These duplicate the content already present in
    nested paths like 'platform/developer-guide/', causing the build to be ~2x larger.
    """
    duplicate_folders = [
        "platform-developer-guide",
        "platform-user-guide",
        "platform-deployment-on-cloud",
        "marketplace-developer-guide",
        "marketplace-user-guide",
        "storefront-developer-guide",
        "storefront-user-guide",
    ]

    removed_count = 0
    freed_bytes = 0

    for folder in duplicate_folders:
        path = os.path.join(site_dir, folder)
        if os.path.exists(path):
            # Calculate size before removal
            folder_size = get_folder_size(path)
            freed_bytes += folder_size

            shutil.rmtree(path)
            removed_count += 1
            print(f"    Removed {folder}/ ({format_size(folder_size)})")

    return removed_count, freed_bytes


def deduplicate_assets(site_dir):
    """
    Replace duplicate MkDocs theme assets folders with symlinks to the root assets.

    MkDocs Material theme copies ~11MB of assets (CSS, JS, fonts, icons) into each
    subsite build. With 10+ subsites, this adds ~100MB+ of duplicate content.
    This function replaces all nested assets/ folders with symlinks to the root assets/.
    """
    root_assets = os.path.join(site_dir, "assets")

    if not os.path.exists(root_assets):
        print("    ⚠️  Root assets folder not found, skipping deduplication")
        return 0, 0

    replaced_count = 0
    freed_bytes = 0

    for root, dirs, _ in os.walk(site_dir, topdown=True):
        if "assets" in dirs and root != site_dir:
            assets_path = os.path.join(root, "assets")

            # Skip if already a symlink
            if os.path.islink(assets_path):
                continue

            # Calculate size before removal
            folder_size = get_folder_size(assets_path)
            freed_bytes += folder_size

            # Calculate relative path from current directory to root assets
            rel_path = os.path.relpath(root_assets, root)

            # Remove the duplicate folder and create symlink
            shutil.rmtree(assets_path)
            os.symlink(rel_path, assets_path)

            replaced_count += 1
            # Print relative path from site_dir for cleaner output
            rel_assets = os.path.relpath(assets_path, site_dir)
            print(f"    Symlinked {rel_assets}/ -> {rel_path}")

    return replaced_count, freed_bytes


def get_folder_size(path):
    """Calculate total size of a folder in bytes."""
    total = 0
    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            # Skip symbolic links
            if not os.path.islink(filepath):
                total += os.path.getsize(filepath)
    return total


def format_size(size_bytes):
    """Format bytes as human-readable size."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} TB"

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
        mike_cmd = [
            "mike", "deploy", "-F", config, "--deploy-prefix", subsite,
            "--update-aliases", version
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

        print("  Copying versioned content (all versions)...")
        # Copy all versioned content from gh-pages
        for subsite in ["marketplace", "platform", "storefront"]:
            for guide in ["developer-guide", "user-guide", "deployment-on-cloud"]:
                src_base = f"{subsite}/{guide}"
                dst_base = f"{args.output_dir}/{subsite}/{guide}"

                if not os.path.exists(src_base):
                    print(f"  ⚠️  {src_base} not found in gh-pages")
                    continue

                # Copy entire versioned subsite (includes all versions: 1.0, 2.0, latest, etc.)
                print(f"    Copying {src_base}/ -> {dst_base}/")
                if os.path.exists(dst_base):
                    shutil.rmtree(dst_base)
                shutil.copytree(src_base, dst_base, ignore=shutil.ignore_patterns('.git'))

                print(f"  ✅ {src_base}")

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

    # Cleanup temp files
    if os.path.exists("mkdocs-temp-root.yml"):
        os.remove("mkdocs-temp-root.yml")

    print("📋 Step 6: Optimize build size (remove duplicates)")

    # Remove duplicate folders created by monorepo plugin
    print("  Removing duplicate folders from monorepo plugin...")
    folders_removed, folders_freed = cleanup_duplicate_folders(args.output_dir)
    print(f"  ✅ Removed {folders_removed} duplicate folders ({format_size(folders_freed)} freed)")

    # Replace duplicate assets with symlinks
    print("  Deduplicating assets folders...")
    assets_replaced, assets_freed = deduplicate_assets(args.output_dir)
    print(f"  ✅ Replaced {assets_replaced} assets folders with symlinks ({format_size(assets_freed)} freed)")

    total_freed = folders_freed + assets_freed
    print(f"✅ Build optimized! Total space saved: {format_size(total_freed)}")

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
