# Configure Asset Blob Storage

Blob is an abstraction that acts as a single point of access for all media files in your online store. Such files can be product images or attachments, PDF specifications, etc., regardless of their location or protocol.

By default, the Platform allows you to configure one of the following blob storage providers:

* [FileSystem.](03-configuring-asset-blob-storage.md#setting-up-filesystem-asset-storage-in-development-mode)
* [Azure Blob Storage.](03-configuring-asset-blob-storage.md#setting-up-azure-blob-storage-in-production-mode)

## Set up FileSystem asset storage in development mode

The FileSystem provider uses the local file system to store media files and make them publicly accessible. This mode implements [Static files in ASP.NET Core](https://docs.microsoft.com/en-us/aspnet/core/fundamentals/static-files?view=aspnetcore-6.0) with all files stored within the app local directory. The FileSystem storage provides public access to the files via relative URIs. 

To switch the Platform to using this provider, edit the `Assets` section of the **appsettings.json** file:

1. Specify `FileSystem` as your default asset provider in the line 2.
1. For `RootPath`, provide the base path to the `wwwroot` directory inside app folder in the line 4.
1. Provide the base URL that will be used when generating a public URI [ASP.NET](http://asp.net/ "http://ASP.NET") Core app serves directly in the line 5. Make sure both host and port are up-to-date and valid for your Platform instance.

```json title="appsettings.json"
"Assets": {
    "Provider": "FileSystem",
    "FileSystem": {
        "RootPath": "~/assets",
        "PublicUrl": "https://localhost:5001/assets/"
    }
},
```

??? Example

    You have an image file named *MyImage.jpg*.
    It is stored at wwwroot/assets/MyImage.jpg. 
    This file will be accessible through https://localhost:5001/assets/MyImage.jpg (a public URI), since [ASP.NET](http://asp.net/ "http://ASP.NET") marks all files in [wwwroot](https://docs.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-6.0#web-root "https://docs.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-6.0#web-root") as servable.

!!! note
    This mode is good for local development purposes and not recommended for production due to lack of scalability.

## Set up Azure Blob Storage in production mode

To set up Azure Blob Storage:

1. Create Azure Blob Storage according to this [quick start guide by Microsoft](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-portal).

1. Open **appsettings.json**.

1. Add the connection string under the `Assets` section.

    1. Specify `AzureBlobStorage` as your default asset provider in the line 2.
    1. In `ConnectionString`, provide the connection string of your storage account.

        ```json title="appsettings.json"
        "Assets": {
            "Provider": "AzureBlobStorage",
            "AzureBlobStorage": {
                "ConnectionString": "DefaultEndpointsProtocol=https;AccountName=<media account name>;AccountKey=<media account key>;EndpointSuffix=core.windows.net"
            }
        },
        ```

!!! tip
    You can get your connection string from your Azure Portal under the Access Keys section.

!!! note
    This mode is recommended for use in a production environment, since it enables sharing the asset storage across multiple Platform instances.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../02-configuring-email-notifications">← Configuring email notifications</a>
    <a href="../04-importing-sample-data">Importing sample data →</a>
</div>