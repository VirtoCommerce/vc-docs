# Configuring Elasticsearch
Virto's [VirtoCommerce.ElasticSearch](https://github.com/VirtoCommerce/vc-module-elastic-search ) module enables integrating [Elasticsearch](https://www.elastic.co/products/elasticsearch) as a [search engine](https://doc.oroinc.com/backend/architecture/tech-stack/search-index/#search-index-overview).

!!! note
	This module only supports Elasticsearch engine versions between 6.5 and 8.0. 

**VirtoCommerce.ElasticSearch** implements `ISearchProvider` defined in the VirtoCommerce Search module and uses the Elasticsearch engine, which stores indexed documents on:

+ Standalone [Elasticsearch](https://www.elastic.co/products/elasticsearch "https://www.elastic.co/products/elasticsearch")
    
+ [Elastic Cloud](https://cloud.elastic.co/ "https://cloud.elastic.co/")
    
+ [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/ "https://aws.amazon.com/opensearch-service/") (successor to Amazon Elasticsearch Service)
    

## Configuration

To configure Elasticsearch as a search provider, use the following schema:

```json
"Search":{
         <!-- The name of the search provider and must be ElasticSearch -->
        "Provider": "ElasticSearch", 
        <!-- A common name (prefix) of all indexes. 
            Each document type is stored in a separate index. 
            Full index name is scope-{documenttype}. 
            One search service can serve multiple indexes. 
            Optional. Default value is default. -->
        "Scope": "default",
        "ElasticSearch": {
        <!-- A network address and port of the Elasticsearch server. -->
            "Server": "https://localhost:9200",
        <!-- A user name for either elastic cloud cluster or private elastic server. 
             Optional. Default value is elastic. -->
            "User": "elastic",
        <!-- A password for either elastic cloud cluster or private elastic server. Optional. -->
            "Key": "{SECRET_KEY}",
        <!-- Compatibilty with eralier version, optional. Must be set to True for ES 8.0 and higher -->
            "EnableCompatibilityMode": "true"         
         }
    }
```

### Elasticsearch v8.x

For Elasticsearch provider v8.x, the configuration string must have seven parameters; namely, you need to add these fields: **EnableCompatibilityMode** with the **true** value for using Elasticsearch v8.x or **false** for earlier version, and **CertificateFingerprint** for certificate fingerprint. You can read more about it [here](https://www.elastic.co/guide/en/elasticsearch/reference/8.1/configuring-stack-security.html).

To activate Elasticsearch integration, make the following changes to the platform configuration:

```json title="appsettings.json"
 "Search":{
        "Provider": "ElasticSearch",
        "Scope": "default",
        "ElasticSearch": {
            "Server": "https://localhost:9200",
            "User": "elastic",
            "Key": "{SECRET_KEY}",
            "EnableCompatibilityMode": "true",
            <!-- Optional -->
            "CertificateFingerprint": "{CERTIFICATE_FINGERPRINT}"
         }
    }
```

### Elasticsearch between v6.5 and v8.x

```json title="appsettings.json"
"Search":{
        "Provider": "ElasticSearch",
        "Scope": "default",
        "ElasticSearch": {
            "Server": "localhost:9200",
         }
    }
```

### Elastic Cloud

```json title="appsettings.json"
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

```json title="appsettings.json"
"Search":{
        "Provider": "ElasticSearch",
        "Scope": "default",
        "ElasticSearch": {
            "Server": "https://{master-user}:{master-user-password}@search-test-vc-c74km3tiav64fiimnisw3ghpd4.us-west-1.es.amazonaws.com;",
         }
    }
```

## Semantic search

Semantic search is a search method that helps you find data based on the intent and contextual meaning of a search query, rather than a match to query terms (lexical search).

![semantic search](media/semantic-search.gif)

Elasticsearch provides semantic search capabilities using natural language processing (NLP) and vector search. Deploying an NLP model to Elasticsearch enables it to extract text embeddings from text. Embeddings are vectors that provide a numeric representation of a text. Pieces of content with similar meaning have similar representations.

??? Example
    ![Example](media/nlp-example.png)

### NLP models

Elasticsearch offers the usage of a wide range of NLP models, including both dense and sparse vector models. Your choice of the language model is critical to the successful implementation of semantic search. By default, we recommend using the ELSER model. Elastic Learned Sparse EncodeR (ELSER) - is an NLP model trained by Elastic that allows you to perform semantic search using a sparse vector representation.

### Prerequisites

Elastic Cloud 8.9 or higher should be deployed and configured.

### Enable machine learning instances

After creating an Elastic Cloud deployment, enable machine learning capabilities:

1. Go to [deployments page](https://cloud.elastic.co/home).
1. In your deployment list, click **Manage**.
1. Click **Actions --> Edit Deployment**.
1. Find **Machine Learning instances** and set:
    * 4 GB RAM for **Size per zone**.
    * 1 zone for **Availability zones**.

    ![machine learning instances](media/machine-learning-instances.png)

1. Click **Save** and wait for configuration to apply.

### Activate machine learning model

After enabling machine learning instances, activate Machine Trained model:

1. Go to Kibana.
1. In your deployment, open **Analytics --> Machine learning --> Trained models**.
1. Select **.elser_model_1** and click **Download model**.
1. After download is finished, start the deployment by clicking the **Start deployment** button.
1. Specify the deployment ID, select the priority, and set the number of allocations and threads per allocation values.
1. Click **Start**.

![deployment](media/start-deployment.png)

### Configure pipeline ingester

To configure pipeline ingester:

1. Go to **Management --> Dev Tools**.
1. Create an ingest pipeline with an inference processor to use ELSER to infer against the data that is being ingested in the pipeline:

```
PUT _ingest/pipeline/elser-v1-pipeline
{
  "processors": [
    {
      "inference": {
        "model_id": ".elser_model_1",
        "target_field": "ml",
        "field_map": {
          "name": "text_field"
        },
        "inference_config": {
          "text_expansion": {
            "results_field": "tokens"
          }
        }
      }
    }
  ]
}
```

### Reindex and query data

To reindex data:

1. Open the Virto Commerce Platform and click **Settings** in the main menu.
1. Type **Search** to find the settings related  to the module.
1. Click **ElasticSearch8x**.
1. In the new blade, **Enable semantic search**. Make sure that semantic model ID, semantic field name and pipeline name are the same as above.
1. Click **Save** to save the changes.
    
    ![path](media/enable-elastic-search.png)

1. Click **Search Index** in the main menu.
1. Check the required items.
1. Click **Build index**.

    ![rebuild index](media/rebuild-index.png)

After indexing is complete, you can use Semantic Search.