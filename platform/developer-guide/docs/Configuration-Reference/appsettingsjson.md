# Appsettings.json

As Virto Commerce Platform is an ASP.NET Core based application, it can be configured as described in [this Microsoft article](https://docs.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-3.1).
<!--caching-start-->
## Configuration Settings

The configuration keys are hierarchical, and the most convenient way to manage them is to work with the **appsettings.json** file. The following sections, organized by configuration node and alphabetically, show the general structure of the file, provide defaults, and explain what each key is.

!!! note
    All settings listed below are optional unless marked **Required**.
<!--caching-end-->

### ConnectionStrings

These **required** settings represent connection strings for VC Platform and modules.

| Node                                    | Default or sample value                      | Description                                                                          |
| --------------------------------------- | ---------------------------------------------| --------------------------------------------------------------------------------------|
| ConnectionStrings.VirtoCommerce         | Data Source=(local)                          | The server name or network address of the SQL Server instance hosting the Virto Commerce database. This can be **(local)** for a local SQL Server instance or a specific server name/IP address. |
| ConnectionStrings.VirtoCommerce.InitialCatalog | VirtoCommerce3.net8                   | The name of the SQL Server database where the Virto Commerce Platform data is stored. This database contains all the necessary tables and data for the platform to operate. |
| ConnectionStrings.VirtoCommerce.PersistSecurityInfo | true<br>false                    | When set to **true**, this option allows security-sensitive information, such as the password, to be retained after the connection is made. |
| ConnectionStrings.VirtoCommerce.UserID  | virto                                        | The username used to authenticate the connection to the SQL Server database. This user must have sufficient permissions to access and manage the database. |
| ConnectionStrings.VirtoCommerce.Password | virto                                       | The password associated with the specified **UserID** for authenticating the connection to the SQL Server database. |
| ConnectionStrings.VirtoCommerce.ConnectTimeout | 30                                    | Specifies the number of seconds to wait before timing out when trying to establish a connection to the SQL Server. A value of 30 seconds is commonly used. |
| ConnectionStrings.VirtoCommerce.TrustServerCertificate | true                          | When set to **true**, this option allows the connection to proceed without validating the SQL Server's SSL certificate. This is often used in development environments where a trusted certificate might not be available. |


**Example**

```json title="appsettings.json"
"ConnectionStrings": {
    "VirtoCommerce": "Data Source=(local);Initial Catalog=VirtoCommerce3.net8;Persist Security Info=True;User ID=virto;Password=virto;Connect Timeout=30;TrustServerCertificate=True;"
```

###  VirtoCommerce

This configuration node defines the system settings of the VC Platform.

| Node                          | Default or sample value                                   | Description                                                                                             |
|-------------------------------|-----------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| LicenseActivationUrl          | https://license.virtocommerce.org/api/licenses/activate/  | The URL used to activate the Virto Commerce Platform license.                                           |
| SampleDataUrl                 | https://virtocommerce.azureedge.net/sample-data           | URL for downloading sample data during the initial setup of the Virto Commerce Platform.                |
| DiscoveryPath                 | ./modules                                                 | The relative or absolute file system path where the platform will discover installed modules.           |
| AllowInsecureHttp             | false                                                     | Controls how the OpenID Connect server (ASOS) handles requests arriving on non-HTTPS endpoints. When set to **false**, it helps mitigate man-in-the-middle attacks. |
| UseResponseCompression        | false                                                     | Enables or disables response compression to improve performance.                                        |
| Hangfire                      | [Read more](appsettingsjson.md#hangfire)                  | Configures background processing settings, including job storage options and retry mechanisms.          |
| ApplicationInsights           | [Read more](appsettingsjson.md#application-insights)      | Manages telemetry settings and sampling options for Application Insights.                               |
| Swagger.Enable                | true                                                      | Controls whether Swagger is enabled, allowing access to the Swagger UI and API documentation.           |
| GraphQLPlayground.Enable      | true                                                      | Controls whether the GraphQL Playground is enabled, allowing access to the GraphQL UI and schemas.      |
| PlatformUI.Enable             | true                                                      | Determines whether the Platform's user interface is enabled.                                            |


**Examples**

=== "Hangfire"

    ```json title="appsettings.json"
    "Hangfire": {
        "JobStorageType": "Database",
        //Set value to false to stop processing the background jobs.
        "UseHangfireServer": true,
        "AutomaticRetryCount": 2,
        //"WorkerCount": 11,
        //"Queues": [
        //    "alpha", "beta", "default"
        //],
        "SqlServerStorageOptions": {
            "CommandBatchMaxTimeout": "00:05:00",
            "SlidingInvisibilityTimeout": "00:05:00",
            "QueuePollInterval": "00:00:00",
            "UseRecommendedIsolationLevel": true,
            "UseIgnoreDupKeyOption": true,
            "UsePageLocksOnDequeue": true,
            "DisableGlobalLocks": true,
            "EnableHeavyMigrations": true,
            "TryAutoDetectSchemaDependentOptions": false,
            "InactiveStateExpirationTimeout": "7.00:00:00"
          },
          "MySqlStorageOptions": {
            "InvisibilityTimeout": "00:05:00",
            "QueuePollInterval": "00:00:05"
          },
          "PostgreSqlStorageOptions": {
            "InvisibilityTimeout": "00:05:00",
            "QueuePollInterval": "00:00:05",
            "UseRecommendedIsolationLevel": true,
            "UsePageLocksOnDequeue": true,
            "DisableGlobalLocks": true
          }
        },
    ```

=== "Swagger"

    ```json title="appsettings.json"
    "Swagger":
    {
    "Enable": true
    }
    ```

=== "Playground"

    ```json title="appsettings.json"
    "GraphQLPlayground": {
      "Enable": false
    }
    ```

=== "FileExtensionsBlackList"

    ```json title="appsettings.json"
    "FileExtensionsBlackList": [".pdf", ".json"]
    ```


#### Application Insights

This node adds and customizes the Application Insight section.

<!--AppInsights1-start-->

| Node                                         | Default or sample value                                   | Description                                                                                        |
| ---------------------------------------------| ----------------------------------------------------------| -------------------------------------------------------------------------------------------------- |
| SamplingOptions.Processor                                 | adaptive <br> fixed-rate | This setting lets you chose between two sampling methods:<br>**Adaptive sampling**: automatically adjusts the volume of telemetry sent from the SDK in your ASP.NET/ASP.NET Core app, and from Azure Functions. Learn more about [configuring this option](https://learn.microsoft.com/en-us/azure/azure-monitor/app/sampling?tabs=net-core-new#configuring-adaptive-sampling-for-aspnet-applications).<br>**Fixed-rate sampling**: reduces the volume of telemetry sent from both the application. Unlike adaptive sampling, it reduces telemetry at a fixed rate controlled by SamplingPercentage setting. |
| SamplingOptions.Adaptive.MaxTelemetryItemsPerSecond       | 5                        | Maximum telemetry items per second allowed in adaptive sampling. |
| SamplingOptions.Adaptive.InitialSamplingPercentage        | 100                      | Initial sampling percentage in adaptive sampling.|
| SamplingOptions.Adaptive.MinSamplingPercentage            | 0.1                      | Minimum sampling percentage in adaptive sampling.|
| SamplingOptions.Adaptive.MaxSamplingPercentage            | 100                      | Maximum sampling percentage in adaptive sampling.|
| SamplingOptions.Adaptive.EvaluationInterval               | 00:00:15                 | Interval between sampling evaluations in adaptive sampling.|
| SamplingOptions.Adaptive.SamplingPercentageDecreaseTimeout | 00:02:00                | Timeout before decreasing sampling percentage in adaptive sampling.|
| SamplingOptions.Adaptive.SamplingPercentageIncreaseTimeout | 00:15:00                | Timeout before increasing sampling percentage in adaptive sampling.|
| SamplingOptions.Adaptive.MovingAverageRatio               | 0.25                     | Ratio used for moving average calculations in adaptive sampling.|
| SamplingOptions.Fixed.SamplingPercentage                  | 100                      | Fixed sampling percentage used for telemetry in Application Insights.|
| SamplingOptions.IncludedTypes                             | Dependency<br>Event<br>Exception<br>PageView<br>Request<br>Trace     | A semi-colon delimited list of types that you do want to subject to sampling. The specified types will be sampled. All telemetry of the other types will always be transmitted. All types are included by default.|
| SamplingOptions.ExcludedTypes                             | Dependency<br>Event<br>Exception<br>PageView<br>Request<br>Trace       | A semi-colon delimited list of types that you do not want to be sampled. All telemetry of the specified types is transmitted. The types that aren't specified will be sampled. Empty by default |
| EnableSqlCommandTextInstrumentation                       | true                     | Controls Application Insight telemetry processor thats excludes dependency SQL queries. Any SQL command name or statement that contains a string from **QueryIgnoreSubstrings** options will be ignored.|
| IgnoreSqlTelemetryOptions.QueryIgnoreSubstrings           | [HangFire]., sp_getapplock, sp_releaseapplock | Specifies substrings to ignore in SQL telemetry to avoid collecting irrelevant data, particularly related to Hangfire's internal operations.     |

<!--AppInsights1-end-->


**Example**

To configure telemetry: 

<!--AppInsights2-start-->


1. Use current active telemetry configuration which is already initialized in most application types like ASP.NET Core:
    ```json title="appsettings.json"
    {
      "ApplicationInsights": {
        "ConnectionString": "<Copy connection string from Application Insights Resource Overview>"
      }
    }
    ```

1. Configure Platform AP telemetry behavior inside the `VirtoCommerce:ApplicationInsights` section: 
    ```json title="appsettings.json"
    {
      "VirtoCommerce": {
        "ApplicationInsights": {
          "SamplingOptions": {
            "Processor": "Adaptive",
            "Adaptive": {
              "MaxTelemetryItemsPerSecond": "5",
              "InitialSamplingPercentage": "100",
              "MinSamplingPercentage": "0.1",
              "MaxSamplingPercentage": "100",
              "EvaluationInterval": "00:00:15",
              "SamplingPercentageDecreaseTimeout": "00:02:00",
              "SamplingPercentageIncreaseTimeout": "00:15:00",
              "MovingAverageRatio": "0.25"
            },
            "Fixed": {
              "SamplingPercentage": 90
            },
            "IncludedTypes": "Dependency;Event;Exception;PageView;Request;Trace",
            "ExcludedTypes": ""
          },
          "EnableSqlCommandTextInstrumentation": true,
          "IgnoreSqlTelemetryOptions": {
            "QueryIgnoreSubstrings": [
              "[HangFire].",
              "sp_getapplock",
              "sp_releaseapplock"
            ]
          }
        }
      }
    }
    ```

<!--AppInsights2-end-->


You can enable AI logging by updating the following `Serilog` configuration sections (the module comes with a [sink](https://github.com/serilog-contrib/serilog-sinks-applicationinsights) for Serilog that writes events to Microsoft Application Insights. To enable AI logging update the following `Serilog` configuration sections):

<!--AppInsights3-start-->


```json title="appsettings.json"
{
  "Serilog": {
    "Using": [
      "Serilog.Sinks.ApplicationInsights"
    ],
    "WriteTo": [
      {
        "Name": "ApplicationInsights",
        "Args": {
          "connectionString": "<Copy connection string from Application Insights Resource Overview>",
          "telemetryConverter": "Serilog.Sinks.ApplicationInsights.TelemetryConverters.TraceTelemetryConverter, Serilog.Sinks.ApplicationInsights",
          "restrictedToMinimumLevel": "Error"
        }
      }
    ]
  }
}
```

<!--AppInsights3-end-->

The **telemetryConverter** has to be specified with the full type name and the assembly name. A **connectionString** can be omitted if it's supplied in the **APPLICATIONINSIGHTS_CONNECTION_STRING** environment variable.

#### Hangfire

This node configures the background processing settings for Hangfire in the Virto Commerce platform. 

|Node                                                                  | Default or sample value  | Description                                                                                        |
|----------------------------------------------------------------------|--------------------------|----------------------------------------------------------------------------------------------------|
| JobStorageType                                                       | Database                 | Specifies the storage type for Hangfire jobs.                     |
| UseHangfireServer                                                    | true                     | Controls whether the Hangfire server is enabled for processing background jobs.  |
| AutomaticRetryCount                                                  | 2                        | Sets the maximum number of retry attempts for failed background jobs. |
| SqlServerStorageOptions.CommandBatchMaxTimeout                       | 00:05:00                 | The maximum timeout for batching commands in Hangfire's SQL Server storage.                        |
| SqlServerStorageOptions.SlidingInvisibilityTimeout                   | 00:05:00                 | Time after which a job is marked as invisible if not processed.                                    |
| SqlServerStorageOptions.QueuePollInterval                            | 00:00:00                 | Interval between polls for new jobs in the queue.                                                  |
| SqlServerStorageOptions.UseRecommendedIsolationLevel                 | true                     | Whether to use the recommended isolation level for transactions.                                   |
| SqlServerStorageOptions.UseIgnoreDupKeyOption                        | true                     | Option to ignore duplicate keys in the database.                                                   |
| SqlServerStorageOptions.UsePageLocksOnDequeue                        | true                     | Enables page locks when dequeuing jobs to improve performance.                                     |
| SqlServerStorageOptions.DisableGlobalLocks                           | true                     | Disables global locks to optimize performance in multi-node environments.                          |
| SqlServerStorageOptions.EnableHeavyMigrations                        | true                     | Enables heavy migrations, which may be necessary for certain schema updates.                       |
| SqlServerStorageOptions.TryAutoDetectSchemaDependentOptions          | false                    | Option to automatically detect schema-dependent options.                                           |
| SqlServerStorageOptions.InactiveStateExpirationTimeout               | 7.00:00:00               | Time after which inactive jobs are removed from storage.                                           |
| MySqlStorageOptions.InvisibilityTimeout                              | 00:05:00                 | Time after which a job is marked as invisible in MySQL storage.                                    |
| MySqlStorageOptions.QueuePollInterval                                | 00:00:05                 | Interval between polls for new jobs in the MySQL queue.                                            |
| PostgreSqlStorageOptions.InvisibilityTimeout                         | 00:05:00                 | Time after which a job is marked as invisible in PostgreSQL storage.                               |
| PostgreSqlStorageOptions.QueuePollInterval                           | 00:00:05                 | Interval between polls for new jobs in the PostgreSQL queue.                                       |
| PostgreSqlStorageOptions.UseRecommendedIsolationLevel                | true                     | Whether to use the recommended isolation level for PostgreSQL transactions.|
| PostgreSqlStorageOptions.UsePageLocksOnDequeue                       | true                     | Enables page locks when dequeuing jobs in PostgreSQL to improve performance.|
| PostgreSqlStorageOptions.DisableGlobalLocks                          | true                     | Disables global locks in PostgreSQL to optimize performance in multi-node environments. |


**Example**

```json title="appsettings.json"
    {
    "VirtoCommerce": {
      "Hangfire": {
          "JobStorageType": "Database",
          //Set value to false to stop processing the background jobs.
          "UseHangfireServer": true,
          "AutomaticRetryCount": 2,
          //"WorkerCount": 11,
          //"Queues": [
          //    "alpha", "beta", "default"
          //],
        "SqlServerStorageOptions": {
          "CommandBatchMaxTimeout": "00:05:00",
          "SlidingInvisibilityTimeout": "00:05:00",
          "QueuePollInterval": "00:00:00",
          "UseRecommendedIsolationLevel": true,
          "UseIgnoreDupKeyOption": true,
          "UsePageLocksOnDequeue": true,
          "DisableGlobalLocks": true,
          "EnableHeavyMigrations": true,
          "TryAutoDetectSchemaDependentOptions": false,
          "InactiveStateExpirationTimeout": "7.00:00:00"
        },
        "MySqlStorageOptions": {
          "InvisibilityTimeout": "00:05:00",
          "QueuePollInterval": "00:00:05"
        },
        "PostgreSqlStorageOptions": {
          "InvisibilityTimeout": "00:05:00",
          "QueuePollInterval": "00:00:05",
          "UseRecommendedIsolationLevel": true,
          "UsePageLocksOnDequeue": true,
          "DisableGlobalLocks": true
        }
      },
    }
    }
```

#### Stores

This node configures default store settings and domain assignments in the Virto Commerce platform.

| Node               | Default or sample value | Description                                                                                         |
|--------------------|-------------------------|-----------------------------------------------------------------------------------------------------|
| DefaultStore       | B2B-store               | Specifies the default store identifier to be used by the platform.                                  |
| Domains            |                         | Allows assigning domain names to specific stores, with the option to map local domains for testing. |

**Example**

```json title="appsettings.json"
{
  "VirtoCommerce": {
    "Stores": {
      "DefaultStore": "B2B-store",
      "Domains": {
        "localhost": "B2B-store"
      }
    }
  }
}
```

### AI Document Processing  

This node configures AI-based document processing services and file upload settings in the application.  

| Node                                  | Default or sample value                      | Description                                                                                   |
| ------------------------------------- | -------------------------------------------- | --------------------------------------------------------------------------------------------- |
| AI:Service                            | "OpenAI"                                     | The AI service provider. Currently, the only supported option is **"OpenAI"**.                |
| AI:OpenAI                             |                                              | OpenAI-specific configuration.                                                               |
| AI:OpenAI:ModelId                     | "gpt-4o"<br>"gpt-4o-mini"                   | Specifies the OpenAI model to use.                                                           |
| AI:OpenAI:ApiKey                      | "your-api-key"                               | The API key used for authentication with OpenAI.                                              |
| FileUpload                            |                                              | Configuration for file uploads.                                                              |
| FileUpload:Scopes                     |                                              | Array of upload scopes, each defining settings for specific file categories.                  |
| FileUpload:Scopes[n]:Scope            | "purchase-request-sources"                  | Name of the file upload scope.                                                               |
| FileUpload:Scopes[n]:MaxFileSize      | 20971520                                     | Maximum file size in bytes. The sample value is **20 MB**.                                    |
| FileUpload:Scopes[n]:AllowedExtensions| [".gif", ".jpeg", ".jpg", ".png", ".webp"]  | Array of allowed file extensions for the specified upload scope.                              |


**Example**  

```json title="appsettings.json"
{
  "AI": {
    "Service": "OpenAI",
    "OpenAI": {
      "ModelId": "gpt-4o",
      "ApiKey": "your-api-key"
    }
  },
  "FileUpload": {
    "Scopes": [
      {
        "Scope": "purchase-request-sources",
        "MaxFileSize": 20971520,
        "AllowedExtensions": [
          ".gif",
          ".jpeg",
          ".jpg",
          ".png",
          ".webp"
        ]
      }
    ]
  }
}
```


### Assets

This **required** node determines how VC Platform will be working with assets, i.e. files.

| Node                              | Default or sample value             | Description                                                                                                                   |
| --------------------------------- | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------  |
| Provider                          | "FileSystem"<br>"AzureBlobStorage"  | Current asset provider.                                                                                                       |
| FileSystem                        |                                     | File system-based asset provider configuration. Used when the **Provider** setting has the value **"FileSystem"**.            |
| FileSystem:RootPath               | "~/assets"                          | The root path where assets are stored in the file system.                                                                     |
| FileSystem:PublicUrl              | "https://localhost:5001/assets/"    | The public Url used to access assets stored in the file system.                                                               |
| AzureBlobStorage                  |                                     | Azure Blob Storage-based asset provider configuration. Used when the **Provider** setting has the value **"AzureBlobStorage"**.   |
| AzureBlobStorage:ConnectionString |                                     | The connection string for Azure Blob Storage.                                                                                 |
| AzureBlobStorage:CdnUrl           |                                     | The optional CDN Url for serving assets from Azure Blob Storage.                                                              |


**Examples**

=== "FileSystem"
    <!--filesystem-start-->
    ```json title="appsettings.json"
     "Assets": {
        "Provider": "FileSystem",
        "FileSystem": {
          "RootPath": "~/assets",
          "PublicUrl": "http://localhost:5001/assets/"
        }
     }
    ```
    <!--filesystem-end-->

=== "AzureBlobStorage"
    <!--azureblobstorage-start-->
    ```json title="appsettings.json"
     "Assets": {
        "Provider": "AzureBlobStorage",
        "AzureBlobStorage": {
            "ConnectionString": "",
            "CdnUrl": ""
        }
     }  
    ```
    <!--azureblobstorage-end-->

### Auth

This setting determines platfom authentication parameters.

| Node                   | Default or sample value              | Description                                                                                                                           |
| ---------------------- | ---------------------------------    | ------------------------------------------------------------------------------------------------------------------------------------- |
| Authority              | https://localhost:5051/ <br> https://auth.example.com/ | The Url of the authentication server.<br>Leave empty for the mode when authorization and resource server are the same application.       |
| Audience               | "resource_server"                    | The audience for which the token is intended.                                                                                         |
| PublicCertPath         | "./certificates/virtocommerce.crt"   | The file path to the public certificate used for token validation.                                                                    |
| PrivateKeyPath         | "./certificates/virtocommerce.pfx"   | The file path to the private key used for token signing.                                                                              |
| PrivateKeyPassword     | "virto"                              | The password for accessing the private key (if protected by a password).                                                              |


**Example**

```json title="appsettings.json"
"Auth": {
    "Authority": "",
    "Audience": "resource_server",
    "PublicCertPath": "./certificates/virtocommerce.crt",
    "PrivateKeyPath": "./certificates/virtocommerce.pfx",
    "PrivateKeyPassword": "virto"
}
```

### Authentication

The Virto Commerce Platform supports the following authentication methods:  

* [Username and password](#passwordlogin): Users can authenticate using their credentials to obtain access tokens. This approach is straightforward and suitable for simple scenarios where no external identity provider is required.  

* [OpenID connect](#oidc): Clients can authenticate end-users via an authorization server. It adheres to the OpenID Connect standard, enabling integration with external identity providers like Entra ID (formerly Azure AD) for more robust identity management.  


#### PasswordLogin

This node enables authentication with username and password.

| Node      | Default or sample value   | Description  |
| ----------| ------------------------  | ------------ |
| Enabled   | true<br> false            | Always enabled by default. Setting to **false** will disable logging in with username and password.
| Priority  | 0                         | Configures the priority of the password login popup on the _Login_ page. The lowest value means the highest priority.


**Example**

```json title="appsettings.json"
{
  "PasswordLogin": {
    "Enabled": true
  }
}
```

#### OIDC

This node defines the settings for OpenID Connect authentication in Virto Commerce. This configuration enables integration with OIDC providers, allowing users to authenticate via external identity systems:  

<!--OIDC-start-->


| Node                             | Default value                                       | Description                                                                                     |
|----------------------------------|-----------------------------------------------------|-------------------------------------------------------------------------------------------------|
| Enabled                          | false                                               | Enables or disables the OIDC authentication.                                                    |
| AuthenticationType               | "oidc"                                              | A unique identifier for the authentication method.                                              |
| AuthenticationCaption            | "OpenID Connect"                                    | A user-friendly name for the authentication method.                                             |
| AllowCreateNewUser               | true                                                | Allows creating new users upon successful authentication.                                       |
| DefaultUserType                  | "Manager"                                           | Specifies the user type of newly created users.                                                |
| DefaultUserRoles                 | []                                                  | List of roles assigned to newly created users.                                                 |
| UserNameClaimType                | "name"                                              | Claim type used to retrieve the username.                                                      |
| EmailClaimType                   | "email"                                             | Claim type used to retrieve the email address.                                                 |
| HasLoginForm                     | true                                                | Displays a dedicated login form for this authentication method.                                |
| Priority                         | 1                                                   | Specifies the sorting order of the authentication method.                                      |
| LogoUrl                          | null                                                | URL of the logo for the OpenID Connect authentication provider.                                |
| Authority                        | "https://localhost:5001"                            | Base URL of the OIDC provider (identity server).                                               |
| ClientId                         | "your-client-id"                                    | Client identifier issued by the OIDC provider.                                                 |
| ClientSecret                     | "your-client-secret"                                | Confidential client secret issued by the OIDC provider.                                        |
| Scope                            | ["openid", "profile", "email"]                      | List of scopes requested from the OIDC provider.                                               |
| ResponseMode                     | "form_post"                                         | Determines how the authorization response is returned.                                         |
| ResponseType                     | "id_token"                                          | Specifies the type of response expected from the OIDC provider.                                |
| GetClaimsFromUserInfoEndpoint    | false                                               | Enables retrieval of additional claims from the user info endpoint.                            |
| CallbackPath                     | "/signin-oidc"                                      | Path for redirection after successful authentication.                                          |
| SignedOutCallbackPath            | "/signout-callback-oidc"                            | Path for redirection after successful logout.                                                  |


=== "Google"  

    ```json title="appsettings.json"
    "oidc": {
        "Enabled": true,
        "AuthenticationType": "google",
        "AuthenticationCaption": "Google",
        "Authority": "https://accounts.google.com",
        "ClientId": "your-client-id",
        "ClientSecret": "your-client-secret",
        "UserNameClaimType": "email"
    }
    ```

    !!! note
        If you are using a single provider, you may not enter values for the callback paths. The system will use the default values.



=== "Microsoft"  

    ```json title="appsettings.json"
    "oidc": {
        "Enabled": true,
        "AuthenticationType": "microsoft",
        "AuthenticationCaption": "Microsoft",
        "Authority": "https://login.microsoftonline.com/your-tenant-id/v2.0",
        "ClientId": "your-application-id",
        "UserNameClaimType": "preferred_username"
    }
    ```

    !!! note
        If you are using a single provider, you may not enter values for the callback paths. The system will use the default values.

=== "Virto Commerce"  

    ```json title="appsettings.json"
    "oidc": {
        "Enabled": true,
        "AuthenticationType": "virto",
        "AuthenticationCaption": "Virto Commerce",
        "Authority": "https://localhost:5001",
        "ClientId": "your-client-id",
        "ClientSecret": "your-client-secret",
        "ResponseMode": "query",
        "ResponseType": "code",
        "GetClaimsFromUserInfoEndpoint": true
    }
    ```

    !!! note
        If you are using a single provider, you may not enter values for the callback paths. The system will use the default values.


=== "Multiple providers"  

    ```json title="appsettings.json"
    "oidc": [
      {
        "Enabled": true,
        "AuthenticationType": "virto",
        "AuthenticationCaption": "Virto Commerce",
        "Authority": "https://localhost:5001",
        "ClientId": "your-client-id",
        "ClientSecret": "your-client-secret",
        "CallbackPath": "/signin-virto",
        "SignedOutCallbackPath": "/signout-virto"
      },
      {
        "Enabled": true,
        "AuthenticationType": "google",
        "AuthenticationCaption": "Google",
        "Authority": "https://accounts.google.com",
        "ClientId": "your-client-id",
        "ClientSecret": "your-client-secret",
        "UserNameClaimType": "email",
        "CallbackPath": "/signin-google",
        "SignedOutCallbackPath": "/signout-google"
      },
      {
        "Enabled": true,
        "AuthenticationType": "microsoft",
        "AuthenticationCaption": "Microsoft",
        "Authority": "https://login.microsoftonline.com/your-tenant-id/v2.0",
        "ClientId": "your-application-id",
        "UserNameClaimType": "preferred_username",
        "CallbackPath": "/signin-microsoft",
        "SignedOutCallbackPath": "/signout-microsoft"
      }
    ]
    ```

    !!! note
        If using multiple providers, make sure you use unique authentication types and callback paths for each.

<!--OIDC-end-->



### Authorization

This configuration node defines authorization settings for the system.

| Node                      | Default or sample value   | Description                                                                                               |
| ------------------------- | ------------------------- | --------------------------------------------------------------------------------------------------------- |
| ReturnPasswordHash        | true<br> false        | A boolean setting that determines whether to return the password hash during user authentication.<br>If set to **true**, the password hash is returned; if set to **false**, it's not returned. |
| RefreshTokenLifeTime     | "30.00:00:00"            | The time span specifying the lifetime of a refresh token.<br>A refresh token is used to obtain a new access token without re-entering<br>the user's credentials. The default is 30 days. |
| AccessTokenLifeTime      | "00:30:00"               | The time span specifying the lifetime of an access token.<br>An access token is used to access protected resources.<br>The default is 30 minutes. |
| LimitedCookiePermissions | "platform:asset:read;platform:export;..." | A semicolon-separated list of permissions that define the limited cookie permissions for the user. These permissions determine what actions the user can perform when using cookies for authentication. |
| AllowApiAccessForCustomers| true<br>false         | A boolean setting that controls whether API access is allowed for customers.<br>If set to **false**, customers are not allowed to access the API; if set to **true**, they are granted API access. |

**Example**

```json title="appsettings.json"
"Authorization": {
  "ReturnPasswordHash": true,
  "RefreshTokenLifeTime": "30.00:00:00",
  "AccessTokenLifeTime": "00:30:00",
  "LimitedCookiePermissions": "platform:asset:read;platform:export;content:read;platform:asset:create;licensing:issue;export:download",
  "AllowApiAccessForCustomers": false
}
```


### AzureAd

This node is used for authentication with Azure Active Directory. 

![Readmore](media/readmore.png){: width="25"}  [How to enable authentication with Azure Active Directory](../Fundamentals/Security/extensions/adding-azure-as-sso-provider.md)

| Node                  | Default or sample value                                   | Description                                                                                                       |
| --------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Enabled               | false<br> true                                            | Enables authentication with Azure Active Directory. By default, this value is **false**, i.e. authentication is disabled.|
| UsePreferredUsername  | false <br> true                                           | If set to **true**, the system will check the **preferred_username** in case the **upn** claim returns empty.             |
| Priority              | 0 <br> 1...                                               | Configures the priority of the Azure Active Directory login popup on the Login page. The lowest value means the highest priority. |
| AuthenticationType    | "AzureAD"                                                 | Provides the authentication scheme. Must always have the **AzureAD** value set.                                      |
| AuthenticationCaption | "Azure Active Directory"                                  | Sets a human-readable caption for the Azure AD authentication provider. Visible on the **Sign In** page.            |
| ApplicationId         |                                                           | The ID of the Virto Commerce platform application registered in Azure Active Directory. You can find it in the Azure control panel through **Azure Active Directory --> App registrations --> (platform app) --> Application ID**. |
| TenantId              |                                                           | The ID of the Azure AD domain that will be used for authentication. You can find it in the Azure control panel through **Azure Active Directory --> Properties --> Directory ID**.  |
| AzureAdInstance       | https://login.microsoftonline.com/                        | Url of the Azure AD endpoint used for authentication.                                                             |
| DefaultUserType       | "Manager"<br>"Customer"                                   | Default user type for new users created upon first sign-in by Azure AD accounts.                                   |
| DefaultUserRoles      | "Order manager"<br>"Store manager"                        | Default user roles assigned to new users created upon first sign-in by Azure AD accounts.                           |
| MetadataAddress       |                                                           | An optional setting that enables the discovery endpoint for obtaining metadata. Must be set only when your app has custom signing keys.<br> If your app has custom signing keys as a result of using the claim mapping feature, you should append the `appid` query parameter containing the app ID in order to get a `jwks_uri` pointing to your app's signing key information.<br> For example, [https://login.microsoftonline.com/{tenant}/v2.0/.well-known/openid-configuration?appid=6731de76-14a6-49ae-97bc-6eba6914391e](https://login.microsoftonline.com/%7Btenant%7D/v2.0/.well-known/openid-configuration?appid=6731de76-14a6-49ae-97bc-6eba6914391e) contains a `jwks_uri` of [https://login.microsoftonline.com/{tenant}/discovery/v2.0/keys?appid=6731de76-14a6-49ae-97bc-6eba6914391e](https://login.microsoftonline.com/%7Btenant%7D/discovery/v2.0/keys?appid=6731de76-14a6-49ae-97bc-6eba6914391e). |
| UsePreferredUsername  | true<br>false                                             | Indicates whether to use the `preferred_username` claim as a fallback scenario in case the UPN claim is not set for getting the username. |

**Example**

Example settings for the `AzureAD` section:

```json
"AzureAd": {
		"Enabled": true,
		"AuthenticationType": "AzureAD",
		"AuthenticationCaption": "Azure Active Directory",
		"ApplicationId": "b6d8dc6a-6ddd-4497-ad55-d65f91ca7f50",
		"TenantId": "fe353e8f-5f08-43b4-89d1-f4acec93df33",
		"AzureAdInstance": "https://login.microsoftonline.com/",
		"DefaultUserType": "Manager",
		"UsePreferredUsername": false,
		"Priority": 0
	},
```


### Caching
This node manages caching configuration.

<!--caching-start-->

| Node                      | Default or sample value                   | Description  |
| ------------------------- | ----------------------------------------- | ------------ |
| Redis                     |                                           | Redis configuration. Includes the message channel to use and the number of retries. |
| CacheEnabled              | true<br>false                             | Cache entries are retained based on the expiration settingsб if **true**.<br>Disables caching of application data for the entire application, if **false**.<br> Used when **ConnectionStrings:RedisConnectionString** is not specified. |
| CacheSlidingExpiration    | "0:15:00"                                 | The cache entry will expire if it is not accessed for a specified amount of time.<br>Used when **CacheAbsoluteExpiration** is not defined.|
| CacheAbsoluteExpiration   | "0:5:00"                                  | The cache entry will expire after a specified amount of time. <br>Used when **RedisConnectionString** is not specified.|


**Examples**

``` json title="appsettings.json"
 "Caching": {
       "CacheEnabled": true, 
       "CacheSlidingExpiration": "0:15:00", 
       //"CacheAbsoluteExpiration": "0:15:00"
    }
```

```json title="appsettings.json"
"Redis": {
"ChannelName": "VirtoCommerceChannel",
"BusRetryCount": 3
} 
```

<!--caching-end-->

### Content

This **required** setting is used for static content configuration (including themes) for the `VirtoCommerce.Content` module.

| Node                                | Default or sample value   | Description                                                                                               |
| ----------------------------------- | ------------------------  | --------------------------------------------------------------------------------------------------------- |
| Provider                            | "FileSystem"           | Current content (file) provider. The supported values are **FileSystem** and **AzureBlobStorage**.           |
| FileSystem                          |                           | File system-based content provider configuration. This is the default provider used unless **AzureBlobStorage** is set as the current provider. |
| FileSystem:RootPath                 | "~/cms-content"        | The root path where content files are stored in the file system.                                          |
| FileSystem:PublicUrl                | "https://localhost:5001/cms-content/" | The public URL used to access content files stored in the file system.                      |
| AzureBlobStorage                    |                           | Azure Blob Storage-based content provider configuration. Used when the **Provider** setting has **AzureBlobStorage** as the value. |
| AzureBlobStorage:ConnectionString   |                           | The connection string for Azure Blob Storage.                                                            |
| AzureBlobStorage:CdnUrl             |                           | The optional CDN (Content Delivery Network) URL for serving content from Azure Blob Storage.             |
| AzureBlobStorage:RootPath           | "cms"                   | The root path within the Azure Blob Storage container where content files are stored.                     |


**Examples**

=== "FileSystem"

    ```json title="appsettings.json"
    "FileSystem": {
    "RootPath": "~/cms-content",
    "PublicUrl": "http://localhost:10645/cms-content/"
    }  
    ```

=== "AzureBlobStorage"

    ```json title="appsettings.json"
    "AzureBlobStorage": {
    "ConnectionString": "",
    "CdnUrl": ""
    }
    ```


### Crud

This configuration node defines settings for the CRUD operations within the system.

| Node            | Default or sample value | Description                                                                                                   |
| --------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------- |
| MaxResultWindow | 2147483647              | The maximum value for the combination of **skip** and **take** parameters in search requests. By setting this value to **2147483647**, there are no specific limits on the number of records that can be retrieved in a single search request. This effectively allows retrieving a large number of records in a single query. |

**Example**

```json title="appsettings.json"
"Crud": {
    "MaxResultWindow": 2147483647
}
```


### DataProtection

This configuration node configures lifetimes for security tokens that are issued by platform like password reset.

| Node                         | Default value                    | Description                                         |
| ---------------------------- | ---------------------------------|---------------------------------------------------- |
| DataProtection.TokenLifespan | "1.00:00:00" - Defaults to 1 day | The amount of time a generated token remains valid. |

**Example**

```json title="appsettings.json"
"DataProtection": {
		"TokenLifespan": "24:00:00",		
	},
```

### DatabaseProvider

The DatabaseProvider node specifies the type of database management system (DBMS) that the Virto Commerce Platform will use to store and manage its data. 

| Node               | Supported values                                  | Description                                                                                                            |
| ------------------ | ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| DatabaseProvider   | SqlServer (default)<br>MySql<br>PostgreSql       | Specifies the type of database management system (DBMS) that the Virto Commerce Platform will use to store and manage data.    |


**Example**

```json title="appsettings.json"
"DatabaseProvider": "SqlServer"
```

### DefaultMainMenuState

This node configures the default state of the main menu in the Virto Commerce platform. It specifies which menu items are shown, their order, and if they are marked as favorites.

| Node            | Default or sample value | Description                                                                                           |
|-----------------|-------------------------|-------------------------------------------------------------------------------------------------------|
| items[].path    | "browse/store"          | The path for a specific menu item. Each path corresponds to a different module or area in the platform.|
| items[].isFavorite | true                 | Indicates whether the menu item is marked as a favorite, making it easily accessible.                  |
| items[].order   | 0                       | Specifies the order in which the menu item appears. Lower numbers appear earlier in the menu list.     |

**Example**

```json title="appsettings.json"
{
  "VirtoCommerce": {
    "DefaultMainMenuState": {
      "items": [
        {
          "path": "browse/store",
          "isFavorite": true,
          "order": 0
        },
        {
          "path": "browse/catalog",
          "isFavorite": true,
          "order": 1
        },
        {
          "path": "browse/pricing",
          "isFavorite": true,
          "order": 2
        },
        {
          "path": "browse/Inventory",
          "isFavorite": true,
          "order": 3
        },
        {
          "path": "browse/orders",
          "isFavorite": true,
          "order": 4
        },
        {
          "path": "browse/member",
          "isFavorite": true,
          "order": 5
        },
        {
          "path": "browse/marketing",
          "isFavorite": true,
          "order": 6
        },
        {
          "path": "browse/assets",
          "isFavorite": true,
          "order": 7
        },
        {
          "path": "browse/content",
          "isFavorite": true,
          "order": 8
        }
      ]
    }
  }
}
```

### ExternalModules

This node configures the settings for external modules in the Virto Commerce platform.

| Node                  | Default or sample value  | Description                                                                                   |
|-----------------------|--------------------------|-----------------------------------------------------------------------------------------------|
| IncludePrerelease     | false                    | Determines whether to include prerelease versions of modules during updates and installations. |
| ModulesManifestUrl    | "https://raw.githubusercontent.com/VirtoCommerce/vc-modules/master/modules_v3.json" | Specifies the URL where the module manifest is located.     |
| AuthorizationToken    |                          | Token used for authorization to access module sources, if needed.                             |
| AutoInstallModuleBundles | ["commerce"]          | Lists the module bundles that will be automatically installed upon platform setup.            |

**Example**

```json title="appsettings.json"
{
  "VirtoCommerce": {
    "ExternalModules": {
      "IncludePrerelease": false,
      "ModulesManifestUrl": "https://raw.githubusercontent.com/VirtoCommerce/vc-modules/master/modules_v3.json",
      "AuthorizationToken": "",
      "AutoInstallModuleBundles": [
        "commerce"
      ]
    }
  }
}
```

### FileUpload

This node configures file upload settings for your application:

| Node                      |Default or sample value            | Description                                               |
|---------------------------|-----------------------------------|-----------------------------------------------------------|
| RootPath                  |                                   | The root directory where uploaded files will be stored.   |
| Scopes.Scope              |                                   | The scope or category of the uploaded files.              |
| Scopes.MaxFileSize        | 123                               | The maximum size in bytes allowed for each uploaded file. |
| Scopes.AllowedExtensions  | [".jpg", ".pdf", ".png", ".txt"]  | The list of allowed extensions for uploads.               |
| Scopes.AllowAnonymousUpload | true <br> false                 | Indicates whether anonymous uploads are permitted.        |


**Example**

```json title="appsettings.json"
{
  "FileUpload": {
    "RootPath": "attachments",
    "Scopes": [
      {
        "Scope": "quote-attachments",
        "MaxFileSize": 123,
        "AllowedExtensions": [ ".jpg", ".pdf", ".png", ".txt" ]
        "AllowAnonymousUpload": true
      }
    ]
  }
}
```

### FrontendSecurity

This node configures frontend security settings.

|Node                       | Default or sample value  | Description                                                     |
|---------------------------|--------------------------|-----------------------------------------------------------------|
|OrganizationMaintainerRole | Organization maintainer | The role that defines permissions for organization maintainers. |

**Example**

```json title="appsettings.json"
"FrontendSecurity": {
    "OrganizationMaintainerRole": "Organization maintainer"
}
```

### Google

This node is used for authentication with Google OAuth 2.0.

![Readmore](media/readmore.png){: width="25"}  [How to enable authentication with Google OAuth 2.0 in the Platform](../Fundamentals/Security/extensions/adding-google-as-sso-provider.md)

![Readmore](media/readmore.png){: width="25"}  [How to enable authentication with Google OAuth 2.0 in the Frontend Application](../../../../storefront/developer-guide/authentication/adding-google-as-sso-provider)


| Node                   | Default or sample value   | Description                                                                                                       |
| ---------------------- | --------------------------| ----------------------------------------------------------------------------------------------------------------- |
| Enabled                | false<br> true            | Enables authentication with Google OAuth 2.0. By default, this value is **false**, i.e., authentication is disabled. |
| AuthenticationType     | "Google"                  | Provides the authentication scheme. Must always have the **Google** value set.                                    |
| AuthenticationCaption  | "Google"                  | Sets a human-readable caption for the Google authentication provider. Visible on the **Sign In** page.            |
| ClientId               |                           | The Client ID of the Google OAuth 2.0 application. You can find it in the Google Cloud Console under **APIs & Services** --> **Credentials**. |
| ClientSecret           |                           | The Client Secret of the Google OAuth 2.0 application. You can find it in the Google Cloud Console under **APIs & Services** --> **Credentials**. |
| DefaultUserType        | "Manager"                 | Default user type for new users created upon first sign-in by Google accounts.                                    |

**Example**

<!--google-start-->

```json title="appsettings.json"

"Google": {
	"Enabled": true,
	"AuthenticationType": "Google",
	"AuthenticationCaption": "Google",
	"ClientId": "<your Client ID>",
	"ClientSecret": "<your Client Secret>",
	"DefaultUserType": "Manager"
},
```
<!--google-end-->

### IdentityOptions

This configuration node configures the ASP.NET Core Identity system. 

<!--security-start-->

![Readmore](media/readmore.png){: width="25"}  [Identity Configuration](https://github.com/dotnet/AspNetCore.Docs/blob/master/aspnetcore/security/authentication/identity-configuration.md#configure-aspnet-core-identity)

| Node                                      | Default or sample value   | Description                                                                                                            |
| ----------------------------------------- | ------------------------  | ---------------------------------------------------------------------------------------------------------------------- |
| Password                                  |                           | Configuration settings related to user password requirements.                                                          |
| Password:RequiredLength                   | 8                       | The minimum required length for user passwords.                                                                        |
| Password:RequireDigit                     | false                   | Indicates whether a digit is required in user passwords.                                                               |
| Password:RequireNonAlphanumeric           | false                   | Indicates whether a non-alphanumeric character is required in user passwords.                                          |
| Password:RepeatedResetPasswordTimeLimit   | "0:01:0"                | The time span within which a user cannot repeatedly reset their password.                                              |
| User                                      |                           | Configuration settings related to user accounts.                                                                       |
| User:MaxPasswordAge                       | 90                      | The maximum age (in days) a user can keep the same password before being required to change it.                        |
| User:RequireUniqueEmail                   | true                    | Indicates whether each user must have a unique email address.                                                          |
| User:RemindPasswordExpiryInDay            | 7                       | The number of days before the password expiration date when the system will start reminding users to change their password. |
| Lockout                                   |                           | Configuration settings related to account lockout.                                                                      |
| Lockout:DefaultLockoutTimeSpan            | "0:15:0"                 | The default duration for which an account is locked out after the specified number of unsuccessful login attempts.      |


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
<!--security-end-->

### LoginPageUI

This node configures background screen and background pattern of the Login page.

| Node                      | Default or sample value   | Description                                                                                              |
| ------------------------- | ------------------------  | -------------------------------------------------------------------------------------------------------- |
| BackgroundUrl             |                           | Url for the background image of the login page. If empty, no background image is displayed.             |
| PatternUrl                |                           | Url for the pattern image of the login page. If empty, no pattern image is displayed.                   |
| Preset                    |                           | The currently selected preset for the login page. If empty, no preset is applied.                         |
| Presets                   |                           | An array of preset configurations for the login page, allowing different visual settings for different scenarios. |
| Presets:Name              | "demo", "prod"...         | The name of the preset. Used for identification and selection of the preset.                              |
| Presets:BackgroundUrl     |                           | Url for the background image specific to the preset. If empty, the default background is used.          |
| Presets:PatternUrl        |                           | Url for the pattern image specific to the preset. If empty, the default pattern is used.          |


**Example**

```json title="appsettings.json"
    "LoginPageUI": {
        "BackgroundUrl": "",
        "PatternUrl": "",
        "Preset": "",
        "Presets": [
          {
            "Name": "demo",
            "BackgroundUrl": "",
            "PatternUrl": "/images/pattern-demo.svg"
          },
          {
            "Name": "prod",
            "BackgroundUrl": "",
            "PatternUrl": "/images/pattern-live.svg"
          }
        ]
      }
```


### Modularity

This node configures external sources, from which modules are being installed and discovered.

<!--modularity-start-->


| Node                      | Default or sample value                         | Description                                                                                                   |
| ------------------------- | ----------------------------------------------  | ------------------------------------------------------------------------------------------------------------- |
| IncludePrerelease         | true<br>false                                   | Shows module versions marked as **Prerelease** if value is **true**.                                       |
| DiscoveryPath             | "./Modules"                                     | Relative or absolute folder location where the platform will discover the installed modules from.             |
| ModulesManifestUrl        |                                                 | Url to the **.json file** that contains module manifests.                 |
| AuthorizationToken        |                                                 | The authorization token to access **ModulesManifestUrl**, added to the **Authorization** header, if specified.|
| AutoInstallModuleBundles  | "commerce"                                      | Group(s) of modules to install automatically during the initial Platform setup.<br>If you do not need to install anything here, provide an empty array. |

**Example**

```json title="appsettings.json"
  "ExternalModules": {
    "IncludePrerelease": false,
    "ModulesManifestUrl": "https://raw.githubusercontent.com/VirtoCommerce/vc-modules/master/modules_v3.json",
    "AuthorizationToken": "",
    "AutoInstallModuleBundles": [
      "commerce"
    ]
  }
```

<!--modularity-end-->



### Notifications

This node enables notification configuration for the `VirtoCommerce.Notifications` module.

<!--notifications-start-->

| Node                              | Default or sample value         | Description                                                                                                               |
| --------------------------------- | ------------------------------  | ------------------------------------------------------------------------------------------------------------------------- |
| Gateway                           | "Smtp"<br>"SendGrid"            | The current notification sending gateway. The out-of-the-box implemented and supported values are **Smtp**, **SendGrid**.  |
| DefaultSender                     |                                 | This **required** setting provides sender<br>identification used by the current notification sending gateway.           |
| Smtp                              |                                 | SMTP gateway configuration.<br>Used if the **Gateway** setting has the **Smtp** value.                                        |
| Smtp:SmtpServer                   |                                 | The SMTP server address for sending emails.                                                                               |
| Smtp:Port                         |                                 | The port number to use when connecting to the SMTP server.                                                                |
| Smtp:Login                        |                                 | The login (username) for authenticating to the SMTP server.                                                               |
| Smtp:Password                     |                                 | The password for authenticating to the SMTP server.                                                                       |
| Smtp:ForceSslTls                  | true<br>false                   | If **true**, forces the usage of SSL/TLS when connecting to the SMTP server.                                         |
| SendGrid                          |                                 | SendGrid gateway configuration.<br>Used when the **Gateway** setting has the **SendGrid** value.                              |
| SendGrid:ApiKey                   |                                 | The API key for authenticating to the SendGrid service.                                                                   |
| Notifications:DiscoveryPath       |                                 | Relative folder path in the local file system<br>that will be used to discover notification template files<br>during notification rendering. |
| Notifications:FallbackDiscoveryPath|                                | Alternative relative folder path in the local file<br>system that will be used to discover alternative template<br>files during notification rendering.<br>Templates found through this path will be used as a backup,<br>in case the templates defined in the<br>**Notifications:DiscoveryPath** setting are not found. |

**Example**

```json title="appsettings.json"
"Notifications": {
    "Gateway": "Smtp",
    "DefaultSender": "noreply@gmail.com",
    "Smtp": {
      "SmtpServer": "smtp.gmail.com",
      "Port": 587,
      "Login": "",
      "Password": "",
      "ForceSslTls": false
    },
    "SendGrid": {
      "ApiKey": ""
    },
    "Notifications:DiscoveryPath": "Templates",
    "Notifications:FallbackDiscoveryPath": ""
}
```

<!--notifications-end-->


### Payments

The Payments node configures various payment gateway integrations for the Virto Commerce platform. This section includes settings for modules such as Authorize.Net and Skyflow, enabling secure payment processing and integration with different payment service providers.

| Node            | Default or sample value               | Description                                                         |
| --------------- | ------------------------------------- | ------------------------------------------------------------------- |
| AuthorizeNet    |                                       | Configuration settings for the Authorize.Net payment gateway.       |
| Skyflow         |                                       | Configuration settings for the Skyflow payment processing module.   |


#### Authorize.Net

This node configures the Authorize.Net payment gateway integration, enabling secure payment processing using Accept.js and the Authorize.Net API. Confidential Authorize.Net account settings should be configured in appsetting.json.

![Readmore](media/readmore.png){: width="25"} [Configuring non-confidential settings](../../../user-guide/authorize-net/manage-authorize-net-module#configure-settings)


<!--authorize-net-start-->

| Node            | Default or sample value           | Description                                                      |
| --------------- | ----------------------------------| ---------------------------------------------------------------- |
| IsActive      | true<br>false                       | Toggle to enable or disable the Authorize.Net payment module.     |
| ApiLogin      | "YourApiLogin"                      | The API login ID provided by Authorize.Net.                       |
| TxnKey        | "YourTransactionKey"                | The transaction key provided by Authorize.Net.                    |


**Example**

```json title="appsettings.json"
"Payments": {
    "AuthorizeNet": {
        "IsActive": true,
        "ApiLogin": "YourApiLogin",
        "TxnKey": "YourTransactionKey",
    }
}
```

<!--authorize-net-end-->

#### Skyflow

This node configures the Skyflow payment processing module, facilitating secure handling of payment data and integration with various payment service providers.

<!--skyflow-start-->

| Node                             | Default or sample value    | Description                                                                        |
| -------------------------------- |--------------------------- | ---------------------------------------------------------------------------------- |
| tokenURI                         |                            | The URI for obtaining authentication tokens from the Skyflow API. Can be taken from credentials.json file downloaded from Skyflow dashboard. |
| vaultURI                         |                            | The URI for the Skyflow vault. Can be taken from Skyflow studio by clicking three dots on the vault and selecting **View details** action.  |
| gatewayURI                       |                            | The URI for invoking outbound connection rules. Replace **vault** with **gateway** in the **vaultURI**. |
| vaultId                          |                            | The identifier for the Skyflow vault.                                              |
| tableName                        |                            | The table name for storing credit card data.                                       |
| PaymentFormAccount               |                            | Service account configuration section with credentials taken from the Skyflow service account configuration in the previous steps. |
| PaymentFormAccount:clientID      |                            | The client ID for authentication with the Skyflow Payment Form account.            |
| PaymentFormAccount:keyID         |                            | The key ID for authentication with the Skyflow Payment Form account.               |
| PaymentFormAccount:privateKey    |                            | The private key for authentication with the Skyflow Payment Form account.          |
| IntegrationsAccount              |                            | Service account configuration section with credentials taken from the Skyflow service account configuration in the previous steps. | 
| IntegrationsAccount:clientID     |                            | The client ID for authentication with the Skyflow Integrations account.            |
| IntegrationsAccount:keyID        |                            | The key ID for authentication with the Skyflow Integrations account.               |
| IntegrationsAccount:privateKey   |                            | The private key for authentication with the Skyflow Integrations account.          |
| TargetPaymentMethod              | "AuthorizeNetPaymentMethod"| The payment method used for authorizing payments via Skyflow. To outbound Payment Service Provider API through the Skyflow connection, create an HttpClient instance IHttpServiceFactory.CreateClient("Skyflow") and execute the request to the Payment Service API with the tokenized card data.                       |
| TargetConnectionRoute            |                            | The connection route for the target payment method.                                |


!!! note
    To execute the outbound Payment Service Provider API through Skyflow connection, create an HttpClient instance IHttpServiceFactory.CreateClient("Skyflow") and execute the request to the Payment Service API with the tokenized card data. 
    
    ??? "See code example"
        ```
        public override PostProcessPaymentRequestResult PostProcessPayment(PostProcessPaymentRequest request)
            {
        ....
              if (request.Parameters["CreditCard"] != null)
              {
                  var tokenizedCard = JsonConvert.DeserializeObject<dynamic>(request.Parameters["CreditCard"]);
                  creditCard = new AuthorizeNetCreditCard
                  {
                      CardCode = tokenizedCard.Cvv,
                      CardNumber = tokenizedCard.CardNumber,
                      ExpirationDate = tokenizedCard.CardExpiration,
                      ProxyEndpointUrl = request.Parameters["ProxyEndpointUrl"],
                      ProxyHttpClientName = request.Parameters["ProxyHttpClientName"]
                  };

                  using var stream = new MemoryStream();
                  var proxyHttpClient = _httpClientFactory.CreateClient(request.CreditCard.ProxyHttpClientName);
                  var xmlSerializer = new XmlSerializer(typeof(AuthorizeNetCreateTransactionRequest));
                  using var xmlWriter = XmlWriter.Create(stream, new XmlWriterSettings
                  {
                      Encoding = new UTF8Encoding(false, true), //Exclude BOM
                      Indent = true,
                  });
                  xmlSerializer.Serialize(xmlWriter, this);
                  using var content = new StreamContent(stream);
                  content.Headers.ContentType = new MediaTypeHeaderValue(MediaTypeNames.Application.Xml);
                  var proxyRequest = new HttpRequestMessage(HttpMethod.Post, new Uri(request.CreditCard.ProxyEndpointUrl))
                  {
                      Content = content
                  };
                  var response = proxyHttpClient.Send(proxyRequest);
              }
        ```

**Example**

```json title="appsettings.json"
{
  "Payments": {
    "Skyflow": {
      "tokenURI": "https://manage.skyflowapis-preview.com/v1/auth/sa/oauth/token",
      "vaultURI": "https://a370a9658141.vault.skyflowapis-preview.com",
      "gatewayURI": "https://a370a9658141.gateway.skyflowapis-preview.com",
      "vaultId": "ff9fc275bec848318361cc8928e094d1",
      "tableName": "credit_cards",
      "PaymentFormAccount": {
        "clientID": "j873500104e6439bbbeb8cec63a6d21",
        "keyID": "a70d977de5f24532810df376585031aa",
        "privateKey": "-----BEGIN PRIVATE KEY-----Base64-----END PRIVATE KEY-----"
      },
      "IntegrationsAccount": {
        "clientID": "b47bea9c61c74cf4aac3b26d09aaf825",
        "keyID": "c950c459157548f0817500288ec8ac96",
        "privateKey": "-----BEGIN PRIVATE KEY-----Base64-----END PRIVATE KEY-----"
      },
      "TargetPaymentMethod": "AuthorizeNetPaymentMethod",
      "TargetConnectionRoute": "b47bea9c61c74cf4aac3b26d09aaf825/xml/v1/request.api"

    }
  }
}
```

<!--skyflow-end-->


### PlatformSettings

This node is used for Used for platform settings overriding.

|Node           | Default or sample value   | Description  |
| ------------- | ------------------------  | ------------ |
| Settings      |                           | Array of settings to be overridden. These settings will be read only in the admin panel.|

**Example**

```json title="appsettings.json"
"Settings":{
  "ItHasValues": true,
  "Value": 20000,
  "RestartRequired": false,
  "ModuleId": "VirtoCommerce.Sitemaps",
  "GroupName": "Sitemap|General",
  "Name": "Sitemap.RecordsLimitPerFile",
  "IsRequired": false,
  "IsHidden": false,
  "ValueType": 8,
  "DefaultValue": 10000,
  "IsDictionary": false
}
```

### PushMessages

This node configures the push notification settings for the Virto Commerce Push Messages` module using Firebase Cloud Messaging (FCM).

| Node                        | Sample value                                                      | Description                                                                 |
|-----------------------------|------------------------------------------------------------------ |-----------------------------------------------------------------------------|
| UseFirebaseCloudMessaging   | true<br> false                                                    | This **required** setting enables/disables Firebase Cloud Messaging.        |
| FcmSenderOptions            |                                                                   | Configuration settings for the FCM sender account.                          |
|    Type                     | "service_account"                                                 | The type of the FCM sender account.                                         |
|    ProjectId                |                                                                   | The project ID of the FCM project.                                          |
|    PrivateKeyId             |                                                                   | The private key ID for the FCM service account.                             |
|    PrivateKey               |                                                                   | The private key for the FCM service account.                                |
|    ClientEmail              |                                                                   | The client email for the FCM service account.                               |
|    ClientId                 |                                                                   | The client ID for the FCM service account.                                  |
|    AuthUri                  | "https://accounts.google.com/o/oauth2/auth"                       | The authentication URI for the FCM service account.                         |
|    TokenUri                 | "https://oauth2.googleapis.com/token"                             | The token URI for the FCM service account.                                  |
|    AuthProviderX509CertUrl  | "https://www.googleapis.com/oauth2/v1/certs"                      | The URL for the X509 certificate provider.                                  |
|    ClientX509CertUrl        |                                                                   | The URL for the client X509 certificate.  |
|    UniverseDomain           |                                                                   | The domain used by the FCM service account.                                 |
| FcmReceiverOptions          |                                                                   | Configuration settings for the FCM receiver account.                        |
|    ApiKey                   |                                                                   | The API key for the FCM receiver.                                           |
|    AuthDomain               |                                                                   | The authentication domain for the FCM receiver.                             |
|    ProjectId                |                                                                   | The project ID for the FCM receiver.                                        |
|    StorageBucket            |                                                                   | The storage bucket for the FCM receiver.                                    |
|    MessagingSenderId        |                                                                   | The messaging sender ID for the FCM receiver.                               |
|    AppId                    |                                                                   | The application ID for the FCM receiver.                                    |
|    VapidKey                 |                                                                   | The VAPID key for the FCM receiver.               |

**Examples**

```json title="appsettings.json"
{
  "PushMessages": {
    "UseFirebaseCloudMessaging": true,
    "FcmSenderOptions": {
      "Type": "service_account",
      "ProjectId": "vc-push-86046",
      "PrivateKeyId": "956335b2eeccd3b37ef8f6871b406a6a31e1b29a",
      "PrivateKey": "-----BEGIN PRIVATE KEY-----\n…-----END PRIVATE KEY-----\n",
      "ClientEmail": "firebase-adminsdk-5gw7s@vc-push-86046.iam.gserviceaccount.com",
      "ClientId": "117271734888260111772",
      "AuthUri": "https://accounts.google.com/o/oauth2/auth",
      "TokenUri": "https://oauth2.googleapis.com/token",
      "AuthProviderX509CertUrl": "https://www.googleapis.com/oauth2/v1/certs",
      "ClientX509CertUrl": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-5gw7s%40vc-push-86046.iam.gserviceaccount.com",
      "UniverseDomain": "googleapis.com"
    },
    "FcmReceiverOptions": {
      "ApiKey": "AIzaSyCy9gsvKM1e77GRYw6M9rKRRSekZNAgRnI",
      "AuthDomain": "vc-push-86046.firebaseapp.com",
      "ProjectId": "vc-push-86046",
      "StorageBucket": "vc-push-86046.appspot.com",
      "MessagingSenderId": "647691501458",
      "AppId": "1:647691501458:web:2b18fc3a864469ac378b4b",
      "VapidKey": "BJyVagnZqcHI6_vwxILEfxpbVAq0F-ASE5k3WwX_F72WaQr_ysHKqhH5-8yWfUhNs9oecGcOy8kJ_m4b-OXrNFs"
    }
  }
}
```

### PushNotifications

This node configures the push notification service settings for scalability in the Virto Commerce platform.

| Node               | Default or sample value                                   | Description                                                                                                               |
|--------------------|-----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| ScalabilityMode    | "None"                                                    | Specifies the scalability mode for notifications. Possible values are `RedisBackplane`, `AzureSignalRService`, or `None`. |
| HubUrl             | "https://localhost:5001/pushNotificationHub"              | The URL for connecting to the platform's SignalR `/pushNotificationHub` as a client. This is used for syncing local notifications with other platform instances.  |
| ForceWebSockets    | false                                                     | Forces the use of WebSockets for notification exchange. The host environment must support WebSockets.                     |
| AzureSignalRService.ConnectionString | "Endpoint=https://{app name}.service.signalr.net;AccessKey={access key};Version=1.0;" | The connection string for Azure SignalR Service, specifying the endpoint and access key. |
| RedisBackplane.ChannelName          | "VirtoCommerceChannel"                              | The name of the channel for Redis backplane, used for scaling notifications across instances.                  |

**Example**

```json title="appsettings.json"
{
  "VirtoCommerce": {
    "PushNotifications": {
      "ScalabilityMode": "None",
      "HubUrl": "https://localhost:5001/pushNotificationHub",
      "ForceWebSockets": false,
      "AzureSignalRService": {
        "ConnectionString": "Endpoint=https://{app name}.service.signalr.net;AccessKey={access key};Version=1.0;"
      },
      "RedisBackplane": {
        "ChannelName": "VirtoCommerceChannel"
      }
    }
  }
}
```

### Search

This node configures full text search for the `VirtoCommerce.Search` module.

<!--search-start-->

| Node                        | Default or sample value   | Description                                                                                       |
| ----------------------------| ------------------------- | ------------------------------------------------------------------------------------------------- |
| Provider                    | "Lucene"<br>"ElasticSearch"<br>"ElasticAppSearch"<br>"ElasticSearch8"<br>"AzureSearch"<br>"AlgoliaSearch"                     | This **required** setting specifies the current search provider.  |
| Scope                       | "default"               | This setting determines the scope to use and is **required**.                                                                                 |


**Examples**

Configure the search provider modules and activate them in the `Search.Provider` section, providing connection parameters as specified in the module documentation:

```json title="appsettings.json"
"Search": {
		"Provider": "ElasticAppSearch",
		"Scope": "default",
		"ElasticAppSearch": {
      "Endpoint": "https://localhost:3002",
			"PrivateApiKey": "private-key",
		  "KibanaBaseUrl": "https://localhost:5601"
		}
	}
```

Tailor the search provider per document type to optimize search performance and functionality:

```json title="appsettings.json"
{
  "Search": {
    "Provider": "ElasticAppSearch",
    "DocumentScopes": [
      {
        "DocumentType": "Category",
        "Provider": "ElasticSearch8"
      }
    ]
  }
}
```
<!--search-end-->


#### ElasticSearch

This node configures the Elastic Search provider:

<!--elasticsearch-start-->

| Node                                       | Default or sample value                    | Description                                                                     |
| -------------------------------------------| -------------------------------------------| -------------------------------------------------------------------------------|
| Search.Provider                            | "ElasticSearch"                             | Specifies the search provider name.       |
| Search.Scope                               | "default"                                   | Specifies the common name (prefix) for all indexes. Each document type is stored in a separate index, and the full index name is **scope-{documenttype}**. This allows one search service to serve multiple indexes. The key is optional. Its default value is **default**.|
| Search.ElasticSearch.Server                |                                             | Specifies the network address and port of the Elasticsearch server.               |
| Search.ElasticSearch.User                  | "elastic"                                   | Specifies the username for either the Elastic Cloud cluster or private Elasticsearch server. |
| Search.ElasticSearch.Key                   |                                             | (Optional) Specifies the password for either the Elastic Cloud cluster or private Elasticsearch server. |
| Search.ElasticSearch.EnableCompatibilityMode | true<br>false                             | (Optional) Set this to **true** to use Elasticsearch v8.x or **false** (default) for earlier versions. |
| Search.ElasticSearch.EnableHttpCompression | true<br>false                               | (Optional) Set this to **true** to enable gzip compressed requests and responses or **false** (default) to disable compression. |
| Search.ElasticSearch.CertificateFingerprint |                                            | During development, you can provide the server certificate fingerprint. When present, it is used to validate the certificate sent by the server. The fingerprint is expected to be the hex string representing the SHA256 public key fingerprint.  |

**Examples**

=== "Elastic Cloud v8.x"

    !!! note
        Virto Commerce has its native [Elasticsearch 8.x module](https://github.com/VirtoCommerce/vc-module-elastic-search-8). The current module works with Elasticsearch 8.x in compatibility mode.

    Enable the compatibility mode for Elastic Cloud v8.x:

    ```json title="appsettings.json"
    "Search": {
        "Provider": "ElasticSearch",
        "Scope": "default",
        "ElasticSearch": {
            "EnableCompatibilityMode": "true",
            "Server": "https://4fe3ad462de203c52b358ff2cc6fe9cc.europe-west1.gcp.cloud.es.io:9243",
            "User": "elastic",
            "Key": "{SECRET_KEY}"
        }
    }
    ```

=== "Elasticsearch v8.x"

    Configure Elasticsearch v8.x without security features enabled:

    ```json title="appsettings.json"
    "Search": {
        "Provider": "ElasticSearch",
        "Scope": "default",
        "ElasticSearch": {
            "EnableCompatibilityMode": "true",
            "Server": "https://localhost:9200"
        }
    }
    ```

    Configure Elasticsearch v8.x with ApiKey authorization:

    ```json title="appsettings.json"
    "Search": {
        "Provider": "ElasticSearch",
        "Scope": "default",
        "ElasticSearch": {
            "EnableCompatibilityMode": "true",
            "Server": "https://localhost:9200",
            "User": "{USER_NAME}",
            "Key": "{SECRET_KEY}"
        }
    }
    ```

=== "Elastic Cloud v7.x"

    Configure Elastic Cloud v7.x as follows:

    ```json title="appsettings.json"
    "Search": {
        "Provider": "ElasticSearch",
        "Scope": "default",
        "ElasticSearch": {
            "Server": "https://4fe3ad462de203c52b358ff2cc6fe9cc.europe-west1.gcp.cloud.es.io:9243",
            "User": "elastic",
            "Key": "{SECRET_KEY}"
        }
    }
    ```

=== "Elasticsearch v7.x"

    Configure Elasticsearch v7.x without security features enabled:

    ```json title="appsettings.json"
    "Search": {
        "Provider": "ElasticSearch",
        "Scope": "default",
        "ElasticSearch": {
            "Server": "https://localhost:9200"
        }
    }
    ```

    Configure Elasticsearch v7.x with ApiKey authorization:

    ```json title="appsettings.json"
    "Search": {
        "Provider": "ElasticSearch",
        "Scope": "default",
        "ElasticSearch": {
            "Server": "https://localhost:9200",
            "User": "{USER_NAME}",
            "Key": "{SECRET_KEY}"
        }
    }
    ```

=== "Amazon OpenSearch Service"

    Configure Amazon OpenSearch Service:

    ```json title="appsettings.json"
    "Search": {
        "Provider": "ElasticSearch",
        "Scope": "default",
        "ElasticSearch": {
            "Server": "https://{master-user}:{master-user-password}@search-test-vc-c74km3tiav64fiimnisw3ghpd4.us-west-1.es.amazonaws.com"
        }
    }
    ```

<!--elasticsearch-end-->


#### Elastic App Search

This node configures the Elastic App Search provider:

<!--elasticappsearch-start-->


| Node                                       | Default or sample value                    | Description                                                                    |
| -------------------------------------------| -------------------------------------------| -------------------------------------------------------------------------------|
| Search.Provider                            | "ElasticAppSearch"                       | Name of the search provider.           |
| Search.Scope                               | "default"                                | (Optional) Specifies the common name (prefix) for all indexes. Each document type is stored in a separate index, and the full index name is **scope-{documenttype}**. This allows one search service to serve multiple indexes. Its default value is set to **default**.|
| Search.ElasticAppSearch.Endpoint           |                                            | Network address and port of the ElasticAppSearch server. |
| Search.ElasticAppSearch.PrivateApiKey      |                                            | API access key that can read and write against all available API endpoints. Prefixed with **private-**.|
| Search.ElasticAppSearch.KibanaBaseUrl      |                                            | Kibana base URL for accessing the Kibana Dashboard from the application menu.|
| Search.ElasticAppSearch.KibanaPath         |                                            | Path to the App Search engine in the Kibana Dashboard. Default value is **/app/enterprise_search/app_search/engines/**.

!!! note
    Endpoint and API key can be managed in the Credential menu within the App Search Dashboard panel.

**Examples**

```json title="appsettings.json"
	"Search": {
		"Provider": "ElasticAppSearch",
		"Scope": "default",
		"ElasticAppSearch": {
				"Endpoint": "https://localhost:3002",
			"PrivateApiKey": "private-key",
		  "KibanaBaseUrl": "https://localhost:5601"
		}
	}
```
##### Dynamic Boosting

The Elastic App Search provider combines static boosting from the Search Relevance Tuning panel with dynamic boosting that can be passed at runtime.

Dynamic Boosting supports both Value Boost and Functional Boosting.

Define Boost Presets as follows:

```json title="appsettings.json"
	"Search": {
		"Provider": "ElasticAppSearch",
		"Scope": "default",
		"ElasticAppSearch": {
		  "Endpoint": "https://localhost:3002",
		  "PrivateApiKey": "private-key",
		  "KibanaBaseUrl": "https://localhost:5601",

		  "BoostPresets": [
			{
			  "Name": "High",
			  "Type": "value",
			  "Operation": "add",
			  "Factor": 5,
			  "IsDefault": true
			},
			{
			  "Name": "Medium",
			  "Type": "value",
			  "Operation": "add",
			  "Factor": 3
			},
			{
			  "Name": "LOw",
			  "Type": "value",
			  "Operation": "add",
			  "Factor": 3
			}
		  ]
		}
	  }
```    

Pass SearchBoost with Search Request:

```json title="appsettings.json"
searchRequest.Boosts = [new SearchBoost
	  {
				FieldName = "brand",
				Value = "Apple",
				Preset = "Medium",
		}];
```

<!--elasticappsearch-end-->


#### Elastic Search 8

This node configures the Elastic Search 8 provider:

<!--elasticsearch8-start-->


| Node                                       | Default or sample value                    | Description                                                                      |
| -------------------------------------------| -------------------------------------------| ---------------------------------------------------------------------------------|
| Search.Provider                            | "ElasticSearch8"                         | Specifies the search provider name.       |
| Search.Scope                               | "default"                                | (Optional) Specifies the common name (prefix) for all indexes. Each document type is stored in a separate index, and the full index name is **scope-{documenttype}**. This allows one search service to serve multiple indexes. Its default value is **default**.                                         |
| Search.ElasticSearch8.Server                |                                           | Specifies the network address and the port of the Elasticsearch8 server.         |
| Search.ElasticSearch8.User                  | "elastic"                                 | Specifies the username for the Elasticsearch8 server.                            |
| Search.ElasticSearch8.Key                   |                                           | (Optional) Specifies the password for the Elasticsearch8 server.                 |
| Search.ElasticSearch8.CertificateFingerprint |                                          | (Optional) During development, you can provide the server certificate fingerprint. When present, it is used to validate the certificate sent by the server. The fingerprint is expected to be the hex string representing the SHA256 public key fingerprint.                                         |

**Examples**

Configure local v8.x server:

```json title="appsettings.json"
"Search": {
    "Provider": "ElasticSearch8",
    "Scope": "default",
    "ElasticSearch8": {
        "Server": "https://localhost:9200",
        "User": "elastic",
        "Key": "{PASSWORD}"
    }
}
```

Configure Elastic Cloud v8.x:

```json title="appsettings.json"
"Search": {
    "Provider": "ElasticSearch8",
    "Scope": "default",
    "ElasticSearch8": {
        "Server": "https://vcdemo.es.eastus2.azure.elastic-cloud.com",
        "User": "elastic",
        "Key": "{SECRET_KEY}"
    }
}
```

<!--elasticsearch8-end-->


#### Lucene

This node configures the Lucene search provider:

<!--lucene-start-->

| Node                                       | Default or sample value                    | Description                                                                    |
| -------------------------------------------| -------------------------------------------| -------------------------------------------------------------------------------|
| Search.Provider                            | "Lucene"                                   | Name of the search provider.                    |
| Search.Lucene.Path                         |                                            | A virtual or physical path to the root directory where indexed documents are stored.
| Search.Scope                               | "default"                                  | (Optional) Specifies the common name (prefix) for all indexes. Each document type is stored in a separate index, and the full index name is **scope-{documenttype}**. This allows one search service to serve multiple indexes. |

**Example**

```json title="appsettings.json"
"Search": {
    "Provider": "Lucene",
    "Scope": "default",
    "Lucene": {
        "Path": "/path/to/lucene/indexes"
    }
}
```

<!--lucene-end-->

#### Azure Search

This node configures the Azure Search provider:

<!--azuresearch-start-->

| Node                                       | Default or sample value                    | Description                                                                    |
| -------------------------------------------| -------------------------------------------| -------------------------------------------------------------------------------|
| Search.Provider                            | "AzureSearch"                              | Name of the search provider.               |
| Search.AzureSearch.SearchServiceName       |                                            | The name of the search service instance in your Azure account. Example: SERVICENAME.search.windows.net.|
| Search.AzureSearch.AccessKey               |                                            | The primary or secondary admin key for this search service.                    |
| Search.AzureSearch.QueryParserType         | Simple<br>Full                         | Type of Query Languages. **Simple** (default) or **Full**.                         |                
| Search.Scope                               | "default"                                  | (Optional) Specifies the common name (prefix) for all indexes. Each document type is stored in a separate index, and the full index name is **scope-{documenttype}**. This allows one search service to serve multiple indexes. |


**Example**

```json title="appsettings.json"
"Search": {
    "Provider": "AzureSearch",
    "Scope": "default",
    "AzureSearch": {
        "SearchServiceName": "YOUR_SEARCH_SERVICE_NAME.search.windows.net",
        "AccessKey": "YOUR_SEARCH_SERVICE_ACCESS_KEY",
        "QueryParserType": "Simple"
    }
}
```

<!--azuresearch-end-->


#### Algolia

This node configures the Algolia search provider:

<!--algolia-start-->

| Node                                       | Default or sample value                    | Description                                                                    |
| -------------------------------------------| -------------------------------------------| -------------------------------------------------------------------------------|
| Search.Provider                            | "AlgoliaSearch"                            | Name of the search provider.             |
| Search.AlgoliaSearch.ApiId                 |                                            | The API id for Algolia server.                                                 |
| Search.AlgoliaSearch.ApiKey                |                                            | The API key for either Algolia server.                                         |


**Example**

```json title="appsettings.json"
"AlgoliaSearch": {
    "AppId": "API_ID",
    "ApiKey": "API_KEY"
}
```

<!--algolia-end-->


#### SecurityHeaders

This node configures security-related HTTP headers in the Virto Commerce platform.

| Node           | Default or sample value | Description                                                                                                       |
|----------------|-------------------------|-------------------------------------------------------------------------------------------------------------------|
| FrameOptions   | "Deny"                  | Specifies the `X-Frame-Options` header configuration. Allowed values are `Deny` (default), `SameOrigin`, or a custom URI.|
| FrameAncestors | "None"                  | Configures the `FrameAncestors` directive within the `Content-Security-Policy` header. Allowed values are `None` (default), `Self`, or a custom URI. |

**Example**

```json title="appsettings.json"
{
  "VirtoCommerce": {
    "SecurityHeaders": {
      "FrameOptions": "Deny",
      "FrameAncestors": "None"
    }
  }
}
```

### Serilog

This node configures the Serilog logging library, allowing customization of logging providers, minimum severity levels, and other logging-related settings.

| Node          | Default or sample value                                             | Description                                                                      |
| ------------- | ------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Using         | "Serilog.Sinks.Console"<br>"Serilog.Sinks.Debug"                    | List of assemblies for logging providers in which<br>configuration methods reside.  |
| MinimumLevel  | Information<br> Warning <br> Error <br> Debug <br> Trace            | Minimum severity level of log messages.                                          |
| WriteTo       | "Console" <br> "Debug"                                              | Specifies the sinks to which log events will be written.                           |
| Enrich        | "FromLogContext"                                                    | List of enrichers that will add additional properties to log events.               |

**Example**

```json title="appsettings.json"
"Serilog": {
    "Using": [
      "Serilog.Sinks.Console",
      "Serilog.Sinks.Debug"
    ],
    "MinimumLevel": {
      "Default": "Information"
    },
    "WriteTo": [
      "Console",
      "Debug"
    ],
    "Enrich": [
      "FromLogContext"
    ]
}
```


### Tax

This setting is used to configure tax providers.

| Node                    | Default value             | Description                                                                                           |
|-------------------------|---------------------------|-------------------------------------------------------------------------------------------------------|
| FixedRateTaxProvider  | true<br>false         | Determines whether the **FixedRateTaxProvider** is enabled or disabled. When set to **false**, the **FixedRateTaxProvider** is not active, and tax calculations will not be performed using this provider. When set to **true** the **FixedRateTaxProvider** will be enabled, allowing the platform to use fixed-rate tax calculations. |

**Example**

```json title="appsettings.json"
{
"FixedRateTaxProvider": {"Enabled": false}
}
```


## Hierarchic Keys and Separators

When working with keys, one should follow these rules:

* Within the Configuration API, a colon separator (`:`) works on all platforms.
* In environment variables, a colon separator may not work on all platforms. A double underscore, `__`, is supported by all platforms and is automatically converted into a colon `:`.
* In Azure Key Vault, hierarchic keys use double hyphen `--` as a separator. The Azure Key Vault configuration provider automatically replaces `--` with a `:` when the secrets are loaded into the app configuration.

??? Example "Configuring ElasticSearch on localhost in the `appsettings.json` file"
    ![Configuration with the appsettings.json file](media/01-configuring-with-appsettings.png)


??? Example "Configuring `VirtoCommerce ConnectionString` and other settings through **environment variables** in the **docker-compose.yml** file"
    ![Configuring the environment variables with Docker)](media/02-configuring-docker.png)

??? Example "Configuring `AzureSearch` and other settings trough the **Application settings** in **Azure**"
    ![Application settings in Azure](media/03-app-settings-azure.png)

![Readmore](media/readmore.png){: width="25"} [ASP.NET configuration guide](https://docs.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-3.1#configuration-keys-and-values)

