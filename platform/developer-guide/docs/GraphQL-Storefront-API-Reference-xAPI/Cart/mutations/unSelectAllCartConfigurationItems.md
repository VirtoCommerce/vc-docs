# unSelectAllCartConfigurationItems ==~mutation~==

This mutation allows you to unselect all configuration items within a single configured line item in a shopping cart. Use it to exclude every configuration section of a line item from checkout in one call.

## Arguments

The `InputChangeAllCartConfigurationItemsSelectedType` represents a set of input parameters for unselecting all configuration items in a line item.

| Field                            | Description                                                              |
|----------------------------------|--------------------------------------------------------------------------|
| `cartId`  ==String==             | The Id of the cart.                                                      |
| `storeId`  ==String!==           | The Id of the store.                                                     |
| `cartName`  ==String==           | The name or description of the cart.                                     |
| `userId`  ==String!==            | The Id of the user.                                                      |
| `currencyCode`  ==String==       | The currency code for the cart.                                          |
| `cultureName`  ==String==        | The culture or locale name for the cart.                                 |
| `cartType`  ==String==           | The type of the cart.                                                    |
| `lineItemId`  ==String!==        | The Id of the configured line item whose configuration items will be unselected. |

## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|


## Example

<div class="grid" markdown>

```json title="Mutation"
mutation unSelectAllCartConfigurationItems($command: InputChangeAllCartConfigurationItemsSelectedType!) {
  unSelectAllCartConfigurationItems(command: $command) {
    id
    items {
      id
      name
      selectedForCheckout
      configurationItems {
        id
        sectionId
        type
        selectedForCheckout
      }
    }
  }
}
```

```json title="Variables"
"command":{
  "storeId": "B2B-store",
  "userId": "23a7f0e9-0186-4293-b511-bf894583fd3b",
  "cartId": "3095ebfe-1de6-4a75-9774-2c4dfdb3d002",
  "currencyCode": "USD",
  "cultureName": "en-US",
  "cartName": "default",
  "lineItemId": "127fffb3-9840-454e-a879-c0e621d7f128"
}
```

</div>
