# Select Control Descriptor

This control presents a dropdown list of options to the user. This control supports static options, dynamic options from the current component context, or options fetched from an external server.

## Descriptor properties

| Property          | Type             | Description                                                                                                                                            |
| ----------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `options`         | OptionModel[]  | Array of static options to display in the dropdown.<br> These values can be grouped using the `group` property.                                        |
| `optionsSelector` | string         | JavaScript snippet to dynamically generate options from the current [`ComponentContext`](component-context.md).<br>Ignored if `request` is defined.      |
| `request`         | OptionsRequest | Configuration to fetch options via a web [request](server-descriptors.md#serverrequestdescriptor).<br>The `label` property from the result will be used for display,<br>and the option's value is taken from the corresponding field.<br>The fetched data is merged with the array from `options`.                                                                          |
| `equalKey`        | string         | Compares values between the current value and available options.                                                                                         |
| `filterList`      | boolean        | Enables filtering the option list in the UI.                                                                                                             |
| `multiple`        | boolean        | Enables multi-select.                                                                                                                                    |

**Example**:

```js
this.page.filter(function(x) { return x.type==='popup' }).map(function(x) { return { label: x.name || x.__id, value: x.__id }; })
```

This script filters all blocks on the page by type (`popup`) and maps the results to a list of options with `label` and `value` fields.

The resulting list is **merged with the static options** provided via the `options` property, if any.

If the control already has a pre-defined value, it will be matched **using the `equalKey`** after all data (static, selector-based, and/or fetched) is loaded.



## Supporting types

The following types define the structure of values used within the select control — including individual options, how options are loaded from a server, and how values are extracted from responses.

### OptionModel

Defines the shape of a single dropdown option:

| Property | Type     | Description         |
| -------- | -------- | ------------------- |
| `label`  | string   | Text shown in UI    |
| `value`  | any      | Option's value      |
| `group`  | string   | Optional group name |


### OptionsRequest

Extends a generic request definition and adds fields to specify which parts of the server response should be used as labels and groups for the select options:

| Property | Type     | Description                              |
| -------- | -------- | ---------------------------------------- |
| `label`  | string | Field name used for displaying the label |
| `group`  | string | (Optional) Field name used for grouping  |

See full details in the [ServerRequestDescriptor](server-descriptors.md#serverrequestdescriptor) documentation.


### SelectValueDescriptor

Extracts the actual `value` for each option from a server response. 

| Property  | Type      | Description                    |
| --------- | --------- | ------------------------------ |
| `key`     | string  | Property name of the value field |
| `query`   | string  | JSONPath to extract value        |
| `isArray` | boolean | Whether the value is an array    |



## Examples

### Basic select

<div class="grid" markdown>

```json
...
    "settings": [
        {
            "id": "theme",
            "type": "select",
            "label": "Theme",
            "placeholder": "Please select theme",
            "options": [
                { "label": "Base", "value": "base" },
                { "label": "Red", "value": "red" },
                { "label": "Green", "value": "green" },
                { "label": "Blue", "value": "blue" }
            ]
        },
        ...
    ]
...
```

![Basic select result](media/basic-select-result.png){: style="display: block; margin: 0 auto;" }

</div>

### Server request

<div class="grid" markdown>

```json
...
    "settings": [
        {
            "id": "category",
            "label": "Choose category",
            "type": "select",
            "equalKey": "id",
            "default": null,
            "request": {
                "url": "/api/reverse-proxy/{{location.params.storeId}}/odt/api/catalog/search/categories",
                "method": "post",
                "body": {
                    "objectType": "Category",
                    "catalogId": "4974648a41df4e6ea67ef2ad76d7bbd4"
                },
                "response": {
                    "result": "items",
                    "isArray": true,
                    "value": [
                        "id",
                        "name"
                    ]
                },
                "label": "name"
            }
        },
        ...
    ]
...
```

    
![Server request result](media/server-request-result.png){: style="display: block; margin: 0 auto;" }


</div>

### Context-based options

<div class="grid" markdown>

```json
...
    "settings": [
        {
            "id": "popupId",
            "label": "Select target popup",
            "type": "select",
            "optionsSelector": "this.page.filter(x => x.type==='popup').map(x => ({ label: x.name || x.__id, value: x.__id }))"
        },
        ...
    ]
...
```


![Context-based select](media/select-control-context-page.png){: style="display: block; margin: 0 auto;" }

</div>

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../search">← Search </a>
    <a href="../string">String →</a>
</div>