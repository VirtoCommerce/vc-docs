# Find blocking queries in SQL Azure

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