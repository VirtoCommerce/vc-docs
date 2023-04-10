# Table Size Control

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