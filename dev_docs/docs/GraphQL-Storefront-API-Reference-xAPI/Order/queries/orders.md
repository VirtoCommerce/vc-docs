# Orders ==~query~==

This query is used to retrieve a list of customer orders based on various criteria.​

## Arguments

| Argument                  | Description                                             |
|---------------------------|---------------------------------------------------------|
| `filter` {==String==}     | Filters query results.                                  |
| `sort` {==String==}       | The sorting order for the retrieved orders.             |
| `cultureName` {==String==}| A language to retrieve data in.                         |
| `userId` {==String==}     | The Id of the user.                                     |
| `after` {==String==}      | A cursor value to paginate through the results.         |
| `first` {==Int==}         | The number of pages in a single query.                  |


## Possible returns

| Possible return                                          	              | Description                           |
|-----------------------------------------------------------------------	|--------------------------------------	|
| [`CustomerOrderConnection`](../objects/customer-order-connection.md)    |  A connection of customer orders.   	|

## Examples

=== "Query"

    ```json linenums="1"
    {
      order (id:"498a60ee-b73a-4235-a0d8-4f013a6b3201") {
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
    ```


=== "Return"

    ```json linenums="1"
    {
      "data": {
        "order": {
          "id": "498a60ee-b73a-4235-a0d8-4f013a6b3201",
          "status": "Processing",
          "number": "ORD-20230701",
          "createdDate": "2023-07-01T12:30:45Z",
          "modifiedDate": "2023-07-01T14:20:10Z",
          "customerId": "45d3f671-c2a1-45e1-9ab7-56fd98d28be9",
          "customerName": "John Doe",
          "shipments": [
            {
              "id": "7a98e3f4-5aee-4f08-9326-c93a701037a1",
              "status": "Shipped",
              "shipmentMethodCode": "Standard",
              "shipmentMethodOption": "Express",
              "total": {
                "amount": 55.99
              }
            }
          ],
          "addresses": [
            {
              "id": "7b60f3e8-498d-4e4f-9fc7-5ad05ab5ac64",
              "firstName": "John",
              "lastName": "Doe",
              "line1": "123 Main Street",
              "countryName": "United States",
              "countryCode": "US",
              "postalCode": "12345"
            },
            {
              "id": "e7e83c51-1c92-4dc8-a66e-7a9e0f8a9c88",
              "firstName": "Jane",
              "lastName": "Doe",
              "line1": "456 Elm Avenue",
              "countryName": "United States",
              "countryCode": "US",
              "postalCode": "67890"
            }
          ],
          "total": {
            "amount": 199.99
          },
          "subTotal": {
            "amount": 169.99
          },
          "discountTotal": {
            "amount": 20.00
          }
        }
      }
    }
    ```