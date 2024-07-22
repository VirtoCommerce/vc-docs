# CartType ==~object~==

This type defines the properties and fields associated with a shopping cart. 

## Fields

| Field                                                                                         | Description                                                                 |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| `id` ==String!==                                                                              | The Id for the cart.                                                        |
| `name` ==String!==                                                                            | The name of the cart.                                                       |
| `status` ==String==                                                                           | The current status of the cart.                                             |
| `storeId` ==String!==                                                                         | The Id of the store associated with the cart.                               |
| `channelId` ==String==                                                                        | The Id of the sales channel associated with the cart.                       |
| `hasPhysicalProducts` ==Boolean==                                                             | Indicates whether the cart contains physical products.                      |
| `isAnonymous` ==Boolean!==                                                                    | Indicates whether the cart is associated with an anonymous user.            |
| `customerId` ==String!==                                                                      | The Id of the customer associated with the cart.                            |
| `customerName` ==String==                                                                     | The name of the customer associated with the cart.                          |
| `organizationId` ==String==                                                                   | The Id of the organization associated with the cart.                        |
| `organizationName` ==String==                                                                 | The name of the organization associated with the cart.                      |
| `isRecuring` ==Boolean==                                                                      | Indicates whether the cart is for a recurring order.                        |
| `comment` ==String==                                                                          | Any comments associated with the cart.                                      |
| `purchaseOrderNumber` ==String==                                                              | The purchase order number associated with the cart.                         |
| `volumetricWeight` ==Decimal==                                                                | The volumetric weight of the items in the cart.                             |
| `weightUnit` ==String==                                                                       | The unit of weight measurement used.                                        |
| `weight` ==Decimal==                                                                          | The total weight of the items in the cart.                                  |
| `total` [==MoneyType!==](../objects/money-type.md)                                            | The total cost of the cart.                                                 |
| `subTotal` [==MoneyType!==](../objects/money-type.md)                                         | The subtotal of the cart before taxes and discounts.                        |
| `subTotalWithTax` [==MoneyType!==](../objects/money-type.md)                                  | The subtotal of the cart including taxes.                                   |
| `extendedPriceTotal` [==MoneyType!==](../objects/money-type.md)                               | The total extended price of the items in the cart.                          |
| `extendedPriceTotalWithTax` [==MoneyType!==](../objects/money-type.md)                        | The total extended price of the items in the cart including taxes.          |
| `currency` [==CurrencyType!==](../objects/currency-type.md)                                   | The currency used for the cart.                                             |
| `taxTotal` [==MoneyType!==](../objects/money-type.md)                                         | The total amount of tax for the cart.                                       |
| `taxPercentRate` ==Decimal!==                                                                 | The tax rate applied to the cart.                                           |
| `taxType` ==String==                                                                          | The type of tax applied to the cart.                                        |
| `taxDetails` [==[TaxDetailType!]!==](../objects/tax-detail-type.md)                           | A list of detailed tax information for the cart.                            |
| `fee` [==MoneyType!==](../objects/money-type.md)                                              | The fee associated with the cart.                                           |
| `feeWithTax` [==MoneyType!==](../objects/money-type.md)                                       | The fee including taxes.                                                    |
| `feeTotal` [==MoneyType!==](../objects/money-type.md)                                         | The total fee for the cart.                                                 |
| `feeTotalWithTax` [==MoneyType!==](../objects/money-type.md)                                  | The total fee for the cart including taxes.                                 |
| `shippingPrice` [==MoneyType!==](../objects/money-type.md)                                    | The shipping price for the cart.                                            |
| `shippingPriceWithTax` [==MoneyType!==](../objects/money-type.md)                             | The shipping price including taxes.                                         |
| `shippingTotal` [==MoneyType!==](../objects/money-type.md)                                    | The total shipping cost for the cart.                                       |
| `shippingTotalWithTax` [==MoneyType!==](../objects/money-type.md)                             | The total shipping cost including taxes.                                    |
| `shipments` [==[ShipmentType!]!==](../objects/shipment-type.md)                               | A list of shipments associated with the cart.                               |
| `availableShippingMethods` [==[ShippingMethodType!]!==](../objects/shipping-method-type.md)   | A list of available shipping methods for the cart.                          |
| `paymentPrice` [==MoneyType!==](../objects/money-type.md)                                     | The price of the payment method for the cart.                               |
| `paymentPriceWithTax` [==MoneyType!==](../objects/money-type.md)                              | The price of the payment method including taxes.                            |
| `paymentTotal` [==MoneyType!==](../objects/money-type.md)                                     | The total payment amount for the cart.                                      |
| `paymentTotalWithTax` [==MoneyType!==](../objects/money-type.md)                              | The total payment amount including taxes.                                   |
| `payments` [==[PaymentType!]!==](../objects/payment-type.md)                                  | A list of payments associated with the cart.                                |
| `availablePaymentMethods` [==[PaymentMethodType!]!==](../objects/payment-method-type.md)      | A list of available payment methods for the cart.                           |
| `handlingTotal` [==MoneyType!==](../objects/money-type.md)                                    | The total handling fee for the cart.                                        |
| `handlingTotalWithTax` [==MoneyType!==](../objects/money-type.md)                             | The total handling fee including taxes.                                     |
| `discountTotal` [==MoneyType!==](../objects/money-type.md)                                    | The total discount applied to the cart.                                     |
| `discountTotalWithTax` [==MoneyType!==](../objects/money-type.md)                             | The total discount including taxes.                                         |
| `subTotalDiscount` [==MoneyType!==](../objects/money-type.md)                                 | The discount applied to the subtotal of the cart.                           |
| `subTotalDiscountWithTax` [==MoneyType!==](../objects/money-type.md)                          | The discount applied to the subtotal including taxes.                       |
| `discounts` [==[DiscountType!]!==](../objects/discount-type.md)                               | A list of discounts applied to the cart.                                    |
| `addresses` [==[CartAddressType!]!==](../objects/money-type.md)                               | A list of addresses associated with the cart.                               |
| `gifts` [==[GiftItemType!]!==](../objects/gift-item-type.md)                                  | A list of gift items in the cart.                                           |
| `availableGifts` [==[GiftItemType!]!==](../objects/gift-item-type.md)                         | A list of available gift items for the cart.                                |
| `items` [==[LineItemType!]!==](../objects/line-item-type.md)                                  | A list of line items in the cart.                                           |
| `itemsCount` ==Int!==                                                                         | The total number of items in the cart.                                      |
| `itemsQuantity` ==Int!==                                                                      | The total quantity of items in the cart.                                    |
| `coupons` [==[CouponType!]!==](../objects/coupon-type.md)                                     | A list of coupons applied to the cart.                                      |
| `dynamicProperties`(...) [==[DynamicPropertyValueType!]!==](../objects/dynamic-property-value-type.md) | A list of dynamic properties associated with the cart.             |
| `validationErrors`(...) [==[ValidationErrorType!]!==](../objects/validation-error-type.md)    | A list of validation errors associated with the cart.                       |
| `type` ==String==                                                                             | The type of the cart.                                                       |
| `warnings` [==[ValidationErrorType!]!==](../objects/validation-error-type.md)                 | A list of warnings related to the cart.                                     |

The `Cart.Addresses` field in `CartType` is a functional enabler. Currently, it is not featured in any internal business logic and is separated from `Cart.Billing.Addresses` and `Cart.Shipping.Addresses`. Feel free to add your own business logic to it.

You can find the address type structure [here](https://github.com/VirtoCommerce/vc-module-experience-api/blob/dev/src/VirtoCommerce.ExperienceApiModule.Core/Schemas/AddressType.cs).