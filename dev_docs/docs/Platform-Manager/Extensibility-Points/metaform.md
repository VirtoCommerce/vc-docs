## Introduction

Most Virto Commerce Platform's blades contain lists or data entry forms. Typically, the data entry form is made of static HTML code with Angular.js bindings. 

This strategy comes with the following drawbacks:

+ You cannot add any new UI elements without changing the source code.
+ You cannot update the existing UI without changing the source code.
+ Most content is produced through copying and pasting HTML code, which may lead to maintenance problems in the future, as data entry forms may potentially lose their common *look and feel*.

In order to eliminate the issues above, we developed a new Angular.js component called *metaform*:

+ **Metaform** is a placeholder (container) control that renders UI content based on the provided metadata.
+ **Meta-field** is a JavaScript object defining metadata for a single logical element inside the **metaform** being rendered.

## Using Metaform

Metaform is implemented as `vaMetaform` Angular.js directive and has the following features:

+ Renders UI elements in a rectangular area and typically should be placed inside a form.
+ Has customizable column count. The rendering runs left to right and top to bottom.
+ Occupies all available width and has auto height.
+ Supports simple input types and custom template elements.

```
<form>
  ...
  <va-metaform registered-inputs="blade.metaFields" blade="blade" column-count="2"></va-metaform>
  ...
</form>
```

|Parameter|Description|
|---------|-----------|
|registered-inputs|Reference to metadata (meta-fields)|
|blade|Reference to parent blade|
|column-count|Number of columns to arrange the rendered elements (optional)|

## Metaform Sample Code
You can view and download our Metaform sample code [here](https://github.com/VirtoCommerce/vc-samples/blob/master/MemberExtensionSampleModule/Scripts/extMembers.js#L14).

## Registering meta-fields

Here is how you can run meta-field registration directly in a blade:

```
blade.metaFields = [
{
  name: 'isApproved',
  title: "Is approved",
  valueType: "Boolean",
  isVisibleFn: function (blade) {
    return !blade.isNew;
  }
},
{
  name: 'status',
  templateUrl: 'statusSelector.html'
},
{
  name: 'startDate',
  isReadOnly: true,
  title: "Data created",
  valueType: "DateTime"
},
{
  name: 'customerId',
  title: "orders.blades.customerOrder-detail.labels.customer",
  templateUrl: 'customerSelector.html'
}];
```

Meta-field registration can also be done using the Platform-level factory. This way, **any module can access and change** the fields displayed inside the metaform:

1. Reference `platformWebApp.metaFormsService` (as `metaFormsService`) in your module's **run** method.
2. Create meta-field definitions and register them using the `metaFormsService.registerMetaFields` method.

```
metaFormsService.registerMetaFields("accountDetails",
                [
                    {
                        name: "isAdministrator",
                        title: "Is admin",
                        valueType: "Boolean"
                    }
                ]);
```

## Meta-field Data Structure

A meta-field has the following structure:

|Parameter|Description|
|---------|-----------|
|name|Property name to bind to. Under the hood, it is bound to `blade.currentEntity.<<name>>`.|
|title|Label value, which can be simple text or a key to localized resource.|
|valueType|Type of auto generated input control. Supported values: ShortText, LongText, Integer, Decimal, DateTime, Boolean, SecureString, Url, Email, Html.|
|isRequired|*Required* property for auto generated input control. Set to *false* by default.|
|isReadOnly|Disables the value for changing auto generated input control. Set to *false* by default.|
|templateUrl|A URL for custom content template. If specified, this template is rendered instead of the auto-generated content.|
|isVisibleFn|Function to control meta-field visibility. The meta-field gets rendered only if this function returns *true* or is undefined.|

