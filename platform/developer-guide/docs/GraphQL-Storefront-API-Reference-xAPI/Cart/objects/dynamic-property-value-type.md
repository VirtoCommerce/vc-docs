# DynamicPropertyValueType ==~object~==

This type represents a value assigned to a dynamic property. 

## Fields

| Field                                                                   | Description                                                                        |
|-------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| `name`  ==String==                                                      | The name or title of the dynamic property value.                                   |
| `valueType`  ==String==                                                 | The type of value stored in the dynamic property.                                  |
| `value`  ==DynamicPropertyValue==                                       | The actual value of the dynamic property.                                          |
| `dynamicPropertyValueType` ==DynamicPropertyValueTypes!==               | The format/category of the value (e.g., **ShortText**, **Integer**, **Boolean**, **DateTime**, etc.) |
| `dictionaryItem` [ ==DictionaryItemType== ](dictionary-item-type.md)    | The dictionary item associated with the dynamic property value, if applicable.     |
| `dynamicProperty` [ ==DynamicPropertyType== ](dynamic-property-type.md) | The dynamic property definition to which this value belongs.                       |
