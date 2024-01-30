
Virto's [VirtoCommerce.AzureSearch](https://github.com/VirtoCommerce/vc-module-azure-search) module enables integrating  [Azure Cognitive Search](https://azure.microsoft.com/en-us/services/search/) as a [search engine](https://doc.oroinc.com/backend/architecture/tech-stack/search-index/#search-index-overview).

`VirtoCommerce.AzureSearch` implements `ISearchProvider` defined within the VirtoCommerce Search module and uses Azure Cognitive Search Engine, which stores indexed documents

## Configuration

You can configure the Azure Cognitive Search provider using the following schema:

```json
"Search":{
         <!-- The name of the search provider and must be AzureSearch-->
        "Provider": "AzureSearch", 
        <!-- A common name (prefix) of all indexes. 
            Each document type is stored in a separate index. 
            Full index name is scope-{documenttype}. 
            One search service can serve multiple indexes. 
            Optional. Default value is default. -->
        "Scope": "default",
        "AzureSearch": {
        <!--  The name of the search service instance in your Azure account, e.g.: SERVICENAME.search.windows.net. -->
            "SearchServiceName": "SERVICENAME.search.windows.net",
        <!-- The primary or secondary admin key for this search service. -->
            "AccessKey": "<<key value>>"     
         }
    }
```

## Example

```json title="appsettings.json"
"Search":{
        "Provider": "AzureSearch",
        "Scope": "default",
```
