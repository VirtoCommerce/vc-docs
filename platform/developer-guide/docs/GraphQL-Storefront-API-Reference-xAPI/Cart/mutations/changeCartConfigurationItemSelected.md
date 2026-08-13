# changeCartConfigurationItemSelected ==~mutation~==

This mutation allows you to toggle the `selectedForCheckout` flag on a single configuration item within a configured line item, without requiring `productId` or `quantity` and without triggering a catalog reload.

## Arguments

The `InputChangeCartConfigurationItemSelectedType` represents a set of input parameters for changing the selection state of a single configuration item.

| Field                                  | Description                                                          |
|----------------------------------------|----------------------------------------------------------------------|
| `cartId`  ==String==                   | The Id of the cart.                                                  |
| `storeId`  ==String!==                 | The Id of the store.                                                 |
| `cartName`  ==String==                 | The name or description of the cart.                                 |
| `userId`  ==String!==                  | The Id of the user.                                                  |
| `currencyCode`  ==String==             | The currency code for the cart.                                      |
| `cultureName`  ==String==              | The culture or locale name for the cart.                             |
| `cartType`  ==String==                 | The type of the cart.                                                |
| `lineItemId`  ==String!==              | The Id of the configured line item that contains the configuration item. |
| `configurationSection`  ==[[ConfigurationSectionKeyInput!]](../objects/ConfigurationSectionKeyInput.md)== | The configuration section to toggle. Identified by `sectionId`, `type`, and an optional `option`. |
| `selectedForCheckout`  ==Boolean!==    | The new selection state. `true` to select, `false` to unselect.      |

## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|


## Example

<div class="grid" markdown>

```graphql title="Mutation"
mutation changeCartConfigurationItemSelected($command: InputChangeCartConfigurationItemSelectedType!) {
  changeCartConfigurationItemSelected(command: $command) {
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
  "lineItemId": "127fffb3-9840-454e-a879-c0e621d7f128",
  "configurationSection": {
    "sectionId": "section-1",
    "type": "Product",
    "option": {
      "productId": "5f9b3d7b-0f5d-4e7f-9f8e-9b4f7e5c3d2a",
      "quantity": 1
    }
  },
  "selectedForCheckout": true
}
```

</div>

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../createConfiguredLineItem">← CreateConfiguredLineItem mutation</a>
    <a href="../selectCartConfigurationItems">SelectCartConfigurationItems mutation →</a>
</div>
