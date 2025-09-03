#!/bin/bash

# Script to serve versioned documentation locally using mike
# Usage: ./serve-versioned.sh [port]

PORT=${1:-8000}

echo "🌐 Starting versioned documentation server on port $PORT..."
echo "Available versions:"
mike list

echo ""
echo "📖 Serving documentation at: http://localhost:$PORT"
echo "Press Ctrl+C to stop the server"

mike serve --dev-addr localhost:$PORT