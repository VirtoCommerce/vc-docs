# Add Case-Insensitive Search Support for PostgreSQL into Virto Commerce Module

By default, PostgreSQL performs case-sensitive string comparisons, unlike SQL Server. This guide walks you through enabling case-insensitive search for specific entity properties.

1. Update your module's platform dependency to version 3.1004 or later to get access to the required PostgreSQL extension methods.

1. Determine which entity properties should support case-insensitive search. Apply this only to properties that require it (typically user-facing fields used in search or filtering).

    !!! note
        Avoid applying case-insensitive collation to all string properties indiscriminately, as it may affect performance and index behavior.

1. Create an `IEntityTypeConfiguration` class in your **MyCompany.MyModuleName.Data.PostgreSql** project for each entity that needs case-insensitive properties.

    Use the `UseCaseInsensitiveCollation()` extension method from `VirtoCommerce.Platform.Data.PostgreSql.Extensions`.

    ```csharp
    using Microsoft.EntityFrameworkCore;
    using Microsoft.EntityFrameworkCore.Metadata.Builders;
    using VirtoCommerce.Platform.Data.Model;
    using VirtoCommerce.Platform.Data.PostgreSql.Extensions;

    public class MyClassEntityConfiguration : IEntityTypeConfiguration<MyClass>
    {
        public void Configure(EntityTypeBuilder<MyClass> builder)
        {
            builder.Property(x => x.Name).UseCaseInsensitiveCollation();
            builder.Property(x => x.UserName).UseCaseInsensitiveCollation();
            builder.Property(x => x.Email).UseCaseInsensitiveCollation();       
        }
    }
    ```

1. Generate a new migration from the PostgreSQL data project directory by running:

    ```csharp
    dotnet ef migrations add AddCaseInsensitiveCollations
    ```

1. Open the generated migration file and verify that it contains AlterColumn calls specifying the case-insensitive collation for the expected columns.

1. At the beginning of the Up method in the generated migration, add the `CreateCaseInsensitiveCollationIfNotExists()` call from `VirtoCommerce.Platform.Data.PostgreSql.Extensions`. This ensures the required collation exists in the database before any columns reference it:

    ```csharp
    using Microsoft.EntityFrameworkCore.Migrations;
    using VirtoCommerce.Platform.Data.PostgreSql.Extensions

    ...

        public partial class AddCaseInsensitiveCollations : Migration
        {
            /// <inheritdoc />
            protected override void Up(MigrationBuilder migrationBuilder)
            {
                migrationBuilder.CreateCaseInsensitiveCollationIfNotExists();
                ...
    ```

1. Build and install the module. Verify that EF Core Contains() and equality (==) operations are now case-insensitive for the configured properties.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../upgrading-to-dot-net-10">← Upgrading to Virto Commerce on .NET10 </a>
    <a href="../swagger-api">Swagger/API integration  →</a>
</div>