#!/usr/bin/env python3
"""
Fix cross-site markdown links

This script converts relative cross-site links to absolute URLs with versioning.

Examples:
    ../../../../platform/user-guide/catalog/overview
    -> /platform/user-guide/latest/catalog/overview

    ../../../storefront/developer-guide/authentication/adding-sso-provider
    -> /storefront/developer-guide/latest/authentication/adding-sso-provider
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

# Configuration
SECTIONS = ['platform', 'storefront', 'marketplace']
GUIDES = ['developer-guide', 'user-guide', 'deployment-on-cloud']
DEFAULT_VERSION = 'latest'

# Pattern to match cross-site relative links
# Matches: ](../../../platform/user-guide/...)
CROSS_SITE_PATTERN = re.compile(
    r'\]\((\.\./)+(' + '|'.join(SECTIONS) + r')/'
    r'(' + '|'.join(GUIDES) + r')/'
    r'([^)]+)\)'
)


def fix_link(match: re.Match) -> str:
    """
    Convert relative cross-site link to absolute path with versioning

    Args:
        match: Regex match object

    Returns:
        Fixed link string
    """
    dots = match.group(1)  # ../../ (not used)
    section = match.group(2)  # platform/storefront/marketplace
    guide = match.group(3)    # developer-guide/user-guide/deployment-on-cloud
    path = match.group(4)     # rest of the path

    # Build absolute versioned path (without domain)
    # This works on production because browser resolves /platform/...
    # relative to the domain root (docs.virtocommerce.org/platform/...)
    fixed = f'](/{section}/{guide}/{DEFAULT_VERSION}/{path})'

    return fixed


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
        fixed = fix_link(match)
        if original != fixed:
            changes.append(f"  {original} -> {fixed}")
        return fixed

    new_content = CROSS_SITE_PATTERN.sub(replacement_callback, content)

    if changes and not dry_run:
        file_path.write_text(new_content, encoding='utf-8')

    return len(changes), changes


def main():
    """Main script entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description='Fix cross-site relative links in markdown files'
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
    print(f"{'Would fix' if args.dry_run else 'Fixed'} {total_changes} cross-site link(s) in {files_changed} file(s)")

    if args.dry_run:
        print()
        print("Run without --dry-run to apply changes")

    return 0


if __name__ == '__main__':
    sys.exit(main())
