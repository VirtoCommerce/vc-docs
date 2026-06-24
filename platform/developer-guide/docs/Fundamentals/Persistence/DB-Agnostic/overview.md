# Overview

Database agnostic architecture is a design strategy that allows an application to function with any database, regardless of its vendor or type.

Virto Commerce has full DB agnostic support for ecommerce modules and offers unlimited scalability - our customers have the flexibility to choose the best-in-breed database. We offer a range of out-of-the-box database providers, including Microsoft SQL Server, MySql, and PostgreSql.

## Architecture principles

Our architecture follows key principles to ensure stability, flexibility, and maintainability:

* **No breaking changes**: Safe updates without disrupting existing solutions.
* **Entity Framework Core**: All data access is built on EF Core.
* **Database provider isolation**: DB-specific code is isolated per project to avoid affecting the core.
* **Customization support**: Designed to support solution customization.

## Supported databases and support level

Virto Commerce ships three first-party database providers, selected through the `DatabaseProvider` setting in **appsettings.json**:

| Provider | `DatabaseProvider` value | Minimum version |
| --- | --- | --- |
| Microsoft SQL Server | `SqlServer` | 2019 |
| MySQL | `MySql` | 5.7 |
| PostgreSQL | `PostgreSql` | 12 |

All three are fully supported for ecommerce modules. **SQL Server is the default**: `DatabaseProvider` falls back to `SqlServer` when it is not set. A few operational paths are SQL Server-specific, namely the legacy Virto Commerce 2.x to 3.x upgrade path and the [SQL maintenance scripts](../../../Operations/maintenance-tasks-for-sql.md). MySQL and PostgreSQL have no such legacy constraints.

![Readmore](media/readmore.png){: width="25"} [Configuring VC with DB providers](configuring-vc-with-db-providers.md)

## Database migrations

Each module owns its schema and ships Entity Framework Core migrations. A module applies its own migrations automatically on startup, so a fresh database is created and an existing one is brought up to date without manual steps.

Migrations are provider-specific. Every database provider project, for example **VirtoCommerce.Platform.Data.SqlServer**, **VirtoCommerce.Platform.Data.MySql**, and **VirtoCommerce.Platform.Data.PostgreSql**, holds its own migration assembly, because each provider can generate slightly different SQL. When you extend the data model, add a migration for every provider you support.

![Readmore](media/readmore.png){: width="25"} [Creating a custom DB-agnostic module](creating-custom-module.md)

For bulk or offline migration, for example generating SQL scripts during a 2.x to 3.x upgrade, use the Grab Migrator tool.

![Readmore](media/readmore.png){: width="25"} [Grab Migrator](../../../CLI-tools/grab-migrator.md)


![Readmore](media/readmore.png){: width="25"} [Handling concurrency conflicts](../Concurrency-handling/concurrency-handling.md)

![Readmore](media/readmore.png){: width="25"} [Caching overview](../../Caching/01-overview.md)

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../../Intent-Search/overview">← Intent Search overview</a>
    <a href="../configuring-vc-with-db-providers">Configuring VC with DB providers →</a>
</div>
