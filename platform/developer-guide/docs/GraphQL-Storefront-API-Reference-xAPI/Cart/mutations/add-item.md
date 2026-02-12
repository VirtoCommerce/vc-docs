# addItem ==~mutation~==

This mutation:

* Validates an item.
* Adds it to the cart. 
* Recalculates promotion rewards and taxes and applies it to the cart.

## Arguments

The `InputAddItemType` represents the arguments for the ClearCart operation. 

| Field                          | Description                                                                                  |
|--------------------------------|----------------------------------------------------------------------------------------------|
| `cartId` ==String==            | The Id of the cart.                                                                          |
| `storeId` ==String!==          | The Id of the store.                                                                         |
| `cartName` ==String==          | The name or description of the cart.                                                         |
| `userId` ==String!==           | The Id of the user.                                                                          |
| `currencyCode` ==String==      | The currency code for the cart.                                                              |
| `cultureName` ==String==       | A language to retrieve data in.                                                              |
| `cartType` ==String==          | The type of the cart.                                                                        |
| `productId` ==String!==        | The Id of the product to add to the cart.                                                    |
| `quantity` ==Int!==            | The quantity of the product to add to the cart.                                              |
| `price` ==Decimal==            | The price of the product.                                                                    |
| `comment` ==String==           | A comment associated with the added item.                                                    |
| `dynamicProperties` [==[InputDynamicPropertyValueType]==](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Profile/Objects/InputDynamicPropertyValueType) | The dynamic properties associated with the added item.  |

## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|



## Example

<div class="grid" markdown>

```json title="Mutation"
    mutation addItem($command: InputAddItemType!) {
      addItem(command: $command) {
        id
        items {
          id
          quantity
          listPrice {
            amount
          }
          note
        }
        total {
          amount
        }
        discountTotal {
          amount
        }
      }
    }
```

```json title="Variables"
  "command": {
    "cartId": "e6a7d5af-6378-44a6-b645-af9ecf702c05",
    "storeId": "B2B-store",
    "cartName": "default",
    "userId": "c50e5237-8a4c-41fe-b878-8e5a72390a08",
    "cartType": "null",
    "productId": "ec235043d51848249e90ef170c371a1c",
    "quantity": 1,
    "currencyCode": "USD",
    "cultureName":"en-US",
    "price": 10.85,
    "comment": ""
  }
```

</div>