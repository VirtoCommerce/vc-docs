# Transforming Custom Module to Support DB Agnostic Approach

To transform your custom module to support DB agnostic approach:

1. Add new Data.[Provider] projects.
1. Add Project references.
1. Add Packages for specific database provider:
    1. MySql - Pomelo.EntityFrameworkCore.MySql 6.0.0
    1. PostgreSql - Npgsql.EntityFrameworkCore.PostgreSQL 6.0.0
    1. Sql Server - Microsoft.EntityFrameworkCore.SqlServer
1. Copy and update:
    1. DbContextOptionsBuilderExtensions.cs
    1. PostgreSqlDbContextFactory.cs
    1. Readme.md
1. Add DB Agnostic AddDbContext in Module.Initialize.
1. Add customization extension OnModelCreating to allow configuration of an entity type for different database types.
1. Refactor and isolate raw Sql server code. 
1. Copy Migrations from Data to SqlServer.
1. Create new Migrations.
1. Compile, compress, and test.