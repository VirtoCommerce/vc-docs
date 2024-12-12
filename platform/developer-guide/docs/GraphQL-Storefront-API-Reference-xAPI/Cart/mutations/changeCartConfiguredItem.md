# changeCartConfiguredItem ==~mutation~==

This mutation updates the configuration or quantity of an existing line item in the cart based on the provided input command.

## Arguments

The `InputChangeCartConfiguredItemType` represents the input object type used for modifying a configured line item in the cart.

| Field                                 | Description                                                                     |
|---------------------------------------|---------------------------------------------------------------------------------|
| `cartId` ==String==                   | The Id of the cart containing the line item.                                    |
| `storeId` ==String!==                 | The Id of the store associated with the cart.                                   |
| `cartName` ==String==                 | The name of the cart.                                                           |
| `userId` ==String!==                  | The Id of the user who owns the cart.                                           |
| `currencyCode` ==String==             | The currency code for the cart.                                                 |
| `cultureName` ==String==              | The culture or language associated with the cart.                               |
| `cartType` ==String==                 | The type of the cart.                                                           |
| `lineItemId` ==String!==              | The Id of the line item to be modified.                                         |
| `quantity` ==Int==                    | The new quantity for the line item.                                             |
| `configurationSections` [==[ConfigurationSectionInput]==](../objects/ConfigurationSectionInput.md) | A list of configuration sections and their associated details.|

## Possible returns

| Possible return                                       | Description                                                               |
|------------------------------------------------------|---------------------------------------------------------------------------|
| [`CartType`](../objects/cart-type.md)                | The updated details and properties of the cart.                          |

=== "Mutation"
    ```graphql linenums="1"
    mutation changeCartConfiguredItem($command: InputChangeCartConfiguredItemType!) {
      changeCartConfiguredItem(command: $command) {
        items {
          configurationItems {
            id
            name
            sectionId
            productId
            quantity
          }
        }
      }
    }
    ```

=== "Variables"
    ```json linenums="1"
    {
      "command": {
        "storeId": "B2B-store",
        "cultureName": "en-US",
        "currencyCode": "USD",
        "userId": "2afc394a-c1e2-41ad-bd3a-c0e27705a12d",
        "lineItemId": "20e00498-c9b1-4a90-b804-4eaf21861ea2",
        "configurationSections": [
          {
            "sectionId": "4db83a8f-9e2b-40c2-8a33-e44147a247ad",
            "value": {
              "productId": "8a106054-6802-472d-991a-d95e1e61e093",
              "quantity": 1
            }
          },
          {
            "sectionId": "5b21606a-a695-4f4e-a370-89f7f64b7759",
            "value": {
              "productId": "cabde383-4411-48bf-a577-e30a0c4fd443",
              "quantity": 2
            }
          }
        ],
        "quantity": 1
      }
    }
    ```
