The Virto Commerce xAPI now provides a comprehensive file upload architecture (X-Files) based on key principles to enhance developer experience, security, and extensibility. This architecture is designed to support different file providers, offer an intuitive developer experience, facilitate extensible post-processing, and seamlessly integrate with xAPI (GraphQL).

| Queries               	                            | Objects                                                      	                                                                        | Mutations      	|
|----------------------------------------------------	|------------------------------------------------------------------------------------------------------------------------------------	|----------------	|
| [fileUploadOptions](Queries/fileUploadOptions.md) 	| [FileUploadScopeOptionsType](Objects/FileUploadScopeOptionsType.md)<br> [DeleteFileCommandType](Objects/DeleteFileCommandType.md) 	| [deleteFile](Mutations/deleteFile.md) 	|

??? "Architecture"

    ![Architecture](media/file-upload.png)

[![Download module](../media/latest_release.png)](https://github.com/VirtoCommerce/vc-module-file-experience-api/releases)