# InputOrderBankCardInfoType ==~object~==

The `InputOrderBankCardInfoType` is a type that represents the input object for providing bank card information during a payment processing operation.

## Fields

| Field                             | Description                                                                                   |
|-----------------------------------|-----------------------------------------------------------------------------------------------|
| `bankCardNumber` {==String==}     | The full number of the bank card being used for the payment.                                  |
| `bankCardType` {==String==}       | The type or brand of the bank card.                                                           |
| `bankCardMonth` {==Int==}         | The expiration month of the bank card.                                                        |
| `bankCardYear` {==Int==}          | The expiration year of the bank card.                                                         |
| `bankCardCVV2` {==String==}       | The Card Verification Value 2 (CVV2) security code printed on the back of the bank card.      |
| `cardholderName` {==String==}     | The name of the cardholder as it appears on the bank card.                                    |
