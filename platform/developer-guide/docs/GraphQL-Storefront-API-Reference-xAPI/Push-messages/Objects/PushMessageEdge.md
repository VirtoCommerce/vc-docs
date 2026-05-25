# PushMessageEdge ==~object~==

This type represents an edge in a connection that contains a cursor and a node.

## Fields

| Field                                                 | Description                                             |
|-------------------------------------------------------|---------------------------------------------------------|
| `cursor` ==String!==                                  | A Id for the edge, used for pagination.                 |
| `node` [==PushMessageType==](PushMessageType.md)      | The push message node associated with this edge.        |