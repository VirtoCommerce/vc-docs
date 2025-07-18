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

=== "Mutation"

    ```graphql linenums="1"
    mutation {
      saveSearchQuery(command: {
        storeId: "b2b-store"
        query: "printers"
      })
    }
    ```

=== "Return"

    ```json linenums="1"
    {
      "data": {
        "saveSearchQuery": true
      }
    }
    ```
