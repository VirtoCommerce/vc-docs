# FulfillmentCenterConnection  ==~object~==

The `FulfillmentCenterConnection` type represents a connection to a list of fulfillment centers. 

## Fields

|Field                                    |Description                         |
|-----------------------------------------|------------------------------------|
|`totalCount` {==Int==}                   |The total number of fulfillment centers in the connection.|
|`pageInfo` [{==PageInfo!==}](PageInfo.md)|Information about the current page of fulfillment centers.|
|`edges` [{==FulfillmentCenterEdge==}](FulfillmentCenterEdge.md)|A connection between fulfillment centers and a cursor associated with it.|
|`items` [{==FulfillmentCenterType==}](FulfillmentCenterType.md)|Fulfillment centers returned in the connection.|

