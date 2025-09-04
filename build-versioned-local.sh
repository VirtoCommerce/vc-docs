#!/bin/bash

# Script for building versioned documentation with mike locally
# Usage: ./build-versioned-local.sh [version] [alias]
# If no version provided, reads from VERSION file or version.json

set -e  # Exit on any error

# Function to get version from local files
get_local_version() {
    if [ -f "version-utils.py" ]; then
        python3 version-utils.py get-version 2>/dev/null || echo "dev"
    elif [ -f "VERSION" ]; then
        cat VERSION 2>/dev/null || echo "dev"
    else
        echo "dev"
    fi
}

# Function to get deployment parameters
get_deploy_params() {
    if [ -f "version-utils.py" ]; then
        python3 version-utils.py get-deploy-params 2>/dev/null
    fi
}

# Determine version and alias
if [ -n "$1" ]; then
    VERSION="$1"
    ALIAS="$2"
    echo "Using provided version: $VERSION"
else
    echo "Reading version from local configuration..."
    
    # Get deployment parameters
    DEPLOY_PARAMS=$(get_deploy_params)
    
    if [ -n "$DEPLOY_PARAMS" ]; then
        VERSION=$(echo "$DEPLOY_PARAMS" | python3 -c "import sys, json; data = json.load(sys.stdin); print(data.get('version', 'dev'))")
        ALIAS=$(echo "$DEPLOY_PARAMS" | python3 -c "import sys, json; data = json.load(sys.stdin); print(data.get('alias', ''))")
        UPDATE_EXISTING=$(echo "$DEPLOY_PARAMS" | python3 -c "import sys, json; data = json.load(sys.stdin); print(data.get('update_existing', False))")
        
        if [ "$UPDATE_EXISTING" = "True" ]; then
            echo "Will update existing version: $VERSION"
        else
            echo "Will create new version: $VERSION"
        fi
    else
        VERSION=$(get_local_version)
        ALIAS=""
        echo "Fallback to basic version detection: $VERSION"
    fi
fi

BRANCH="gh-pages"

echo "=== Building versioned documentation ==="
echo "Version: $VERSION"
if [ -n "$ALIAS" ]; then
    echo "Alias: $ALIAS"
fi
echo "Target branch: $BRANCH"
echo "============================================"

# Install dependencies if requirements.txt exists
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies..."
    pip3 install -r requirements.txt
fi

# Configure git for mike
if [ -z "$(git config --get user.name)" ]; then
    git config --global user.name "CI Bot"
    git config --global user.email "ci@virtocommerce.com"
fi

# Initialize gh-pages branch if it doesn't exist
if ! git show-ref --quiet refs/heads/$BRANCH; then
    echo "Creating $BRANCH branch..."
    git checkout --orphan $BRANCH
    git rm -rf .
    git commit --allow-empty -m "Initial commit for documentation versions"
    git push origin $BRANCH
    git checkout -
fi

# Build all documentation components first
echo "Building documentation components..."

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
echo "Deploying documentation with mike..."
if [ -n "$ALIAS" ]; then
    mike deploy --push --branch $BRANCH $VERSION $ALIAS
    if [ "$ALIAS" = "latest" ]; then
        mike set-default --push --branch $BRANCH latest
    fi
else
    mike deploy --push --branch $BRANCH $VERSION
fi

# List all versions
echo "Current versions:"
mike list --branch $BRANCH

echo "Documentation deployment completed!"
echo "Available at: https://docs.virtocommerce.org/$VERSION/"
if [ -n "$ALIAS" ]; then
    echo "Also available at: https://docs.virtocommerce.org/$ALIAS/"
fi