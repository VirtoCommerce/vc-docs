# UpdateQuoteDynamicPropertiesCommandType  ==~object~==

This type is used to update the dynamic properties associated with a specific quote.

## Fields

| Field                                                                                            | Description                                                         |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| `quoteId` ==String!==                                                                            | The Id of the quote for which dynamic properties are being updated. |
| `dynamicProperties` [ ==[InputDynamicPropertyValueType]!== ](../../Profile/Objects/InputDynamicPropertyValueType.md) | A list of dynamic properties to be assigned to the quote.           |

