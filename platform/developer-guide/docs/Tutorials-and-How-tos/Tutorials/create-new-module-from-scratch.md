# Create New Module from Scratch

This guide explores how to create a new module from scratch using Visual Studio, following the example of the Dummy module.

## Create Solution and Projects

1. Create an empty solution named **DummyModule** [using Visual Studio](https://learn.microsoft.com/en-us/visualstudio/get-started/tutorial-projects-solutions?view=vs-2022##create-a-solution).
1. Add **src** and **tests** Solution Folders using Visual Studio.
    1. In the **src** folder, add the following projects:
        * **DummyModule.Core**: Class library (.NET Core).
        * **DummyModule.Data**: Class library (.NET Core).
        * **DummyModule.Web**: ASP.NET Core Web Application (Empty template).
    1. Delete the auto-generated `Class1.cs` from all projects.
    1. In the **tests** folder, add a project:
        * **DummyModule.Tests**: xUnit Test Project (.NET Core).
1. Set **Target framework** to **.NET Core 3.1** for all projects.
1. Set project references and NuGet package references as outlined in the guide:
    1. **References to Projects:**
        * **DummyModule.Data:** Reference **DummyModule.Core**.
        * **DummyModule.Web:** References **DummyModule.Core** and **DummyModule.Data**.
        * **DummyModule.Tests:** Reference **DummyModule.Core**, **DummyModule.Data**, and **DummyModule.Web** projects to facilitate comprehensive testing and integration.
    1. **References to NuGet Packages:**
        * **DummyModule.Core:** Add a reference to the latest version of the **VirtoCommerce.Platform.Core** package to leverage core functionalities.
        * **DummyModule.Data:** Add a reference to the latest version of the **VirtoCommerce.Platform.Data** package for data management capabilities.
    1. **Compile the Solution:** Ensure successful build completion without any warnings or errors.

## Fill DummyModule.Core Project

To populate the **DummyModule.Core** project with essential components:

1. Add **ModuleConstants.cs** for Module Constants:

   1. Create a class named **ModuleConstants.cs** to store module constants such as security permissions and settings.
   1. In the **ModuleConstants** class, define sub-classes for **Security** and **Permissions**. These classes contain constants representing various permissions within the module, structured as follows:

        ```csharp
        public static class Security
        {
            public static class Permissions
            {
                public const string Access = "dummy:access";
                public const string Read =   "dummy:read";
                public const string Create = "dummy:create";
                public const string Update = "dummy:update";
                public const string Delete = "dummy:delete";

                public static string[] AllPermissions = { Access, Read, Create, Update, Delete };
            }
        }
        ```

1. In the **ModuleConstants** class, add sub-classes such as **Settings** and **General**. These sub-classes contain settings definitions of type **SettingDescriptor**, facilitating the management of module settings:

    ```csharp
    public static SettingDescriptor DummyInteger = new SettingDescriptor
    {
        Name = "Dummy.Integer",
        GroupName = "Dummy|General",
        ValueType = SettingValueType.Integer,
        DefaultValue = 50
    };
    ```

    !!! note
        Refer to [sample ModuleConstants.cs](https://github.com/VirtoCommerce/vc-samples/blob/v3/DummyModule/DummyModule/src/DummyModule.Core/ModuleConstants.cs) for complete code examples.

1. Add additional components if necessary:

   * If your module includes domain models, create a **Models** folder and define all domain models in it.
   * For search functionality, include a **Search** subfolder containing **SearchCriteria** and **SearchResult** classes.
   * Utilize the **Services** folder to create interfaces for required services, often including CRUD and search operations.
   * Model-related events can be added to the **Events** folder, derived from the base **GenericChangedEntryEvent** class.
   * Define new types of **Notifications** in the **Notifications** folder, each inheriting from **EmailNotification/SmsNotification** or a custom class based on **Notification**.

These steps ensure the **DummyModule.Core** project contains essential components for module functionality and management.

## Fill DummyModule.Data Project

To populate the **DummyModule.Data** project with necessary components:

1. Add Models Folder for Persisted Data.

   * If your module involves persisting domain data, create a **Models** folder.
   * All models related to persistence should be defined within this folder.
   * Ensure that each class under this folder corresponds to a class in **DummyModule.Core/Models**.
   * These classes should define the database table structure and any restrictions, along with the ability to convert to/from corresponding Core model classes.

1. Include **Repositories** folder:
   1. Within **DummyModule.Data**, add a **Repositories** folder.
   1. In the **Repositories** folder:
     1. Add a class named **DummyDbContext**, deriving from **DbContextWithTriggers**. Check and copy the contents of the class from a sample **DummyDbContext.cs**.
     1. Add a class named **DesignTimeDbContextFactory**. Check and copy the contents of the class from a sample **DesignTimeDbContextFactory.cs**. Ensure that the connection to your development SQL server is accurate.
    1. Introduce a data repository abstraction (interface) that derives from **IRepository** for the defined persistence model.
    1. Implement the repository with a class that derives from **DbContextRepositoryBase<DummyDbContext>**.

1. Generate code-first migration as follows:
    1. Set the **DummyModule.Data** project as the startup project in Solution Explorer.
    1. Open the NuGet Package Manager Console.
    1. Set the **Default project** to **src\DummyModule.Data**.
    1. Run the command:

       ```sql
       Add-Migration Initial -Verbose
       ```

     A new EF migration will be generated, facilitating the extension of an existing module's model.

1. Include Additional folders if necessary:

   * **Caching folder:** If data caching is required, add a folder for cache region classes. Typically, each model should have its own region. Derive the cache region from the generic **CancellableCacheRegion<T>** class.
   * **Services folder:** Implement interfaces defined in the **.Core** project within this folder.
   * **ExportImport folder:** Add a class for data export/import, which should be called from **Module.cs** and contain the implementation for module data export and import.
   * **Handlers folder:** Include handlers for domain events defined under **.Core/Events**. These handlers facilitate reacting to and managing domain events within the module.

## Fill DummyModule.Web Project

1. Add the required folders and files such as **Controllers/Api**, **Localizations**, **Scripts**, and **module.manifest**.
1. Implement the module manifest, controllers for API endpoints, JavaScript files, stylesheets, and localizations.
1. Configure webpack for JavaScript and stylesheet bundling.
1. If required, add unit tests and integration tests.

## Filling DummyModule.Tests Project

1. Add unit tests and integration tests as needed.
1. Ensure integration tests are marked appropriately with the **Trait** attribute.

## Creating Module Package

Create the module package following [this article](../../CLI-tools/overview.md).

By following these steps, you can create a new module in a structured and organized manner, ensuring compatibility with the VirtoCommerce platform.