# Upgrading to Virto Commerce on .NET 10

Virto Commerce on NET 10 (3.1000+) introduces a significant technical update by transitioning the platform to .NET 10.
This update focuses on:

* **Enhanced performance**: The compiler in .NET 10 includes significant enhancements that improve performance through better code generation and optimization strategies.
* **Stability**: This updates offers fewer disruptions, improved error handling, and increased overall system stability.

It involves updating the Target Framework to .NET 10 and integrating the latest LTS releases of third-party libraries. 

!!! note
    No code refactoring or alterations to the API and internal structure have been made.

The release has undergone extensive testing, including unit, end-to-end, regression, and performance tests to ensure a seamless transition as well as for other stable releases.

![Read more](media/readmore.png){: width="20"} [What's new in NET10](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-10/overview)

![Read more](media/readmore.png){: width="20"} [What's new in EF 10 Core](https://learn.microsoft.com/en-us/ef/core/what-is-new/ef-core-10.0/whatsnew)

![Read more](media/readmore.png){: width="20"} [What's new in ASP.NET Core 10](https://learn.microsoft.com/en-us/aspnet/core/release-notes/aspnetcore-10.0)

## Virto Commerce update path

1. Install **.NET 10**. Begin by ensuring that you have .NET 10 installed on your system. Follow the [official installation guidelines](https://dotnet.microsoft.com/en-us/download/dotnet/10.0) to set up the environment for the upgrade. 
1. Update Virto Commerce Platform to **v3.1000** or higher.
1. Update [**Customer**](https://github.com/VirtoCommerce/vc-module-customer) and [**xAPI**](https://github.com/VirtoCommerce/vc-module-x-api) modules to **v3.1000** or higher.
1. Update other Virto Commerce modules to [Stable Release 12](https://docs.virtocommerce.org/platform/user-guide/1.0/versions/v3-2025-S12/) and higher. 

!!! note
    By default, Virto Commerce Platform on .NET10 is backwards compatible with previous platform stable releases on .NET8 (3.800+). However, it is recommended to update custom modules to the latest versions to leverage new features and improvements.

## Known limitations and breaking changes

This section outlines known limitations and breaking changes introduced with the .NET 10 upgrade that may require adjustments to existing solutions or custom module.

### Updated MySQL Provider

Virto Commerce uses **Pomelo.EntityFrameworkCore.MySql 9.0.0** for MySql.

### EF Core 9: Strict validation of pending model changes

Starting with EF Core 9.0, the runtime enforces stricter validation of entity models. If there are model changes that are not reflected in the latest migration, an exception is thrown when executing:

* `dotnet ef database update`
* `Migrate`
* `MigrateAsync`

When pending model changes are detected, the following exception is raised: The model for context `DbContext` has pending changes.

Add a new migration before updating the database. This behavior replaces the previous warning-based approach.

Forgetting to add a migration after modifying the data model is a common source of runtime inconsistencies that can be difficult to diagnose. By failing fast, EF Core ensures that the application model and database schema remain synchronized after migrations are applied.

The exception can be suppressed or downgraded to a warning by handling the `RelationalEventId.PendingModelChangesWarning` event via:

* `DbContext.OnConfiguring`, or
* `AddDbContext configuration`

![Read more](media/readmore.png){: width="20"} [PendingModelChangesWarning in .NET 10 (EF Core 10) - what happened, how we diagnosed it](https://www.virtocommerce.org/t/pendingmodelchangeswarning-in-net-10-ef-core-10-what-happened-how-we-diagnosed-it/817). 

### Upgraded Microsoft.OpenApi

Virto Commerce updated Microsoft.OpenApi from version 1.0.0 to 2.3.0 that includes some breaking changes. You will need to update and rebuild your custom module if you use Microsoft.OpenApi.

![Read more](media/readmore.png){: width="20"} [Breaking changes in Microsoft.OpenApi](https://github.com/microsoft/OpenAPI.NET/blob/main/docs/upgrade-guide-2.md).

!!! note
    If you find any new breaking changes, submit a question on [Virto Commerce Community](https://www.virtocommerce.org/c/support/12).

## Clean up BuildHost artifacts after upgrade

After updating Microsoft.EntityFrameworkCore.Design to 10.x, you will see that your project includes two folders **BuildHost-net472** and **BuildHost-netcore** under **obj** folder.
These folders are created by Microsoft.EntityFrameworkCore.Design - a package to support design-time services for different target frameworks. 

You can remove these two folders by modifying your **.csproj file** to include the following PackageReference for Microsoft.EntityFrameworkCore.Design with PrivateAssets set to all:

```xml
<PackageReference Include="Microsoft.EntityFrameworkCore.Design" Version="10.0.1">
  <PrivateAssets>all</PrivateAssets>
  <IncludeAssets>runtime; build; native; analyzers; buildtransitive</IncludeAssets>
</PackageReference>
```

## Resolve ModuleTypeLoadingException in .NET 10

You can get the ModuleTypeLoadingException exception after updating Platform and modules to v3.1000+:

```txt
Unhandled exception. VirtoCommerce.Platform.Core.Modularity.Exceptions.ModuleTypeLoadingException: Failed to load type for module SomeModule.
Cannot load "Microsoft.IO.RecyclableMemoryStream" for module ...
```
In .NET 10, Microsoft refreshed and excluded some assemblies (dll) that are no longer needed.

To resolve the issue, you can:

=== "Option 1"
    
    Add **module.keep** file in your custom module project with the following content, it adds the required dll into module package:

    ```txt
    Microsoft.IO.RecyclableMemoryStream.dll
    ```

=== "Option 2"
    
    Update your module to .NET 10 using the [instructions](#update-virto-commerce-platform-and-modules-to-v31000).

## 415 Unsupported Media Type for JSON Patch Requests

After upgrading to .NET 10, you may encounter a **415 Client Error: Unsupported Media Type** when performing store update operations that use JSON Patch, such as:

```txt
PATCH /api/stores/{storeId}
```

For example:

```txt
 /api/stores/B2B-store
```

| Why it happens | How to fix |
|----------------|------------|
| After upgrading to .NET 10, JSON Patch endpoints enforce stricter validation of the request `Content-Type`. The API now expects `application/json-patch+json` for `PATCH` requests. If the client sends `application/json`, the request is rejected with a **415 Unsupported Media Type** error. | Update the API client to send `Content-Type: application/json-patch+json` for all JSON Patch (`PATCH`) requests. This ensures the request is accepted and prevents 415 errors. |


## Update Virto Commerce Platform and modules to v3.1000+

=== "Use vc-build Update command"

    Use the vc-build Update command for an automated update. This method streamlines the update process, ensuring that all components are seamlessly transitioned to the new version.

    ```cmd
    vc-build Update -Stable -v 12
    ```

=== "Update via package.json"

    If you use **package.json** file for automated deployment, change versions of the Platform and Virto Commerce modules to 3.1000.0+. Based on latest **Stable 12** or **Edge** release strategy.

=== "Update manually"

    Manually download update the Platform and modules to version 3.1000+. This method provides more control over the update process, allowing for a step-by-step transition.

## Update custom modules

### Prerequisites

1. Install Visual Studio 2026.
1. Install Virto Commerce CLI (vc-build):
    ```cmd
    dotnet tool install VirtoCommerce.GlobalTool  -g
    ```

    or update:

    ```cmd
    dotnet tool update VirtoCommerce.GlobalTool -g
    ```

1. Install dotnet-ef to version 10.0+:

    ```cmd
    dotnet tool install --global dotnet-ef --version 10.0.1
    ```

    or update:

    ```cmd
    dotnet tool update --global dotnet-ef --version 10.0.1
    ```

If you develop a custom module, we recommend updating it to the .NET10 version.

### Update solution to NET10

1. Download and execute the [vc-net10-update.ps1 Power Shell script](vc-net10-update.ps1) in your solution folder. 

    !!! info

        If script execution is restricted, temporarily allow PowerShell scripts for the current session:

        ```powershell
        Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
        ```
  
1. Run the script from the solution root directory:

    ```powershell
    ./vc-net10-update.ps1
    ```

    This script automates several tasks, including:

    * Updating the Target Framework to .NET 10 for every project.
    * Updating project dependencies, including Microsoft NuGet dependencies to version 10.0.0 and VirtoCommerce NuGet dependency to version 3.1000.0 and latest.
    * Updating other third-party dependencies to the version used by Virto Commerce Platform .NET10.
    * Updating the module.manifest file to align with the changes in .NET 10.

### Build solution

1. Build the solution and meticulously address any compilation errors and warnings if required. This step ensures that the solution is compatible with the updated framework.
1. Verify Tests for Issues, perform a thorough verification of tests to identify and address any issues introduced by the update. This step guarantees that the updated solution maintains the expected functionality and performance.


### Create module package

Generate a module package by running: 

```cmd
vc-build Compress
```

This step finalizes the update process, creating a package that encapsulates the updated modules for deployment.

## Run and enjoy Virto Commerce on .NET 10

With the update process completed, you can now run and enjoy the enhanced capabilities of Virto Commerce on the .NET 10. Explore the Platform's new features and optimizations to leverage its full potential for a resilient and efficient ecommerce solution.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../overview">← Tutorials and how-tos </a>
    <a href="../adding-case-sensitive-search-support-for-postgre">Adding case-insensitive search support for PostgreSQL  →</a>
</div>