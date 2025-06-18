# Number Control Descriptor

This control allows input of numeric values with optional constraints such as minimum, maximum, and step size. It can also display the current value inside the slider thumb if enabled.

| Property | Type    | Description                                                  |
| -------- | ------- | ------------------------------------------------------------ |
| `min`      | number  | Minimum allowed value.                                       |
| `max`      | number  | Maximum allowed value.                                       |
| `step`     | number  | Increment step for value changes.                            |
| `thumb`    | boolean | If true, displays the current value inside the slider thumb. |

## Example
### Numeric input field

<div class="grid" markdown>

```json
...
    "settings": [
        {
            "id": "amount",
            "type": "number",
            "label": "Amount",
            "min": 10,
            "max": 50,
            "step": 5
        },
        ...
    ]
...
```


![Number control](media/number-control.gif){: style="display: block; margin: 0 auto;" }


</div>


### Slider control

<div class="grid" markdown>

```json
...
    "settings": [
        {
            "id": "amount",
            "type": "slider",
            "label": "Amount",
            "min": 10,
            "max": 50,
            "step": 5,
            "thumb": true
        },
        ...
    ]
...
```


![Slider control](media/slider-control.png){: style="display: block; margin: 0 auto;" }


</div>

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../markdown">← Markdown </a>
    <a href="../object">Object →</a>
</div>
