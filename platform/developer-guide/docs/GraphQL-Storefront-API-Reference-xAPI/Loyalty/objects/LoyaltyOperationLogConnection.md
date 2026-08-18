# LoyaltyOperationLogConnection ==~object~==

This type defines a connection from an object to a list of loyalty program operation logs. It supports pagination, total counts, and convenient access to items.

## Fields

| Field                                                               | Description                                                                                                                               |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `totalCount` ==Int==                                                | The total number of log entries in the connection, ignoring pagination. Useful for displaying counts like “5 of 83.” If exact counts are unavailable (e.g., infinite scrolling), this field may return `null`. |
| `pageInfo` [ ==PageInfo!== ](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Catalog/objects/PageInfo)      | Information to assist with pagination, such as whether more results are available.                                                       |
| `edges` [ ==LoyaltyOperationLogEdge== ](LoyaltyOperationLogEdge.md) | A list of edges that include both the log entry (`node`) and its pagination cursor.                                                       |
| `items` [ ==LoyaltyOperationLog== ](LoyaltyOperationLog.md)         | A direct list of log entries. This is a shortcut to access items without edges, but should not be used if cursor data is required (e.g., with Relay). |
