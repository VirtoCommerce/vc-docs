# Elastic Search 8

The Virto Commerce **Elastic Search 8** module implements the `ISearchProvider` defined in the Virto Commerce Search module. It leverages the Elasticsearch engine to store indexed documents.

The module supports the following deployment options:

* Elastic Cloud 8.x
* Standalone Elasticsearch 8.x

[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-elastic-search-8/)

## Features

* Full-text search with new .NET client for Elasticsearch.
* [Semantic search](semantic-search.md).
* Hybrid mode search.
* [Third party ML models support](semantic-search.md#semantic-search-and-third-party-ml-model-setup).

## Known Limitations

The known limitations are: 

* The Catalog object serialization via **Store serialized catalog objects in the index** platform settings is not implemented. Document field `__object` will not be indexed.
* Blue-Green indexation is not implemented.
* Partial indexation is not implemented.

## Configuration

Configure the Elastic Search 8 provider using the following schema:

{%
   include-markdown "../../../Configuration-Reference/appsettingsjson.md"
   start="<!--elasticsearch8-start-->"
   end="<!--elasticsearch8-end-->"
%}


## Full-Text Search 
The provider performs full-text keyword searches on a documents, optionally with filters and aggregations.
