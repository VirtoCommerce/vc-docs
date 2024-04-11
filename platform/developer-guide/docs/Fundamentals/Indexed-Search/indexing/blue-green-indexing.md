# Blue-Green Indexing

!!! note
    The blue-green indexing is only supported by the ElasticSearch module.<br>
    ![Readmore](media/readmore.png){: width="25"} [Elastic Search module](../../../../../user-guide/elastic-search/overview)

After you choose **Delete and build** when building search index:

1. A new backup index is generated for the chosen document type.
1. The indexing operations are carried out on this backup index.
1. Throughout the full indexing process, the existing index remains unaffected, allowing uninterrupted search operations.
1. Once the reindexing is complete, a swap occurs: the backup index becomes active, while the previous index transitions to a backup role.

To revert to the previous index, use the **Swap indices** feature:

1. Click **Show backup indices** in the top toolbar.

    ![Backup indices](media/show-backup-indices.png)

1. Click on the three dots to the left of the required document type.
1. Select **Swap indices** in the popup menu.
1. Click **Hide backup indices** in the top toolbar.

    ![Three dots](media/three-dots.png)

The roles of the backup and active indices have been exchanged.

### Implementation Details

Elasticsearch implements blue-green indexing using Elasticsearch [aliases](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-aliases.html). Search provider implementations use two aliases to distinguish one index role from the other: **active** and **backup**. The full index alias is built as **scope name + document type name + alias name**; for example, an active index alias for the **Members** index using the `default` scope will be `default-member-active`.

Each time you start the **Delete and build** process, the Elasticsearch index provider looks for an existing backup index by the backup alias, for example, `default-member-backup`, and deletes it if it is found. After that, when the reidnexing process starts, a new backup index is created with the `backup' alias. However, an actual index name is created dynamically: this is a special alphanumeric token suffix added to the end of the index name. The only way to tell which index is active is to look at its alias. After the indexing process is complete, the active and backup indices swap aliases, i.e. the active index becomes the backup index, and vice versa.

![Kibana index alias](media/implementation.png)