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

### Quick Start - Interactive CLI

Launch the interactive version manager:

```bash
# All platforms (Linux/Mac/Windows)
python3 version-manager.py

# Or on Windows
python version-manager.py
```

You'll see an interactive menu where you can:
- Deploy versions to one or all subsites (with automatic push to GitHub)
- Delete versions
- List all versions
- Set default versions
- Add aliases

Simply choose an option and follow the prompts!

**Note:** When deploying, you can choose to automatically push changes to GitHub's `gh-pages` branch.

### Available Subsites

- `marketplace/developer-guide`
- `marketplace/user-guide`
- `platform/developer-guide`
- `platform/user-guide`
- `platform/deployment-on-cloud`
- `storefront/developer-guide`
- `storefront/user-guide`

### Test Locally

```bash
# View deployed versions
git checkout gh-pages
python3 -m http.server 8000
# Open http://localhost:8000/marketplace/developer-guide/

# Development mode (no versions)
cd marketplace/developer-guide
mkdocs serve
```

### Documentation

- **[QUICKSTART.md](QUICKSTART.md)** - Simple commands and common workflows
- **[VERSIONING.md](VERSIONING.md)** - Complete versioning documentation
- **Legacy scripts** in `scripts/` directory (deprecated, use `version.sh` instead)

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
