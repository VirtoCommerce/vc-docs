# evaluateDynamicContent ==~query~==

This query allows you to evaluate dynamic content.

## Arguments

| Argument                   	| Description              	                                 |
|----------------------------	|----------------------------------------------------------	 |
| `storeId`  ==String==      	| The Id of the store.     	                                 |
| `placeName`  ==String==     | The name of the place where the content is evaluated.      |
| `categoryId`  ==String==    | The Id of the category to which the content belongs.       |
| `productId`  ==String==     | The Id of the product for which the content is evaluated.  |
| `cultureName`  ==String==  	| A language to retrieve data in.  	                         |
| `toDate`  ==DateTime==      | The date up to which the content is evaluated.             |
| `tags`  ==[String]==        | An array of tags associated with the dynamic content.      |
| `userGroups`  ==[String]==  | An array of user groups used to filter the content.        |

## Possible returns

| Possible return             	                                                          | Description                                          	|
|---------------------------------------------------------------------------------------	|-----------------------------------------------------	|
| [`EvaluateDynamicContentResultType`](../objects/EvaluateDynamicContentResultType.md)    | The result type for the evaluation of dynamic content.|

## Example

<div class="grid" markdown>

```json title="Query"
{
  evaluateDynamicContent(
    storeId: "B2B-store"
    placeName: "MainSlider"
    tags: ["Main"]
    userGroups: ["Customers"]
    productId: "8b7b07c165924a879392f4f51a6f7ce0"
  ) {
    items {
      id
      name
      contentType
      dynamicProperties {
        name
        value
      }
    }
    totalCount
  }
}
```

```json title="Return"
{
  "data": {
    "evaluateDynamicContent": {
      "items": [
        {
          "id": "1165b9ab-205f-488f-a9c7-64187bb85702",
          "name": "B2B slider",
          "contentType": "slider",
          "dynamicProperties": [
            {
              "name": "Content type",
              "value": "slider"            }
          ]
        }
      ],
      "totalCount": 1    }
  }
}
```

</div>