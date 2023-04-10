# Finding and Creating Missing Index

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