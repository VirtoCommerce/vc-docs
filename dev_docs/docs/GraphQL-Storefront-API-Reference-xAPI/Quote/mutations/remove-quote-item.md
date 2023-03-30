# removeQuoteItem

This mutation removes a product item from the quote request. 

```
mutation removeQuoteItem($command: RemoveQuoteItemCommandType!){
removeQuoteItem(command: $command){
  comment
  customerId
  customerName
  id
  number
  organizationId
  organizationName
  items{
    id
    sku
    productId
    product{
    name
    }
     }
  }
}
```
