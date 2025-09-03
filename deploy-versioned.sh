#!/bin/bash

# Deployment script for versioned documentation using mike
# Usage: ./deploy-versioned.sh <version> [alias]
# Example: ./deploy-versioned.sh 3.800 latest

set -e  # Exit on any error

VERSION=$1
ALIAS=${2:-""}

if [ -z "$VERSION" ]; then
    echo "Error: Version is required"
    echo "Usage: $0 <version> [alias]"
    echo "Example: $0 3.800 latest"
    exit 1
fi

echo "Deploying documentation version: $VERSION"
if [ ! -z "$ALIAS" ]; then
    echo "With alias: $ALIAS"
fi

# Deploy the main documentation portal
echo "🚀 Deploying main documentation portal..."
if [ ! -z "$ALIAS" ]; then
    mike deploy --push --update-aliases $VERSION $ALIAS
else
    mike deploy --push $VERSION
fi

echo "✅ Successfully deployed documentation version $VERSION"
echo ""
echo "📚 Available versions:"
mike list

echo ""
echo "🌐 To view the documentation, visit the deployed site or serve locally with:"
echo "  mike serve"