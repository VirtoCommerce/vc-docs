# updateQuoteAddresses

This mutation updates a quote request address.


```
mutation updateQuoteAddresses($command: UpdateQuoteAddressesCommandType!){
updateQuoteAddresses(command: $command){
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
id
key
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
