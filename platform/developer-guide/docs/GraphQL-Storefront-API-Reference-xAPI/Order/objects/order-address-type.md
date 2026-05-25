# OrderAddressType ==~object~==

This type represents an address associated with a customer order.

## Fields

| Field                     | Description                                                                   |
|---------------------------|-------------------------------------------------------------------------------|
| `id`  ==String==          | The Id of the order address.                                                  |
| `key`  ==String==         | A key or a code associated with the order address.                            |
| `city`  ==String==        | The city name for the order address.                                          |
| `countryCode`  ==String== | The ISO code of the country for the order address.                            |
| `countryName`  ==String== | The name of the country for the order address.                                |
| `email`  ==String==       | An email address associated with the order address.                           |
| `firstName`  ==String==   | First name of the recipient for the order address.                            |
| `middleName`  ==String==  | Middle name of the recipient for the order address.                           |
| `lastName`  ==String==    | Last name of the recipient for the order address.                             |
| `line1`  ==String==       | The primary street address line for the order address.                        |
| `line2`  ==String==       | A secondary street address line for the order address.                        |
| `name`  ==String==        | A name associated with the order address.                                     |
| `organization`  ==String== | An organization name associated with the order address.                      |
| `phone`  ==String==       | A phone number associated with the order address.                             |
| `postalCode`  ==String!== | The postal or ZIP code for the order address.                                 |
| `regionId`  ==String==    | The Id of the region or state for the order address.                          |
| `regionName`  ==String==  | The name of the region or state for the order address.                        |
| `zip`  ==String==         | An optional ZIP or postal code associated with the order address.             |
| `outerId`  ==String==     | An optional external identifier associated with the order address.            |
| `addressType`  ==Int==    | An integer representing the type of the order address.                        |

