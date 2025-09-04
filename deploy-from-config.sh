#!/bin/bash

# Deploy documentation based on version-config.json
# This script reads the configuration and deploys accordingly
# Usage: ./deploy-from-config.sh [--push] [--new-version]

set -e

CONFIG_FILE="version-config.json"
LAST_DEPLOYED_FILE=".last-deployed-version"

if [ ! -f "$CONFIG_FILE" ]; then
    echo "❌ Error: $CONFIG_FILE not found"
    exit 1
fi

# Read configuration
VERSION=$(jq -r '.version' "$CONFIG_FILE")
ALIAS=$(jq -r '.alias' "$CONFIG_FILE")
SET_DEFAULT=$(jq -r '.setDefault' "$CONFIG_FILE")
DESCRIPTION=$(jq -r '.description' "$CONFIG_FILE")

# Parse flags
PUSH_FLAG=""
NEW_VERSION="true"

for arg in "$@"; do
    case $arg in
        --push)
            PUSH_FLAG="--push"
            echo "🔄 Will push to remote repository"
            ;;
        --update-existing)
            NEW_VERSION="false"
            ;;
    esac
done

echo "🚀 Deploying documentation from configuration..."
echo "📋 Version: $VERSION"
echo "📋 Alias: $ALIAS"
echo "📋 Set as default: $SET_DEFAULT"
echo "📋 Description: $DESCRIPTION"
echo "📋 New version: $NEW_VERSION"

# Deploy using mike
if [ "$ALIAS" != "null" ] && [ "$ALIAS" != "" ]; then
    if [ "$NEW_VERSION" = "true" ]; then
        echo "📦 Deploying NEW version $VERSION with alias $ALIAS..."
        mike deploy $PUSH_FLAG --update-aliases "$VERSION" "$ALIAS"
    else
        echo "🔄 Updating EXISTING version $VERSION with alias $ALIAS..."
        mike deploy $PUSH_FLAG --update-aliases "$VERSION" "$ALIAS"
    fi
else
    if [ "$NEW_VERSION" = "true" ]; then
        echo "📦 Deploying NEW version $VERSION without alias..."
        mike deploy $PUSH_FLAG "$VERSION"
    else
        echo "🔄 Updating EXISTING version $VERSION without alias..."
        mike deploy $PUSH_FLAG "$VERSION"
    fi
fi

# Set as default if requested (only for new versions or if explicitly requested)
if [ "$SET_DEFAULT" = "true" ]; then
    echo "🎯 Setting $VERSION as default version..."
    mike set-default $PUSH_FLAG "$VERSION"
fi

# Record the deployed version
echo "$VERSION" > "$LAST_DEPLOYED_FILE"

if [ "$NEW_VERSION" = "true" ]; then
    echo "✅ Successfully deployed NEW version $VERSION"
else
    echo "✅ Successfully updated EXISTING version $VERSION"
fi

# Show current versions
echo ""
echo "📚 All available versions:"
mike list