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

This project uses [Mike](https://github.com/jimporter/mike) for documentation versioning. Mike makes it easy to deploy multiple versions of your MkDocs documentation with a version selector.

### View existing versions
```bash
mike list
```

### Serve documentation with version selector
```bash
mike serve
```
Open http://localhost:8000 - you'll see the version selector in the top right corner.

### Deploy a new version
```bash
# Deploy version 3.2025-S13
mike deploy 3.2025-S13

# Deploy version and update the 'latest' alias
mike deploy --update-aliases 3.2025-S13 latest

# Set default version (for root URL redirect)
mike set-default latest
```

### How Mike Works

Mike stores all versions in the `gh-pages` branch as static files. The version selector is included automatically.

**Important:** 
- `mike serve` - only for local preview (doesn't create files)
- `mike deploy` - creates/updates version in gh-pages branch
- Version selector requires a web server (won't work with `file://`)

### Export for Deployment

To get all versioned documentation with selector for deployment:

```bash
# Method 1: Use the export script
./export-versioned-docs.sh

# Method 2: Manual export
git checkout gh-pages
cp -r . ../site-export
git checkout -
mv ../site-export site
```

After export, the `site/` folder will contain:
- All versions (latest/, 3.2025-S12/, etc.)
- versions.json (version list)
- index.html (redirect to default version)
- Version selector (built into each version)

Deploy the entire `site/` folder to your web server.

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
