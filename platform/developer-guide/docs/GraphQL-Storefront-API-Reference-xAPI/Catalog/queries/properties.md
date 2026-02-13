# Properties ==~query~==

This connection allows you to search for catalog property metadata.

## Arguments

| Argument                   	| Description                                                	|
|----------------------------	|------------------------------------------------------------	|
| `after`  ==String==       	| A cursor value to paginate through the results.           	|
| `first`  ==Int==           	| The number of pages in a single query.                    	|
| `storeId`  ==String!==     	| The ID of the store to retrieve pages from.   	            |
| `types`  ==PropertyType==  	| The type of property to retrieve.                          	|
| `filter`  ==String==       	| Filters query results.                                    	|
| `cultureName`  ==String==  	| A language to retrieve data in.                            	|

## Possible returns

| Possible return                                                       	| Description                                      	|
|-----------------------------------------------------------------------	|-------------------------------------------------	|
| [`PropertyConnection`](../objects/Property/PropertyConnection.md)       | An individual item within a property dictionary 	|


## Examples

=== "Example 1"

    <div class="grid" markdown>

    ```json title="Query 1"
    { 
      properties(
        storeId: "B2B-Store"
        cultureName: "en-EN"
        types: [PRODUCT, VARIATION]
      )  
        items {
          name
          type
          id
          multivalue
          propertyDictItems {
            totalCount
            items {
              value
            }
          }
        }
      }
    ```

    ```json title="Return 1"
    {
      "data": {
        "properties": {
          "items": [
            {
              "name": "date_prp",
              "type": "Product",
              "id": "2e412a78-e6fb-46d9-837e-e187512b7f62",
              "multivalue": false,
              "propertyDictItems": {
                "totalCount": 0,
                "items": []
              }
            },
            {
              "name": "variation_prop_date",
              "type": "Variation",
              "id": "0a1b9281-b567-40c5-b456-f3c5f420f5bd",
              "multivalue": false,
              "propertyDictItems": {
                "totalCount": 0,
                "items": []
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
      properties(
        storeId: "B2B-Store")
      {
        items {
          name
          type
          id
          multivalue
          propertyDictItems {
            totalCount
            items {
              value
            }
          }
        }
      }
    }
    ```

    ```json title="Return 2"
    {
      "data": {
        "properties": {
          "items": [
            {
              "name": "catalog_0_0_0",
              "type": "Catalog",
              "id": "2cdd23ca-f7cc-4496-a46b-2ab7063e86a5",
              "multivalue": false,
              "propertyDictItems": {
                "totalCount": 0,
                "items": []
              }
            },
            {
              "name": "propertycatalog_d",
              "type": "Catalog",
              "id": "bbe0d9f6-7ddd-417c-bb1d-c297044b2b57",
              "multivalue": true,
              "propertyDictItems": {
                "totalCount": 4,
                "items": [
                  {
                    "value": "qwertyq"
                  },
                  {
                    "value": "3"
                  },
                  {
                    "value": "2"
                  },
                  {
                    "value": "4"
                  }
                ]
              }
            },
            {
              "name": "variation_prop_date",
              "type": "Variation",
              "id": "0a1b9281-b567-40c5-b456-f3c5f420f5bd",
              "multivalue": false,
              "propertyDictItems": {
                "totalCount": 0,
                "items": []
              }
            }
          ]
        }
      }
    }
    ```

    </div>