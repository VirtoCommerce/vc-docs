# Contact ==~query~==

This connection allows you to get the contact by its Id.

## Arguments

| Argument                           	| Description                                                                   	|
|------------------------------------	|--------------------------------------------------------------------------------	|
| `Id`  ==String!==         	        | The Id of the contact.                                                        	|
| `userId`  ==String==              	| The current user Id.                                                          	|


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
          totalCount
          pageInfo
          edges
          items
        }    
        addresses {
          totalCount
          pageInfo
          edges
          items
        }
        defaultBillingAddress {
          id
          key
          city
          countryName
        }
        defaultShippingAddress {
          id
          key
          city
          countryName
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
          "memberType": "Customer",
          "name": "johndoe",
          "organizationId": "123456",
          "emails": ["john.doe@example.com", "johndoe@gmail.com"],
          "organizations": {
            "totalCount": 2,
            "pageInfo": {
            "hasNextPage": false,
            "hasPreviousPage": false,
            "startCursor": null,
            "endCursor": null
            },
            "edges": [
              {
                "node": {
                "id": "org1",
                "key": "companyA",
                "city": "New York",
                "countryName": "United States"
                }
              },
              {
                "node": {
                "id": "org2",
                "key": "companyB",
                "city": "London",
                "countryName": "United Kingdom"
                }
              }
            ],
            "items": [
              {
                "id": "org1",
                "name": "Company A"
              },
              {
                "id": "org2",
                "name": "Company B"
              }
            ]
          },
          "addresses": {
            "totalCount": 2,
            "pageInfo": {
              "hasNextPage": false,
              "hasPreviousPage": false,
              "startCursor": null,
              "endCursor": null
            },
            "edges": [
              {
                "node": {
                  "id": "addr1",
                  "key": "home",
                  "city": "New York",
                  "countryName": "United States"
                }
              },
              {
                "node": {
                  "id": "addr2",
                  "key": "office",
                  "city": "San Francisco",
                  "countryName": "United States"
                }
              }
            ],
            "items": [
              {
                "id": "addr1",
                "name": "Home",
                "addressType": "Residential",
                "isDefault": true
              },
              {
                "id": "addr2",
                "name": "Office",
                "addressType": "Business",
                "isDefault": false
              }
            ]
          },
          "defaultBillingAddress": {
            "id": "addr1",
            "key": "home",
            "city": "New York",
            "countryName": "United States"
          },
          "defaultShippingAddress": {
            "id": "addr1",
            "key": "home",
            "city": "New York",
            "countryName": "United States"
          }
        }
      }
    }
    ```