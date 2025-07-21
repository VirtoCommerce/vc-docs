# SEO

The Virto Commerce **SEO** module provides a flexible infrastructure for managing SEO-related data across the Platform. It supports SEO metadata (e.g., slugs, titles, meta descriptions) for various entities such as catalogs, categories, products, and custom pages.

[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-seo/)

[![Latest release](media/latest_release.png)](https://github.com/VirtoCommerce/vc-module-seo/releases)


## Key features

- **SEO info lookup**: Efficient retrieval of SEO records matching given criteria such as `permalink`, `storeId`, `language`, and others.
- **Best match resolution**: Logic to determine the most relevant SEO entry when multiple matches are found.
- **Duplicate detection**: Extensible interface `ISeoDuplicatesDetector` for identifying and resolving conflicting SEO entries.
- **Broken links detection and management**: Identify and report dead or misconfigured SEO links.

## For users of previous SEO functionality

All SEO-related logic and components have been extracted into a dedicated SEO module.​ The following modules were updated to integrate with the new SEO module instead of relying on legacy SEO implementations:​

* [xAPI](https://github.com/VirtoCommerce/vc-module-x-api/releases/tag/3.915.0)
* [xCatalog​](https://github.com/VirtoCommerce/vc-module-x-catalog/releases/tag/3.919.0)
* [Catalog​](https://github.com/VirtoCommerce/vc-module-catalog/releases/tag/3.868.0)
* [Sitemaps​](https://github.com/VirtoCommerce/vc-module-sitemaps/releases/tag/3.816.0)
* [Store​](https://github.com/VirtoCommerce/vc-module-store/releases/tag/3.818.0)
* [Customer​](https://github.com/VirtoCommerce/vc-module-customer/releases/tag/3.833.0)
* [xProfile](https://github.com/VirtoCommerce/vc-module-profile-experience-api/releases/tag/3.917.0)
* [Content​](https://github.com/VirtoCommerce/vc-module-content/releases/tag/3.827.0)
* [Pages​](https://github.com/VirtoCommerce/vc-module-pages/releases/tag/3.808.0)
* [Catalog personalization​](https://github.com/VirtoCommerce/vc-module-catalog-personalization/releases/tag/3.804.0)
* [Catalog publishing​](https://github.com/VirtoCommerce/vc-module-catalog-publishing/releases/tag/3.806.0)
* [Dynamic associations](https://github.com/VirtoCommerce/vc-module-dynamic-associations/releases/tag/3.807.0)
* [xCart​](https://github.com/VirtoCommerce/vc-module-x-cart/releases/tag/3.918.0)

All SEO-related services and models in the core module have been marked as **Obsolete**. Update your custom extensions to use the new SEO module.​

### Breaking changes

To keep using SEO functionality:

* You need to install Seo module for e-commerce bundle.​
* If you have custom code referencing SEO functionality in the core module, you should migrate to SEO module.​


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../taxes/new-tax-provider-registration">← Registering new tax provider </a>
    <a href="../add-seo-to-module">Adding SEO capabilities to module →</a>
</div>
