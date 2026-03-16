# Object Control Descriptor

This control allows you to edit complex objects composed of multiple fields. You can define the object editor either inline using the `element` property or reference an external descriptor file with `elementDescriptor`. The control supports showing a collapsed summary by specifying which property to display.

| Property            | Type                 | Description                                                         |
| ------------------- | -------------------- | ------------------------------------------------------------------- |
| `title`             | string               | Title of the object editor.                                         |
| `displayField`      | string               | Name of the property used to display the object when collapsed.     |
| `element`           | ControlDescriptor\[] | List of descriptors that define the object’s fields inline.         |
| `elementDescriptor` | string               | Name of the object descriptor file located in the `objects` folder. |

## Examples

### Inline settings schema

```json
...
    "settings": [
        {
            "id": "button",
            "label": "Describe a button",
            "type": "object",
            "title": "The button",
            "displayField": "caption",
            "element": [
                {
                    "id": "caption",
                    "type": "string",
                    "label": "Caption"
                },
                {
                    "id": "action",
                    "type": "select",
                    "label": "onClick action",
                    "default": "popup",
                    "options": [
                        { "label": "Show popup", "value": "popup" },
                        { "label": "Go to link", "value": "url" }
                    ]
                },
                {
                    "id": "url",
                    "type": "string",
                    "label": "Enter link",
                    "visibility": "!!this.item && this.item.action === 'url'"
                }
            ]
        },
        ...
    ]
...
```

**Inline settings result**:

```json
{
    "button": {
        "caption": "Buy now!",
        "action": "url",
        "url": "https://virtocommerce.com"
    }
}
```

### External elementDescriptor schema

You can also define the object editor separately in a file (e.g., `buttonEditor.json`) inside the `theme/config/objects/` folder:

```json
{
    "settings": [
        {
            "id": "caption",
            "type": "string",
            "label": "Caption"
        },
        {
            "id": "action",
            "type": "select",
            "label": "onClick action",
            "default": "popup",
            "options": [
                { "label": "Show popup", "value": "popup" },
                { "label": "Go to link", "value": "url" }
            ]
        },
        {
            "id": "url",
            "type": "string",
            "label": "Enter link",
            "visibility": "!!this.item && this.item.action === 'url'"
        }
    ]
}
```

You can reference this descriptor from your main settings:

```json
{
    ...
    "settings": [
        {
            "id": "button",
            "label": "Describe a button",
            "type": "object",
            "title": "The button",
            "displayField": "caption",
            "elementDescriptor": "buttonEditor"
        },
        ...
    ]
}
```


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../number">← Number </a>
    <a href="../paragraph">Paragraph →</a>
</div>