"""
MkDocs hook to fix search index URLs for versioned documentation built with mike.

This hook ensures that search results link to the correct versioned paths by:
1. Detecting the current version being built (from MIKE_VERSION env var)
2. Prepending the version to all document locations in the search index
3. Only running when building with mike (not for local development)

Usage: Add to mkdocs.yml hooks section
"""

import os
import json
import logging

log = logging.getLogger('mkdocs.plugins.search_index_fixer')

def on_post_build(config, **kwargs):
    """
    Called after mkdocs build completes.
    Fixes search index URLs to include version prefix.
    """

    # Check if we're building with mike (MIKE_VERSION env var is set)
    mike_version = os.environ.get('MIKE_VERSION')

    if not mike_version:
        log.info('Not building with mike - skipping search index fix')
        return

    # Get the site directory
    site_dir = config.get('site_dir', 'site')
    search_index_path = os.path.join(site_dir, 'search', 'search_index.json')

    # Check if search index exists
    if not os.path.exists(search_index_path):
        log.warning(f'Search index not found at {search_index_path}')
        return

    try:
        # Read the search index
        with open(search_index_path, 'r', encoding='utf-8') as f:
            search_index = json.load(f)

        # Fix all document locations
        fixed_count = 0
        for doc in search_index.get('docs', []):
            location = doc.get('location', '')

            # Skip if location is empty or already has version
            if not location or location.startswith(f'{mike_version}/'):
                continue

            # Prepend version to location
            doc['location'] = f'{mike_version}/{location}'
            fixed_count += 1

        # Write the fixed search index back
        with open(search_index_path, 'w', encoding='utf-8') as f:
            json.dump(search_index, f, ensure_ascii=False, separators=(',', ':'))

        log.info(f'✅ Fixed {fixed_count} document locations in search index with version: {mike_version}')

    except Exception as e:
        log.error(f'❌ Error fixing search index: {e}')
        # Don't fail the build, just log the error
