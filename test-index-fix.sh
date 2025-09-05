#!/bin/bash

# Test script to verify index file fix for intermediate directories

set -e

echo "=========================================="
echo "=== Testing Index File Fix ==="
echo "=========================================="

# Read current version
VERSION=$(cat VERSION | tr -d '[:space:]')
echo "Testing version: $VERSION"

# Simple build test to check if index files are created
echo "Building documentation with index fix..."

# Build main site
mkdocs build -d ./site --clean

# Build using the corrected approach
echo "Building platform with correct structure..."
mkdocs build -f platform/mkdocs.yml -d ./site/platform --clean

if [ -f "site/platform/index.html" ]; then
    echo "✓ Platform index.html created"
    echo "  Checking content for custom template..."
    if grep -q "platform-home.html\|Platform" site/platform/index.html; then
        echo "  ✓ Platform homepage contains expected content"
    else
        echo "  ✗ Platform homepage missing custom content"
    fi
else
    echo "✗ Platform index.html not created"
fi

echo "Building storefront with correct structure..."
mkdocs build -f storefront/mkdocs.yml -d ./site/storefront --clean

if [ -f "site/storefront/index.html" ]; then
    echo "✓ Storefront index.html created"
else
    echo "✗ Storefront index.html not created"
fi

echo "Building marketplace with correct structure..."
mkdocs build -f marketplace/mkdocs.yml -d ./site/marketplace --clean

if [ -f "site/marketplace/index.html" ]; then
    echo "✓ Marketplace index.html created"
else
    echo "✗ Marketplace index.html not created"
fi

# Check what we have
echo ""
echo "Built structure:"
ls -la site/ | grep "^d"
echo ""
echo "Platform directory:"
ls -la site/platform/ 2>/dev/null | head -5 || echo "Platform directory not found"
echo ""
echo "Storefront directory:"  
ls -la site/storefront/ 2>/dev/null | head -5 || echo "Storefront directory not found"
echo ""
echo "Marketplace directory:"
ls -la site/marketplace/ 2>/dev/null | head -5 || echo "Marketplace directory not found"

echo "=========================================="
echo "Test completed!"
echo "To test locally, run:"
echo "  python3 -m http.server 8000 --directory site"
echo "Then test these URLs:"
echo "  http://localhost:8000/"
echo "  http://localhost:8000/platform/"
echo "  http://localhost:8000/storefront/" 
echo "  http://localhost:8000/marketplace/"
echo "=========================================="