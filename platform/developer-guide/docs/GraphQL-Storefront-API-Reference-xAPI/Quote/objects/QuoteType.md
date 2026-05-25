# QuoteType ==~object~==

This type contains various fields or attributes that provide information about the quote. 

## Fields

| Field                                         | Description                                                                       |
| --------------------------------------------- | --------------------------------------------------------------------------------- |
| `cancelledDate`  ==DateTime==                 | The date when the quote was cancelled.                                             |
| `cancelReason`  ==String==                    | The reason for cancelling the quote.                                               |
| `channelId`  ==String==                       | The Id for the channel through which the quote was placed.                        |
| `comment`  ==String==                         | Any additional comments or notes related to the quote.                            |
| `coupon`  ==String==                          | The coupon associated with the quote.                                             |
| `customerId`  ==String==                      | The Id for the customer who placed the quote.                                     |
| `customerName`  ==String==                    | The name of the customer who placed the quote.                                    |
| `createdBy`  ==String==                       | The user responsible for creating the quote.                                      |
| `createdDate`  ==DateTime!==                  | The date and time when the quote was created.                                     |
| `employeeId`  ==String==                      | The Id of the employee associated with the quote.                                 |
| `employeeName`  ==String==                    | The name of the employee linked to the quote.                                     |
| `enableNotification`  ==Boolean!==            | A flag indicating whether notifications related to the quote are enabled.         |
| `expirationDate`  ==DateTime==                | The date when the quote or related elements will expire.                          |
| `id`  ==String!==                             | The Id for the quote.                                                             |
| `innerComment`  ==String==                    | Internal comments or notes related to the quote.                                  |
| `isAnonymous`  ==Boolean!==                   | A flag indicating whether the quote is anonymous.                         |
| `isCancelled`  ==Boolean!==                   | A flag indicating whether the quote has been cancelled.                    |
| `isLocked`  ==Boolean!==                      | A flag indicating whether the quote is locked.                            |
| `languageCode`  ==String==                    | The language code associated with the quote.                                      |
| `modifiedBy`  ==String==                      | The user who last modified the quote.                                             |
| `modifiedDate`  ==DateTime==                  | The date and time when the quote was last modified.                               |
| `number`  ==String!==                         | The unique quote number.                                                          |
| `objectType`  ==String==                      | The type of object the quote represents within the system.                        |
| `organizationId`  ==String==                  | The Id of the organization associated with the quote.                             |
| `organizationName`  ==String==                | The name of the organization linked to the quote.                                 |
| `reminderDate`  ==DateTime==                  | The date when a reminder associated with the quote is set to trigger.             |
| `status`  ==String==                          | The status of the quote.                                                          |
| `storeId`  ==String!==                        | The Id for the store where the quote was placed.                                  |
| `tag`  ==String==                             | A tag or label associated with the quote.                                         |   
| `currency` [ ==CurrencyType== ](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/quote/objects/currency-type) | The currency used for financial transactions within the quote. |
| `manualRelDiscountAmount`  ==MoneyType==      | The manually applied relative discount amount.                                    |
| `manualShippingTotal`  ==MoneyType==          | The manually calculated shipping total for the quote.                             |
| `manualSubTotal`  ==MoneyType==               | The manually calculated subtotal for the quote.                                   |
| `totals` [ ==QuoteTotalsType== ](QuoteTotalsType.md)| A structured set of data representing various quote totals.                 |
| `items` [ ==[QuoteItemType]== ](QuoteItemtype.md) | An array of items comprising the quote.                                       |
| `addresses` [ ==[QuoteAddressType]== ](QuoteAddressType.md) | An array of addresses associated with the quote.                    |
| `attachments` [ ==[QuoteAttachmentType]== ](QuoteAttachmentType.md) | An array of attachments or documents linked to the quote.   |
| `shipmentMethod` [ ==QuoteShipmentMethodType== ](QuoteShipmentMethodType.md)| The selected method for shipping items in the quote.|
| `taxDetails` [ ==[QuoteTaxDetailType]== ](QuoteTaxDetailType.md) | An array of tax details associated with the quote.             |
| `dynamicProperties(...)` [ ==[DynamicPropertyValueType]== ](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Cart/objects/dynamic-property-value-type) | An array of dynamic properties that can be associated with the quote.     |