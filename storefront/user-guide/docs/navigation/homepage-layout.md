# Homepage Layout

The homepage can be visually divided into 3 parts:

* [Top menu.](homepage-layout.md#top-menu)
* [Catalogs, subcatalogs, and facets.](homepage-layout.md#catalogs-subcatalogs-facets)
* [Catalog items details.](homepage-layout.md#catalog-items-details)

![homepage](../media/navigation-homepage.png)

## Top menu

From the top menu, you can:

* Access your account profile.
* Select language and currency to display prices in.
* Search for products by their name or SKU, and more.
* Quickly access comparison and shopping lists.
* View the list of orders.
* Read notifications.
* Quickly navigate through the catalog via the mega menu. You can navigate the menu using keyboard arrow keys ([as of Frontend 2.29.0](https://github.com/VirtoCommerce/vc-frontend/releases/tag/2.29.0)). The mega menu can be hidden from anonymous users ([as of Frontend 2.29.0](https://github.com/VirtoCommerce/vc-frontend/releases/tag/2.29.0)).

![top menu](../media/top-menu.png)

![Readmore](../media/readmore.png){: width="25"} [Bulk orders](../shopping/bulk-orders.md)

![Readmore](../media/readmore.png){: width="25"} [Comparing products](../shopping/compare-products.md)

![Raedmore](../media/readmore.png){: width="25"} [Managing mega menu](../../../../platform/user-guide/content/managing-linklists#manage-mega-menu)



## Catalogs, subcatalogs, facets

From the left side menu, you can:

* Quickly navigate to the required subcatalog.
* Narrow down the number of items displayed by specifying the required product characteristics in the facets.

![Readmore](../media/readmore.png){: width="25"} [Search options](../shopping/searching-for-products.md)

## Catalog items details

In this area, you can:

* Switch between grid view and list view of the catalog items.
* Check the availability of the products in the selected branches.
* Sort products by price or name.
* View product details, etc.

![Catalog items details](../media/catalog-details.png)


Each product card displays:

* Product name and its basic characteristics.
* Its quantity in stock.
* Discounts applied, etc. 

![product card](../media/product-card.png)

!!! info
    By default, the **Add to cart** interface looks like this:
    
    ![Add to cart](../media/add-to-cart.png)

    A simplified **+ / −** interface is also available. If a product has a minimum purchase quantity, clicking the **+** button will add that quantity to the cart. Clicking the **-** button will remove that quantity from the cart. The cart updates instantly without unnecessary reloads:

    ![Plus-minus](../media/plus-minus.gif)

    The product cart and checkout interfaces will have the same design.  


## Keyboard navigation

You can use the keyboard to navigate through the store:

| Key                  | Description                                                                   |
|----------------------|-------------------------------------------------------------------------------|
| **Tab**              | Open a new line of navigation for quick access to the main content or footer. |
| **Tab** (repeatedly) | Move focus forward.                                                           |
| **Shift + Tab**      | Move focus backward.                                                          |
| **Enter**            | Activate buttons or open links.                                               |
| **Space**            | Select or deselect checkboxes and radio buttons.                              |
| **Esc**              | Close dropdowns and modals.                                                   |

![Tab navigation](../media/keyboard-interaction.gif)


## Mobile version

In the Frontend Application mobile version, the core principles and functionality remain consistent with the desktop version. Users may notice differences in the layout on their mobile devices, tailored to enhance usability and navigation on smaller screens.

### Homepage

![Mobile homepage](../media/storefront-mobile-homepage.png){: style="display: block; margin: 0 auto;" width="800"}

### Menu

![Catalog](../media/storefront-mobile-catalog.png){: style="display: block; margin: 0 auto;" width="500"}

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../registration_and_signing_in/create-account">← Registration and signing in</a>
    <a href="../product-page-layout">Product page layout →</a>
</div>