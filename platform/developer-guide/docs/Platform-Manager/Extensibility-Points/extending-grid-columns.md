To extend grid columns, get `platformWebApp.ui-grid.extension` in the module run function, and then register the extension function to add a custom column permanently (data-independent) into the list.

```js title="order2.js"
...
gridOptionExtension.registerExtension("customerOrder-list-grid", function (gridOptions) {
    var customColumnDefs = [
        { name: 'newField', displayName: 'orders.blades.customerOrder-list.labels.newField', width: '***' }
    ];

    gridOptions.columnDefs = _.union(gridOptions.columnDefs, customColumnDefs);
});
...
```

This allows you to add a column that will always be available.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../widgets">← Widgets </a>
    <a href="../blade-toolbar">Blade toolbar  →</a>
</div>