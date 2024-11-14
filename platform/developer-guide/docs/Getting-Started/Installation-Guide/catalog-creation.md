# Catalog Configuration

In this guide, we are going to configure catalog as follows: 

* Structure and fill catalog with products:
    * [Create categories and subcategories.](catalog-creation.md#create-categories-and-subcategories)
    * [Add products to our catalog.](catalog-creation.md#add-products)
    * [Add prices.](catalog-creation.md#add-prices)
    * [Add fulfillment centers.](catalog-creation.md#add-fulfillment-centers)

* Configure product properties and filtering facets:
    * Configure properties for [catalog](catalog-creation.md#configure-properties-for-catalog), [categories](catalog-creation.md#configure-properties-for-category), and [products.](catalog-creation.md#bulk-add-properties-to-products)
    * [Configure facets.](catalog-creation.md#configure-facets)


## Create categories and subcategories

Categories are containers for subcategories or products. In our example, we are going to create the following catalog structure:

<table border="1">
    <tr>
        <th>Catalog</th>
        <th>Category</th>
        <th>Subcategory</th>
        <th>Products</th>
    </tr>
    <tr>
        <td rowspan="12">Dental demo </td>
        <td rowspan="3">Anesthetics</td>
        <td>Anesthetic accessories</td>
        <td>1 product</td>
    </tr>
    <tr>
        <td>Anesthesia reversal</td>
        <td>1 product</td>
    </tr>
    <tr>
        <td>Anesthetic cartridges</td>
        <td>4 products</td>
    </tr>
    <tr>
        <td rowspan="3">Burs and diamonds</td>
        <td>Carbide burs</td>
        <td>8 products</td>
    </tr>
    <tr>
        <td>Diamond burs</td>
        <td>16 products</td>
    </tr>
    <tr>
        <td>Diamond disks</td>
        <td>2 products</td>
    </tr>
    <tr>
        <td rowspan="3">Crown and bridge materials</td>
        <td>Crown instruments</td>
        <td>4 products</td>
    </tr>
    <tr>
        <td>Polycarbonate crowns</td>
        <td>1 product</td>
    </tr>
    <tr>
        <td>Stainless steel crowns</td>
        <td>4 products</td>
    </tr>
    <tr>
        <td rowspan="3">Instruments</td>
        <td>Amalgam carriers</td>
        <td>4 products</td>
    </tr>
    <tr>
        <td>Carvers</td>
        <td>2 products</td>
    </tr>
    <tr>
        <td>Barnhart curettes</td>
        <td>4 products</td>
    </tr>
</table>


In the Platform, add a category to the master catalog as follows:

1. Select the newly created catalog.
1. In the next **Categories and items** blade, click **Add** in the toolbar.
1. In the **New category item** blade, select **Category**.
1. Enter the category name. The code is generated automatically.
1. Click **Create**.

    ![New Category](media/create-categories.png)

Your new category appears in the **Categories** list. Repeat these steps to add more categories.

To add a subcategory:

1. Select the newly created category.
1. In the next **Categories and items** blade, click **Add** in the toolbar.
1. In the **New category item** blade, select **Category**.
1. Enter the subcategory name. The code is generated automatically.
1. Click **Create**.

Your new subcategory appears in the list of subcategories inside the category. Repeat these steps to add more subcategories.

## Add products

!!! note
    There is an alternative way to quickly populate your catalog with products, prices, inventory, etc. using a csv file. You can learn more about this method in the [guide](add-products-via-csv.md). However, for first-time users who want to familiarize themselves with Virto Commerce products, the manual method of structuring and filling the catalog with products described below is sufficient.

To fill catalog with products:

1. Click on your catalog, select category and subcategory you want to add your product to. 
1. Click **Add** in the toolbar. 
1. In the next blade, select **Physical product**.
1. In the next blade, enter product name, (optionally) add image and description.
1. Click **Create**.

The product has been added to the selected category and subcategory of the catalog. Repeat these steps to add more products.

## Add prices

First, you need to create a pricelist:

1. Go to **Pricing** --> **Price lists**.
1. In the next blade, click **Add** in the toolbar.
1. In the next blade, fill in the fields as follows:

    ![Create price list](media/create-price-list.png)

1. Click **Create**.

To add prices to each product:

1. Go to **Catalog** --> Your catalog.
1. Click on a product from your catalog (in our example, Alpen FG surgical carbide burs).
1. In the next blade, click on the **Price** widget.
1. In the next blade, select your price list as a source price list, then click **Add new price**.
1. Enter list price, sale price (optionally), and minimum quantity (optionally).
1. Click **Save** in the toolbar.

![Adding prices](media/add-prices.png)

Repeat these steps to add more prices.

Now, we need to add a price list assignment:

1. Go to **Pricing** --> **Price list assignment**.
1. In the next blade, click **Add** in the toolbar.
1. In the next blade, fill in the fields as follows:

    ![Proce list assignment](media/add-price-list-assignment.png)

1. Click **Save** in the toolbar.

The prices have been configured. 

## Add fulfillment centers

By adding a fulfillment center you will be able to specify product quantities in stock: 

1. Click **Inventory** in the main menu.
1. In the next blade, click **Add** in the toolbar.
1. In the next blade, fill in the required fields. For trial purposes, you can only add fulfillment center name.
1. Click **Save** in the toolbar.

The fulfillment center has been added to the list. Repeat these steps to add more fulfillment centers.

## Specify quantities in stock

Now you need to add product stock in the fulfillment center.

1. Click on a product from your catalog (in our example, Alpen FG surgical carbide burs). 
1. In the next blade, click on the **Fulfillment centers** widget. 
1. In the next blade, you will see the list of all the available fulfillment centers. Click on a fulfillment center from the list.
1. In the next blade, fill in the necessary information. For the purpose of this guide, you can add only quantity in stock.
1. Click **Save** in the toolbar.

![Add FFC](media/add-ffc.png)

The specified stock appears next to the fulfillment center.

## Add semantic URL for your catalog

1. Open **Catalog**.
1. In the next blade, click on the three dots next to the name of your catalog.
1. Select **Manage** from the popup menu.
1. In the next blade, click on the **SEO** widget.
1. In the next blade, click **Add** in the toolbar.
1. In the next blade, fill in the fields as follows:

    ![Add slug URL](media/add-catalog-slug.png)

1. Click **OK**

The URL has been added for your catalog.

## View results on frontend

After completing the above steps, you have a simplified version of a fully functional store. To view the result on the frontend:

1. [Review search index](deploy-on-virto-cloud.md#review-search-index).
1. Refresh your store web page. In our example, https://dentalstoredemo.govirto.com/.

Now, your store catalog is filled with products and organized into categories and subcategories, as shown in the table above.

The **Catalog** button is now collapsible, displaying all categories and subcategories:

![Categories](media/catalog-categories-frontend.png)

Click on any category or subcategory to view the products within:

![Catalog](media/store-frontend.png)


## Configure properties

For enhanced product filtering and search, let's configure properties within our catalog. They allow customers to filter and search for products based on specific attributes. In the Frontend Application, they are displayed as filtering facets. In this guide, we are going to create the following properties displayed as facets:

![Facets](media/properties-configuration.png)

Properties can be set for:

* **Catalog**. The properties apply universally across multiple categories or to all products in the catalog. 
* **Category**. The properties apply to attributes specific to products within a particular category.
* **Product**. The properties are unique to individual items and not used frequently for filtering (e.g., a specific product model).
* **Variation**. The properties apply to different versions of a product, like color, or pack size.

In our example, we are going to add the following properties:

<table border="1" style="border-collapse: collapse; width: 100%;">
    <tr>
        <th>Level</th>
        <th>Property Type</th>
        <th>Properties</th>
    </tr>
    <!-- Catalog Level -->
    <tr>
        <td rowspan="4" style="border-right: none; border-bottom: none;">Catalog</td>
        <td>Catalog Properties</td>
        <td>-</td>
    </tr>
    <tr>
        <td>Category Properties</td>
        <td>-</td>
    </tr>
    <tr>
        <td>Product Properties</td>
        <td>Brand, Material, Size</td>
    </tr>
    <tr style="border-bottom: 2px solid black;">
        <td>Variation Properties</td>
        <td>-</td>
    </tr>
    <!-- Anesthetics Category Level -->
    <tr>
        <td rowspan="3" style="border-right: none; border-bottom: none;">Anesthetics category</td>
        <td>Category Properties</td>
        <td>-</td>
    </tr>
    <tr>
        <td>Product Properties</td>
        <td>Brand (inherited), Material (inherited), Size (inherited), Date of preparation, Physical state</td>
    </tr>
    <tr style="border-bottom: 2px solid black;">
        <td>Product Variation Properties</td>
        <td>-</td>
    </tr>
    <!-- Burs and Diamonds Category Level -->
    <tr>
        <td rowspan="3" style="border-right: none; border-bottom: none;">Burs and diamonds category</td>
        <td>Category Properties</td>
        <td>Shape</td>
    </tr>
    <tr>
        <td>Product Properties</td>
        <td>-</td>
    </tr>
    <tr style="border-bottom: 2px solid black;">
        <td>Variation Properties</td>
        <td>-</td>
    </tr>
    <!-- Crown and Bridge Materials Category Level -->
    <tr>
        <td rowspan="3" style="border-right: none; border-bottom: none;">Crown and bridge materials category</td>
        <td>Category Properties</td>
        <td>-</td>
    </tr>
    <tr>
        <td>Product Properties</td>
        <td>Length</td>
    </tr>
    <tr style="border-bottom: 2px solid black;">
        <td>Variation Properties</td>
        <td>-</td>
    </tr>
    <!-- Products Level -->
    <tr>
        <td rowspan="2" style="border-right: none;">Products</td>
        <td>Product Properties</td>
        <td>Brand (inherited), Material (inherited), Size (inherited), Date of preparation (inherited), Physical state (inherited)</td>
    </tr>
    <tr>
        <td>Variation Properties</td>
        <td>-</td>
    </tr>
</table>


### Configure properties for catalog

Let's add a **Brand** property at the catalog level:

1. Click **Catalog** in the main menu.
1. In the next blade, click on the three dots to the left of the required catalog and select **Manage** from the dropdown list.  
1. In the next blade, click on the **Properties** widget. 
1. In the next blade, click **Add property** in the toolbar.
1. In the next blade, select **Product property**.

    ![Add product property](media/add-property.png)

1. In the next blade, enter property name, switch the **Dictionary** option to on, and select **Short text**  [value type](catalog-creation.md#value-type-selection):

    ![Manage product property](media/manage-product-property.png)

1. Click **Save** in the toolbar.
1. Click **Dictionary**, then click **Add** in the next blade toolbar to add brand options:

    ![Manage dictionary](media/manage-dictionary.png)

    Click **Save** in the toolbar to add the dictionary entry to the list. Continue to add options as required:

    ![Dictionary items](media/dictionary-items.png)

The property appears in the list. On the frontend, the **Brand** facets becomes collapsible and the properties are displayed as follows:

![Brand on frontend](media/brand-property-on-frontend.png)

Continue to add properties and their values according to the table above.

![Catalog properties](media/catalog-properties-added.png)


#### Value type selection

When adding product properties, you can select the following value types from the dropdown list:

| **Value type**   | **Description**                                                | **Example**                                   |
|------------------|----------------------------------------------------------------|-----------------------------------------------|
| Short text       | Single-line text, ideal for short descriptive values.          | Brand: Alpen, Premier                         |
| Long text        | Multi-line text, suitable for longer descriptions or notes.    | Product description: “High-quality stainless steel instruments…” |
| Decimal number   | Numerical value with decimals, used for precise measurements.  | Length: 100 mm                                |
| Date time        | Date and time entry, useful for events or production dates.    | Date of production: 2024-11-01 10:00          |
| Boolean          | True/false value, suitable for binary attributes.              | Requires assembly: false                      |
| Integer          | Whole number, ideal for quantities or counts.                  | Pack size: 10                                 |
| Geo Point        | Geographical coordinates (latitude and longitude) for location-based data.| Store location: 40.7128° N, 74.0060° W  |

### Configure properties for category

Let's add a **Date of preparation** property to the **Anesthetics** category:

1. Click **Catalog** in the main menu.
1. In the next blade, select the required catalog.  
1. In the next blade, click on the three dots to the left of the required category and select **Manage** from the dropdown list.  
1. In the next blade, click on the **Properties** widget. 
1. In the next blade, click **Add property** in the toolbar.
1. In the next blade, select **Category property**.

    ![Add category property](media/add-category-property.png)

1. In the next blade, enter property name and select **Date time** value type from the dropdown list:

    ![Manage category property](media/manage-category-property.png)

1. Click **Save** in the toolbar.

The property appears in the list. Continue to add properties according to the table above.


### Add properties to products

Now, we will add properties to the products:

1. In your catalog, select the product you want to add properties to (**OraVerse** in our example).
1. In the product details blade, click on the **Properties** widget.
1. In the next blade, you fill in the properties you have added in the previous steps. From the dropdown lists, select the product's brand and its physical state. Enter date of preparation by clicking ![Calendar](media/calendar.png){: width="25"}:

    ![Adding properties to products](media/add-properties-to-product.png)

1. Click **OK** to save the changes.

The properties have been added to your product. Continue to add properties and their values to your products manually or use the instruction below to bulk add properties to products.

#### Bulk add properties to products

To add similar properties and property to a group of products:

1. Click **Catalog** in the main menu.
1. Select your catalog from the list of catalogs (**Dental Demo** in our example).
1. In the next blade, select the required category.
1. In the next blade, check (or bulk select) the products you want to add similar properties to.
1. Click **Bulk actions** in the toolbar.
1. In the next blade, click **Edit properties**.
1. In the next blade, click **Select properties**
1. In the next blade, add all or some previously added product properties.
1. Click **OK** to add the properties to the group of products.

    ![Bulk add properties](media/bulk-add-properties.png)

1. In the next blade, specify values for the selected properties, then click **OK**.

    ![Add property values](media/bulk-add-properties-to-product.png)

1. Click **Execute** in the previous blade.

The properties have been added to the selected products.

## Configure facets

To set the visibility of facets:

1. Go to **Stores** --> **Your store (Dental Demo Store)** --> **Aggregation properties** widget.
1. In the next blade, click on the properties in the left column (available properties) to move them to the right column (properties visible on the frontend):

    ![Facets visibility](media/facets-visibility.png)

1. Click **Save** in the toolbar to save the changes.

The selected facets are now displayed in the Frontend Application.


## View results on frontend

1. In the main menu, click **Stores**.
1. In the next blade, click on the required store (**Dental Demo Store** in our case).
1. In the next blade, click **Open in browser** in the top toolbar.

The properties are displayed as facets:

![Facets](media/facets-frontend-view.png)

The product properties are also displayed in the product cards:

![Product properties](media/product-properties.png)