# FulfillmentCenterEdge  ==~object~==

The `FulfillmentCenterEdge` type represents an edge that connects a fulfillment center to a connection. It contains fields that provide information about the cursor and the fulfillment center node. 

## Fields

|Field|Description|
|----------|-----------|
|`cursor` {==String!==}|A cursor that represents the position of the fulfillment center in the connection. It is a string value used for pagination and navigating through the list of fulfillment centers.|
|`node` [{==FulfillmentCenterType==}](FulfillmentCenterType.md)|The fulfillment center node associated with the edge. It represents the actual fulfillment center item and is of type `FulfillmentCenterType`.|
