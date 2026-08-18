# Overview

The **xFrontend** module provides a set of optimized backend queries designed specifically to improve rendering performance and enhance frontend user experience scenarios. This module introduces a unified GraphQL query that consolidates several commonly requested data types into a single optimized call. This reduces network round-trips and simplifies frontend integration.

This module is intended to be installed in a Virto Commerce backend as part of a frontend integration strategy. Once enabled, the unified **pageContext** query becomes available to clients consuming the Virto GraphQL API - typically storefronts, SSR apps, or SPA frameworks.

[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-tax)

[![Download](media/latest_release.png)](https://github.com/VirtoCommerce/vc-module-tax/releases)


## Key features

* Optimized queries tailored for frontend rendering needs.
* Single GraphQL endpoint delivering combined contextual data.
* Aggregated page information retrieval for efficient rendering.
* Extended GraphQL schema with a new **pageContext** query returning:
    * **SlugInfoType**.
    * **StoreType**.
    * **WhiteLabelingSettingsType**.
    * **UserType**.

![Read more](media/readmore.png){: width="20"} [pageContext query](../../../developer-guide/GraphQL-Storefront-API-Reference-xAPI/xFrontend/PageContext)


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../event-bus/overview">← Event Bus module overview</a>
    <a href="../../gdpr/overview">GDPR module overview →</a>
</div>