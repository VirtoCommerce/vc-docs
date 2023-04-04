
# changeQuoteComment

This mutation changes comment to the quote.

```
mutation changeQuoteComment($command: ChangeQuoteCommentCommandType!){
changeQuoteComment(command: $command){
  comment
  customerId
  customerName
  id
  number
  organizationId
  organizationName
  items{
    id
    productId
    product{
    name
    }
     }
  addresses{
    addressType
    postalCode
    city
    countryCode
    countryName
    regionName
    firstName
    lastName
  }
}
}
```
