# Products Management

The **Products** menu item includes:

- **Marketplace Products**: Products uploaded by all vendors in the marketplace. Use this section to [add your own offer to another vendor's products](#add-offer-to-another-vendors-product). 
- **My Products**: Products uploaded by the current vendor in their marketplace. Use this section to [add your own products](#add-own-product) and [offers](#add-offer-to-own-product) or [manage product associations](#manage-product-associations). 

A product can be associated with multiple offers, each of which provides a specific product variation, its price, and its inventory. Each offer can contain multiple price tags, reflecting various pricing strategies or conditions. In the example below,  the product ("Laptop Model A") is associated with different offers, each offer has multiple price tags:


| **Product**         | **Offer**                             | **Price tag**            | **Price**       | **Condition/Note**                |
|---------------------|---------------------------------------|--------------------------|-----------------|-----------------------------------|
|   Laptop Model A    |   8GB RAM, 256GB SSD                  | Standard Price           | $799.99         | Regular price                     |
|                     |                                       | Bulk Purchase Price      | $749.99         | When buying 5 or more             |
|                     |                                       | Holiday Sale Price       | $699.99         | Valid during holiday sale         |
|                     |   16GB RAM, 512GB SSD                 | Standard Price           | $999.99         | Regular price                     |
|                     |                                       | Loyalty Member Price     | $949.99         | For loyalty program members       |
|                     |                                       | Pre-Order Price          | $969.99         | Available for pre-orders only     |
|                     |   16GB RAM, 1TB SSD, Refurbished      | Standard Price           | $849.99         | Regular price for refurbished unit|
|                     |                                       | Clearance Price          | $799.99         | Clearance sale                    |
|                     |                                       | Flash Sale Price         | $749.99         | Limited-time offer                |

!!! note
    You can view products either as a list or organized by category:

    ![View products and categories](media/product-category-view.gif)


## Add offer to another vendor's product

If you want to add your own offer for a product listed by another vendor:

1. Click **Marketplace Products** in the main menu to open the list of all products in the marketplace.
1. In the next blade, click on the desired product to open its details.
1. In the next blade, click on the **Offers** widget.
1. In the next blade, click **Add** in the toolbar to add your own offer.

    ![Adding own offer](media/add-offer-to-another-vendors-product.gif)

1. In the next blade, fill in the required fields.
1. Click **Save** in the toolbar to save the changes.

Your offer has been added to the list of offers for the product. All vendor-created product offers are stored in the **Offers** section of the main menu, where they can be easily managed. Complete your offer by [adding price tags](#add-price-tags-to-offer). 

## Add own product 

To add your own product to the marketplace:

1. Click **My Products** in the main menu to open the list of your products.
1. In the next blade, click **Add** in the toolbar to add a new product.
1. In the next blade, enter all the descriptive data of the product, such as name, description, code, image(s), etc.

    !!! note
        A vendor can only upload products to the categories assigned by a marketplace operator. When a Vendor adds a product, it can only be assigned to one category from the list available to him.

    You can use the OpenAI and Grok AI providers to generate product descriptions based on product names and selected categories, and then translate those descriptions into the desired language:

    ![Product descriptions](media/ai-generated-content.gif)

    Product properties can be automatically generated using AI based on the product’s name and images:

    ![Product properties](media/product-properties-generation.gif)

    Product accent colors can be automatically assigned based on their entered English name using standard HTML color names. Users can still manually adjust the color code if needed:

    ![Color picker](media/color-picker-names.gif)

1. Click **Save as draft** in the toolbar to save the changes.

    ![Add own product](media/add-own-product.png)

1. Click **Submit for approval** to submit your product for approval by an Operator Portal manager. Only after the product has been approved and the offer for the product has been created it will be available for purchase by a customer.

![Readmore](media/readmore.png){: width="25"} [Product approval process](../Operator-portal/marketplace-products.md#approve-product)

Now you can add offer to your product.


### Add offer to own product

After your product has been approved by an Operator Portal manager it appears in the list of vendor's products with the **Is published** status. Now you can add your offers (variations) to the published product:

1. Click on the published product in the list of products.
1. In the next blade, click on the **Offers** widget. 
1. In the next blade, click **Add** in the toolbar to add your own offer.
1. In the next blade, fill in the required fields.
1. Click **Save** in the toolbar to save the changes.

    ![Add offer to own product](media/add-offer-to-own-product.gif)

Your offer has been added to the product. All vendor-created product offers are stored in the **Offers** section of the main menu, where they can be easily managed. Another way to add offers to your products is described [here](offers.md#add-offers-to-product). 

Complete your offer by [adding price tags](#add-price-tags-to-offer).

## Add price tags to offer

For various pricing strategies a vendor might set different price tags for a single product:

1. Select an offer from the offers list.
1. In the next blade, click on the **Price tags** widget.
1. In the next blade, fill in the required fields.

    !!! note
        The Vendor Portal supports multi-currencies pricing and volume-based pricing (configured through the [Store module](/platform/user-guide/latest/store/configuring-store)).

        ![Multi-currency pricing](media/multi-currency-pricing.png){: style="display: block; margin: 0 auto;" width="600"}

    ![Adding price tags](media/add-price-tags.gif)

1. Click **Confirm** in the toolbar, then **Save** to save the changes.

Your price tag has been added to the offer:

![Added price tags](media/price-tags-added.png){: style="display: block; margin: 0 auto;" width="700"}


## Manage product associations

To increase sales and improve product discovery, Vendors can manage product associations:

1. Click **My Products** in the main menu to open the list of your products.
1. In the next blade, select the desired product.
1. In the next blade, click on the **Associations** widget.
1. In the next blade, add associations to the product:

    ![Product associations](media/product-associations.gif)

The associations have been added.

## Communicate with Operator

When an Operator has a question about a Vendor's product, the Vendor will see it in the **Communication** widget:

![Communication widget](media/communication-widget.png){: style="display: block; margin: 0 auto;" }

Clicking on the widget, opens a communication blade, where the Vendor can send instant replies to the Operator:

![Communication blade](media/communication-blade.png){: style="display: block; margin: 0 auto;" width="550"}

All dialogs are stored in the **Communication** section of the main menu, where they can be easily managed.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../quotes">← Quotes</a>
    <a href="../products-management">Products management →</a>
</div>