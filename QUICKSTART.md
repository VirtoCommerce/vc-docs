# Quick Start Guide - Documentation Versioning

Simple interactive CLI for managing documentation versions.

## Launch Interactive CLI

**All platforms (Linux/Mac/Windows):**
```bash
python3 version-manager.py
```

Or on Windows:
```powershell
python version-manager.py
```

## Interactive Menu

After launching, you'll see a menu:

```
╔════════════════════════════════════════════════════════════╗
║  Virto Commerce Documentation Version Manager          ║
╚════════════════════════════════════════════════════════════╝

Choose an action:

  1) Deploy version to single subsite
  2) Deploy version to ALL subsites
  3) Delete version from single subsite
  4) Delete version from ALL subsites
  5) List versions
  6) Set default version
  7) Add alias to version
  0) Exit

Enter your choice [0-7]:
```

Simply enter the number and follow the prompts!

## Available Subsites

- `marketplace/developer-guide`
- `marketplace/user-guide`
- `platform/developer-guide`
- `platform/user-guide`
- `platform/deployment-on-cloud`
- `storefront/developer-guide`
- `storefront/user-guide`

## Common Workflows

### Release New Version

1. Run `python3 version-manager.py`
2. Select option `2` (Deploy version to ALL subsites)
3. Enter version (e.g., `1.2`)
4. Answer `y` to set as latest
5. Answer `y` to set as default
6. Answer `y` to push to GitHub immediately
7. Confirm with `y`

The changes will be automatically pushed to the `gh-pages` branch!

### Update Single Subsite

1. Run `python3 version-manager.py`
2. Select option `1` (Deploy version to single subsite)
3. Choose subsite from list
4. Enter version (e.g., `1.1.1`)
5. Answer `y` to set as latest

### Remove Old Version

1. Run `python3 version-manager.py`
2. Select option `4` (Delete version from ALL subsites)
3. Enter version to delete (e.g., `1.0`)
4. Confirm with `y`

### Test Locally

```bash
# Switch to gh-pages branch
git checkout gh-pages

# Start server
python3 -m http.server 8000

# Open browser
# http://localhost:8000/marketplace/developer-guide/
```

### Push to Production

**Option 1: Automatic (recommended)**
When deploying, answer `y` to "Push to GitHub immediately?" and changes will be pushed automatically.

**Option 2: Manual push**
If you chose not to push automatically:
```bash
git push origin gh-pages
```

## That's It!

For detailed documentation, see [VERSIONING.md](VERSIONING.md).

