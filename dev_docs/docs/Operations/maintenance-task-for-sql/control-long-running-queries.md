# Control and Elimination of Long-Running Queries

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