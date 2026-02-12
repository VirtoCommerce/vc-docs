# Fuzzy Search

Enabling the `fuzzy` query parameter allows the search to include products that have slight variations from the search text. For instance, if a user searches for **stel**, the fuzzy search will also return products labeled as **steel**.

You can optionally specify the fuzzy level using the `fuzzyLevel` parameter. If not specified, the search will automatically determine the fuzzy level based on the length of the searched text. The minimum fuzzy level is 3, and the maximum is 6.


<div class="grid" markdown>

```json title="Sample query"
{
  products(query: "stel" storeId: "B2B-Store" first:20, fuzzy: true) {
      totalCount
      items
      {
        name
        imgSrc
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
          "name": "1\" Steel Carriage Bolt, Grade 5, Zinc Plated Finish, 1/4\"-20 Dia/Thread Size, 100 PK",
          "imgSrc": "https://qademovc3.blob.core.windows.net/catalog/7829d/5ZMR1/5ZMR1.jpg"
        },
        {
          "name": "1\" Stainless Steel Carriage Bolt, 18-8, NL-19(SM) Finish, 1/4\"-20 Dia/Thread Size, 50 PK",
          "imgSrc": "https://qademovc3.blob.core.windows.net/catalog/7829d/53MF87/53MF87.jpg"
        },
        // ... more product items
      ]
    }
  }
}
```

</div>