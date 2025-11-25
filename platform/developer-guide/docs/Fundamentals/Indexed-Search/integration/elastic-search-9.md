# Elasticsearch 9

!!! note
    As confirmed in Elastic's official resources ([Enterprise Search FAQ](https://www.elastic.co/resources/search/enterprise-search-faq) and [9.x Upgrade Guide](https://www.elastic.co/guide/en/enterprise-search/8.18/upgrading-to-9-x.html)) Standalone App Search is deprecated (fully removed in 9.x). For Elastic customers who currently use Elastic App Search product line with its included features and functionalities, these products remain available in the latest 8.x versions and will be maintained until January 15, 2027 and supported until July 15, 2027 after the official EOL announcement, according to the EOL policies. Virto Commerce will discontinue support for legacy App Search and transition all development efforts to the new **Elasticsearch 9** module.


The Virto Commerce **Elasticsearch 9** module implements the `ISearchProvider` defined in the Virto Commerce Search module. It leverages the Elasticsearch engine to store indexed documents.

The module supports the following deployment options:

* Elastic Cloud 9.x and 10.x
* Elasticsearch 9.x and 10.x

[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-elastic-search-8/releases)

## Key features

* Full-text search with new .NET client for Elasticsearch.
* [Semantic search](semantic-search-es9.md).
* Hybrid mode search.
* [Third party ML models support](semantic-search-es9.md#semantic-search-and-third-party-ml-model-setup).

## Configuration

Configure the Elasticsearch 9 provider using the following schema:

{% include-markdown "../../../Configuration-Reference/appsettingsjson.md" start="<!--elasticsearch9-start-->" end="<!--elasticsearch9-end-->" %}


## Full-text search 
The provider performs full-text keyword searches on documents, optionally with filters and aggregations.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../search/faceted-search">← Faceted search</a>
    <a href="../semantic-search-es9">Semantic search →</a>
</div>