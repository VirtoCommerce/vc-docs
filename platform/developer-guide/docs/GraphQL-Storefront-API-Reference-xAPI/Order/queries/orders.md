# Orders ==~query~==

This query is used to retrieve a list of customer orders based on various criteria.​

## Arguments

| Argument                  | Description                                             |
|---------------------------|---------------------------------------------------------|
| `filter` ==String==       | Filters query results.                                  |
| `sort` ==String==         | The sorting order for the retrieved orders.             |
| `facet` ==String==        | Facets to apply to the query results, allowing for categorization or grouping based on specific attributes. |
| `cultureName` ==String==  | A language to retrieve data in.                         |
| `userId` ==String==       | The Id of the user.                                     |
| `after` ==String==        | A cursor value to paginate through the results.         |
| `first` ==Int==           | The number of pages in a single query.                  |


## Possible returns

| Possible return                                          	              | Description                           |
|-----------------------------------------------------------------------	|--------------------------------------	|
| [`CustomerOrderConnection`](../objects/customer-order-connection.md)    |  A connection of customer orders.   	|

## Example

<div class="grid" markdown>

```json title="Query"
query {
  orders {
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

```json title="Return"
{
  "data": {
    "orders": {
      "totalCount": 3,
      "items": [
        {
          "id": "order_id_1",
          "status": "Processing",
          "number": "ORD-20230702",
          "createdDate": "2023-07-02T10:15:30Z",
          "modifiedDate": "2023-07-02T11:45:25Z",
          "customerId": "customer_id_1",
          "customerName": "Alice Johnson",
          "shipments": [
            {
              "id": "shipment_id_1",
              "status": "Shipped",
              "shipmentMethodCode": "Standard",
              "shipmentMethodOption": "Express",
              "total": {
                "amount": 45.99
              }
            }
          ],
          "addresses": [
            {
              "id": "address_id_1",
              "firstName": "Alice",
              "lastName": "Johnson",
              "line1": "789 Oak Street",
              "countryName": "United States",
              "countryCode": "US",
              "postalCode": "56789"
            }
          ],
          "total": {
            "amount": 149.99
          },
          "subTotal": {
            "amount": 129.99
          },
          "discountTotal": {
            "amount": 20.00
          }
        },
        {
          "id": "order_id_2",
          // more items
        }
      ]
    }
  }
}
```

</div>