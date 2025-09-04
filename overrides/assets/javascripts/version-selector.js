// Simple version selector - fallback if versions.json fails
document.addEventListener("DOMContentLoaded", function() {
    try {
        // Try to load versions.json
        fetch('/versions.json')
            .then(response => response.ok ? response.json() : Promise.reject())
            .then(versions => {
                if (versions && versions.length > 0) {
                    const versionSelector = document.getElementById('version-selector');
                    if (versionSelector) {
                        versionSelector.innerHTML = versions.map(v => 
                            `<a href="/${v.version}/" class="md-select__item">${v.title || v.version}</a>`
                        ).join('');
                        document.getElementById('__versioning').style.display = 'block';
                    }
                }
            })
            .catch(() => {
                // Silently fail - version selector will remain hidden
                console.log('Version selector disabled: versions.json not available');
            });
    } catch (e) {
        // Prevent any JavaScript errors from breaking the site
        console.log('Version selector error:', e);
    }
});