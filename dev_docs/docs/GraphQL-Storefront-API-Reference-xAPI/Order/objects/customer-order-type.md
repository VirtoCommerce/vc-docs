# CustomerOrderType ==~object~==

The `CustomerOrderType` represents a customer order. 

## Fields

| Field                               | Description                                                                                                                         |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `id` {==String!==}                   | The Id of the customer order.                                                                                                      |
| `operationType` {==String!==}        | The type of operation associated with the customer order.                                                                          |
| `parentOperationId` {==String==}    | The Id of the parent operation.                                                                                                     |
| `number` {==String!==}               | The unique number or Id of the customer order.                                                                                     |
| `isApproved` {==Boolean!==}          | Indicates whether the customer order is approved.                                                                                  |
| `status` {==String==}               | The current status of the customer order.                                                                                           |
| `statusDisplayValue` {==String==}   | A representation of the current status of the customer order. Localized representation, if any.                                     |
| `comment` {==String==}              | A comment or note associated with the customer order.                                                                               |
| `outerId` {==String==}              | An external Id for the customer order.                                                                                              |
| `isCancelled` {==Boolean!==}         | Indicates whether the customer order is cancelled.                                                                                 |
| `cancelledDate` {==DateTime==}      | The date and time when the customer order was cancelled.                                                                            |
| `cancelReason` {==String==}         | The reason for canceling the customer order.                                                                                        |
| `objectType` {==String!==}           | The type of the customer order object.                                                                                             |
| `customerId` {==String!==}           | The Id of the customer associated with the order.                                                                                  |
| `customerName` {==String==}         | The name of the customer associated with the order.                                                                                 |
| `channelId` {==String==}            | The Id of the channel associated with the order.                                                                                    |
| `storeId` {==String!==}              | The Id of the store associated with the order.                                                                                     |
| `storeName` {==String==}            | The name of the store associated with the order.                                                                                    |
| `organizationId` {==String==}       | The Id of the organization associated with the order.                                                                               |
| `organizationName` {==String==}     | The name of the organization associated with the order.                                                                             |
| `employeeId` {==String==}           | The Id of the employee associated with the order.                                                                                   |
| `employeeName` {==String==}         | The name of the employee associated with the order.                                                                                 |
| `shoppingCartId` {==String==}       | The Id of the shopping cart associated with the order.                                                                              |
| `isPrototype` {==Boolean!==}         | Indicates whether the order is a prototype.                                                                                        |
| `subscriptionNumber` {==String==}   | The number or Id of the subscription associated with the order.                                                                     |
| `subscriptionId` {==String==}       | The Id of the subscription associated with the order.                                                                               |
| `fee` {==MoneyType==}               | The fee amount associated with the order.                                                                                           |
| `purchaseOrderNumber` {==String==}  | The purchase order number associated with the order.                                                                                |
| `feeWithTax` {==Decimal!==}          | The fee amount with tax included.                                                                                                  |
| `feeTotal` {==Decimal!==}            | The total fee amount.                                                                                                              |
| `feeTotalWithTax` {==Decimal!==}     | The total fee amount with tax included.                                                                                            |
| `taxType` {==String==}              | The type of tax applied to the order.                                                                                               |
| `taxPercentRate` {==Decimal!==}      | The tax percent rate applied to the order.                                                                                         |
| `languageCode` {==String==}        | The language code associated with the order.                                                                                         |
| `createdDate` {==DateTime!==}       | The date and time of the order creation.                                                                                            |
| `createdBy` {==String==}           | The user or entity who created the order.                                                                                            |
| `modifiedDate` {==DateTime==}      | The date and time when the order was last modified.                                                                                  |
| `modifiedBy` {==String==}          | The user or entity who last modified the order.                                                                                      |
| `currency` {==CurrencyType==}      | The currency type used for monetary values in the order.                                                                             |
| `total` {==MoneyType==}             | The total amount of the order.                                                                                                      |
| `taxTotal` {==MoneyType==}          | The total tax amount for the order.                                                                                                 |
| `discountAmount` {==MoneyType==}    | The total discount amount applied to the order.                                                                                     |
| `subTotal` {==MoneyType==}          | The subtotal amount for the order.                                                                                                  |
| `subTotalWithTax` {==MoneyType==}   | The subtotal amount with tax included.                                                                                              |
| `subTotalDiscount` {==MoneyType==}  | The total discount applied to the order sub-total.                                                                                  |
| `subTotalDiscountWithTax` {==MoneyType==} | The total discount amount with tax included for the order sub-total.                                                          |
| `subTotalTaxTotal` {==MoneyType==}  | The total tax amount applied to the order sub-total.                                                                                |
| `shippingTotal` {==MoneyType==}     | The total shipping amount for the order.                                                                                            |
| `shippingTotalWithTax` {==MoneyType==} | The total shipping amount with tax included.                                                                                     |
| `shippingSubTotal` {==MoneyType==}  | The shipping sub-total amount for the order.                                                                                        |
| `shippingSubTotalWithTax` {==MoneyType==} | The shipping sub-total amount with tax included.                                                                              |
| `shippingDiscountTotal` {==MoneyType==} | The total discount applied to the shipping.                                                                                     |
| `shippingDiscountTotalWithTax` {==MoneyType==} | The total discount amount with tax included for the shipping.                                                            |
| `shippingTaxTotal` {==MoneyType==}  | The total tax amount applied to the shipping.                                                                                       |
| `paymentTotal` {==MoneyType==}     | The total payment amount for the order.                                                                                              |
| `paymentTotalWithTax` {==MoneyType==} | The total payment amount with tax included.                                                                                       |
| `paymentSubTotal` {==MoneyType==}  | The payment sub-total amount for the order.                                                                                          |
| `paymentSubTotalWithTax` {==MoneyType==} | The payment sub-total amount with tax included.                                                                                |
| `paymentDiscountTotal` {==MoneyType==} | The total discount applied to the payment.                                                                                       |
| `paymentDiscountTotalWithTax` {==MoneyType==} | The total discount amount with tax included for the payment.                                                              |
| `paymentTaxTotal` {==MoneyType==}  | The total tax amount applied to the payment.                                                                                         |
| `discountTotal` {==MoneyType==}    | The total discount amount for the order.                                                                                             |
| `discountTotalWithTax` {==MoneyType==} | The total discount amount with tax included for the order.                                                                       |
| `addresses` [{==[OrderAddressType]!==}](order-address-type.md) | Addresses associated with the order.                                                                     |
| `items` [{==[OrderLineItemType]!==}](order-line-item-type.md) | Items (order line items) included in the order.                                                           |
| `inPayments` [{==[PaymentInType]!==}](payment-in-type.md) | In-payment entities associated with the order.                                                                |
| `shipments` [{==[OrderShipmentType]==}](order-shipment-type.md) | Shipments associated with the order.                                                                    |
| `taxDetails` [{==[OrderTaxDetailType]!==}](order-tax-detail-type.md) | Tax details for the order.                                                                         |
| `dynamicProperties` [{==[DynamicPropertyValueType]==}](../../Cart/objects/dynamic-property-value-type.md) | An array of dynamic property value types.                     |
| `coupons` {==[String]==}            | Coupon codes applied to the order.                                                                                                  |
| `discounts` [{==[OrderDiscountType]==}](order-discount-type.md) | Discount entities associated with the order.                                                            |
| `availablePaymentMethods` [{==[OrderPaymentMethodType]==}](order-payment-method-type.md) | An array of available payment methods for the order.                           |
