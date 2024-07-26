# DynamicPropertyType ==~object~==

This type represents a value assigned to a dynamic property. 

## Fields

| Field                                                                                 | Description                                                  |
|---------------------------------------------------------------------------------------|--------------------------------------------------------------|
| `id`  ==String==                                                                      | The Id of the dynamic property.                              |
| `name`  ==String==                                                                    | The name or title of the dynamic property.                   |
| `objectType`  ==String==                                                              | The type of object to which the dynamic property belongs.    |
| `label`  ==String==                                                                   | The label or display name of the dynamic property.           |
| `displayOrder`  ==Int==                                                               | The order in which the dynamic property is displayed.        |
| `valueType`  ==String==                                                               | The type of value stored in the dynamic property.            |
| `isArray`  ==Boolean==                                                                | Indicates whether the dynamic property accepts an array of values. |
| `isDictionary`  ==Boolean==                                                           | Indicates whether the dynamic property is a dictionary.       |
| `isMultilingual`  ==Boolean==                                                         | Indicates whether the dynamic property supports multilingual values. |
| `isRequired`  ==Boolean==                                                             | Indicates whether the dynamic property is required.      |
| `dictionaryItems(...)` [ ==DictionaryItemConnection== ](dictionary-item-connection.md)| Retrieves the dictionary items associated with the dynamic property. |
