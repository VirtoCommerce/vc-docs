# Configure Environments for Comparison

With the **Environments Compare (Environments Comparison)** module you can compare platform settings, environment configurations, and system information across multiple Virto Commerce environments (development, staging, production, etc.). 

![Read more](media/readmore.png){: width="20"} [Environments comparison](../../../../user-guide/environments-comparison/overview)

To start comparing environments:

1. [Check your prerequisites.](#prerequisites)
1. [Configure your environments.](#configure-environments)

## Prerequisites

Before configuring the Environments Compare module, ensure you have:

* At least two running Virto Commerce environments with the Environments Compare module installed on each.
* The main environment (from which comparisons are performed) has network access to secondary environments via HTTP/HTTPS protocol.
* Valid URLs for all secondary environments that will be compared.

## Configure environments

To compare two environments you must configure:

* [The main environment](#configure-main-environment), which initiates and displays comparisons.
* [One or more secondary environments](#configure-secondary-environment), which expose their settings for comparison.

### Configure main environment

!!! note
    We recommend to keep ApiKey and URL in a secure storage for security reasons.

You can configure the main environment using either **appsettings.json** or deployment configuration files (**.yml**), depending on your deployment model.


=== "appsettings.json"

    On the main environment (the environment from which you will perform comparisons), configure the list of secondary environments to compare in the **appsettings.json** file:

    ```json title="appsettings.json"
    {
    "EnvironmentsCompare": {
        "CurrentEnvironmentName": "Production",
        "ComparableEnvironments": [
        {
            "Name": "QA",
            "Url": "https://qa.mydomaim.com",
            "ApiKey": "a4a86441-cabb-4a60-af90-9c6ebe11a401"
        },
        {
            "Name": "Development",
            "Url": "https://dev.mydomaim.com",
            "ApiKey": "a4a86441-cabb-4a60-af90-9c6ebe11a401"
        }
        ]
    }
    }
    ```

=== ".yml files"

    For deployment configuration files (**.yml** format), use the following structure:

    ```yaml
    EnvironmentsCompare__CurrentEnvironmentName=Production
    EnvironmentsCompare__ComparableEnvironments__0__Name: QA
    EnvironmentsCompare__ComparableEnvironments__0__Url: https://qa.mydomaim.com
    EnvironmentsCompare__ComparableEnvironments__0__ApiKey: a4a86441-cabb-4a60-af90-9c6ebe11a401
    EnvironmentsCompare__ComparableEnvironments__1__Name: Development
    EnvironmentsCompare__ComparableEnvironments__1__Url: https://dev.mydomaim.com
    EnvironmentsCompare__ComparableEnvironments__1__ApiKey: a4a86441-cabb-4a60-af90-9c6ebe11a401
    ```


    | Parameter | Description                                                                                   |
    | --------- | --------------------------------------------------------------------------------------------- |
    | Name      | A descriptive name for the environment, for example Staging, Production, or Development       |
    | Url       | The base URL of the secondary environment, which must be accessible from the main environment |
    | ApiKey    | The API key used to authenticate a Virto Commerce Platform user on the secondary environment  |


### Configure secondary environment

Each secondary environment must explicitly allow configuration access from the main environment.

On every secondary environment to be compared:

* Create **Environments compare** role with **environments-compare:read** permission.
* Create an account assigned to the **EnvironmentsCompare** role.
* Create API keys for user.

## Configure comparison scope

By default, the module has a whitelist of **appsettings.json** sections and keys that are compared across environments.

You can extend or narrow down which **appsettings.json** sections and keys are compared by configuring `EnvironmentsCompare:WhiteList`.

The whitelist supports two levels of filtering:

* `SectionKeys`: Controls which top-level configuration sections from **appsettings.json** are considered during comparison
* `SettingKeys`: Controls which individual configuration keys are treated as public (non-sensitive) and can be compared

For both levels, you can define:

* `Include`: Explicitly allows specific sections or keys.
* `Exclude`: Explicitly omits sections or keys from comparison.

```json title="appsettings.json"
{
  "EnvironmentsCompare": {
    "WhiteList": {
      "SectionKeys": {
        "Include": [ "Logging", "ConnectionStrings" ],
        "Exclude": [ "Notifications" ]
      },
      "SettingKeys": {
        "Include": [ "LoginPageUI:BackgroundUrl" ],
        "Exclude": [ "Assets:AzureBlobStorage:CdnUrl" ]
      }
    }
  }
}
```

This configuration allows you to precisely control the comparison surface. It ensures meaningful visibility into configuration differences and keeps sensitive values protected.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../migration-to-new-xapi-modules">← Migration to new xAPI modules </a>
    <a href="../../../Updating-Virto-Commerce-Based-Project/release-strategy-overview">Release strategy  →</a>
</div>