# OrderLineItemType ==~object~==

The `OrderLineItemType` type represents a line item within a customer order.

## Fields

| Field                                                                                                             | Description                                                                                     |
|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `id` {==String!==}                                                                                                | The Id of the order line item.                                                                |
| `productType` {==String==}                                                                                        | The type of the product associated with the order line item.                                     |
| `name` {==String!==}                                                                                              | The name of the product associated with the order line item.                            |
| `comment` {==String==}                                                                                            | An additional information related to the order line item.                                     |
| `imageUrl` {==String==}                                                                                           | An URL to an image representing the product associated with the order line item.       |
| `isGift` {==Boolean==}                                                                                            | Indicates whether the order line item is a gift or not.                               |
| `shippingMethodCode` {==String==}                                                                                 | The code representing the shipping method for the order line item.                              |
| `fulfillmentLocationCode` {==String==}                                                                            | The code representing the fulfillment location for the order line item.                         |
| `fulfillmentCenterId` {==String==}                                                                                | The Id of the fulfillment center associated with the order line item.            |
| `fulfillmentCenterName` {==String==}                                                                              | The name of the fulfillment center associated with the order line item.                         |
| `outerId` {==String==}                                                                                            | An external Id associated with the order line item.                             |
| `weightUnit` {==String==}                                                                                         | The unit of measurement for the weight of the product associated with the order line item.      |
| `weight` {==Decimal==}                                                                                            | The weight of the product associated with the order line item.                                   |
| `measureUnit` {==String==}                                                                                        | The unit of measurement for the dimensions of the product.              |
| `height` {==Decimal==}                                                                                            | The height of the product associated with the order line item.                                   |
| `length` {==Decimal==}                                                                                            | The length of the product associated with the order line item.                                   |
| `width` {==Decimal==}                                                                                             | The width of the product associated with the order line item.                                    |
| `isCancelled` {==Boolean==}                                                                                       | Indicates whether the order line item is cancelled or not.                            |
| `cancelledDate` {==DateTime==}                                                                                    | The date when the order line item was cancelled, if applicable.                                  |
| `cancelReason` {==String==}                                                                                       | The reason for cancelling the order line item, if applicable.                                    |
| `objectType` {==String!==}                                                                                        | The type of the object, which is always "OrderLineItem".                                         |
| `status` {==String==}                                                                                             | The status of the order line item.                                                               |
| `categoryId` {==String==}                                                                                         | The Id of the category associated with the order line item.                      |
| `catalogId` {==String!==}                                                                                         | The Id of the catalog associated with the order line item.                       |
| `sku` {==String!==}                                                                                               | The SKU of the product associated with the order line item.                |
| `priceId` {==String==}                                                                                            | The Id of the price associated with the order line item.                         |
| `price` {==MoneyType==}                                                                                           | The price of the product associated with the order line item.                                    |
| `priceWithTax` {==MoneyType==}                                                                                    | The price of the product including tax, associated with the order line item.                   |
| `taxType` {==String!==}                                                                                           | The type of tax applied to the order line item.                                                  |
| `taxPercentRate` {==Decimal!==}                                                                                   | The percentage rate of tax applied to the order line item.                                      |
| `reserveQuantity` {==Int!==}                                                                                      | The quantity of the product reserved for the order line item.                                   |
| `quantity` {==Int!==}                                                                                             | The quantity of the product associated with the order line item.                                |
| `productId` {==String!==}                                                                                         | The Id of the product associated with the order line item.                      |
| `currency` {==CurrencyType==}                                                                                     | The currency type used for pricing and transactions.                                            |
| `discountAmount` {==MoneyType==}                                                                                  | The amount of discount applied to the product associated with the order line item.             |
| `discountAmountWithTax` {==MoneyType==}                                                                          | The amount of discount, including tax, applied to the product associated with the order line item.|
| `discountTotal` {==MoneyType==}                                                                                   | The total discount amount applied to the order line item.                                       |
| `discountTotalWithTax` {==MoneyType==}                                                                            | The total discount amount, including tax, applied to the order line item.                      |
| `extendedPrice` {==MoneyType==}                                                                                   | The extended price (subtotal after discounts) for the order line item.                         |
| `extendedPriceWithTax` {==MoneyType==}                                                                            | The extended price, including tax (subtotal after discounts), for the order line item.         |
| `placedPrice` {==MoneyType==}                                                                                     | The price of the product when the order was placed.                                              |
| `placedPriceWithTax` {==MoneyType==}                                                                              | The price of the product, including tax, when the order was placed.                            |
| `taxTotal` {==MoneyType==}                                                                                        | The total amount of tax applied to the order line item.                              |
| `taxDetails` [{==[OrderTaxDetailType]==}](order-tax-detail-type.md)                                               | Tax details associated with the order line item.                                   |
| `discounts` [{==[OrderDiscountType]==}](order-discount-type.md)                                                   | Discounts applied to the order line item.                                           |
| `product` [{==Product==}](../../Catalog/objects/ProductType.md)                                                   | The detailed information about the product associated with the order line item.                |
| `vendor` [{==CommonVendor==}](../../Catalog/objects/CommonVendor/Commonvendor.md)                                 | The information about the common vendor associated with the order line item.                   |
| `dynamicProperties(...)` [{==[DynamicPropertyValueType]==}](../../Cart/objects/dynamic-property-value-type.md)    | Dynamic property value types. |