# Configuration
This section explains the basic configuration for the indexed search logic via the [appsettings.json file](../../Configuration-Reference/appsettingsjson.md#search).

| Node                        | Default or sample value   | Description                                                                                                                                   |
| ----------------------------| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Provider                    | `"Lucene"`                | This **required** setting specifies the current search provider. The supported values are  `Lucene`, `AzureSearch`, and `ElasticSearch`.      |
| Scope                       | `"default"`               | This setting determines the scope to use and is **required**.                                                                                 |
| Lucene                      |                           | Lucene provider configuration for the **VirtoCommerce.LuceneSearch** module.<br>Used when the `Provider` setting has the `Lucene` value.            |
| AzureSearch                 |                           | AzureSearch provider configuration for the **VirtoCommerce.AzureSearch** module.<br>Used when the `Provider` setting has the `AzureSearch` value.  |
| ElasticSearch               |                           | Elasticsearch  provider configuration for the **VirtoCommerce.ElasticSearch** module.<br>Used when the `Provider` setting has the `ElasticSearch` value.|
|OrderFullTextSearchEnabled   | `true`<br> `false`        | This boolean setting enables full-text search for orders.<br>If true (by default), full-text search for orders is enabled,<br>and it allows searching for orders based on their content. |
|ContentFullTextSearchEnabled | `true` <br> `false`       | This boolean setting enables full-text search for content.<br>If true (by default), full-text search for content is enabled,<br>and it allows searching for content items based on their textual content.|

**Examples**

=== "Lucene"

    ```json title="appsettings.json"
    "Lucene": {
    "Path": "App_Data/Lucene"
    } 
    ```

=== "AzureSearch"

    ```json title="appsettings.json"
    "AzureSearch": {
    "SearchServiceName": "my-ServiceName",
    "Key": "my-AccessKey"
    } 
    ```

=== "ElasticSearch"

    ```json title="appsettings.json"
    "ElasticSearch": {
    "Server": "localhost:9200",
    "User": "elastic",
    "Key": "",
    "EnableHttpCompression": ""
    <!-- For ES 8.0 and higher must be set to True -->
    "EnableCompatibilityMode": true 
    } 
    ```