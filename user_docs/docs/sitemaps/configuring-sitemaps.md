# Configuring Sitemaps
In order to configure the store sitemaps, navigate to  _More > Stores_, select the store you need to manage sitemaps for, and click the  _Sitemaps_  widget. On the  _Sitemaps_  screen, you will see a list of sitemaps to be included into the sitemap index file:

![Sitemaps screen](media/sitemaps-screen.png)

## Adding New Sitemap to Store
In order to add a new sitemap, click the  _Add sitemap_  toolbar button. The  _New sitemap_  screen will show up. Each sitemap contains two required parameters:  _Sitemap location_  and  _Sitemap item location_, as well as a list of items to be included into the sitemap file:

![New sitemap](media/new-sitemap.png)

The _Sitemap location_ parameter means the relative URL, which will be defining the respective location (where the info for sitemaps will be taken from). You can add as many locations as needed, and all of them will be included into the sitemap xml file. The requirements to this parameter are the same as to the respective URL. The sitemap location value must end with the  `.xml`  extension. You cannot use  `sitemap.xml`  as a location, as this is the reserved file name for the sitemap index file. Some good examples may include  `products.xml`  or  `sitemap/vendors.xml`.
    
The _Sitemap item location_ is where the sitemap items are going to be placed. Since this parameter is a second part of the sitemap location, the requirements to its value are the same as to the respective URLs. The value of this option can be constructed with patterns (which will be replaced with language code of the relevant SEO info or with the default store language if the sitemap item has no SEO info, i.e., en-US, en-UK, etc.).

The example below has three sitemap locations referring to vendor, catalog, and blog pages, while the sitemap item locations are defined through the language-culture slug:

```xml
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

### Adding Sitemap Items
Adding sitemap items includes the following steps:

+ Select a sitemap from the list and click the  _Add items_  button located on the toolbar.
+ Provide sitemap items for the following types, as needed:

	![Item types](media/item-types.png)

	+ Catalog sitemap items may include both individual products and categories with subcategories and products. For each category and product, a different URL record for SEO sematic URL will be added to the relevant language.
	+ Vendor sitemap items: For each vendor, a different URL record for SEO sematic URL will be added in the relevant language.
	+ Custom sitemap items: If you want to include a custom URL in a sitemap, set its absolute URL here.
	+ Static content items: This type allows you to include static pages from your website to the sitemap, e.g., the About Us page, blog posts, and more.

+ Select the item and add it to the sitemap.
+ The selected item will be added to the  _Sitemap_  screen:

![Items added](media/items-added.png)
