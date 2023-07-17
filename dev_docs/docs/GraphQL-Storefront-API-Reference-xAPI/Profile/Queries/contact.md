# Contact ==~query~==

This connection allows you to get the contact by its Id.

## Arguments

| Argument                           	| Description                                                                   	|
|------------------------------------	|--------------------------------------------------------------------------------	|
| `Id` {==String!==}        	        | The Id of the contact.                                                        	|
| `userId` {==String==}             	| The current user Id.                                                          	|


## Possible returns

| Possible return                                    	| Description                             	|
|---------------------------------------------------	|------------------------------------------	|
| [`Contact`](../Objects/ContactType.md)              | The contact's information and attributes.	|

## Examples

=== "Query"
    ```json linenums="1"
    {
      contact(id: "5f807280-bb1a-42b2-9a96-ed107269ea06") {
        id
        fullName
        memberType
        name
        organizationId
        emails
        organizations {
          name
        }
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
        "contact": {
          "id": "5f807280-bb1a-42b2-9a96-ed107269ea06",
          "fullName": "John Doe",
          "memberType": "Employee",
          "name": "John",
          "organizationId": "689a72757c754bef97cde51afc663430",
          "emails": [
            "john.doe@example.com",
            "johndoe@gmail.com"
          ],
          "organizations": [
            {
              "name": "Example Organization"
            }
          ],
          "addresses": [
            {
              "name": "Home",
              "addressType": "Physical",
              "isDefault": true
            },
            {
              "name": "Office",
              "addressType": "Physical",
              "isDefault": false
            }
          ],
          "defaultBillingAddress": {
            "name": "Home"
          },
          "defaultShippingAddress": {
            "name": "Home"
          }
        }
      }
    }
    ```
