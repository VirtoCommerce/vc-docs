# Properties

This connection allows you to search for catalog property metadata.

## Definition

```
properties(storeId: !string, types: [PropertyType], filter: string, cultureName: string)
```

## Arguments

|# |Name        |Type                     |Description                |
|--|------------|-------------------------|---------------------------|
| 1|storeId      |Non null StringGraphType |Store Id            |
| 2|types      |ListGraphType of PropertyTypeEnum's |The owner types (Catalog, Category, Product, Variation or combinations)            |
| 3|filter      |StringGraphType |This parameter applies a filter to the query results           |
| 4|cultureName      |StringGraphType |Culture name (e.g. "en-US")            |

## Example 1: Enlisting Property Metadata with Dictionary Items, Specified Culture, Specific Name and Types:

```json
{
  properties (storeId:"Electronics", cultureName:"de-DE", filter:"keyword:Brand", types:[PRODUCT, VARIATION])
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

## Example 2: Getting Properties for Specific Category:

```json
{
  properties (storeId:"Electronics", filter:"categoryId:53e239451c844442a3b2fe9aa82d95c8")
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