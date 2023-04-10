# Overview
Virto Commerce uses MS SQL as master data storage. However, modern object-database mappers such as Entity Framework hide all maintenance tasks from developers. 
While the system operates successfully in development, quality assurance, and acceptance environments, production environments may experience performance degradation due to the regular maintenance requirements of SQL Server databases. This is particularly crucial for e-commerce solutions.

Use the following common SQL Server maintenance tasks regularly to avoid performance degradation:

* [Check index defragmentation and rebuild index.](index-defragmentation.md)
* [Find and create missing index.](creating-missing-index.md)
* [Control and eliminate long-running queries.](control-long-running-queries.md)
* [Prune PlatformOperationLog and NotificationMessage tables.](prune-of-tables.md)
* [Control size of tables.](table-size-control.md)
* [Use Azure SQL Elastic Pool and several databases instead of the Big One.](azure-sql-elastic-pool.md)
* [Use Azure tools.](use-azure-tools.md)
* [Find blocking queries in SQL Azure.](find-blocking-queries.md)
* [Set the maximum number of concurrent requests and sessions.](set-number-of-concurrent-sessions.md)