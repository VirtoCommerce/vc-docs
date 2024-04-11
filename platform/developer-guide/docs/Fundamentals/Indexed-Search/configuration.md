# Configuration

This section explains the basic configuration for the indexed search logic via the [appsettings.json file](../../Configuration-Reference/appsettingsjson.md#search).

## Search

This node configures full text search for the `VirtoCommerce.Search` module.

| Node                        | Default or sample value   | Description                                                                                                                                   |
| ----------------------------| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Provider                    | `"Lucene"`                | This **required** setting specifies the current search provider. The supported values are:<ul> <li>`ElasticSearch`</li> <li>`ElasticAppSearch`</li> <li>`ElasticSearch8`</li> <li>`Lucene`</li> <li>`AzureSearch`</li> <li>`AlgoliaSearch`</li> </ul>      |
| Scope                       | `"default"`               | This setting determines the scope to use and is **required**.                                                                                 |


**Examples**

Configure the search provider modules and activate them in the `Search.Provider` section, providing connection parameters as specified in the module documentation:

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

Tailor the search provider per document type to optimize search performance and functionality. Configure the provider for each document type as needed:

```json title="appsettings.json"
{
  "Search": {
    "Provider": "ElasticAppSearch",
    "DocumentScopes": [
      {
        "DocumentType": "Category",
        "Provider": "ElasticSearch8"
      }
    ]
  }
}
```