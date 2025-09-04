#!/bin/bash

# Script for deploying versioned documentation to production
# This script is used by CI/CD pipeline

set -e  # Exit on any error

VERSION=${1:-"auto"}
ALIAS=${2:-"auto"}
BUILD_MODE=${3:-"versioned"}

echo "=== Versioned Documentation Deployment ==="
echo "Version: $VERSION"
echo "Alias: $ALIAS"
echo "Build Mode: $BUILD_MODE"
echo "=========================================="

# If auto mode, read from local files
if [ "$VERSION" = "auto" ]; then
    if [ -f "version-utils.py" ]; then
        VERSION=$(python3 version-utils.py get-version 2>/dev/null || echo "dev")
        echo "Auto-detected version: $VERSION"
    elif [ -f "VERSION" ]; then
        VERSION=$(cat VERSION 2>/dev/null || echo "dev")
        echo "Version from VERSION file: $VERSION"
    else
        VERSION="dev"
        echo "Using default version: $VERSION"
    fi
fi

if [ "$ALIAS" = "auto" ]; then
    if [ -f "version-utils.py" ]; then
        CONFIG=$(python3 version-utils.py get-config 2>/dev/null)
        if [ -n "$CONFIG" ]; then
            ALIAS=$(echo "$CONFIG" | python3 -c "import sys, json; data = json.load(sys.stdin); print(data.get('alias', ''))")
            echo "Auto-detected alias: $ALIAS"
        fi
    fi
fi

# Configure git for mike if needed
if [ -z "$(git config --get user.name)" ]; then
    echo "Configuring git..."
    git config --global user.name "CI Bot"
    git config --global user.email "ci@virtocommerce.com"
fi

# Install dependencies
echo "Installing dependencies..."
pip3 install -r requirements.txt

# Build individual documentation sites
echo "Building individual documentation components..."

# Build main site
echo "Building main site..."
mkdocs build -d ./site

# Build storefront docs
echo "Building storefront documentation..."
mkdocs build -f storefront/mkdocs.yml -d ../site/storefront
mkdocs build -f storefront/user-guide/mkdocs.yml -d ../../site/storefront/user-guide
mkdocs build -f storefront/developer-guide/mkdocs.yml -d ../../site/storefront/developer-guide

# Build platform docs
echo "Building platform documentation..."
mkdocs build -f platform/mkdocs.yml -d ../site/platform
mkdocs build -f platform/user-guide/mkdocs.yml -d ../../site/platform/user-guide
mkdocs build -f platform/developer-guide/mkdocs.yml -d ../../site/platform/developer-guide
mkdocs build -f platform/deployment-on-cloud/mkdocs.yml -d ../../site/platform/deployment-on-cloud

# Build marketplace docs
echo "Building marketplace documentation..."
mkdocs build -f marketplace/mkdocs.yml -d ../site/marketplace
mkdocs build -f marketplace/user-guide/mkdocs.yml -d ../../site/marketplace/user-guide
mkdocs build -f marketplace/developer-guide/mkdocs.yml -d ../../site/marketplace/developer-guide

echo "All components built successfully!"

# Deploy with mike
echo "Deploying with mike..."
if [ -n "$ALIAS" ]; then
    mike deploy --push --branch gh-pages $VERSION $ALIAS
    if [ "$ALIAS" = "latest" ]; then
        mike set-default --push --branch gh-pages latest
    fi
else
    mike deploy --push --branch gh-pages $VERSION
fi

# List current versions
echo "Current deployed versions:"
mike list --branch gh-pages

echo "=== Deployment completed successfully! ==="
echo "Documentation available at:"
echo "- https://docs.virtocommerce.org/$VERSION/"
if [ -n "$ALIAS" ]; then
    echo "- https://docs.virtocommerce.org/$ALIAS/"
fi