# Files Control Descriptor

This control uses the [file-upload](https://pivan.github.io/file-upload/) component. The corresponding [npm package](https://www.npmjs.com/package/@iplab/ngx-file-upload) is also available.

| Property                 | Type                  | Description                                                                                                                            |
| ------------------------ | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `accept`                 | string              | Comma-separated list of accepted file extensions or MIME types.<br>Used directly in [`accept`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/file#accept) attribute. |
| `multiple`               | boolean               | Allows multiple file uploads. Default is `true`.                                                                                 |
| `sortable`               | boolean               | Allows files to be reordered. Default is `true`.                                                               |
| `maxFileSize`            | number                | Maximum allowed file size (in bytes).                                                                                            |
| `collapseThreshold`      | number                | Number of files after which the preview panel collapses. Default is `6`.                                                         |
| `collapseCount`          | number                | Number of file previews shown in collapsed state. Default is `4`.                                                                |
| `skipRemoveConfirmation` | boolean               | Skips the confirmation prompt when removing a file.                                                                              |
| `removeMessage`          | string              | Message shown in the remove confirmation dialog.                                                                                 |
| `urlField`               | string              | Field name containing the file URL (if value is an object).                                                                      |
| `filenameField`          | string              | Field name containing the filename (if value is an object).                                                                      |
| `element`                | ControlDescriptor[] | Additional descriptors for custom fields in the file object.                                                                     |
| `UploadAcceptRequest`    | <br> AssetsRequest<br> string <br> inline       | Custom request descriptor used to upload assets.                                                     |

The value of this control is an array of URLs by default, or an array of objects if the `element` property is defined.

If `uploadAssetsRequest` is **inline**, the file will be converted into **base64** and stored directly into page, without uploading to server. Such image can be used as the [data URL](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Schemes/data).

If `uploadAssetsRequest` is **string**, it should be property name from the [builder settings](settings.md) object. Also it can be just [ServerRequestDescriptor](server-descriptors.md#serverrequestdescriptor) object, which will be used to upload files to server.

If `uploadAssetsRequest` is not defined, the default request will be used, which is defined in [builder settings](settings.md) as `uploadAssetsRequest`.

## Examples
### Single file


```json
...
    "settings": [
        {
            "id": "attachment",
            "label": "Attach a file",
            "type": "files",
            "multiple": false,
            "accept": ".pdf,application/pdf"
        },
        ...
    ]
...
```

**Result**
<div class="grid" markdown>

![Single file](media/file-control-single.gif)

```json
...
    "content": [
        {
            "attachment": "https://localhost:5001/cms-content/Pages/B2B-store/assets/pages/contract.pdf"
            ...
        },
        ...
    ]
...
```
</div>



### Multiple files

```json
...
    "settings": [
        {
            "id": "attachment",
            "label": "Attach a file",
            "type": "files",
            "multiple": false,
            "accept": ".pdf,application/pdf"
        },
        ...
    ]
...
```

**Result**

<div class="grid" markdown>

![Multiple files](media/file-control.png)

```json
...
    "content": [
        {
            "attachments": [
              "https://localhost:5001/cms-content/Pages/B2B-store/assets/pages/2-requerimento.pdf",
              "https://localhost:5001/cms-content/Pages/B2B-store/assets/pages/89e49b95-98e5-43fe-a250-3746af0660bf.pdf",
              "https://localhost:5001/cms-content/Pages/B2B-store/assets/pages/6268a3827af6a8c184ce400727.pdf",
              ...
            ]
            ...
        },
        ...
    ]
...
```
</div>



### Files as objects

```json
...
    "settings": [
        {
            "id": "attachments",
            "label": "Attach files",
            "type": "files",
            "urlField": "url",
            "filenameField": "filename",
            "element": [
                {
                    "id": "filename",
                    "type": "string",
                    "label": "File name"
                },
                {
                    "id": "url",
                    "type": "string",
                    "label": "File url"
                },
                {
                    "id": "altText",
                    "type": "string",
                    "label": "Alternative text"
                }
            ]
        },
        ...
    ]
...
```

**Result**

<div class="grid" markdown>

![Multiple files](media/file-control-object.png)

```json
...
    "content": [
        {
            "attachments": [
                {
                    "filename": "2-requerimento.pdf",
                    "url": "https://localhost:5001/cms-content/Pages/B2B-store/assets/pages/2-requerimento.pdf",
                    "altText": "Requerimento"
                },
                {
                    "filename": "89e49b95-98e5-43fe-a250-3746af0660bf.pdf",
                    "url": "https://localhost:5001/cms-content/Pages/B2B-store/assets/pages/89e49b95-98e5-43fe-a250-3746af0660bf.pdf",
                    "altText": "Another file"
                },
                ...
            ]
            ...
        },
        ...
    ]
...
```


</div>

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../color">← Color </a>
    <a href="../header">Header →</a>
</div>