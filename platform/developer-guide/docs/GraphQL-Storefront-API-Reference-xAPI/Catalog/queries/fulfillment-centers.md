# FullfillmentCenters ==~query~==

This connection allows you to search for fulfillment centers.

## Argument

| Argument                          	    | Description                                                                                            	|
|----------------------------------------	|--------------------------------------------------------------------------------------------------------	|
| `after`  ==String==                    	| A cursor value to paginate through the results.                                                	        |
| `first`  ==Int==                       	| The number of pages in a single query.                                                       	          |
| `storeId`  ==String==                  	| The Id of the store to retrieve pages from.                                                  	          |
| `query`  ==String==                    	| Performs the full-text search.                                                                         	|
| `sort`  ==String==                    	| Specifies the sorting order of the returned products.                                                  	|
| `fullfillmentCentersIds`  ==String==  	| Identifies fulfillment centers. This argument is exclusive! If set, it overrides all other arguments. 	|

## Possible returns

| Possible return                                           	                    | Description                                                   	|
|-------------------------------------------------------------------------------	|---------------------------------------------------------------	|
| [`FulfillmentCenterConnection`](../objects/FulfillmentCenterConnection.md) 	    | A data type that describes a fulfillment center.              	|

## Examples

=== "Example 1"

    <div class="grid" markdown>

    ```json title="Query 1"
    {
      fulfillmentCenters(
        fulfillmentCenterIds: ["vendor-fulfillment", "los-angeles-fulfillment"]
      ) {
        totalCount
        items {
          id
          name
          shortDescription
          address {
            city
            countryCode
          }
        }
      }
    }
    ```

    ```json title="Return 1"
    {
      "data": {
        "fulfillmentCenters": {
          "totalCount": 1,
          "items": [
            {
              "id": "vendor-fulfillment",
              "name": "Los Angeles Branch",
              "shortDescription": null,
              "address": {
                "city": "Los Angeles",
                "countryCode": "USA"
              }
            }
          ]
        }
      }
    }
    ```

    </div>

=== "Example 2"

    <div class="grid" markdown>

    ```json title="Query 2"
    {
      products (storeId:"B2B-store")
      {
        items{
          name
          availabilityData
          {
            isActive
            inventories
            {
              fulfillmentCenterId
              fulfillmentCenterName
              inStockQuantity
            }
          }
        }
      }
    }
    ```

    ```json title="Return 2"
    {
      "data": {
        "products": {
          "items": [
            {
              "name": "1\" Steel Carriage Bolt, Grade 5, Chrome Plated Finish, 1/4\"-20 Dia/Thread Size, 5 PK",
              "availabilityData": {
                "isActive": true,
                "inventories": [
                  {
                    "fulfillmentCenterId": "tulsa-branch",
                    "fulfillmentCenterName": "Tennessee Branch",
                    "inStockQuantity": 10
                  },
                  {
                    "fulfillmentCenterId": "vendor-fulfillment",
                    "fulfillmentCenterName": "Los Angeles Branch",
                    "inStockQuantity": 10
                  }
                ]
              }
            },
            {
              "name": "Eyebolt, 1/2-13,3/8In",
              "availabilityData": {
                "isActive": true,
                "inventories": [
                  {
                    "fulfillmentCenterId": "vendor-fulfillment",
                    "fulfillmentCenterName": "Los Angeles Branch",
                    "inStockQuantity": 245
                  }
                ]
              }
            }
          ]
        }
      }
    }
    ```

    </div>