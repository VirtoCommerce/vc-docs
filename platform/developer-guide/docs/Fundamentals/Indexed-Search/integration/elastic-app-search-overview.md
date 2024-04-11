# Elastic App Search Overview

The Virto Commerce **Elastic App Search** module enables integrating  [Azure Cognitive Search](https://azure.microsoft.com/en-us/services/search/) as a [search engine](https://doc.oroinc.com/backend/architecture/tech-stack/search-index/#search-index-overview).

Elastic App Search provides search, aggregation, and analytic capabilities as a service, on top of ElasticSearch. It also supplies tools that can help you tune search result sets without development:

* [Relevance Tuning](https://www.elastic.co/guide/en/app-search/current/precision-tuning.html)
* [Synonyms](https://www.elastic.co/guide/en/app-search/current/synonyms-guide.html)
* [Curations](https://www.elastic.co/guide/en/app-search/current/curations-guide.html)

![Readmore](media/readmore.png){: width="25"} [Deploying Elastic App Search](https://www.elastic.co/guide/en/app-search/current/installation.html)

[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-elastic-app-search/)

## Key Features

The Elastic App Search module offers:

* Full-text search provider compatibility with Elastic App Search version 8.12 and higher.
* Boosting profile functionality.
* Dynamic boosting concatenation, combining dynamic boosting with query and static boosting from the Search Relevance Tuning panel.

## Configuration

Configures the Elastic App Search using the following schema:

| Node                                       | Default or Sample Value                    | Description                                                                    |
| -------------------------------------------| -------------------------------------------| -------------------------------------------------------------------------------|
| Search.Provider                            | `"ElasticAppSearch"`                       | Name of the search provider, which must be set to `ElasticAppSearch`           |
| Search.Scope                               | `"default"`                                | (Optional) Specifies the common name (prefix) for all indexes. Each document type is stored in a separate index, and the full index name is `scope-{documenttype}`. This allows one search service to serve multiple indexes. Its default value is set to `default`.|
| Search.ElasticAppSearch.Endpoint           |                                            | Network address and port of the ElasticAppSearch server. |
| Search.ElasticAppSearch.PrivateApiKey      |                                            | API access key that can read and write against all available API endpoints. Prefixed with `private-`.|
| Search.ElasticAppSearch.KibanaBaseUrl      |                                            | Kibana base URL for accessing the Kibana Dashboard from the application menu.|
| Search.ElasticAppSearch.KibanaPath         |                                            | Path to the App Search engine in the Kibana Dashboard. Default value is `/app/enterprise_search/app_search/engines/`.

!!! note
    Endpoint and API key can be managed in the Credential menu within the App Search Dashboard panel.

**Examples**

```json title="appsettings.json"
	"Search": {
		"Provider": "ElasticAppSearch",
		"Scope": "default",
		"ElasticAppSearch": {
				"Endpoint": "https://localhost:3002",
			"PrivateApiKey": "private-key",
		  "KibanaBaseUrl": "https://localhost:5601"
		}
	}
```
### Dynamic Boosting

The Elastic App Search provider combines static boosting from the Search Relevance Tuning panel with dynamic boosting that can be passed at runtime.

Dynamic Boosting supports both Value Boost and Functional Boosting.

Define Boost Presets as follows:

```json title="appsettings.json"
	"Search": {
		"Provider": "ElasticAppSearch",
		"Scope": "default",
		"ElasticAppSearch": {
		  "Endpoint": "https://localhost:3002",
		  "PrivateApiKey": "private-key",
		  "KibanaBaseUrl": "https://localhost:5601",

		  "BoostPresets": [
			{
			  "Name": "High",
			  "Type": "value",
			  "Operation": "add",
			  "Factor": 5,
			  "IsDefault": true
			},
			{
			  "Name": "Medium",
			  "Type": "value",
			  "Operation": "add",
			  "Factor": 3
			},
			{
			  "Name": "LOw",
			  "Type": "value",
			  "Operation": "add",
			  "Factor": 3
			}
		  ]
		}
	  }
```    

Pass SearchBoost with Search Request:

```json title="appsettings.json"
searchRequest.Boosts = [new SearchBoost
	  {
				FieldName = "brand",
				Value = "Apple",
				Preset = "Medium",
		}];
```

## Performance

After running load tests and comparing Elasticsearch Vs Elastic App Search, we can confirm that both engines are ready for production and demonstrate the same results.

## Limitations

![Readmore](media/readmore.png){: width="25"} [App Search Limitations](https://www.elastic.co/guide/en/app-search/8.3/limits.html)