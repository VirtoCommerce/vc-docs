# PickupLocationAddressType ==~object~==

This type represents the detailed address and contact information for a pickup location.

## Fields

| Field                     | Description                                                   |
| ------------------------- | ------------------------------------------------------------- |
| `id` ==String!==          | The unique identifier of the address.                         |
| `key` ==String==          | A key associated with the address.                            |
| `name` ==String==         | The name of the address or location.                          |
| `organization` ==String== | The company or organization name associated with the address. |
| `countryCode` ==String==  | The ISO code of the country.                                  |
| `countryName` ==String==  | The full name of the country.                                 |
| `city` ==String==         | The city of the pickup location.                              |
| `postalCode` ==String==   | The postal or ZIP code.                                       |
| `line1` ==String==        | The first line of the street address.                         |
| `line2` ==String==        | The second line of the street address.                        |
| `regionId` ==String==     | The identifier of the region, state, or province.             |
| `regionName` ==String==   | The name of the region, state, or province.                   |
| `phone` ==String==        | A contact phone number for the address.                       |
| `email` ==String==        | A contact email address for the address.                      |
| `outerId` ==String==      | An external identifier for the address.                       |
| `description` ==String==  | A description or additional details about the address.        |
| `addressType` ==Int==     | A numeric code representing the type of address.              |
