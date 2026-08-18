# LineItemType ==~object~==

This type represents the data structure that holds information about a line item, which is a specific product added to a cart or order. 

## Fields

| Field                              | Description                                                                                           |
|------------------------------------|-------------------------------------------------------------------------------------------------------|
| `product`  ==Product==             | The product associated with the line item.                                                            |
| `inStockQuantity`  ==Int==         | The quantity of the product currently in stock.                                                       |
| `warehouseLocation`  ==String==    | The location of the warehouse where the product is stored.                                            |
| `isValid`  ==Boolean==             | Indicates whether the line item is valid.                                                             |
| `validationErrors` [ ==[ValidationErrorType]== ](validation-error-type.md) | A list of validation errors associated with the line item.    |
| `catalogId`  ==String==            | The identifier of the catalog to which the product belongs.                                           |
| `categoryId`  ==String==           | The identifier of the category to which the product belongs.                                          |
| `createdDate`  ==DateTime==        | The date and time when the line item was created.                                                     |
| `height`  ==Decimal==              | The height of the product.                                                                            |
| `id`  ==String!==                  | The unique identifier of the line item.                                                               |
| `imageUrl`  ==String==             | The URL of the image associated with the line item.                                                   |
| `isGift`  ==Boolean==              | Indicates whether the line item is a gift.                                                            |
| `isReadOnly`  ==Boolean==          | Indicates whether the line item is read-only.                                                         |
| `isReccuring`  ==Boolean==         | Indicates whether the line item is recurring.                                                         |
| `selectedForCheckout`  ==Boolean== | Indicates whether the line item is selected for buying.                                               |
| `languageCode`  ==String==         | The language code associated with the line item.                                                      |
| `length`  ==Decimal==              | The length of the product.                                                                            |
| `measureUnit`  ==String==          | The unit of measurement for the product.                                                              |
| `name`  ==String==                 | The name of the line item.                                                                            |
| `note`  ==String==                 | A note or additional information about the line item.                                                 |
| `objectType`  ==String==           | The type of object for the line item.                                                                 |
| `productId`  ==String==            | The identifier of the product associated with the line item.                                          |
| `productType`  ==String==          | The type of product for the line item.                                                                |
| `quantity`  ==Int==                | The quantity of the line item.                                                                        |
| `requiredShipping`  ==Boolean==    | Indicates whether shipping is required for the line item.                                             |
| `shipmentMethodCode`  ==String==   | The code representing the shipment method for the line item.                                          |
| `sku`  ==String==                  | The stock keeping unit (SKU) for the line item.                                                       |
| `taxPercentRate`  ==Decimal==      | The tax percent rate applied to the line item.                                                        |
| `taxType`  ==String==              | The type of tax applied to the line item.                                                             |
| `thumbnailImageUrl`  ==String==    | The URL of the thumbnail image associated with the line item.                                         |
| `volumetricWeight`  ==Decimal==    | The volumetric weight of the line item.                                                               |
| `weight`  ==Decimal==              | The weight of the line item.                                                                          |
| `weightUnit`  ==String==           | The unit of weight measurement used for the line item.                                                |
| `width`  ==Decimal==               | The width of the product.                                                                             |
| `fulfillmentCenterId`  ==String==  | The identifier of the fulfillment center associated with the line item.                               |

