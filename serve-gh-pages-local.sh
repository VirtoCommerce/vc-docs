#!/bin/bash

# Serve gh-pages branch locally without Mike

echo "=== Serving gh-pages branch locally ==="

# Check out gh-pages to temporary directory
TEMP_DIR="gh-pages-preview"

# Clean up if exists
rm -rf $TEMP_DIR

# Clone gh-pages branch
echo "Checking out gh-pages branch..."
git worktree add $TEMP_DIR gh-pages

# Start Python HTTP server
echo "Starting HTTP server..."
echo "Documentation will be available at http://localhost:8080"
echo "Press Ctrl+C to stop the server"

cd $TEMP_DIR
python3 -m http.server 8080

# Cleanup will happen when you Ctrl+C
trap "cd ..; git worktree remove $TEMP_DIR --force" EXIT