# Manage Categories

A category is basically a container for other categories, subcategories, or products.

Categories enable building hierarchies and links between various items in the catalog, which helps the customers navigate to the items they would like to purchase.

If you have large catalogs containing many items, you might want to create multiple categories and subcategories using the parent-child structure.

## Add new category

To add a new category to the catalog or a subcategory to a category:

1. Click **Catalog** in the main menu.
1. In the next **Manage catalogs** blade, select the required catalog.
1. In the next **Categories and Items** blade, click **Add** in the toolbar.
1. In the **New category item** blade, select **Category**.

    !!! tip
        In this step, you can copy the current URL and paste it into a new window to open the desired category immediately.  

1. Fill in the category name. The code is generated automatically.

    ![New Category Item](media/add-new-category-path.png){: style="display: block; margin: 0 auto;" }

1. Click **Create** to open the category details.
1. Fill in the category details. 

    ![New Category Item](media/new-category-blade.png){: style="display: block; margin: 0 auto;" }

1. Click **Save**. 

Your new category appears in the **Categories** list.

Let'a add the **Epson** subcategory to the **Printers** category of the **B2B** catalog:

<div>
  <script async src="https://js.storylane.io/js/v2/storylane.js"></script>
  <div class="sl-embed" style="position:relative;padding-bottom:calc(49.22% + 25px);width:100%;height:0;transform:scale(1)">
    <iframe loading="lazy" class="sl-demo" src="https://virtocommerce.storylane.io/demo/0xnucjskm5o2?embed=inline" name="sl-embed" allow="fullscreen" allowfullscreen style="position:absolute;top:0;left:0;width:100%!important;height:100%!important;border:1px solid rgba(63,95,172,0.35);box-shadow: 0px 0px 18px rgba(26, 19, 72, 0.15);border-radius:10px;box-sizing:border-box;"></iframe>
  </div>
</div>

### Tax type

!!! info
	You can add as many tax types as needed. 

To add a tax type:

1. In the **Category details blade**, click ![pencil](media/pencil.png){: width="20"} next to the **Tax type** field to open the **Tax types** blade.
1. Click **Add** in the toolbar.
1. Type the name of the tax type and click ![Save](media/save.png){: width="20"}. 
1. Click **Save** in the toolbar to save the changes.

Your new tax type is displayed in the **Tax type** dropdown list.

### Images

To add images to a category:

1. In the **Category details** blade, click the **Images** widget to open the **Manage Images** blade.
1. Click **Add** to open the **Upload Images** blade.
1. Fill in the fields.

    ![new image blade](media/new-image-blade.png){: style="display: block; margin: 0 auto;" }

1. Click **OK** to save the changes.

Your image(s) have been saved. 

### SEO 

To add a new SEO block:

1. In the **Category details** blade, click the **SEO** widget to open the **Manage SEO** blade.
1. Click **Add** to open the **SEO details** blade.
    
    ![New SEO](media/screen-add-new-seo.png){: style="display: block; margin: 0 auto;" }
 
1. Fill in the fields and click **OK**. 

Your new SEO block has been added to the SEO list.  

### Manual links

To link categories, subcategories, or products to the catalog items manually:

1. Select the category or subcategory you need to add a link to.
1. Click on the **Links** widget.
1. In the next blade, click **Add** in the toolbar.
1. In the next blade, select the desired items. You can not select the current category (if it is in the list), categories labelled as Marked, or category links within virtual catalogs.
1. Click **Map** in the toolbar to create the links.

The links have been created.

Let's add an **Epson printer** link to **Epson** category of the **B2B** catalog manually:

<div>
  <script async src="https://js.storylane.io/js/v2/storylane.js"></script>
  <div class="sl-embed" style="position:relative;padding-bottom:calc(49.22% + 25px);width:100%;height:0;transform:scale(1)">
    <iframe loading="lazy" class="sl-demo" src="https://virtocommerce.storylane.io/demo/ptkcucd6voyw?embed=inline" name="sl-embed" allow="fullscreen" allowfullscreen style="position:absolute;top:0;left:0;width:100%!important;height:100%!important;border:1px solid rgba(63,95,172,0.35);box-shadow: 0px 0px 18px rgba(26, 19, 72, 0.15);border-radius:10px;box-sizing:border-box;"></iframe>
  </div>
</div>

![Readmore](media/readmore.png){: width="25"} [Properties widget](managing-properties.md)

![Readmore](media/readmore.png){: width="25"} [User Groups widget](../catalog-personalization/user-groups.md)

### Automatic links

To link products to the catalog categories or subcategories automatically:

1. Select the category or subcategory you need to add a link to.
1. Click on the three dots to the left of the selected subcategory, then select **Manage** from the dropdown menu.
1. In the next blade, click on the **Automatic links** widget.
1. In the next blade:
    1. Select a catalog to add items from. 
    1. Define the desired items using the [query syntax expressions](../search-query-syntax.md).
1. Click **Preview** in the toolbar to see the list of automatically found items in the new blade.
1. Click **Create** to link the found items to the category or subcategory.

The links have been created.

Let's add automatic links to display all HP printers within the HP subcategory of the Printers category in the B2B catalog:

<div>
  <script async src="https://js.storylane.io/js/v2/storylane.js"></script>
  <div class="sl-embed" style="position:relative;padding-bottom:calc(49.22% + 25px);width:100%;height:0;transform:scale(1)">
    <iframe loading="lazy" class="sl-demo" src="https://virtocommerce.storylane.io/demo/nu7xyycbo4bd?embed=inline" name="sl-embed" allow="fullscreen" allowfullscreen style="position:absolute;top:0;left:0;width:100%!important;height:100%!important;border:1px solid rgba(63,95,172,0.35);box-shadow: 0px 0px 18px rgba(26, 19, 72, 0.15);border-radius:10px;box-sizing:border-box;"></iframe>
  </div>
</div>

![Readmore](media/readmore.png){: width="25"} [Properties widget](managing-properties.md)

![Readmore](media/readmore.png){: width="25"} [User Groups widget](../catalog-personalization/user-groups.md)


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../export-catalog">← Exporting catalogs</a>
    <a href="../managing-brands-page">Managing Brands page →</a>
</div>