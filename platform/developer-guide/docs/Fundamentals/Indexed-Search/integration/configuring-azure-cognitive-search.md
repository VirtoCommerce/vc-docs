# Azure Search

The Virto Commerce **Azure Search** module enables integrating  [Azure Cognitive Search](https://azure.microsoft.com/en-us/services/search/) as a [search engine](https://doc.oroinc.com/backend/architecture/tech-stack/search-index/#search-index-overview).

Azure Search implements **ISearchProvider** defined within the Virto Commerce Search module and uses Azure Cognitive Search Engine, which stores indexed documents.

[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-azure-search)

## Configuration

To configure the Azure Search provider, use the following schema:

{%
   include-markdown "../../../Configuration-Reference/appsettingsjson.md"
   start="<!--azuresearch-start-->"
   end="<!--azuresearch-end-->"
%}



