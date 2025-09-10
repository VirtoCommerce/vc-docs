// Version Selector JavaScript
(function() {
    'use strict';
    
    // Function to get current version from URL
    function getCurrentVersion() {
        const path = window.location.pathname;
        const match = path.match(/\/([^\/]+)\//);
        return match ? match[1] : 'latest';
    }
    
    // Function to switch version
    function switchVersion(newVersion) {
        const currentPath = window.location.pathname;
        const currentVersion = getCurrentVersion();
        const newPath = currentPath.replace('/' + currentVersion + '/', '/' + newVersion + '/');
        window.location.href = newPath;
    }
    
    // Function to load versions
    function loadVersions() {
        fetch('/versions.json')
            .then(response => response.json())
            .then(versions => {
                createVersionSelector(versions);
            })
            .catch(error => {
                console.error('Failed to load versions:', error);
            });
    }
    
    // Function to create version selector
    function createVersionSelector(versions) {
        const currentVersion = getCurrentVersion();
        
        // Create container
        const container = document.createElement('div');
        container.className = 'version-selector-container';
        
        // Create label
        const label = document.createElement('span');
        label.className = 'version-label';
        label.textContent = 'Version:';
        
        // Create select element
        const select = document.createElement('select');
        select.className = 'version-selector';
        
        // Add versions to select
        versions.forEach(function(versionInfo) {
            const option = document.createElement('option');
            option.value = versionInfo.version;
            option.textContent = versionInfo.title || versionInfo.version;
            
            // Mark current version as selected
            if (versionInfo.version === currentVersion || 
                (versionInfo.aliases && versionInfo.aliases.includes(currentVersion))) {
                option.selected = true;
            }
            
            select.appendChild(option);
            
            // Add aliases as separate options
            if (versionInfo.aliases) {
                versionInfo.aliases.forEach(function(alias) {
                    const aliasOption = document.createElement('option');
                    aliasOption.value = alias;
                    aliasOption.textContent = alias + ' (' + versionInfo.version + ')';
                    if (alias === currentVersion) {
                        aliasOption.selected = true;
                    }
                    select.appendChild(aliasOption);
                });
            }
        });
        
        // Add change event listener
        select.addEventListener('change', function(e) {
            switchVersion(e.target.value);
        });
        
        // Assemble and add to page
        container.appendChild(label);
        container.appendChild(select);
        document.body.appendChild(container);
    }
    
    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', loadVersions);
    } else {
        loadVersions();
    }
})();
