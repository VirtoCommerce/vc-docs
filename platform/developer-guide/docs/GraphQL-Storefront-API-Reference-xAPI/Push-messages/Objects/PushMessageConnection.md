# PushMessageConnection ==~object~==

This type defines the structure of the response containing push messages.

## Fields

| Field                                                                   | Description                                            |
|-------------------------------------------------------------------------|--------------------------------------------------------|
| `totalCount` ==Int==                                                    | The total number of push messages.                     |
| `pageInfo` [==PageInfo!==](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Catalog/objects/PageInfo)           | Information about pagination.                          |
| `edges` [==[PushMessageEdge]==](PushMessageEdge.md)                     | A list of edges, each containing a `PushMessageType`.  |
| `items` [==[PushMessageType!]!==](PushMessageType.md)                   | An array containing individual push messages.          |