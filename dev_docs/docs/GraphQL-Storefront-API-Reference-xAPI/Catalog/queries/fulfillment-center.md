# FulfillmentCenter ==~query~==

This query allows you to get a fulfillment center by its Id.

## Argument

| Argument           	| Description                         	|
|--------------------	|-------------------------------------	|
| `id` {==String!==} 	| The Id of the fullfillment center. 	  |

## Possible returns

| Possible return                                	                    | Description                       	|
|--------------------------------------------------------------------	|------------------------------------	|
| [`FulfillmentCenterType`](../objects/FulfillmentCenterType.md) 	    | A type or category of properties.  	|

## Examples

=== "Query"
    ```json linenums="1"
    {
      fulfillmentCenter(
        id: "vendor-fulfillment"
      ) {
        id
        name
        description
        shortDescription
        outerId
        geoLocation
        address {
          city
        }
        nearest (take: 3) {
          name
          id
        }
      }
    }
    ```

=== "Return"
    ```json linenums="1"
      {
        "data": {
          "fulfillmentCenter": {
            "id": "vendor-fulfillment",
            "name": "Los Angeles Branch",
            "description": "<h3>Open 24/7</h3>,
            "shortDescription": null,
            "outerId": null,
            "geoLocation": null,
            "address": {
              "city": "Los Angeles"
            },
            "nearest": [
              {
                "name": "Chicago Branch",
                "id": "142ba5568ae4454aad553ece41b9c3b5"
              },
              {
                "name": "New York Branch",
                "id": "c20d27cdb09c4c7abd5d78a71510ab83"
              },
              {
                "name": "Tennessee Branch",
                "id": "tulsa-branch"
              }
            ]
          }
        }
      }    
    ```