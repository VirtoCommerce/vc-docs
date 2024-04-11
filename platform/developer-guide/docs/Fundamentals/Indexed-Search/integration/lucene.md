# Lucene

The Virto Commerce **Lucene Search** module implements `ISearchProvider` defined in the VirtoCommerce Search module and uses Lucene search engine which stores indexed documents in a local file system.

[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-lucene-search)

## Configuration

Configure the Lucene search provider using the following schema:

| Node                                       | Default or Sample Value                    | Description                                                                    |
| -------------------------------------------| -------------------------------------------| -------------------------------------------------------------------------------|
| Search.Provider                            | `"Lucene"`                                 | Name of the search provider, which must be set to `Lucene`.                    |
| Search.Lucene.Path                         |                                            | A virtual or physical path to the root directory where indexed documents are stored.
| Search.Scope                               | `"default"`                                | (Optional) Specifies the common name (prefix) for all indexes. Each document type is stored in a separate index, and the full index name is `scope-{documenttype}`. This allows one search service to serve multiple indexes. |

**Example**

```json title="appsettings.json"
"Search": {
    "Provider": "Lucene",
    "Scope": "default",
    "Lucene": {
        "Path": "/path/to/lucene/indexes"
    }
}
```
