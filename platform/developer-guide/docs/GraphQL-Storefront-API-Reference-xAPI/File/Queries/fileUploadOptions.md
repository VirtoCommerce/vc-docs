# fileUploadOptions ==~query~==

This query allows retrieving the file upload options for the specified scope.

## Arguments

| Argument                           | Description                                                    |
|------------------------------------|----------------------------------------------------------------|
| `scope` ==String!==                | Specifies the scope for which to retrieve file upload options. |


## Possible returns

| Possible return                                         	                            | Description                                                             |
|------------------------------------------------------------------------------------	  |------------------------------------------------------------------------	|
| [`FileUploadScopeOptionsType`](../Objects/FileUploadScopeOptionsType.md)              | Represents the options for file upload within the specified scope.    	|

## Example

<div class="grid" markdown>

```json title="Query"
query {
  fileUploadOptions(scope: "quote-attachments"){
    scope
    maxFileSize
    allowedExtensions
  }
}
```

```json title="Return"
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

</div>