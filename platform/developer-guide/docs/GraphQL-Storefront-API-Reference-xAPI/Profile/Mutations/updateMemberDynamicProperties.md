# updateMemberDynamicProperties ==~mutation~==

This mutation updates the member's dynamic properties.

## Arguments

The `InputUpdateMemberDynamicPropertiesType!` represents the input for updating the dynamic properties of a member.

| Field                                                                                                  | Description                                                                                       |
|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| `memberId`  ==String!==                                                                                | The Id of the member for which the dynamic properties are being updated.  |
| `dynamicProperties` [ ==InputDynamicPropertyValueType== ](../Objects/InputDynamicPropertyValueType.md) | An array of input dynamic property values containing the updated values for the member's dynamic properties. |

## Possible returns

| Possible return                                          	             | Description                                	|
|------------------------------------------------------------------------|---------------------------------------------	|
| [`MemberType`](../Objects/MemberType.md)                               | A member entity                          	|


=== "Mutation"
    ```json linenums="1"
    mutation updateMemberDynamicProperties($command: InputUpdateMemberDynamicPropertiesType!) {
      updateMemberDynamicProperties(command: $command) {
        name
        dynamicProperties {
          name
          value
          valueType
          dictionaryItem {
            label
            name 
            id
          }
        }
      }
    }
    ```

=== "Variables"
    ```json linenums="1"
    {
    "command": {
      "memberId": "820c58c5-b518-454b-aefd-2fc4616bd25e",
      "dynamicProperties": [
        {
          "name": "Sex",
          "value": "d58bedc559c6420fbde35666adae3251"
        },
        {
          "name": "Multilanguage",
          "cultureName":"fr-FR",
          "value": "fr-value"
        },
        {
          "name": "occupation",
          "value": "578fadeb1d2a40b3b08b1daf8db09463"
        },
        {
          "name": "occupation",
          "value": "6fba64f496a24317b476b8101fddb57b"
        },
        {
          "name": "Default shipping address",
          "value": "aDefault"
        },
        {
          "name": "Married",
          "value": "true"
        }
        ]
      }
    }
    ```
