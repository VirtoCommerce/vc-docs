# UpdateCartDynamicProperties ==~mutation~==

This mutation updates dynamic properties within the cart.

## Arguments

The `InputUpdateCartDynamicPropertiesType` represents the input object type used for updating dynamic properties of a cart.

| Field                      | Description                                                       |
|----------------------------|-------------------------------------------------------------------|
| `cartId` {==String==}                  | The ID of the cart to update the dynamic properties.                       |
| `storeId` {==String!==}               | The ID of the store associated with the cart.                                |
| `cartName` {==String==}                | The name of the cart.                                                       |
| `userId` {==String==}                  | The ID of the user who owns the cart.                                        |
| `currencyCode` {==String==}            | The currency code for the cart.                                             |
| `cultureName` {==String==}             | The culture or language associated with the cart.                            |
| `cartType` {==String==}                | The type of the cart.                                                       |
| `dynamicProperties` {==[InputDynamicPropertyValueType]!==} | The updated dynamic properties of the cart.                          |

## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|


=== "Mutation"
    ```json linenums="1"
    mutation ($command: InputUpdateCartDynamicPropertiesType!)
    {
        updateCartDynamicProperties(command: $command)
        {
            dynamicProperties
            {
                name
                value
                valueType
                dictionaryItem
                {
                    label
                    name
                    id
                }
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
        "dynamicProperties": [
            {
                "name": "Example string property",
                "value": "12345678"
            },
            {
                "name": "Example multilanguage property",
                "locale":"de-DE",
                "value": "hallo welt"
            },
            {
                "name": "Example dictionary property",
                "value": "578fadeb1d2a40b3b08b1daf8db09463"
            }
        ]
    }
    }
    ```