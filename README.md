# Overview

## What Is MkDocs?

MkDocs is a **fast**, **simple** and **downright gorgeous** static site generator that's geared towards building project documentation.
More info: https://www.mkdocs.org/

## Prerequisites

- **Python 3.10 or newer.** `platform/developer-guide` depends on `mkdocs-awesome-nav` v3, which requires Python ≥ 3.10.
  - macOS: `brew install python@3.10`
  - Ubuntu: `apt-get install python3.10 python3.10-venv`
  - Windows: install from https://www.python.org/downloads/

## Setup

Create a virtualenv with Python 3.10+ and install pinned dependencies:

```bash
# macOS / Linux
python3.10 -m venv .venv
source .venv/bin/activate
pip install -r requirements-docs.txt
```

```powershell
# Windows
py -3.10 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-docs.txt
```

`requirements-docs.txt` pins every plugin to the version known to work with the current overrides (notably `mkdocs-material==9.5.27` and `mkdocs-awesome-nav==3.3.0`).

## Quick start

After activating the venv:

```bash
mkdocs serve -f platform/developer-guide/mkdocs.yml
# open http://127.0.0.1:8000
```

For other guides, swap the `-f` path (`platform/user-guide/mkdocs.yml`, `storefront/developer-guide/mkdocs.yml`, etc.).

### Build the full multi-site

```bash
./build.sh    # builds every sub-site into ./site
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
