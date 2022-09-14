# FulfillmentCenterType

## Schema Fields

|#|Name|Type|Description|
|-|----------|----------|-----------|
|1|id|StringGraphType|Fulfillment center ID|
|2|name|StringGraphType|Fulfillment center name|
|4|description|StringGraphType|Full description of the fulfillment center|
|5|shortDescription|StringGraphType|Short description of the fulfillment center|
|6|geoLocation|StringGraphType|Fulfillment center geo location. Latitude and longitude are separated with a comma without spaces, e.g. "41.40338,12.17403"|
|9|outerId|StringGraphType|Fulfillment center outer ID|
|9|address|FulfillmentCenterAddressType|Fulfillment center address|
|9|nearest|List of FulfillmentCenterType|Contains the top 10 nearest fulfillment centers ordered by distance between geo-coordinates. Accepts the `take` (int) argument to limit the selection|