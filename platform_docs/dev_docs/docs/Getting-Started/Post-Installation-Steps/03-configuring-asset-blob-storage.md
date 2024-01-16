# Configuring Asset Blob Storage

Blob is an abstraction that works as a single point of access to all media files in your online store. Such files could be product images or attachments, PDF specs, etc., regardless of their location or protocol.

By default, the platform allows you to configure one of the following blob storage providers:

-   FileSystem.
    
-   Azure Blob Storage.

## Setting Up FileSystem Asset Storage in Development Mode

The FileSystem provider uses the local file system to store and provide public access to all media files. This mode implements [Static files in ASP.NET Core](https://docs.microsoft.com/en-us/aspnet/core/fundamentals/static-files?view=aspnetcore-6.0) with all files stored within the app local directory. The FileSystem storage provides public access to the files via relative URIs. 

To switch platform to using this provider, edit the `Assets` section of the **appsetting.json** file:

1. Specify `FileSystem` as your default asset provider in the line 2.
1. For `RootPath`, provide the base path to the `wwwroot` directory inside app folder in the line 4.
1. Provide the base URL that will be used when generating a public URI [ASP.NET](http://asp.net/ "http://ASP.NET") Core app serves directly in the line 5. Make sure both host and port are up-to-date and valid for your platform instance.

``` title="appsettings.json"
1 "Assets": {
2        "Provider": "FileSystem",
3        "FileSystem": {
4            "RootPath": "~/assets",
5            "PublicUrl": "https://localhost:5001/assets/"
6        }
7    },
```

??? Example

    You have an image file named *MyImage.jpg*.
    It is stored at wwwroot/assets/MyImage.jpg. 
    This file will be accessible through https://localhost:5001/assets/MyImage.jpg (a public URI), since [ASP.NET](http://asp.net/ "http://ASP.NET") marks all files in [wwwroot](https://docs.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-6.0#web-root "https://docs.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-6.0#web-root") as servable.

!!! note
    This mode is good for local development purposes and not recommended for production due to lack of scalability.

### Setting up Azure Blob Storage in Production Mode

To set up Azure blob storage:

1. Create Azure blob storage according to this [quick start guide by Microsoft](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-portal).

1. Open **appsettings.json**.

1. Add the connection string under the `Assets` section.

    1. Specify `AzureBlobStorage` as your default asset provider in the line 2.
    1. In `ConnectionString`, provide the connection string of your storage account.

        ``` title="appsettings.json"
        1 "Assets": {
        2        "Provider": "AzureBlobStorage",
        3        "AzureBlobStorage": {
        4            "ConnectionString": "DefaultEndpointsProtocol=https;AccountName=<media account name>;AccountKey=<media account key>;EndpointSuffix=core.windows.net"
        5        }
        6    },
        ```

!!! tip
    You can get your connection string from your Azure Portal under the Access Keys section.

!!! note
    This mode is recommended for using in production environment since it enables sharing the asset storage across multiple platform instances.
