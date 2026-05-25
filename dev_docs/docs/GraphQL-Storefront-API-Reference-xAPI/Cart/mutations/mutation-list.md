# Mutation List

|# |Endpoint|Arguments|Description|
|--|-----------------------|---------------------|---------|
|1 |[addItem](#additem)|`!productId` `!quantity` `price` `comment`|Adds item to cart|
|2 |[clearCart](#clearcart)|-|Removes items from cart|
|3 |[changeComment](#changecomment)|`comment`|Updates cart comment|
|4 |[changeCartItemPrice](#changecartitemprice)|`!productId` `!price`|Changes cart item price|
|5 |[changeCartItemQuantity](#changecartitemquantity)|`!lineItemId` `!quantity`|Changes cart item quantity|
|6 |[changeCartItemComment](#changecartitemcomment)|`!lineItemId` `comment`|Changes cart item comment|
|7 |[removeCartItem](#removecartitem)|`!lineItemId`|Removes cart item from cart|
|8 |[addCoupon](#addcoupon)|`!couponCode`|Adds coupon to cart|
|9 |[removeCoupon](#removecoupon)|`couponCode`|Removes coupon from cart; if no specific coupon name is supplied, clears all coupons from cart|
|10|[removeShipment](#removeshipment)|`shipmentId`|Removes shipping method from cart|
|11|[addOrUpdateCartShipment](#addorupdatecartshipment)|`!shipment`([type](https://github.com/VirtoCommerce/vc-module-experience-api/blob/dev/src/XPurchase/VirtoCommerce.XPurchase/Schemas/InputShipmentType.cs))|Adds or updates shipping method for cart.|
|12|[addOrUpdateCartPayment](#addorupdatecartpayment)|`!payment`([type](https://github.com/VirtoCommerce/vc-module-experience-api/blob/dev/src/XPurchase/VirtoCommerce.XPurchase/Schemas/InputPaymentType.cs))|Adds or updates payment method for cart|
|13|[validateCoupon](#validatecoupon)|`!coupon`|Validates coupon and returns result|
|14|[mergeCart](#mergecart)|`!secondCartId`|Merges two carts into one|
|15|[removeCart](#removecart)|`!cartId`|Removes cart|
|16|[clearShipments](#clearshipments)|-|Clears cart shipping methods|
|17|[clearPayments](#clearpayments)|-|Clears cart payment methods|
|18|[updateCartDynamicProperties](#updatecartdynamicproperties)|`!dynamicProperties`|Updates dynamic properties within cart|
|19|[updateCartItemDynamicProperties](#updatecartitemdynamicproperties)|`!lineItemId` `!dynamicProperties`|Updates dynamic properties within cart items|
|20|[updateCartShipmentDynamicProperties](#updatecartshipmentdynamicproperties)|`!shipmentId` `!dynamicProperties`|Updates dynamic properties whitin cart shipping methods|
|21|[updateCartPaymentDynamicProperties](#updatecartpaymentdynamicproperties)|`!paymentId` `!dynamicProperties`|Updates dynamic properties within cart payment methods|
|22|[addCartAddress](#addcartaddress)|`!address`([type](https://github.com/VirtoCommerce/vc-module-experience-api/blob/dev/src/XPurchase/VirtoCommerce.XPurchase/Schemas/InputAddOrUpdateCartAddressType.cs))|Adds address for cart or updates it by type
|23|[addWishlistBulkItem](#addwishlistbulkitem)|`!listIds` `!productId`|Adds product to multiple wish lists|

!!! note
	The *Arguments* column lists only additional arguments; those marked with an exclamation mark are required.