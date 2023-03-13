# Evaluate dynamic content

This query allows you to evaluate dynamic content based on:

* Dynamic content place.
* Store.
* Product.
* Category.
* Tags.
* User groups.

## Definition

```
evaluateDynamicContent(
  storeId: String, 
  placeName: String, 
  categoryId: String, 
  productId: String, 
  cultureName: String, 
  toDate: DateTime, 
  tags: [String], 
  userGroups: [String])
)
```

## Arguments
|Name        |Type                       |Description                |
|------------|---------------            |---------------------------|
|storeId     |StringGraphType            |Store Id                   |
|placeName   |StringGraphType            |Dynamic content place name |
|categoryId  |StringGraphType            |Category Id                |
|productId   |StringGraphType            |Product Id                 |
|cultureName |StringGraphType            |Culture name (e.g. "en-US")|
|toDate      |StringGraphType            |Evaluation date            |
|tags        |List of StringGraphType    |List of tags               |
|userGroups  |List of StringGraphType    |List of user groups|

## Example

```json
{
  evaluateDynamicContent(
    storeId: "B2B-store"
    placeName: "MainSlider"
    tags: ["Main"]
    userGroups: ["Customers"]
    productId: "8b7b07c165924a879392f4f51a6f7ce0"
  ) {
    items {
      id
      name
      contentType
      dynamicProperties {
        name
        value
      }
    }
    totalCount
  }
}
```