# Color Control Descriptor

This control uses the [ngx-color](https://ngx-color.vercel.app/) color picker. The [npm package](https://www.npmjs.com/package/ngx-color) is also available.

| Property       | Type                 | Description                                                                   |
| -------------- | -------------------- | ----------------------------------------------------------------------------- |
| `colorMode`    | color <br> presets   | Use the Sketch picker for `color` mode, and the Twitter picker for `presets`. |
| `disableAlpha` | boolean            | Removes the alpha (transparency) slider and options.                          |
| `clearValue`   | string             | Text shown for the clear/reset button.                                        |
| `inline`       | boolean            | Displays the color picker inline instead of as a popup.                       |
| `presets`      | string[]           | List of predefined color values used in `presets` mode.                       |


## Examples
### Color picker in HSLA format

<div class="grid" markdown>

```json
...
    "settings": [
        {
            "id": "headerColor",
            "label": "Header color",
            "type": "color",
            "outputFormat": "hsla"
        },
        ...
    ]
...
```

![Color picker in HSLA format](media/color-picker-popup.png){: style="display: block; margin: 0 auto;" }


</div>


### Color picker displayed inline

<div class="grid" markdown>

```json
        "settings": [
            {
                "id": "headerColor",
                "label": "Header color",
                "type": "color",
                "inline": "true"
            },
            ...
        ]
    ```

...
```

![Inline color picker](media/color-picker-inline.png){: style="display: block; margin: 0 auto;" }


</div>


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../collection">← Collection </a>
    <a href="../files">Files →</a>
</div>