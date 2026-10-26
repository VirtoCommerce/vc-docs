/**
 * Version Selector Visibility Handler
 *
 * Manages version selector visibility based on:
 * - Search state (hide when search is open)
 * - Mobile viewport (hide on small screens)
 * - Scroll position (optional fade out on scroll)
 *
 * This script enhances the CSS-only solution with JavaScript for smoother UX
 */
(function() {
    'use strict';

    // Configuration
    const CONFIG = {
        mobileBreakpoint: 768,      // Hide version selector below this width
        enableScrollHide: false,    // Set to true to hide on scroll
        scrollThreshold: 100,       // Pixels to scroll before hiding
        animationClass: 'md-version--animated',
        debug: true                 // Enable debug logging (set to false for production)
    };

    // Initialize when DOM is ready
    function init() {
        if (CONFIG.debug) {
            console.log('[Version Selector] Script loaded, initializing...');
        }

        // Get elements to hide/show
        const versionSelector = document.querySelector('.md-version');
        const megaMenu = document.querySelector('.mega-menu');

        if (!versionSelector && !megaMenu) {
            // Neither element found
            if (CONFIG.debug) {
                console.log('[Version Selector] No .md-version or .mega-menu found - not a versioned page');
            }
            return;
        }

        if (CONFIG.debug) {
            console.log('[Version Selector] Initialized', {
                versionSelector: !!versionSelector,
                megaMenu: !!megaMenu,
                isMobile: window.innerWidth < CONFIG.mobileBreakpoint,
                config: CONFIG
            });
        }

        // Add animation class for smooth transitions
        if (versionSelector) {
            versionSelector.classList.add(CONFIG.animationClass);
        }

        /**
         * Check if viewport is mobile
         */
        function isMobile() {
            return window.innerWidth < CONFIG.mobileBreakpoint;
        }

        /**
         * Update version selector and mega-menu visibility based on all conditions
         */
        function updateVisibility() {
            const searchCheckbox = document.querySelector('input[data-md-toggle="search"]');
            const searchOpen = searchCheckbox ? searchCheckbox.checked : false;
            const mobile = isMobile();

            // Debug logging
            if (CONFIG.debug || window.DEBUG_VERSION_SELECTOR) {
                console.log('[Version Selector] Update visibility:', {
                    searchOpen,
                    mobile,
                    checkboxFound: !!searchCheckbox,
                    checkboxChecked: searchCheckbox ? searchCheckbox.checked : null
                });
            }

            // Hide if search is open OR on mobile
            if (searchOpen || mobile) {
                if (versionSelector) {
                    versionSelector.style.display = 'none';
                    versionSelector.setAttribute('aria-hidden', 'true');
                }
                if (megaMenu) {
                    megaMenu.style.display = 'none';
                    megaMenu.setAttribute('aria-hidden', 'true');
                }
            } else {
                if (versionSelector) {
                    versionSelector.style.display = '';
                    versionSelector.removeAttribute('aria-hidden');
                }
                if (megaMenu) {
                    megaMenu.style.display = '';
                    megaMenu.removeAttribute('aria-hidden');
                }
            }
        }

        /**
         * Handle scroll-based hiding (optional)
         */
        let lastScrollTop = 0;
        function handleScroll() {
            if (!CONFIG.enableScrollHide) return;

            const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

            if (scrollTop > CONFIG.scrollThreshold && scrollTop > lastScrollTop) {
                // Scrolling down past threshold
                versionSelector.classList.add('md-version--hidden-scroll');
            } else if (scrollTop < lastScrollTop - 50) {
                // Scrolling up significantly
                versionSelector.classList.remove('md-version--hidden-scroll');
            }

            lastScrollTop = scrollTop;
        }

        // Watch for search toggle changes
        const searchToggle = document.querySelector('input[data-md-toggle="search"]');
        if (searchToggle) {
            // Listen for change events
            searchToggle.addEventListener('change', updateVisibility);

            // Also watch for click events on search button/label
            const searchButton = document.querySelector('label[for="__search"]');
            if (searchButton) {
                searchButton.addEventListener('click', function() {
                    // Delay to let the checkbox state update
                    setTimeout(updateVisibility, 100);
                });
            }
        }

        // Watch for changes to search overlay visibility (clicking overlay closes search)
        const searchOverlay = document.querySelector('.md-search__overlay');
        if (searchOverlay) {
            searchOverlay.addEventListener('click', function() {
                setTimeout(updateVisibility, 100);
            });
        }

        // Watch for Escape key (closes search)
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                setTimeout(updateVisibility, 100);
            }
        });

        // Use MutationObserver to catch any state changes we might miss
        const observer = new MutationObserver(function() {
            updateVisibility();
        });

        // Observe changes to body class (some themes add classes when search is active)
        observer.observe(document.body, {
            attributes: true,
            attributeFilter: ['class', 'data-md-state']
        });

        // Observe the search checkbox for attribute changes
        if (searchToggle) {
            observer.observe(searchToggle, {
                attributes: true,
                attributeFilter: ['checked']
            });
        }

        // Watch for window resize
        let resizeTimer;
        window.addEventListener('resize', function() {
            clearTimeout(resizeTimer);
            resizeTimer = setTimeout(updateVisibility, 150);
        });

        // Optional: Watch for scroll
        if (CONFIG.enableScrollHide) {
            let scrollTimer;
            window.addEventListener('scroll', function() {
                clearTimeout(scrollTimer);
                scrollTimer = setTimeout(handleScroll, 50);
            }, { passive: true });
        }

        // Initial visibility check
        updateVisibility();
    }

    // Run init when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        // DOM is already ready
        init();
    }
})();
