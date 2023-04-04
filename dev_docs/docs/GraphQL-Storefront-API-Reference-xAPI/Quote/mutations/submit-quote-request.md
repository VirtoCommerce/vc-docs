# submitQuoteRequest

This mutation confirms and submits quotes request.

```
mutation submitQuoteRequest($command: SubmitQuoteCommandType!){
  submitQuoteRequest(command:$command){
    id
    status
    storeId
    customerId
    customerName
    comment
    number
        items{
      productId
      name
      sku
      product{
        id
        name
      }
      }
    addresses{
      countryCode
      countryName
      city
      regionName
      line1
      line2
      email
      firstName
      lastName
      phone
      postalCode
      organization
      addressType
    }
    totals{
      originalSubTotalExlTax{
        amount
      }
      subTotalExlTax{
        amount
      }
      shippingTotal{
        amount
      }
    }
  }
}
```
