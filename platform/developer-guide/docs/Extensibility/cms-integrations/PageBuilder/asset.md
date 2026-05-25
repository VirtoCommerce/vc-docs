# Asset File

The **Asset file** model in the Virto Commerce Page Builder represents a file that has been uploaded or attached using the visual editor. It is used in components such as:

* [Images.](images.md)
* [Files.](files.md)
* [Markdown.](markdown.md)

This model extends the standard JavaScript [File](https://developer.mozilla.org/en-US/docs/Web/API/File) object, adding extra fields for use in upload workflows and rendering.

The **AssetFile** object serves as the **data model** for file upload requests and responses. When a user selects files to upload, each file is converted into an **AssetFile** and uploaded sequentially.

When uploading assets, each file is converted to an **AssetFile** and passed to the upload service, which is configured via the **settings.json** file.

## Interface

```ts
export interface AssetFile extends File {
    data?: any;                // Optional metadata from the component's descriptor
    url?: string;              // Full URL where the file is stored
    previewUrl: string | null; // URL for previewing the file (e.g., image thumbnail)
    assetName: string;         // Original or assigned name of the file
}
```

## Example 

```json title="settings.json"
{
  "uploadAssetsRequest": {
    "url": "/api/content/pages/{{location.params.storeId}}?folderUrl=/assets/pages&name={{file.assetName}}",
    "method": "POST",
    "form": {
      "name": "uploadedFile",
      "fileName": "{{file.assetName}}"
    },
    "response": {
      "result": "$[0].url",
      "isArray": false
    }
  }
}
```

**Expected response:**

The server is expected to return a response in the following structure:

```json
[
  {
    "url": "https://url.to.image",
    ...
  }
]
```

This response is then mapped to:

```ts
"https://url.to.image"
```

which is assigned to the `url` field of the **AssetFile**.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../component-context">← Component context </a>
    <a href="../calendar">Controls →</a>
</div>