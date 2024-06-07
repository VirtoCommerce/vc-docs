# StoreSettingsType ==~object~==

The `StoreSettingsType` represents the settings configuration for a store.

## Fields

| Field                                     | Description                                                                                       |
|-------------------------------------------|---------------------------------------------------------------------------------------------------|
| `quotesEnabled` ==Boolean!==              | A boolean indicating whether quotes are enabled for the store.                                    |
| `subscriptionEnabled` ==Boolean!==        | A boolean indicating whether subscriptions are enabled for the store.                             |
| `taxCalculationEnabled` ==Boolean!==      | A boolean indicating whether tax calculation is enabled for the store.                            |
| `anonymousUsersAllowed` ==Boolean!==      | A boolean indicating whether anonymous users are allowed in the store.                            |
| `isSpa` ==Boolean!==                      | A boolean indicating whether the store is a single-page application (SPA).                        |
| `emailVerificationEnabled` ==Boolean!==   | A boolean indicating whether email verification is enabled for the store.                         |
| `emailVerificationRequired` ==Boolean!==  | A boolean indicating whether email verification is required for the store.                        |
| `createAnonymousOrderEnabled` ==Boolean!== | A boolean indicating whether creating anonymous orders is enabled for the store.                 |
| `seoLinkType` ==String!==                 | The type of SEO link used for the store.                                                          |
| `defaultSelectedForCheckout` ==Boolean!== | A boolean indicating whether the store has the default selected option for checkout.              | 
| `environmentName` ==String!==             | The environment name in which the store is running.                                               |
| `passwordRequirements` [==PasswordOptionsType==](PasswordOptionsType.md)| The password requirements for user accounts in the store.           |
| `modules` [==[ModuleSettingsType!]==](ModuleSettingsType.md)| An array of settings for the store's modules.                                   |