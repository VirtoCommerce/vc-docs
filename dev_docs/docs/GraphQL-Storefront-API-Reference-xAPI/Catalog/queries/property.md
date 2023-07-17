# Property ==~query~==

This connection allows you to get metadata for a specific catalog property.

## Arguments

| Argument                   	| Description              	        |
|----------------------------	|---------------------------------	|
| `id` {==String!==}        	| The property Id.         	        |
| `cultureName` {==String==} 	| A language to retrieve data in.  	|

## Possible returns

| Possible return                                	| Description                       	|
|------------------------------------------------	|------------------------------------	|
| [`Property`](../objects/Property/Property.md) 	| A type or category of properties.  	|

## Examples

=== "Query"
    ```json linenums="1"
    {
      property (id:"43d14478-d142-4a65-956f-0a308d0c4ee8", cultureName:"de-DE")
      {
        propertyDictItems
        {
          items
          {
            value
          }
        }
      }
    }
    ```

=== "Return"
    ```json linenums="1"
    {
      "data": {
        "property": {
          "propertyDictItems": {
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
              }
            ]
          }
        }
      }
    }
    ```