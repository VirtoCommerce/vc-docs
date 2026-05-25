# BrandConnection ==~object~==

This type represents a connection to a list of brands.

## Fields

| Field                                   | Description                                                                                                                                                      |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `totalCount` ==Int==                    | A count of the total number of brands in the connection, ignoring pagination.<br>>Returns `null` when the total count is unavailable (e.g. with infinite scrolling). |
| `pageInfo` [==PageInfo!==](PageInfo.md) | Information about the current page of brands and pagination details.                                                                                             |
| `edges` [==BrandEdge==](BrandEdge.md)   | A connection between brands and a cursor associated with each one.                                                                                               |
| `items` [==BrandType==](BrandType.md)   | Brands returned in the connection. This shortcut can be used<br>instead of querying `edges { node }` when cursor information is not required.                       |
