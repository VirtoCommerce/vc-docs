# updateCartDynamicProperties ==~mutation~==

This mutation updates dynamic properties within the cart.

## Arguments

The `InputUpdateCartDynamicPropertiesType` represents the input object type used for updating dynamic properties of a cart.

| Field                                 | Description                                                       |
|---------------------------------------|-------------------------------------------------------------------|
| `cartId`  ==String==                  | The Id of the cart to update the dynamic properties.              |
| `storeId`  ==String!==                | The Id of the store associated with the cart.                     |
| `cartName`  ==String==                | The name of the cart.                                             |
| `userId`  ==String==                  | The Id of the user who owns the cart.                             |
| `currencyCode`  ==String==            | The currency code for the cart.                                   |
| `cultureName`  ==String==             | The culture or language associated with the cart.                 |
| `cartType`  ==String==                | The type of the cart.                                             |
| `dynamicProperties`  ==[InputDynamicPropertyValueType]!==  | The updated dynamic properties of the cart.  |

## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|


=== "Mutation"
    ```json linenums="1"
    mutation updateCartDynamicProperties(
      $command: InputUpdateCartDynamicPropertiesType!
    ) {
      updateCartDynamicProperties(command: $command) {
        id
        dynamicProperties {
          name
          value
          valueType
          dictionaryItem {
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
      "cartId": "e6a7d5af-6378-44a6-b645-af9ecf702c05",
      "storeId": "B2B-Store",
      "userId": "c50e5237-8a4c-41fe-b878-8e5a72390a08",
      "currencyCode": "USD",
      "cultureName": "en-US",
      "cartName": "default",
      "dynamicProperties": [
        {
          "name":"Purchase order number",
          "value":"new value_1_2"
        },
        {
        "name":"Decimal",
        "value":"33.88"
        }
      ]
    }
    ```