# Full Text Search

The `query` parameter performs the full text search against the product index document. It expects a full text search phrase.

## Searchable Fields

The search performs full text search over product data in the index. Product search returns all product variations a product has.
All searchable text data of a product are stored in the single `__content` field in the resulting index document; the full text search is performed only for this field.

An example of product document in the index may look like this:

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

The following product properties are stored in the `__content` field and are searched by default.

- `product.name`
- `product.code`
- `product.seoinfos.seoinfo.slug`
- `product.properties.value`
- `product.variations.code`
- `product.variations.properties.value`

Example requests:

```json
# Search all products by keyword `sony` and return the name and primary image URL for first 20 found products and total count
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