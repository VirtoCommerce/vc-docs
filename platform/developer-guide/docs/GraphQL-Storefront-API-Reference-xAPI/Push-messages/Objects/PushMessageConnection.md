# PushMessageConnection ==~object~==

The `PushMessageConnection` defines the structure of the response containing push messages.

## Fields

| Field                                                                   | Description                                            |
|-------------------------------------------------------------------------|--------------------------------------------------------|
| `totalCount` ==Int==                                                    | The total number of push messages.                     |
| `pageInfo` [==PageInfo!==](../../Catalog/objects/PageInfo.md)           | Information about pagination.                          |
| `edges` [==[PushMessageEdge]==](PushMessageEdge.md)                     | A list of edges, each containing a `PushMessageType`.  |
| `items` [==[PushMessageType!]!==](PushMessageType.md)                   | An array containing individual push messages.          |