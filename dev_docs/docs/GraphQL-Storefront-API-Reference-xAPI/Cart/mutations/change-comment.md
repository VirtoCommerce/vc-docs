# ChangeComment ==~mutation~==

This mutation changes the cart comments.

## Arguments

The `InputChangeCommentType` represents the input object type used for changing the comment or note associated with a cart.  


| Field                   | Description                                                            |
|----------------------------|---------------------------------------------------------------------------|
| `cartId` {==String==}      | The identifier of the cart.                                               |
| `storeId` {==String!==}    | The identifier of the store.                                              |
| `cartName` {==String==}    | The name of the cart.                                                     |
| `userId` {==String!==}     | The identifier of the user.                                               |
| `currencyCode` {==String==}| The currency code for the cart.                                           |
| `cultureName` {==String==} | The culture or locale name for the cart.                                  |
| `cartType` {==String==}    | The type or category of the cart.                                         |
| `comment` {==String==}     | The new comment or note to be associated with the cart.                   |

## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|


=== "Mutation"
    ```json linenums="1"
    mutation ($command:InputChangeCommentType!)
    {
        (command: $command)
        {
            name
            comment
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
        "comment": "Hi, Virto! :)"
    }
    ```