
# createQuoteFromCart

This mutation creates a quote request from a particular cart.

```
mutation ($command: CreateQuoteFromCartCommandType!){
  createQuoteFromCart(command: $command)
      {
    id
    number
    status
    comment
        items{
          productId
          name
          sku
           listPrice{
            amount
          }
          salePrice{
            amount
          }
          selectedTierPrice{
            quantity
            price{
              amount
            }
          }
      }
  }
}
```
