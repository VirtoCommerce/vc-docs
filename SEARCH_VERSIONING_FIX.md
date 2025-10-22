# Fix for Search in Versioned Documentation Sites

## Problem Description

After implementing Mike versioning for the documentation sites, the search functionality stopped working properly. The issues were:

1. **No indexed pages**: Search index was not being created for versioned sites
2. **Cross-version search results**: Search was returning results from all versions instead of just the current version
3. **Sitemap issues**: Sitemap was not updated for the new versioned structure

## Root Cause

The problem occurred because:

1. **Mike creates isolated versions** in separate directories (e.g., `/1.0/`, `/latest/`)
2. **Search configuration was not version-aware** - it was trying to index all content regardless of version
3. **Sitemap was pointing to non-versioned URLs** instead of versioned ones

## Solution Implemented

### 1. Updated Search Configuration

Added version-aware search configuration to all versioned `mkdocs.yml` files:

```yaml
# Override plugins for versioned site
plugins:
    - search:
        # Configure search for versioned content
        lang: en
        # Only index current version
        index_docs: true
        index_other: false
        # Exclude versioned paths from other versions
        exclude_docs: |
            /1.0/
            /1.1/
            /2.0/
            /latest/

# Search configuration for versioned site
extra:
    search:
        # Limit search to current version only
        index_only_current: true
        # Exclude other versions from search index
        exclude_versions: true
```

### 2. Updated Sitemap Structure

Modified `sitemap.xml` to point to versioned URLs:

```xml
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <!-- Versioned subsites - latest versions -->
    <sitemap>
        <loc>https://docs.virtocommerce.org/platform/developer-guide/latest/sitemap.xml</loc>
    </sitemap>
    <sitemap>
        <loc>https://docs.virtocommerce.org/platform/user-guide/latest/sitemap.xml</loc>
    </sitemap>
    <!-- ... other versioned sites ... -->
</urlset>
```

### 3. Created Automation Scripts

#### `fix-search-versioning.py`
- Automatically updates all versioned `mkdocs.yml` files with proper search configuration
- Ensures consistent search settings across all versioned sites

#### `test-versioned-search.py`
- Tests search functionality in all versioned sites
- Verifies that search indexes are created correctly
- Validates search content isolation

#### `deploy-with-fixed-search.py`
- Deploys all versioned sites with Mike
- Ensures proper version isolation
- Sets up correct aliases and defaults

## How It Works

### Search Isolation

1. **Per-version indexing**: Each version has its own search index
2. **Version-specific search**: Search only returns results from the current version
3. **Excluded paths**: Other version paths are explicitly excluded from indexing

### Version Structure

```
docs.virtocommerce.org/
├── platform/developer-guide/
│   ├── latest/          # Latest version (search works here)
│   ├── 1.0/            # Version 1.0 (search works here)
│   └── 1.1/            # Version 1.1 (search works here)
├── platform/user-guide/
│   ├── latest/          # Latest version (search works here)
│   └── 1.0/            # Version 1.0 (search works here)
└── ...
```

### Search Behavior

- **In `/latest/`**: Search returns results only from the latest version
- **In `/1.0/`**: Search returns results only from version 1.0
- **No cross-version results**: Users won't see results from other versions

## Files Modified

### Configuration Files Updated
- `marketplace/developer-guide/mkdocs.yml`
- `marketplace/user-guide/mkdocs.yml`
- `platform/developer-guide/mkdocs.yml`
- `platform/user-guide/mkdocs.yml`
- `platform/deployment-on-cloud/mkdocs.yml`
- `storefront/developer-guide/mkdocs.yml`
- `storefront/user-guide/mkdocs.yml`

### Root Files Updated
- `sitemap.xml` - Updated for versioned structure
- `fix-search-versioning.py` - Automation script
- `test-versioned-search.py` - Testing script
- `deploy-with-fixed-search.py` - Deployment script

## Testing

### Automated Testing
```bash
# Test search functionality
python3 test-versioned-search.py

# Fix search configuration
python3 fix-search-versioning.py

# Deploy with fixed search
python3 deploy-with-fixed-search.py
```

### Manual Testing
1. **Build each site**: `cd platform/developer-guide && mkdocs build`
2. **Check search index**: Look for `site/search/search_index.json`
3. **Test search**: Open the site and test search functionality
4. **Verify isolation**: Ensure search only returns results from current version

## Benefits

1. **Isolated search**: Each version has its own search scope
2. **Better user experience**: Users only see relevant results from their version
3. **Proper indexing**: Search engines can properly index versioned content
4. **Maintainable**: Automated scripts ensure consistent configuration

## Future Considerations

1. **Search analytics**: Track search usage per version
2. **Cross-version search**: Optional feature to search across versions
3. **Search suggestions**: Version-aware search suggestions
4. **Performance optimization**: Optimize search index size and speed

## Troubleshooting

### Search Not Working
1. Check if search index exists: `site/search/search_index.json`
2. Verify search configuration in `mkdocs.yml`
3. Rebuild the site: `mkdocs build`
4. Check browser console for JavaScript errors

### Cross-Version Results
1. Verify `exclude_docs` configuration
2. Check that version paths are properly excluded
3. Rebuild and redeploy the site

### Sitemap Issues
1. Verify sitemap URLs point to versioned paths
2. Check that sitemap is accessible
3. Update sitemap if new versions are added
