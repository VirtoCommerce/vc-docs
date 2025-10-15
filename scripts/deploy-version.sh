#!/bin/bash

# Deploy specific version for a documentation subsite using Mike
#
# Usage:
#   ./scripts/deploy-version.sh marketplace/developer-guide 1.0 latest
#   ./scripts/deploy-version.sh platform/user-guide 2.5
#   ./scripts/deploy-version.sh marketplace/developer-guide 1.0 latest --set-default
#
# Parameters:
#   $1: SubsitePath - Path to subsite (e.g., "marketplace/developer-guide")
#   $2: Version - Version number (e.g., "1.0", "2.5", "3.2025-S13")
#   $3: Alias (optional) - Alias (e.g., "latest", "stable")
#   --set-default: Set this version as default
#   --update-aliases: Update aliases

set -e  # Exit on error

# Color output functions
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
GRAY='\033[0;90m'
WHITE='\033[1;37m'
NC='\033[0m' # No Color

print_success() {
    echo -e "${GREEN}$1${NC}"
}

print_info() {
    echo -e "${CYAN}$1${NC}"
}

print_warning() {
    echo -e "${YELLOW}$1${NC}"
}

print_error() {
    echo -e "${RED}$1${NC}"
}

# Validate arguments
if [ $# -lt 2 ]; then
    print_error "Error: Missing required arguments"
    echo ""
    echo "Usage: $0 <subsite-path> <version> [alias] [--set-default] [--update-aliases]"
    echo ""
    echo "Examples:"
    echo "  $0 marketplace/developer-guide 1.0 latest"
    echo "  $0 platform/user-guide 2.5"
    echo "  $0 marketplace/developer-guide 1.0 latest --set-default"
    echo ""
    echo "Valid subsite paths:"
    echo "  - marketplace/developer-guide"
    echo "  - marketplace/user-guide"
    echo "  - platform/developer-guide"
    echo "  - platform/user-guide"
    echo "  - platform/deployment-on-cloud"
    echo "  - storefront/developer-guide"
    echo "  - storefront/user-guide"
    exit 1
fi

SUBSITE_PATH="$1"
VERSION="$2"
ALIAS="${3:-}"
SET_DEFAULT=false
UPDATE_ALIASES=false

# Parse additional flags
shift 2
while [[ $# -gt 0 ]]; do
    case $1 in
        --set-default)
            SET_DEFAULT=true
            shift
            ;;
        --update-aliases)
            UPDATE_ALIASES=true
            shift
            ;;
        *)
            if [ -z "$ALIAS" ]; then
                ALIAS="$1"
            fi
            shift
            ;;
    esac
done

# Validate subsite path
VALID_SUBSITES=(
    "marketplace/developer-guide"
    "marketplace/user-guide"
    "platform/developer-guide"
    "platform/user-guide"
    "platform/deployment-on-cloud"
    "storefront/developer-guide"
    "storefront/user-guide"
)

is_valid=false
for valid in "${VALID_SUBSITES[@]}"; do
    if [ "$SUBSITE_PATH" == "$valid" ]; then
        is_valid=true
        break
    fi
done

if [ "$is_valid" == false ]; then
    print_error "Error: Invalid subsite path: $SUBSITE_PATH"
    echo "Valid paths: ${VALID_SUBSITES[*]}"
    exit 1
fi

# Validate mike is installed
print_info "Checking if mike is installed..."
if ! command -v mike &> /dev/null; then
    print_error "Error: mike is not installed. Please install it using: pip install mike"
    exit 1
fi
print_success "✓ Mike is installed"

# Validate mkdocs.yml exists for subsite
CONFIG_PATH="$SUBSITE_PATH/mkdocs.yml"
if [ ! -f "$CONFIG_PATH" ]; then
    print_error "Error: Configuration file not found at $CONFIG_PATH"
    exit 1
fi
print_success "✓ Configuration file found: $CONFIG_PATH"

# Build the mike deploy command
MIKE_CMD="mike deploy -F $CONFIG_PATH --deploy-prefix $SUBSITE_PATH $VERSION"

# Add alias if provided
if [ -n "$ALIAS" ]; then
    MIKE_CMD="$MIKE_CMD $ALIAS"
fi

# Add update aliases flag if set
if [ "$UPDATE_ALIASES" == true ]; then
    MIKE_CMD="$MIKE_CMD --update-aliases"
fi

# Execute mike deploy
print_info "\nDeploying version $VERSION for $SUBSITE_PATH..."
echo -e "${GRAY}Command: $MIKE_CMD${NC}"
echo ""

if eval $MIKE_CMD; then
    print_success "\n✓ Successfully deployed version $VERSION for $SUBSITE_PATH"

    # Set as default if requested
    if [ "$SET_DEFAULT" == true ]; then
        print_info "\nSetting version $VERSION as default..."
        SET_DEFAULT_CMD="mike set-default -F $CONFIG_PATH --deploy-prefix $SUBSITE_PATH $VERSION"

        if eval $SET_DEFAULT_CMD; then
            print_success "✓ Successfully set version $VERSION as default"
        else
            print_error "✗ Failed to set default version"
            exit 1
        fi
    fi

    print_info "\nDeployment Summary:"
    echo -e "${WHITE}  Subsite:  $SUBSITE_PATH${NC}"
    echo -e "${WHITE}  Version:  $VERSION${NC}"
    if [ -n "$ALIAS" ]; then
        echo -e "${WHITE}  Alias:    $ALIAS${NC}"
    fi
    if [ "$SET_DEFAULT" == true ]; then
        echo -e "${WHITE}  Default:  Yes${NC}"
    fi
    echo ""
    print_info "To test locally:"
    echo -e "${GRAY}  1. Development (without versions): cd $SUBSITE_PATH && mkdocs serve${NC}"
    echo -e "${GRAY}  2. View deployed versions: git checkout gh-pages && python3 -m http.server 8000${NC}"
    echo -e "${GRAY}     Then open: http://localhost:8000/$SUBSITE_PATH/${NC}"
    echo ""
else
    print_error "\n✗ Failed to deploy version $VERSION for $SUBSITE_PATH"
    exit 1
fi

