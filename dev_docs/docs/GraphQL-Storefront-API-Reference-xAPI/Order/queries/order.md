## General Order Details

Get information about the order with the following queries:


* General order information:
  ```
  {
  order(
    number: 
    userId:
  )
  }
  ```
* Customer information:
  ```
  {
    id
    customerId
    customerName
    createdDate
    dynamicProperties { name value valueType }
    addresses {
      postalCode
    }
  }
  ```

* Order items information:
  ```
  {
    items {
      sku
      name
      quantity
    }
  }
  ```

* Currency:
  ```
  {
    currency {
    code
    }
  }
  ```

* Total amount:
  ```
  {
    total {
      amount
    }
  }

  ```
* Cancellation date:
  ```
  {
    cancelledDate
  }
  ```

<details>
<summary>Example</summary>

```
{
  "data": {
    "order": {
      "id": "9d27c868-2e31-4ab4-861b-909bc3f86657",
      "customerId": "0cda0396-43fe-4034-a20e-d0bab4c88c93",
      "customerName": "George Basker",
      "createdDate": "2021-01-06",
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
          "sku": "QRY-61202734",
          "name": "Dark Blue Floral Print Twist Cut Out Back Dress",
          "quantity": 1
        }
      ],
      "total": {
        "amount": 62.99
      },
      "cancelledDate": null
    }
  },
  "extensions": {}
}
```
</details>

</p>

> !!! tip
	The fields you can use in your requests are listed in the [OrderType chart](../objects/order-type.md).

