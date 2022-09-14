# Fulfillment Center

This query allows you to get a fulfillment center by its ID.

## Definition

```
fulfillmentCenter(id: !string)
```

## Arguments

|#|Name        |Type         |Description|
|--|-----------|-------------|-----------|
| 1|id |Non null StringGraphType |Fulfillment center id |


## Example
Getting a single fulfillment center with the top three nearest fulfillment centers:

```js
query {
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