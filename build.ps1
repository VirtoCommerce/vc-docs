mkdocs build  -d ./site

mkdocs build  -f storefront_docs/mkdocs.yml -d ../site/storefront_docs
mkdocs build  -f storefront_docs/user_docs/mkdocs.yml -d ../../site/storefront_docs/user_docs
mkdocs build  -f storefront_docs/dev_docs/mkdocs.yml -d ../../site/storefront_docs/dev_docs

mkdocs build  -f platform_docs/mkdocs.yml -d ../site/platform_docs
mkdocs build  -f platform_docs/user_docs/mkdocs.yml -d ../../site/platform_docs/user_docs
mkdocs build  -f platform_docs/dev_docs/mkdocs.yml -d ../../site/platform_docs/dev_docs

mkdocs build  -f marketplace_docs/mkdocs.yml -d ../site/marketplace_docs
mkdocs build  -f marketplace_docs/user_docs/mkdocs.yml -d ../../site/marketplace_docs/user_docs
mkdocs build  -f marketplace_docs/dev_docs/mkdocs.yml -d ../../site/marketplace_docs/dev_docs
