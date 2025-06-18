# Calendar Control Descriptor

This control allows users to select dates, times, or both, using a configurable date/time picker based on [datetime-picker](https://h2qutc.github.io/angular-material-components).

| Property  | Type                                                | Description                                                                 |
| --------- | --------------------------------------------------- | --------------------------------------------------------------------------- |
| `mode`    | date <br> datetime <br> time <br> month <br> year   | Defines the mode of the calendar: full datetime, date only, time only, etc. |
| `minDate` | date                                                | The minimum selectable date.                                                |
| `maxDate` | date                                                | The maximum selectable date.                                                |
| `inline`  | boolean                                             | Displays the calendar inline instead of as a popup.                         |



## Example

```json
...
    "settings": [
        {
            "id": "date",
            "label": "Date",
            "type": "calendar",
            "placeholder": "Please choose a date",
            "hint": "You can select date in calendar",
            "info": "This control returns a JavaScript Date object"
        },
        ...
    ]
...
```

Some of the available calendar modes are as follows:

![Calendar modes](media/calendar-modes.png)

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../component-context">← Component context </a>
    <a href="../checkbox">Checkbox →</a>
</div>