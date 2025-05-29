# updateQuoteDynamicProperties ==~mutation~==

This mutation updates the dynamic properties of a quote.

## Arguments

The `UpdateQuoteDynamicPropertiesCommandType!` represents the input required to update dynamic properties on a quote.

| Field                                                                                                           | Description                                                 |
|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| `command` [==UpdateQuoteDynamicPropertiesCommandType!==](../objects/UpdateQuoteDynamicPropertiesCommandType.md) | Contains the quote ID and the dynamic properties to update. |

## Possible returns

| Possible return                        | Description                                    |
| -------------------------------------- | ---------------------------------------------- |
| [`QuoteType`](../objects/QuoteType.md) | Updated quote information with new properties. |

=== "Mutation"
    ```json linenums="1"
    mutation {
      updateQuoteDynamicProperties(
        command: {
          quoteId: "6c03681f-clef-4210-afb0-cd849957aacc",
          dynamicProperties: [
            {
              name: "TestDyn2",
              value: "TestDyn2",
              locale: "English",
              cultureName: "en-US"
            }
          ]
        }
      )
    }

    ```

=== "Return"
    ```json linenums="1"
    {
      data"：{
        "updateQuoteDynamicProperties": {
          "id": "6c03681f-clef-4210-afb-cd849957aacc",
          "dynamicProperties": [
            {
              "name": "TestDyn2",
              "value": "TestDyn2"
            },
            {
              "name": "TestDyn1",
              "value": "TestDyn1"
            }
          ]
        }
      }
    }
    ```
