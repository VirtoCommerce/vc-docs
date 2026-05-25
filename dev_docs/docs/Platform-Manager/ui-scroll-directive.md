## Introduction
Generic UI scroll directive helps developers add dropdown lists to the UI and bind them to a custom data source. 

## Using Directive

UI scroll is implemented as the `uiScrollDropDown` Angular.js directive and has the following features:

+ Bound to a search resource function allowing pagination and filtering 
+ Enables single select drop down list or multiple select
+ Allows binding to a custom data source
+ Can define data filter expression
+ Supports events

### Basic Usage Example
This is how UI scroll directive would work in an HTML template:

```HTML
<form>
...
    <ui-scroll-drop-down 
        ng-model="blade.currentEntity.mainReturnsFulfillmentCenterId"
        data="searchFulfillmentCenters(criteria)"
        placeholder="'stores.blades.store-advanced.placeholders.fulfillment-center'">
    </ui-scroll-drop-down>
...
</form>
```

This is how it will work in an underlying `.js` file:

```JS
$scope.searchFulfillmentCenters = function (criteria) {
    return fulfillments.search(criteria);
}
```

## Parameters

|Parameter|Description|
|---------|-----------|
|data|Function that provides data to the dropdown list.
|filter|Function that will be applied to the data after each page fetch.|
|multiple|Manages single select or multiple dropdown select mode.|
|onSelect|Function that is triggered when a value is selected.|
|onRemove|Function that is triggered when the selected value is cleared or removed.|
|pageSize|Manages page size on a single scroll (default at 20).|
|placeholder|Defines the text that is displayed when the dropdown value is not selected.|
|isRequired|The *required* flag value of the underlying `ui-select` directive (*false* by default).|
|isReadOnly|The *disabled* flag value oof the underlying `ui-select` directive (*false* by default).|

## Examples

### Data Function 
The data function should either return a resource call result (`$promise`) or an array of predefined objects:

```HTML
<ui-scroll-drop-down 
    ng-model="currentEntity"
    data="getData(criteria)">
</ui-scroll-drop-down>
```
Server call:

```JS
$scope.getData = function (criteria) {
    return resource.search(criteria);
}
```
Predefined data array:

```JS
$scope.currentEntity = 'ID2';
$scope.getData = function () {
    return [{ id: 'ID1', name: 'name 1' }, { id: 'ID2', name: 'name 2' }, { id: 'ID3', name: 'name 3' }];
}
```

### Multiple Select Mode
To enable multi select mode, run the following code:

```HTML
<ui-scroll-drop-down 
    multiple
    ng-model="currentEntity"
    data="getData(criteria)">
</ui-scroll-drop-down>
``` 

Model value must be an array type if you use `multiple`:

```JS
$scope.currentEntity = ['ID2', 'ID3'];
```

### Filter Expression
If set, this function is called after each new page of data is fetched. This does not work with predefined array data function.

```HTML
<ui-scroll-drop-down 
    ng-model="currentEntity"
    data="serverSearch(criteria)"
    filter="entitiesToHideFnc(items)">
</ui-scroll-drop-down>
``` 
```JS
$scope.entitiesToHideFnc = function (items) {
    return _.filter(items, function (x) {
        console.log(x.name);
        if (x.name === 'name2') return false;
        return true;
    });
}
```

### Events
The directive provides on-select and on-delete events:

```HTML
<ui-scroll-drop-down 
    ng-model="currentEntity"
    data="getData(criteria)"
    on-select="onSelect(item, model)"
    on-remove="onRemove(item, model)">
</ui-scroll-drop-down>
``` 
```JS
$scope.onSelect = function (item, model) {
    console.log(item);
}

$scope.onRemove = function (item, model) {
    console.log(item);
}
```
