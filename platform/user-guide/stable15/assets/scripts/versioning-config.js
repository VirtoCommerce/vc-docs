/**
 * Versioning Configuration for Documentation Site
 *
 * This file configures the automatic version redirects for legacy URLs.
 * It's optional - if not included, version-redirect.js will use default values.
 *
 * To use: Include this file BEFORE version-redirect.js in mkdocs.yml:
 *   extra_javascript:
 *     - assets/scripts/versioning-config.js
 *     - assets/scripts/version-redirect.js
 */

window.DOCS_VERSIONING = {
    /**
     * Top-level sections of the documentation
     * Add new sections here when expanding the documentation structure
     */
    sections: [
        'marketplace',
        'platform',
        'storefront'
    ],

    /**
     * Guide types within each section
     * These are the subsections that use versioning
     */
    guides: [
        'developer-guide',
        'user-guide',
        'deployment-on-cloud'
    ],

    /**
     * Default version to redirect to
     * Usually 'latest' to always point to the newest version
     */
    defaultVersion: 'latest',

    /**
     * Regex pattern for version numbers
     * Matches:
     *   - 1.0
     *   - 1.0.1
     *   - 3.0-S11
     *   - etc.
     *
     * Escape backslashes in strings: \\d instead of \d
     */
    versionPattern: '\\d+\\.\\d+(\\.\\d+)?(-S\\d+)?',

    /**
     * Paths to exclude from redirect logic
     * These will not trigger redirects even if they match the pattern
     */
    excludedPaths: [
        'versions\\.json',  // Mike's version list
        'index\\.html'      // Root index pages
    ],

    /**
     * Enable debug logging (useful for troubleshooting)
     * Set to true to see console logs for redirects
     */
    debug: false
};

// Freeze config to prevent accidental modifications
Object.freeze(window.DOCS_VERSIONING);
