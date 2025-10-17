#!/bin/bash

# Quick test script for local documentation

echo "=== Documentation System Test ==="

# Test 1: Check version.json
echo "1. Checking version.json..."
if [ -f "version.json" ]; then
    VERSION=$(python3 -c "import json; data=json.load(open('version.json')); print(data.get('version', 'unknown'))")
    ALIAS=$(python3 -c "import json; data=json.load(open('version.json')); print(data.get('alias', 'none'))")
    echo "   ✓ Found version.json: $VERSION ($ALIAS)"
else
    echo "   ✗ version.json not found!"
fi

# Test 2: Check gh-pages branch
echo "2. Checking gh-pages branch..."
if git show-ref --verify --quiet refs/heads/gh-pages; then
    echo "   ✓ gh-pages branch exists locally"
elif git show-ref --verify --quiet refs/remotes/origin/gh-pages; then
    echo "   ✓ gh-pages branch exists on remote"
else
    echo "   ✗ gh-pages branch not found!"
fi

# Test 3: Check deployed versions
echo "3. Checking deployed versions..."
./list-versions.sh | grep -A 5 "Version"

# Test 4: Check if ports are available
echo "4. Checking if port 8000 is available..."
if lsof -i :8000 > /dev/null 2>&1; then
    echo "   ⚠ Port 8000 is in use. You may need to stop the existing server."
    echo "   Run: pkill -f 'python.*http.server'"
else
    echo "   ✓ Port 8000 is available"
fi

# Test 5: Check required tools
echo "5. Checking required tools..."
if command -v python3 &> /dev/null; then
    echo "   ✓ Python3 is installed"
else
    echo "   ✗ Python3 not found!"
fi

if command -v mkdocs &> /dev/null; then
    echo "   ✓ MkDocs is installed"
else
    echo "   ✗ MkDocs not found!"
fi

if command -v git &> /dev/null; then
    echo "   ✓ Git is installed"
else
    echo "   ✗ Git not found!"
fi

echo ""
echo "=== Test Complete ==="
echo ""
echo "To start local preview:"
echo "  ./serve-local.sh"
echo ""
echo "To deploy new version:"
echo "  ./deploy-auto-version.sh"
echo ""
echo "Access your documentation at:"
echo "  http://localhost:8000/v4.800/"
echo "  http://localhost:8000/latest/"