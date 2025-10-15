# Manage Brands Page

[On the frontend](https://virtostart-demo-store.govirto.com/brands), products from the catalog can be displayed on a dedicated page organized by brands in alphabetical order:

![Brands page on frontend](media/brands-page.png){: style="display: block; margin: 0 auto;" }

<br>
<br>
Creating such pages includes the following steps:

1. [Creating a catalog of brands.](#create-catalog-of-brands)
1. [Enabling brands page for the store.](#enable-brands-page-for-store)
1. [Adding brands to the catalog.](#add-brands-to-catalog)

## Create catalog of brands

Creating a catalog of brands is similar to [creating regular catalog](add-new-catalog.md#add-new-catalog):

1. Click **Catalog** in the main menu.
1. In the next blade, click **Add** in the toolbar.
1. In the next catalog, select the type of catalog you want to create: physical or virtual.
1. In the next blade, fill in the catalog name (**Brands** in our case):

    ![Creating brands page](media/creating-brands-page.png){: style="display: block; margin: 0 auto;" }

1. Click **Create**. 

The **Brands** catalog appears in the list.

## Enable brands page for store

To start displaying brands page on the frontend:

1. Click **Stores** in the main menu.
1. In the next blade, select a store to enable brand pages for.
1. In the next blade, click on the **Brand settings** widget.
1. In the next blade, configure the following:

    ![Brand settings configuration](media/enable-brands.png)

1. Click **Save** in the toolbar of the current and of the previous blades.

The brands page has been enabled for the store.


## Add brands to catalog

Adding brands to the newly created catalog is similar to [creating categories](managing-categories.md):

1. Open your newly created catalog.
1. In the next blade, click **Add** in the toolbar.
1. In the next blade, select **Category**.
1. In the next blade, fill in the category name. The code is generated automatically.

    ![Adding brands to catalog](media/adding-brand-to-catalog.png){: style="display: block; margin: 0 auto;" }

1. Click **Create** to open the brand details. In our example, we will:

    * Set the brand name (**A** in our case. This will appear at the top of the brands list and in the logos carousel).
    * Upload images (logo and banner).

        ![Filling in brand properties](media/filling-in-brand-properties.png){: style="display: block; margin: 0 auto;" }

    * Turn the **Featured** option to on in the **Properties** widget to include the brand logo among the top 12 with images:

        ![Featured option on](media/featured-option-on.png){: style="display: block; margin: 0 auto;" }

1. Click **OK** to save the changes, then click **Save** in the previous blade's toolbar.

The new brand appears on the frontend:

![New brand added](media/new-brand-added.png)

Clicking the brand opens a page displaying all products associated with that brand:

![A-brand products](media/a-brand-products.png)

## Multilingual SEO

As of [Catalog 3.895.0](https://github.com/VirtoCommerce/vc-module-catalog/releases/tag/3.895.0) and [xCatalog 3.938.0](https://github.com/VirtoCommerce/vc-module-x-catalog/releases/tag/3.938.0), admins can configure SEO settings for the Brands page separately for each language:

1. Click **Catalog** in the main menu.
1. In the next blade, click on the three dots to the left of the **Brands** catalog and select **Manage** from the dropdown menu.
1. In the next catalog, click on the **SEO** widget.
1. In the next blade, select the language to configure SEO for.
1. In the next blade, configure the following fields:

    ![Brands page SEO](media/brands-localized-seo.png){: style="display: block; margin: 0 auto;" }

    !!! note
        If SEO info for the selected language isn’t defined, the system automatically uses the default store language or another available version. 


1. Click **OK** to save the changes.

The configured SEO data is applied for accurate language-specific rendering.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../managing-categories">← Managing categories</a>
    <a href="../product-management-overview">Product management options →</a>
</div>