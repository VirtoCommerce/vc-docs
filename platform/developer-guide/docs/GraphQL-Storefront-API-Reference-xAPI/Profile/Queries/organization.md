# Organization ==~query~==

This connection allows you to get the organization by its Id.

## Arguments

| Argument                           	| Description                                                                   	|
|------------------------------------	|--------------------------------------------------------------------------------	|
| `Id`  ==String!==         	        | The Id of the organization.                                                   	|
| `userId`  ==String==              	| The current user Id.                                                          	|

## Possible returns

| Possible return                                      	| Description                           	        |
|------------------------------------------------------	|-----------------------------------------------	|
| [`Organization`](../Objects/OrganizationType.md)     	| The organization's information and attributes.	|

## Example

<div class="grid" markdown>

```json title="Query"
{
  organization(id: "689a72757c754bef97cde51afc663430") {
    id
    name
    ownerId
    parentId
    businessCategory
    addresses {
      name
      addressType
      isDefault
    }
    defaultBillingAddress {
      name
    }
    defaultShippingAddress {
      name
    }
  }
}
```

```json title="Return"
{
  "data": {
    "organization": {
      "id": "689a72757c754bef97cde51afc663430",
      "name": "Example Organization",
      "ownerId": "123456789",
      "parentId": "987654321",
      "businessCategory": "Technology",
      "addresses": [
        {
          "name": "Headquarters",
          "addressType": "Physical",
          "isDefault": true
        },
        {
          "name": "Branch Office",
          "addressType": "Physical",
          "isDefault": false
        }
      ],
      "defaultBillingAddress": {
        "name": "Headquarters"
      },
      "defaultShippingAddress": {
        "name": "Headquarters"
      }
    }
  }
}
```

</div>