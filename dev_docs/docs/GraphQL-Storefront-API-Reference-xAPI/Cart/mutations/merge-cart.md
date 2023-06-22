# MergeCart ==~mutation~==

This mutation merges two carts. You can use it to merge an anonymous cart with a user cart after user authentication.

## Arguments

The `InputMergeCartType` represents the input object type used for merging two carts into one. 

| Field                  | Description                                                         |
|------------------------|---------------------------------------------------------------------|
| `cartId` {==String==}              | The ID of the primary cart that will receive the merged data.            |
| `storeId` {==String!==}           | The ID of the store associated with the carts.                           |
| `cartName` {==String==}            | The name of the primary cart.                                           |
| `userId` {==String==}              | The ID of the user who owns the primary cart.                            |
| `currencyCode` {==String==}        | The currency code for the primary cart.                                 |
| `cultureName` {==String==}         | The culture or language associated with the primary cart.                |
| `cartType` {==String==}            | The type of the primary cart.                                           |
| `secondCartId` {==String==}        | The ID of the secondary cart that will be merged into the primary cart.  |

## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|


=== "Mutation"
    ```json linenums="1"
    mutation ($command:InputMergeCartType!)
    {
        (command: $command)
        {
            id
            isAnonymous
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
        "secondCartId": "7777-7777-7777-7777",
    }
    ```