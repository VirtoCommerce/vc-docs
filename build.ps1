mkdocs build  -d ./site

mkdocs build  -f storefront/mkdocs.yml -d ../site/storefront
mkdocs build  -f storefront/user-guide/mkdocs.yml -d ../../site/storefront/user-guide
mkdocs build  -f storefront/developer-guide/mkdocs.yml -d ../../site/storefront/developer-guide

mkdocs build  -f platform/mkdocs.yml -d ../site/platform
mkdocs build  -f platform/user-guide/mkdocs.yml -d ../../site/platform/user-guide
mkdocs build  -f platform/developer-guide/mkdocs.yml -d ../../site/platform/developer-guide

mkdocs build  -f marketplace/mkdocs.yml -d ../site/marketplace
mkdocs build  -f marketplace/user-guide/mkdocs.yml -d ../../site/marketplace/user-guide
mkdocs build  -f marketplace/developer-guide/mkdocs.yml -d ../../site/marketplace/developer-guide
