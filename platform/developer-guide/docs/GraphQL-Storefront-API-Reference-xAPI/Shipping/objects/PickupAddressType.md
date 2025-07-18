# PickupAddressType ==~object~==

This type represents the structured address details of a pickup location, including location, contact, and organization information.

## Fields

| Field                     | Description                                             |
| ------------------------- | ------------------------------------------------------- |
| `id` ==String!==          | The unique identifier of the address.                   |
| `key` ==String==          | An optional key to reference the address internally.    |
| `name` ==String==         | The name associated with the address (e.g., recipient). |
| `organization` ==String== | The company or organization name.                       |
| `countryCode` ==String==  | The ISO country code (e.g., US, DE).                |
| `countryName` ==String==  | The full name of the country.                           |
| `city` ==String==         | The city of the pickup location.                        |
| `postalCode` ==String==   | The postal or ZIP code.                                 |
| `line1` ==String==        | The first line of the street address.                   |
| `line2` ==String==        | The second line of the street address (optional).       |
| `regionId` ==String==     | The region or state identifier.                         |
| `regionName` ==String==   | The full name of the region or state.                   |
| `phone` ==String==        | The phone number associated with the address.           |
| `email` ==String==        | The email address associated with the address.          |
| `outerId` ==String==      | An external identifier, if available.                   |
| `description` ==String==  | Additional information or notes about the address.      |
| `addressType` ==Int==     | The type of address (e.g., billing, shipping, pickup).  |
