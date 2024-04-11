# Algolia

The Virto Commerce **Algolia Search** module implements `ISearchProvider` defined in the VirtoCommerce.Core module and uses Algolia search cloud service [Algolia Search](https://algolia.com).

[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-algolia-search/)

## Configuration

Configure the Algolia search provider using the following schema:

| Node                                       | Default or Sample Value                    | Description                                                                    |
| -------------------------------------------| -------------------------------------------| -------------------------------------------------------------------------------|
| Search.Provider                            | `"AlgoliaSearch"`                          | Name of the search provider, which must be set to `AlgoliaSearch`.             |
| Search.AlgoliaSearch.ApiId                 |                                            | The API id for Algolia server.                                                 |
| Search.AlgoliaSearch.ApiKey                |                                            | The API key for either Algolia server.                                         |


**Example**

```json title="appsettings.json"
"AlgoliaSearch": {
    "AppId": "API_ID",
    "ApiKey": "API_KEY"
}
```
