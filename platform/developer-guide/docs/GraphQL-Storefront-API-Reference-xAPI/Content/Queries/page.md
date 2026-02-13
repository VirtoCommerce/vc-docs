# Page ==~query~==

This query retrieves information about a specific page based on the provided criteria.

## Arguments

| Argument                | Description                                                           |
|-------------------------|-----------------------------------------------------------------------|
| `storeId` ==String!==   | The ID of the store from which to retrieve the page.                  |
| `cultureName` ==String==| The language in which to retrieve the page content.                   |
| `id` ==String!==        | The unique identifier of the page to retrieve.                        |

## Possible returns

| Possible return                                          	| Description                             	|
|---------------------------------------------------------	|------------------------------------------	|
| [`PageType`](../Objects/PageType.md)        	            |  Details of the requested page.          	|


## Example

<div class="grid" markdown>

```json title="Query"
{
  page(storeId: "B2B-store", cultureName: "en-US", id: "12345") {
    id
    name
    relativeUrl
    permalink
    content
  }
}
```

```json title="Return"
{
  "data": {
    "page": {
      "id": "12345",
      "name": "Example Page",
      "relativeUrl": "/example-page",
      "permalink": "/example-page",
      "content": "<p>This is an example page.</p>"
    }
  }
}
```

</div>