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
    ```json linenums="1"
    {
      products(query: "bolt" storeId: "B2B-Store" first:10) {
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
          "totalCount": 7,
          "items": [
            {
              "name": "Eye Bolt,Carbon Steel 4.6,M6x70,PK25",
              "imgSrc": "https://qademovc3.blob.core.windows.net/catalog/7829d/38DJ66/5ZA21_AS01.jpg"
            },
            {
              "name": "20mm Steel Hex Flange Bolt, Class 10.9, Plain Finish, M10-1.50 Dia/Thread Size, 400 PK",
              "imgSrc": "https://qademovc3.blob.core.windows.net/catalog/7829d/157A20/41MY01.jpg"
            },
            {
              "name": "16mm Stainless Steel Carriage Bolt, A2, Plain Finish, M5-0.80 Dia/Thread Size, 100 PK",
              "imgSrc": "https://qademovc3.blob.core.windows.net/catalog/7829d/54FT59/164W33.jpg"
            },
            {
              "name": "2\" Alloy Steel Camrail Bolt, Grade 8, 3/4\"-10 Dia/Thread Size, 100 PK",
              "imgSrc": "https://qademovc3.blob.core.windows.net/catalog/7829d/19N083/19N102.jpg"
            },
            {
              "name": "16mm Steel Hex Flange Bolt, Class 8.8, Zinc Plated Finish, M8-1.25 Dia/Thread Size, 100 PK",
              "imgSrc": "https://qademovc3.blob.core.windows.net/catalog/7829d/DCJ-12823700/41MY01.jpg"
            },
            {
              "name": "2\" Steel Carriage Bolt, Grade 5, Plain Finish, 5/8-11 Dia/Thread Size, 25 PK",
              "imgSrc": "https://qademovc3.blob.core.windows.net/catalog/7829d/BBI-43450591/21A915.jpg"
            },
            {
              "name": "3-1/2\" Alloy Steel Camrail Bolt, Grade 8, 7/8\"-9 Dia/Thread Size, 5 PK",
              "imgSrc": "https://qademovc3.blob.core.windows.net/catalog/7829d/19N069/19N069.jpg"
            }
          ]
        }
      }
    }
    ```