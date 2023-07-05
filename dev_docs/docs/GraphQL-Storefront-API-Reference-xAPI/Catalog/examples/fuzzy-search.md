# Fuzzy search

Enabling the `fuzzy` query parameter allows the search to include products that have slight variations from the search text. For instance, if a user searches for **unversty**, the fuzzy search will also return products labeled as **university**.

You can optionally specify the fuzzy level using the `fuzzyLevel` parameter. If not specified, the search will automatically determine the fuzzy level based on the length of the searched text. The minimum fuzzy level is 3, and the maximum is 6.

=== "Sample query"
    Returns products that contain "university", "unversty", "universe", etc.
    ```json linenums="1"
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

=== "Sample return"
    ```json linenums="1"
    {
      "products": {
        "totalCount": 7,
        "items": [
          {
            "name": "University Notebook",
            "imgSrc": "https://example.com/images/university_notebook.jpg"
          },
          {
            "name": "Universe Explorer Telescope",
            "imgSrc": "https://example.com/images/universe_explorer_telescope.jpg"
          },
          // ... more product items
        ]
      }
    }
    ```