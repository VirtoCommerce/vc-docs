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
import tempfile

SITE_URL = "https://docs.virtocommerce.org"

VERSIONED_SUBSITES = [
    "platform/developer-guide",
    "platform/user-guide",
    "platform/deployment-on-cloud",
    "marketplace/developer-guide",
    "marketplace/user-guide",
    "storefront/developer-guide",
    "storefront/user-guide"
]

def get_latest_version(output_dir, subsite):
    """Get the actual version number that has 'latest' alias from versions.json"""
    versions_path = os.path.join(output_dir, subsite, "versions.json")
    if os.path.exists(versions_path):
        with open(versions_path) as f:
            versions = json.load(f)
        for v in versions:
            if "latest" in v.get("aliases", []):
                return v["version"]
        # If no 'latest' alias found, return first version
        if versions:
            return versions[0]["version"]
    return None


def generate_sitemap_index(output_dir):
    """Generate sitemap_index.xml referencing all subsite sitemaps for the latest version"""
    sitemap_entries = []

    # Add root sitemap
    root_sitemap = os.path.join(output_dir, "sitemap.xml")
    if os.path.exists(root_sitemap):
        sitemap_entries.append(f"{SITE_URL}/sitemap.xml")

    # Add subsite sitemaps for latest version
    for subsite in VERSIONED_SUBSITES:
        actual_version = get_latest_version(output_dir, subsite)
        if not actual_version:
            print(f"    ⚠️  No version found for {subsite}, skipping sitemap")
            continue

        sitemap_path = os.path.join(output_dir, subsite, actual_version, "sitemap.xml")
        if os.path.exists(sitemap_path):
            sitemap_entries.append(f"{SITE_URL}/{subsite}/{actual_version}/sitemap.xml")
            print(f"    Added sitemap for {subsite} (v{actual_version})")
        else:
            print(f"    ⚠️  Sitemap not found: {sitemap_path}")

    # Write sitemap index
    xml_entries = "\n".join(
        f"    <sitemap>\n        <loc>{url}</loc>\n    </sitemap>"
        for url in sitemap_entries
    )
    sitemap_index_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{xml_entries}
</sitemapindex>
"""
    sitemap_index_path = os.path.join(output_dir, "sitemap_index.xml")
    with open(sitemap_index_path, "w") as f:
        f.write(sitemap_index_xml)

    print(f"    ✅ Generated sitemap_index.xml with {len(sitemap_entries)} sitemaps")


def generate_robots_txt(output_dir):
    """Generate robots.txt with sitemap reference"""
    robots_content = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap_index.xml
"""
    robots_path = os.path.join(output_dir, "robots.txt")
    with open(robots_path, "w") as f:
        f.write(robots_content)
    print(f"    ✅ Generated robots.txt")


def copy_static_root_files(output_dir):
    """Copy static files from docs/ that must be at site root (e.g. Google verification)"""
    docs_dir = "docs"
    copied = 0
    for filename in os.listdir(docs_dir):
        filepath = os.path.join(docs_dir, filename)
        if os.path.isfile(filepath) and not filename.endswith(".md"):
            dest = os.path.join(output_dir, filename)
            if not os.path.exists(dest):
                shutil.copy2(filepath, dest)
                print(f"    Copied {filename} to {output_dir}/")
                copied += 1
    if copied:
        print(f"    ✅ Copied {copied} static root files")
    else:
        print(f"    No additional static files to copy")


def merge_search_indexes(output_dir):
    """Merge search indexes from all versioned subsites into a global index"""
    merged_docs = []
    config = {"lang": ["en"], "separator": "[\\s\\-]+", "pipeline": ["stopWordFilter"], "fields": {"title": {"boost": 1000.0}, "text": {"boost": 1.0}, "tags": {"boost": 1000000.0}}}

    for subsite in VERSIONED_SUBSITES:
        # Get actual version from versions.json (latest is an alias)
        actual_version = get_latest_version(output_dir, subsite)
        if not actual_version:
            print(f"    ⚠️  No versions.json found for {subsite}")
            continue

        index_path = os.path.join(output_dir, subsite, actual_version, "search", "search_index.json")
        if os.path.exists(index_path):
            with open(index_path) as f:
                data = json.load(f)

            # Add prefix using 'latest' alias for URL consistency
            prefix = f"{subsite}/latest/"
            for doc in data.get("docs", []):
                doc["location"] = prefix + doc["location"]
                merged_docs.append(doc)

            print(f"    Added {len(data.get('docs', []))} docs from {subsite} (v{actual_version})")
        else:
            print(f"    ⚠️  Index not found: {index_path}")

    # Write merged index
    merged_index = {"config": config, "docs": merged_docs}
    search_dir = os.path.join(output_dir, "search")
    os.makedirs(search_dir, exist_ok=True)

    with open(os.path.join(search_dir, "search_index.json"), "w") as f:
        json.dump(merged_index, f)

    print(f"    Total: {len(merged_docs)} docs in global search index")

def run_command(cmd, check=True, cwd=None):
    """Run shell command and return result"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    if check and result.returncode != 0:
        print(f"❌ Error: {result.stderr}")
        sys.exit(1)
    return result


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

    print("📋 Step 2: Build non-versioned sites (root + intermediate landing pages only)")

    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)

    # Build root site using mkdocs.yml (WITHOUT monorepo plugin)
    # This builds only the main page + redirects, without rebuilding all subsites
    # Search index will be merged from versioned subsite indexes later
    print("  Building root site (without monorepo)...")
    run_command("mkdocs build -f mkdocs.yml -d " + args.output_dir, check=False)

    # Build intermediate landing pages (platform, marketplace, storefront)
    # Using mkdocs.yml configs which override plugins to exclude redirects
    # This prevents generating hundreds of redirect HTML files
    print("  Building intermediate landing pages...")
    run_command(f"mkdocs build -f storefront/mkdocs.yml -d ../{args.output_dir}/storefront", check=False)
    run_command(f"mkdocs build -f platform/mkdocs.yml -d ../{args.output_dir}/platform", check=False)
    run_command(f"mkdocs build -f marketplace/mkdocs.yml -d ../{args.output_dir}/marketplace", check=False)

    print("✅ Non-versioned landing pages built (subsites will come from gh-pages)")

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

    # Create temp directory OUTSIDE the repo to avoid git conflicts
    temp_dir = tempfile.mkdtemp(prefix="vc-docs-versioned-")
    print(f"  Using temp directory: {temp_dir}")

    try:
        # Stash changes and checkout gh-pages
        print("  Stashing changes and switching to gh-pages branch...")
        run_command("git stash push -m 'temp changes for CI/CD build'", check=False)
        run_command("git checkout gh-pages")

        print("  Copying versioned content (all versions) to temp dir...")
        # Copy all versioned content from gh-pages to TEMP dir
        for subsite in ["marketplace", "platform", "storefront"]:
            for guide in ["developer-guide", "user-guide", "deployment-on-cloud"]:
                src_base = f"{subsite}/{guide}"
                dst_base = os.path.join(temp_dir, subsite, guide)

                if not os.path.exists(src_base):
                    print(f"  ⚠️  {src_base} not found in gh-pages")
                    continue

                print(f"    Copying {src_base}/ -> temp/{subsite}/{guide}/")
                os.makedirs(os.path.dirname(dst_base), exist_ok=True)
                shutil.copytree(src_base, dst_base, ignore=shutil.ignore_patterns('.git'))
                print(f"  ✅ {src_base}")

        # Return to original branch (no conflicts now!)
        print(f"  Returning to {current_branch} branch...")
        run_command(f"git checkout {current_branch}")
        run_command("git stash pop", check=False)

        # NOW move files from temp to site/
        print("  Moving versioned content from temp to site/...")
        for subsite in ["marketplace", "platform", "storefront"]:
            for guide in ["developer-guide", "user-guide", "deployment-on-cloud"]:
                src_base = os.path.join(temp_dir, subsite, guide)
                dst_base = f"{args.output_dir}/{subsite}/{guide}"

                if not os.path.exists(src_base):
                    continue

                print(f"    Moving temp/{subsite}/{guide}/ -> {dst_base}/")
                if os.path.exists(dst_base):
                    shutil.rmtree(dst_base)
                shutil.move(src_base, dst_base)

    except Exception as e:
        print(f"❌ Error during versioned content copy: {e}")
        # Try to return to original branch
        run_command(f"git checkout {current_branch}", check=False)
        sys.exit(1)
    finally:
        # Cleanup temp directory
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
            print(f"  Cleaned up temp directory")

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

    print("📋 Step 6: Merge search indexes from versioned subsites")

    # Merge search indexes from all versioned subsites into a global search index
    # This replaces the monorepo-generated index without rebuilding all subsites
    merge_search_indexes(args.output_dir)

    print("✅ Search indexes merged")

    print("📋 Step 7: Generate SEO files (sitemap index, robots.txt, static root files)")
    generate_sitemap_index(args.output_dir)
    generate_robots_txt(args.output_dir)
    copy_static_root_files(args.output_dir)
    print("✅ SEO files generated")

    # Cleanup
    if os.path.exists("mkdocs-temp-root.yml"):
        os.remove("mkdocs-temp-root.yml")

    print("📋 Step 8: Optimize build size (remove duplicates)")

    # Replace duplicate assets with symlinks
    print("  Deduplicating assets folders...")
    assets_replaced, assets_freed = deduplicate_assets(args.output_dir)
    print(f"  ✅ Replaced {assets_replaced} assets folders with symlinks ({format_size(assets_freed)} freed)")

    total_freed = assets_freed
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
