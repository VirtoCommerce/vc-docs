# InputQuoteAddressType ==~object~==

The `InputQuoteAddressType`defines the format and fields used to provide input for updating or creating address information within a quote. 

## Fields

| Field                         | Description                                                       |
| ----------------------------- | ----------------------------------------------------------------- |
| `addressType`  ==Int==        | The type of address.                                              |
| `id`  ==String==              | The Id of the address.                                            |
| `key`  ==String==             | A key associated with the address.                                |
| `outerId`  ==String==         | An external Id associated with the address.                       |
| `name`  ==String==            | The name associated with the address.                             |
| `countryCode`  ==String==     | The country code of the address.                                  |
| `countryName`  ==String!==    | The name of the country for the address.                          |
| `postalCode`  ==String==      | The postal code or ZIP code associated with the address.          |
| `regionId`  ==String==        | The Id of the region or state for the address.                    |
| `regionName`  ==String==      | The name of the region or state for the address.                  |
| `city`  ==String!==           | The city associated with the address.                             |
| `line1`  ==String==           | The first line of the address.                                    |
| `line2`  ==String==           | The second line of the address.                                   |
| `email`  ==String==           | The email address associated with the address.                    |
| `phone`  ==String==           | The phone number associated with the address.                     |
| `firstName`  ==String!==      | The first name of the individual associated with the address.     |
| `lastName`  ==String!==       | The last name of the individual associated with the address.      |
| `organization`  ==String==    | The name of the organization associated with the address.         |
