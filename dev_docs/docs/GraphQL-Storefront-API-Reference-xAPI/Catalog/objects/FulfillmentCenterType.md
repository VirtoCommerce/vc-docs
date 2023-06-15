# FulfillmentCenterType

The `FulfillmentCenterType` describes a fulfillment center. It provides information about various attributes of a fulfillment center. 

## Fields

|Field|Description|
|----------|-----------|
|`id` {==String==}|The unique identifier of the fulfillment center.|
|`name` {==String==}|The name of the fulfillment center.|
|`description` {==String==}|A detailed description of the fulfillment center.|
|`shortDescription` {==String==}|A brief description of the fulfillment center.|
|`geoLocation` {==String==}|The geographical location of the fulfillment center specified as latitude and longitude separated by a comma without spaces (e.g., "41.40338,12.17403").|
|`outerId` {==String==}|The external identifier of the fulfillment center.|
|`address` [{==FulfillmentCenterAddressType==}](FulfillmentCenterAddressType.md)|The address of the fulfillment center. |
|`nearest` {==FulfillmentCenterType==}|A list of the top 10 nearest fulfillment centers to the current one, ordered by the distance between their geo-coordinates. This property accepts an optional take argument (integer) to limit the selection. |