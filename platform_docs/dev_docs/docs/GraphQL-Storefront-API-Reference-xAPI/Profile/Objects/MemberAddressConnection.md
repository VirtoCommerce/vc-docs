# MemberAddressConnection ==~object~==

The `MemberAddressConnection` represents a connection to a list of member addresses.

## Fields

| Field                                                             | Description                                                        |
|-------------------------------------------------------------------|--------------------------------------------------------------------|
| `totalCount` {==Int==}                                            | The total number of member addresses in the connection.            |
| `pageInfo` [{==PageInfo!==}](../../Catalog/objects/PageInfo.md)   | The information about the current page.                            |
| `edges` [{==[MemberAddressEdge]==}](MemberAddressEdge.md)         | The edges containing the cursor and node of each member address.   |
| `items` [{==[MemberAddressType]==}](MemberAddressType.md)         | The list of member addresses in the connection.                    |
