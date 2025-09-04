# VirtoCommerce Documentation Versioning - Quick Start

## 🚀 Quick Start

### 1. Installation
```bash
pip install -r requirements.txt
```

### 2. Version Setup
Edit the `VERSION` file:
```bash
echo "1.0.0" > VERSION
```

Or create extended configuration `version.json`:
```json
{
  "version": "1.0.0",
  "alias": "latest"
}
```

### 3. Local Build
```bash
# Automatic version detection
./build-versioned-local.sh

# Or with explicit specification
./build-versioned-local.sh v3.2024 latest
```

### 4. Preview
```bash
mike serve
# Open http://localhost:8000
```

## 📋 Version Management

### Automatic Behavior:
- **Version NOT changed** → updates content of existing version
- **Version changed** → creates new version

### Examples:
```bash
# Update documentation without version change
# (VERSION = 1.0.0, version already deployed)
./build-versioned-local.sh
# → Will update content of version 1.0.0

# Create new version
echo "1.1.0" > VERSION
./build-versioned-local.sh
# → Will create new version 1.1.0
```

## 🔧 Utilities

```bash
# Check current version
python3 version-utils.py get-version

# Find out what the system will do
python3 version-utils.py check-should-update

# List deployed versions
mike list
```

## 🚢 GitHub Actions

### Automatic mode (recommended):
1. Actions → virtocommerce.com docs
2. Run workflow
3. Use default parameters:
   - version: `auto`
   - alias: `auto`
   - deploy_mode: `versioned`

### Manual version specification:
- version: `v3.2024`
- alias: `latest`
- deploy_mode: `versioned`

## 📁 File Structure

```
vc-docs/
├── VERSION                  # ← Change version here
├── version.json            # ← Optional configuration
├── build-versioned-local.sh # ← Run for build
└── version-utils.py        # ← Utilities for checking
```

## 🔗 URL Structure

- `/` → latest version
- `/1.0.0/` → specific version
- `/dev/` → development version

## ❓ Help

Full documentation: [VERSIONING.md](./VERSIONING.md)