# Import Shopify Taxonomy

The Shopify Taxonomy module imports attributes from the Shopify's Standard Product Taxonomy. These attributes are imported as properties into the Virto Commerce catalog and can be uses to define product characteristics. 

Attributes defined at multiple levels of the taxonomy hierarchy bubble up to the parent category. For example, if a category has an attribute **Color** and its subcategory has the same attribute, the parent category will keep the **Color** attribute and all subcategories will inherit it. 

If an attribute is defined across different root-level categories, it is promoted to the catalog level. For example, the **Pattern** attribute appears both under **Business & Industrial** and under the **Furniture** subcategory that are both level 0 categories. In this case, **Pattern** is created as a catalog-level property.

Learn how to create a new catalog in Virto Commerce and populate it with the Shopify taxonomy for further product management with the interactive demo:

<div>
  <script async src="https://js.storylane.io/js/v2/storylane.js"></script>
  <div class="sl-embed" style="position:relative;padding-bottom:calc(49.22% + 25px);width:100%;height:0;transform:scale(1)">
    <iframe loading="lazy" class="sl-demo" src="https://virtocommerce.storylane.io/demo/hjjkow0jmhuy?embed=inline" name="sl-embed" allow="fullscreen" allowfullscreen style="position:absolute;top:0;left:0;width:100%!important;height:100%!important;border:1px solid rgba(63,95,172,0.35);box-shadow: 0px 0px 18px rgba(26, 19, 72, 0.15);border-radius:10px;box-sizing:border-box;"></iframe>
  </div>
</div>

Now, you can import your products.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../overview">← Shopify Taxonomy module overview</a>
    <a href="../settings">Settings →</a>
</div>