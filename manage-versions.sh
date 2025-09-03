#!/bin/bash

# Script to manage documentation versions using mike
# Usage: ./manage-versions.sh <command> [args...]

set -e

COMMAND=$1

show_help() {
    echo "Documentation Version Management Script"
    echo ""
    echo "Usage: $0 <command> [args...]"
    echo ""
    echo "Commands:"
    echo "  list                          - List all available versions"
    echo "  deploy <version> [alias]      - Deploy a new version"
    echo "  alias <version> <alias>       - Set an alias for a version"
    echo "  delete <version>              - Delete a version"
    echo "  set-default <version>         - Set default version"
    echo "  serve [port]                  - Serve documentation locally"
    echo ""
    echo "Examples:"
    echo "  $0 list"
    echo "  $0 deploy 3.800 latest"
    echo "  $0 alias 3.800 stable"
    echo "  $0 set-default latest"
    echo "  $0 delete 3.700"
    echo "  $0 serve 8080"
}

case $COMMAND in
    "list")
        echo "📚 Available documentation versions:"
        mike list
        ;;
    "deploy")
        VERSION=$2
        ALIAS=$3
        if [ -z "$VERSION" ]; then
            echo "Error: Version is required for deploy command"
            echo "Usage: $0 deploy <version> [alias]"
            exit 1
        fi
        echo "🚀 Deploying version $VERSION..."
        if [ ! -z "$ALIAS" ]; then
            mike deploy --update-aliases $VERSION $ALIAS
            echo "✅ Deployed version $VERSION with alias $ALIAS"
        else
            mike deploy $VERSION
            echo "✅ Deployed version $VERSION"
        fi
        ;;
    "alias")
        VERSION=$2
        ALIAS=$3
        if [ -z "$VERSION" ] || [ -z "$ALIAS" ]; then
            echo "Error: Both version and alias are required"
            echo "Usage: $0 alias <version> <alias>"
            exit 1
        fi
        echo "🏷️  Setting alias $ALIAS for version $VERSION..."
        mike alias $VERSION $ALIAS
        echo "✅ Alias set successfully"
        ;;
    "delete")
        VERSION=$2
        if [ -z "$VERSION" ]; then
            echo "Error: Version is required for delete command"
            echo "Usage: $0 delete <version>"
            exit 1
        fi
        echo "🗑️  Deleting version $VERSION..."
        mike delete $VERSION
        echo "✅ Version $VERSION deleted"
        ;;
    "set-default")
        VERSION=$2
        if [ -z "$VERSION" ]; then
            echo "Error: Version is required for set-default command"
            echo "Usage: $0 set-default <version>"
            exit 1
        fi
        echo "🎯 Setting default version to $VERSION..."
        mike set-default $VERSION
        echo "✅ Default version set to $VERSION"
        ;;
    "serve")
        PORT=${2:-8000}
        echo "🌐 Starting versioned documentation server on port $PORT..."
        echo "📚 Available versions:"
        mike list
        echo ""
        echo "📖 Access documentation at: http://localhost:$PORT"
        echo "Press Ctrl+C to stop the server"
        mike serve --dev-addr localhost:$PORT
        ;;
    "help"|"-h"|"--help"|"")
        show_help
        ;;
    *)
        echo "Error: Unknown command '$COMMAND'"
        echo ""
        show_help
        exit 1
        ;;
esac