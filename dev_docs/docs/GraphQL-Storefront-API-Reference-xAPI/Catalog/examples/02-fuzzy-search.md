### Fuzzy Search

When the `fuzzy` query parameter is set to true, the search will also return products that contain slight differences to the search text.

For example, when someone searches for *unversty*, the fuzzy search would also return products labelled with *university*.

The fuzzy level can be optionally set with the `fuzzyLevel` parameter; otherwise, the search will use auto fuzzy level based on the length of the searched text, with the minimum value at 3, and maximum, at 6.

Example requests:

```json
# Will return products that contain "university", "unversty", "universe", etc.
{
  products(query: "unversty" storeId: "Electronics" first:20) {
      totalCount
      items
      {
        name
        imgSrc
      }
  }
}
```