/**
 * Search URL Fix for Versioned Documentation
 *
 * This script fixes search result URLs to include /latest/ versioning
 * for versioned documentation sections.
 */

// Skip URL fixing for local development (mkdocs serve) or local build testing
function isLocalDevelopment() {
    return window.location.hostname === 'localhost' ||
           window.location.hostname === '127.0.0.1' ||
           window.location.hostname.includes('localhost') ||
           window.location.protocol === 'file:' ||
           // Check if this is a local build without versioning (no /latest/ in URL structure)
           (!window.location.pathname.includes('/latest/') &&
            !window.location.pathname.match(/\/[0-9]+\.[0-9]+/));
}

// Define versioned sections that need /latest/ added
const VERSIONED_SECTIONS = [
    '/marketplace/developer-guide/',
    '/marketplace/user-guide/',
    '/platform/developer-guide/',
    '/platform/user-guide/',
    '/platform/deployment-on-cloud/',
    '/storefront/developer-guide/',
    '/storefront/user-guide/'
];

/**
 * Fix URL by replacing any version with /latest/ after versioned section
 * @param {string} url - Original URL
 * @returns {string} - Fixed URL with /latest/
 */
function fixSearchUrl(url) {
    if (!url) return url;

    // Skip fixing for local development
    if (isLocalDevelopment()) {
        return url;
    }

    // Check if URL matches any versioned section
    for (const section of VERSIONED_SECTIONS) {
        if (url.includes(section)) {
            // Find the end of the section path
            const sectionEnd = url.indexOf(section) + section.length;
            const afterSection = url.substring(sectionEnd);

            // If there's already /latest/ after the section, leave it alone
            if (afterSection.startsWith('latest/')) {
                return url;
            }

            // If there's a version (numbered or stable), replace it with /latest/
            const versionMatch = afterSection.match(/^(stable|[0-9]+\.[0-9]+(\.[0-9]+)?(-S[0-9]+)?)\//);
            if (versionMatch) {
                const version = versionMatch[1];
                const restOfPath = afterSection.substring(version.length + 1); // +1 for the slash
                return url.substring(0, sectionEnd) + 'latest/' + restOfPath;
            }

            // If there's no version, add /latest/
            return url.substring(0, sectionEnd) + 'latest/' + url.substring(sectionEnd);
        }
    }

    return url;
}

/**
 * Fix all search result links
 */
function fixSearchResultLinks() {
    const searchResults = document.querySelectorAll('.md-search-result__list a, .md-search-result__meta a');

    searchResults.forEach(link => {
        const originalHref = link.getAttribute('href');
        if (originalHref) {
            const fixedHref = fixSearchUrl(originalHref);
            if (fixedHref !== originalHref) {
                link.setAttribute('href', fixedHref);
                console.log(`🔧 Fixed search URL: ${originalHref} → ${fixedHref}`);
            } else {
                console.log(`✅ URL already correct: ${originalHref}`);
            }
        }
    });
}

/**
 * Initialize search URL fixing with enhanced detection
 */
function initSearchUrlFix() {
    // Skip initialization for local development
    if (isLocalDevelopment()) {
        console.log('🔧 Search URL fix script loaded - skipping for local development');
        return;
    }

    // Fix URLs when search results are displayed
    const searchResultContainer = document.querySelector('.md-search-result__list');

    if (searchResultContainer) {
        // Use MutationObserver to watch for new search results
        const observer = new MutationObserver((mutations) => {
            let shouldFix = false;
            mutations.forEach((mutation) => {
                if (mutation.type === 'childList' && mutation.addedNodes.length > 0) {
                    shouldFix = true;
                }
            });

            if (shouldFix) {
                // Small delay to ensure DOM is updated
                setTimeout(fixSearchResultLinks, 50);
            }
        });

        observer.observe(searchResultContainer, {
            childList: true,
            subtree: true
        });

        // Also fix any existing results
        fixSearchResultLinks();
    }
}

/**
 * Enhanced initialization with multiple triggers
 */
function initializeSearchFix() {
    // Initialize immediately
    initSearchUrlFix();

    // Also watch for search input changes
    const searchInput = document.querySelector('.md-search__input');
    if (searchInput) {
        searchInput.addEventListener('input', () => {
            setTimeout(fixSearchResultLinks, 200);
        });
    }

    // Watch for search modal open/close
    const searchOverlay = document.querySelector('.md-search__overlay');
    if (searchOverlay) {
        searchOverlay.addEventListener('click', () => {
            setTimeout(initSearchUrlFix, 300);
        });
    }
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeSearchFix);
} else {
    initializeSearchFix();
}

// Also initialize when search is opened (for dynamic content)
document.addEventListener('click', (event) => {
    if (event.target.closest('.md-search__input') ||
        event.target.closest('.md-search__overlay') ||
        event.target.closest('.md-search__icon')) {
        setTimeout(initializeSearchFix, 300);
    }
});

// Watch for search result updates
document.addEventListener('keyup', (event) => {
    if (event.target.closest('.md-search__input')) {
        setTimeout(fixSearchResultLinks, 100);
    }
});

// Log initialization status
if (isLocalDevelopment()) {
    console.log('🔧 Search URL fix script loaded - skipping for local development');
} else {
    console.log('🔧 Search URL fix script loaded - ready to fix versioned URLs');
}
