
To start uploading files from clients applications:

1. [Register the upload scope.](#register-upload-scope)
1. [Query settings.](#query-settings)
1. [Upload files.](#upload-files)
1. [Extend xAPI.](#extend-xapi)
1. [Implement security.](#implement-security)
1. [Download files.](#download-files)
1. [Delete files.](#delete-files)

For demonstration purposes, let's use the **Quotes** module and the Frontend Application as examples of how to use **File xAPI** module.

## Register upload scope

Update **appsettings.json** with file upload scope settings:

```json title="appsettings.json"
{
  "FileUpload": {
    "RootPath": "attachments",
    "Scopes": [
      {
        "Scope": "quote-attachments",
        "MaxFileSize": 123,
        "AllowedExtensions": [ ".jpg", ".pdf", ".png", ".txt" ],
        "AllowAnonymousUpload": true
      }
    ]
  }
}
```

## Query settings

Use GraphQL to [query file upload options](Queries/fileUploadOptions.md) for the desired scope from client application.


## Upload files

Use the provided API endpoint to upload files as multipart/form-data and obtain a safe file ID:

```bash
POST https://<YOUR-DOMAIN>/api/files/quote-attachments
Content-Type: multipart/form-data
...
```

```bash
curl.exe -k -F file=@test.txt https://<YOUR-DOMAIN>/api/files/quote-attachments?api_key=***
```

## Extend xAPI

Extend your xAPI queries and mutations to [include file attachments](../Quote/mutations/addQuoteAttachments.md) with the safe file ID as needed for your application.


## Implement security

Implement security callback to control access to files based on your application's requirements with implementation of `IFileAuthorizationRequirementFactory`.

## Download files

Use the provided API endpoint to download files using the safe file ID obtained during upload:

```bash
GET https://<YOUR-DOMAIN>/api/files/<safe-file-id>
```

## Delete files

Use the [deleteFile](Mutations/deleteFile.md) mutation to remove file from storage.