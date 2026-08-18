# Overview

Virto Commerce **Intent Search** is an advanced AI-powered search intent classification and product categorization module that intelligently analyzes search queries and classifies products for ecommerce platforms. Built with enterprise-grade multi-tenancy, performance monitoring, and flexible configuration capabilities, it transforms how your platform understands customer search intent and categorizes products.

When a user enters a natural-language query (such as “HP white laptop”) the Intent Search module analyzes the text and breaks it into meaningful components. Instead of treating the whole phrase as a single keyword, the module intelligently interprets user intent and restructures the query with the help of external AI services:

* **Hugging Face**.
* **Weaviate**.

The combined workflow is as follows:

| Step | Actor           | Description                                                | Example                                                                                                         |
|------|-----------------|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| 1    | User            | Types a query                                              | **"HP laptop white"**                                                                                           |
| 2    | Hugging Face    | Converts the query into a vector and extracts key concepts | Embeds the query into a vector and identifies concepts: **HP**, **laptop**, **white**                           |
| 3    | Weaviate        | Finds matching vectors using semantic similarity           | Returns semantically closest product/category vectors (e.g., laptops with HP/white attributes)                  |
| 4    | Intent Search   | Transforms the query into structured search input          | Combines semantic matches with filters. **Keyword:** laptop; **Filters:** Brand = HP, Color = White             |
| 5    | Search provider | Performs high-performance, relevance-ranked search         | Returns final product results for HP white laptops                                                              |


As a result, the shopper sees more accurate and highly relevant products on the Frontend:

![Frontend](media/intent-search-frontend.png){: style="display: block; margin: 0 auto;" width="850"}


<br>
<br>
[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-intent-search)

[![Release](media/latest_release.png)](https://github.com/VirtoCommerce/vc-module-intent-search/releases)



## Key features

* **Lightning-fast AI classification**: Analyze search intent and categorize products in milliseconds.
* **Advanced search intent analysis**: Understand complex queries with 17 different intent classes.
* **Multi-tenant architecture**: Complete data isolation for different organizations.
* **Performance monitoring**: Deep insights into every classification operation.
* **Flexible configuration**: Tenant-specific settings and custom taxonomies.
* **Intelligent query understanding**: Parse queries like "Samsung 55 inch 4K OLED TV under $2000".
* **Technical specification detection**: Automatically identify and standardize measurements, voltages, capacities.
* **Smart facet extraction**: Match search terms to product facets for enhanced filtering.
* **Multi-classifier integration**: 17 intent classes working together for comprehensive understanding.
* **Product categorization**: Match product titles to taxonomies with confidence scoring.


![Read more](media/readmore.png){: width="20"} [Intent Search Installation](/platform/developer-guide/Fundamentals/Intent-Search/installation-and-configuration)

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../generic-export/overview">← Generic Export module overview</a>
    <a href="../../loyalty/overview">Loyalty module overview →</a>
</div>
