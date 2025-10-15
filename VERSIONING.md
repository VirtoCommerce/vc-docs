# Documentation Versioning Strategy

This document describes the versioning strategy for Virto Commerce documentation using [Mike](https://github.com/jimporter/mike).

## Overview

The documentation is structured as multiple independent sites, with versioning implemented at the subsite level:

### Site Structure

```
docs.virtocommerce.org/
├── / (root - NOT versioned)
├── marketplace/ (intermediate - NOT versioned)
│   ├── developer-guide/ (VERSIONED)
│   └── user-guide/ (VERSIONED)
├── platform/ (intermediate - NOT versioned)
│   ├── developer-guide/ (VERSIONED)
│   ├── user-guide/ (VERSIONED)
│   └── deployment-on-cloud/ (VERSIONED)
└── storefront/ (intermediate - NOT versioned)
    ├── developer-guide/ (VERSIONED)
    └── user-guide/ (VERSIONED)
```

### Versioned Subsites

Each of the following subsites has independent version management:

1. **marketplace/developer-guide**
2. **marketplace/user-guide**
3. **platform/developer-guide**
4. **platform/user-guide**
5. **platform/deployment-on-cloud**
6. **storefront/developer-guide**
7. **storefront/user-guide**

## URL Structure

Versions are reflected in the URL path:

```
https://docs.virtocommerce.org/marketplace/developer-guide/1.0/
https://docs.virtocommerce.org/platform/user-guide/3.2025-S13/
https://docs.virtocommerce.org/storefront/developer-guide/latest/
```

## Version Naming Convention

We use the following version naming conventions:

### Product Versions
Format: `3.YYYY-SNN` (e.g., `3.2025-S13`)
- `3` - Major version
- `YYYY` - Year
- `SNN` - Sprint number

### Module/Feature Versions
Format: `MAJOR.MINOR[.PATCH]` (e.g., `1.0`, `2.5`, `1.2.3`)
- Follows semantic versioning
- Used for specific module documentation

### Special Aliases
- `latest` - Points to the most recent version
- `stable` - Points to the current stable/recommended version
- Version-specific aliases as needed

## Mike Storage Structure

Mike stores versions in the `gh-pages` branch:

```
gh-pages/
├── marketplace/
│   ├── developer-guide/
│   │   ├── 1.0/           (version 1.0 files)
│   │   ├── 1.1/           (version 1.1 files)
│   │   ├── latest/        (symlink or copy)
│   │   └── versions.json  (version metadata)
│   └── user-guide/
│       ├── 1.0/
│       └── versions.json
├── platform/
│   ├── developer-guide/
│   │   ├── 3.2025-S11/
│   │   ├── 3.2025-S12/
│   │   ├── 3.2025-S13/
│   │   ├── latest/
│   │   └── versions.json
│   ├── user-guide/
│   │   └── versions.json
│   └── deployment-on-cloud/
│       └── versions.json
└── storefront/
    ├── developer-guide/
    │   └── versions.json
    └── user-guide/
        └── versions.json
```

## Deployment Workflows

### Development Workflow (Non-Versioned)

For local development and testing without versioning:

```powershell
# Build all sites without versioning
.\build.ps1

# Or serve locally for live reload
mkdocs serve

# Or serve specific subsite
cd marketplace/developer-guide
mkdocs serve
```

### Production Workflow (Versioned)

For production deployment with versioning:

#### 1. Deploy All Subsites with Same Version

Deploy all 7 subsites with the same version number:

```powershell
# PowerShell
.\scripts\build-versioned.ps1 -Version "3.2025-S13" -SetAsLatest -SetAsDefault

# Bash
./scripts/build-versioned.sh 3.2025-S13 --set-latest --set-default
```

#### 2. Deploy Single Subsite

Deploy a specific subsite with a version:

```powershell
# PowerShell
.\scripts\deploy-version.ps1 `
    -SubsitePath "marketplace/developer-guide" `
    -Version "1.0" `
    -Alias "latest" `
    -UpdateAliases `
    -SetDefault

# Bash
./scripts/deploy-version.sh marketplace/developer-guide 1.0 latest --set-default --update-aliases
```

#### 3. List Versions

View all deployed versions:

```powershell
# PowerShell - all subsites
.\scripts\list-versions.ps1

# PowerShell - specific subsite
.\scripts\list-versions.ps1 -SubsitePath "platform/developer-guide"

# Bash - all subsites
./scripts/list-versions.sh

# Bash - specific subsite
./scripts/list-versions.sh platform/developer-guide
```

#### 4. Test Locally

Test versioned documentation locally:

```bash
# Serve specific subsite with versions
mike serve -F marketplace/developer-guide/mkdocs.yml \
    --deploy-prefix marketplace/developer-guide

# Open browser to http://localhost:8000
```

#### 5. Push to Production

After testing, push to gh-pages:

```bash
git push origin gh-pages
```

## Version Management Best Practices

### When to Create a New Version

Create a new version when:
- Major feature updates
- Breaking changes in functionality
- Quarterly/sprint releases
- Significant content updates

### When to Update Existing Version

Update existing version when:
- Fixing typos and minor errors
- Updating screenshots
- Adding clarifications
- Small content improvements

### Managing Multiple Versions

1. **Keep 3-4 recent versions** - Archive older versions to keep the version selector manageable
2. **Update 'latest' alias** - Always point to the newest version
3. **Maintain 'stable' alias** - Point to the current recommended production version
4. **Set proper defaults** - Ensure the default version is appropriate for new users

### Deleting Old Versions

To delete an old version:

```bash
mike delete -F <subsite>/mkdocs.yml --deploy-prefix <subsite> <version>

# Example
mike delete -F marketplace/developer-guide/mkdocs.yml \
    --deploy-prefix marketplace/developer-guide 0.9
```

### Retitling Versions

To change version title:

```bash
mike retitle -F <subsite>/mkdocs.yml --deploy-prefix <subsite> <version> "New Title"

# Example
mike retitle -F platform/developer-guide/mkdocs.yml \
    --deploy-prefix platform/developer-guide 3.2025-S13 "Spring 2025 (S13)"
```

## Version Selector UI

The version selector appears automatically in the header of each versioned subsite. Users can:
- Switch between versions
- See which version they're currently viewing
- Identify the default version

### Customization

Version selector can be customized via MkDocs Material theme configuration in each subsite's `mkdocs.yml`:

```yaml
extra:
  version:
    provider: mike
    default: latest
```

## Release Process

### Standard Release

1. **Prepare content** - Ensure all changes are committed
2. **Deploy version** - Use build-versioned script
3. **Test locally** - Verify using mike serve
4. **Update aliases** - Set latest/stable as needed
5. **Push to production** - Push gh-pages branch
6. **Verify live site** - Check production URLs

### Hotfix Release

1. **Checkout version** - Switch to gh-pages branch
2. **Find version files** - Navigate to specific version directory
3. **Apply fixes** - Edit HTML files directly (not recommended) OR
4. **Redeploy version** - Use deploy-version script with same version number
5. **Push changes** - Push gh-pages branch

## Troubleshooting

### Version Selector Not Appearing

1. Verify `extra.version.provider: mike` in mkdocs.yml
2. Check that Mike deployed successfully
3. Ensure versions.json exists in gh-pages branch
4. Clear browser cache

### Wrong Default Version

```bash
# Set correct default
mike set-default -F <subsite>/mkdocs.yml --deploy-prefix <subsite> <version>
```

### Missing Versions in Selector

```bash
# List versions to verify
mike list -F <subsite>/mkdocs.yml --deploy-prefix <subsite>

# If missing, redeploy
.\scripts\deploy-version.ps1 -SubsitePath <path> -Version <ver>
```

### Conflicts in gh-pages

If gh-pages branch has conflicts:

```bash
# Backup current gh-pages
git checkout gh-pages
git branch gh-pages-backup

# Force rebuild if necessary (CAUTION: This deletes all versions!)
git checkout main
git branch -D gh-pages
git checkout -b gh-pages --orphan
.\scripts\build-versioned.ps1 -Version "latest"
git push -f origin gh-pages
```

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Deploy Documentation

on:
  push:
    branches: [ main ]
    tags: [ 'v*' ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: |
          pip install mkdocs-material mike
          pip install mkdocs-awesome-pages-plugin mkdocs-git-revision-date-localized-plugin
          pip install mkdocs-minify-plugin mkdocs-redirects mkdocs-monorepo-plugin

      - name: Configure Git
        run: |
          git config user.name github-actions
          git config user.email github-actions@github.com

      - name: Extract version
        id: version
        run: echo "VERSION=${GITHUB_REF#refs/tags/v}" >> $GITHUB_OUTPUT

      - name: Deploy versioned docs
        run: ./scripts/build-versioned.sh ${{ steps.version.outputs.VERSION }} --set-latest --set-default

      - name: Push to gh-pages
        run: git push origin gh-pages
```

## Migration Guide

### Migrating Existing Non-Versioned Docs

If you have existing non-versioned documentation:

1. **Backup current site** directory
2. **Choose initial version** (e.g., "1.0" or current product version)
3. **Deploy first version**:
   ```bash
   .\scripts\build-versioned.ps1 -Version "1.0" -SetAsLatest -SetAsDefault
   ```
4. **Verify** using mike serve
5. **Push to production**

### Migrating from Other Versioning Solutions

If migrating from other versioning tools:

1. Export existing version content
2. Organize into Mike-compatible structure
3. Deploy each version separately using deploy-version script
4. Set appropriate aliases and defaults
5. Test thoroughly before pushing to production

## Support

For issues or questions about versioning:
- Check Mike documentation: https://github.com/jimporter/mike
- Review this guide's troubleshooting section
- Contact the documentation team

