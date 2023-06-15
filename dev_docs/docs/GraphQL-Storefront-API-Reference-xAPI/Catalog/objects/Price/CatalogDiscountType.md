# CatalogDiscountType ==~object~==

The `CatalogDiscountType` represents a discount applied to a catalog or specific items within a catalog.

## Fields

| Field                              	| Description                                                                                  	|
|------------------------------------	|----------------------------------------------------------------------------------------------	|
| `coupon` {==String==}                	| The coupon code associated with the catalog discount.                                        	|
| `description` {==String==}           	| The description or details of the catalog discount.                                          	|
| `promotionId` {==String==}           	| The identifier of the promotion associated with the catalog discount.                        	|
| `amount` {==Decimal==}               	| The amount of discount applied to the item without taxes.                                    	|
| `moneyAmount` {==MoneyType==}        	| The amount of discount applied to the item without taxes, represented as a monetary value.   	|
| `amountWithTax` {==Decimal==}        	| The amount of discount applied to the item including taxes.                                  	|
| `moneyAmountWithTax` {==MoneyType==} 	| The amount of discount applied to the item including taxes, represented as a monetary value. 	|
| `promotion` {==Promotion==}          	| The promotion object associated with the catalog discount.                                   	|



[Read more about managing promotions](https://docs.virtocommerce.org/new/user_docs/marketing/managing-promotions/){ .md-button }