# Overview

The File Experience API (xFile) module manages all file-related operations from file upload to file content download for various client applications. 

Its architecture is designed to:

* Support different file providers.
* Offer an intuitive developer experience.
* Facilitate extensible post-processing.
* Seamlessly integrate with xAPI (GraphQL).

## Key features

The xFiles modules provides the following features:

* **Isolation**: File upload operations are scoped, allowing for defined settings and isolation from mutations. The process involves uploading files to blob storage and then manipulating them via xAPI, creating the Xapi.FileUpload module.
* **Intuitive developer experience**: The file upload process supports different upload processes with customizable validation rules, such as file extensions, count, size limits, and antivirus scanning. Developers can access core validation settings by scope for client-side validation.
* **Extensible post processing**: File upload process supports post-processing actions like AI integration, leveraging a pipelines architecture for extensibility.
* **Ready to use with client applications**: xAPI supports file usage with mutations and queries, enabling seamless integration with client applications.
* **Security**: Anonymous file uploads are disabled by default, ensuring a security-first approach. Clean answers are provided for security inquiries.

[![Download module](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-file-experience-api/releases)

[![Download module](media/latest_release.png)](https://github.com/VirtoCommerce/vc-module-file-experience-api/releases/latest)
