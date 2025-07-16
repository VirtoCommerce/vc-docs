# Overview

The **xRecommend** (**Recommendations**) module displays recommendations to the current product. These recommendations help users expand their search and explore more broadly by suggesting similar or complementary items. This allows users to discover alternatives even if they don’t find an exact match:

![Recommendations](media/recommendations.png)

In the cart, it also shows recently browsed products:

![Recently browsed products](media/recently-browsed-products.png){: width="750"}

In the product page after **Products related to this item** block, you can also display items that other customers frequently bought together with those the current user is purchasing:

![Other customers bought](media/other-customers-bought.png)

Although the xRecommend module does not have its own user interface, you need to have it installed to manage recommendations. 

[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-x-recommend)

[![Download](media/latest_release.png)](https://github.com/VirtoCommerce/vc-module-x-recommend/releases)

## Prerequisites

* [xAPI module](https://github.com/VirtoCommerce/vc-module-x-api) module version 3.800 or higher.
* [xCatalog module](https://github.com/VirtoCommerce/vc-module-x-catalog) module version 3.800 or higher.
* [ElasticSearch8 module](https://github.com/VirtoCommerce/vc-module-elastic-search-8) module module version 3.805 or higher.
* [Semantic Search and ELSER model](https://github.com/VirtoCommerce/vc-module-elastic-search-8?tab=readme-ov-file#semantic-search-and-elser-model-setup) should be set up for Elastic Search 8 module.

## Key features

* **Semantic similarity**: Machine learning-based product recommendations using Elastic Search.
* **Customizability**: Adjustable parameters, including the number of recommendations.
* **Extensibility**: Support for extending the **related-products model** or adding custom algorithms.
* **Integration simplicity**: Toggle setting for enabling or disabling recommendations in your store.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../rating-reviews/overview">← Rating and Reviews module overview</a>
    <a href="../enable-recommendations">Enabling recommendations →</a>
</div>