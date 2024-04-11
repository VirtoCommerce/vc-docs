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

| Node                                       | Default or Sample Value                    | Description                                                                      |
| -------------------------------------------| -------------------------------------------| ---------------------------------------------------------------------------------|
| Search.Provider                            | `"ElasticSearch8"`                         | Specifies the search provider name, which must be set<br>to `"ElasticSearch8"`.       |
| Search.Scope                               | `"default"`                                | (Optional) Specifies the common name (prefix) for all indexes.<br> Each document type is stored in a separate index, and<br> the full index name is `scope-{documenttype}`. <br>This allows one search service to serve multiple indexes. <br>Its default value is `default`.                                           |
| Search.ElasticSearch8.Server                |                                           | Specifies the network address and the port <br>of the Elasticsearch8 server.         |
| Search.ElasticSearch8.User                  | `"elastic"`                               | Specifies the username for the Elasticsearch8 server.                            |
| Search.ElasticSearch8.Key                   |                                           | (Optional) Specifies the password for the <br>Elasticsearch8 server.                 |
| Search.ElasticSearch8.CertificateFingerprint |                                          | (Optional) During development, you can provide <br>the server certificate fingerprint. <br>When present, it is used to validate the certificate sent by the server. <br>The fingerprint is expected to be the hex string <br>representing the SHA256 public key fingerprint.                                         |

**Examples**

Configure local v8.x server:

```json title="appsettings.json"
"Search": {
    "Provider": "ElasticSearch8",
    "Scope": "default",
    "ElasticSearch8": {
        "Server": "https://localhost:9200",
        "User": "elastic",
        "Key": "{PASSWORD}"
    }
}
```

Configure Elastic Cloud v8.x:

```json title="appsettings.json"
"Search": {
    "Provider": "ElasticSearch8",
    "Scope": "default",
    "ElasticSearch8": {
        "Server": "https://vcdemo.es.eastus2.azure.elastic-cloud.com",
        "User": "elastic",
        "Key": "{SECRET_KEY}"
    }
}
```


## Full-Text Search 
The provider performs full-text keyword searches on a documents, optionally with filters and aggregations.
