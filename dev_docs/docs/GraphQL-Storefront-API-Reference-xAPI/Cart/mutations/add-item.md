# AddItem ==~mutation~==

This mutation:

* Validates an item.
* Adds it to the cart. 
* Recalculates promotion rewards and taxes and applies it to the cart.

## Arguments

The `InputAddItemType` represents the arguments for the ClearCart operation. 

| Field                         | Description                                                                                  |
|----------------------------------|----------------------------------------------------------------------------------------------|
| `cartId` {==String==}            | The identifier of the cart.                                                                  |
| `storeId` {==String!==}          | The identifier of the store.                                                                 |
| `cartName` {==String==}          | The name or description of the cart.                                                         |
| `userId` {==String!==}           | The identifier of the user.                                                                  |
| `currencyCode` {==String==}      | The currency code for the cart.                                                              |
| `cultureName` {==String==}       | The culture or locale name for the cart.                                                     |
| `cartType` {==String==}          | The type or category of the cart.                                                            |
| `productId` {==String!==}       | The identifier of the product to add to the cart.                                             |
| `quantity` {==Int!==}            | The quantity of the product to add to the cart.                                              |
| `price` {==Decimal==}            | The price of the product.                                                                    |
| `comment` {==String==}           | A comment or note associated with the added item.                                             |
| `dynamicProperties` {==[InputDynamicPropertyValueType]==} | The dynamic properties associated with the added item.               |

## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|


=== "Mutation"
    ```json linenums="1"
    mutation ($command:InputAddItemType!)
    {
        (command: $command)
        {
            name
            items
            {
                id
                sku
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
        "productId": "9cbd8f316e254a679ba34a900fccb076",
        "quantity": 1,
        "dynamicProperties": [
            {
                "name": "ItemProperty",
                "value": "test value"
            }
        ]
    }
    ```