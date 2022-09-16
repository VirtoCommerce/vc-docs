# Filtering
The section below explains you how to manage the filtering process in the most frequently occuring scenarios.

## Filtering by Category

You can also filter products that belong to the exactly specified category path.

`filter: "category.path:{catalog id/category path}"`

`filter: "category.path:catalogId/cat1d1/cat2id"`

!!! note
	The search will be performed against the `__path` index field of the product document.

Filter by category subtrees, keep only the products that belong to the specified Category or any of its descendant categories.

`filter: "category.subtree:{catalog id/category path}"`

`filter: "category.subtree:catalogId/cat1d1/cat2id"`

!!! note
	The search will be performed against the `__outline` index field of the product document.


## Filtering by Price

This filter will include only the products, the price of which matches the specified value or range:

`filter: "price.{currency}.{pricelist?}:{range expression}"`

`filter: "price.usd:(TO 100]"`

`filter: "price.usd.pricelist_1:(20 TO 100]"`

Keep only products that  with at least one price set:

`filter: "is:priced`

!!! note
	The search will be performed against the `price_{currency}` and `price_{currency}_{pricelist}` index fields of the product document.

!!! note
	Only the indexed prices may be used for filtration. Scoped prices based on user groups or dynamic expressions temporary do not support filtration.

## Filtering by SKU

Use this filter to keep only the product that matches the specified SKU:

`filter: "sku:DLL-65789352`

## Filtering Products or Variations

This includes only either the products or variations in the result. If not set, it will return both types.

`filter: "is:product status:visible"`

`filter: "is:variation status:hidden"`

### Example

Displaying products and variations in a list from a specific category:

```json
query {
  products(
    storeId: "B2B-store"
    cultureName: "en-US"
    first:20
    after: "0"
   	filter:"status:hidden,visible category.path:7829d35f417e4dd98851f51322f32c23/4fbaca886f014767a52f3f38b9df648f"
  ) {
    items 
    {
      name
    }
    totalCount
  }}
```

## Filtering by Custom Properties

Keep only the products or variation with the custom attribute matching the specified value or range:

`filter: "properties.{property name}: {value}`

`filter: "properties.color:red`

To use property name contains spaces need to use the following syntax with escaped double quotes
`filter= "\"processor core (ghz)\":\"1.8 GHz Intel GTX Quad-Core\""`

For numeric and date time properties you might use range filter

`filter: "length:(10 TO 20)"`

`filter: "publishDate:(TO \"2020-01-28\")"`

!!! note
	All product custom properties are stored in the index as fields with the same names as the base properties have (`{property.name}:{property.value}`).

## Filtering by Product Availability

Keep only the products or variations with the availability matching the specified value or range:

`filter: "available_in:{warehouse}"`

`filter: "available_in:my-warehouse"`

## Sorting

By default, search results are sorted descending by their relevancy with respect to the provided text (that is their “score”). An alternative sorting can be specified  via the sort query parameter, which has the `{field}:{asc|desc}` structure. You can combine multiple sort expression using `;` (semicolon):

`sort: "priority:desc;price_usd;score"`