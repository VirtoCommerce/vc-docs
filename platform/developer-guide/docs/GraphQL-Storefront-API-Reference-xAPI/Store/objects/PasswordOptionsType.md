# PasswordOptionsType ==~object~==

This type represents the configuration for password requirements in a store.

## Fields

| Field                                    | Description                                                 |
|------------------------------------------|-------------------------------------------------------------|
| `requiredLength` ==Int!==                | The minimum length required for passwords.                  |
| `requiredUniqueChars` ==Int!==           | The minimum number of unique characters required in a password. |
| `requireNonAlphanumeric` ==Boolean!==    | A boolean indicating whether non-alphanumeric characters are required. |
| `requireLowercase` ==Boolean!==          | A boolean indicating whether lowercase letters are required. |
| `requireUppercase` ==Boolean!==          | A boolean indicating whether uppercase letters are required. |
| `requireDigit` ==Boolean!==              | A boolean indicating whether digits are required.            |