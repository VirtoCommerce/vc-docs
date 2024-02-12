# FileUploadScopeOptionsType ==~object~==

The `FileUploadScopeOptionsType` represents the options for file upload within a specific scope.

## Fields

| Field                             | Description                                                   |
|-----------------------------------|---------------------------------------------------------------|
| `scope` ==String!==               | Specifies the scope for which to retrieve file upload options.|
| `maxFileSize` ==Long!==           | Maximum allowed file size for uploads, in bytes.              |
| `allowedExtensions` ==[String]!== | List of file extensions allowed for uploads within the scope. |
