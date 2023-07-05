# CreateOrderFromCart

This mutation creates an order from the cart with a specific ID.

## Query

```
mutation {
  createOrderFromCart(
    command: { cartId: "05479fa6-9b6f-4028-94b1-cda21447e268" }
  )
  {
    id
    items {
      id
      sku
      name
    }
    total {
      amount
    }
  }
}
```