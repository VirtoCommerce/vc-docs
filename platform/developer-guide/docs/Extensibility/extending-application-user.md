# Extend ApplicationUser

Extending the ApplicationUser entity in the Virto Commerce Platform allows you to add custom fields and behavior to user profiles. This guide explains how to create a custom `ExtendedApplicationUser` class, update the security database context, and configure the platform to use the extended user model.

To extend an application user:

1. Create `ExtendedSecurityDbContext` class derived from `SecurityDbContext` or change the base class of your existing DbContext to `SecurityDbContext`.
Override the `OnModelCreating()` method and add `modelBuilder.UseOpenIddict<...>();`:

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
        
            modelBuilder.UseOpenIddict<VirtoOpenIddictEntityFrameworkCoreApplication,
                                    VirtoOpenIddictEntityFrameworkCoreAuthorization,
                                    VirtoOpenIddictEntityFrameworkCoreScope,
                                    VirtoOpenIddictEntityFrameworkCoreToken,
                                    string>();
            ...
        }
    }
    ```

1. Create a temporary migration:

    ```powershell
    dotnet ef migrations add Temporary
    ```

    This temporary migration will contain the code that creates all the security tables.
    Delete temporary migration files `*_Temporary.cs` and `*_Temporary.Designer.cs`, but keep the `ExtendedSecurityDbContextModelSnapshot.cs`.

1. Create `ExtendedApplicationUser` class derived from `ApplicationUser` and add your new fields:

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

1. In the `ExtendedSecurityDbContext.OnModelCreating()` method add your `ExtendedApplicationUser` entity:

    ```csharp
    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        base.OnModelCreating(modelBuilder);
        
        modelBuilder.UseOpenIddict<VirtoOpenIddictEntityFrameworkCoreApplication,
                                VirtoOpenIddictEntityFrameworkCoreAuthorization,
                                VirtoOpenIddictEntityFrameworkCoreScope,
                                VirtoOpenIddictEntityFrameworkCoreToken,
                                string>();

        modelBuilder.Entity<ExtendedApplicationUser>().Property("Discriminator").HasDefaultValue(nameof(ExtendedApplicationUser));
        ...
    }
    ```

1. Create new migration:

    ```powershell
    dotnet ef migrations add ExtendApplicationUser
    ```

1. Create `ExtendedUserStore` class derived form the platform's `CustomUserStore`, and pass the `ExtendedSecurityDbContext` to its constructor:

    ```csharp
    using Microsoft.AspNetCore.Identity;
    using VirtoCommerce.ExtendedSecurity.Data.Repositories;
    using VirtoCommerce.Platform.Security;

    namespace VirtoCommerce.ExtendedSecurity.Data.Services;

    public class ExtendedUserStore(ExtendedSecurityDbContext context, IdentityErrorDescriber describer = null)
        : CustomUserStore(context, describer)
    {
    }
    ```

1. In the `Module.Initialize()` method override `ApplicationUser` and `IUserStore<ApplicationUser>`:

    ```csharp
    public void Initialize(IServiceCollection serviceCollection)
    {
        ...
        AbstractTypeFactory<ApplicationUser>.OverrideType<ApplicationUser, ExtendedApplicationUser>();
        serviceCollection.AddScoped<IUserStore<ApplicationUser>, ExtendedUserStore>();
    }
    ```

By following these steps, you can correctly extend the `ApplicationUser` entity in the Virto Commerce Platform, add custom fields, and ensure compatibility with the base context.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../product-completeness-evaluator">← Extending product completeness evaluator </a>
    <a href="../opentelemetry">Open Telemetry  →</a>
</div>