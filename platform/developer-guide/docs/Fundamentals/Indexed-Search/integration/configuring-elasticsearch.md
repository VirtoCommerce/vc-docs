# Elasticsearch

The Virto Commerce **Elasticsearch** module enables integrating [Elasticsearch](https://www.elastic.co/products/elasticsearch) as a [search engine](https://doc.oroinc.com/backend/architecture/tech-stack/search-index/#search-index-overview).

ElasticSearch implements **ISearchProvider** defined in the Virto Commerce Search module and uses the Elasticsearch engine, which stores indexed documents on:

* Standalone [Elasticsearch](https://www.elastic.co/products/elasticsearch "https://www.elastic.co/products/elasticsearch")
* [Elastic Cloud](https://cloud.elastic.co/ "https://cloud.elastic.co/")
* [OpenSearch](https://opensearch.org/)
* [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/ "https://aws.amazon.com/opensearch-service/")
    
[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-elastic-search/)

## Configuration

To configure Elasticsearch as a search provider, use the following schema:

| Node                                       | Default or Sample Value                    | Description                                                                     |
| -------------------------------------------| -------------------------------------------| -------------------------------------------------------------------------------|
| Search.Provider                            | `"ElasticSearch"`                           | Specifies the search provider name, which must be set to "ElasticSearch".       |
| Search.Scope                               | `"default"`                                 | Specifies the common name (prefix) for all indexes. Each document type is stored in a separate index, and the full index name is `scope-{documenttype}`. This allows one search service to serve multiple indexes. The key is optional. Its default value is `default`.|
| Search.ElasticSearch.Server                |                                             | Specifies the network address and port of the Elasticsearch server.               |
| Search.ElasticSearch.User                  | `"elastic"`                                 | Specifies the username for either the Elastic Cloud cluster or private Elasticsearch server. |
| Search.ElasticSearch.Key                   |                                             | (Optional) Specifies the password for either the Elastic Cloud cluster or private Elasticsearch server. |
| Search.ElasticSearch.EnableCompatibilityMode | `false`                                   | (Optional) Set this to "true" to use Elasticsearch v8.x or "false" (default) for earlier versions. |
| Search.ElasticSearch.EnableHttpCompression | `false`                                     | (Optional) Set this to "true" to enable gzip compressed requests and responses or "false" (default) to disable compression. |
| Search.ElasticSearch.CertificateFingerprint |                                            | During development, you can provide the server certificate fingerprint. When present, it is used to validate the certificate sent by the server. The fingerprint is expected to be the hex string representing the SHA256 public key fingerprint.  |

**Examples**

=== "Elastic Cloud v8.x"

    !!! note
        Virto Commerce has its native [Elasticsearch 8.x module](https://github.com/VirtoCommerce/vc-module-elastic-search-8). The current module works with Elasticsearch 8.x in compatibility mode.

    Enable the compatibility mode for Elastic Cloud v8.x:

    ```json title="appsettings.json"
    "Search": {
        "Provider": "ElasticSearch",
        "Scope": "default",
        "ElasticSearch": {
            "EnableCompatibilityMode": "true",
            "Server": "https://4fe3ad462de203c52b358ff2cc6fe9cc.europe-west1.gcp.cloud.es.io:9243",
            "User": "elastic",
            "Key": "{SECRET_KEY}"
        }
    }
    ```

=== "Elasticsearch v8.x"

    Configure Elasticsearch v8.x without security features enabled:

    ```json title="appsettings.json"
    "Search": {
        "Provider": "ElasticSearch",
        "Scope": "default",
        "ElasticSearch": {
            "EnableCompatibilityMode": "true",
            "Server": "https://localhost:9200"
        }
    }
    ```

    Configure Elasticsearch v8.x with ApiKey authorization:

    ```json title="appsettings.json"
    "Search": {
        "Provider": "ElasticSearch",
        "Scope": "default",
        "ElasticSearch": {
            "EnableCompatibilityMode": "true",
            "Server": "https://localhost:9200",
            "User": "{USER_NAME}",
            "Key": "{SECRET_KEY}"
        }
    }
    ```

=== "Elastic Cloud v7.x"

    Configure Elastic Cloud v7.x as follows:

    ```json title="appsettings.json"
    "Search": {
        "Provider": "ElasticSearch",
        "Scope": "default",
        "ElasticSearch": {
            "Server": "https://4fe3ad462de203c52b358ff2cc6fe9cc.europe-west1.gcp.cloud.es.io:9243",
            "User": "elastic",
            "Key": "{SECRET_KEY}"
        }
    }
    ```

=== "Elasticsearch v7.x"

    Configure Elasticsearch v7.x without security features enabled:

    ```json title="appsettings.json"
    "Search": {
        "Provider": "ElasticSearch",
        "Scope": "default",
        "ElasticSearch": {
            "Server": "https://localhost:9200"
        }
    }
    ```

    Configure Elasticsearch v7.x with ApiKey authorization:

    ```json title="appsettings.json"
    "Search": {
        "Provider": "ElasticSearch",
        "Scope": "default",
        "ElasticSearch": {
            "Server": "https://localhost:9200",
            "User": "{USER_NAME}",
            "Key": "{SECRET_KEY}"
        }
    }
    ```

=== "Amazon OpenSearch Service"

    Configure Amazon OpenSearch Service:

    ```json title="appsettings.json"
    "Search": {
        "Provider": "ElasticSearch",
        "Scope": "default",
        "ElasticSearch": {
            "Server": "https://{master-user}:{master-user-password}@search-test-vc-c74km3tiav64fiimnisw3ghpd4.us-west-1.es.amazonaws.com"
        }
    }
    ```




<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../search_relevance_tuning">← Improving search relevance</a>
    <a href="../configuring-azure-cognitive-search">Azure cognitive search →</a>
</div>
