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
