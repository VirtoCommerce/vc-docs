# OpenSearch

The Virto Commerce **OpenSearch** module implements `ISearchProvider` defined in the Virto Commerce Search module and uses the OpenSearch engine to store indexed documents.

[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-open-search)

The module supports the following OpenSearch deployment options:

* [OpenSearch.](https://opensearch.org/)
* [Amazon OpenSearch Service.](https://aws.amazon.com/opensearch-service/)

![Read more](media/readmore.png){: width="20"} [How OpenSearch works](/platform/user-guide/opensearch/overview)

## Configuration

To configure OpenSearch as a search provider, use the following schema:

{%
   include-markdown "../../../Configuration-Reference/appsettingsjson.md"
   start="<!--opensearch-start-->"
   end="<!--opensearch-end-->"
%}


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../configuring-elasticsearch">← Elasticsearch</a>
    <a href="../configuring-azure-cognitive-search">Azure Cognitive Search →</a>
</div>