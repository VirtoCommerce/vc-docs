# TierPriceType ==~object~==

The `TierPriceType` represents the pricing information for a specific tier or quantity range of a product. It allows setting different prices based on the quantity purchased.

## Fields

| Field                        	| Description                                                                                            	|
|------------------------------	|--------------------------------------------------------------------------------------------------------	|
| `price` {==MoneyType==}        	| The price of the item without any discounts or taxes applied for the specified tier or quantity range. 	|
| `priceWithTax` {==MoneyType==} 	| The price of the item including taxes for the specified tier or quantity range.                        	|
| `quantity` {==Long==}          	| The minimum quantity required to be eligible for the price or discount defined by the tier.            	|
