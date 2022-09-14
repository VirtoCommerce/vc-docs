# Orders Connection
With this connection, you can get all user orders.

```
{
  orders(
    after: "0"
    first: 10
    sort: "createdDate:desc"
    language: "en-US"
    userId: "0cda0396-43fe-4034-a20e-d0bab4c88c93"
  ) {
    totalCount
    items {
      id
      customerId
      customerName
      createdDate
      addresses {
        postalCode
      }
      currency {
        code
      }
      items {
        sku
        name
        quantity
      }
      total {
        amount
      }
      cancelledDate
    }
  }
}

```

<details>
<summary>Result (click to expand)</summary>

```
{
  "data": {
    "orders": {
      "totalCount": 3,
      "items": [
        {
          "id": "11a6d4a0-284f-46b1-8e17-add55983353f",
          "customerId": "0cda0396-43fe-4034-a20e-d0bab4c88c93",
          "customerName": "George Basker",
          "createdDate": "2019-01-06",
          "addresses": [
            {
              "postalCode": "77462"
            }
          ],
          "currency": {
            "code": "EUR"
          },
          "items": [
            {
              "sku": "PTO-38363811",
              "name": "Laced In Love White Floral Prom Dress",
              "quantity": 1
            },
            {
              "sku": "EIQ-20582301",
              "name": "Burgundy Baroque Lace Waist Dress",
              "quantity": 2
            },
            {
              "sku": "334713255",
              "name": "Wide Fit Lilac Ankle Strap Straw Wedges",
              "quantity": 1
            }
          ],
          "total": {
            "amount": 106.98
          },
          "cancelledDate": null
        }
      ]
    }
  },
  "extensions": {}
}
```
</details>

</p>