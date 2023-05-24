# Pages

| Endpoint 	| Arguments                                                                                       	| Return                                                                         	|
|----------	|-------------------------------------------------------------------------------------------------	|--------------------------------------------------------------------------------	|
| `pages`  	| `after`<br>`first`<br>`storeId`<br>`keyword`<br>`cultureName`	| List of pages from **Pages** and **Blogs** sections in the **Content** module. 	|


## Example

<hr />
=== "Query"

    The query is retrieving information about pages in the B2B-store that match the provided search parameters. It includes the total count of matching pages, information about each page such as its relative URL, name, and type, and pagination details.

    ```
    {
      pages(storeId: "B2B-store", keyword: "aliases:test", after: "0", first: 30) {
        totalCount
        items {
          relativeUrl
          name
          __typename
        }
        pageInfo {
          startCursor
          endCursor
          hasNextPage
          hasPreviousPage
        }
      }
    }
    ```

=== "Return"

    The return indicates that the query resulted in one matching page with a relative URL of `/testpagefrompage` and a name of `testpagefrompage`. The pagination information confirms that there is no next or previous page available.

    ```
    {
      "data": {
        "pages": {
          "totalCount": 1,
          "items": [
            {
              "relativeUrl": "/testpagefrompage",
              "name": "testpagefrompage",
              "__typename": "PageType"
            }
          ],
          "pageInfo": {
            "startCursor": "0",
            "endCursor": "1",
            "hasNextPage": false,
            "hasPreviousPage": false
          }
        }
      }
    }
    ```