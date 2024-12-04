# Manage Sitemaps

Managing sitemaps includes:

* [Adding new sitemaps to stores](#add-new-sitemap-to-store)
* [Adding sitemaps items](#add-sitemap-items)
* [Downloading sitemaps](#download-sitemaps)
* [Exporting sitemaps to the store assets](#export-sitemaps-to-store-assets)

To manage the store sitemaps:

1. In the main menu, click **Stores**.
1. From the list of stores, click the store you need to manage sitemaps for.
1. In the next blade, click the **Sitemaps** widget. 
1. In the next **Sitemaps** blade, you will see a list of sitemaps to be included into the sitemap index file.

![Sitemaps screen](media/sitemaps-screen.png)

## Add new sitemap to store

To add a new sitemap: 

1. Click **Add** in the toolbar.
1. Fill in the following fields:

    ![New sitemap](media/new-sitemap.png)

1. Click **Create** to save the changes.

The example below involves three sitemap locations for different types of pages. The sitemap item locations are determined using language-culture slugs.

```xml linenums="1"
<sitemapindex xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap>
    <loc>https://sitemaps/en-US/sitemap/vendor.xml</loc>
  </sitemap>
  <sitemap>
    <loc>https://sitemaps/en-US/sitemap/catalog.xml</loc>
  </sitemap>
  <sitemap>
    <loc>https://sitemaps/en-US/sitemap/blog.xml</loc>
  </sitemap>
</sitemapindex>
```

## Add sitemap items

To add sitemap items:

1. Select a sitemap from the list.
1. In the next blade, click the  **Add items** in the toolbar.
1. Select the items to be added to the sitemap:

	![Item types](media/item-types.png)

1. Click **Save** to save the changes.

## Download sitemaps

After creating your sitemap, you can download a ZIP package containing your sitemap(s) in order to view what it includes:

1. Click **Download sitemaps** in the top toolbar.

1. In the new window, enter base URL for sitemaps and confirm your action.

The ZIP package you have downloaded contains the **sitemap.xml** file with the sitemap locations (see the example above) and the sitemap item XML files:

![Sitemap ZIP package folder structure](media/sitemap-folders.png)

Each sitemap item file includes the corresponding URL with a specific language culture:

```xml linenums="1"
<urlset xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://vcplatform-storefront.qa.govirto.com/en-US/</loc>
    <changefreq>weekly</changefreq>
    <priority>0.5</priority>
  </url>
</urlset>
```

## Export sitemaps to store assets

You can export sitemaps: 

* [Manually.](#manual-export)
* [Automatically via a scheduled job.](#automated-export)

### Manual export

To export sitemaps to store assets manually:

1. Click **Stores** in the main menu.
1. In the next blade, select your store.
1. In the next blade, click on the **Sitemaps** widget.
1. In the next blade, click **Export to store assets** in the toolbar.
1. Confirm your action.
1. Monitor the export progress in the next blade.
1. Once complete, click on the **Assets** widget in your store details blade to verify the sitemaps.

![Manual export](media/manual-export.gif)

You can see that the sitemaps have been added to the store assets. Now, you can download them or send links to them to other users.

### Automated export

Automated export simplifies the process by using a scheduled job. By default, it is disabled and requires activation at both the global and store levels:

1. Enable in the Store module:

    1. Click **Stores** in the main menu.
    1. In the next blade, select your store.
    1. In the next blade, click on the settings widget.
    1. In the next blade, find the "Export to assets" feature and enable it.
    1. Click **OK** to save the changes.

    ![Enable via stores](media/enable-via-stores.gif) 

1. Enable via the settings and configure export schedule:

    1. Click **Settings** in the main menu.
    1. In the next blade, type **Sitemaps** to find the settings related to the module.
    1. Click **Enable export sitemap files by job**.
    1. In the next blade, switch the **Export sitemap files by job** option to on.
    1. Set the cron expression to "0 0 * * *" to export sitemaps to store assets daily at 00:00.
    1. Click **Save** in the toolbar to save the changes.

  ![Enable sitemaps export](media/enable-sitemaps-export-in-settings.gif)

With automated export enabled, sitemaps will be regularly updated and saved to store assets, ensuring they're always up-to-date and accessible.