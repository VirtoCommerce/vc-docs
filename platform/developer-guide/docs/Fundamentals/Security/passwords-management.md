# Passwords Management

Virto Commerce uses **ASP.NET Core Identity** for user authentication and password management. All key password-related settings can be configured in the `IdentityOptions` section of your **appsettings.json** file. This allows you to define password strength, expiration rules, lockout behavior, and other security requirements.

This guide explains what each configuration option means and how to adjust it for your security needs.

## Adjust password strength requirements

The `Password` node controls what a user’s password must contain.

| Setting                                     | Meaning                                                                       |
| ------------------------------------------- | ----------------------------------------------------------------------------- |
| **Password:RequiredLength**                 | Sets the minimum number of characters a password must contain.                |
| **Password:RequireDigit**                   | When set to `true`, the password must include at least one number (0–9).      |
| **Password:RequireNonAlphanumeric**         | When `true`, requires characters like `!@#%` etc.                             |
| **Password:RepeatedResetPasswordTimeLimit** | Controls how soon a user can reset their password again after a recent reset. |


If you want stricter rules, set more requirements to `true` and increase `RequiredLength`.
If you need a simpler flow (for testing or internal systems), you can relax these rules.


**Example: Strong password policy**

```json title="appsettings.json"
"Password": {
  "RequiredLength": 12,
  "RequireDigit": true,
  "RequireNonAlphanumeric": true,
  "RepeatedResetPasswordTimeLimit": "0:05:0"
}
```


## Set password expiration and user account policies

Password expiration rules are controlled under the `User` node.

| Setting                            | Meaning                                                                                                                    |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **User:MaxPasswordAge**            | Number of days a password remains valid. After this period, the user must set a new one. Set to `0` to disable expiration. |
| **User:RequireUniqueEmail**        | Ensures each email is used by only one account.                                                                            |
| **User:RemindPasswordExpiryInDay** | How many days before expiration the system starts warning the user.                                                        |

If you want passwords to expire every 90 days, keep the default.
If you prefer no expiration, set `MaxPasswordAge` to `0`.


**Example: Forced password expiration**

```json title="appsettings.json"
"User": {
  "MaxPasswordAge": 90,
  "RequireUniqueEmail": true,
  "RemindPasswordExpiryInDay": 7
}
```


## Managing lockout rules after failed login attempts

The `Lockout` node helps protect accounts from brute-force attacks.

| Setting                            | Meaning                                                                                 |
| ---------------------------------- | --------------------------------------------------------------------------------------- |
| **Lockout:DefaultLockoutTimeSpan** | The time a user must wait before trying to log in again after too many failed attempts. |


If you want more protection, increase the lockout duration.
If users complain about being locked too often, reduce it.

**Example: Stricter lockout**

```json title="appsettings.json"
"Lockout": {
  "DefaultLockoutTimeSpan": "0:30:0"
}
```



<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../security-in-depth">← Security-in-depth </a>
    <a href="../configuration">Configuration →</a>
</div>