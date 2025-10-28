/**
 * Automatic version redirect for URLs without version
 * Redirects old URLs to the latest version
 * Example: /platform/developer-guide/Fundamentals/... -> /platform/developer-guide/latest/Fundamentals/...
 */
(function() {
    'use strict';

    // Skip redirect for local development (mkdocs serve) or local build testing
    if (window.location.hostname === 'localhost' ||
        window.location.hostname === '127.0.0.1' ||
        window.location.hostname.includes('localhost') ||
        window.location.protocol === 'file:' ||
        // Check if this is a local build without versioning (no /latest/ in URL structure)
        (!window.location.pathname.includes('/latest/') &&
         !window.location.pathname.match(/\/[0-9]+\.[0-9]+/))) {
        console.log('[Version Redirect] Skipping redirect for local development or non-versioned build');
        return;
    }

    // Get current path
    const currentPath = window.location.pathname;

    // Pattern to match paths without version: /{section}/{guide}/{content}
    // Where content doesn't start with a version number or 'latest'/'stable'
    const pathPattern = /^\/(marketplace|platform|storefront)\/(developer-guide|user-guide|deployment-on-cloud)\/(?!([0-9]+\.[0-9]+|[0-9]+\.[0-9]+-S[0-9]+|latest|stable|versions\.json))(.+)$/;

    const match = currentPath.match(pathPattern);

    if (match) {
        const section = match[1];      // marketplace, platform, or storefront
        const guide = match[2];         // developer-guide, user-guide, or deployment-on-cloud
        const content = match[3];       // rest of the path

        // Construct new URL with 'latest' version
        const newPath = `/${section}/${guide}/latest/${content}`;
        const newUrl = window.location.origin + newPath + window.location.search + window.location.hash;

        console.log('[Version Redirect] Redirecting from:', currentPath, 'to:', newPath);

        // Perform redirect
        window.location.replace(newUrl);
    }
})();

