# Fulfillment Centers

This connection allows you to search for fulfillment centers.

## Definition

```
fulfillmentCenters(after: String, first: Int, storeId: String, query: String, sort: String, fulfillmentCenterIds: [String])
```

## Arguments

|#|Name        |Type         |Description|
|--|-----------|-------------|-----------|
| 1|first |IntGraphType |Pagination size. Default is 20|
| 2|after |StringGraphType |Pagination cursor|
| 3|sort |StringGraphType |The sort expression|
| 4|storeId |StringGraphType |Search fulfillment centers by store ID|
| 5|query |StringGraphType |Search by fulfillment center name|
| 6|fulfillmentCenterIds |List of StringGraphType |Get fulfillment centers by provided IDs. Note: this argument is exclusive, if set it will override all other arguments|


## Example 1

Getting two fulfillment centers by known IDs:

```js
query {
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

## Example 2

Getting all fulfillment centers attached to B2B Store: 

```js
query {
  fulfillmentCenters(
    storeId: "B2B-store"
  )
   {
    totalCount
    items {
      id
      name
      outerId
      geoLocation
    }
  }
}
```