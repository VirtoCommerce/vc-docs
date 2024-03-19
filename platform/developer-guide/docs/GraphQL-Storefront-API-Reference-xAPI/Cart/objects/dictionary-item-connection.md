# DictionaryItemConnection ==~object~==

The `DictionaryItemConnection` provides a standardized way of fetching and navigating through a large collection of dictionary items. 

## Fields

| Field                                                                 | Description                                                                       |
|-----------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| `name`  ==String==                                                    | The name or title of the dynamic property value.                                  |
| `valueType`  ==String==                                               | The type of value stored in the dynamic property.                                 |
| `value` [ ==DynamicPropertyValue== ](dynamic-property-value-type.md)  | The actual value of the dynamic property.                                         |
| `dictionaryItem` [ ==DictionaryItemType== ](dictionary-item-type.md)  | The dictionary item associated with the dynamic property value, if applicable.    |
| `dynamicProperty` [ ==DynamicPropertyType== ](dynamic-property-type.md)| The dynamic property definition to which this value belongs.                     |
