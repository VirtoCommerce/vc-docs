# ChangeCartItemComment ==~mutation~==

This mutation changes cart item comments.

## Arguments

The `InputChangeCartItemCommentType` represents the input object type used for changing the comment of a specific item in a cart. 

| Field            | Description                                                               |
|------------------|---------------------------------------------------------------------------|
| `cartId` {==String==}           | The ID of the cart to which the item belongs.                                |
| `storeId` {==String!==}        | The ID of the store associated with the cart.                                |
| `cartName` {==String==}         | The name of the cart.                                                       |
| `userId` {==String==}           | The ID of the user who owns the cart.                                        |
| `currencyCode` {==String==}     | The currency code associated with the cart.                                  |
| `cultureName` {==String==}      | The culture or language name associated with the cart.                       |
| `cartType` {==String==}         | The type of the cart.                                                        |
| `lineItemId` {==String!==}     | The ID of the line item for which the comment is being changed.              |
| `comment` {==String!==}        | The new comment to be assigned to the line item.                             |

## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|


=== "Mutation"
    ```json linenums="1"
    mutation ($command:InputChangeCartItemCommentType!)
    {
        (command: $command)
        {
            id
            items
            {
                sku
                productId
                comment
            }
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
        "comment": "nice product"
    }
    ```