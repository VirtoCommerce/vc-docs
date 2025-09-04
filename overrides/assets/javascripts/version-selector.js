// Mike version selector initialization
document.addEventListener("DOMContentLoaded", function() {
    // Load versions.json and populate version selector
    fetch('/versions.json')
        .then(response => response.json())
        .then(versions => {
            const versionSelector = document.getElementById('version-selector');
            const currentVersionSpan = document.querySelector('#__versioning .md-select__link');
            
            if (versionSelector && versions && versions.length > 0) {
                // Clear existing content
                versionSelector.innerHTML = '';
                
                // Find current version from URL
                const currentPath = window.location.pathname;
                const currentVersion = currentPath.split('/')[1] || 'latest';
                
                // Update current version display
                if (currentVersionSpan) {
                    const current = versions.find(v => v.version === currentVersion || v.aliases.includes(currentVersion));
                    if (current) {
                        currentVersionSpan.textContent = current.title || current.version;
                    }
                }
                
                // Populate dropdown with versions
                versions.forEach(version => {
                    const link = document.createElement('a');
                    link.href = `/${version.version}/`;
                    link.className = 'md-select__item';
                    link.textContent = version.title || version.version;
                    
                    // Mark current version
                    if (version.version === currentVersion || version.aliases.includes(currentVersion)) {
                        link.setAttribute('aria-selected', 'true');
                        link.style.fontWeight = 'bold';
                    }
                    
                    versionSelector.appendChild(link);
                });
                
                // Show version selector
                document.getElementById('__versioning').style.display = 'block';
            }
        })
        .catch(error => {
            console.warn('Could not load versions:', error);
            // Hide version selector if versions.json is not available
            const versionSelector = document.getElementById('__versioning');
            if (versionSelector) {
                versionSelector.style.display = 'none';
            }
        });
});