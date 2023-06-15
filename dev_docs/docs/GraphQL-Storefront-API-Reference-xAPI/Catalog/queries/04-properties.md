# Properties ==~query~==

This connection allows you to search for catalog property metadata.

## Arguments

| Argument                 	| Description                                                	|
|--------------------------	|------------------------------------------------------------	|
| `after` {==String==}    	| Defines a cursor value to paginate through the results.    	|
| `first` {==Int==}          	| Indicates the number of pages in a single query.        	|
| `storeId` {==String!==}    	| Specifies the ID of the store to retrieve pages from.   	|
| `types` {==PropertyType==} 	| Specifies the type of property to retrieve.             	|
| `filter` {==String==}      	| Applies a filter to the query results.                  	|
| `cultureName` {==String==} 	| Specifies the language.                                 	|

## Possible returns

| Possible return                                                       	| Description                                      	|
|-----------------------------------------------------------------------	|-------------------------------------------------	|
| [`PropertyConnection`](../objects/Property/PropertyConnection.md)       | An individual item within a property dictionary 	|


## Examples
<hr />
=== "Query 1"
    ```json
    {
      properties (storeId:"Electronics", cultureName:"de-DE", 
      filter:"keyword:Brand", types:[PRODUCT, VARIATION])
      {
        items
        {
          name
          type
          id
          multivalue
          propertyDictItems
          {
            totalCount
            items
            {
              value
            }
          }
        }
      }
    }
    ```

=== "Return 1"
    ```json
    {
      "data": {
        "properties": {
          "items": [
            {
              "name": "Brand",
              "type": "Product",
              "id": "43d14478-d142-4a65-956f-0a308d0c4ee8",
              "multivalue": false,
              "propertyDictItems": {
                "totalCount": 21,
                "items": [
                  {
                    "value": "3DR"
                  },
                  {
                    "value": "Apple"
                  },
                  {
                    "value": "Asus"
                  },
                  {
                    "value": "Beats By Dr Dre"
                  },
                  {
                    "value": "BLU"
                  },
                  {
                    "value": "DJI"
                  }
                ]
              }
            }
          ]
        }
      }
    }
    ```
    
=== "Query 2"
    ```json
    {
      properties (storeId:"Electronics", 
      filter:"categoryId:53e239451c844442a3b2fe9aa82d95c8")
      {
        items
        {
          name
          type
          id
          multivalue
          propertyDictItems
          {
            totalCount
            items
            {
              value
            }
          }
        }
      }
    }
    ```

=== "Return 2"
    ```json
    {
      "data": {
        "properties": {
          "items": [
            {
              "name": "Camcorder_Type",
              "type": "Category",
              "id": "4af9a56f-fcf2-4a2d-b5bb-8b979ae38f9b",
              "multivalue": false,
              "propertyDictItems": {
                "totalCount": 0,
                "items": []
              }
            },
            {
              "name": "Features",
              "type": "Product",
              "id": "1b91897a-19d4-41d9-97db-9b3b2bd3637b",
              "multivalue": false,
              "propertyDictItems": {
                "totalCount": 4,
                "items": [
                  {
                    "value": "3D"
                  },
                  {
                    "value": "GPS"
                  },
                  {
                    "value": "Waterproof"
                  },
                  {
                    "value": "Wi-Fi"
                  }
                ]
              }
            }
          ]
        }
      }
    }
    ```  