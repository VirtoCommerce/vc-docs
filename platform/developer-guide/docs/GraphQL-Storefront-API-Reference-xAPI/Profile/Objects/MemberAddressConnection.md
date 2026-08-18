# MemberAddressConnection ==~object~==

This type represents a connection to a list of member addresses.

## Fields

| Field                                                             | Description                                                        |
|-------------------------------------------------------------------|--------------------------------------------------------------------|
| `totalCount`  ==Int==                                             | The total number of member addresses in the connection.            |
| `pageInfo` [ ==PageInfo!== ](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Catalog/objects/PageInfo)   | The information about the current page.                            |
| `edges` [ ==[MemberAddressEdge]== ](MemberAddressEdge.md)         | The edges containing the cursor and node of each member address.   |
| `items` [ ==[MemberAddressType]== ](MemberAddressType.md)         | The list of member addresses in the connection.                    |
