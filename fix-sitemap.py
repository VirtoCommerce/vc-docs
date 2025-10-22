#!/usr/bin/env python3
"""
Sitemap fixer for versioned documentation
This script corrects sitemap.xml URLs to include proper versioning
"""

import os
import sys
import xml.etree.ElementTree as ET
from urllib.parse import urlparse
import re

def fix_sitemap_urls(sitemap_path, version="1.0", use_latest=True):
    """
    Fix sitemap.xml URLs to include proper versioning

    Args:
        sitemap_path: Path to sitemap.xml file
        version: Version to use (e.g., "1.0", "3.2025-S13")
        use_latest: If True, use 'latest' instead of specific version
    """

    if not os.path.exists(sitemap_path):
        print(f"❌ Sitemap file not found: {sitemap_path}")
        return False

    print(f"🔧 Fixing sitemap URLs in {sitemap_path}")
    print(f"   Version: {version if not use_latest else 'latest'}")

    # Parse the sitemap
    try:
        tree = ET.parse(sitemap_path)
        root = tree.getroot()
    except ET.ParseError as e:
        print(f"❌ Error parsing sitemap: {e}")
        return False

    # Define URL patterns that need versioning - ALL URLs under versioned sections
    # These patterns match any URL that contains versioned section paths
    versioned_patterns = [
        r'/marketplace/developer-guide/',
        r'/marketplace/user-guide/',
        r'/platform/developer-guide/',
        r'/platform/user-guide/',
        r'/platform/deployment-on-cloud/',
        r'/storefront/developer-guide/',
        r'/storefront/user-guide/',
    ]

    # Compile regex patterns
    compiled_patterns = [re.compile(pattern) for pattern in versioned_patterns]

    modified_count = 0

    # Process each URL in the sitemap
    for url_elem in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
        loc_elem = url_elem.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
        if loc_elem is not None:
            original_url = loc_elem.text
            if original_url:
                # Check if this URL needs versioning
                needs_versioning = any(pattern.search(original_url) for pattern in compiled_patterns)

                if needs_versioning:
                    # Parse the URL
                    parsed = urlparse(original_url)
                    path = parsed.path

                    # Skip if already has version in path
                    if '/latest/' in path or re.search(r'/\d+\.\d+/', path):
                        continue

                    # Insert version after the section name
                    # Find which pattern matched and insert version after it
                    new_path = path
                    for pattern in compiled_patterns:
                        if pattern.search(path):
                            # Find the end of the matched section
                            match = pattern.search(path)
                            if match:
                                section_end = match.end()
                                # Insert version after the section
                                if use_latest:
                                    new_path = path[:section_end] + 'latest/' + path[section_end:]
                                else:
                                    new_path = path[:section_end] + f'{version}/' + path[section_end:]
                            break

                    # Reconstruct the URL
                    new_url = f"{parsed.scheme}://{parsed.netloc}{new_path}"

                    # Update the URL
                    loc_elem.text = new_url
                    modified_count += 1

                    print(f"   ✓ {original_url} → {new_url}")

    if modified_count > 0:
        # Write the modified sitemap back
        try:
            # Create a new XML structure without namespace prefixes
            new_root = ET.Element("urlset")
            new_root.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")

            # Copy all URL elements without namespace prefixes
            for url_elem in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
                new_url = ET.SubElement(new_root, "url")

                loc_elem = url_elem.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
                if loc_elem is not None:
                    new_loc = ET.SubElement(new_url, "loc")
                    new_loc.text = loc_elem.text

                lastmod_elem = url_elem.find('{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod')
                if lastmod_elem is not None:
                    new_lastmod = ET.SubElement(new_url, "lastmod")
                    new_lastmod.text = lastmod_elem.text

                changefreq_elem = url_elem.find('{http://www.sitemaps.org/schemas/sitemap/0.9}changefreq')
                if changefreq_elem is not None:
                    new_changefreq = ET.SubElement(new_url, "changefreq")
                    new_changefreq.text = changefreq_elem.text

            # Write the new XML structure
            new_tree = ET.ElementTree(new_root)
            ET.indent(new_tree, space="    ", level=0)
            new_tree.write(sitemap_path, encoding='utf-8', xml_declaration=True)

            # Also update the compressed version if it exists
            gz_path = sitemap_path + '.gz'
            if os.path.exists(gz_path):
                import gzip
                with open(sitemap_path, 'rb') as f_in:
                    with gzip.open(gz_path, 'wb') as f_out:
                        f_out.write(f_in.read())
                print(f"✅ Updated compressed sitemap: {gz_path}")

            print(f"✅ Fixed {modified_count} URLs in sitemap")
            return True
        except Exception as e:
            print(f"❌ Error writing sitemap: {e}")
            return False
    else:
        print("ℹ️  No URLs needed fixing")
        return True

def main():
    """Main function"""
    if len(sys.argv) < 2:
        print("Usage: python fix-sitemap.py <sitemap_path> [version] [--use-latest]")
        print("Example: python fix-sitemap.py site/sitemap.xml 1.0")
        print("Example: python fix-sitemap.py site/sitemap.xml --use-latest")
        sys.exit(1)

    sitemap_path = sys.argv[1]
    version = "1.0"
    use_latest = False

    # Parse command line arguments
    if len(sys.argv) > 2:
        if sys.argv[2] == "--use-latest":
            use_latest = True
        else:
            version = sys.argv[2]

    if "--use-latest" in sys.argv:
        use_latest = True

    success = fix_sitemap_urls(sitemap_path, version, use_latest)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
