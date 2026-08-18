# Markdown Control Descriptor

This control provides a Markdown editor. The content can be saved as Markdown, HTML, or both formats simultaneously.

| Property            | Type                            | Description                                                                         |
| ------------------- | ------------------------------- | ----------------------------------------------------------------------------------- |
| `resultType`          | markdown <br>html <br> mixed    | Determines the output format.                                                       |
| `styles`              | string[] <br> string            | Links to CSS files for styling the preview pane.<br>Be careful with CORS restrictions. |
| `uploadAssetsRequest` | AssetsRequest                 | Descriptor used to upload images pasted from the clipboard.                         |
| `urlField`            | string                          | Field name used for the image URL.                                                  |
| `filenameField`       | string                          | Field name used for the alt text of pasted images.                                  |

When the resultType is `markdown` or `html`, the control returns a string. For `mixed`, the value is an object containing both `markdown` and `html` properties.

If resultType is set to `html`, the editor converts the HTML back to Markdown using the [turndown](https://github.com/mixmark-io/turndown) library.

## Example


<div class="grid" markdown>

```json
...
    "settings": [
        {
            "id": "content",
            "label": "Content",
            "type": "markdown",
            "resultType": "mixed"
        },
        ...
    ]
```

```json
{
    "content": [
        {
            "type": "markdown-example",
            "content": {
                "markdown": "## Markdown example",
                "html": "<h2>Markdown example</h2>"
            }
        }
    ] 
}
```

</div>

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../images">← Images </a>
    <a href="../number">Number →</a>
</div>