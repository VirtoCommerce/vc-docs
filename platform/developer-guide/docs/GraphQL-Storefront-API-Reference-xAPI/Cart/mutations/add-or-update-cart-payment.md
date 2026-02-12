# addOrUpdateCartPayment ==~mutation~==

This mutation:

* Adds or updates cart payment. 
* Supports partial update, with all fields in `command.payment` and `command.payment.billingAddress` being optional.

## Arguments

The `InputAddOrUpdateCartPaymentType` represents the input object type used for adding or updating a payment for a cart.

| Field                               | Description                                                      |
|-------------------------------------|------------------------------------------------------------------|
| `cartId` ==String==                 | The Id of the cart to which the payment will be added or updated.   |
| `storeId` ==String!==               | The Id of the store associated with the cart.                       |
| `cartName` ==String==               | The name of the cart.                                              |
| `userId` ==String==                 | The Id of the user who owns the cart.                               |
| `currencyCode` ==String==           | The currency code for the cart.                                    |
| `cultureName` ==String==            | The culture or language associated with the cart.                   |
| `cartType` ==String==               | The type of the cart.                                              |
| `payment` ==InputPaymentType!==     | The payment details to be added or updated for the cart.           |

## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|











## Example

<div class="grid" markdown>

```json title="Mutation"
    mutation addOrUpdateCartPayment($command: InputAddOrUpdateCartPaymentType!) {
      addOrUpdateCartPayment(command: s$command) {
        id
        payments {
          id
          outerId
          paymentGatewayCode
          price {
            amount
          }
          amount {
            amount
          }
          billingAddress {
            id
            city
            countryCode
            countryName
            email
            firstName
            lastName
            line1
            line2
            middleName
            name
            organization
            phone
            postalCode
            regionId
            regionName
            zip
          }
        }
      }
    }
```

```json title="Variables"
    "command": {
      "cartId": "e6a7d5af-6378-44a6-b645-af9ecf702c05",
      "storeId": "B2B-Store",
      "cartName": "default",
      "userId": "c50e5237-8a4c-41fe-b878-8e5a72390a08",
        "currencyCode": "USD",
        "cultureName":"en-US",
      "cartType": "null",
      "payment": {
        "id": "paymentid_default_test_1",
        "outerId": "paymentouterud_default_test_1",
        "paymentGatewayCode": "DefaultManualPaymentMethod",
            "billingAddress": {
            "city": "City 17",
            "countryCode": "RU",
            "countryName": "Russia",
            "email": "addressCart email test",
            "firstName": "First test name",
            "id": "KeyTest",
            "key": "KeyTest",
            "lastName": "Last name test",
            "line1": "Address Line 1",
            "line2": "Address line 2",
            "middleName": "Test Middle Name",
            "name": "First name address",
            "organization": "OrganizationTestName",
            "phone": "88005553535",
            "postalCode": "111111",
            "regionId": "Test region",
            "regionName": "Region 15",
            "zip": "13413",
            "addressType": 1
            },
        "currency": "USD",
        "price": "1050",
        "amount": "1050"
      }
    }
```

</div>

