## Extending Grid Columns

To extend grid columns, get `platformWebApp.ui-grid.extension` in the module run function, and then register the extension function to add a custom column permanently (data-independent) into the list.

*`order2.js`*
```JS
...
gridOptionExtension.registerExtension("customerOrder-list-grid", function (gridOptions) {
    var customColumnDefs = [
        { name: 'newField', displayName: 'orders.blades.customerOrder-list.labels.newField', width: '***' }
    ];

    gridOptions.columnDefs = _.union(gridOptions.columnDefs, customColumnDefs);
});
...
```

This will allow you to add a column that will be always available.