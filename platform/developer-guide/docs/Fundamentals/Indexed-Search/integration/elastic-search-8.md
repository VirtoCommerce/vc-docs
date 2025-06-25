# Elasticsearch 8

The Virto Commerce **Elasticsearch 8** module implements the `ISearchProvider` defined in the Virto Commerce Search module. It leverages the Elasticsearch engine to store indexed documents.

The module supports the following deployment options:

* Elastic Cloud 8.x
* Elasticsearch 8.x and 9.x

!!! info

    As of version [3.815.0](https://github.com/VirtoCommerce/vc-module-elastic-search-8/releases/tag/3.815.0), the Virto Commerce Elasticsearch module supports Elasticsearch 8 and 9.

    Virto Commerce follows the official Elasticsearch language client compatibility guidelines: language clients are **forward compatible** across minor versions within the same or next major Elasticsearch version.

    | Client Version | Compatible with Elasticsearch 8.x | Compatible with Elasticsearch 9.x | Compatible with Elasticsearch 10.x |
    | -------------- | --------------------------------- | --------------------------------- | ---------------------------------- |
    | 9.x            | ❌ no                              | ✅ yes                             | ✅ yes                              |
    | 8.x            | ✅ yes                             | ✅ yes                             | ❌ no                               |

    Language clients are also **backward compatible** within the same major version (e.g., a client built for 8.12 works with 8.13), though **feature parity is not guaranteed**.

    Compatibility does not ensure access to new features introduced in later Elasticsearch minor versions. A client built for 8.12 will work with 8.13, but won't expose features unique to 8.13.

    This update enables users to adopt newer Elasticsearch platforms while maintaining seamless integration with Virto Commerce.


[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-elastic-search-8/releases)

## Key features

* Full-text search with new .NET client for Elasticsearch.
* [Semantic search](semantic-search.md).
* Hybrid mode search.
* [Third party ML models support](semantic-search.md#semantic-search-and-third-party-ml-model-setup).

## Known limitations

The known limitations are: 

* The Catalog object serialization via **Store serialized catalog objects in the index** Platform settings is not implemented. Document field `__object` will not be indexed.
* Blue-Green indexation is not implemented.
* Partial indexation is not implemented.

## Configuration

Configure the Elasticsearch 8 provider using the following schema:

{%
   include-markdown "../../../Configuration-Reference/appsettingsjson.md"
   start="<!--elasticsearch8-start-->"
   end="<!--elasticsearch8-end-->"
%}


## Full-text search 
The provider performs full-text keyword searches on a documents, optionally with filters and aggregations.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../search/faceted-search">← Faceted search</a>
    <a href="../semantic-search">Semantic search →</a>
</div>