# updateQuoteAddresses ==~mutation~==

This mutation updates a quote request address.

## Fields

The `UpdateQuoteAddressesCommandType!` is a type that represents a command for updating quote request addresses. 

| Field                                                                             | Description                                                   |
|-----------------------------------------------------------------------------------|---------------------------------------------------------------|
| `quoteId` ==String!==                                                           | The Id of the quote to be updated.                            |
| `addresses` [==InputQuoteAddressType!==](../objects/InputQuoteAddressType.md)   | An array of updated address information for the quote request.|

## Possible returns

| Possible return                                     | Description          	          |
|-----------------------------------------------------|--------------------------------	|
| [`QuoteType`](../objects/QuoteType.md)           	  |  Information about the order.  	|


## Example

<div class="grid" markdown>

```json title="Mutation"
mutation UpdateQuoteAddresses($command: UpdateQuoteAddressesCommandType!) {
  updateQuoteAddresses(command: $command) {
    id
    addresses {
      name
      id
      countryCode
      addressType
      city
    }
  }
}
```

```json title="Variables"
{
  "command": {
    "quoteId": "quote-12345",
    "addresses": [
      {
        "id": "addr-001",
        "name": "Billing Address",
        "addressType": "Billing",
        "countryCode": "US",
        "city": "New York",
        "line1": "123 Main St",
        "line2": "Apt 4B",
        "postalCode": "10001",
        "region": "NY"
      },
      {
        "id": "addr-002",
        "name": "Shipping Address",
        "addressType": "Shipping",
        "countryCode": "US",
        "city": "Los Angeles",
        "line1": "456 Sunset Blvd",
        "line2": "",
        "postalCode": "90028",
        "region": "CA"
      }
    ]
  }
}
```

</div>