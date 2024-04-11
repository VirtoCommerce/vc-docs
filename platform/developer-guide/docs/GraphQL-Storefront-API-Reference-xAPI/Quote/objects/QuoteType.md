# QuoteType ==~object~==

The `QuoteType` contains various fields or attributes that provide information about the order. 

## Fields

| Field                                         | Description                                                                       |
| --------------------------------------------- | --------------------------------------------------------------------------------- |
| `cancelledDate`  ==DateTime==                 | The date when the order was canceled.                                             |
| `cancelReason`  ==String==                    | The reason for canceling the order.                                               |
| `channelId`  ==String==                       | The Id for the channel through which the order was placed.                        |
| `comment`  ==String==                         | Any additional comments or notes related to the order.                            |
| `coupon`  ==String==                          | The coupon associated with the order.                                             |
| `customerId`  ==String==                      | The Id for the customer who placed the order.                                     |
| `customerName`  ==String==                    | The name of the customer who placed the order.                                    |
| `createdBy`  ==String==                       | The user responsible for creating the order.                                      |
| `createdDate`  ==DateTime!==                  | The date and time when the order was created.                                     |
| `employeeId`  ==String==                      | The Id of the employee associated with the order.                                 |
| `employeeName`  ==String==                    | The name of the employee linked to the order.                                     |
| `enableNotification`  ==Boolean!==            | A flag indicating whether notifications related to the order are enabled.         |
| `expirationDate`  ==DateTime==                | The date when the order or related elements will expire.                          |
| `id`  ==String!==                             | The Id for the order.                                                             |
| `innerComment`  ==String==                    | Internal comments or notes related to the order.                                  |
| `isAnonymous`  ==Boolean!==                   | A flag indicating whether the order is anonymous.                         |
| `isCancelled`  ==Boolean!==                   | A flag indicating whether the order has been canceled.                    |
| `isLocked`  ==Boolean!==                      | A flag indicating whether the order is locked.                            |
| `languageCode`  ==String==                    | The language code associated with the order.                                      |
| `modifiedBy`  ==String==                      | The user who last modified the order.                                             |
| `modifiedDate`  ==DateTime==                  | The date and time when the order was last modified.                               |
| `number`  ==String!==                         | The unique order number.                                                          |
| `objectType`  ==String==                      | The type of object the order represents within the system.                        |
| `organizationId`  ==String==                  | The Id of the organization associated with the order.                             |
| `organizationName`  ==String==                | The name of the organization linked to the order.                                 |
| `reminderDate`  ==DateTime==                  | The date when a reminder associated with the order is set to trigger.             |
| `status`  ==String==                          | The status of the order.                                                          |
| `storeId`  ==String!==                        | The Id for the store where the order was placed.                                  |
| `tag`  ==String==                             | A tag or label associated with the order.                                         |   
| `currency` [ ==CurrencyType== ](../../Order/objects/currency-type.md) | The currency used for financial transactions within the order. |
| `manualRelDiscountAmount`  ==MoneyType==      | The manually applied relative discount amount.                                    |
| `manualShippingTotal`  ==MoneyType==          | The manually calculated shipping total for the order.                             |
| `manualSubTotal`  ==MoneyType==               | The manually calculated subtotal for the order.                                   |
| `totals` [ ==QuoteTotalsType== ](QuoteTotalsType.md)| A structured set of data representing various order totals.                 |
| `items` [ ==[QuoteItemType]== ](QuoteItemtype.md) | An array of items comprising the order.                                       |
| `addresses` [ ==[QuoteAddressType]== ](QuoteAddressType.md) | An array of addresses associated with the order.                    |
| `attachments` [ ==[QuoteAttachmentType]== ](QuoteAttachmentType.md) | An array of attachments or documents linked to the order.   |
| `shipmentMethod` [ ==QuoteShipmentMethodType== ](QuoteShipmentMethodType.md)| The selected method for shipping items in the order.|
| `taxDetails` [ ==[QuoteTaxDetailType]== ](QuoteTaxDetailType.md) | An array of tax details associated with the order.             |
| `dynamicProperties(...)` [ ==[DynamicPropertyValueType]== ](../../Cart/objects/dynamic-property-value-type.md) | An array of dynamic properties that can be associated with the order.     |