# productSuggestions ==~query~==

This query provides product name suggestions based on partial user input. It is typically used for autocomplete functionality in search fields.

## Arguments

| Argument              | Description                                               |
| --------------------- | --------------------------------------------------------- |
| `storeId` ==String!== | The Id of the store to retrieve product suggestions from. |
| `query` ==String==    | The text to search for product name suggestions.          |
| `size` ==Int==        | The maximum number of suggestions to return.              |

## Possible return

| Possible return                                                                            | Description                         |
|--------------------------------------------------------------------------------------------|-------------------------------------|
| [`ProductSuggestionsQueryResponseType`](../objects/ProductSuggestionsQueryResponseType.md) | A list of product name suggestions. |



=== "Query"

    ```json linenums="1"
    {
      productSuggestions(
        storeId: "B2B-store",
        size: 10,
        query: "xer"
      ) {
        suggestions
      }
    }
    ```

=== "Return"

    ```json linenums="1"
    {
      "data": {
        "productSuggestions": {
          "suggestions": [
            "Xerox WorkCentre 3215/NI Monochrome Laser Printer",
            "Xerox WorkCentre 6515/DN - multifunction printer",
            "Xerox WorkCentre 3225/DNI Monochrome Laser Printer",
            "Xerox WorkCentre 3335DNI Mono Laser Multifunction Printer/Copier/Scanner/Fax Machine"
          ]
        }
      }
    }
    ```
