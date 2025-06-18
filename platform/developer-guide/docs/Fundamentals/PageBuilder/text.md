# Text Control Descriptor

This control provides a rich-text editor based on [ckeditor-angular](https://www.npmjs.com/package/ckeditor4-angular). It allows users to format text using a WYSIWYG interface.

| Property   | Type   | Description                           |
| ---------- | ------ | ------------------------------------- |
| `config`   | object | [Configuration options](https://ckeditor.com/docs/ckeditor4/latest/api/CKEDITOR_config.html) for the editor. |

## Example

```json
...
    "settings": [
        {
            "id": "caption",
            "type": "text",
            "label": "Caption",
            "default": "Lorem ipsum"
        },
        ...
    ]
...
```


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../string">← String </a>
    <a href="../../Payments/new-payment-method-registration">Payments. New payment method →</a>
</div>