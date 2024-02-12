
You can view the list of [submitted quotes](../../../../storefront/user-guide/shopping/submit-quotes) via the `Quotes` module.

## Key Features

* **Isolation**: File upload operations are scoped, allowing for defined settings and isolation from mutations. The process involves uploading files to blob storage and then manipulating them via XAPI, creating the Xapi.FileUpload module.
* **Intuitive Developer Experience**: The file upload process supports different upload processes with customizable validation rules, such as file extensions, count, size limits, and antivirus scanning. Developers can access core validation settings by scope for client-side validation.
* **Extensible Post Processing**: File upload process supports post-processing actions like AI integration, leveraging a pipelines architecture for extensibility.
* **Ready to Use with Client Applications**: XAPI supports file usage with mutations and queries, enabling seamless integration with client applications.
* **Security**: Anonymous file uploads are disabled by default, ensuring a security-first approach. Clean answers are provided for security inquiries.

[![Download module](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-file-experience-api/releases)

[![Download module](media/latest_release.png)](https://github.com/VirtoCommerce/vc-module-file-experience-api/releases/latest)
