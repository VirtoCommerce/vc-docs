# Cache Configuration

Cache is commonly configured in the `Caching` section of the [appsettings.json file](../../Configuration-Reference/appsettingsjson.md#caching):

{%
   include-markdown "../../Configuration-Reference/appsettingsjson.md"
   start="<!--caching-start-->"
   end="<!--caching-end-->"
%}

!!! note 
    `CacheSlidingExpiration` or `CacheAbsoluteExpiration` set a sliding or absolute expiration time for all cached application data that does not have a manually configured expiration value.
