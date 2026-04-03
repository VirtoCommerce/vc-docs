# PromotionCouponConnection ==~object~==

This type represents a connection from an object to a list of objects of type `PromotionCoupon`.

## Fields

| Field                            | Description                                                                                                                                               |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `totalCount`  ==Int==                                                                          | The total number of objects in this connection. |
| `pageInfo`  [==PageInfo!==](../../Catalog/objects/PageInfo.md)                                 | Information to aid in pagination.                                                    |
| `edges` [[ ==PromotionCouponEdge== ]](../objects/PromotionCouponEdge.md)                       | A list of all edges returned in the connection.                                      |
| `items` [[ ==PromotionCouponType== ]](../objects/PromotionCouponType.md)                       | A list of all objects returned in the connection. |