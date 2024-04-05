# Manage Search Index

To open search index details:

1. Click **Search Index** in the main menu.
1. The next blade displays:
    * The managed record types:
        * **Members**: Users or entities that have access to the platform.
        * **Content files**: Any type of digital content stored within the platform.
        * **Product**: The goods or services offered for sale within the Virto Commerce platform.
        * **Category**: Similar characteristics used to organize and classify products within the platform.
        * **Customer order**: Transactions where customers purchase products or services from the platform.

    * The search provider for each record type:
        * Elastic App Search.
        * Elasticsearch 8.
        * Lucene.
        * Elasticsearch.
        * Azure Cognitive Search.
        * Algolia.

    * Last indexed date, record count, and scope if specified by the user:

    ![Search index](media/open-search-index-module.png)

## Build Search Index

To build search index:

1. Check the required record types from the list.
1. Click **Build index** in the top toolbar.
1. In the popup window, choose how you want to update the search index. There are two options available:
    * **Build**: Index all data without recreating.
    * **Delete and build**: Delete the existing search index and build a new one from scratch. 
    
    !!! Note
        No search results will be available until the build process is over.

The next blade displays the result of indexation:

![Indexation result](media/indexation-result.png)

