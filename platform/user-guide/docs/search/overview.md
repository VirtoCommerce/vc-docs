# Overview

The **Search** module (called **Search Index** in the Platform menu) provides a comprehensive solution for indexed search functionality, offering full-text search capability, extensible document models, and multi-document support. It enables efficient indexing, querying, and management of search data for various e-commerce entities, empowering administrators to optimize search experiences for end-users.

[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-search)

[![Latest release](media/latest_release.png)](https://github.com/VirtoCommerce/vc-module-search/releases)


## Providers

The Search module defines common abstractions for indexed search functionality across various search engines, providing flexibility and scalability for e-commerce search solutions. The Virto Commerce Platform is search provider agnostic, allowing different search modules to be installed separately to better meet user preferences. Create a custom search provider to integrate with the search engine or choose from a range of well-know search engines:

* [Elastic Search 8](https://github.com/VirtoCommerce/vc-module-elastic-search-8): Version compatible with Elasticsearch 8.x. For driving innovation like semantic and hybrid search.
* [Elastic App Search](https://github.com/VirtoCommerce/vc-module-elastic-app-search): Preferred search provider with rich no-code search customization and analytics tools.
* [Lucene](https://github.com/VirtoCommerce/vc-module-lucene-search): Recommended for local development mode.
* [Elastic Search](https://github.com/VirtoCommerce/vc-module-elastic-search): Version compatible with Elasticsearch 7.x.
* [Azure Cognitive Search](https://github.com/VirtoCommerce/vc-module-azure-search): A fully managed cloud search service offered by Microsoft Azure that enables developers to build powerful search capabilities into applications without the need for managing infrastructure. 
* [Algolia](https://github.com/VirtoCommerce/vc-module-algolia-search): A cloud-based search platform that provides developers with a set of APIs to easily implement fast and relevant search experiences in their applications. 

!!! note
    There should be at least one search engine installed.

!!! note
    You have two installation options for search providers:

    1. Begin by installing the **Search** module, then add the required search provider module.
    2. Alternatively, install the required search provider module, and the **Search** module will be automatically installed alongside it.

## Key Features

With the **Search** module:

* Full-text search capability is provided.
* Extensible document model is available.
* Multi-document support is implemented, enabling indexing and search across multiple entities such as Products, Categories, Members, and Orders.
* Blue Green indexation methodology is used.
* Indexation logs are generated.
* Native integration with the Admin Back Office is included.

The diagram below illustrates the functionality of the Search module:

![Key entities](media/key-entities.png)