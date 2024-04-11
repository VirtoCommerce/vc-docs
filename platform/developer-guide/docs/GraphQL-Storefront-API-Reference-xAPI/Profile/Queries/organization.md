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

## Examples

=== "Query"
    ```json linenums="1"
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
=== "Return"
    ```json linenums="1"
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
