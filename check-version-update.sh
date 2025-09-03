#!/bin/bash

# Script to check deployment configuration
# Returns 0 if deployment should happen, 1 if disabled

set -e

CONFIG_FILE="version-config.json"
LAST_DEPLOYED_FILE=".last-deployed-version"

if [ ! -f "$CONFIG_FILE" ]; then
    echo "❌ Error: $CONFIG_FILE not found"
    exit 1
fi

# Extract current version from config
CURRENT_VERSION=$(jq -r '.version' "$CONFIG_FILE")
DEPLOY_ON_PUSH=$(jq -r '.deployOnPush' "$CONFIG_FILE")

# Check if deployment is enabled
if [ "$DEPLOY_ON_PUSH" != "true" ]; then
    echo "🚫 Deployment disabled in $CONFIG_FILE (deployOnPush: false)"
    exit 1
fi

# Check if this is a new version or update to existing
if [ -f "$LAST_DEPLOYED_FILE" ]; then
    LAST_VERSION=$(cat "$LAST_DEPLOYED_FILE")
    if [ "$CURRENT_VERSION" = "$LAST_VERSION" ]; then
        echo "🔄 Version $CURRENT_VERSION - updating existing version"
        echo "new_version=false" >> $GITHUB_OUTPUT
    else
        echo "✅ New version $CURRENT_VERSION ready for deployment"
        echo "new_version=true" >> $GITHUB_OUTPUT
    fi
else
    echo "✅ First deployment of version $CURRENT_VERSION"
    echo "new_version=true" >> $GITHUB_OUTPUT
fi

echo "📝 Config details:"
jq '.' "$CONFIG_FILE"

exit 0