# changeCartItemPrice ==~mutation~==

This mutation changes the cart item price.

## Arguments

The `InputChangeCartItemPriceType` represents the input object type used for changing the price of a specific item within a cart. 

| Field                  | Description                                                                        |
|---------------------------|---------------------------------------------------------------------------------|
| `cartId` {==String==}     | The Id of the cart to which the item belongs.                                   |
| `storeId` {==String!==}   | The Id of the store to which the cart belongs.                                  |
| `cartName` {==String==}   | The name of the cart.                                                           |
| `userId` {==String==}     | The Id of the user associated with the cart.                                    |
| `currencyCode` {==String==}| The currency code for the cart.                                                |
| `cultureName` {==String==}| The culture or locale name for the cart.                                        |
| `cartType` {==String==}   | The type or category of the cart.                                               |
| `lineItemId` {==String==} | The Id of the specific item within the cart for which the price is being changed.|
| `price` {==Decimal!==}    | The new price value to be set for the item.                                     |

## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|


=== "Mutation"
    ```json linenums="1"
    mutation($command: InputChangeCartItemPriceType!) {
      changeCartItemPrice(command: $command) {
        id
        items {
          sku
          productId
          listPrice
          listPriceWithTax
          salePrice
          salePriceWithTax
        }
      }
    }
    ```

=== "Variables"
    ```json linenums="1"
    "command": {
        "cartId": "e6a7d5af-6378-44a6-b645-af9ecf702c05"
        "storeId": "B2B-store",
        "cartName": "default",
        "userId": "c50e5237-8a4c-41fe-b878-8e5a72390a08",
        "cultureName": "en-US",
        "currencyCode": "USD",
        "cartType": "cart",
        "lineItemId": "127fffb3-9840-454e-a879-c0e621d7f128"
        "price": 777
    }
    ```