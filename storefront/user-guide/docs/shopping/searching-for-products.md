# Search Options

The Frontend Application provides the following ways to find products:

* [Text-based search.](#text-based-search)
* [Barcode scanning.](#barcode-scanner)


## Text-based search

Enter keywords, SKU numbers, or other product attributes in the search bar. Use filters (facets) such as category, brand, price, and availability to refine results. 

For example, when searching for books, you can narrow your selection by author, course, or price. For additional precision, you can filter results based on product availability, indicated by the **Show in stock** checkbox. Search results can be sorted:

* Alphabetically.
* By price.
* By date.
    
![facet search](../media/faceted-search.png)

## Barcode scanner

A barcode scanner allows customers and sales representatives to quickly find products in the catalog using their mobile phones. Instead of manually searching, users can scan a product’s barcode with their phone’s camera to instantly open the product page.
The barcode scanner provides immediate access to product details, inventory levels, and pricing. This feature helps streamline inventory management, update product information, and speed up order fulfillment:

![Barcode scanner](../media/barcode-scanning.gif)

??? "Understanding barcodes"
    Barcodes are machine-readable symbols consisting of lines, spaces, characters, and digits. They are used to identify and track products throughout various stages of the supply chain. Common applications include inventory tracking in fulfillment centers, aiding accounting processes on invoices, and facilitating purchases in retail stores.

    Many industries and businesses integrate barcodes into their workflows due to their numerous advantages:

    * **Accurate inventory tracking**: Barcodes provide more reliable data than manual entry, helping track inventory, pricing, and product details such as expiration dates or weight. This ensures accurate stock levels and reduces errors in inventory management.

    * **Real-time data**: Barcode scanning provides instant access to product information, eliminating the need for manual data entry or retrieval. This allows businesses to quickly locate items in databases or online marketplaces.

    * **Ease of use**: Barcode scanners are simple to operate and require minimal training, making them an efficient tool in fulfillment centers and retail environments.

    * **Global acceptance**: Barcodes are widely used across industries and recognized worldwide, making them a universal tool for tracking and managing products in various business sectors.

    The most commonly used barcode types include:

    | **Barcode Type** | **Structure**  | **Capacity**              | **Usage** |
    |-----------------|--------------|----------------------|-------------------------------------------------------------|
    | **UPC-A**   | GTIN-12   | 12 digits            | Commonly used on retail products in North America. |
    | **UPC-E**   | GTIN-12   | 12 digits            | Suitable for small packages or retail products such as cosmetics, packs of chewing gum, and cigarettes in North America. |
    | **EAN-13**  | GTIN-13   | 13 digits            | Primarily used for retail products such as periodicals, magazines, and books outside of North America. |
    | **EAN-8**   | GTIN-8    | 8 digits             | Designed for small packages or retail products such as cosmetics, packs of chewing gum, and cigarettes outside of North America. |
    | **Code 39** | Non-GTIN  | 43 characters        | Commonly found in warehousing and industrial applications, including automotive and electronics. It supports letters and numbers. |
    | **Code 128**| Non-GTIN  | 48 characters        | Used in industries like warehousing, apparel, food processing, pharmaceuticals, and medical equipment. Code 128 offers the highest character density per inch and is 20-30% smaller than Code 39. It supports letters, numbers, special characters, and control codes. |
    | **ISBN**    | GTIN-13   | 13 digits (10 digits before January 2007) | Used to identify physical books and e-books globally. |





<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../products-purchase-options">← Company members</a>
    <a href="../back-in-stock-notifications">Back-in-stock notifications →</a>
</div>
