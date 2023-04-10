# Index Defragmentation and Rebuilding

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

