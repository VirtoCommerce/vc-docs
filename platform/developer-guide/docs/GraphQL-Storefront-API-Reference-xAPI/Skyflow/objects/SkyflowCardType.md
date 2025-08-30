# SkyflowCardType ==~object~==

This type represents the details of a stored Skyflow card.

## Fields

| Field                       | Description                                                 |
| --------------------------- | ----------------------------------------------------------- |
| `cardExpiration` ==String== | The full expiration date of the card.                       |
| `cardNumber` ==String!==    | The card number (may be masked for security).               |
| `cardholderName` ==String== | The name of the cardholder.                                 |
| `cvv` ==String==            | The card verification value (CVV).                          |
| `expiryMonth` ==String==    | The expiration month of the card.                           |
| `expiryYear` ==String==     | The expiration year of the card.                            |
| `skyflowId` ==String!==     | The unique identifier of the card in Skyflow.               |
| `userId` ==String!==        | The Id of the user associated with the card.                |
| `active` ==Boolean!==       | Indicates whether the card is active and available for use. |
