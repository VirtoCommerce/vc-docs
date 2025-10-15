#!/bin/bash

# Build and deploy all versioned documentation subsites using Mike
#
# This script is for production deployment with versioning.
# For development builds without versioning, use the root build.ps1 script.
#
# Usage:
#   ./scripts/build-versioned.sh 3.2025-S13
#   ./scripts/build-versioned.sh 3.2025-S13 --set-latest
#   ./scripts/build-versioned.sh 3.2025-S13 --set-latest --set-default
#   ./scripts/build-versioned.sh 3.2025-S13 --subsites-only
#
# Parameters:
#   $1: Version number (e.g., "3.2025-S13", "1.0", "2.5")
#   --set-latest: Set this version as 'latest' alias
#   --set-default: Set this version as default version
#   --subsites-only: Deploy only subsites (skip root and intermediate sites)

set -e  # Exit on error

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BLUE='\033[0;34m'
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

print_step() {
    echo -e "\n${BLUE}═══════════════════════════════════════════════════${NC}"
    echo -e "${WHITE}  $1${NC}"
    echo -e "${BLUE}═══════════════════════════════════════════════════${NC}"
}

# Validate arguments
if [ $# -lt 1 ]; then
    print_error "Error: Missing version number"
    echo ""
    echo "Usage: $0 <version> [--set-latest] [--set-default] [--subsites-only]"
    echo ""
    echo "Examples:"
    echo "  $0 3.2025-S13"
    echo "  $0 3.2025-S13 --set-latest"
    echo "  $0 3.2025-S13 --set-latest --set-default"
    exit 1
fi

VERSION="$1"
SET_AS_LATEST=false
SET_AS_DEFAULT=false
SUBSITES_ONLY=false

# Parse flags
shift
while [[ $# -gt 0 ]]; do
    case $1 in
        --set-latest)
            SET_AS_LATEST=true
            shift
            ;;
        --set-default)
            SET_AS_DEFAULT=true
            shift
            ;;
        --subsites-only)
            SUBSITES_ONLY=true
            shift
            ;;
        *)
            print_error "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Validate mike is installed
print_info "Validating prerequisites..."
if ! command -v mike &> /dev/null; then
    print_error "Error: mike is not installed. Please install it using: pip install mike"
    exit 1
fi

if ! command -v mkdocs &> /dev/null; then
    print_error "Error: mkdocs is not installed. Please install it using: pip install mkdocs-material"
    exit 1
fi

print_success "✓ Prerequisites validated"

# Define all versioned subsites
declare -A VERSIONED_SUBSITES=(
    ["marketplace/developer-guide"]="Marketplace Developer Guide"
    ["marketplace/user-guide"]="Marketplace User Guide"
    ["platform/developer-guide"]="Platform Developer Guide"
    ["platform/user-guide"]="Platform User Guide"
    ["platform/deployment-on-cloud"]="Platform Deployment on Cloud"
    ["storefront/developer-guide"]="Storefront Developer Guide"
    ["storefront/user-guide"]="Storefront User Guide"
)

# Counter for tracking
TOTAL_SUBSITES=${#VERSIONED_SUBSITES[@]}
DEPLOYED_COUNT=0
FAILED_COUNT=0
FAILED_SUBSITES=()

print_info "\nDeployment Plan:"
echo -e "${WHITE}  Version:        $VERSION${NC}"
echo -e "${WHITE}  Set as latest:  $SET_AS_LATEST${NC}"
echo -e "${WHITE}  Set as default: $SET_AS_DEFAULT${NC}"
echo -e "${WHITE}  Subsites:       $TOTAL_SUBSITES${NC}"
echo ""

# Build non-versioned sites first (if not subsites only)
if [ "$SUBSITES_ONLY" != true ]; then
    print_step "Building Non-Versioned Sites"

    print_info "Building root site..."
    if mkdocs build -d ./site; then
        print_success "✓ Root site built"
    else
        print_error "✗ Root site build failed"
    fi

    # Build intermediate sites (marketplace, platform, storefront)
    INTERMEDIATE_SITES=("storefront" "platform" "marketplace")

    for site in "${INTERMEDIATE_SITES[@]}"; do
        print_info "Building $site intermediate site..."
        if mkdocs build -f "$site/mkdocs.yml" -d "../site/$site"; then
            print_success "✓ $site intermediate site built"
        else
            print_error "✗ $site intermediate site build failed"
        fi
    done
fi

# Deploy versioned subsites
print_step "Deploying Versioned Subsites (Version: $VERSION)"

CURRENT=0
for path in "${!VERSIONED_SUBSITES[@]}"; do
    CURRENT=$((CURRENT + 1))
    name="${VERSIONED_SUBSITES[$path]}"
    config_path="$path/mkdocs.yml"

    print_info "\n[$CURRENT/$TOTAL_SUBSITES] Deploying: $name"
    echo -e "${WHITE}  Path: $path${NC}"

    # Check if config exists
    if [ ! -f "$config_path" ]; then
        print_error "  ✗ Configuration not found at $config_path"
        FAILED_COUNT=$((FAILED_COUNT + 1))
        FAILED_SUBSITES+=("$name")
        continue
    fi

    # Build mike command
    MIKE_CMD="mike deploy -F $config_path --deploy-prefix $path $VERSION"

    # Add 'latest' alias if requested
    if [ "$SET_AS_LATEST" == true ]; then
        MIKE_CMD="$MIKE_CMD latest --update-aliases"
    fi

    echo -e "${GRAY}  Command: $MIKE_CMD${NC}"

    # Execute deployment
    if eval $MIKE_CMD; then
        print_success "  ✓ Deployed successfully"
        DEPLOYED_COUNT=$((DEPLOYED_COUNT + 1))

        # Set as default if requested
        if [ "$SET_AS_DEFAULT" == true ]; then
            SET_DEFAULT_CMD="mike set-default -F $config_path --deploy-prefix $path $VERSION"
            if eval $SET_DEFAULT_CMD; then
                print_success "  ✓ Set as default"
            else
                print_warning "  ⚠ Failed to set as default"
            fi
        fi
    else
        print_error "  ✗ Deployment failed"
        FAILED_COUNT=$((FAILED_COUNT + 1))
        FAILED_SUBSITES+=("$name")
    fi
done

# Summary
print_step "Deployment Summary"

echo ""
echo -e "${WHITE}Total Subsites:     $TOTAL_SUBSITES${NC}"
print_success "Successfully Deployed: $DEPLOYED_COUNT"

if [ $FAILED_COUNT -gt 0 ]; then
    print_error "Failed:              $FAILED_COUNT"
    echo -e "\nFailed subsites:"
    for failed in "${FAILED_SUBSITES[@]}"; do
        print_error "  - $failed"
    done
fi

echo ""

if [ $DEPLOYED_COUNT -eq $TOTAL_SUBSITES ]; then
    print_success "═══════════════════════════════════════════════════"
    print_success "  ✓ All subsites deployed successfully!"
    print_success "═══════════════════════════════════════════════════"
    echo ""
    print_info "Next steps:"
    echo -e "${GRAY}  1. View versions: ./scripts/list-versions.sh${NC}"
    echo -e "${GRAY}  2. Test locally: git checkout gh-pages && python3 -m http.server 8000${NC}"
    echo -e "${GRAY}  3. Push to gh-pages: git push origin gh-pages${NC}"
    echo ""
    exit 0
else
    print_error "═══════════════════════════════════════════════════"
    print_error "  ✗ Some subsites failed to deploy"
    print_error "═══════════════════════════════════════════════════"
    echo ""
    exit 1
fi

