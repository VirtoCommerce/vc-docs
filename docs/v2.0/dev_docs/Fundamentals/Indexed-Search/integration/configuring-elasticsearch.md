
# Configuring Elasticsearch
Virto's [VirtoCommerce.ElasticSearch](https://github.com/VirtoCommerce/vc-module-elastic-search ) module enables integrating [Elasticsearch](https://www.elastic.co/products/elasticsearch) as a [search engine](https://doc.oroinc.com/backend/architecture/tech-stack/search-index/#search-index-overview).

!!! note
	This module only supports Elasticsearch engine versions between 6.5 and 8.0. 

*VirtoCommerce.ElasticSearch* implements `ISearchProvider` defined in the VirtoCommerce Search module and uses the Elasticsearch engine, which stores indexed documents on:

+ Standalone [Elasticsearch](https://www.elastic.co/products/elasticsearch "https://www.elastic.co/products/elasticsearch")
    
+ [Elastic Cloud](https://cloud.elastic.co/ "https://cloud.elastic.co/")
    
+ [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/ "https://aws.amazon.com/opensearch-service/") (successor to Amazon Elasticsearch Service)
    

## Configuration

To configure Elasticsearch as a search provider, use the following schema:

```
"Search":{
         <!-- is the name of the search provider and must be ElasticSearch -->
        "Provider": "ElasticSearch", 
        <!-- is a common name (prefix) of all indexes. 
            Each document type is stored in a separate index. 
            Full index name is scope-{documenttype}. 
            One search service can serve multiple indexes. 
            Optional. Default value is default. -->
        "Scope": "default",
        "ElasticSearch": {
        <!-- is a network address and port of the Elasticsearch server. -->
            "Server": "https://localhost:9200",
        <!-- is a user name for either elastic cloud cluster or private elastic server. 
             Optional. Default value is elastic. -->
            "User": "elastic",
        <!-- is a password for either elastic cloud cluster or private elastic server. Optional. -->
            "Key": "{SECRET_KEY}",
        <!-- compatibilty with eralier version. optional -->
            "EnableCompatibilityMode": "true",
            "CertificateFingerprint": "{CERTIFICATE_FINGERPRINT}"
         }
    }
```

### Elasticsearch v8.x

For Elasticsearch provider v8.x, the configuration string must have seven parameters; namely, you need to add these fields: **EnableCompatibilityMode** with the **true** value for using Elasticsearch v8.x or **false** for earlier version, and **CertificateFingerprint** for certificate fingerprint. You can read more about it [here](https://www.elastic.co/guide/en/elasticsearch/reference/8.1/configuring-stack-security.html).

To activate Elasticsearch integration, make the following changes to the platform configuration:

`appsettings.json`

```
 "Search":{
        "Provider": "ElasticSearch",
        "Scope": "default",
        "ElasticSearch": {
            "Server": "https://localhost:9200",
            "User": "elastic",
            "Key": "{SECRET_KEY}",
            "EnableCompatibilityMode": "true",
            "CertificateFingerprint": "{CERTIFICATE_FINGERPRINT}"
         }
    }
```

### Elasticsearch between v6.5 and v8.x

`appsettings.json`

```
"Search":{
        "Provider": "ElasticSearch",
        "Scope": "default",
        "ElasticSearch": {
            "Server": "localhost:9200",
         }
    }
```

### Elastic Cloud

`appsettings.json`

```
"Search":{
        "Provider": "ElasticSearch",
        "Scope": "default",
        "ElasticSearch": {
            "Server": "https://4fe3ad462de203c52b358ff2cc6fe9cc.europe-west1.gcp.cloud.es.io:9243",
            "Key": "{SECRET_KEY}",
         }
    }
```

### Amazon OpenSearch Service

`appsettings.json`

```
"Search":{
        "Provider": "ElasticSearch",
        "Scope": "default",
        "ElasticSearch": {
            "Server": "https://{master-user}:{master-user-password}@search-test-vc-c74km3tiav64fiimnisw3ghpd4.us-west-1.es.amazonaws.com;",
         }
    }
```