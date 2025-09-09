#!/bin/bash

# Script for building versioned documentation with mike locally
# Usage: ./build-versioned-local.sh [version] [alias]
# If no version provided, reads from VERSION file or version.json

set -e  # Exit on any error

# Function to get version from local files
get_local_version() {
    if [ -f "version.json" ]; then
        python3 -c "import json; data=json.load(open('version.json')); print(data.get('version', 'dev'))" 2>/dev/null || echo "dev"
    elif [ -f "version-utils.py" ]; then
        python3 version-utils.py get-version 2>/dev/null || echo "dev"
    elif [ -f "VERSION" ]; then
        cat VERSION 2>/dev/null || echo "dev"
    else
        echo "dev"
    fi
}

# Function to get alias from local files  
get_local_alias() {
    if [ -f "version.json" ]; then
        python3 -c "import json; data=json.load(open('version.json')); print(data.get('alias', ''))" 2>/dev/null || echo ""
    else
        echo ""
    fi
}

# Function to get deployment parameters
get_deploy_params() {
    if [ -f "version-utils.py" ]; then
        python3 version-utils.py get-deploy-params 2>/dev/null || echo ""
    else
        echo ""
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
    
    if [ -n "$DEPLOY_PARAMS" ] && [ "$DEPLOY_PARAMS" != "" ]; then
        # Validate JSON before parsing
        echo "$DEPLOY_PARAMS" | python3 -c "import sys, json; json.load(sys.stdin)" 2>/dev/null
        if [ $? -eq 0 ]; then
            VERSION=$(echo "$DEPLOY_PARAMS" | python3 -c "import sys, json; data = json.load(sys.stdin); print(data.get('version', 'dev'))")
            ALIAS=$(echo "$DEPLOY_PARAMS" | python3 -c "import sys, json; data = json.load(sys.stdin); print(data.get('alias', ''))")
            UPDATE_EXISTING=$(echo "$DEPLOY_PARAMS" | python3 -c "import sys, json; data = json.load(sys.stdin); print(data.get('update_existing', False))")
        else
            echo "Invalid JSON from get-deploy-params, falling back to basic detection"
            VERSION=$(get_local_version)
            ALIAS=""
            UPDATE_EXISTING="False"
        fi
        
        if [ "$UPDATE_EXISTING" = "True" ]; then
            echo "Will update existing version: $VERSION"
        else
            echo "Will create new version: $VERSION"
        fi
    else
        VERSION=$(get_local_version)
        ALIAS=$(get_local_alias)
        echo "Fallback to basic version detection: $VERSION"
        if [ -n "$ALIAS" ]; then
            echo "Detected alias: $ALIAS"
        fi
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

# Deploy with Mike (builds and deploys unified documentation)
echo "Deploying unified documentation with Mike..."

# Ensure mike is installed
pip3 install mike

if [ -n "$ALIAS" ]; then
    mike deploy --push --branch $BRANCH --update-aliases $VERSION $ALIAS
    echo "Setting $ALIAS as default version..."
    mike set-default --push --branch $BRANCH $ALIAS
else
    mike deploy --push --branch $BRANCH $VERSION
    echo "Setting $VERSION as default version..."  
    mike set-default --push --branch $BRANCH $VERSION
fi

# List all versions
echo "Current versions:"
mike list --branch $BRANCH

echo "Documentation deployment completed!"
echo "Available at: https://docs.virtocommerce.org/$VERSION/"
if [ -n "$ALIAS" ]; then
    echo "Also available at: https://docs.virtocommerce.org/$ALIAS/"
fi