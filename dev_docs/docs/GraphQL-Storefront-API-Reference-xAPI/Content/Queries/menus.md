# Menus

This query is used to retrieve a collection of menus based on the provided criteria. 

## Arguments

| Arguments                   | Description                                                                     |
|-----------------------------|---------------------------------------------------------------------------------|
| `storeId` {==String!==}     | The Id of the store for which to retrieve menus.                                |
| `cultureName` {==String==}  | A language to retrieve data in.                                                 |
| `keyword` {==String==}      | A keyword used to filter menus based on their content.                          |

## Possible returns

| Possible return                                          	| Description             	|
|---------------------------------------------------------	|--------------------------	|
| [`MenuLinkListType`](../Objects/MenuLinkListType.md)      |  A list of menu links.   	|


## Examples

=== "Query"

    ```json linenums="1"
    query {
      menus(
        storeId:"B2B-store"
        cultureName:"en-US"
      )
      {
        name
        outerId
        items{
          url
          title
          outerId
          priority
          associatedObjectId
          associatedObjectName
          associatedObjectType
        }
      }
    }
    ```

=== "Return"

    ```json linenums="1"
    {
      "data": {
        "menus": [
          {
            "name": "catalog-menu",
            "outerId": null,
            "items": [
              {
                "url": "/bolts",
                "title": "Bolts",
                "outerId": null,
                "priority": 20,
                "associatedObjectId": null,
                "associatedObjectName": null,
                "associatedObjectType": null
              },
              {
                "url": "/printers",
                "title": "Printers",
                "outerId": null,
                "priority": 10,
                "associatedObjectId": null,
                "associatedObjectName": null,
                "associatedObjectType": null
              }
            ]
          },
          {
            "name": "Bolts",
            "outerId": null,
            "items": [
              {
                "url": "/bolts/freight-car-bolts",
                "title": "Freight car bolts",
                "outerId": null,
                "priority": 30,
                "associatedObjectId": null,
                "associatedObjectName": null,
                "associatedObjectType": null
              },
              {
                "url": "/bolts/carriage-bolts",
                "title": "Carriage bolts",
                "outerId": null,
                "priority": 20,
                "associatedObjectId": null,
                "associatedObjectName": null,
                "associatedObjectType": null
              },
              {
                "url": "/bolts/eyebolts",
                "title": "Eyebolts",
                "outerId": null,
                "priority": 10,
                "associatedObjectId": null,
                "associatedObjectName": null,
                "associatedObjectType": null
              },
              {
                "url": "/bolts/flange-bolts",
                "title": "Flange Bolts",
                "outerId": null,
                "priority": 0,
                "associatedObjectId": null,
                "associatedObjectName": null,
                "associatedObjectType": null
              }
            ]
          },
        ]
      }
    }   
    ```
