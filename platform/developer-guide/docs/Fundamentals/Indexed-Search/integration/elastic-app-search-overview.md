# Elastic App Search

The Virto Commerce **Elastic App Search** module enables integrating  [Azure Cognitive Search](https://azure.microsoft.com/en-us/services/search/) as a [search engine](https://doc.oroinc.com/backend/architecture/tech-stack/search-index/#search-index-overview).

Elastic App Search provides search, aggregation, and analytic capabilities as a service, on top of ElasticSearch. It also supplies tools that can help you tune search result sets without development:

* [Relevance tuning.](https://www.elastic.co/guide/en/app-search/current/precision-tuning.html)
* [Synonyms.](https://www.elastic.co/guide/en/app-search/current/synonyms-guide.html)
* [Curations.](https://www.elastic.co/guide/en/app-search/current/curations-guide.html)

![Readmore](media/readmore.png){: width="25"} [Deploying Elastic App Search](https://www.elastic.co/guide/en/app-search/current/installation.html)

[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-elastic-app-search/)

## Key features

The Elastic App Search module offers:

* Full-text search provider compatibility with Elastic App Search version 8.12 and higher.
* Boosting profile functionality.
* Dynamic boosting concatenation, combining dynamic boosting with query and static boosting from the Search Relevance Tuning panel.

## Configuration

Configure the Elastic App Search using the following schema:

{%
   include-markdown "../../../Configuration-Reference/appsettingsjson.md"
   start="<!--elasticappsearch-start-->"
   end="<!--elasticappsearch-end-->"
%}

## Performance

After running load tests and comparing Elasticsearch Vs Elastic App Search, we can confirm that both engines are ready for production and demonstrate the same results.

## Limitations

![Readmore](media/readmore.png){: width="25"} [App search limitations](https://www.elastic.co/guide/en/app-search/8.3/limits.html)



<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../elastic-search-8">← Elasticsearch 8</a>
    <a href="../configuring-elastic-app-search">Elastic App Search Configuration →</a>
</div>