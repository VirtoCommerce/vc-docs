#!/bin/bash

# List all versions for documentation subsites
#
# Usage:
#   ./scripts/list-versions.sh
#   ./scripts/list-versions.sh marketplace/developer-guide

set -e  # Exit on error

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
GRAY='\033[0;90m'
NC='\033[0m' # No Color

print_success() {
    echo -e "${GREEN}$1${NC}"
}

print_info() {
    echo -e "${CYAN}$1${NC}"
}

print_error() {
    echo -e "${RED}$1${NC}"
}

print_header() {
    local header="$1"
    local line=$(printf '=%.0s' $(seq 1 ${#header}))
    echo -e "\n${YELLOW}${header}${NC}"
    echo -e "${YELLOW}${line}${NC}"
}

# Validate mike is installed
if ! command -v mike &> /dev/null; then
    print_error "Error: mike is not installed. Please install it using: pip install mike"
    exit 1
fi

# Define all subsites
SUBSITES=(
    "marketplace/developer-guide"
    "marketplace/user-guide"
    "platform/developer-guide"
    "platform/user-guide"
    "platform/deployment-on-cloud"
    "storefront/developer-guide"
    "storefront/user-guide"
)

# If specific subsite is requested, use only that one
if [ $# -gt 0 ]; then
    SUBSITES=("$1")
fi

print_info "\nListing versions for documentation subsites..."
echo ""

for subsite in "${SUBSITES[@]}"; do
    CONFIG_PATH="$subsite/mkdocs.yml"

    # Check if config exists
    if [ ! -f "$CONFIG_PATH" ]; then
        print_error "Warning: Configuration not found at $CONFIG_PATH - skipping"
        continue
    fi

    print_header "$subsite"

    # Get versions using mike list
    MIKE_CMD="mike list -F $CONFIG_PATH --deploy-prefix $subsite"

    if output=$($MIKE_CMD 2>&1); then
        if [ -n "$output" ]; then
            echo "$output"
        else
            echo -e "${GRAY}  No versions deployed yet${NC}"
        fi
    else
        echo -e "${GRAY}  No versions deployed yet${NC}"
    fi
done

echo ""
print_info "To deploy a new version, use:"
echo -e "${GRAY}  ./scripts/deploy-version.sh <subsite-path> <version> [alias]${NC}"
echo ""

