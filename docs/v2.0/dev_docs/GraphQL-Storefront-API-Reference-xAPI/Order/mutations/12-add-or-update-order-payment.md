# AddOrUpdateOrderPayment

This mutation adds or updates payment details for the order. It supports partial update, with all fields in `command.payment` and `command.payment.billingAddress` being optional. If you provide `command.payment.id`, the existing payment will be updated.

## Query

```
mutation addOrUpdateOrderPayment($command: InputAddOrUpdateOrderPaymentType!) {
  addOrUpdateOrderPayment(command: $command) {
        id
        inPayments (first: 10, sort:"ModifiedDate:desc") {
          id
          createdDate
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
            addressType
          }
          paymentMethod {
            code
            paymentMethodType
            paymentMethodGroupType
          }
        }
      }
  }

```

## Variables

```
"command": {
    "orderId": "74d8b492-0bb5-486e-a0e6-0915848a7379",
    "payment": {
        "id": "New-Id-1",
        "paymentGatewayCode": "AuthorizeNetPaymentMethod",          
        "billingAddress": {
            "city": "Test",
            "countryCode": "US",
            "countryName": "US",
            "email": "address@mail.test",
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
            "addressType": 2
        }
    }
}
```