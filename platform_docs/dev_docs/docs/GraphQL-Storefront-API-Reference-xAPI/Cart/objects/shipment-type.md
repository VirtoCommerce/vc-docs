# ShipmentType ==~object~==

The `ShipmentType` represents a shipment within a shopping cart or order. 

## Fields

| Field                                                             | Description                                                                                                          |
|-------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| `id` {==String==}                                                 | The unique identifier of the shipment.                                                                               |
| `shipmentMethodCode` {==String==}                                 | The code representing the shipment method.                                                                           |
| `shipmentMethodOption` {==String==}                               | The specific option or variant of the shipment method.                                                               |
| `fulfillmentCenterId` {==String==}                                | The unique identifier of the fulfillment center responsible for handling the shipment.                               |
| `deliveryAddress` [{==CartAddressType==}](cart-address-type.md)   | The address where the shipment should be delivered, represented as a `CartAddressType` object.                       |
| `volumetricWeight` {==Decimal==}                                  | The volumetric weight of the shipment.                                                                               |
| `weightUnit` {==String==}                                         | The unit of weight measurement used for the shipment.                                                                |
| `weight` {==Decimal==}                                            | The weight of the shipment.                                                                                          |
| `measureUnit` {==String==}                                        | The unit of measurement used for the dimensions of the shipment.                                                     |
| `height` {==Decimal==}                                            | The height of the shipment.                                                                                          |
| `length` {==Decimal==}                                            | The length of the shipment.                                                                                          |
| `width` {==Decimal==}                                             | The width of the shipment.                                                                                           |
| `price` [{==MoneyType==}](money-type.md)                          | The price of the shipment, represented as a `MoneyType` object.                                                      |
| `priceWithTax` [{==MoneyType==}](money-type.md)                   | The price of the shipment including taxes, represented as a `MoneyType` object.                                      |
| `total` [{==MoneyType==}](money-type.md)                          | The total cost of the shipment, represented as a `MoneyType` object.                                                 |
| `totalWithTax` [{==MoneyType==}](money-type.md)                   | The total cost of the shipment including taxes, represented as a `MoneyType` object.                                 |
| `discountAmount` [{==MoneyType==}](money-type.md)                 | The discount amount applied to the shipment, represented as a `MoneyType` object.                                    |
| `discountAmountWithTax` [{==MoneyType==}](money-type.md)          | The discount amount applied to the shipment including taxes, represented as a `MoneyType` object.                    |
| `items` [{==[CartShipmentItemType]==}](cart-shipment-item-type.md)| The items included in the shipment, represented as an array of `CartShipmentItemType` objects.                       |
| `taxTotal` {==MoneyType==}                                        | The total tax amount applied to the shipment, represented as a `MoneyType` object.                                   |
| `taxPercentRate` {==Decimal==}                                    | The tax rate applied to the shipment.                                                                                |
| `taxType` {==String==}                                            | The type or category of tax applied to the shipment.                                                                 |
| `taxDetails` [{==[TaxDetailType]==}](tax-detail-type.md)          | The details of the taxes applied to the shipment, represented as an array of `TaxDetailType` objects.                |
| `discounts` [{==[DiscountType]==}](discount-type.md)              | The discounts applied to the shipment, represented as an array of `DiscountType` objects.                            |
| `currency` [{==CurrencyType==}](currency-type.md)                 | The currency used for the shipment, represented as a `CurrencyType` object.                                          |
| `comment` {==String==}                                            | Additional comments or notes related to the shipment.                                                                |
| `vendor` [{==CommonVendor==}](../../Catalog/objects/CommonVendor/Commonvendor.md) | The vendor associated with the shipment.                                                             |
| `dynamicProperties(...)` [{==[DynamicPropertyValueType]==}](dynamic-property-value-type.md) | The dynamic properties associated with the shipment, represented as an array of `DynamicPropertyValueType` objects. |
