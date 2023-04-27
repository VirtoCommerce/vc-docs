# Configuring Cache
Cache is commonly configured in the `Caching` section of the [appsettings.json file](../../Configuration-Reference/appsettingsjson.md):

``` json title="appsettings.json"
 "Caching": {
       "CacheEnabled": true, 
       "CacheSlidingExpiration": "0:15:00", 
       //"CacheAbsoluteExpiration": "0:15:00"
    }
```
## Values Description 

| Node | Default or Sample Value | Description  |
| ------------- | ------------------------ | ------------ |
| `CacheEnabled` | <ul><li>`true`</li><br><li>`false`</li></ul> | <ul><li>Cache entries are retained based on the expiration settings.</li><li>Disables caching of application data for the entire application.</li></ul> Used when `ConnectionStrings:RedisConnectionString` is not specified.
| `CacheSlidingExpiration` | `"0:15:00"` | The cache entry will expire if it is not accessed for a specified amount of time.<br>Used when `CacheAbsoluteExpiration` is not defined.
| `CacheAbsoluteExpiration` | `"0:5:00"` | The Cache entry will expire after a specified amount of time. <br>Used when `RedisConnectionString` is not specified.


!!! Note 

    `CacheSlidingExpiration` or `CacheAbsoluteExpiration` set a sliding or absolute expiration time for all cached application data that does not have a manually configured expiration value.
