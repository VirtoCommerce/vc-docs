# Images Control Descriptor

This control functions similarly to the [files control](files.md), but with a default `accept` value set to `image/*`.

## Example

<div class="grid" markdown>

```json
...
    "settings": [
        {
            "id": "image",
            "label": "Image",
            "type": "images",
            "default": {
                "url": "/themes/assets/blocks/portfolio.png"
            }
        },
        ...
    ]
...
```


![Header control](media/image-control.png){: style="display: block; margin: 0 auto;" }


</div>

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../header">← Header </a>
    <a href="../markdown">Markdown →</a>
</div>