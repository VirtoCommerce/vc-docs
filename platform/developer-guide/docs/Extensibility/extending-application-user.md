# Extend ApplicationUser

Extending the `ApplicationUser` entity in the Virto Commerce Platform allows you to add custom fields and behaviors to user profiles. This guide outlines the steps to extend `ApplicationUser` by creating a new class, `ExtendedApplicationUser`, and updating the database context accordingly.

To extend an application user:

1. Create a new class named `ExtendedSecurityDbContext` derived from `SecurityDbContext`:

    ```csharp
    using Microsoft.EntityFrameworkCore;
    using VirtoCommerce.Platform.Security.Repositories;

    public class ExtendedSecurityDbContext : SecurityDbContext
    {
        public ExtendedSecurityDbContext(DbContextOptions<ExtendedSecurityDbContext> options)
            : base(options)
        {
        }

        protected ExtendedSecurityDbContext(DbContextOptions options)
            : base(options)
        {
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);

            modelBuilder.Entity<ExtendedApplicationUser>();
        }
    }
    ```

1. Create a temporary migration to initialize the security tables:

    ```powershell
    dotnet ef migrations add Temporary
    ```

    This temporary migration contains the code that creates all the security tables. Delete the temporary files `*_Temporary.cs` and `*_Temporary.Designer.cs`, but keep `ExtendedSecurityDbContextModelSnapshot.cs`.

    Creating migrations with `dotnet ef migrations add ...` will generate migrations for all entities and fields in the extension module, even if these entities or fields already exist in the original module and database.  
    
    To avoid that:
    
    === "Option 1"
        Copy the DB snapshot file (`SecurityDbContextModelSnapshot.cs`) from the original module to the migrations directory of your extension module and change its namespace to match the new module.  
    
    === "Option 2"
        Regenerate the DB snapshot file by creating an empty migration (before registering the extension entities in the new DB context):  
    
        1. Run `dotnet ef migrations add Temporary`.  
        1. Remove the content of the `Up` and `Down` methods in the generated migration, but keep the snapshot file unchanged.  
        1. Then, add your extended fields or entities and run `dotnet ef migrations add AddRecommendedPrice` again.  
        1. The second migration will now contain only the new fields or entities introduced in your extension.

1. Define a new class, `ExtendedApplicationUser`, derived from `ApplicationUser`, and add any additional fields:

    ```csharp
    using VirtoCommerce.Platform.Core.Security;

    public class ExtendedApplicationUser : ApplicationUser
    {
        public string NewField { get; set; }

        public override void Patch(ApplicationUser target)
        {
            base.Patch(target);

            if (target is ExtendedApplicationUser extendedUser)
            {
                extendedUser.NewField = NewField;
            }
        }
    }
    ```

1. Create a new migration to apply the changes made to the database schema:

    ```powershell
    dotnet ef migrations add AddRecommendedPrice -c Pricing2DbContext
    ```

    The migration should be created **in the extension project** (not in the base module).  
    The `-c` parameter specifies which database context to use — in this case, your **extended context**.  
    
    For example:
    ```powershell
    dotnet ef migrations add AddRecommendedPrice -c Pricing2DbContext
    ```
    where `Pricing2DbContext` is the DbContext defined in your extension.

    When EF Core generates the migration, it automatically adds a system field called `Discriminator`.  
    This field is used by Entity Framework to store the class name that EF should instantiate when reading entities from the database.  
    
    ![Readmore](media/readmore.png){: width="25"} [Inheritance in EF Core](https://learn.microsoft.com/en-us/ef/core/modeling/inheritance)

    Usually, this field does not need to be defined manually in the `OnModelCreating()` method — it is added automatically to the migration, as shown below:

    ```csharp
    public partial class AddRecommendedPrice : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<string>(
                name: "Discriminator",
                table: "Price",
                type: "character varying(128)",
                maxLength: 128,
                nullable: false,
                defaultValue: "Price2Entity");

            migrationBuilder.AddColumn<decimal>(
                name: "RecommendedPrice",
                table: "Price",
                type: "Money",
                nullable: true);
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "RecommendedPrice",
                table: "Price");

            migrationBuilder.DropColumn(
                name: "Discriminator",
                table: "Price");
        }
    }
    ```

    In this example, `RecommendedPrice` is the extended field, `Discriminator` is a system field that defines which derived entity (`Price2Entity`) should be used when reading data from the database.

    Even if this field is not specified in the `DbContext`, it will still appear in the snapshot and designer files generated by EF.

    !!! note
        **Before applying the migration**, make sure to manually review the generated migration file.  
        It must contain only your extended fields and the `Discriminator` field — nothing else.  
        Otherwise, you may face issues later and need to manually roll back or remove incorrect migrations.

1.  Once verified, apply the migration to the database (in the **extension project**) using the command:

    ```powershell
    dotnet ef database update -c Pricing2DbContext
    ```

    This command updates the database using the migrations associated with the specified extended context.

1. In the `Module.Initialize()` method of your module, override `ApplicationUser` and `SecurityDbContext`:

    ```csharp
    public void Initialize(IServiceCollection serviceCollection)
    {
        // Other initialization code

        AbstractTypeFactory<ApplicationUser>.OverrideType<ApplicationUser, ExtendedApplicationUser>();
        serviceCollection.AddTransient<SecurityDbContext, ExtendedSecurityDbContext>();
    }
    ```

By following these steps, you can correctly extend the `ApplicationUser` entity in the Virto Commerce Platform, add custom fields, and ensure compatibility with the base context.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../product-completeness-evaluator">← Extending product completeness evaluator </a>
    <a href="../page-builder-extension">Adding new blocks to Page Builder  →</a>
</div>