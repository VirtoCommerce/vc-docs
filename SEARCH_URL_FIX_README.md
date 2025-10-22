# Search URL Fix for Versioned Documentation

## Problem

The sitemap.xml contains correct URLs with `/latest/` versioning (e.g., `/platform/developer-guide/latest/`), but the internal search on the website generates URLs without versioning (e.g., `/platform/developer-guide/`), making them incorrect and leading to 404 errors.

## Solution

We've created a JavaScript solution that automatically fixes search result URLs to include `/latest/` versioning for versioned documentation sections.

## Files Added/Modified

1. **`overrides/assets/scripts/search-url-fix.js`** - JavaScript script that fixes search URLs
2. **`mkdocs.yml`** - Updated to include the search URL fix script
3. **`SEARCH_URL_FIX_README.md`** - This documentation

## How It Works

### 1. URL Detection
The script identifies URLs that need versioning based on predefined patterns:
- `/marketplace/developer-guide/`
- `/marketplace/user-guide/`
- `/platform/developer-guide/`
- `/platform/user-guide/`
- `/platform/deployment-on-cloud/`
- `/storefront/developer-guide/`
- `/storefront/user-guide/`

### 2. URL Fixing
URLs are automatically updated to include `/latest/` after the section name:
- **Before**: `/platform/developer-guide/getting-started`
- **After**: `/platform/developer-guide/latest/getting-started`

### 3. Dynamic Detection
The script uses multiple detection methods:
- **MutationObserver**: Watches for new search results being added to the DOM
- **Event Listeners**: Responds to search input changes and modal interactions
- **Multiple Triggers**: Initializes on DOM ready, search open, and input changes

## Technical Implementation

### JavaScript Features

```javascript
// Define versioned sections
const VERSIONED_SECTIONS = [
    '/marketplace/developer-guide/',
    '/marketplace/user-guide/',
    '/platform/developer-guide/',
    '/platform/user-guide/',
    '/platform/deployment-on-cloud/',
    '/storefront/developer-guide/',
    '/storefront/user-guide/'
];

// Fix URL by adding /latest/ after versioned section
function fixSearchUrl(url) {
    // Skip if URL already has version
    if (url.includes('/latest/') || url.includes('/1.0/') || url.includes('/2.0/')) {
        return url;
    }

    // Check if URL matches any versioned section
    for (const section of VERSIONED_SECTIONS) {
        if (url.includes(section)) {
            const sectionEnd = url.indexOf(section) + section.length;
            return url.substring(0, sectionEnd) + 'latest/' + url.substring(sectionEnd);
        }
    }

    return url;
}
```

### Integration with MkDocs

The script is automatically loaded on all pages through the `mkdocs.yml` configuration:

```yaml
extra_javascript:
    - assets/scripts/scripts-loader.js
    - assets/scripts/scroll-menu.js
    - assets/scripts/search-url-fix.js
```

## Benefits

1. **Automatic Fix**: No manual intervention required
2. **Real-time**: Fixes URLs as search results are displayed
3. **Comprehensive**: Covers all versioned documentation sections
4. **Non-intrusive**: Only affects search results, doesn't break existing functionality
5. **Performance**: Lightweight script with efficient DOM watching

## Testing

### Manual Testing

1. Open the documentation website
2. Use the search functionality
3. Check that search result URLs include `/latest/`
4. Verify that clicking search results leads to correct pages

### Console Testing

Open browser developer tools and check the console for messages like:
```
🔧 Search URL fix script loaded - ready to fix versioned URLs
🔧 Fixed search URL: /platform/developer-guide/getting-started → /platform/developer-guide/latest/getting-started
```

## Browser Compatibility

The script uses modern JavaScript features:
- **MutationObserver**: Supported in all modern browsers
- **ES6 Features**: Arrow functions, const/let, template literals
- **Event Delegation**: Efficient event handling

## Troubleshooting

### If URLs are not being fixed:

1. **Check Console**: Look for JavaScript errors in browser console
2. **Verify Script Loading**: Ensure `search-url-fix.js` is loaded
3. **Check Selectors**: Verify that search result elements use expected CSS classes
4. **Test Manually**: Use browser developer tools to test the `fixSearchUrl()` function

### Common Issues:

1. **Script not loading**: Check `mkdocs.yml` configuration
2. **Timing issues**: Script may need to wait for search results to load
3. **CSS class changes**: MkDocs Material updates may change CSS classes

## Future Enhancements

1. **Configuration**: Make versioned sections configurable
2. **Version Detection**: Automatically detect current version instead of hardcoding `/latest/`
3. **Analytics**: Track how many URLs are being fixed
4. **Fallback**: Provide fallback for older browsers

## Related Files

- `fix-sitemap.py` - Fixes sitemap.xml URLs
- `versioned-build.py` - Build process that includes sitemap fixing
- `SITEMAP_FIX_README.md` - Documentation for sitemap fixing

## Integration with Build Process

The search URL fix is automatically included in all builds:
1. **Development**: Script is loaded during `mkdocs serve`
2. **Production**: Script is included in the built site
3. **Versioned Builds**: Script works with all versioned documentation sections

This ensures that search functionality works correctly across all documentation sections, providing a seamless user experience.
