# Configuration

You can manage notification configuration through the `Notifications` node in the `appsettings.json` file, which has the following settings:

`Notifications:DiscoveryPath`: Relative folder path in the local file system that will be used to discover notification template files during notification rendering. Its default value is `Templates`.

`Notifications:FallbackDiscoveryPath`: Alternative relative folder path in the local file system that will be used to discover alternative template files during notification rendering. Templates found through this path will be used as backup, in case the templates defined in the `Notifications:DiscoveryPath` setting are not found.

!!! note
	You can find more info on configuring notifications through the `appsettings.json` file [here](../Configuration-Reference/appsettingsjson.md#notifications).
