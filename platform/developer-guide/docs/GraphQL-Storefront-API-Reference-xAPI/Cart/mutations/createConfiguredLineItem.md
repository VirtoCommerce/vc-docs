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


## Example

<div class="grid" markdown>

```json title="Mutation"
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

```json title="Variables"
{
  "command": {
    "storeId": "B2B-store",
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
      ...
      }
    ]
  }
}
```

</div>