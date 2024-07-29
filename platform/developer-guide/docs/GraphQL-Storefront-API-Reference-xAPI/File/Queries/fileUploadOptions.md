# fileUploadOptions ==~query~==

This query allows retrieving the file upload options for the specified scope.

## Arguments

| Argument                           | Description                                                    |
|------------------------------------|----------------------------------------------------------------|
| `scope` ==String!==                | Specifies the scope for which to retrieve file upload options. |
| `maxFileSize` ==Long!==            | The maximum size, in bytes, allowed for each uploaded file.    |
| `allowedExtensions` ==[String]!==  | A list of file extensions that are permitted for uploads.      |
| `allowAnonymousUpload` ==Boolean!==| Indicates whether anonymous users are allowed to upload files. |

## Possible returns

| Possible return                                         	                            | Description                                                             |
|------------------------------------------------------------------------------------	  |------------------------------------------------------------------------	|
| [`FileUploadScopeOptionsType`](../Objects/FileUploadScopeOptionsType.md)              | Represents the options for file upload within the specified scope.    	|

## Examples

=== "Query"
    ```graphql linenums="1"
    query {
      fileUploadOptions(scope: "quote-attachments"){
        scope
        maxFileSize
        allowedExtensions
      }
    }
    ```

=== "Return"
    ```graphql linenums="1"
    {
      "data": {
        "fileUploadOptions": {
          "scope": "quote-attachments",
          "maxFileSize": 10485760,
          "allowedExtensions": [
            ".csv",
            ".docx",
            ".jpg",
            ".pdf",
            ".png",
            ".txt",
            ".xlsx"
          ]
        }
      }
    }
    ```
