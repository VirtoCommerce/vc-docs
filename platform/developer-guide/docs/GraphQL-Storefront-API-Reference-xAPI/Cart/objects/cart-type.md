# CartType ==~object~==

The `CartType` defines the properties and fields associated with a shopping cart. 

## Fields

| Field                                                                       | Description                                                                                                 |
|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| `id`  ==String==                                                            | The unique identifier of the cart.                                                          	            |
| `name`  ==String!==                             	                          | The name of the cart.                                                                                       |
| `status`  ==String==                             	                          | The status of the cart.                                                                     	            |
| `storeId`  ==String==                                                       | The identifier of the store associated with the cart.                                        	            |
| `channelId`  ==String==                          	                          | The identifier of the channel associated with the cart.                                     	            |
| `hasPhysicalProducts`  ==Boolean==                                          | Indicates whether the cart contains physical products or not.                                               |
| `isAnonymous`  ==Boolean==                      	                          | Indicates whether the cart is anonymous or associated with a user.                        	                |
| `customerId`  ==String==                        	                          | The identifier of the customer associated with the cart.                                    	            |
| `customerName`  ==String==                      	                          | The name of the customer associated with the cart.                                                          |
| `organizationId`  ==String==                     	                          | The identifier of the organization associated with the cart.                                 	            |
| `isRecurring`  ==Boolean==                      	                          | Indicates whether the cart is for a recurring purchase or not.                                              |
| `comment`  ==String==                           	                          | Additional comment or notes related to the cart.                                           	                |
| `purchaseOrderNumber`  ==String==                	                          | The purchase order number associated with the cart.                                         	            |
| `volumetricWeight`  ==Decimal==                 	                          | The volumetric weight of the cart.                                                                          |
| `weightUnit`  ==String==                         	                          | The unit of weight measurement used for the cart.                                                           |
| `weight`  ==Decimal==                            	                          | The weight of the cart.                                                                                    	|
| `total` [ ==MoneyType== ](money-type.md)         	                          | The total amount of the cart.                                                                              	|
| `subTotal` [ ==MoneyType== ](money-type.md)                                 | The subtotal amount of the cart without considering discounts, taxes, or additional fees.                  	|
| `subTotalWithTax` [ ==MoneyType== ](money-type.md)                          | The subtotal amount of the cart including taxes.                                                           	|
| `extendedPriceTotal` [ ==MoneyType== ](money-type.md)                       | The extended price total of the cart, including discounts, taxes, and additional fees.                     	|
| `extendedPriceTotalWithTax` [ ==MoneyType== ](money-type.md)                | The extended price total of the cart, including discounts, taxes, and additional fees, with taxes applied. 	|
| `currency` [ ==CurrencyType== ](currency-type.md)                           | The currency associated with the cart.                                                                     	|
| `taxTotal` [ ==MoneyType== ](money-type.md)                                 | The total amount of taxes applied to the cart.                                                             	|
| `taxPercentRate`  ==Decimal==                                               | The percentage rate of taxes applied to the cart.                                                          	|
| `taxType`  ==String==                                                       | The type of taxes applied to the cart.                                                                     	|
| `taxDetails` [ ==TaxDetailType== ](tax-detail-type.md)                      | A list of tax details associated with the cart.                                                            	|
| `fee` [ ==MoneyType== ](money-type.md)                                      | The additional fee applied to the cart.                                                                    	|
| `shippingPrice` [ ==MoneyType== ](money-type.md)                            | The price of shipping for the cart.                                                                        	|
| `shippingPriceWithTax` [ ==MoneyType== ](money-type.md)                     | The price of shipping for the cart, including taxes.                                                       	|
| `shippingTotal` [ ==MoneyType== ](money-type.md)                            | The total amount of shipping charges for the cart.                                                         	|
| `shippingTotalWithTax` [ ==MoneyType== ](money-type.md)                     | The total amount of shipping charges for the cart, including taxes.                                        	|
| `shipments` [ ==ShipmentType== ](shipment-type.md)                          | A list of shipments associated with the cart.                                                              	|
| `availableShippingMethods` [ ==ShippingMethodType== ](shipping-method-type.md) | A list of available shipping methods for the cart.                                                     	|
| `paymentPrice` [ ==MoneyType== ](money-type.md)                        	  | The price of payment for the cart.                                                                         	|
| `paymentPriceWithTax` [ ==MoneyType== ](money-type.md)                   	  | The price of payment for the cart, including taxes.                                                        	|
| `paymentTotal` [ ==MoneyType== ](money-type.md)                         	  | The total amount of payment charges for the cart.                                                          	|
| `paymentTotalWithTax` [ ==MoneyType== ](money-type.md)             	      | The total amount of payment charges for the cart, including taxes.                                         	|
| `payments` [ ==PaymentType== ](payment-type.md)                      	      | A list of payments associated with the cart.                                                               	|
| `availablePaymentMethods` [ ==PaymentMethodType== ](payment-method-type.md) | A list of available payment methods for the cart. 	                                                        |
| `handlingTotal` [ ==MoneyType== ](money-type.md)                            | The total amount of handling charges for the cart.                                                         	|
| `handlingTotalWithTax` [ ==MoneyType== ](money-type.md)  	                  | The total amount of handling charges for the cart, including taxes.                                        	|
| `discountTotal` [ ==MoneyType== ](money-type.md)                            | The total discount amount applied to the cart.                                                             	|
| `discountTotalWithTax` [ ==MoneyType== ](money-type.md)                     | The total discount amount applied to the cart, including taxes.                                            	|
| `subTotalDiscount` [ ==MoneyType== ](money-type.md)                         | The discount amount applied to the cart's subtotal.                                                        	|
| `subTotalDiscountWithTax` [ ==MoneyType== ](money-type.md)                  | The discount amount applied to the cart's subtotal, including taxes.                                       	|
| `discounts` [ ==DiscountType== ](discount-type.md)                       	  | A list of discounts applied to the cart.                                                                   	|
| `addresses` [ ==CartAddressType== ](cart-address-type.md)                	  | A list of addresses associated with the cart.                                                              	|
| `gifts` [ ==GiftItemType== ](gift-item-type.md)                       	  | A list of gift items associated with the cart.                                                             	|
| `availableGifts`  [ ==GiftItemType== ](gift-item-type.md)                   | A list of available gift items for the cart.                                                                |
| `items` [ ==LineItemType== ](line-item-type.md)                             | A list of line items (products) in the cart.                                                                |
| `itemsCount`  ==Int==                                                       | The total number of items in the cart.                                                                      |
| `itemsQuantity`  ==Int==                                                    | The total quantity of items in the cart.                                                                    |
| `coupons` [ ==CouponType== ](coupon-type.md)                                | A list of coupons applied to the cart.                                                                      |
| `dynamicProperties(...)` [ ==DynamicPropertyValueType== ](dynamic-property-value-type.md) | A list of dynamic properties associated with the cart.                                        |
| `validationErrors(...)` [ ==ValidationErrorType== ](validation-error-type.md)             | A list of validation errors associated with the cart.                                         |
| `type`  ==String==                                                          | The type of the cart.                                                                                       |
| `warnings` [ ==ValidationErrorType== ](validation-error-type.md)            | A list of warnings associated with the cart.                                                                |

The `Cart.Addresses` field in `CartType` is a functional enabler. Currently, it is not featured in any internal business logic and is separated from `Cart.Billing.Addresses` and `Cart.Shipping.Addresses`. Feel free to add your own business logic to it.

You can find the address type structure [here](https://github.com/VirtoCommerce/vc-module-experience-api/blob/dev/src/VirtoCommerce.ExperienceApiModule.Core/Schemas/AddressType.cs).