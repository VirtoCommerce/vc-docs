#!/usr/bin/env python3
"""
VirtoCommerce documentation versioning utilities
"""

import json
import os
import sys
import subprocess
from pathlib import Path
from typing import Dict, Any, Optional


class VersionManager:
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.version_file = self.project_root / "VERSION"
        self.version_json = self.project_root / "version.json"
    
    def get_current_version(self) -> str:
        """Get current version from VERSION file"""
        try:
            if self.version_file.exists():
                return self.version_file.read_text().strip()
            return "dev"
        except Exception as e:
            print(f"Error reading version: {e}")
            return "dev"
    
    def get_version_config(self) -> Dict[str, Any]:
        """Get full version configuration from JSON"""
        try:
            if self.version_json.exists():
                return json.loads(self.version_json.read_text())
            return {
                "version": self.get_current_version(),
                "alias": "",
                "title": "VirtoCommerce Documentation",
                "description": "Official VirtoCommerce Platform Documentation"
            }
        except Exception as e:
            print(f"Error reading version configuration: {e}")
            return {
                "version": self.get_current_version(),
                "alias": "",
                "title": "VirtoCommerce Documentation",
                "description": "Official VirtoCommerce Platform Documentation"
            }
    
    def get_deployed_version(self, branch: str = "gh-pages") -> Optional[str]:
        """Get latest deployed version from mike"""
        try:
            result = subprocess.run(
                ["mike", "list", "--branch", branch],
                capture_output=True,
                text=True,
                check=True
            )
            
            lines = result.stdout.strip().split('\n')
            for line in lines:
                if '[latest]' in line or '[default]' in line:
                    # Extract version from line like "1.0.0 [latest]"
                    version = line.split()[0]
                    return version
            
            # If no default/latest, take first version
            if lines and lines[0].strip():
                return lines[0].split()[0]
            
            return None
        except subprocess.CalledProcessError:
            return None
        except Exception as e:
            print(f"Error getting deployed version: {e}")
            return None
    
    def version_exists(self, version: str, branch: str = "gh-pages") -> bool:
        """Check if version exists in deployment"""
        try:
            result = subprocess.run(
                ["mike", "list", "--branch", branch],
                capture_output=True,
                text=True,
                check=True
            )
            
            for line in result.stdout.strip().split('\n'):
                if line.startswith(version + ' ') or line == version:
                    return True
            return False
        except:
            return False
    
    def should_update_existing_version(self) -> tuple[str, bool]:
        """
        Determine whether to update existing version or create new one
        Returns: (version, should_update_existing)
        """
        current_version = self.get_current_version()
        deployed_version = self.get_deployed_version()
        
        print(f"Current version in file: {current_version}")
        print(f"Last deployed version: {deployed_version}")
        
        if deployed_version == current_version:
            print(f"Version {current_version} already deployed. Will update content.")
            return current_version, True
        else:
            print(f"New version {current_version}. Will create new deployment.")
            return current_version, False
    
    def get_deployment_params(self) -> Dict[str, Any]:
        """Get deployment parameters"""
        config = self.get_version_config()
        version = config.get("version", "dev")
        alias = config.get("alias", "")
        
        current_version, update_existing = self.should_update_existing_version()
        
        return {
            "version": current_version,
            "alias": alias if not update_existing else alias,  # Keep alias when updating
            "title": config.get("title", f"VirtoCommerce Documentation v{current_version}"),
            "update_existing": update_existing,
            "config": config
        }


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python version-utils.py get-version")
        print("  python version-utils.py get-config")
        print("  python version-utils.py get-deploy-params")
        print("  python version-utils.py check-should-update")
        sys.exit(1)
    
    manager = VersionManager()
    command = sys.argv[1]
    
    if command == "get-version":
        print(manager.get_current_version())
    
    elif command == "get-config":
        print(json.dumps(manager.get_version_config(), indent=2))
    
    elif command == "get-deploy-params":
        params = manager.get_deployment_params()
        print(json.dumps(params, indent=2))
    
    elif command == "check-should-update":
        version, should_update = manager.should_update_existing_version()
        result = {
            "version": version,
            "should_update_existing": should_update
        }
        print(json.dumps(result))
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()