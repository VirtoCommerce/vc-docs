# OrderShipmentType ==~object~==

The `OrderShipmentType` contains information about a shipment within a customer order.

## Fields

| Field                                                                                                          | Description                                                        |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| `id` {==String!==}                                                                                             | The Id of the shipment.                                            |
| `operationType` {==String!==}                                                                                  | The type of operation associated with the shipment.                |
| `parentOperationId` {==String==}                                                                               | The Id of the parent operation.                                    |
| `number` {==String!==}                                                                                         | The unique number identifying the shipment.                        |
| `isApproved` {==Boolean!==}                                                                                    | Indicates whether the shipment is approved.                        |
| `status` {==String==}                                                                                          | The status of the shipment, indicating its current state.          |
| `comment` {==String==}                                                                                         | An optional comment or note related to the shipment.               |
| `outerId` {==String==}                                                                                         | An external Id associated with the shipment.                       |
| `isCancelled` {==Boolean!==}                                                                                   | Indicates whether the shipment is cancelled.                       |
| `cancelledDate` {==DateTime==}                                                                                 | The date and time when the shipment was cancelled.                 |
| `cancelReason` {==String==}                                                                                    | A reason for the cancellation of the shipment.                     |
| `objectType` {==String!==}                                                                                     | The type of the shipment object.                                   |
| `organizationId` {==String==}                                                                                  | The Id of the organization associated with the shipment.           |
| `organizationName` {==String==}                                                                                | The name of the organization associated with the shipment.         |
| `fulfillmentCenterId` {==String==}                                                                             | The Id of the fulfillment center used for the shipment.            |
| `fulfillmentCenterName` {==String==}                                                                           | The name of the fulfillment center used for the shipment.          |
| `employeeId` {==String==}                                                                                      | The Id of the employee associated with the shipment.               |
| `employeeName` {==String==}                                                                                    | The name of the employee associated with the shipment.             |
| `shipmentMethodCode` {==String==}                                                                              | The code representing the shipment method used for delivery.       |
| `shipmentMethodOption` {==String==}                                                                            | The option or variant of the shipment method used for delivery.    |
| `shippingMethod` [{==OrderShippingMethodType==}](order-shipping-method-type.md)                                | The shipping method type used for the shipment.                    |
| `customerOrderId` {==String==}                                                                                 | The Id of the customer order associated with the shipment.         |
| `weightUnit` {==String==}                                                                                      | The unit of weight used for the shipment.                          |
| `weight` {==Decimal==}                                                                                         | The weight of the shipment.                                        |
| `measureUnit` {==String==}                                                                                     | The unit of measurement used for the dimensions of the shipment.   |
| `height` {==Decimal==}                                                                                         | The height of the shipment.                                        |
| `length` {==Decimal==}                                                                                         | The length of the shipment.                                        |
| `width` {==Decimal==}                                                                                          | The width of the shipment.                                         |
| `deliveryAddress` [{==OrderAddressType==}](order-address-type.md)                                              | The address to which the shipment will be delivered.               |
| `taxType` {==String==}                                                                                         | The type of tax applied to the shipment.                           |
| `taxPercentRate` {==Decimal!==}                                                                                | The tax percentage rate applied to the shipment.                   |
| `trackingNumber` {==String==}                                                                                  | The tracking number associated with the shipment.                  |
| `trackingUrl` {==String==}                                                                                     | The URL where the customer can track the shipment.                 |
| `deliveryDate` {==DateTime==}                                                                                  | The expected delivery date and time for the shipment.              |
| `price` {==MoneyType==}                                                                                        | The price associated with the shipment.                            |
| `priceWithTax` {==MoneyType==}                                                                                 | The price of the shipment including tax.                           |
| `total` {==MoneyType==}                                                                                        | The total price of the shipment.                                   |
| `totalWithTax` {==MoneyType==}                                                                                 | The total price of the shipment including tax.                     |
| `discountAmount` {==MoneyType==}                                                                               | The discount amount applied to the shipment.                       |
| `discountAmountWithTax` {==MoneyType==}                                                                        | The discount amount applied to the shipment, including tax.        |
| `taxTotal` {==MoneyType==}                                                                                     | The total tax amount applied to the shipment.                      |
| `currency` [{==CurrencyType==}](currency-type.md)                                                              | The currency code used for pricing in the shipment.                |
| `taxDetails` [{==[OrderTaxDetailType]==}](order-tax-detail-type.md)                                            | Tax details associated with the shipment.                          |
| `items` [{==[OrderShipmentItemType]==}](order-shipment-item-type.md)                                           | Line items associated with the shipment.                           |
| `packages` [{==[OrderShipmentPackageType]==}](order-shipment-package-type.md)                                  | Packages associated with the shipment.                             |
| `inPayments` [{==[PaymentInType]==}](payment-in-type.md)                                                       | Payment transactions associated with the shipment.                 |
| `discounts` [{==[OrderDiscountType]==}](order-discount-type.md)                                                | Discounts applied to the shipment.                                 |
| `vendor` [{==CommonVendor==}](../../Catalog/objects/CommonVendor/Commonvendor.md)                              | The common vendor associated with the shipment.                    |
| `dynamicProperties(...)` [{==[DynamicPropertyValueType]==}](../../Cart/objects/dynamic-property-value-type.md) | An array of dynamic properties associated with the shipment.       |



