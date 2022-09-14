# Mutation List

|# |Endpoint|Arguments|Description|
|--|-----------------------|---------------------|---------|
|1 |[createOrderFromCart](#createOrderFromCart)|`!cartId`|Creates an order from an existing cart|
|2 |[changeOrderStatus](#changeOrderStatus)|`!orderId` `!status`|Changes order status|
|3 |[confirmOrderPayment](#confirmOrderPayment)|`payment { id sum caurrency …}`|Confirms order payment|
|4 |[cancelOrderPayment](#cancelOrderPayment)|`payment { id sum caurrency …}`|Cancels order payment|
|5 |[updateOrderDynamicProperties](#updateOrderDynamicProperties)|`!dynamicProperties`|Updates dynamic properties within an order|
|6 |[updateOrderItemDynamicProperties](#updateOrderItemDynamicProperties)|`!lineItemId` `!dynamicProperties`|Updates dynamic properties within order items|
|7 |[updateOrderShipmentDynamicProperties](#updateOrderShipmentDynamicProperties)|`!shipmentId` `!dynamicProperties`|Updates dynamic properties within order shipping methods|
|8 |[updateOrderPaymentDynamicProperties](#updateOrderPaymentDynamicProperties)|`!paymentId` `!dynamicProperties`|Updates dynamic properties within order payment methods|
|9 |[initializePayment](#initializePayment)|`orderId` `!paymentId`|Initiates payment processing
|10|[authorizePayment](#authorizePayment)|`orderId` `!paymentId` `parameters { key value }`|Finalizes the first step of payment processing
|11|[addOrUpdateOrderPayment](#addOrUpdateOrderPayment)|`!orderId` `!payment` ([type](https://github.com/VirtoCommerce/vc-module-experience-api/blob/dev/src/XPurchase/VirtoCommerce.ExperienceApiModule.XOrder/Schemas/InputOrderPaymentType.cs))|Adds or updates payment method for an order|

!!! note
	The *Arguments* column lists additional arguments; those marked with an exclamation mark are required.