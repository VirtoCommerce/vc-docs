# LoyaltyOperationLogEdge ==~object~==

This type represents an edge in a paginated connection for loyalty operation logs. It contains a cursor for pagination and the associated log entry.

## Fields

| Field                                                               | Description                                                        |
| ------------------------------------------------------------------- | ------------------------------------------------------------------ |
| `cursor` ==String!==                                                | A cursor used for pagination to fetch subsequent pages of results. |
| `node` [==LoyaltyOperationLog==](LoyaltyOperationLog.md)            | The loyalty operation log entry at the end of the edge.            |
