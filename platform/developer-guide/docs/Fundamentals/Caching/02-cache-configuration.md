# Cache Configuration

Cache is commonly configured in the **Caching** section of the [appsettings.json file](/platform/developer-guide/latest/Configuration-Reference/appsettingsjson.md#caching):

{%
   include-markdown "platform/developer-guide/Configuration-Reference/appsettingsjson"
   start="<!--caching-start-->"
   end="<!--caching-end-->"
%}

!!! note 
    `CacheSlidingExpiration` or `CacheAbsoluteExpiration` set a sliding or absolute expiration time for all cached application data that does not have a manually configured expiration value.


<br>
<br>
![Readmore](media/readmore.png){: width="25"} [Configuration reference](/platform/developer-guide/latest/Configuration-Reference/appsettingsjson)




<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../01-overview">← Overview</a>
    <a href="../03-setting-up-redis">Setting up Redis →</a>
</div>
