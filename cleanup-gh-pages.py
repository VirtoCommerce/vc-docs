#!/usr/bin/env python3
"""
Cleanup script for gh-pages branch.
Removes garbage folders that accumulate from mike/mkdocs builds.
"""

import os
import subprocess
import shutil
import argparse


def run_command(cmd, check=True, cwd=None):
    """Run shell command and return result"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    if check and result.returncode != 0:
        print(f"Error: {result.stderr}")
        return None
    return result


def get_folder_size(path):
    """Calculate total size of a folder in bytes."""
    total = 0
    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if not os.path.islink(filepath):
                try:
                    total += os.path.getsize(filepath)
                except OSError:
                    pass
    return total


def format_size(size_bytes):
    """Format bytes as human-readable size."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} TB"


def find_garbage_folders(root_dir):
    """
    Find garbage folders in gh-pages that should be removed.

    Garbage includes:
    1. 'site/' folders inside versioned subsites (created by mkdocs build accidents)
    2. Duplicate folders like 'developer-guide/developer-guide/' (naming collision artifacts)
    """
    garbage = []

    # Pattern 1: site/ folders inside versioned paths
    # e.g., platform/developer-guide/site/, marketplace/user-guide/site/
    for section in ["marketplace", "platform", "storefront"]:
        section_path = os.path.join(root_dir, section)
        if not os.path.exists(section_path):
            continue

        # Check section/site/ (intermediate level)
        site_path = os.path.join(section_path, "site")
        if os.path.exists(site_path) and os.path.isdir(site_path):
            garbage.append(site_path)

        # Check section/guide/site/
        for guide in ["developer-guide", "user-guide", "deployment-on-cloud"]:
            guide_path = os.path.join(section_path, guide)
            if not os.path.exists(guide_path):
                continue

            site_path = os.path.join(guide_path, "site")
            if os.path.exists(site_path) and os.path.isdir(site_path):
                garbage.append(site_path)

    # Pattern 2: Duplicate nested folders (developer-guide/developer-guide/, etc.)
    # These are created when mike deploy path gets confused
    for section in ["marketplace", "platform", "storefront"]:
        for guide in ["developer-guide", "user-guide", "deployment-on-cloud"]:
            nested_path = os.path.join(root_dir, section, guide, guide)
            if os.path.exists(nested_path) and os.path.isdir(nested_path):
                garbage.append(nested_path)

    return garbage


def main():
    parser = argparse.ArgumentParser(description='Cleanup gh-pages branch from garbage folders')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be deleted without actually deleting')
    parser.add_argument('--push', action='store_true', help='Push changes to remote after cleanup')
    args = parser.parse_args()

    print("Cleanup gh-pages branch from garbage folders")
    print("=" * 50)

    # Check if we're in the right directory
    if not os.path.exists(".git"):
        print("Error: Please run this script from the vc-docs root directory")
        return 1

    # Save current branch
    result = run_command("git branch --show-current")
    if not result:
        print("Error: Could not determine current branch")
        return 1
    original_branch = result.stdout.strip()
    print(f"Current branch: {original_branch}")

    # Stash any changes
    print("\nStashing any uncommitted changes...")
    run_command("git stash push -m 'cleanup-gh-pages temp stash'", check=False)

    try:
        # Checkout gh-pages
        print("Switching to gh-pages branch...")
        result = run_command("git checkout gh-pages")
        if not result:
            print("Error: Could not checkout gh-pages branch")
            return 1

        # Find garbage folders
        print("\nScanning for garbage folders...")
        garbage = find_garbage_folders(".")

        if not garbage:
            print("No garbage folders found!")
            return 0

        # Calculate sizes and display
        total_size = 0
        print(f"\nFound {len(garbage)} garbage folders:")
        print("-" * 50)

        for path in sorted(garbage):
            size = get_folder_size(path)
            total_size += size
            rel_path = os.path.relpath(path, ".")
            print(f"  {rel_path}/ ({format_size(size)})")

        print("-" * 50)
        print(f"Total size to be freed: {format_size(total_size)}")

        if args.dry_run:
            print("\n[DRY RUN] No changes made.")
            return 0

        # Confirm deletion
        print("\nDeleting garbage folders...")
        deleted_count = 0

        for path in garbage:
            rel_path = os.path.relpath(path, ".")
            try:
                shutil.rmtree(path)
                print(f"  Deleted: {rel_path}/")
                deleted_count += 1
            except Exception as e:
                print(f"  Error deleting {rel_path}: {e}")

        print(f"\nDeleted {deleted_count}/{len(garbage)} folders")

        # Commit changes
        if deleted_count > 0:
            print("\nCommitting changes...")
            run_command("git add -A")
            run_command('git commit -m "chore: cleanup garbage folders from gh-pages\n\nRemoved site/ folders and duplicate nested folders.\nFreed approximately ' + format_size(total_size) + '."')
            print("Changes committed!")

            if args.push:
                print("\nPushing to remote...")
                result = run_command("git push origin gh-pages")
                if result:
                    print("Pushed successfully!")
                else:
                    print("Warning: Push failed. You may need to push manually.")

        return 0

    finally:
        # Return to original branch
        print(f"\nReturning to {original_branch} branch...")
        run_command(f"git checkout {original_branch}")
        run_command("git stash pop", check=False)
        print("Done!")


if __name__ == "__main__":
    exit(main())
