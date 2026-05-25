# Promotion rules

Promotion rules, or conditions, define the behavior and effects of your promotions. Similar to the [publish conditions](publish-conditions.md) that you use to customize the display of your content, promotion rules allow you to customize your campaign to target specific customers, match different catalog and cart conditions, and offer specific rewards.
The following conditions can be configured:

| Condition 	| Description                                 											| Options                                                                                        |
|-----------	|---------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------	|
| Customers 	| Defines the customers the promotion is valid for. Provide at least one condition.   	| Registered users<br> Everyone<br> First time customers<br> User groups contains                                                                                                                                                                                                               |
| Catalog   	| Enables including/ excluding catalog-related conditions to the promotion.           	| Specific category<br> Product code contains...<br> Currency is...<br> Specific product<br> In stock quantity is...<br> Apply only to full price items and not sales items |
| Cart      	| Defines cart-related conditions for the promotion.<br> The additional operators allow you to build expressions as precisely as possible.<br> For example, you can configure the purchase amount to be exactly $100,<br>at least $100, or between $100 and $200. 	| Number of items in the shoppig cart<br> Number of items out of a category in the shopping cart<br> Number of specific product items in the shopping cart<br> Cart subtotal is...                                                                                                                                                                                |
| Rewards   	| Specifies the rewards your customers gets within your promotion campaign.<br> Add at least one reward to save the promotion. 	|  $... off cart subtotal...<br> % off cart subtotal, no more than $... <br> ... free items of ... product <br> $... off <br> $... off for ... specific product items... <br> % off for product ..., no more than $... <br> ...% off for ... specific product items, no more than $... <br> ... items of ... product as a gift <br> $... off for shipping at ... <br> % off for shipping at ..., no more than $... <br> $... off for using ... payment method <br> ...% off for using ... payment method, no more than $... <br> ...% off for ... of every ... specific product items <br> ...% off for ... items of a specific product per every ... items of another product 	|


## Example

The conditions below are configured as follows:

* Only registered users qualify for this promotion.
* This promotion **does not** apply to the **Cell Phones** category and **is not** valid unless there are more than five items in stock.
* This promotion is only valid with a minimum purchase of $200 **and** with at least two items in the shopping cart.
* The customers who qualify for this promotion will get 10% discount (not to exceed $50) when using a specific payment method **and** a gift (headphones).

![Promotion conditions example](media/promotion-rules/promotion-conditions-example.png)













