# PageEdge ==~object~==

This type is utilized in combination with other types, such as `PageConnection`, to create paginated lists or connections of pages. It provides the necessary fields to identify and retrieve specific pages within the connection.

## Fields

| Field                               | Description                                |
|-------------------------------------|--------------------------------------------|
| `cursor` ==String==                 | The cursor associated with the page edge.  |
| `node` [==PageType==](PageType.md)  | The page node associated with the edge.    |

