# Google Analytics Events

Google Analytics is used in the Virto Commerce Frontend Application to track user interactions and provide insights into user behavior. To make it easier for marketers, we have added several events that can be tracked by Google Analytics. This section details these events and how to implement them. You can track the results of these events in Google Tag Manager.

## Tracked Sales Funnel Events

After proceeding to checkout, the following events are tracked in the specified order.

| GA event         	    | Action (trigger)                                                                          | Checkout step                                                          	|
|-------------------	|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------------	|
| begin_checkout    	| Сlick **Proceed to checkout**.                                                           	|                                                                         	|
| add_shipping_info 	| Сlick **Proceed to billing** after specifying the shipping address and delivery method. 	| Shipping.                                                             	|
| add_payment_info  	| Сlick **Review order** after specifying the billing address and the payment method.       | Billing.                                                              	|
| place_order       	| Сlick **Place order** after reviewing the order.                                       	| Order review.                                                         	|
| purchase          	| Сlick **Pay now** after selecting the payment method.                                 	| Payment (unless manual payment was select at the previous step). 	        |

!!! note
    For a single-step checkout, only `begin-chekout` and `place_order` are tracked. Other events can be added at the client's request.

## Other Tracked Events

You can also track different search actions. For example, after you type a query into a search field, a dropdown list appears. Clicking **Enter**/ ![Magnifying glass](../media/magnifying-glass.png){: width="25"} / **View all results** triggers the **search**, **search_term**, **items_count**, **visible_items**, and **view_item_list** GA events:

![GA events](../media/google-analytics-events.png)


Other tracked actions are as follows:

| GA event                                              |Action (trigger)                                   | Result                                                | Location                                      |  
| ------------------------------------------------------|---------------------------------------------------|-------------------------------------------------------|-----------------------------------------------|
| view_item_list <br> item_list_name <br> items_skus	|Type query into the search field.                  | Dropdown list appears.                                | Catalog/Search field/ Related products/Lists  | 
| view_item                                             | Open product page.                                | Product page opens.                                   | Product page                                  | 
| select_item                                           |Go to Catalog --> select any item from it.         | Product page opens.                                   | Catalog                                       |
| view_cart                                             |Go to Catalog --> add products to cart --> open cart. | Cart with product opens.                           | Cart                                          | 
| add_to_cart                                           |Add products to cart.                              | Products are added to the cart.                       | Cart                                          | 
| remove_from_cart                                      |Remove item from cart.                             | Products are removed from cart.                       | Cart                                          | 
| clear_cart                                            |Click **Clear cart**.                              | The cart is empty.                                    | Cart                                          |
| add_to_wishlist                                       |Add product to wishlist.                           | The product is added to list.                         | Category page/ Product page                   |


