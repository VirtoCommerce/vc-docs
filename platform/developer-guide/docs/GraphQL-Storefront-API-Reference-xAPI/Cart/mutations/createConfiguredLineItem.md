# createConfiguredLineItem ==~mutation~==

This mutation creates a new line item with a specific configuration based on the provided input command.

## Arguments

The `InputCreateConfiguredLineItemCommand` represents the input object type used for creating a configured line item.

| Field                             | Description                                                                                   |
|-----------------------------------|-----------------------------------------------------------------------------------------------|
| `storeId` ==String==              | The Id of the store associated with the configured line item.                                 |
| `currencyCode` ==String==         | The currency code for the line item.                                                          |
| `cultureName` ==String==          | The culture or language associated with the line item.                                        |
| `configurableProductId` ==String!== | The Id of the configurable product.                                                           |
| `configurationSections` [==[ConfigurationSectionInput]==](../objects/ConfigurationSectionInput.md) | A list of configuration sections and their associated details. |

## Possible returns

| Possible return                                                      | Description                                                 |
|----------------------------------------------------------------------|-------------------------------------------------------------|
| [`ConfigurationLineItemType`](../objects/ConfigurationLineItemType.md) | The details and properties of the configured line item.    |

=== "Mutation"
    ```graphql linenums="1"
    mutation createConfiguredLineItem($command: InputCreateConfiguredLineItemCommand!) {
      createConfiguredLineItem(command: $command) {
        currency {
          code
        }
        listPrice {
          amount
        }
        salePrice {
          amount
        }
        discountAmount {
          amount
        }
        extendedPrice {
          amount
        }
      }
    }
    ```

=== "Variables"
    ```json linenums="1"
    {
      "command": {
        "storeId": "Electronics",
        "currencyCode": "USD",
        "cultureName": "en-US",
        "configurableProductId": "d733871c-f763-44b2-99c9-5f55edf28c16",
        "configurationSections": [
          {
            "sectionId": "Beverages",
            "value": {
              "productId": "e7eee66223da43109502891b54bc33d3",
              "quantity": 2
            }
          },
          {
            "sectionId": "Baloons",
            "value": {
              "productId": "0f7a77cc1b9a46a29f6a159e5cd49ad1",
              "quantity": 2
            }
          },
          {
            "sectionId": "Chips and Snacks",
            "value": {
              "productId": "77bffc3b23ba4b48a56baa56bd5d769c",
              "quantity": 2
            }
          }
        ]
      }
    }
    ```
