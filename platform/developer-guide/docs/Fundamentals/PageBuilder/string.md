# String Control Descriptor

This control is used to input short or long text values. You can configure it to allow single-line or multi-line input.

| Property  | Type    | Description                             |
| --------- | ------- | --------------------------------------- |
| `multiline` | boolean | Allows entering text in multiple lines. |

## Example


<div class="grid" markdown>

```json
...
    "settings": [
        {
            "id": "title",
            "type": "string",
            "label": "Title",
            "placeholder": "Please enter title"
        },
        {
            "id": "message",
            "type": "string",
            "label": "Message",
            "placeholder": "Please enter message",
            "multiline": true
        },
        ...
    ]
...
```


![String control](media/string-control.png){: style="display: block; margin: 0 auto;" }


</div>

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../select">← Select </a>
    <a href="../text">Text →</a>
</div>