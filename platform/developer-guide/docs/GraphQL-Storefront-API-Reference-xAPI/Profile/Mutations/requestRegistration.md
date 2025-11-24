# requestRegistration ==~mutation~==

This mutation registers:

* A company if all arguments have been provided.
* A customer only if the company value is null.

When a company is created, the customer becomes its member and owner. In this case, the customer is assigned the role of **Organization maintainer**, whose name or Id must be specified in [appsettings.json](/platform/developer-guide/latest/Configuration-Reference/appsettingsjson).

## Arguments

The `InputRequestRegistrationType!` represents the input object for requesting registration. It defines the fields required to initiate a registration process.

| Field                                                                                             | Description                                                                                                |
|---------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| `storeId`  ==String!==                                                                            | The Id of the store where the registration is being requested.                                             |
| `languageCode`  ==String==                                                                        | The language code used for localization during the registration process.                                   |
| `organization` [ ==InputRegisterOrganizationType== ](../Objects/InputRegisterOrganizationType.md) | The input object containing the details of the organization associated with the registration.              |
| `contact` [ ==InputRegisterContactType== ](../Objects/InputRegisterContactType.md)                | The input object containing the details of the contact person for the registration.                        |
| `account` [ ==InputRegisterAccountType== ](../Objects/InputRegisterAccountType.md)                | The input object containing the details of the user account to be created during the registration.         |

## Possible returns

| Possible return                                          	             | Description                                         	|
|------------------------------------------------------------------------|-----------------------------------------------------	|
| [`RequestRegistrationType`](../Objects/RequestRegistrationType.md)     | A registration request.                          	|


=== "Mutation"
    ```json linenums="1"
    mutation requestRegistration (command: InputRequestRegistrationType!) {
        registrationRequest(command: $command) {
            organization {
                id
                name
                status
                createdBy
                ownerId
            }
            contact {
                id
                name
                status
                createdBy
            }
            account {
                id
                username
                email
                status
            }
            result {
                succeede
                errors
            }
        }
    }
    ```

=== "Variables"
    ```json linenums="1"
    {
    "command": {
        "storeId": "store_id",
        "contact": {
        "firstName": "first_name",
        "lastName": "last_name",
        "phoneNumber": "phone_number"
        },
        "organization": {
        "name": "company_name"
        "description": "description"
        "address": {
            "city": "City"
            "countryCode":"USA"
            "countryName":"United States"
            "email":"e@mail.test"
            "firstName":"First_name"
            "lastName:"Last_name"
            "line1":"line1"
            "postalCode":"123654"
        }
        }
        "account": {
        "username": "user_name",
        "password": "password",
        "email": "e@mail.test" 
        }
    }
    }
    ```
