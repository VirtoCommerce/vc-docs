# Collection Control Descriptor

This control allows the user to manage a list of repeatable items, each defined by its own set of nested fields.

| Property                 | Type                  | Description                                                          |
| ------------------------ | --------------------- | -------------------------------------------------------------------- |
| `addText`                | string                | Text for the “Add item” button. Default is `Add item`.               |
| `displayField`           | string                | Property name used to display a collection item in the list.         |
| `skipRemoveConfirmation` | boolean               | If **true**, skips the confirmation dialog when removing an item.      |
| `removeMessage`          | string                | Custom message for the item removal confirmation dialog.             |
| `elementDescriptor`      | string                | Name of the object in the `objects` folder to be used as a template. |
| `element`                | ControlDescriptor[] | Describes the structure of each collection item.                     |

## Example


<div class="grid" markdown>

```json
...
    "settings": [
        {
            "id": "formFields",
            "label": "Fields list",
            "type": "list",
            "addText": "Add a field",
            "displayField": "labelText",
            "element": [
                {
                    "id": "fieldType",
                    "label": "Type",
                    "type": "select",
                    "default": "text",
                    "options": [
                        { "value": "checkbox", "label": "Checkbox" },
                        { "value": "text", "label": "Text" }
                    ]
                },
                {
                    "id": "fieldName",
                    "label": "Name",
                    "type": string  
                },
                {
                    "id": "labelText",
                    "label": "Label",
                    "type": string  
                }
            ],
            "default": [
                {
                    "fieldType": "text",
                    "fieldName": "fullname",
                    "labelText": "Full name"
                },
                {
                    "fieldType": "text",
                    "fieldName": "email",
                    "labelText": "Email"
                },
                {
                    "fieldType": "checkbox",
                    "fieldName": "accept",
                    "labelText": "By clicking \"Submit\" I understand that I consent to opt-in to the Terms and Policy"
                }
            ]
        },
        ...
    ]
...
```

![List control](media/list-control.png){: style="display: block; margin: 0 auto;" }


</div>


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../checkbox">← Checkbox </a>
    <a href="../color">Color →</a>
</div>