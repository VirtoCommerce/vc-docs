# Configure Microsoft Entra-Only Authentication for Azure SQL

If the Platform runs on Azure, Microsoft Defender for Cloud may flag a High severity recommendation: **Azure SQL logical servers should have Microsoft Entra-only authentication enabled**. The Virto Commerce Platform supports this setting today. No code changes, no platform configuration changes, and no custom modules are required. Virto Cloud environments can already use it, and self-hosted deployments on Azure can switch in a few steps.

## Why Microsoft recommends Entra-only authentication

Microsoft Entra-only authentication routes every connection through a single identity store instead of a mix of SQL logins and Entra accounts. Disabling an identity in Microsoft Entra ID disables it everywhere: SQL, storage, Key Vault, and the portal. There is no SQL login with a password left behind in a connection string.

When Microsoft Entra-only authentication is enabled, SQL authentication is disabled for the whole logical server. The SQL admin account, logins, and users can no longer connect. Only Microsoft Entra principals can. Because Defender rates this recommendation as High severity, it appears prominently in secure-score reports and compliance audits.

## What changes in Virto Commerce

Nothing changes in the Platform itself. The Virto Commerce Platform connects to SQL Server through EF Core and **Microsoft.Data.SqlClient**. Microsoft.Data.SqlClient authenticates to Azure SQL by acquiring a token through a managed identity, so no password is required.

Instead of a connection string with a SQL user and a password, the connection string points to a managed identity. The identity receives a token from Microsoft Entra ID. The token replaces the password, and the driver refreshes it automatically. The Platform still reads a plain connection string. This means:

* No platform code changes.
* No **appsettings.json** changes beyond the connection string itself.
* No extra environment variables or feature flags.
* No custom modules or dependencies.
* The same approach works for any Virto Commerce solution, because every solution connects to Azure SQL the same way.

## Virto Cloud

Virto Cloud already uses Microsoft Entra-only authentication. Each environment runs its own user-assigned managed identity. The SQL server allows Microsoft Entra authentication only, and the identity is referenced in the connection string. Application pods connect to the database with a token. There is no SQL password to store, rotate, or leak. If an existing Virto Cloud environment still uses SQL authentication, contact the Virto Cloud team to switch it.

## Enable Entra-only authentication on self-hosted deployment

Connect the Platform through Microsoft Entra ID first, then lock the server down. This order avoids downtime if a step is misconfigured.

To switch a self-hosted deployment to Microsoft Entra-only authentication:

1. [Set a Microsoft Entra admin on the SQL server](#set-microsoft-entra-admin-on-sql-server).
1. [Create a user-assigned managed identity for the Platform](#create-user-assigned-managed-identity-for-platform).
1. [Create a database user for the managed identity](#create-database-user-for-managed-identity).
1. [Update the connection string](#update-connection-string).
1. [Restart and verify](#restart-and-verify).
1. [Enable Microsoft Entra-only authentication on the server](#enable-microsoft-entra-only-authentication-on-server).
1. [Check Defender for Cloud](#check-defender-for-cloud).

### Prerequisites

Before configuring the module, make sure you have:

* An Azure SQL logical server that hosts the Virto Commerce database.
* Owner or Contributor access on that server, or the SQL Security Manager role for the step that enables Entra-only authentication.
* Permission to create a user-assigned managed identity in the same Microsoft Entra tenant as the SQL server.

### Set Microsoft Entra admin on SQL server

An Entra admin must be set on the server before Entra-only authentication can be enabled.

1. In the Azure portal, open the SQL server resource.
1. Select **Microsoft Entra ID** under **Settings**.
1. Select **Set admin**, choose an identity, then select **Save**.

A Microsoft Entra security group is recommended over a single user. Every member of the group inherits the admin role, so access can be managed by adding or removing group members instead of reconfiguring the server.

### Create user-assigned managed identity for Platform

Create a user-assigned managed identity in the same tenant as the SQL server, then attach it to whatever runs the Platform:

* For AKS, attach it through Microsoft Entra Workload ID. Virto Cloud uses this approach.
* For App Service or Container Apps, attach it under **Identity** → **User assigned** on the resource.

A managed identity is preferable to a service principal with a secret, because the identity is bound to the Azure resource and there is no credential to copy or store.

### Create database user for managed identity

Connect to the Virto Commerce database with the Microsoft Entra admin from the first step. Use SSMS, Azure Data Studio, or the portal query editor, then run:

```sql
CREATE USER [<managed-identity-name>] FROM EXTERNAL PROVIDER;
ALTER ROLE db_owner ADD MEMBER [<managed-identity-name>];
```

Because the SQL server belongs to the Entra tenant, `FROM EXTERNAL PROVIDER` looks the identity up in Microsoft Entra ID and creates a contained database user for it. The `db_owner` role is required because the Platform applies EF Core migrations on startup. If migrations run separately instead, `db_datareader`, `db_datawriter`, and `db_ddladmin` are enough.

### Update connection string

Replace `User Id=...;Password=...` with the managed identity:

```json title="appsettings.json"
"ConnectionStrings": {
  "VirtoCommerce": "Server=tcp:<server>.database.windows.net,1433;Initial Catalog=<database>;Authentication=Active Directory Managed Identity;User Id=<client-id-of-the-managed-identity>;Encrypt=True;TrustServerCertificate=False;"
},
```

For a user-assigned identity, `User Id` is the identity's client ID. For a system-assigned identity, omit `User Id`. For the full list of `ConnectionStrings` fields, see the [appsettings.json reference](../../../Configuration-Reference/appsettingsjson.md#connectionstrings).

`Authentication=Active Directory Default` works in both places. Locally it uses developer credentials from the Azure CLI or Visual Studio. In Azure it uses the managed identity, so the same connection string can be reused across every environment.

### Restart and verify

Restart the Platform and check the logs. It should start, apply migrations, and serve the Back office as before, with nothing else different.

### Enable Microsoft Entra-only authentication on server

Now lock the server down:

* In the Azure portal, open **SQL server** → **Settings** → **Microsoft Entra ID**. Turn on **Support only Microsoft Entra authentication for this server**, then select **Save**.
* Or with Azure CLI:

    ```bash
    az sql server ad-only-auth enable --resource-group <rg> --name <server>
    ```

This action requires the SQL Security Manager role, or a higher role such as Owner or Contributor.

For a new server, enable this setting during creation. Note that a policy checking only the creation-time setting does not enforce that local authentication stays off afterward. Assign the Microsoft Entra-only authentication initiative to enforce that separately.

### Check Defender for Cloud

Within the next assessment cycle, the recommendation turns green. Existing SQL logins are not deleted. They can no longer connect, so they can be removed at any pace afterward.

Microsoft Entra-only authentication is now enabled for the server, and the Platform connects to it using the managed identity instead of a SQL password.

## Summary

The following table summarizes what changes:

|  | Before | After |
| --- | --- | --- |
| Credentials | SQL login and password in the connection string. | Managed identity with a token. Nothing to store. |
| Revocation | Change the password and redeploy everywhere. | Disable the identity in Microsoft Entra ID, effective everywhere. |
| Defender for Cloud | High severity finding. | Compliant |
| Virto Commerce changes |  | None |

The same approach applies to Azure Database for PostgreSQL Flexible Server, which has an equivalent policy.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../configuring-vc-with-db-providers">← Configuring VC with DB providers</a>
    <a href="../creating-custom-module">Creating custom module →</a>
</div>
