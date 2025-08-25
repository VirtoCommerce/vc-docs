# moveFromSavedForLater ==~mutation~==

This mutation moves one or more items from the customer’s **Saved for Later** list back to the active shopping cart, based on the provided input command.

## Arguments

The `InputSaveForLaterType` represents the input object type used for moving a saved-for-later line item back to the cart.

| Field                     | Description                                                  |
| ------------------------- | ------------------------------------------------------------ |
| `cartId` ==String==       | The Id of the cart to move the item(s) into.                 |
| `storeId` ==String!==     | The Id of the store associated with the cart.                |
| `userId` ==String!==      | The Id of the customer who owns the cart.                    |
| `lineItemIds` ==[String]!== | The Ids of line items to move from the Saved for Later list. |
| `currencyCode` ==String== | The currency code for the cart.                              |
| `cultureName` ==String==  | The language to retrieve data in.        |

## Possible returns

| Possible return                                      | Description                                                               |
| ---------------------------------------------------- | ------------------------------------------------------------------------- |
| [`CartWithListType`](../objects/CartWithListType.md) | The updated cart details, including the Saved for Later list information. |

=== "Mutation"

    ```graphql linenums="1"
    mutation moveFromSavedForLater($command: InputSaveForLaterType!) {
    moveFromSavedForLater(command: $command) {
        id
        name
        items {
        id
        name
        productId
        quantity
        }
        savedForLater {
        id
        name
        productId
        quantity
        }
    }
    }
    ```

=== "Variables"

    ```json linenums="1"
    {
    "command": {
        "storeId": "B2B-store",
        "cartId": "4f36f405-70fe-4de7-ad72-5d1aed912f48",
        "userId": "2afc394a-c1e2-41ad-bd3a-c0e27705a12d",
        "lineItemIds": [
        "20e00498-c9b1-4a90-b804-4eaf21861ea2"
        ],
        "currencyCode": "USD",
        "cultureName": "en-US",
        "cartType": "ShoppingCart",
        "cartName": "Default"
    }
    }
    ```
