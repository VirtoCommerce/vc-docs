# createOrderFromCart ==~mutation~==

This mutation creates an order from the cart with a specific Id.

## Arguments

The `InputCreateOrderFromCartType!` represents the input object for creating an order from a cart.

| Field                  | Description                                                |
|------------------------|----------------------------------------------------------  |
| `cartId` ==String==    | The Id of the cart from which the order will be created . |

## Possible returns

| Possible return                                          	| Description          	|
|---------------------------------------------------------	|----------------------	|
| [`CustomerOrderType`](../objects/customer-order-type.md)  |  A customer order.  	|




## Example

<div class="grid" markdown>

```json title="Mutation"
mutation createOrder($command: InputCreateOrderFromCartType!) {
  createOrderFromCart(command: $command) {
  id
  items
  {
    name
    id
    quantity
    product
    {
      availabilityData
      {
        isActive
        isInStock
        isBuyable
        isAvailable
        availableQuantity
      }
    }
  }
  customerId
  }
}
```

```json title="Variables"
{
  "command": {
    "cartId": "297056b4-df8e-4f78-aab7-40c048b42959"
  }
}
```

</div>