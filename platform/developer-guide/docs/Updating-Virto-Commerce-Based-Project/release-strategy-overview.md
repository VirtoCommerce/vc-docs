# Virto Commerce Release Strategy

Virto Commerce follows a structured release strategy designed to provide flexibility, stability, and innovation for a wide range of user needs.  To cater to various scenarios, this strategy includes:

* [Releases.](#releases)
* [Private modules.](#private-modules)
* [Bundles.](#bundles)
* [Packaged business capabilities.](#packaged-business-capabilities-pbcs)

## Releases

At Virto Commerce, we provide frequent releases for various modules, packed with new features, enhancements, and fixes. 

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

* **Alfa bundle**: Includes the latest experimental features and updates. Designed for testing and feedback, it provides early access to innovations still in development.  
* **Edge bundle**: Contains modules that are more stable than those in the Alfa Bundle but may still undergo adjustments. Ideal for early adopters seeking access to new features before full stabilization.  
* **Stable bundle**: Comprises thoroughly tested and finalized modules. These modules are considered production-ready and are recommended for use in live environments.

## Packaged Business Capabilities (PBCs)

Packaged Business Capabilities (PBCs) are a core component of Virto Commerce's modular and flexible approach, known as the Virto Atomic Architecture. These PBCs are designed to encapsulate specific business functionalities, making them an ideal choice for decision-makers across various business entities.

![Readmore](media/readmore.png){: width="25"} [Available PBCs and their installation](pbcs.md)

## Outdated strategy

Virto Commerce ensures a smooth user migration while improving the quality of the platform. This includes necessary updates that occasionally cause disruption. We manage this by using the Obsolete attribute for deprecated methods and assigning unique DiagnosticIds to track changes and provide clear references for developers.

```cs
[Obsolete("Method1 is deprecated, please use Method2 instead.", DiagnosticId = "VC0005", UrlFormat = "https://docs.virtocommerce.org/platform/user-guide/versions/virto3-products-versions/")]
public void Method1()
{
}
```

Our approach also ensures a controlled transition period. The `Obsolete` attribute typically remains active for the next two stable releases, giving our partners ample time to adapt their code to the newer alternatives. This approach is in line with our commitment to provide a smooth migration process, giving developers the necessary timeframe to adjust their implementations. 


![Readmore](media/readmore.png){: width="25"} [Install specific platform or module version](installing-specific-version.md)

![Readmore](media/readmore.png){: width="25"} [Useful tips](tips.md)