# Overview

Virto Commerce Intent Search is an advanced AI-powered search intent classification and product categorization module that intelligently analyzes search queries and classifies products for e-commerce platforms. Built with enterprise-grade multi-tenancy, performance monitoring, and flexible configuration capabilities, it transforms how your platform understands customer search intent and categorizes products.

![Read more](media/readmore.png){: width="20"} [How Intent Search works](../../../../user-guide/intent-search/overview)

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

[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-intent-search)

[![Release](media/latest_release.png)](https://github.com/VirtoCommerce/vc-module-intent-search/releases)

## Architecture

The Intent Search architecture combines AI-powered semantic understanding, multi-tenant data isolation, and high-performance vector search to deliver accurate, context-aware search transformations. It integrates external AI services (Hugging Face for embeddings and Weaviate for semantic vector search) and orchestrates multiple classifiers to interpret user intent and categorize products:

* Multi-tenant design:
    * Organization-based tenancy: Each Virto Commerce organization automatically maps to a separate Weaviate tenant.
    * Data isolation: Complete separation of data between tenants at the database level.
    * Transparent operation: Existing APIs work without modification.

* AI Classification pipeline:
    * Input processing: Parse and tokenize search queries or product information.
    * Multi-classifier analysis: Run specialized classifiers to identify intent classes:
        * ExactId: Specific product codes (SKU, MPN, GTIN, EAN).
        * StandardCode: Standard classification codes (UNSPSC, HS, ISO).
        * BrandModel: Brand and model identification.
        * ProductType: Category keywords.
        * SymptomJob: Problem/task-based searches.
        * UseCase: Scenario/theme-based queries.
        * Feature: Material, color, size attributes.
        * TechnicalSpec: Technical specifications and measurements.
        * Price: Price and budget information.
        * Dimension: Physical measurements.
        * And 7 additional specialized classes.
    * Confidence scoring: Each classifier provides confidence levels.
    * Result aggregation: Combine results with intelligent weighting.

* Performance monitoring:
    * Non-intrusive tracking: Monitor performance without impacting API response times.
    * Complete context storage: Full request/response logging for debugging.
    * Correlation-based analysis: Link performance data to specific requests.
    * Real-time insights: Immediate availability of performance metrics.

## Configuration

The module provides flexible configuration options that allow organizations to tailor intent detection, taxonomy behavior, and performance monitoring to their specific business needs. Settings can be adjusted per tenant, ensuring precise control and full isolation across environments.

### Tenant settings

Each tenant can customize:

* Taxonomy selection: Choose which taxonomies to use for categorization.
* Classifier configuration: Enable/disable specific classifiers and set custom regex patterns.
* Quality thresholds: Set confidence levels and result filtering.
* Processing settings: Configure caching, batch processing, and performance tuning.

### Performance monitoring

Configure monitoring behavior:

* Sampling rate: Control what percentage of requests to monitor.
* Retention policies: Set how long to keep performance data.
* Cache settings: Optimize performance data retrieval.



<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../Indexed-Search/overview">← Indexed Search overview</a>
    <a href="../installation-and-configuration">Installation and configuration →</a>
</div>
