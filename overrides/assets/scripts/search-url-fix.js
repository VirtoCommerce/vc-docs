/**
 * Search URL Fix for Versioned Documentation
 *
 * This script fixes search result URLs to include /latest/ versioning
 * for versioned documentation sections.
 */

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
 * Fix URL by adding /latest/ after versioned section
 * @param {string} url - Original URL
 * @returns {string} - Fixed URL with /latest/
 */
function fixSearchUrl(url) {
    if (!url) return url;

    // Skip if URL already has version
    if (url.includes('/latest/') || url.includes('/1.0/') || url.includes('/2.0/') || url.includes('/3.0/')) {
        return url;
    }

    // Check if URL matches any versioned section
    for (const section of VERSIONED_SECTIONS) {
        if (url.includes(section)) {
            // Find the end of the section path
            const sectionEnd = url.indexOf(section) + section.length;
            // Insert /latest/ after the section
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
            }
        }
    });
}

/**
 * Initialize search URL fixing with enhanced detection
 */
function initSearchUrlFix() {
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

console.log('🔧 Search URL fix script loaded - ready to fix versioned URLs');
