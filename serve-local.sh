#!/bin/bash

# Serve custom versioned documentation locally

echo "=== Serving Custom Versioned Documentation Locally ==="

# Check out gh-pages to temporary directory
TEMP_DIR="gh-pages-preview"

# Clean up if exists
rm -rf $TEMP_DIR

# Create worktree from gh-pages branch
echo "Checking out gh-pages branch..."
if ! git worktree add $TEMP_DIR gh-pages 2>/dev/null; then
    echo "Failed to create worktree. Trying to fetch gh-pages first..."
    git fetch origin gh-pages
    git worktree add $TEMP_DIR origin/gh-pages
fi

# Check what's available
echo ""
echo "Available versions:"
ls -la $TEMP_DIR | grep "^d" | grep -v "^\.$\|^\.git\|assets" | awk '{print "  - " $9}' || echo "  No versions found"

# Start Python HTTP server
echo ""
echo "Starting HTTP server..."
echo "Documentation will be available at:"
echo "  http://localhost:8000"
echo ""
echo "You can access specific versions:"
echo "  http://localhost:8000/v4.800/"
echo "  http://localhost:8000/latest/"
echo ""
echo "Press Ctrl+C to stop the server"

cd $TEMP_DIR
python3 -m http.server 8000

# Cleanup will happen when you Ctrl+C
trap 'cd ..; git worktree remove $TEMP_DIR --force 2>/dev/null || true' EXIT