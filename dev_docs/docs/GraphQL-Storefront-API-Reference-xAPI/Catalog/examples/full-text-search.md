# Full text search

The `query` parameter performs the full text search against the product index document. It expects a full text search phrase.

The search performs full text search over product data in the index. Product search returns all product variations a product has.
All searchable text data of a product are stored in the single `__content` field in the resulting index document. The full text search is performed only for this field.

??? "Product document example in the index"
    ```json
    "__content": [
      "JGC-85796278",
      "ASUS ZenFone 2 ZE551ML Gold",
      "asus",
      "android",
      "2.3 ghz intel gtx quad-core",
      "micro-sim",
      "1080"
    ],
    ```

The following product properties are stored in the `__content` field and are searched by default:

- `product.name`
- `product.code`
- `product.seoinfos.seoinfo.slug`
- `product.properties.value`
- `product.variations.code`
- `product.variations.properties.value`


=== "Sample query"
    Retrieves the names and primary image URLs of the first 20 products found and provides the total count when searching for products using the keyword "sony".
    ```json linenums="1"
    {
      products(query: "sony" storeId: "Electronics" first:20) {
          totalCount
          items
          {
            name
            imgSrc
          }
      }
    }
    ```

=== "Sample return"
    ```json linenums="1"
    {
      "data": {
        "products": {
          "totalCount": 5,
          "items": [
            {
              "name": "Sony W600B Series 47.6\" Full HD Smart LED TV",
              "imgSrc": "https://qademovc3.blob.core.windows.net/catalog/SOKDL48W600B/1390258056000_1023453.jpg"
            },
            {
              "name": "Sony FDR-AX100 4K Ultra HD Camcorder",
              "imgSrc": "https://qademovc3.blob.core.windows.net/catalog/SOFDRAX100/1389198276000_IMG_360504.jpg"
            },
            {
              "name": "Sony XBR-49X830C 49\"-Class 4K Smart LED TV",
              "imgSrc": "https://qademovc3.blob.core.windows.net/catalog/SOXBR49X830C/1424805855000_1120442.jpg"
            },
            {
              "name": "Sony BDV-E3100 3D Blu-ray Home Theater with Wi-Fi",
              "imgSrc": "https://qademovc3.blob.core.windows.net/catalog/SOBDVE3100/1365778134000_964998.jpg"
            },
            {
              "name": "Sony 32GB HDR-PJ540 Full HD Handycam Camcorder with Built-in Projector",
              "imgSrc": "https://qademovc3.blob.core.windows.net/catalog/SOHDRPJ540B/1434579141000_IMG_362938.jpg"
            }
          ]
        }
      }
    }
    ```