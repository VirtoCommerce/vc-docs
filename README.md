# Overview

## What Is MkDocs?

MkDocs is a **fast**, **simple** and **downright gorgeous** static site generator that's geared towards building project documentation.
More info: https://www.mkdocs.org/

## Prerequisites - Install pip on Windows
Follow the instructions in this article
https://www.dataquest.io/blog/install-pip-windows/

## Setup on-premises

### Install MkDocs and all required packages
```bash
# Install MkDocs Material theme and core dependencies
pip install mkdocs-material

# Install additional plugins
pip install mkdocs-awesome-pages-plugin mkdocs-git-revision-date-localized-plugin \
    mkdocs-minify-plugin mkdocs-redirects mkdocs-monorepo-plugin \
    mkdocs-include-markdown-plugin pymdown-extensions jinja2

# Install Mike for versioning support
pip install mike
```

### Quick install (all at once)
```bash
pip install mkdocs-material mike mkdocs-awesome-pages-plugin \
    mkdocs-git-revision-date-localized-plugin mkdocs-minify-plugin \
    mkdocs-redirects mkdocs-monorepo-plugin mkdocs-include-markdown-plugin \
    pymdown-extensions jinja2
```

## Documentation Versioning with Mike

This project uses [Mike](https://github.com/jimporter/mike) for **independent versioning of each documentation subsite**.

### Architecture

The documentation is structured with **7 independently versioned subsites**:

- `marketplace/developer-guide` ✓ Versioned
- `marketplace/user-guide` ✓ Versioned
- `platform/developer-guide` ✓ Versioned
- `platform/user-guide` ✓ Versioned
- `platform/deployment-on-cloud` ✓ Versioned
- `storefront/developer-guide` ✓ Versioned
- `storefront/user-guide` ✓ Versioned

Root site (`/`) and intermediate sites (`/marketplace/`, `/platform/`, `/storefront/`) remain **unversioned**.

### URL Structure

Versions are part of the URL path:
```
https://docs.virtocommerce.org/marketplace/developer-guide/1.0/
https://docs.virtocommerce.org/platform/user-guide/3.2025-S13/
https://docs.virtocommerce.org/storefront/developer-guide/latest/
```

### Quick Start Commands

#### Deploy All Subsites (Same Version)

Deploy all 7 subsites with version 3.2025-S13:

```powershell
# PowerShell
.\scripts\build-versioned.ps1 -Version "3.2025-S13" -SetAsLatest -SetAsDefault

# Bash/Linux/macOS
./scripts/build-versioned.sh 3.2025-S13 --set-latest --set-default
```

#### Deploy Single Subsite

Deploy a specific subsite with a version:

```powershell
# PowerShell
.\scripts\deploy-version.ps1 -SubsitePath "marketplace/developer-guide" -Version "1.0" -Alias "latest" -SetDefault

# Bash/Linux/macOS
./scripts/deploy-version.sh marketplace/developer-guide 1.0 latest --set-default
```

#### List Versions

View all deployed versions:

```powershell
# PowerShell
.\scripts\list-versions.ps1                                    # All subsites
.\scripts\list-versions.ps1 -SubsitePath "platform/user-guide" # Specific subsite

# Bash/Linux/macOS
./scripts/list-versions.sh                        # All subsites
./scripts/list-versions.sh platform/user-guide    # Specific subsite
```

#### Test Locally with Versions

**Option 1: Test a versioned subsite with Mike**

```bash
# From root directory
cd /Users/symbot/DEV/vc-docs

# Set default version (required for root URL to work)
mike set-default -F marketplace/developer-guide/mkdocs.yml \
    --deploy-prefix marketplace/developer-guide 1.0

# Start server from subsite directory
cd marketplace/developer-guide && mike serve

# Open http://localhost:8000
```

**Option 2: View all deployed versions from gh-pages**

```bash
# Switch to gh-pages branch
git checkout gh-pages

# Start HTTP server
python3 -m http.server 8000

# Open http://localhost:8000/marketplace/developer-guide/
```

### How It Works

Mike stores versions in the `gh-pages` branch with this structure:

```
gh-pages/
├── marketplace/
│   ├── developer-guide/
│   │   ├── 1.0/
│   │   ├── 1.1/
│   │   ├── latest/
│   │   └── versions.json
│   └── user-guide/
│       ├── 1.0/
│       └── versions.json
├── platform/
│   ├── developer-guide/
│   └── user-guide/
└── storefront/
    ├── developer-guide/
    └── user-guide/
```

Each subsite maintains its own:
- Version history
- Version selector
- Default version
- Aliases (latest, stable, etc.)

### Documentation

For detailed information, see:
- **[VERSIONING.md](VERSIONING.md)** - Complete versioning strategy, workflows, and best practices
- **Scripts documentation:**
  - `scripts/build-versioned.ps1` - Deploy all subsites with a version
  - `scripts/deploy-version.ps1` - Deploy single subsite with a version
  - `scripts/list-versions.ps1` - List versions for subsites

## Development Workflow

### Regular development (without versioning)
```bash
# Serve documentation locally for development
mkdocs serve
```
Open http://127.0.0.1:8000

### Build documentation
```bash
# Build to site/ directory
mkdocs build

# Build to custom directory
mkdocs build -d /path/to/output
```

## Preview specific docs

### Preview User docs
```bash
cd user-guide
mkdocs serve
```
Open http://127.0.0.1:8000

### Preview Dev docs
```bash
cd developer-guide
mkdocs serve
```
Open http://127.0.0.1:8000
