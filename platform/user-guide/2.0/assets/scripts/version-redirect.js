/**
 * Automatic version redirect for URLs without version
 *
 * Configuration-driven approach: reads versioning config from window.DOCS_VERSIONING
 * or falls back to data attributes on the script tag.
 *
 * Example usage in mkdocs.yml:
 *   extra_javascript:
 *     - assets/scripts/version-redirect.js
 *
 * Configuration via window object (preferred):
 *   window.DOCS_VERSIONING = {
 *     sections: ['marketplace', 'platform', 'storefront'],
 *     guides: ['developer-guide', 'user-guide', 'deployment-on-cloud'],
 *     defaultVersion: 'latest',
 *     versionPattern: '\\d+\\.\\d+(\\.\\d+)?(-S\\d+)?'
 *   };
 */
(function() {
    'use strict';

    // Skip redirect for local development
    if (['localhost', '127.0.0.1', ''].includes(window.location.hostname) ||
        window.location.protocol === 'file:') {
        return;
    }

    // Load configuration from window object or use defaults
    const config = window.DOCS_VERSIONING || {
        sections: ['marketplace', 'platform', 'storefront'],
        guides: ['developer-guide', 'user-guide', 'deployment-on-cloud'],
        defaultVersion: 'latest',
        versionPattern: '\\d+\\.\\d+(\\.\\d+)?(-S\\d+)?',
        excludedPaths: ['versions\\.json', 'index\\.html'],
        debug: false
    };

    // Helper for debug logging
    const log = config.debug ? console.log.bind(console, '[Version Redirect]') : () => {};

    // Prevent redirect loops
    const sessionKey = 'version_redirect_attempted';
    const currentPath = window.location.pathname;

    if (sessionStorage.getItem(sessionKey) === currentPath) {
        sessionStorage.removeItem(sessionKey);
        log('Loop prevention: Already attempted redirect for', currentPath);
        return;
    }

    /**
     * Build regex pattern dynamically from config
     * Pattern: /^\/({sections})\/({guides})\/(?!({versions}|latest|stable|{excluded}))(.+)$/
     */
    function buildPattern() {
        const sectionsPattern = config.sections.join('|');
        const guidesPattern = config.guides.join('|');
        const excludedPattern = config.excludedPaths.join('|');

        // Negative lookahead: (?!version|latest|stable|excluded)
        const negativeLookahead = `(?!(${config.versionPattern}|latest|stable|${excludedPattern}))`;

        return new RegExp(
            `^\\/(${sectionsPattern})\\/(${guidesPattern})\\/${negativeLookahead}([^\\/]+.*)$`
        );
    }

    /**
     * Extract path components and redirect to versioned URL
     */
    function redirectToVersioned() {
        const pattern = buildPattern();
        log('Built pattern:', pattern);
        log('Testing path:', currentPath);

        const match = currentPath.match(pattern);

        if (!match) {
            log('No match - path is already versioned or not a versioned section');
            return;
        }

        const section = match[1];
        const guide = match[2];
        // match[3] is the negative lookahead (captured but not used)
        const content = match[4];

        // Construct new URL with default version
        const versionedPath = `/${section}/${guide}/${config.defaultVersion}/${content}`;
        const versionedUrl = window.location.origin + versionedPath +
                           window.location.search + window.location.hash;

        log('Redirecting:', {
            from: currentPath,
            to: versionedPath,
            section,
            guide,
            content
        });

        // Mark redirect attempt
        sessionStorage.setItem(sessionKey, currentPath);

        // Perform redirect (replaces history entry)
        window.location.replace(versionedUrl);
    }

    // Execute redirect logic
    redirectToVersioned();
})();

