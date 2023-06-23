# ChangeCartItemQuantity ==~mutation~==

This mutation changes the cart item quantity.

## Arguments

The `InputChangeCartItemQuantityType` represents the input object type used for changing the quantity of a specific item in a cart. 

| Field                | Description                                                                                      |
|--------------------------|--------------------------------------------------------------------------------------------------|
| `cartId` {==String==}    | The identifier of the cart to which the item belongs.                                             |
| `storeId` {==String!==}  | The identifier of the store to which the cart belongs.                                           |
| `cartName` {==String==}  | The name or description of the cart.                                                             |
| `userId` {==String==}    | The identifier of the user associated with the cart.                                             |
| `currencyCode` {==String==} | The currency code for the cart.                                                             |
| `cultureName` {==String==} | The culture or locale name for the cart.                                                    |
| `cartType` {==String==} | The type or category of the cart.                                                              |
| `lineItemId` {==String==} | The identifier of the specific item within the cart for which the quantity is being changed.    |
| `quantity` {==Int!==}   | The new quantity value to be set for the item.                                                  |

## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|


=== "Mutation"
    ```json linenums="1"
    mutation ($command:InputChangeCartItemQuantityType!)
    {
        (command: $command)
        {
            id
            items
            {
                sku
                productId
                quantity
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
        "quantity": 7
    }
    ```