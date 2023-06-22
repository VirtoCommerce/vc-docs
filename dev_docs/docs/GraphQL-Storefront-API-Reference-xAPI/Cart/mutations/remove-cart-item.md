# RemoveCartItem ==~mutation~==

This mutation enables removing an item from the cart.

## Arguments

The `InputRemoveItemType` represents the input object type used for removing a specific item from a cart.

| Field                          | Description                                                        |
|-----------------------------------|--------------------------------------------------------------------|
| `cartId` {==String==}             | The ID of the cart from which the item is to be removed.               |
| `storeId` {==String!==}           | The ID of the store associated with the cart.                         |
| `cartName` {==String==}         | The name of the cart.                                                |
| `userId` {==String==}           | The ID of the user who owns the cart.                                 |
| `currencyCode` {==String==}     | The currency code for the cart.                                      |
| `cultureName` {==String==}      | The culture or language associated with the cart.                     |
| `cartType` {==String==}         | The type of the cart.                                                |
| `lineItemId` {==String==}       | The ID of the line item to be removed from the cart.                  |

## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|


=== "Mutation"
    ```json linenums="1"
    mutation ($command:InputRemoveItemType!)
    {
        (command: $command)
        {
            id
            items
            {
                sku
                productId
            }
            itemsCount
            itemsQuantity
        }
    }
    ```

=== "Variables"
    ```json linenums="1"
    "command": {
        "storeId": "Electronics",
        "cartName": "default",
        "userId": "b57d06db-1638-4d37-9734-fd01a9bc59aa",
        "cultureName": "en-US",
        "currencyCode": "USD",
        "cartType": "cart",
        "lineItemId": "9cbd8f316e254a679ba34a900fccb076",
    }
    ```