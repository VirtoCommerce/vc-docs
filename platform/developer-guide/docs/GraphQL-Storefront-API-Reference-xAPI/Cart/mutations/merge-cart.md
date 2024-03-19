# mergeCart ==~mutation~==

This mutation merges two carts. You can use it to merge an anonymous cart with a user cart after user authentication.

## Arguments

The `InputMergeCartType` represents the input object type used for merging two carts into one. 

| Field                              | Description                                                              |
|----------------------------------- |--------------------------------------------------------------------------|
| `cartId`  ==String==               | The Id of the primary cart that will receive the merged data.            |
| `storeId`  ==String!==             | The Id of the store associated with the carts.                           |
| `cartName`  ==String==             | The name of the primary cart.                                            |
| `userId`  ==String==               | The Id of the user who owns the primary cart.                            |
| `currencyCode`  ==String==         | The currency code for the primary cart.                                  |
| `cultureName`  ==String==          | The culture or language associated with the primary cart.                |
| `cartType`  ==String==             | The type of the primary cart.                                            |
| `secondCartId`  ==String==         | The Id of the secondary cart that will be merged into the primary cart.  |

## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|


=== "Mutation"
    ```json linenums="1"
    mutation mergeCart($command: InputMergeCartType!) {
      mergeCart(command: $command) {
        id
        items {
          id
          name
          quantity
        }
        total {
          amount
        }
      }
    }
    ```

=== "Variables"
    ```json linenums="1"
    "command": {
        "storeId": "B2B-Store",
        "cartName": "default",
        "userId": "c50e5237-8a4c-41fe-b878-8e5a72390a08",
        "cultureName": "en-US",
        "currencyCode": "USD",
        "cartType": "cart",
        "secondCartId": "7777-7777-7777-7777",
    }
    ```