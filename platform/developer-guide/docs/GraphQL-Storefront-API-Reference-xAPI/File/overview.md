Virto Commerce now offers an enhanced file upload solution, which prioritizes security and extensibility principles to elevate the developer experience. This architecture is designed to support different file providers and offer an intuitive developer experience.

This function is now used in our Storefront to [attach files to the created quotes](../../../../../storefront/user-guide/shopping/submit-quotes). However, developers can now add the file uploader to any segment, such as the Order module.  

| Queries               	                            | Objects                                                      	            | Mutations                                 |
|----------------------------------------------------	|-------------------------------------------------------------------------	|----------------	                        |
| [fileUploadOptions](Queries/fileUploadOptions.md) 	| [FileUploadScopeOptionsType](Objects/FileUploadScopeOptionsType.md)<br>  	| [deleteFile](Mutations/deleteFile.md) 	|

??? "Architecture"

    ![Architecture](media/file-upload.png)

    The file upload solution generally operates as follows:

    1. The developer integrates a form onto the quote page to gather files.
    2. Users attach files to the form.
    3. The form transmits the files to the **VirtoCommerce.FileExperienceApi** module.
    4. This module processes the files, generating secure links for them, and returns these links.
    5. The quote page then stores these links.


[![Download module](../media/latest_release.png)](https://github.com/VirtoCommerce/vc-module-file-experience-api/releases)