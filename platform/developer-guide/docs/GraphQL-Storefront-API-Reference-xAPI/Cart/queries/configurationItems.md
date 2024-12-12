# configurationItems ==~query~==

This query retrieves a list of configuration options for a specific cart or line item, enabling customization based on the provided parameters.  

## Arguments  

| Argument          | Description                                                                   |
|-------------------|-------------------------------------------------------------------------------|
| `cartId`       ==String==  | The Id of the cart to retrieve configurations for.                   |
| `lineItemId`   ==String!== | The Id of the specific line item in the cart.                        |
| `storeId`      ==String!== | The Id of the store for which configurations apply.                  |
| `currencyCode` ==String!== | A standardized code for the currency used in the configuration.      |
| `cartType`     ==String==  | The type of cart (e.g., "ShoppingCart" or "Wishlist").               |
| `cartName`     ==String==  | The name of the cart.                                                |
| `userId`       ==String==  | The current user Id.                                                 |
| `cultureName`  ==String==  | A language to retrieve data in.                                      |

## Possible return  

| Possible return                                                                   | Description                                         |
|-----------------------------------------------------------------------------------|-----------------------------------------------------|
| [ConfigurationItemsResponseType](../objects/ConfigurationItemsResponseType.md)    | The response type containing configuration options. |


## Examples  

=== "Query"

    ```json linenums="1"
    {
      configurationItems(
        lineItemId: "95770655-dd4b-49a0-b91c-1ee59eb5daec"
        storeId: "B2B-store"
        currencyCode: "USD"
        cultureName: "en-US"
        cartId: "4f36f405-70fe-4de7-ad72-5d1aed912f48"
    ) {
        configurationItems {
        id
        name
        quantity
        productId
        sectionId
        }
      }
    }
    ```

=== "Response"

    ```json linenums="1"
    {
        "data": {
            "configurationItems": {
                "configurationItems": [
                    {
                        "id": "33a351ef-1496-4503-9683-0f84f9f56e95",
                        "name": "Mattress cover Fitted sheet, light pink, 90x200 cm",
                        "quantity": 1,
                        "productId": "06f5c0ad-1990-4a28-a77c-6d3172c9f81e",
                        "sectionId": "ec90e98e-f43d-4730-bcd5-6ae5bea75144"
                    },
                    {
                        "id": "41a1f2b2-e590-4def-a028-296fa3d1a556",
                        "name": "Pillow 50X60",
                        "quantity": 2,
                        "productId": "7de77e67-efab-41c9-a879-6ee466d2e7a7",
                        "sectionId": "5b9f20f2-fd30-4b74-a47e-fbb3378ce947"
                    },
                    {
                        "id": "e4ae38b3-5bfc-4938-a7ea-1ee65210358a",
                        "name": "Blanket, medium warm, 150x200 cm",
                        "quantity": 1,
                        "productId": "f35b3373-7b40-4c0f-8d84-f1b28ff4358e",
                        "sectionId": "af6eff9b-30e4-431a-a01a-63d8af1ac04e"
                    }
                ]
            }
        }
    }
    ```