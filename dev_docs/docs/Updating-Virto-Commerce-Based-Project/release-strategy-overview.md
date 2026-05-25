# Virto Commerce Release Strategy

Here at Virto Commerce, we publish new releases for different modules with features, enhancements, and fixes daily.

Generally, we have three release channels: 

* [Stable](release-strategy-overview.md#stable-releases)
* [Edge](release-strategy-overview.md#edge-releases)
* [Preview](release-strategy-overview.md#preview-releases)

Depending on your requirements and development cycle, you can choose a strategy for the appropriate release type.

## Stable releases

Releases in the **Stable** channel have passed our full regression, E2E, and load testing, and are recommended to all users to avoid issues and maximize capabilities.

Every quarter, we publish a new stable release in our [Stable Release Module Manifest](https://github.com/VirtoCommerce/vc-modules/blob/master/modules_v3.json) on GitHub. You can use it with Virto Commerce CLI to apply updates.

If we fix a bug, we release a hotfix for the two latest stable releases.

We recommend using it for maintenance updates and new solution development.

## Edge releases

The **Edge** channel provides you with an opportunity to be among the first to try the latest updates, performance improvements, and new features, all with minimum risk.

We publish edge releases for various modules every single day. You can find more information about our releases on the [Virto Commerce GitHub repository](https://github.com/VirtoCommerce ) and in the [Module Manifest](https://github.com/VirtoCommerce/vc-modules/blob/master/modules_v3.json) file.

By default, Virto Commerce CLI works with edge releases.

We recommend using such releases if you want to keep up to date and get access to some features faster.

## Preview releases

The releases in the **Preview** channel show what we are working on right now. Such releases may still have some bugs, as we want to share our new features with you as soon as possible.

Usually, we create a preview release for either PR or contribution, so that we could verify the implementation process and align it at an early stage.

## Obsolete strategy

Virto Commerce ensures smooth user migration while enhancing platform quality. This involves necessary updates, occasionally causing disruptions. We manage this using the Obsolete attribute for deprecated methods, and assign unique DiagnosticId to track changes and provide clear references for developers.

```cs
[Obsolete("Method1 is deprecated, please use Method2 instead.", DiagnosticId = "VC0005", UrlFormat = "https://docs.virtocommerce.org/products/products-virto3-versions/")]
public void Method1()
{
}

```

Moreover, our approach ensures a controlled transition period. The `Obsolete` attribute typically remains active for the next two stable releases, affording our partners ample time to adapt their code to the newer alternatives. This approach aligns with our commitment to provide a smooth migration process, giving developers the necessary timeframe to adjust their implementations. 

## More details
Check out these guides for more details:

+ [Installing stable releases](stable-releases.md)
+ [Installing edge releases](edge-releases.md)
+ [Installing specific platform or module version](installing-specific-version.md)
+ [Useful tips](tips.md)
