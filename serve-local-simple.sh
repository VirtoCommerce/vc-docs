#!/bin/bash

# Simple local server for versioned documentation

echo "=== Simple Local Documentation Server ==="

# Create temporary directory and clone gh-pages
TEMP_DIR="gh-pages-temp-$(date +%s)"

echo "Creating temporary directory: $TEMP_DIR"
mkdir -p $TEMP_DIR

# Clone gh-pages branch content
echo "Fetching gh-pages content..."
if git show-ref --verify --quiet refs/heads/gh-pages; then
    # Use local gh-pages branch
    echo "Using local gh-pages branch..."
    git archive gh-pages | tar -x -C $TEMP_DIR
elif git show-ref --verify --quiet refs/remotes/origin/gh-pages; then
    # Fetch and use remote gh-pages
    echo "Fetching remote gh-pages branch..."
    git fetch origin gh-pages:gh-pages 2>/dev/null
    git archive gh-pages | tar -x -C $TEMP_DIR
else
    echo "Error: gh-pages branch not found!"
    echo "Please run a deployment first: ./deploy-auto-version.sh"
    exit 1
fi

# Check what we have
echo ""
echo "Available versions in $TEMP_DIR:"
ls -la $TEMP_DIR | grep "^d" | grep -v "^\.$\|^\.\.$ \|assets" | awk '{print "  - " $9}' || echo "  No versions found"

# Find available port
PORT=8000
while lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null 2>&1; do
    echo "Port $PORT is in use, trying $((PORT+1))..."
    PORT=$((PORT+1))
    if [ $PORT -gt 8010 ]; then
        echo "Error: No available ports found in range 8000-8010"
        exit 1
    fi
done

# Start server
echo ""
echo "Starting HTTP server on port $PORT..."
echo "Documentation will be available at:"
echo "  http://localhost:$PORT/"
echo "  http://localhost:$PORT/v4.800/"
echo "  http://localhost:$PORT/latest/"
echo ""
echo "Press Ctrl+C to stop the server and cleanup"

# Cleanup function
cleanup() {
    echo ""
    echo "Stopping server and cleaning up..."
    rm -rf $TEMP_DIR
    echo "Cleanup complete"
}

# Set trap for cleanup
trap cleanup EXIT INT TERM

# Start server
cd $TEMP_DIR
python3 -m http.server $PORT