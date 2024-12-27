
To start uploading files from clients applications:

1. [Register the upload scope](getting-started.md#register-upload-scope)
1. [Query settings.](getting-started.md#register-upload-scope)
1. [Upload files.](getting-started.md#upload-files)
1. [Extend xAPI.](getting-started.md#extend-xapi)
1. [Implement security.](getting-started.md#implement-security)
1. [Download files.](getting-started.md#download-files)
1. [Delete files.](getting-started.md#delete-files)

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
        "AllowedExtensions": [ ".jpg", ".pdf", ".png", ".txt" ]
        "AllowAnonymousUpload": true
      }
    ]
  }
}
```

## Query settings

Use GraphQL to query file upload options for the desired scope from client application:

```graphql
query {
  fileUploadOptions(scope: "quote-attachments"){
    scope
    maxFileSize
    allowedExtensions
    allowAnonymousUpload
  }
}
```

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

Extend your XAPI queries and mutations to include file attachments with the safe file ID as needed for your application:

```graphql
mutation {
  addQuoteAttachments(
    command: {
      quoteId: "a73c6031-ab6a-4acc-9f16-466d287d7565"
      urls: [
        "/api/files/699fa784949a40c1acd891f74b4223d9"
        "/api/files/4c25e506a637407782bda5a5480f26a2"
      ]
    }
  )
}
```


## Implement security

Implement security callback to control access to files based on your application's requirements with implementation of `IFileAuthorizationRequirementFactory`.

## Download files

Use the provided API endpoint to download files using the safe file ID obtained during upload:

```bash
GET https://<YOUR-DOMAIN>/api/files/<safe-file-id>
```

## Delete files

Use `deleteFile` mutation to remove file from storage:

```graphql
mutation {
  deleteFile(
    command: {
      id: "d6e575f9633946f19b9791eee0db5e1f"
    }
  )
}
```