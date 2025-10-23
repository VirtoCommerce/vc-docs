/**
 * Automatic version redirect for URLs without version
 * Redirects old URLs to the latest version
 * Example: /platform/developer-guide/Fundamentals/... -> /platform/developer-guide/latest/Fundamentals/...
 */
(function() {
    'use strict';

    // Get current path
    const currentPath = window.location.pathname;

    // Pattern to match paths without version: /{section}/{guide}/{content}
    // Where content doesn't start with a version number or 'latest'/'stable'
    const pathPattern = /^\/(marketplace|platform|storefront)\/(developer-guide|user-guide|deployment-on-cloud)\/(?!([0-9]+\.[0-9]+|[0-9]+\.[0-9]+-S[0-9]+|latest|stable|versions\.json))(.+)$/;

    const match = currentPath.match(pathPattern);

    if (match) {
        const section = match[1];      // marketplace, platform, or storefront
        const guide = match[2];         // developer-guide, user-guide, or deployment-on-cloud
        const content = match[4];       // rest of the path

        // Construct new URL with 'latest' version
        const newPath = `/${section}/${guide}/latest/${content}`;
        const newUrl = window.location.origin + newPath + window.location.search + window.location.hash;

        console.log('[Version Redirect] Redirecting from:', currentPath, 'to:', newPath);

        // Perform redirect
        window.location.replace(newUrl);
    }
})();

