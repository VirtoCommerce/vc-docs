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
    }
    ```

1. Create a temporary migration to initialize the security tables:

    ```powershell
    dotnet ef migrations add Temporary
    ```

    This temporary migration contains the code that creates all the security tables. Delete the temporary files `*_Temporary.cs` and `*_Temporary.Designer.cs`, but keep `ExtendedSecurityDbContextModelSnapshot.cs`.

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

1. Override the `OnModelCreating()` method in `ExtendedSecurityDbContext` to configure the extended user entity:

    ```csharp
    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        base.OnModelCreating(modelBuilder);

        modelBuilder.Entity<ExtendedApplicationUser>().Property("Discriminator").HasDefaultValue(nameof(ExtendedApplicationUser));
        // Add any additional configuration here
    }
    ```

1. Create a new migration to apply the changes made to the database schema:

    ```powershell
    dotnet ef migrations add ExtendApplicationUser
    ```

1. In the `Module.Initialize()` method of your module, override `ApplicationUser` and `SecurityDbContext`:

    ```csharp
    public void Initialize(IServiceCollection serviceCollection)
    {
        // Other initialization code

        AbstractTypeFactory<ApplicationUser>.OverrideType<ApplicationUser, ExtendedApplicationUser>();
        serviceCollection.AddTransient<SecurityDbContext, ExtendedSecurityDbContext>();
    }
    ```

By following these steps, you can seamlessly extend the `ApplicationUser` entity in the Virto Commerce Platform to accommodate your specific requirements.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../product-completeness-evaluator">← Extending product completeness evaluator </a>
    <a href="../page-builder-extension">Adding new blocks to Page Builder  →</a>
</div>