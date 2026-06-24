# TierPriceType ==~object~==

This type represents the pricing information for a specific tier or quantity range of a product. 

## Fields

| Field                        	| Description                                                                                            	|
|------------------------------	|--------------------------------------------------------------------------------------------------------	|
| `price`  ==MoneyType==         	| The price of the item without any discounts or taxes applied for the specified tier or quantity range. 	|
| `priceWithTax`  ==MoneyType==  	| The price of the item including taxes for the specified tier or quantity range.                        	|
| `quantity`  ==Long==           	| The minimum quantity required to be eligible for the price or discount defined by the tier.            	|

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../PriceType">← PriceType</a>
    <a href="../CatalogDiscountType">CatalogDiscountType →</a>
</div>
