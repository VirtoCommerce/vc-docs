# getSavedForLater ==~query~==

This query retrieves a list of items that a customer has saved for later, based on the provided parameters.

## Arguments

| Argument                    | Description                                                         |
| --------------------------- | ------------------------------------------------------------------- |
| `storeId`      ==String!==  | The Id of the store to retrieve saved-for-later items from.         |
| `userId`       ==String!==  | The Id of the customer whose saved-for-later items are requested.   |
| `organizationId` ==String== | The Id of the organization associated with the customer. |
| `currencyCode` ==String==   | A standardized code for the currency.                               |
| `cultureName`  ==String==   | The language to retrieve data in.                           |

## Possible return

| Possible return                     | Description                                                |
| ----------------------------------- | ---------------------------------------------------------- |
| [CartType](../objects/cart-type.md) | The response type containing saved-for-later cart details. |


## Example

<div class="grid" markdown>

```json title="Query"
{
  getSavedForLater(
    storeId: "B2B-store"
    userId: "customer-123"
    organizationId: "org-456"
    currencyCode: "USD"
    cultureName: "en-US"
) {
    id
    name
    items {
    id
    productId
    name
    quantity
    }
  }
}
```

```json title="Return"
{
"data": {
    "getSavedForLater": {
    "id": "saved-later-cart-1",
    "name": "Saved For Later",
    "items": [
        {
        "id": "item-1",
        "productId": "prod-001",
        "name": "Office Chair",
        "quantity": 1
        },
        {
        "id": "item-2",
        "productId": "prod-002",
        "name": "Desk Lamp",
        "quantity": 2
        }
    ]
    }
}
}
```

</div>