# Migration to New xAPI Modules

In July 2024, we migrated to a new xAPI architecture to better support the evolving needs of our business API with GraphQL. The **VirtoCommerce.ExperienceApi** module has been replaced with a suite of new, more specialized modules. This change is part of our effort to simplify business API development and streamline our release cycle.

## Actions required

Please migrate from the legacy **VirtoCommerce.ExperienceApi** module to the new modules listed below:

* [xAPI](https://github.com/VirtoCommerce/vc-module-x-api): Core business API module.
* [xCart](https://github.com/VirtoCommerce/vc-module-x-cart): Cart-related functionalities management.
* [xCatalog](https://github.com/VirtoCommerce/vc-module-x-catalog): Catalog-related operations management.
* [xCMS](https://github.com/VirtoCommerce/vc-module-x-cms): Content Management System integration.
* [xOrder](https://github.com/VirtoCommerce/vc-module-x-order): Order processing.


## Breaking changes

### Frontend

* **GraphQL schema compatibility**: All GraphQL schemas remain compatible, so no frontend modifications are required directly due to schema changes.

    !!! note
        Deprecated **validateCoupon** mutation was removed. Use **validateCoupon** query instead.

* **API endpoint changes**: If your frontend directly calls endpoints provided by **VirtoCommerce.ExperienceApi**, verify and update the endpoint URLs to match the new module structure if necessary.
* **Testing**: Thoroughly test frontend interactions to ensure smooth functionality with the new backend modules.

### Custom modules

* **Dependency changes**: Custom modules that depended on **VirtoCommerce.ExperienceApi** will need to be updated to depend on the appropriate new modules (**VirtoCommerce.Xapi**, **VirtoCommerce.XCart**, **VirtoCommerce.XCatalog**, **VirtoCommerce.XCMS**, **VirtoCommerce.XOrder**).
* **Uninstall old packages**: Ensure to uninstall the NuGet packages from **VirtoCommerce.ExperienceApi** and replace them with the new packages.
* **Code adjustments**: Review and adjust your code to align with the new module structures and namespaces.

## Update path

To migrate to the new modules:

1. Uninstall **VirtoCommerce.ExperienceApi**.
1. Install the new modules:
    * [xAPI](https://github.com/VirtoCommerce/vc-module-x-api)
    * [xCart](https://github.com/VirtoCommerce/vc-module-x-cart)
    * [xCatalog](https://github.com/VirtoCommerce/vc-module-x-catalog)
    * [xCMS](https://github.com/VirtoCommerce/vc-module-x-cms)
    * [xOrder](https://github.com/VirtoCommerce/vc-module-x-order)

1. Update other modules to the new version if required, ensuring they now depend on **VirtoCommerce.Xapi**:
    * [MarketingExperienceApi](https://github.com/VirtoCommerce/vc-module-marketing-experience-api/releases/latest)
    * [Quote](https://github.com/VirtoCommerce/vc-module-quote/releases/latest)
    * [CustomerReviews](https://github.com/VirtoCommerce/vc-module-customer-review/releases/latest)
    * [Skyflow](https://github.com/VirtoCommerce/vc-module-skyflow/releases/latest)
    * [TaskManagement](https://github.com/VirtoCommerce/vc-module-task-management/releases/latest)
    * [File xAPI](https://github.com/VirtoCommerce/vc-module-file-experience-api/releases/latest)
    * [WhiteLabeling](https://github.com/VirtoCommerce/vc-module-white-labeling/releases/latest)

1. For any custom modules, uninstall the NuGet packages from **VirtoCommerce.ExperienceApi** and replace them with the new ones.
1. Models, service interfaces, GraphQL schema types, and input types, commands, queries, and aggregates are moved to respective Core projects of the new modules (**XCatalog.Core**, **XCart.Core**, etc.) with namespaces adjusted. Data projects contain service implementations, command and query builders, command and query handlers, and middleware.


## Update and support

**VirtoCommerce.ExperienceApi** is archived and will be supported in Stable 8 and Stable 9 releases. Future developments will focus on the new VirtoCommerce.Xapi and related modules. The latest Edge release has adopted the new modules.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../enable-embedded-mode-for-vc-shell">← Enabling embedded mode for VC-Shell instances </a>
    <a href="../../../Updating-Virto-Commerce-Based-Project/release-strategy-overview">Release strategy  →</a>
</div>