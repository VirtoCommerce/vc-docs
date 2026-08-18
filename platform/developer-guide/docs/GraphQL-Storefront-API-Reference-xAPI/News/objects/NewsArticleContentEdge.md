# NewsArticleContentEdge ==~object~==

This type represents an edge in a connection from an object to another object of type **NewsArticleContent**. It provides both the article node and a pagination cursor.

## Fields

| Field                                                      | Description                                                                                         |
| ---------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `cursor` ==String!==                                       | A cursor string used for pagination. It identifies the position of this edge within the connection. |
| `node` [ ==NewsArticleContent== ](NewsArticleContent.md)   | The `NewsArticleContent` object that this edge refers to (the actual news article).                 |
