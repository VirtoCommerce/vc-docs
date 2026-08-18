# Full Text Search

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


<div class="grid" markdown>

```json title="Sample query"
query {
  products(
    query: "shirt",
    cultureName: "en-US"
  ) {
    items {
      id
      name
      ...
    }
  }
}
```

```json title="Sample return"
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
           // ... more product items
          ]
        }
      }
    }
```

</div>


!!! note
    The `cultureName` parameter is required for retrieving localized fields such as name, description, etc. If it is not passed, the request will return an error like **Cannot resolve field `name`**.