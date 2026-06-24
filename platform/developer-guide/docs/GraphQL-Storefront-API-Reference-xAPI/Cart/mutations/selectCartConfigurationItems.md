# selectCartConfigurationItems ==~mutation~==

This mutation allows you to select a batch of configuration items within a single configured line item in a shopping cart. Use it to mark several configuration sections as included for checkout in one call.

## Arguments

The `InputChangeCartConfigurationItemsSelectedType` represents a set of input parameters for selecting configuration items.

| Field                                                       | Description                                                              |
|-------------------------------------------------------------|--------------------------------------------------------------------------|
| `cartId`  ==String==                                        | The Id of the cart.                                                      |
| `storeId`  ==String!==                                      | The Id of the store.                                                     |
| `cartName`  ==String==                                      | The name or description of the cart.                                     |
| `userId`  ==String!==                                       | The Id of the user.                                                      |
| `currencyCode`  ==String==                                  | The currency code for the cart.                                          |
| `cultureName`  ==String==                                   | The culture or locale name for the cart.                                 |
| `cartType`  ==String==                                      | The type of the cart.                                                    |
| `lineItemId`  ==String!==                                   | The Id of the configured line item that contains the configuration items. |
| `configurationSections`  ==[[ConfigurationSectionKeyInput!]](../objects/ConfigurationSectionKeyInput.md)== | The list of configuration sections to select. Each is identified by `sectionId`, `type`, and an optional `option`. |

## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|


## Example

<div class="grid" markdown>

```json title="Mutation"
mutation selectCartConfigurationItems($command: InputChangeCartConfigurationItemsSelectedType!) {
  selectCartConfigurationItems(command: $command) {
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
  "configurationSections": [
    {
      "sectionId": "section-1",
      "type": "Product",
      "option": {
        "productId": "5f9b3d7b-0f5d-4e7f-9f8e-9b4f7e5c3d2a",
        "quantity": 1
      }
    },
    {
      "sectionId": "section-2",
      "type": "Text"
    }
  ]
}
```

</div>

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../changeCartConfigurationItemSelected">← ChangeCartConfigurationItemSelected mutation</a>
    <a href="../unSelectCartConfigurationItems">UnSelectCartConfigurationItems mutation →</a>
</div>
