# Configuring Cache
Cache configuration is commonly provided by the _Caching_ section of the _appsettings.json_ files:


``` json title="appsettings.json"
 "Caching": {
       "CacheEnabled": true, 
       "CacheSlidingExpiration": "0:15:00", 
       //"CacheAbsoluteExpiration": "0:15:00"
    }
```
Notes: 

+ `CacheEnabled`: Set to `false` to disable caching of application data for the entire application.

+ `CacheSlidingExpiration` or `CacheAbsoluteExpiration`: Sets a sliding or absolute expiration time for all cached application data that does not have a manually configured expiration value.
