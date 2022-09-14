
Virto's [VirtoCommerce.AzureSearch](https://github.com/VirtoCommerce/vc-module-azure-search) module enables integrating  [Azure Cognitive Search](https://azure.microsoft.com/en-us/services/search/) as a [search engine](https://doc.oroinc.com/backend/architecture/tech-stack/search-index/#search-index-overview).

`VirtoCommerce.AzureSearch` implements `ISearchProvider` defined within the VirtoCommerce Search module and uses Azure Cognitive Search Engine, which stores indexed documents

## Configuration

You can configure the Azure Cognitive Search provider using the following schema:

```
"Search":{
         <!-- is the name of the search provider and must be AzureSearch-->
        "Provider": "AzureSearch", 
        <!-- is a common name (prefix) of all indexes. 
            Each document type is stored in a separate index. 
            Full index name is scope-{documenttype}. 
            One search service can serve multiple indexes. 
            Optional. Default value is default. -->
        "Scope": "default",
        "AzureSearch": {
        <!--  is the name of the search service instance in your Azure account Ex: SERVICENAME.search.windows.net. -->
            "SearchServiceName": "SERVICENAME.search.windows.net",
        <!-- is the primary or secondary admin key for this search service. -->
            "AccessKey": "<<key value>>"     
         }
    }
```

## Example

`appsetings.json`
```
"Search":{
        "Provider": "AzureSearch",
        "Scope": "default",
```
