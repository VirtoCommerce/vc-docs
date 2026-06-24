# FileUploadScopeOptionsType ==~object~==

This type represents the options for file upload within a specific scope.

## Fields

| Field                             | Description                                                   |
|-----------------------------------|---------------------------------------------------------------|
| `scope` ==String!==               | Specifies the scope for which to retrieve file upload options.|
| `maxFileSize` ==Long!==           | Maximum allowed file size for uploads, in bytes.              |
| `allowedExtensions` ==[String]!==  | A list of file extensions that are permitted for uploads.      |
| `allowAnonymousUpload` ==Boolean!==| Indicates whether anonymous users are allowed to upload files. |

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../Queries/fileUploadOptions">← FileUploadOptions query</a>
    <a href="../DeleteFileCommandType">DeleteFileCommandType →</a>
</div>
