# Virto Commerce Release Strategy

Virto Commerce follows a structured release strategy designed to provide flexibility, stability, and innovation for a wide range of user needs.  To cater to various scenarios, this strategy includes:

* [Releases.](#releases)
* [Private modules.](#private-modules)
* [Bundles.](#bundles)
* [Packaged business capabilities and PBCs Max](#packaged-business-capabilities-pbcs-and-pbcs-max)

## Releases

At Virto Commerce, we provide frequent releases for various modules and the Platform, packed with new features, enhancements, and fixes. Releases are a foundation for all [bundles](#bundles) and [PBCs](#packaged-business-capabilities-pbcs).

Generally, we have three release channels: 

* [Stable.](release-strategy-overview.md#stable-releases)
* [Edge.](release-strategy-overview.md#edge-releases)
* [Preview.](release-strategy-overview.md#preview-releases)

Depending on your needs and development cycle, you can choose a release strategy that suits you best.

### Stable releases

Releases in the **Stable** channel have passed our full regression, E2E and load testing and are recommended for all users to avoid issues and maximize functionality.

By default, Virto Commerce CLI runs on stable releases.

Every quarter, we publish a new stable release in our [Stable Release Module Manifest](https://github.com/VirtoCommerce/vc-modules/blob/master/modules_v3.json) on GitHub. You can use it with Virto Commerce CLI to apply updates.

When we fix a bug, we release a hotfix for the two latest stable releases. 

We recommend using it for maintenance updates and new solution development.

![Readmore](media/readmore.png){: width="25"} [Install and update stable release](stable-releases.md)


### Edge releases

The **Edge** channel gives you the opportunity to be among the first to try the latest updates, performance enhancements, and new features with minimal risk.

We publish edge releases for various modules on a daily basis. You can find more information about our releases in the [Virto Commerce GitHub repository](https://github.com/VirtoCommerce) and in the [Module Manifest](https://github.com/VirtoCommerce/vc-modules/blob/master/modules_v3.json) file.

We recommend using these releases if you want to stay up to date and get access to some features faster.

![Readmore](media/readmore.png){: width="25"} [Install and update edge release](edge-releases.md)

### Preview releases

The releases in the **Preview** channel show what we are currently working on. These releases may still have some bugs, as we want to get our new features out to you as quickly as possible.

We usually create a preview release for either PR or Contribution so that we can review and adjust the implementation process early on.

## Private modules

Virto Commerce also offers private modules that are not included in the public repository. These modules are available to customers with specific requirements such as AI, Enterprise, High Performance, and Marketplace functionality. [Contact us](https://virtocommerce.com/request-demo) for access to private modules.

## Bundles

The release types can be combined into the following bundles to meet different needs:  

| Bundle                                     | Included releases             | Description                                                                                      |
|--------------------------------------------|-------------------------------|------------------------------------------------------------------------------------------------------|
| Alfa                                       | Preview releases              | Includes experimental features and updates for testing and feedback; provides early access to innovations in development. |
| Edge                                       | Edge releases                 | Contains more stable modules than the Alfa Bundle but may include adjustments and breaking changes; suited for early adopters. |
| [Stable](https://github.com/VirtoCommerce/vc-modules/tree/master/bundles/latest)     | Stable releases  | Comprises thoroughly tested and finalized modules; production-ready and recommended for live environments. |


## Packaged Business Capabilities (PBCs) and PBCs Max

Packaged Business Capabilities (PBCs) are a core component of Virto Commerce's modular and flexible approach, known as the Virto Atomic Architecture:

* **PBC** is a module or a group of modules (in some cases) that solves an individual business problem, such as Catalog, or logging in. 
* **PBC Max** is a combination of modules, grouped by functionality to address specific business needs, such as setting up and customizing product catalogs. The PBCs Max are designed to encapsulate specific business functionalities, making them an ideal choice for decision-makers across various business entities.

    !!! note
        Virto Commerce offers [6 preset PBCs Max](pbcs.md). However, you can create any number of custom PBCs Max to address specific business tasks.

![Readmore](media/readmore.png){: width="25"} [Available PBCs Max and their installation](pbcs.md)

![Readmore](media/readmore.png){: width="25"} [Install specific Platform or module version](installing-specific-version.md)

![Readmore](media/readmore.png){: width="25"} [Useful tips](tips.md)


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../Tutorials-and-How-tos/overview">← Tutorials and how-tos </a>
    <a href="../stable-releases">Stable releases  →</a>
</div>