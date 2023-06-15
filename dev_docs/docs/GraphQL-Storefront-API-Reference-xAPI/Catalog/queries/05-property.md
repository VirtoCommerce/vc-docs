# Property

This connection allows you to get metadata for a specific catalog property.

<<<<<<< Updated upstream
## Definition

```
property(id: !string, cultureName: string)
```

## Arguments

|#|Name        |Type                     |Description                |
|--|------------|-------------------------|---------------------------|
| 1|id      |Non null StringGraphType |Property id            |
| 2|cultureName      |StringGraphType |Culture name (e.g. "en-US")            |

## Example

Getting a single property with dictionary items for a specific culture:

```json
{
  property (id:"43d14478-d142-4a65-956f-0a308d0c4ee8", cultureName:"de-DE")
  {
    propertyDictItems
=======
## Arguments

| Argument                   	| Description              	|
|----------------------------	|--------------------------	|
| `id` {==String!==}        	| Identifies the property. 	|
| `cultureName` {==String==} 	| Specifies the language.  	|

## Possible returns

| Possible return                                	| Description                       	|
|------------------------------------------------	|------------------------------------	|
| [`Property`](../objects/Property/Property.md) 	| A type or category of properties.  	|

## Examples
<hr />
=== "Query"
    ```json
>>>>>>> Stashed changes
    {
      items
      {
        value
      }
    }
<<<<<<< Updated upstream
  }
}
```
=======
    ```

=== "Return"
    ```json
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
>>>>>>> Stashed changes
