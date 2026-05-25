# Access Dynamic Properties in Code

The `DynamicPropertyAccessor` class provides a simplified way to work with dynamic properties in entities that implement the `IHasDynamicProperties` interface.
It allows developers to read and modify dynamic property values directly through dynamic syntax, without manually managing the `DynamicProperties` collection.

**Example: accessing a short text dynamic property `Age`**

```csharp title="Program.cs"
var entity = new EntityWithDynamicProperties(); // Class that inherits from IHasDynamicProperties

dynamic properties = new DynamicPropertyAccessor(entity);
properties.Age = "New Value"; // Set value of the dynamic property named "Age"
string age = properties.Age;  // Get value of the dynamic property named "Age"
```

![Read more](media/readmore.png){: width="20"} [Managing dynamic properties via Platform](/platform/user-guide/dynamic-properties/managing-dynamic-properties/)

## Read values with a default fallback

When you only need to read a value safely and fall back to a default if the property is missing, use the `GetDynamicPropertyValue<T>()` extension method available on any entity that implements `IHasDynamicProperties`. The method returns the typed value or the supplied default.

```csharp title="Program.cs"
// Get a string property with a default value.
string customField = entity.GetDynamicPropertyValue("CustomField", "default");

// Get an integer property.
int count = entity.GetDynamicPropertyValue("Count", 0);
```

## Supported value types

`DynamicPropertyAccessor` maps each Virto Commerce dynamic property value type to the corresponding .NET type:

| Value type | .NET type |
| --- | --- |
| ShortText | `string` |
| LongText | `string` |
| Integer | `int` |
| Decimal | `decimal` |
| Boolean | `bool` |
| DateTime | `DateTime` |
| Html | `string` |
| Image | `string` |

## Add DynamicPropertyAccessor to entity

Expose `DynamicPropertyAccessor` on your entity by implementing `IHasDynamicProperties` and adding a lazily initialized accessor property:

```csharp title="EntityWithDynamicProperties.cs"
public class EntityWithDynamicProperties : AuditableEntity, IHasDynamicProperties
{
    public string ObjectType => typeof(EntityWithDynamicProperties).FullName;
    public ICollection<DynamicObjectProperty> DynamicProperties { get; set; } = [];
    private DynamicPropertyAccessor _dynamicPropertyAccessor;
    public DynamicPropertyAccessor DynamicPropertyAccessor
    {
        get
        {
            _dynamicPropertyAccessor ??= new DynamicPropertyAccessor(this);
            return _dynamicPropertyAccessor;
        }
        set
        {
            _dynamicPropertyAccessor = value;
            _dynamicPropertyAccessor.ConnectEntity(this);
        }
    }
}
```

## Use DynamicPropertyAccessor via REST API

`DynamicPropertyAccessor` is also available in the Platform REST API. It allows reading and updating dynamic property values in a simplified, structured way - without manually handling the `DynamicProperties` array. You can retrieve, modify, or patch dynamic properties directly through the `dynamicPropertyAccessor` object in API requests and responses.

### GET dynamic properties

A GET response returns the values directly under the `dynamicPropertyAccessor` object, with each property name as a key:

```json
{
  "dynamicPropertyAccessor": {
    "DateTimeFieldSingleValue": "2025-09-25T22:00:00Z",
    "DecimalFieldMultiValue": [678, 1011, 123, 345],
    "DecimalFieldSingleValue": 345.45,
    "HtmlFieldSingleValue": "<b>Hi</b>",
    "ImageFieldSingleValue": null,
    "IntegerFieldMiltiValue": [456, 123],
    "IntegerFieldSingleValue": 123,
    "LongTextFieldSingleValue": "Long text value...",
    "ShortTextFieldSingleValue": "Short text value",
    "ShortTextFieldSingleValue_Localized": {
      "values": {
        "en-US": null,
        "de-DE": null,
        "fr-FR": null,
        "ru-RU": null,
        "it-IT": null,
        "pl": null,
        "ja-JP": null
      }
    }
  },
  "createdBy": "unknown",
  "modifiedBy": "admin",
  "id": "cb0a5340-f9fb-4f49-bd62-9d03518868ff"
}
```

### Update dynamic properties

To replace one or more property values, send a PUT request and include the new values inside the `dynamicPropertyAccessor` object.

!!! note
    Don’t forget to force usage of `dynamicPropertyAccessor` by setting `useDynamicPropertyAccessor` to `true`.


<div class="grid cards" markdown>

-   __Request__

    ```http
    PUT /api/members
    ```

-   __Body__


    ```json
    {
    "useDynamicPropertyAccessor": true,
    "dynamicPropertyAccessor": {
        "Age": "New Value"
    }
    }
    ```

</div>


### Patch dynamic properties

To change a single property without resubmitting the full object, use a JSON Patch request:

```json
[
  {
    "op": "replace",
    "path": "/dynamicPropertyAccessor/HtmlFieldSingleValue",
    "value": "<b>Hello World</b>"
  }
]
```


## Use with extended entities

`DynamicPropertyAccessor` can also be used to transform dynamic properties into system-level properties, allowing developers to expose them as standard entity properties without extending the database.

```csharp title="EntityWithDynamicProperties.cs"
public string[] Tags
{
    get
    {
        dynamic dynamicPropertyAccessor = DynamicPropertyAccessor;
        return dynamicPropertyAccessor.Tags;
    }
    set
    {
        dynamic dynamicPropertyAccessor = DynamicPropertyAccessor;
        dynamicPropertyAccessor.Tags = value;
    }
}
```


## Request Dynamic Property Metadata

You can retrieve metadata for dynamic properties using the `DynamicPropertyMetadata` static class or inspect value type capabilities via `DynamicPropertyValueTypeCapability`.

### Get dynamic property metadata

Use `DynamicPropertyMetadata` to fetch the list of properties registered for a given entity type, either by generic argument or by object type name:

```csharp title="DynamicPropertyMetadata.cs"
public static class DynamicPropertyMetadata
{
    public static Task<IList<DynamicProperty>> GetProperties<TEntity>();
    public static async Task<IList<DynamicProperty>> GetProperties(string objectType);
}
```

### Get value type capabilities

Inspect whether a value type supports arrays, dictionaries, and localization through `DynamicPropertyValueTypeCapability`:

```csharp title="DynamicPropertyValueTypeCapability.cs"
public class DynamicPropertyValueTypeCapability
{
    public DynamicPropertyValueType ValueType { get; set; }
    public bool SupportArray { get; set; }
    public bool SupportDictionary { get; set; }
    public bool SupportLocalization { get; set; }
}
```

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../SEO/overview">← SEO module overview </a>
    <a href="../../Notifications/overview">Managing notifications  →</a>
</div>