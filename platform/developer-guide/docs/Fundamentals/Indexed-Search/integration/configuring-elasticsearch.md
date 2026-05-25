# Elasticsearch

The Virto Commerce **Elasticsearch** module enables integrating [Elasticsearch](https://www.elastic.co/products/elasticsearch) as a [search engine](https://doc.oroinc.com/backend/architecture/tech-stack/search-index/#search-index-overview).

ElasticSearch implements **ISearchProvider** defined in the Virto Commerce Search module and uses the Elasticsearch engine, which stores indexed documents on:

* Standalone [Elasticsearch.](https://www.elastic.co/products/elasticsearch "https://www.elastic.co/products/elasticsearch")
* [Elastic Cloud.](https://cloud.elastic.co/ "https://cloud.elastic.co/")
* [OpenSearch.](https://opensearch.org/)
* [Amazon OpenSearch Service.](https://aws.amazon.com/opensearch-service/ "https://aws.amazon.com/opensearch-service/")

!!! note
    **OpenSearch** and **Amazon OpenSearch Service** are also supported by the dedicated [OpenSearch module](opensearch.md), which uses the native OpenSearch client for full compatibility with OpenSearch-specific features.


[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-elastic-search/)

## Configuration

To configure Elasticsearch as a search provider, use the following schema:

{%
   include-markdown "../../../Configuration-Reference/appsettingsjson.md"
   start="<!--elasticsearch-start-->"
   end="<!--elasticsearch-end-->"
%}


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../search_relevance_tuning">← Improving search relevance</a>
    <a href="../opensearch">OpenSearch search →</a>
</div>
