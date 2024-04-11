# organizationOrders ==~query~==

This query is used to view all orders from your organization. The user can view all the orders from the organization in the dashboard.​

## Arguments

| Argument                      | Description                                                     |
|-------------------------------|-----------------------------------------------------------------|
| `filter`  ==String==          | Refines the search results for organization orders.             |
| `sort`  ==String==            | Specifies the order of the results based on certain criteria.   |
| `cultureName`  ==String==     | A language to retrieve data in.                                 |
| `organizationId`  ==String!== | The Id of the organization for which the orders are retrieved.  |
| `after`  ==String==           | A cursor value to paginate through the results.                 |
| `first`  ==Int==              | The number of pages in a single query.                          |

## Possible returns

| Possible return                                          	                  | Description             	            |
|----------------------------------------------------------------------------	|-------------------------------------	|
| [`CustomerOrderConnection`](../objects/customer-order-connection.md)        |  A connection of customer orders.   	|

## Examples

=== "Query"

    ```json linenums="1"
    {
      organizationOrders(organizationId: "testidorg") {
        totalCount
        items {
          id
          status
          number
          createdDate
          modifiedDate
          customerId
          customerName
          shipments {
            id
            status
            shipmentMethodCode
            shipmentMethodOption
            total {
              amount
            }
          }
          addresses {
            id
            firstName
            lastName
            line1
            countryName
            countryCode
            postalCode
          }
          total {
            amount
          }
          subTotal {
            amount
          }
          discountTotal {
            amount
          }
        }
      }
    }
    ```


=== "Return"

    ```json linenums="1"
    {
      "data": {
        "organizationOrders": {
          "totalCount": 3,
          "items": [
            {
              "id": "order123",
              "status": "Pending",
              "number": "ORD12345",
              "createdDate": "2023-06-28T10:00:00Z",
              "modifiedDate": "2023-06-28T15:30:00Z",
              "customerId": "customer123",
              "customerName": "John Doe",
              "shipments": [
                {
                  "id": "shipment1",
                  "status": "Shipped",
                  "shipmentMethodCode": "standard",
                  "shipmentMethodOption": "2-day delivery",
                  "total": {
                    "amount": 25.99
                  }
                }
              ],
              "addresses": [
                {
                  "id": "address1",
                  "firstName": "John",
                  "lastName": "Doe",
                  "line1": "123 Main Street",
                  "countryName": "United States",
                  "countryCode": "US",
                  "postalCode": "12345"
                }
              ],
              "total": {
                "amount": 99.99
              },
              "subTotal": {
                "amount": 120.00
              },
              "discountTotal": {
                "amount": 20.01
              }
            }
          ]
        }
      }
    }
    ```