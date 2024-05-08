# Lucene

The Virto Commerce **Lucene Search** module implements `ISearchProvider` defined in the VirtoCommerce Search module and uses Lucene search engine which stores indexed documents in a local file system.

[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-lucene-search)

## Configuration

Configure the Lucene search provider using the following schema:

{%
   include-markdown "../../../Configuration-Reference/appsettingsjson.md"
   start="<!--lucene-start-->"
   end="<!--lucene-end-->"
%}