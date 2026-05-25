# NewsArticleContentConnection ==~object~==

This type is used to represent a connection of news articles and provides metadata and pagination information for the retrieved articles.

## Fields

| Field                                                                | Description                                                                                                |
| ---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| `totalCount` ==Int==                                                 | The total count of news articles in the connection, ignoring pagination.                                   |
| `pageInfo` [ ==PageInfo!== ](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Catalog/objects/PageInfo)      | Information about the current page of news articles, used to manage pagination.                            |
| `edges` [ ==NewsArticleContentEdge== ](NewsArticleContentEdge.md)    | An array of edges representing the connection between news articles and cursor-based pagination details.   |
| `items` [ ==NewsArticleContent== ](NewsArticleContent.md)            | An array representing the actual news article objects retrieved in the connection.                         |

