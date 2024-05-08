# Maintenance Tasks for SQL
Virto Commerce uses MS SQL as master data storage. However, modern object-database mappers such as Entity Framework hide all maintenance tasks from developers. 
While the system operates successfully in development, quality assurance, and acceptance environments, production environments may experience performance degradation due to the regular maintenance requirements of SQL Server databases. This is particularly crucial for e-commerce solutions.

Below are common SQL Server maintenance tasks that you should perform regularly to avoid performance degradation.

## Index Defragmentation and Rebuilding

Index fragmentation happens when logical order based on the key value doesn't match physical order within pages. Database Engine automatically modifies indexes when inserting, updating or deleting data.  For example, the addition of rows in a table may cause existing pages in rowstore indexes to split to make room for the insertion of new key values. Modifications over time lead to scattered information and fragmented indexes in the database. Heavily fragmented indexes can degrade query performance due to additional I/O required to locate data to which the index points. More I/O slows down the application, particularly during scan operations.

!!!note
    Rebuilding is recommended if `avg_fragmentation_in_percent` is greater than 30%.

To start index defragmentation and rebuilding:

1. Run the query to find out the percentage of fragmentation:
    ```sql
    SELECT
    DB_NAME() AS DBName
    ,OBJECT_NAME(ps.object_id) AS TableName
    ,i.name AS IndexName
    ,ips.index_type_desc
    ,ips.avg_fragmentation_in_percent
    FROM sys.dm_db_partition_stats ps
    INNER JOIN sys.indexes i
    ON ps.object_id = i.object_id
    AND ps.index_id = i.index_id
    CROSS APPLY sys.dm_db_index_physical_stats(DB_ID(), ps.object_id, ps.index_id, null, 'LIMITED') ips
    ORDER BY ips.avg_fragmentation_in_percent desc, ps.object_id, ps.index_id
    ```
1.  Run the query to rebuilding indexes. Use the [SQL maintenance script](https://raw.githubusercontent.com/yochananrachamim/AzureSQL/master/AzureSQLMaintenance.txt) or the simplest one:
    ```sql
    DECLARE @TableName varchar(255)
    
    DECLARE TableCursor CURSOR FOR
    (
    SELECT '[' + IST.TABLE_SCHEMA + '].[' + IST.TABLE_NAME + ']' AS [TableName]
    FROM INFORMATION_SCHEMA.TABLES IST
    WHERE IST.TABLE_TYPE = 'BASE TABLE'
    )
    
    OPEN TableCursor
    FETCH NEXT FROM TableCursor INTO @TableName
    WHILE @@FETCH_STATUS = 0
    
    BEGIN
    PRINT('Rebuilding Indexes on ' + @TableName)
    Begin Try
    EXEC('ALTER INDEX ALL ON ' + @TableName + ' REBUILD with (ONLINE=ON)')
    End Try
    Begin Catch
    PRINT('Cannot do rebuild with Online=On option, taking table ' + @TableName+' down for douing rebuild')
    EXEC('ALTER INDEX ALL ON ' + @TableName + ' REBUILD')
    End Catch
    FETCH NEXT FROM TableCursor INTO @TableName
    END
    
    CLOSE TableCursor
    DEALLOCATE TableCursor
    ```

## Find and Create Missing Index

SQL Server keeps up with index statistics behind the scenes. When you use Entity Framework, very easy to skip the required index and decrease the performance of the solution.

The higher the `improvement_measure` is, the better is your performance. If you see a missing index with a high `user_seeks` value, which is the number of times the index could have been used, add it.

!!! note
    Do not create more than 5-10 indexes per table.

To find missing indexes, run the query and copy SQL command to create them:

```sql
SELECT CONVERT (varchar, getdate(), 126) AS runtime,
       mig.index_group_handle,
       mid.index_handle,
       CONVERT (decimal (28,1),
        migs.avg_total_user_cost *
        migs.avg_user_impact *
        (migs.user_seeks + migs.user_scans))
        AS improvement_measure,
       'CREATE INDEX missing_index_' +
       CONVERT (varchar, mig.index_group_handle) +
       '_' +
       CONVERT (varchar, mid.index_handle) +
       ' ON ' +
       mid.statement +
       ' (' + ISNULL (mid.equality_columns,'') +
       CASE WHEN mid.equality_columns IS NOT NULL
            AND mid.inequality_columns IS NOT NULL
        THEN ','
        ELSE ''
        END + ISNULL (mid.inequality_columns, '') +
        ')' +
        ISNULL (' INCLUDE (' + mid.included_columns + ')',
                '') AS create_index_statement,
        migs.*,
    mid.database_id, mid.[object_id]
    FROM sys.dm_db_missing_index_groups mig
    INNER JOIN sys.dm_db_missing_index_group_stats migs
        ON migs.group_handle = mig.index_group_handle
    INNER JOIN sys.dm_db_missing_index_details mid
        ON mig.index_handle = mid.index_handle
    WHERE CONVERT (decimal (28,1),
                   migs.avg_total_user_cost *
               migs.avg_user_impact *
              (migs.user_seeks + migs.user_scans)) > 10
    ORDER BY migs.avg_total_user_cost *
             migs.avg_user_impact *
         (migs.user_seeks + migs.user_scans) DESC
```

## Control and Eliminate Long-Running Queries

To find slow and long-running queries, run the script:

```sql
SELECT TOP 20 total_worker_time/execution_count AS [avg_cpu_time],
    (SELECT TOP 1 SUBSTRING(s2.text,statement_start_offset / 2+1 ,
      ((CASE WHEN statement_end_offset = -1
         THEN
            (LEN(CONVERT(nvarchar(max),s2.text)) * 2)
         ELSE
            statement_end_offset
         END)
      - statement_start_offset) / 2+1))  AS sql_statement,
    execution_count,
    plan_generation_num,
    last_execution_time,   
    total_worker_time,
    last_worker_time,
    min_worker_time,
    max_worker_time,
    total_physical_reads,
    last_physical_reads,
    min_physical_reads,  
    max_physical_reads,  
    total_logical_writes,
    last_logical_writes,
    min_logical_writes,
    max_logical_writes,
  s1.sql_handle
FROM sys.dm_exec_query_stats AS s1
CROSS APPLY sys.dm_exec_sql_text(sql_handle) AS s2  
WHERE s2.objectid is null
ORDER BY  (total_worker_time/execution_count) DESC

```

## Prune PlatformOperationLog and NotificationMessage Tables

The recommended retention period for PlatformOperationLog and NotificationMessage is 45 days. This is usually enough to find the reason for the issues. Create a task and run it either nightly or weekly.

```sql

SELECT TOP $processRowsCount Id FROM [dbo].[$tableName] WHERE CreatedDate < '$thresholdDate' ORDER BY CreatedDate
"@
    Write-Output "Parameters set to remove $processRowsCount rows from $tableName table in $Database database with created date < $thresholdDate"
    $records = @()
    try {
        $records = Invoke-Sqlcmd -ServerInstance $SqlServer -Database $Database -Username $SqlUsername -Password $SqlPass -Query $sqlQuery -ConnectionTimeout $ConnectionTimeout
    } catch {
        Write-Error "$error"
        throw "$error"
    }
    if ($records.count -eq 0) { Write-Output "No records found fitting the parameters"}
    $c = 0
    foreach ($entry in $records) {
        if ($VerboseOutput -eq 1){Write-Output "Removing record with Id $($records[$c].Id)"}
        $sqlQuery2 = @"
DELETE FROM [dbo].[$tableName] WHERE Id = '$($records[$c].Id)'
"@
        try {
            Invoke-Sqlcmd -ServerInstance $SqlServer -Database $Database -Username $SqlUsername -Password $SqlPass -Query $sqlQuery2 -ConnectionTimeout $ConnectionTimeout
        } catch {
            Write-Error "$error"
            throw "$error"
        }
        $c = $c + 1
    }
    Write-Output "Removed $c rows"
}
```

## Control Table Size 

It is very important to control the size of tables. It takes more time to apply any operation to a larger table. If you have temporary or log tables, don't forget to clean up the expired data.

Run the script to return the size of the table in Mbytes:
```sql
select    
      sys.objects.name, sum(reserved_page_count) * 8.0 / 1024
from    
      sys.dm_db_partition_stats, sys.objects
where    
      sys.dm_db_partition_stats.object_id = sys.objects.object_id

group by sys.objects.name
ORDER BY 2 DESC
```

## Use Azure SQL Elastic Pool and Multiple Databases Instead of Single One

Azure SQL pools are well suited for Virto Commerce solutions. Virto Commerce allows you to create a unique connection string for each module. The more databases you can add to a Pool, the more you're going to save. Depending on your application usage patterns, it's possible to see savings with as few as two S3 databases.

To set own connection string for every module, use Module Id as a name of a connection string. You can find Module Id in the [module.manifest](../Fundamentals/Modularity/06-module-manifest-file.md) file. For example, Module Id for the Order module is as follows:

```
<?xml version="1.0" encoding="utf-8" ?>
<module>
    <id>VirtoCommerce.Orders</id>
    <version>2.17.30</version>
    <platformVersion>2.13.42</platformVersion>
    <dependencies>
        <dependency id="VirtoCommerce.Core" version="2.25.24" />
        <dependency id="VirtoCommerce.Catalog" version="2.12.0" />
        <dependency id="VirtoCommerce.Pricing" version="2.11.0" />
        <dependency id="VirtoCommerce.Customer" version="2.11.0" />
        <dependency id="VirtoCommerce.Store" version="2.11.0" />
    </dependencies>
```

Set your own connection strings for:

* VirtoCommerce.Cart.
* VirtoCommerce.Catalog.
* VirtoCommerce.Customer.
* VirtoCommerce.Orders.
* VirtoCommerce.Pricing.
* VirtoCommerce - Default database for other modules.

It decreases database size and cost, increases performance and simplifies maintenance tasks.

## Use Azure Tools

Azure supports a big list of the service to improve Maintenance Tasks for SQL Server.

Here is the automatic tuning list:

* Automated performance tuning of Azure SQL databases.
* Automated verification of performance gains.
* Automated rollback and self-correction.
* Tuning history.
* Tuning action T-SQL scripts for manual deployments.
* Proactive workload performance monitoring.
* Scale-out capability on hundreds of thousands of databases.
* Positive impact to DevOps resources and the total cost of ownership.

For more information, read [Automatic tuning in Azure SQL Database and Azure SQL Managed Instance](https://learn.microsoft.com/en-us/azure/azure-sql/database/automatic-tuning-overview?view=azuresql).

## Find Blocking Queries in SQL Azure

To finding blocking queries in SQL Azure, run:

```sql
SELECT TOP 10 r.session_id, 
r.plan_handle,      
r.sql_handle, 
r.request_id,      
r.start_time, 
r.status,      
r.command, 
r.database_id,      
r.user_id, 
r.wait_type,     
 r.wait_time, 
r.last_wait_type,      
r.wait_resource, 
r.total_elapsed_time,      
r.cpu_time, 
r.transaction_isolation_level,      
r.row_count, 
st.text  
FROM sys.dm_exec_requests r  
CROSS APPLY sys.dm_exec_sql_text(r.sql_handle) as st  
WHERE r.blocking_session_id = 0       
and r.session_id in       
(SELECT distinct(blocking_session_id) FROM sys.dm_exec_requests)  
GROUP BY r.session_id, r.plan_handle, r.sql_handle,
r.request_id, r.start_time, r.status, 
r.command, r.database_id, r.user_id, r.wait_type,      
r.wait_time, r.last_wait_type, r.wait_resource, 
r.total_elapsed_time, r.cpu_time, 
r.transaction_isolation_level, r.row_count, st.text  
ORDER BY r.total_elapsed_time desc

```

## Set Maximum Number of Concurrent Requests and Sessions

To set max concurrent request and sessions, run:

```sql
SELECT COUNT(*) AS [Concurrent_Requests] FROM sys.dm_exec_requests R
SELECT COUNT(*) AS [Sessions] FROM sys.dm_exec_connections

```
