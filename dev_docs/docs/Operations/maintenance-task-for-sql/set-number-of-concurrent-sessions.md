# Setting Maximum Number of Concurrent Requests and Sessions

To set max concurrent request and sessions, run:
```sql
SELECT COUNT(*) AS [Concurrent_Requests] FROM sys.dm_exec_requests R
SELECT COUNT(*) AS [Sessions] FROM sys.dm_exec_connections

```