// Version Selector JavaScript (inspired by Mike)
window.addEventListener("DOMContentLoaded", function() {
    'use strict';
    
    function expandPath(path) {
        // Get the base directory components.
        var expanded = window.location.pathname.split("/");
        expanded.pop();
        var isSubdir = false;

        path.split("/").forEach(function(bit, i) {
            if (bit === "" && i === 0) {
                isSubdir = false;
                expanded = [""];
            } else if (bit === "." || bit === "") {
                isSubdir = true;
            } else if (bit === "..") {
                if (expanded.length === 1) {
                    // We must be trying to .. past the root!
                    throw new Error("invalid path");
                } else {
                    isSubdir = true;
                    expanded.pop();
                }
            } else {
                isSubdir = false;
                expanded.push(bit);
            }
        });

        if (isSubdir)
            expanded.push("");
        return expanded.join("/");
    }

    // Get current base URL and version
    var currentPath = window.location.pathname;
    var pathParts = currentPath.split('/').filter(function(part) { return part !== ''; });
    var CURRENT_VERSION = pathParts.length > 0 ? pathParts[0] : 'latest';
    var ABS_BASE_URL = '/' + CURRENT_VERSION + '/';

    function makeSelect(options) {
        var select = document.createElement("select");
        select.classList.add("version-selector");

        options.forEach(function(i) {
            var option = new Option(i.text, i.value, undefined, i.selected);
            select.add(option);
        });

        return select;
    }

    // Fetch versions and create selector
    fetch('/versions.json').then(function(response) {
        return response.json();
    }).then(function(versions) {
        var realVersion = versions.find(function(i) {
            return i.version === CURRENT_VERSION ||
                   (i.aliases && i.aliases.includes(CURRENT_VERSION));
        });
        
        if (!realVersion) {
            realVersion = { version: CURRENT_VERSION };
        }

        var select = makeSelect(versions.filter(function(i) {
            return i.version === realVersion.version || 
                   !i.properties || 
                   !i.properties.hidden;
        }).map(function(i) {
            return {
                text: i.title || i.version, 
                value: i.version,
                selected: i.version === realVersion.version
            };
        }));
        
        select.addEventListener("change", function(event) {
            var newVersion = this.value;
            var newPath = currentPath.replace('/' + CURRENT_VERSION + '/', '/' + newVersion + '/');
            window.location.href = newPath;
        });

        var container = document.createElement("div");
        container.id = "version-selector-container";
        container.className = "version-selector-container";
        
        var label = document.createElement("span");
        label.className = "version-label";
        label.textContent = "Version: ";
        
        container.appendChild(label);
        container.appendChild(select);

        // Try to insert into Material theme header
        var header = document.querySelector(".md-header__inner") || 
                    document.querySelector(".md-header") || 
                    document.querySelector("header") ||
                    document.querySelector(".navbar");
                    
        if (header) {
            header.appendChild(container);
        } else {
            // Fallback: add to body
            document.body.appendChild(container);
        }
    }).catch(function(error) {
        console.error('Failed to load versions:', error);
    });
});
