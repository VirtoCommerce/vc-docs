# Azure Search

The Virto Commerce **Azure Search** module enables integrating  [Azure Cognitive Search](https://azure.microsoft.com/en-us/services/search/) as a [search engine](https://doc.oroinc.com/backend/architecture/tech-stack/search-index/#search-index-overview).

AzureSearch implements `ISearchProvider` defined within the Virto Commerce Search module and uses Azure Cognitive Search Engine, which stores indexed documents.

[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-azure-search)

## Configuration

To configure the Azure Search provider, use the following schema:

| Node                                       | Default or Sample Value                    | Description                                                                    |
| -------------------------------------------| -------------------------------------------| -------------------------------------------------------------------------------|
| Search.Provider                            | `"AzureSearch"`                            | Name of the search provider, which must be set to `AzureSearch`.               |
| Search.AzureSearch.SearchServiceName       |                                            | The name of the search service instance in your Azure account.<br>Example: `SERVICENAME.search.windows.net`.|
| Search.AzureSearch.AccessKey               |                                            | The primary or secondary admin key for this search service.                    |
| Search.AzureSearch.QueryParserType         | `Simple` <br>`Full` | Type of Query Languages. `Simple` (default) or `Full`.                         |                
| Search.Scope                               | `"default"`                                | (Optional) Specifies the common name (prefix) for all indexes.<br>Each document type is stored in a separate index,<br>and the full index name is `scope-{documenttype}`.<br>This allows one search service to serve multiple indexes. |


**Example**

```json title="appsettings.json"
"Search": {
    "Provider": "AzureSearch",
    "Scope": "default",
    "AzureSearch": {
        "SearchServiceName": "YOUR_SEARCH_SERVICE_NAME.search.windows.net",
        "AccessKey": "YOUR_SEARCH_SERVICE_ACCESS_KEY",
        "QueryParserType": "Simple"
    }
}
```
