# Configuration

This section explains the basic configuration for the security logic via the [appsettings.json file](../../Configuration-Reference/appsettingsjson.md#identityoptions).

![Readmore](media/readmore.png){: width="25"}  [Identity Configuration](https://github.com/dotnet/AspNetCore.Docs/blob/master/aspnetcore/security/authentication/identity-configuration.md#configure-aspnet-core-identity)

| Node                                      | Default or Sample Value   | Description                                                                                                            |
| ----------------------------------------- | ------------------------  | ---------------------------------------------------------------------------------------------------------------------- |
| Password                                  |                           | Configuration settings related to user password requirements.                                                          |
| Password:RequiredLength                   | `8`                       | The minimum required length for user passwords.                                                                        |
| Password:RequireDigit                     | `false`                   | Indicates whether a digit is required in user passwords.                                                               |
| Password:RequireNonAlphanumeric           | `false`                   | Indicates whether a non-alphanumeric character is required in user passwords.                                          |
| Password:RepeatedResetPasswordTimeLimit   | `"0:01:0"`                | The time span within which a user cannot repeatedly reset their password.                                              |
| User                                      |                           | Configuration settings related to user accounts.                                                                       |
| User:MaxPasswordAge                       | `90`                      | The maximum age (in days) a user can keep the same password before being required to change it.                        |
| User:RequireUniqueEmail                   | `true`                    | Indicates whether each user must have a unique email address.                                                          |
| User:RemindPasswordExpiryInDay            | `7`                       | The number of days before the password expiration date when the system will start reminding users to change their password. |
| Lockout                                   |                           | Configuration settings related to account lockout.                                                                      |
| Lockout:DefaultLockoutTimeSpan            | `"0:15:0"`                | The default duration for which an account is locked out after the specified number of unsuccessful login attempts.      |


**Example**

```json title="appsettings.json"
"IdentityOptions": {
    "Password": {
      "RequiredLength": 8,
      "RequireDigit": false,
      "RequireNonAlphanumeric": false,
      "RepeatedResetPasswordTimeLimit": "0:01:0"
    },
    "User": {
      "MaxPasswordAge": 90,
      "RequireUniqueEmail": true,
      "RemindPasswordExpiryInDay": 7
    },
    "Lockout": {
      "DefaultLockoutTimeSpan": "0:15:0"
    }
```
