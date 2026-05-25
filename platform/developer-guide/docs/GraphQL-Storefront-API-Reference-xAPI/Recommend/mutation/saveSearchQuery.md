# saveSearchQuery ==~mutation~==

This mutation stores a user’s search query for future use, such as populating recent search history or improving personalization in search recommendations.

## Fields

The `InputSaveSearchQueryType!` is a type that represents the input object for saving a search query.

| Field                  | Description                                                  |
| ---------------------- | ------------------------------------------------------------ |
| `storeId` ==String!==  | The ID of the store where the search query was made.         |
| `query` ==String!==    | The search string entered by the user that should be stored. |

## Possible returns

| Possible return | Description                                                          |
| --------------- | -------------------------------------------------------------------- |
| `Boolean`       | A boolean value indicating whether the query was saved successfully. |


## Example

<div class="grid" markdown>

```json title="Mutation"
mutation {
  saveSearchQuery(command: {
    storeId: "b2b-store"
    query: "printers"
  })
}
```

```json title="Expected response"
{
  "data": {
    "saveSearchQuery": true
  }
}
```

</div>