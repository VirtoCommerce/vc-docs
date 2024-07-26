# AccountCreationResultType

This type represents the result of an account creation operation. 

## Fields

| Field                                                            | Description                                                                                       |
|------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| `succeeded`  ==Boolean!==                                        | Indicates whether the account creation operation succeeded (`true`) or failed (`false`).          |
| `errors` [ ==RegistrationErrorType== ](RegistrationErrorType.md) | An array of registration error types that capture any errors during the account creation process. |

