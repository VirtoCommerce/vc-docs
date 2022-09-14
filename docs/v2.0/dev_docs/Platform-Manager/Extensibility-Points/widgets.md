## Introduction

A **widget** is a relatively simple and intuitive web UI [component](http://en.wikipedia.org/wiki/Software_component) within Virto Commerce Platform. It is basically a transient or auxiliary tile, which:

+ Occupies just a fraction of a blade
+ Provides useful information
+ Usually enables opening another blade with extra information and functions
+ Is reusable and can be added to as many blades (**widget containers**) as you want

A **widget container** is a placeholder control for **widgets**, which:

* Displays widgets in a rectangular area
* Accepts options like size, widget column and row count, etc.
* Allows the user to manage widget position within designated area

A **widget service** is a platform level engine for registering **widgets** and distributing them to the appropriate **widget containers**.

## Widget Container

You can implement widget containes as the **vaWidgetContainer** Angular.js directive. We use [angular-gridster](http://manifestwebdesign.github.io/angular-gridster/) under the hood, which means our containers support and accept angular-gridster options. 

```
<va-widget-container group="itemDetail" blade="blade" gridster-opts="{columns: 6, minRows: 4}"></va-widget-container>
```

|Parameter|Description|
|---------|-----------|
|group|Widget group ID. Only widgets from this group will be displayed. The value should be in line with the context of the container, e.g. `itemDetail`, and be unique among all widget containers.|
|blade|Reference to parent blade. Sent to each widget inside the container.|
|gridster-opts|Angular-gridster options (optional value).|

## Registering Widget

You can register widgets through the Platform-level factory, which means **any module can register new widgets to any widget container**:

1. Reference `platformWebApp.widgetService` (as `widgetService`) in your module's `run` method.
2. Create widget option definition and call `widgetService.registerWidget`.

```
var variationWidget = {
  controller: 'virtoCommerce.catalogModule.itemVariationWidgetController',
  size: [2, 1],
  isVisible: function (blade) { return !blade.isNew && blade.controller === 'virtoCommerce.catalogModule.itemDetailController'; },
  template: 'Modules/$(VirtoCommerce.Catalog)/Scripts/widgets/itemVariationWidget.tpl.html'
};
widgetService.registerWidget(variationWidget, 'itemDetail');
```

`WidgetService.registerWidget` parameters:

|Parameter|Description|
|---------|-----------|
|widget|Widget options|
|containerName|Widget group ID that will be added to the widget container having the same group.|

Widget options:

|Option|Description|
|------|-----------|
|controller|An Angular.js controller for the widget. Instantiated only on widget rendering, which means parent blade is accessible in the *$scope.blade* variable.|
|size|Widget dimensions: [number of columns, number of rows]. An optional parameter with the default value at [1,1].|
|isVisible|Toggles widget visibility (a widget get invisible if this option is set to *false*). Set to *true* by default.|
|template|Template URL for the widget. Check our [Style Guide](../style-guide) for details.|

## Widget Visibility and Permissions

Widget visibility is controlled by defining the `isVisible` method in widget registration options. There are at least two use cases when limiting visibility is required:

+ The widget is appropriate only in some scenarios, e.g., you need to hide order widget while creating a new item or hide inventory widget for a digital product.
+ Access to the widget is restricted by security permission, as in the sample piece of code below:

```
isVisible: function (blade) { return authService.checkPermission('pricing:query'); },
```
