# FulfillmentCenterConnection  ==~object~==

The `FulfillmentCenterConnection` type represents a connection to a list of fulfillment centers.<br>It contains various fields to provide information about the connection, pagination, and the fulfillment center items themselves. 

## Fields

|Field|Description|
|----------|-----------|
|`totalCount` {==Int==}|The total count of fulfillment centers in the connection.|
|`pageInfo` [{==PageInfo!==}](PageInfo.md)|Information about the current page of fulfillment centers.|
|`edges` [{==FulfillmentCenterEdge==}](FulfillmentCenterEdge.md)|An array of edges that connect the fulfillment centers to the connection.<br>Each edge contains a cursor and the corresponding fulfillment center item.|
|`items` [{==FulfillmentCenterType==}](FulfillmentCenterType.md)|An array of fulfillment center items contained in the connection.|

