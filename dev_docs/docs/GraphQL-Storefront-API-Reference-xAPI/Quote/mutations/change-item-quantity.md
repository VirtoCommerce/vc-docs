
# changeQuoteItemQuantity

This mutation changes the items quantity in the quote request.

```
mutation changeQuoteItemQuantity($command: ChangeQuoteItemQuantityCommandType!){
changeQuoteItemQuantity(command: $command){
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
