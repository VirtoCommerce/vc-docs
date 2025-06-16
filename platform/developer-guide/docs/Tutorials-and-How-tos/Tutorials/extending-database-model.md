# Extend Database Model

This tutorial provides specific steps to extend the model and persistence layer of an existing module. In this guide, we will use the [Virto Commerce Orders Module](https://github.com/VirtoCommerce/vc-module-order/tree/master/samples/VirtoCommerce.OrdersModule2.Web) as an example. 

We recommend following a 3-tier architecture (Core, Data, and Web) for both custom modules and the Virto Commerce platform.

## Changes in ".Core" project

1. Add a reference to the ".Core" NuGet package containing the base models, for example, `VirtoCommerce.OrdersModule.Core`.
1. Define a new model class by extending the base model in the **Models** folder, for example: `CustomerOrder2 : CustomerOrder`.
1. Add additional properties required for the new model.

## Changes in ".Data" project

1. Add a reference to ".Data" NuGet package containing the base models, for example, `VirtoCommerce.OrdersModule.Data`.
1. Define a new model class by extending the base model in the **Models** folder, for example: `CustomerOrder2Entity : CustomerOrderEntity`. 
1. Add additional properties required for the new model.
1. Override the `ToModel`, `FromModel`, and `Patch` methods.
1. Modify the **Repositories** folder:
    1. Define a new DbContext class by extending the parent DbContext. Add 1 public constructor and override `OnModelCreating`. Refer to [the example](https://github.com/VirtoCommerce/vc-module-order/blob/release/3.0.0/samples/VirtoCommerce.OrdersModule2.Web/Repositories/Order2DbContext.cs) for more details.
    1. Create `DesignTimeDbContextFactory` for DbContext, defined in the previous step.
    1. **Optionally** extend the parent repository interface by adding the `IQueryable<T>` property and additional methods as needed.
    1. Extend the parent repository by implementing the interface defined in the previous step. If new interface wasn't defined, override the base methods as needed. Add the `IQueryable<the new type>`, for example:

        ```csharp
        public IQueryable<CustomerOrder2Entity> CustomerOrders2 => DbContext.Set<CustomerOrder2Entity>();
        ```
   
1. Generate code-first DB migration:
    1. Set your ".Data" project as a startup project in Solution Explorer.
    1. Open the NuGet **Package Manager Console**.
    1. Select your ".Data" as the default project in the console.
    1. Run the command to add a new migration. Replace `YourNewMigrationName` with the desired migration name:
    
        ```console
        Add-Migration YourNewMigrationName
        ```

1. Examine the generated code and **remove** the commands that do not reflect your model changes or configurations defined in your **DbContext.OnModelCreating()**. These changes have already been applied by migrations in the base module. Make sure that the **Up()** method defines:

    * New tables and indices:

        ```cs
        migrationBuilder.CreateTable(
               name: "OrderInvoice",
               ...
        );

        migrationBuilder.CreateIndex(
              name: "IX_OrderInvoice_CustomerOrder2Id",
              table: "OrderInvoice",
              column: "CustomerOrder2Id");
        ```

    * New column(s) when modifying the existing:

        ```csharp
        migrationBuilder.AddColumn<string>(name: "NewField", table: "CustomerOrder", maxLength: 128, nullable: true);
        ```

    * A `Discriminator` column if new columns were defined in the previous step AND it didn't exist in the original table:

        ```csharp
        migrationBuilder.AddColumn<string>(name: "Discriminator", table: "CustomerOrder", nullable: false, maxLength: 128, defaultValue: "CustomerOrder2Entity");
        ```

        !!! note
            You need to add SQL script for adding the field to `20000000000000_Update<Module>V2.cs` for backward compatibility with v.2.:
            ```sql
            ALTER TABLE [CustomerOrder] ADD [Discriminator] nvarchar(128) NOT NULL DEFAULT('CustomerOrder2Entity')
            ```

        If the `Discriminator` already exists and you want to migrate from v.2, add SQL script to update the field to `20000000000000_Update<Module>V2.cs` for backward compatibility with v.2.:

        ```cs
        migrationBuilder.Sql(
                @"BEGIN                                   
                      EXEC('UPDATE [CustomerOrder] SET [Discriminator] = ''CustomerOrder2Entity''')
                  END");
        ```

    * Any custom SQL scripts if data update is required.

        ![Readmore](media/readmore.png){: width="25"} [EF Core article about inheritance](https://docs.microsoft.com/en-us/ef/core/modeling/inheritance)

1. The **Down()** method should do the opposite of what Up() does. That way you can quickly apply and unapply your changes quickly by `Update-Database` command in console.

## Changes in ".Web" project

1. Modify the **module.manifest** file. Ensure that a dependency on the appropriate module is added to the **dependencies** section:

    ```xml
        <dependency id="VirtoCommerce.Orders" version="3.0.0" />
    ```

1. Modify the **Module.cs** regarding the model extension:

    1. In the **Initialize()** method:

        1. Register the new DbContext in DI:

            ```csharp
            serviceCollection.AddDbContext<Order2DbContext>((provider, options) =>
            {
                var configuration = provider.GetRequiredService<IConfiguration>();
                options.UseSqlServer(configuration.GetConnectionString("VirtoCommerce"));
            });
            ```

        1. Register the new **Repository_ implementation** in DI:

            ```csharp
            serviceCollection.AddTransient<IOrderRepository, OrderRepository2>();
            ```

    1. In the **PostInitialize()** method:

        1. Register type override(s) to AbstractTypeFactory.
        1. Register new type(s) to AbstractTypeFactory as usual.
        1. Add code to ensure that the migrations from new DbContext are applied:

            ```csharp
            using (var serviceScope = appBuilder.ApplicationServices.CreateScope())
            {
                var dbContext = serviceScope.ServiceProvider.GetRequiredService<Order2DbContext>();
                dbContext.Database.EnsureCreated();
                dbContext.Database.Migrate();
            }
            ```

1. Test your changes in the Solution REST API documentation (Swagger) and in the database.


![Readmore](media/readmore.png){: width="25"} [Creating new module](creating-custom-module.md)



<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../How-tos/docker-modules-development">← Modules development via Docker </a>
    <a href="../build-platform-manager-ui">Building Platform manager UI  →</a>
</div>