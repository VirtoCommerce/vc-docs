# Property

This connection allows you to get metadata for a specific catalog property.

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
    {
      items
      {
        value
      }
    }
  }
}
```