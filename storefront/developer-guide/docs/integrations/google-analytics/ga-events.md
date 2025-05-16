# Google Analytics Events

Google Analytics is used in the Virto Commerce Frontend Application to track user interactions and provide insights into user behavior. To make it easier for marketers, we have added several events that can be tracked by Google Analytics. This section details these events and how to implement them. You can track the results of these events in Google Tag Manager.

## Tracked sales funnel events

After proceeding to checkout, the following events are tracked in the specified order.

| GA event         	    | Action (trigger)                                                                          | Checkout step                                                          	|
|-------------------	|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------------	|
| begin_checkout    	| Сlick **Proceed to checkout**.                                                           	|                                                                         	|
| add_shipping_info 	| Сlick **Proceed to billing** after specifying the shipping address and delivery method. 	| Shipping.                                                             	|
| add_payment_info  	| Сlick **Review order** after specifying the billing address and the payment method.       | Billing.                                                              	|
| place_order       	| Сlick **Place order** after reviewing the order.                                       	| Order review.                                                         	|
| purchase          	| Сlick **Pay now** after selecting the payment method.                                 	| Payment (unless manual payment was select at the previous step). 	        |

!!! note
    For a single-step checkout, only `begin-checkout` and `place_order` are tracked. Other events can be added at the client's request.

## Other tracked events

You can also track different search actions. For example, after you type a query into a search field, a dropdown list appears. Clicking **Enter**/ ![Magnifying glass](../media/magnifying-glass.png){: width="25"} / **View all results** triggers the **search**, **search_term**, **items_count**, **visible_items**, and **view_item_list** GA events:

![GA events](../media/google-analytics-events.png)


<table border="1" cellpadding="8" cellspacing="0">
  <thead>
    <tr>
      <th>GA event</th>
      <th>Action (trigger)</th>
      <th>Result</th>
      <th>Location</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="7">view_item_list</td>
      <td>Type query into the search bar.</td>
      <td>Dropdown list appears.</td>
      <td>Wherever search bar is present.</td>
    </tr>
    <tr>
      <td>Open product page → View related products (e.g. <b>Products related to this item</b>, <b>Customers bought together</b>).</td>
      <td>Related products widgets appear on product page.</td>
      <td>Related products widget on product page.</td>
    </tr>
    <tr>
      <td>Open product page → View variations.</td>
      <td>Product variations appear on product page.</td>
      <td>Product variations widget on product page.</td>
    </tr>
    <tr>
      <td>Open cart → View recently browsed products.</td>
      <td>Recently browsed products widget appears on cart page.</td>
      <td>Recently browsed products widget on cart page.</td>
    </tr>
    <tr>
      <td>Open product comparison page → View compared products.</td>
      <td>The list of products added for comparison appears on product comparison page.</td>
      <td>Product comparison page.</td>
    </tr>
    <tr>
      <td>Open catalog → View products in the catalog.</td>
      <td>The products from the catalog appear.</td>
      <td>Catalog.</td>
    </tr>
    <tr>
      <td>Open lists.</td>
      <td>The products lists appear.</td>
      <td>Lists.</td>
    </tr>
    <tr>
      <td>view_item</td>
      <td>Open product page.</td>
      <td>Product page opens.</td>
      <td>Product page.</td>
    </tr>
    <tr>
      <td rowspan="8">select_item</td>
      <td>Go to Catalog → Select any item from it</td>
      <td>Product page opens.</td>
      <td>Catalog</td>
    </tr>
    <tr>
      <td>Type query into the search bar → Select product from the dropdown</td>
      <td>Product page opens.</td>
      <td>Product page.</td>
    </tr>
    <tr>
      <td>Go to product page → Select item from the recommended products</td>
      <td>Product page opens.</td>
      <td>Recommended products widgets on product page.</td>
    </tr>
    <tr>
      <td>Go to product page → Select item from the related products.</td>
      <td>Product page opens.</td>
      <td>Related products widget on product page.</td>
    </tr>
    <tr>
      <td>Go to cart → Select item from the recently browsed products.</td>
      <td>Product page opens.</td>
      <td>Recently browsed products on cart page.</td>
    </tr>
    <tr>
      <td>Go to cart page → Select item from the products list.</td>
      <td>Product page opens.</td>
      <td>Product list on cart page.</td>
    </tr>
    <tr>
      <td>Go to lists → Select item from the list.</td>
      <td>Product page opens.</td>
      <td>Lists.</td>
    </tr>
    <tr>
      <td>Go to compare page → Select item from the compared products list.</td>
      <td>Product page opens.</td>
      <td>Product comparison page.</td>
    </tr>
    <tr>
      <td>view_cart</td>
      <td>Go to Catalog → Add products to cart → Open cart.</td>
      <td>Cart with product opens.</td>
      <td>Cart.</td>
    </tr>
    <tr>
      <td>add_to_cart</td>
      <td>Add products to cart.</td>
      <td>Products are added to the cart.</td>
      <td>Cart.</td>
    </tr>
    <tr>
      <td>remove_from_cart</td>
      <td>Remove item from cart.</td>
      <td>Products are removed from cart.</td>
      <td>Cart</td>
    </tr>
    <tr>
      <td>clear_cart</td>
      <td>Click <strong>Clear cart</strong>.</td>
      <td>The cart is empty.</td>
      <td>Cart</td>
    </tr>
    <tr>
      <td>add_to_wishlist</td>
      <td>Add product to wishlist.</td>
      <td>The product is added to list.</td>
      <td>Category page.<br>Product page.</td>
    </tr>
  </tbody>
</table>








<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../../authentication/authentication-types">← Authentication types </a>
    <a href="../../prerender_io/">Enhancing SEO with Prerender.io  →</a>
</div>