# promotionCoupons ==~query~==

This query allows you to retrieve promotion coupons.

## Arguments

| Argument                   	| Description              	                                                                                                  |
|----------------------------	|----------------------------------------------------------------------------------------------------------------------------	|
| `storeId`  ==String!==      	| The Id of the store.     	                                                                                                  |
| `after`  ==String==         | A cursor for pagination. Only edges after the specified cursor are returned.                                                 |
| `first`  ==Int==            | The maximum number of edges to return, starting after the cursor specified by `after`, <br> or the first number of edges if `after` is not specified. |
| `keyword`  ==String==       | A keyword to filter coupons by.                                                                                             |
| `sort`  ==String==          | The sorting order for the returned coupons.                                                                                 |
| `userId`  ==String==        | The Id of the user for whom the coupons are retrieved.                                                                      |
| `currencyCode`  ==String==  | The currency code used to filter or evaluate coupons.                                                                       |
| `cultureName`  ==String==  	| A language to retrieve data in.  	                                                                                          |

## Possible returns

| Possible return             	                | Description                                          	|
|----------------------------------------------	|-----------------------------------------------------	|
| [PromotionCouponConnection](../objects/PromotionCouponConnection.md) | A connection object containing the promotion coupons matching the specified criteria. |

## Example

<div class="grid" markdown>

```json title="Query"
{
  promotionCoupons(
    storeId: "B2B-store"
    first: 10
    keyword: "SUMMER"
    userId: "user123"
    currencyCode: "USD"
    cultureName: "en-US"
  ) {
    items {
      id
      code
    }
    totalCount
  }
}
```

```json title="Return"
{
  "data": {
    "promotionCoupons": {
      "items": [
        {
          "id": "3a7c19de-104f-4b62-bc21-57d3f98a1e4c",
          "code": "SUMMER20"
        }
      ],
      "totalCount": 1
    }
  }
}
```

</div>