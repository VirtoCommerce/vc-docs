# Configure VC with DB Providers

Virto Commerce is built on a DB agnostic architecture. The following databases are supported out of the box:

* Microsoft SQL Server.
* MySql Server.
* PostgreSQL.

At the same time, Virto Commerce architecture allows you add custom database provider on top of Entity Framework for solution as well as for a specific module.

Select the tab with the required provider setup information.

=== "Microsoft SQL Server"

    **Supported version**: Microsoft SQL Server 2019 or higher

    To setup DB Provider:

    1. Install and configure database. Run the SQL command `CREATE DATABASE [database_name];` to create a new database.
    1. Create a user with access to the database.
    1. Open the appsettings.json file in Visual Studio or other text editor. 
    1. Change `DatabaseProvider` to `"SqlServer"`.
    1. Change `ConnectionStrings` as follows: 

        ```json
        "DatabaseProvider": "SqlServer",
        "ConnectionStrings": {
        "VirtoCommerce": "Data Source=(local);Initial Catalog=VirtoCommerce3;Persist Security Info=True;User ID=virto;Password=virto;Connect Timeout=30;TrustServerCertificate=True;"
        },
        ```

=== "MySql"

    **Supported version**: MySql Server 5.7 or higher.

    To setup DB Provider:

    1. Install and configure database. Run the SQL command `CREATE DATABASE [database_name];` to create a new database.
    1. Create a user with access to the database.
    1. Open the appsettings.json file in Visual Studio or other text editor. 
    1. Change `DatabaseProvider` to `"MySql"`.
    1. Change `ConnectionStrings` as follows: 

        ```json
        "DatabaseProvider": "MySql",
        "ConnectionStrings": {
        "VirtoCommerce": "Server=myServerAddress;Database=myDataBase;Uid=myUsername;Pwd=myPassword;"
        },
        ```

        or
        
        ```json
        "DatabaseProvider": "MySql",
        "ConnectionStrings": {
        "VirtoCommerce": "Server=127.0.0.1;Port=6306;Uid=root;Pwd=Password1;Database=VirtoCommerce3;"
        },
        ```

=== "PostgreSql"

    **Supported version**: PostgreSQL 12 or higher.

    To setup DB Provider:

    1. Install and configure database. Run the SQL command `CREATE DATABASE [database_name];` to create a new database.
    1. Create a user with access to the database.
    1. Open the appsettings.json file in Visual Studio or other text editor. 
    1. Change `DatabaseProvider` to `"PostgreSql"`.
    1. Change "ConnectionString" as follows: 

        ```json
        "DatabaseProvider": "PostgreSql",
        "ConnectionStrings": {
        "VirtoCommerce": "User ID=postgres;Password=password;Host=localhost;Port=5432;Database=virtocommerce3;"
        },
        ```

!!! note  
    Migrations must be created and applied **separately** for each supported database provider. Each provider may generate slightly different SQL and behaviors, so a single migration run is not sufficient.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../overview">← DB agnostic architecture overview</a>
    <a href="../creating-custom-module">Creating custom module →</a>
</div>
