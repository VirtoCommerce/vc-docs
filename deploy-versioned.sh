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

# If auto mode, read from version.json
if [ "$VERSION" = "auto" ]; then
    if [ -f "version.json" ]; then
        VERSION=$(python3 -c "import json; data=json.load(open('version.json')); print(data.get('version', 'dev'))")
        echo "Auto-detected version from version.json: $VERSION"
    elif [ -f "VERSION" ]; then
        VERSION=$(cat VERSION 2>/dev/null || echo "dev")
        echo "Version from VERSION file: $VERSION"
    else
        VERSION="dev"
        echo "Using default version: $VERSION"
    fi
fi

if [ "$ALIAS" = "auto" ]; then
    if [ -f "version.json" ]; then
        ALIAS=$(python3 -c "import json; data=json.load(open('version.json')); print(data.get('alias', ''))")
        echo "Auto-detected alias from version.json: $ALIAS"
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

# Deploy with Mike (proper versioned deployment)
echo "Deploying documentation with Mike..."

# Ensure Mike is installed
pip3 install mike

# Deploy main documentation (unified site)
echo "Deploying main documentation..."
if [ -n "$ALIAS" ]; then
    mike deploy --push --branch gh-pages --update-aliases $VERSION $ALIAS
    echo "Setting $ALIAS as default version..."
    mike set-default --push --branch gh-pages $ALIAS
else
    mike deploy --push --branch gh-pages $VERSION
    echo "Setting $VERSION as default version..."
    mike set-default --push --branch gh-pages $VERSION
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