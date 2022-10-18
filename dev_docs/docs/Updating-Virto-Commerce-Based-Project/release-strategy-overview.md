# Virto Commerce Release Strategy

Here at Virto Commerce, we publish new releases for different modules with features, enhancements, and fixes daily.

Generally, we have three release channels: ***Stable***, ***Edge***, and ***Preview***.

Depending on your requirements and development cycle, you can choose a strategy for the appropriate release type.

## Stable Releases

Releases in the ***Stable*** channel have passed our full regression, E2E, and load testing, and are recommended to all users to avoid issues and maximize capabilities.

Every quarter, we publish a new stable release in our [Stable Release Module Manifest](https://github.com/VirtoCommerce/vc-modules/blob/master/modules_v3.json) on GitHub. You can use it with Virto Commerce CLI to apply updates.

If we fix a bug, we release a hotfix for the two latest stable releases.

We recommend using it for maintenance updates and new solution development.

## Edge Releases

The ***Edge*** channel provides you with an opportunity to be among the first to try the latest updates, performance improvements, and new features, all with minimum risk.

We publish edge releases for various modules every single day. You can find more information about our releases on the [Virto Commerce GitHub repository](https://github.com/VirtoCommerce ) and in the [Module Manifest](https://github.com/VirtoCommerce/vc-modules/blob/master/modules_v3.json) file.

By default, Virto Commerce CLI works with edge releases.

We recommend using such releases if you want to keep up to date and get access to some features faster.

## Preview Releases

The releases in the **Preview** channel show what we are working on right now. Such releases may still have some bugs, as we want to share our new features with you as soon as possible.

Usually, we create a preview release for either PR or contribution, so that we could verify the implementation process and align it at an early stage.


## More Details
Check out these guides for more details:

+ [Installing stable releases](stable-releases.md)
+ [Installing edge releases](edge-releases.md)
+ [Installing specific platform or module version](installing-specific-version.md)
+ [Useful tips](tips.md)
