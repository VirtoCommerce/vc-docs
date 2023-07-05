# PriceType ==~object~==

The `priceType` object represents the pricing information for a product or variation.

## Fields

| Field                                 	| Description                                                                                                           	|
|---------------------------------------	|-----------------------------------------------------------------------------------------------------------------------	|
| `list` {==MoneyType==}                  	| The regular price of the item without any discounts or taxes applied.                                                 	|
| `listWithTax` {==MoneyType==}           	| The regular price of the item including taxes.                                                                        	|
| `sale` {==MoneyType==}                  	| The discounted price of the item without taxes applied.                                                               	|
| `saleWithTax` {==MoneyType==}           	| The discounted price of the item including taxes.                                                                     	|
| `actual` {==MoneyType==}                	| The current actual price of the item, which may reflect a sale or promotion.                                          	|
| `actualWithTax` {==MoneyType==}         	| The current actual price of the item including taxes.                                                                 	|
| `discountAmount` {==MoneyType==}        	| The amount of discount applied to the item without taxes.                                                             	|
| `discountAmountWithTax` {==MoneyType==} 	| The amount of discount applied to the item including taxes.                                                           	|
| `discountPercent` {==Decimal==}         	| The percentage of discount applied to the item.                                                                       	|
| `currency` {==String==}                 	| The currency code in which the prices are expressed.                                                                  	|
| `startDate` {==DateTime==}              	| The start date and time of the pricing period or promotion.                                                           	|
| `endDate` {==DateTime==}                	| The end date and time of the pricing period or promotion.                                                             	|
| `tierPrices` [{==TierPriceType==}](TierPriceType.md)        	| The tiered pricing options available for the item. 	                                                |
| `discounts` [{==CatalogDiscountType==}](CatalogDiscountType.md)   	| The catalog-level discounts applied to the item.                                             	|
| `pricelistId` {==String==}              	| The Id of the price list to which the item's price belongs.                                                           	|
| `minQuantity` {==Int==}                 	| The minimum quantity required to be eligible for the price or discount.                                               	|