# Google Analytics Events

Google Analytics is used in the Virto Commerce Storefront to track user interactions and provide insights into user behavior. To make it easier for marketers, we have added several events that can be tracked by Google Analytics. This section details these events and how to implement them. You can track the results of these events in Google Tag Manager.

## Tracked Sales Funnel Events

After the buyer proceeds to checkout, the following events are tracked in the specified order.

| GA event         	    | Trigger                                                                                        	    | Checkout step                                                          	|
|-------------------	|-------------------------------------------------------------------------------------------------	    |-----------------------------------------------------------------------	|
| begin_checkout    	| The buyer clicks **Proceed to checkout**.                                                           	|                                                                         	|
| add_shipping_info 	| The buyer clicks **Proceed to billing** after specifying the shipping address and delivery method. 	| Shipping.                                                             	|
| add_payment_info  	| The buyer clicks **Review order** after specifying the billing address and the payment method.        | Billing.                                                              	|
| place_order       	| The buyer clicks **Place order** after reviewing the order.                                       	| Order review.                                                         	|
| purchase          	| The buyer clicks **Pay now** after selecting the payment method.                                 	    | Payment (unless manual payment was select at the previous step). 	        |

!!! note
    For a single-step checkout, only `begin-chekout` and `place_order` are tracked. Other events can be added at the client's request.

## Other Tracked Events

Other added event to be tracked by Google Analytics are as follows:

| GA event          | Trigger                                           	|
|------------------	|---------------------------------------------------	|
| search           	| A search query is performed.     	                    |
| view_item_list   	| A list of items is viewed. 	                        |
| select_item      	| An item is selected from a list of items.           	|
| view_item        	| A specific item is viewed.                          	|
| add_to_wishlist  	| An item is added to the wishlist.                   	|
| add_to_cart      	| An item is added to the shopping cart.              	|
| remove_from_cart 	| An item is removed from the shopping cart.          	|
| view_cart        	| A cart is viewed.                                 	|
| clear_cart       	| All items are removed from the shopping cart.       	|

