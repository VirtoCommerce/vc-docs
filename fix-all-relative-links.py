#!/usr/bin/env python3
"""
Fix all relative markdown links that use ../

This script converts ALL relative links (both cross-site and same-site) to absolute URLs with versioning.

Examples:
    From /platform/user-guide/docs/azure-ad/overview.md:
    ../../../developer-guide/Fundamentals/Security/extensions/adding-azure-as-sso-provider
    -> /platform/developer-guide/latest/Fundamentals/Security/extensions/adding-azure-as-sso-provider

    ../../../../platform/user-guide/catalog/overview
    -> /platform/user-guide/latest/catalog/overview

    ../../../storefront/developer-guide/authentication/adding-sso-provider
    -> /storefront/developer-guide/latest/authentication/adding-sso-provider
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional

# Configuration
SECTIONS = ['platform', 'storefront', 'marketplace']
GUIDES = ['developer-guide', 'user-guide', 'deployment-on-cloud']
DEFAULT_VERSION = 'latest'

# Pattern to match any relative link with ../
RELATIVE_LINK_PATTERN = re.compile(r'\]\(((?:\.\./)+)([^)]+)\)')


def resolve_relative_path(source_file: Path, relative_path: str) -> Optional[str]:
    """
    Resolve a relative path from a source file to its absolute path

    Args:
        source_file: The markdown file containing the link
        relative_path: The relative path (e.g., ../../../developer-guide/...)

    Returns:
        Absolute path string (e.g., /platform/developer-guide/latest/...) or None if not resolvable
    """
    # Get the directory containing the source file
    source_dir = source_file.parent

    # Resolve the relative path to an absolute path
    try:
        # Join the source directory with the relative path and resolve it
        target_path = (source_dir / relative_path).resolve()

        # Get the repository root (parent of this script)
        repo_root = Path(__file__).parent.resolve()

        # Make the target path relative to the repo root
        try:
            rel_to_root = target_path.relative_to(repo_root)
        except ValueError:
            # Target is outside the repository
            return None

        # Parse the path components
        parts = rel_to_root.parts

        if len(parts) < 3:
            return None

        section = parts[0]  # platform, storefront, marketplace
        guide = parts[1]    # developer-guide, user-guide, deployment-on-cloud

        # Check if it's a valid section and guide
        if section not in SECTIONS or guide not in GUIDES:
            return None

        # Skip 'docs' if it's present
        start_idx = 2
        if len(parts) > 2 and parts[2] == 'docs':
            start_idx = 3

        # Get the remaining path
        if len(parts) <= start_idx:
            return None

        remaining_path = '/'.join(parts[start_idx:])

        # Remove .md extension if present
        if remaining_path.endswith('.md'):
            remaining_path = remaining_path[:-3]

        # Build absolute versioned path
        return f'/{section}/{guide}/{DEFAULT_VERSION}/{remaining_path}'

    except Exception as e:
        # If resolution fails, return None
        return None


def fix_link(match: re.Match, source_file: Path) -> str:
    """
    Convert relative link to absolute path with versioning

    Args:
        match: Regex match object
        source_file: The file containing this link

    Returns:
        Fixed link string or original if not fixable
    """
    original = match.group(0)
    dots = match.group(1)  # ../../
    path = match.group(2)  # rest of the path

    # Skip if it's just a media/image reference within the same directory
    if not dots.count('../') >= 2:
        return original

    # Skip anchor links
    if path.startswith('#'):
        return original

    # Skip external URLs (already absolute)
    if path.startswith('http://') or path.startswith('https://') or path.startswith('//'):
        return original

    # Skip if it starts with /
    if path.startswith('/'):
        return original

    # Try to resolve the relative path
    absolute_path = resolve_relative_path(source_file, dots + path)

    if absolute_path:
        return f']({absolute_path})'

    # If we couldn't resolve it, return original
    return original


def process_file(file_path: Path, dry_run: bool = False) -> Tuple[int, List[str]]:
    """
    Process a single markdown file

    Args:
        file_path: Path to markdown file
        dry_run: If True, don't write changes

    Returns:
        Tuple of (number of changes, list of changes)
    """
    content = file_path.read_text(encoding='utf-8')
    changes = []

    def replacement_callback(match):
        original = match.group(0)
        fixed = fix_link(match, file_path)
        if original != fixed:
            changes.append(f"  {original} -> {fixed}")
        return fixed

    new_content = RELATIVE_LINK_PATTERN.sub(replacement_callback, content)

    if changes and not dry_run:
        file_path.write_text(new_content, encoding='utf-8')

    return len(changes), changes


def main():
    """Main script entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description='Fix all relative links (../) in markdown files'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be changed without modifying files'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Show all changes'
    )
    parser.add_argument(
        'paths',
        nargs='*',
        help='Specific files or directories to process (default: all sections)'
    )

    args = parser.parse_args()

    # Determine which files to process
    base_dir = Path(__file__).parent

    if args.paths:
        files = []
        for path_str in args.paths:
            path = Path(path_str)
            if path.is_file():
                files.append(path)
            elif path.is_dir():
                files.extend(path.rglob('*.md'))
    else:
        # Process all markdown files in all sections
        files = []
        for section in SECTIONS:
            section_path = base_dir / section
            if section_path.exists():
                files.extend(section_path.rglob('*.md'))

    if not files:
        print("No markdown files found to process")
        return 1

    print(f"{'DRY RUN: ' if args.dry_run else ''}Processing {len(files)} markdown files...")
    print()

    total_changes = 0
    files_changed = 0

    for file_path in sorted(files):
        num_changes, changes = process_file(file_path, dry_run=args.dry_run)

        if num_changes > 0:
            files_changed += 1
            total_changes += num_changes

            # Show relative path from base dir
            try:
                rel_path = file_path.relative_to(base_dir)
            except ValueError:
                rel_path = file_path

            print(f"✓ {rel_path}: {num_changes} link(s) fixed")

            if args.verbose:
                for change in changes:
                    print(change)
                print()

    print()
    print(f"{'Would fix' if args.dry_run else 'Fixed'} {total_changes} relative link(s) in {files_changed} file(s)")

    if args.dry_run:
        print()
        print("Run without --dry-run to apply changes")

    return 0


if __name__ == '__main__':
    sys.exit(main())
