# VirtoCommerce Documentation Versioning

Automatic documentation versioning system using [Mike](https://github.com/jimporter/mike).

## 🔑 Key Feature

**Version is specified locally in project files**, and the system automatically determines whether to update an existing version or create a new one.

## Version Configuration Files

### 1. VERSION (required)
Simple text file with version number:
```
1.0.0
```

### 2. version.json (optional)
Extended configuration with metadata:
```json
{
  "version": "1.0.0",
  "alias": "latest",
  "title": "VirtoCommerce Documentation v1.0.0",
  "description": "Official VirtoCommerce Platform Documentation",
  "releaseDate": "2025-09-04",
  "changelog": [
    "Initial documentation release",
    "Complete platform documentation"
  ]
}
```

## Automatic System Behavior

### Logic:
1. **Version unchanged** → updates content of existing version
2. **Version changed** → creates new version
3. **First deployment** → creates new version with specified alias

### Workflow example:
```bash
# Current version: 1.0.0 (already deployed)
# Update documentation...
./build-versioned-local.sh
# → Will update content of version 1.0.0

# Change version to 1.1.0
echo "1.1.0" > VERSION
./build-versioned-local.sh
# → Will create new version 1.1.0
```

## Local Development

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Build and Deploy
```bash
# Automatic version detection from files
./build-versioned-local.sh

# Explicit version specification (overrides files)
./build-versioned-local.sh v3.2024 latest

# Local preview
mike serve
```

### Version Management Utilities
```bash
# Get current version
python3 version-utils.py get-version

# Get configuration
python3 version-utils.py get-config

# Check if it will update or create new version
python3 version-utils.py check-should-update

# Get deploy parameters
python3 version-utils.py get-deploy-params
```

## GitHub Actions

### Automatic Mode (Recommended)
Workflow dispatch with default parameters:
- **version**: `auto` (reads from VERSION/version.json)
- **alias**: `auto` (reads from version.json)
- **deploy_mode**: `versioned`

### Manual Override
You can specify explicit values:
- **version**: `v3.2024`
- **alias**: `latest`
- **deploy_mode**: `versioned`

### Scheduled Deployment
Automatically runs daily at 19:30 UTC with `auto` parameter.

## Version Management

### Mike Commands
```bash
# List all versions
mike list

# Set default version
mike set-default latest

# Delete version
mike delete old-version

# Add alias to version
mike alias v1.0.0 stable

# Rename version
mike retitle v1.0.0 "Version 1.0.0 (Stable)"
```

## URL Structure

- `https://docs.virtocommerce.org/` → redirect to latest
- `https://docs.virtocommerce.org/latest/` → latest stable version
- `https://docs.virtocommerce.org/1.0.0/` → specific version
- `https://docs.virtocommerce.org/dev/` → development version

## Docker and Nginx

The system uses two nginx configurations:
1. **nginx.versioned.conf** - for versioned mode with Mike support
2. **nginx.default.conf** - for legacy mode

Configuration is automatically selected based on `deploy_mode`.

## Project File Structure

```
vc-docs/
├── VERSION                      # Version number (required)
├── version.json                # Extended configuration (optional)
├── version-utils.py            # Version management utilities
├── requirements.txt            # Python dependencies
├── build-versioned-local.sh   # Local build with auto-detection
├── deploy-versioned.sh         # Production deploy for CI/CD
└── docs/                       # Documentation
```

## Migration and Backward Compatibility

- **Legacy mode** continues to work via `deploy_mode: legacy`
- **Existing URLs** supported through nginx redirects
- **Gradual migration** without disrupting system operation

## Troubleshooting

### Problem: Version not updating
**Solution**: Check that you changed the `VERSION` file before deployment.

### Problem: Alias not working
**Solution**: Make sure the alias is specified in `version.json`.

### Problem: Old URLs not working
**Solution**: Check nginx.versioned.conf for redirect rules.

## Frequently Asked Questions

**Q: How to rollback a version?**
A: Use `mike delete <version>` and redeploy the needed version.

**Q: Can I have multiple aliases?**
A: Yes, use `mike alias <version> <new-alias>`.

**Q: How to update existing version?**
A: Simply run deployment with the same version in the `VERSION` file.

**Q: Where are versions stored?**
A: All versions are stored in the `gh-pages` branch of the Git repository.